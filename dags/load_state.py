from datetime import datetime
import logging

import pandas as pd

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from etl.config.conn import get_engine

from etl.transforms.table_builder import (
    load_mapping,
    validate_mapping_structure,
    validate_mapping_columns,
    validate_target_object,
    get_source_files,
    apply_transform,
    write_table,
)

from models.registry import get_model


logger = logging.getLogger(__name__)

MAPPING_DATASET = "state"

mapping_df = load_mapping(MAPPING_DATASET)

source_tables = (
    mapping_df["source_table"]
    .dropna()
    .unique()
)

model = get_model(
    database_name="blixhealth",
    schema_name="silver",
    table_name=MAPPING_DATASET,
)


# =========================================================
# LOAD & VALIDATE MAPPING
# =========================================================
def load_mapping_task() -> None:

    logger.info(
        "Loading mapping for '%s'.",
        MAPPING_DATASET,
    )

    logger.info(
        "Validating mapping structure."
    )

    validate_mapping_structure(
        mapping_df
    )

    logger.info(
        "Validating mapping columns."
    )

    validate_mapping_columns(
        mapping_df,
        model,
    )

    logger.info(
        "Validating target object."
    )

    validate_target_object(
        mapping_df
    )

    logger.info(
        "Mapping validation successful."
    )


# =========================================================
# DISCOVER SOURCE FILES
# =========================================================
def get_source_files_task() -> None:

    if len(source_tables) == 0:

        raise ValueError(
            f"No source tables defined in mapping "
            f"'{MAPPING_DATASET}'."
        )

    source_files = []

    for source_table in source_tables:

        source_files.extend(
            get_source_files(
                source_table
            )
        )

    logger.info(
        "Found %s bronze file(s) across %s source table(s).",
        len(source_files),
        len(source_tables),
    )

    for file in source_files:

        logger.info(
            file
        )


# =========================================================
# BUILD BRONZE DATAFRAME
# =========================================================
def build_bronze_df() -> pd.DataFrame:

    dfs = []

    for source_table in source_tables:

        files = get_source_files(
            source_table
        )

        for file in files:

            dfs.append(
                pd.read_parquet(
                    file
                )
            )

    bronze_df = pd.concat(
        dfs,
        ignore_index=True,
    )

    logger.info(
        "Bronze dataframe shape: %s",
        bronze_df.shape,
    )

    logger.info(
        "Bronze columns: %s",
        bronze_df.columns.tolist(),
    )

    return bronze_df


# =========================================================
# APPLY TRANSFORMS
# =========================================================
def apply_transforms_task() -> None:

    bronze_df = build_bronze_df()

    silver_df = pd.DataFrame(
        index=bronze_df.index
    )

    for _, row in mapping_df.iterrows():

        source_field = row["source_field"]
        target_field = row["target_field"]
        transforms = row["python_transform"]

        logger.info(
            "Processing mapping: "
            "source=%s, target=%s, transforms=%s",
            source_field,
            target_field,
            transforms,
        )

        if (
            str(transforms)
            .strip()
            .lower()
            == "autoincrement"
        ):
            logger.info(
                "Skipping autoincrement column '%s'.",
                target_field,
            )
            continue

        silver_df[target_field] = apply_transform(
            source=bronze_df[source_field],
            transforms=transforms,
        )

    silver_df = silver_df.drop_duplicates(subset=["state_code", "state_name", "fips_code"]
)

    logger.info(
        "Created silver dataframe with columns: %s",
        silver_df.columns.tolist(),
    )

    logger.info(
        "Silver dataframe rows: %s",
        len(silver_df),
    )

    engine = get_engine()

    logger.info(
        "Writing %s rows to %s.%s",
        len(silver_df),
        mapping_df["target_schema"].iloc[0],
        mapping_df["target_table"].iloc[0],
    )

    write_table(
        mapping_df=mapping_df,
        df=silver_df,
        engine=engine,
    )

    logger.info(
        "Table load completed successfully."
    )
# =========================================================
# DAG
# =========================================================
with DAG(
    dag_id="load_state",
    start_date=datetime(
        2025,
        1,
        1,
    ),
    schedule=None,
    catchup=False,
    tags=[
        "load",
        "state",
    ],
) as dag:

    load_mapping_op = PythonOperator(
        task_id="load_mapping",
        python_callable=load_mapping_task,
    )

    get_source_files_op = PythonOperator(
        task_id="get_source_files",
        python_callable=get_source_files_task,
    )

    apply_transforms_op = PythonOperator(
        task_id="apply_transforms",
        python_callable=apply_transforms_task,
    )

    (
        load_mapping_op
        >> get_source_files_op
        >> apply_transforms_op
    )