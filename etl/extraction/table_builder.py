from pathlib import Path
import pandas as pd

from etl.setup.paths import (
    LANDING_DIR,
    SOURCE_TO_BRONZE_MAPPINGS_DIR,
    BRONZE_TO_SILVER_MAPPINGS_DIR,
    SILVER_TO_GOLD_MAPPINGS_DIR
)

from etl.transforms.transforms_registry import (
    TRANSFORM_REGISTRY, 
    SYSTEM_TRANSFORMS
)

from models.registry import get_model
from models.base import Base
from sqlalchemy.engine import Engine


# =========================================================
# VALIDATE MAPPING STRUCTURE
# =========================================================
def validate_mapping_structure(mapping_df: pd.DataFrame) -> None:

    required_columns = {
        "source_database",
        "source_schema",
        "source_table",
        "source_field",
        "target_database",
        "target_schema",
        "target_table",
        "target_field",
        "sql_transform",
        "python_transform",
        "lookup_table",
    }

    missing_columns = sorted(
        required_columns - set(mapping_df.columns)
    )

    if missing_columns:
        raise ValueError(
            f"Mapping is missing required columns: "
            f"{missing_columns}"
        )
    
# =========================================================
# VALIDATE TARGET OBJECT
# =========================================================
def validate_target_object(mapping_df: pd.DataFrame) -> None:

    if mapping_df["target_database"].nunique() != 1:
        raise ValueError(
            "Mapping contains multiple target databases."
        )

    if mapping_df["target_schema"].nunique() != 1:
        raise ValueError(
            "Mapping contains multiple target schemas."
        )

    if mapping_df["target_table"].nunique() != 1:
        raise ValueError(
            "Mapping contains multiple target tables."
        )

# =========================================================
# VALIDATE TRANSFORMS
# =========================================================
def validate_transforms(transforms: str) -> None:

    if pd.isna(transforms):
        return

    parsed_transforms = [
        transform.strip().lower()
        for transform in transforms.split("|")
        if transform.strip()
    ]

    if (
        "autoincrement" in parsed_transforms
        and len(parsed_transforms) > 1
    ):
        raise ValueError(
            "'autoincrement' cannot be combined "
            "with other transforms"
        )

# =========================================================
# LOAD MAPPING
# =========================================================
def load_mapping(mapping_type: str, dataset: str) -> pd.DataFrame:

    if mapping_type == "bronze_to_silver":
        mapping_dir = BRONZE_TO_SILVER_MAPPINGS_DIR
    elif mapping_type == "source_to_bronze":
        mapping_dir = SOURCE_TO_BRONZE_MAPPINGS_DIR
    elif mapping_type == "silver_to_gold":
        mapping_dir = SILVER_TO_GOLD_MAPPINGS_DIR
    else:
        raise ValueError(f"Unknown mapping type: {mapping_type}")
    
    mapping_file_path = (mapping_dir / f"{dataset.lower()}.xlsx")

    if not mapping_file_path.exists():

        available_files = sorted(
            p.name
            for p in mapping_dir.glob("*.xlsx")
        )

        raise FileNotFoundError(
            f"Mapping for dataset '{dataset}' was not found.\n"
            f"Expected file: {mapping_file_path.name}\n"
            f"Available files: {available_files}"
        )
    
    mapping_doc = pd.ExcelFile(mapping_file_path)
    mapping_df = mapping_doc.parse(mapping_doc.sheet_names[0])
    validate_mapping_structure(mapping_df)
    validate_target_object(mapping_df)
    mapping_df["python_transform"].apply(validate_transforms)

    return mapping_df


# =========================================================
# VALIDATE MAPPING COLUMNS
# =========================================================
def compare_mapping_with_model (mapping_df: pd.DataFrame, model: type[Base]) -> None:

    model_columns = {
        column.name
        for column in model.__table__.columns
    }

    target_columns = set(
        mapping_df["target_field"]
    )

    missing_columns = sorted(
        target_columns - model_columns
    )

    if missing_columns:
        raise ValueError(
            f"Target columns not found in model "
            f"{model.__name__}: {missing_columns}"
        )
    


