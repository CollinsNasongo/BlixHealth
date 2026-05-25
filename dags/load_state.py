from datetime import datetime
import logging
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from etl.config.conn import get_engine
from etl.transforms.table_builder import (
    load_mapping,
    validate_mapping_structure,
    validate_mapping_columns,
    validate_target_object,
    get_source_files,
    validate_columns_exist,
)

from models.registry import get_model

logger = logging.getLogger(__name__)
mapping_dataset = "state"
mapping_df = load_mapping(mapping_dataset)
source_tables = mapping_df["source_table"].dropna().unique()
model = get_model(
        database_name="blixhealth",
        schema_name="silver",
        table_name=mapping_dataset,
    )


def load_mapping_task() -> None:

    logger.info(
        "Loading mapping for '%s'.",
        mapping_dataset,
    )

    logger.info(
        "Loading target model for '%s'.",
        mapping_dataset,
    )

    logger.info(
        "Validating mapping structure."
    )
    validate_mapping_structure(mapping_df)

    logger.info(
        "Validating mapping columns."
    )
    validate_mapping_columns(mapping_df, model)

    logger.info(
        "Validating target object."
    )
    validate_target_object(mapping_df)

    logger.info(
        "Mapping validation successful."
    )



def get_source_files_task() -> None:
    
    if len(source_tables) == 0:
        raise ValueError(
            f"No source tables defined in mapping '{mapping_dataset}'."
        )

    files = []

    for source_table in source_tables:
        files.extend(
            get_source_files(source_table)
        )

    logger.info(
        "Found %s bronze file(s) across %s source table(s).",
        len(files),
        len(source_tables),
    )

    for file in files:
        logger.info(file)

def apply_transforms_task() -> None:
    validate_columns_exist()

with DAG(
    dag_id="load_state",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["load", "state"],
) as dag:
    load_mapping_task_op = PythonOperator(
        task_id="load_mapping",
        python_callable=load_mapping_task,
        )
    get_source_files_task_op = PythonOperator(
        task_id="get_source_files",
        python_callable=get_source_files_task,
        )

load_mapping_task_op >> get_source_files_task_op