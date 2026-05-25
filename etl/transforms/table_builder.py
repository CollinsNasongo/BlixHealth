from pathlib import Path

import pandas as pd

from sqlalchemy import (
    Integer,
    String,
    Float,
    Boolean,
    Date,
    DateTime,
)

from etl.config.paths import (
    BRONZE_DIR,
    BRONZE_TO_SILVER_MAPPINGS_DIR
)

from etl.transforms.transforms_registry import (
    TRANSFORM_REGISTRY, SYSTEM_TRANSFORMS
)

from models.registry import get_model

from models.base import Base
from sqlalchemy.engine import Engine

# =========================================================
# LOAD MAPPING
# =========================================================
def load_mapping(dataset: str) -> pd.DataFrame:
    
    mapping_path = (BRONZE_TO_SILVER_MAPPINGS_DIR / f"{dataset.lower()}.xlsx")

    if not mapping_path.exists():

        available_files = sorted(
            p.name
            for p in BRONZE_TO_SILVER_MAPPINGS_DIR.glob("*.xlsx")
        )

        raise FileNotFoundError(
            f"Mapping for dataset '{dataset}' was not found.\n"
            f"Expected file: {mapping_path.name}\n"
            f"Available files: {available_files}"
        )

    return pd.read_excel(mapping_path)

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
# VALIDATE MAPPING COLUMNS
# =========================================================
def validate_mapping_columns(mapping_df: pd.DataFrame, model: type[Base]) -> None:

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
# LOAD BRONZE DATA
# =========================================================
def get_source_files(dataset: str) -> list[Path]:

    dataset_path = (Path(BRONZE_DIR) / dataset)

    parquet_files_list = sorted(dataset_path.glob("*.parquet"))

    if not parquet_files_list: raise FileNotFoundError(f"No parquet files found for {dataset}")

    return parquet_files_list


# =========================================================
# VALIDATE MODEL COLUMNS
# =========================================================
def validate_columns_exist(df: pd.DataFrame, model: type[Base]) -> None:

    model_columns = {
        column.name
        for column in model.__table__.columns
    }

    missing_columns = [
        column
        for column in df.columns
        if column not in model_columns
    ]

    if missing_columns:

        raise ValueError(
            f"Columns not found in model "
            f"{model.__name__}: "
            f"{missing_columns}"
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
# APPLY TRANSFORMS
# =========================================================
def apply_transform(source: pd.Series, transforms: str) -> pd.Series:

    validate_transforms(
        transforms
    )

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


# =========================================================
# VALIDATE NULLABLE RULES
# =========================================================
def validate_nullable_rules(
    df: pd.DataFrame,
    model: type[Base]
) -> None:

    for column in model.__table__.columns:

        if (
            column.name in df.columns
            and not column.nullable
            and not column.primary_key
        ):

            if df[column.name].isna().any():

                raise ValueError(
                    f"Non-nullable column "
                    f"contains NULLs: "
                    f"{column.name}"
                )


# =========================================================
# VALIDATE DATATYPES
# =========================================================
def validate_datatypes(
    df: pd.DataFrame,
    model: type[Base]
) -> None:

    for column in model.__table__.columns:

        if column.name not in df.columns:
            continue

        series = df[column.name]

        if isinstance(column.type, Integer):

            if not (
                pd.api.types.is_integer_dtype(
                    series
                )
            ):
                raise TypeError(
                    f"{column.name} "
                    f"must be Integer"
                )

        elif isinstance(column.type, String):

            if not (
                pd.api.types.is_object_dtype(
                    series
                )
            ):
                raise TypeError(
                    f"{column.name} "
                    f"must be String"
                )

        elif isinstance(column.type, Float):

            if not (
                pd.api.types.is_float_dtype(
                    series
                )
                or
                pd.api.types.is_integer_dtype(
                    series
                )
            ):
                raise TypeError(
                    f"{column.name} "
                    f"must be Float"
                )

        elif isinstance(column.type, Boolean):

            if not (
                pd.api.types.is_bool_dtype(
                    series
                )
            ):
                raise TypeError(
                    f"{column.name} "
                    f"must be Boolean"
                )

        elif isinstance(
            column.type,
            (
                Date,
                DateTime,
            )
        ):

            if not (
                pd.api.types
                .is_datetime64_any_dtype(
                    series
                )
            ):
                raise TypeError(
                    f"{column.name} "
                    f"must be Date/DateTime"
                )


# =========================================================
# MODEL VALIDATION
# =========================================================
def validate_target_model(df: pd.DataFrame, model: type[Base]) -> None:

    validate_columns_exist(
        df,
        model
    )

    validate_nullable_rules(
        df,
        model
    )

    validate_datatypes(
        df,
        model
    )


# =========================================================
# WRITE TABLE
# =========================================================
def write_table(mapping_df: pd.DataFrame, df: pd.DataFrame, engine: Engine) -> None:
    
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

    model = get_model(
        database_name=target_database,
        schema_name=target_schema,
        table_name=target_table
    )

    validate_target_model(
    df=df,
    model=model)

    Base.metadata.create_all(
        bind=engine,
        tables=[model.__table__]
    )

    try:
        df.to_sql(
        name=target_table,
        schema=target_schema,
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )
        
    except Exception as e:
        raise RuntimeError(
            f"Failed to write to table "
            f"{target_database}.{target_schema}.{target_table}: "
            f"{str(e)}"
        ) from e