# =========================================================
# LOAD BRONZE DATA
# =========================================================
def get_source_files(dataset: str) -> list[Path]:

    dataset_path = (Path(LANDING_DIR) / dataset)

    csv_files_list = sorted(dataset_path.glob("*.csv"))

    if not csv_files_list: raise FileNotFoundError(f"No CSV files found for {dataset}")

    return csv_files_list


# =========================================================
# VALIDATE MODEL COLUMNS
# =========================================================
def compare_data_with_model(source_df: pd.DataFrame, model: type[Base]) -> None:

    model_columns = {
        column.name
        for column in model.__table__.columns
    }

    missing_columns = [
        column
        for column in source_df.columns
        if column not in model_columns
    ]

    if missing_columns:

        raise ValueError(
            f"Columns not found in model "
            f"{model.__name__}: "
            f"{missing_columns}"
        )



# =========================================================
# APPLY TRANSFORMS
# =========================================================
def apply_transform(source: pd.Series, transforms: str) -> pd.Series:

    if pd.isna(transforms):
        return source

    result = source

    for transform in transforms.split("|"):

        transform = transform.strip().lower()

        if not transform:
            continue

        if transform in SYSTEM_TRANSFORMS:
            continue

        try:

            if ":" in transform:

                transform_name, *parameters = (
                    transform.split(":")
                )

                result = TRANSFORM_REGISTRY[
                    transform_name
                ](
                    result,
                    *map(int, parameters)
                )

            else:

                result = TRANSFORM_REGISTRY[
                    transform
                ](
                    result
                )

        except KeyError:
            raise ValueError(
                f"Unsupported transform '{transform}'"
            )

        except ValueError as e:
            raise ValueError(
                f"Invalid parameters for transform "
                f"'{transform}': {e}"
            ) from e

    return result

def apply_transforms(
    source_df: pd.DataFrame,
    mapping_df: pd.DataFrame,
) -> pd.DataFrame:

    transformed_df = pd.DataFrame(index=source_df.index)

    for _, row in mapping_df.iterrows():

        source_field = row["source_field"]
        target_field = row["target_field"]
        transforms = row["python_transform"]
        if pd.isna(source_field):
            if transforms in SYSTEM_TRANSFORMS:
                continue
            raise ValueError(
                f"Target field '{target_field}' has no source field "
                f"and is not a recognized system transform."
            )
        transformed_df[target_field] = apply_transform(
            source=source_df[source_field],
            transforms=transforms,
        )

    return transformed_df

# =========================================================
# WRITE TABLE
# =========================================================
def write_table(
    mapping_df: pd.DataFrame,
    df: pd.DataFrame,
    engine: Engine,
    write_mode: str = "append",
) -> None:

    target_database = (
        mapping_df["target_database"]
        .iloc[0]
        .lower()
    )

    target_schema = (
        mapping_df["target_schema"]
        .iloc[0]
        .lower()
    )

    target_table = (
        mapping_df["target_table"]
        .iloc[0]
        .lower()
    )

    write_mode = write_mode.lower()

    supported_modes = {
        "append",
        "overwrite",
        "update",
    }

    if write_mode not in supported_modes:

        raise ValueError(
            f"Unsupported write mode: "
            f"{write_mode}"
        )

    # =====================================================
    # HANDLE UPDATE MODE
    # =====================================================

    if write_mode == "update":

        raise NotImplementedError(
            "Update mode is not yet implemented."
        )

    # =====================================================
    # MAP WRITE MODE
    # =====================================================

    if_exists_mode = {
        "append": "append",
        "overwrite": "replace",
    }[write_mode]

    try:

        df.to_sql(
            name=target_table,
            schema=target_schema,
            con=engine,
            if_exists=if_exists_mode,
            index=False,
            chunksize=1000,
        )

    except Exception as e:

        raise RuntimeError(
            f"Failed to write to table "
            f"{target_database}."
            f"{target_schema}."
            f"{target_table}: "
            f"{str(e)}"
        ) from e