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
    SILVER_DIR,
    BRONZE_TO_SILVER_MAPPINGS_DIR
)

from models.registry import get_model


# =========================================================
# LOAD MAPPING
# =========================================================
def load_mapping(dataset: str) -> pd.DataFrame:
    
    mapping_path = (
        BRONZE_TO_SILVER_MAPPINGS_DIR
        / f"{dataset.lower()}.xlsx"
    )

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
# LOAD BRONZE DATA
# =========================================================
def load_bronze_dataset(
    dataset: str
) -> pd.DataFrame:

    dataset_path = (
        Path(BRONZE_DIR)
        / dataset
    )

    parquet_files = list(
        dataset_path.glob("*.parquet")
    )

    if not parquet_files:
        raise FileNotFoundError(
            f"No parquet files found for {dataset}"
        )

    frames = [
        pd.read_parquet(file)
        for file in parquet_files
    ]

    return pd.concat(
        frames,
        ignore_index=True
    )


# =========================================================
# PYTHON TRANSFORM
# =========================================================
def apply_python_transform(
    source: pd.Series,
    transform: str,
    df: pd.DataFrame
) -> pd.Series:

    return eval(
        transform,
        {"pd": pd},
        {
            "source": source,
            "df": df
        }
    )


# =========================================================
# LOOKUP
# =========================================================
def perform_lookup(
    source_series: pd.Series,
    lookup_table: str
) -> pd.Series:

    """
    Placeholder.

    Future:
        Load lookup table from
        SQLAlchemy reference tables.
    """

    return source_series


# =========================================================
# SURROGATE KEY
# =========================================================
def generate_surrogate_key(
    df: pd.DataFrame,
    key_name: str
) -> pd.DataFrame:

    df.insert(
        0,
        key_name,
        range(1, len(df) + 1)
    )

    return df


# =========================================================
# VALIDATE MODEL COLUMNS
# =========================================================
def validate_columns_exist(
    df: pd.DataFrame,
    model
) -> None:

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
# VALIDATE PRIMARY KEYS
# =========================================================
def validate_primary_keys(
    df: pd.DataFrame,
    model
) -> None:

    primary_keys = [
        column.name
        for column
        in model.__table__.primary_key.columns
    ]

    for primary_key in primary_keys:

        if primary_key not in df.columns:

            raise ValueError(
                f"Primary key missing: "
                f"{primary_key}"
            )


# =========================================================
# VALIDATE NULLABLE RULES
# =========================================================
def validate_nullable_rules(
    df: pd.DataFrame,
    model
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
    model
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
def validate_target_model(
    df: pd.DataFrame,
    model
) -> None:

    validate_columns_exist(
        df,
        model
    )

    validate_primary_keys(
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
# WRITE SILVER
# =========================================================
def write_silver_table(
    dataset: str,
    df: pd.DataFrame
) -> Path:

    dataset_path = (
        Path(SILVER_DIR)
        / dataset
    )

    dataset_path.mkdir(
        parents=True,
        exist_ok=True
    )

    target_file = (
        dataset_path
        / f"{dataset}.parquet"
    )

    df.to_parquet(
        target_file,
        index=False
    )

    return target_file


# =========================================================
# BUILD SILVER TABLE
# =========================================================
def build_silver_table(
    dataset: str
) -> None:

    mapping_df = load_mapping(
        dataset
    )

    bronze_df = load_bronze_dataset(
        dataset
    )

    target_df = pd.DataFrame()

    for _, mapping in mapping_df.iterrows():

        source_field = mapping["source_field"]
        target_field = mapping["target_field"]

        source = bronze_df[source_field]

        if pd.notna(
            mapping["lookup_table"]
        ):

            target_df[target_field] = (
                perform_lookup(
                    source,
                    mapping["lookup_table"]
                )
            )

        elif pd.notna(
            mapping["python_transform"]
        ):

            target_df[target_field] = (
                apply_python_transform(
                    source,
                    mapping["python_transform"],
                    bronze_df
                )
            )

        else:

            target_df[target_field] = source

    # -----------------------------------------
    # Load target model
    # -----------------------------------------

    target_schema = (
        mapping_df.iloc[0]
        ["target_schema"]
    )

    target_table = (
        mapping_df.iloc[0]
        ["target_table"]
    )

    model = get_model(
        target_schema,
        target_table
    )

    # -----------------------------------------
    # Generate surrogate key
    # -----------------------------------------

    primary_keys = [
        column.name
        for column
        in model.__table__.primary_key.columns
    ]

    if len(primary_keys) == 1:

        primary_key = primary_keys[0]

        if primary_key not in target_df.columns:

            target_df = (
                generate_surrogate_key(
                    target_df,
                    primary_key
                )
            )

    # -----------------------------------------
    # Validate against model
    # -----------------------------------------

    validate_target_model(
        target_df,
        model
    )

    # -----------------------------------------
    # Write Silver
    # -----------------------------------------

    write_silver_table(
        dataset,
        target_df
    )