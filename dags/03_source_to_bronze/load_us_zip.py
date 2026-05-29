from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.utils.log.logging_mixin import LoggingMixin

import pandas as pd
from datetime import datetime
from pathlib import Path
from uuid import uuid4
from sqlalchemy.orm import Session

from etl.setup.connect import get_engine
from etl.utils.logger import log_dataset_run
from etl.extraction.table_builder import load_mapping, compare_mapping_with_model, get_source_files, compare_data_with_model, apply_transforms, write_table
from models.registry import get_model

logger = LoggingMixin().log
engine = get_engine()

dataset_name = "us_zip"
mapping_type = "source_to_bronze"

mapping_df = pd.DataFrame()
transformed_df = pd.DataFrame()
source_files = [Path()]

MappingModel = get_model(
        "blix_healthcare_db",
        "bronze",
        "us_zip"
    )


def load_mapping_task(dataset_name: str) -> pd.DataFrame:

    try:
        mapping_df = load_mapping(dataset=dataset_name, mapping_type=mapping_type)
        logger.info(
            f"Successfully loaded mapping "
            f"for dataset '{dataset_name}'"
        )

        return mapping_df

    except Exception as e:
        logger.exception(
            f"Error loading mapping "
            f"for dataset '{dataset_name}': {e}"
        )

        raise

def compare_mapping_with_model_task(mapping_df: pd.DataFrame) -> None:

    try:
        compare_mapping_with_model(mapping_df=mapping_df, model=MappingModel)
        logger.info(f"Mapping validation successful for dataset '{dataset_name}'")

    except Exception as e:
        logger.exception(f"Mapping validation failed for dataset '{dataset_name}': {e}")
        raise

def get_source_files_task() -> list[Path]:

    try:
        source_files = get_source_files(dataset=dataset_name)
        logger.info(f"Found {len(source_files)} source files for dataset '{dataset_name}'")

        return [str(f) for f in source_files]

    except Exception as e:
        logger.exception(f"Error getting source files for dataset '{dataset_name}': {e}")
        raise

from uuid import uuid4
from sqlalchemy.orm import Session

def load_data_task(
    source_files: list[str],
    mapping_df: pd.DataFrame,
) -> None:

    session = Session(engine)

    try:

        for source_file in source_files:

            run_id = str(uuid4())

            try:

                source_df = pd.read_csv(source_file)

                compare_data_with_model(
                    source_df=source_df,
                    model=MappingModel,
                )

                transformed_df = apply_transforms(
                    source_df=source_df,
                    mapping_df=mapping_df,
                )

                write_table(
                    mapping_df=mapping_df,
                    df=transformed_df,
                    engine=engine,
                    write_mode="overwrite",
                )

                log_dataset_run(
                    session=session,
                    run_id=run_id,
                    dataset=dataset_name,
                    source_file=source_file,
                    target_file="blix_healthcare_db.bronze.us_zip",
                    status="SUCCESS",
                    records_processed=len(transformed_df),
                )

            except Exception as e:

                log_dataset_run(
                    session=session,
                    run_id=run_id,
                    dataset=dataset_name,
                    source_file=source_file,
                    target_file="blix_healthcare_db.bronze.us_zip",
                    status="FAILED",
                    error_message=str(e),
                )

                raise

        logger.info(
            "Data loading completed successfully for dataset '%s'",
            dataset_name,
        )

    finally:
        session.close()
    


with DAG(
    dag_id="load_us_zip",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    load_mapping_op = PythonOperator(
    task_id="load_mapping",
    python_callable=load_mapping_task,
    op_kwargs={"dataset_name": dataset_name},
)
    compare_mapping_with_model_op = PythonOperator(
    task_id="compare_mapping_with_model",
    python_callable=compare_mapping_with_model_task,
    op_kwargs={"mapping_df": load_mapping_op.output},
)
    get_source_files_op = PythonOperator(
    task_id="get_source_files",
    python_callable=get_source_files_task,
)
    load_data_op = PythonOperator(
    task_id="load_data",
    python_callable=load_data_task,
    op_kwargs={"source_files": get_source_files_op.output, "mapping_df": load_mapping_op.output},
)

load_mapping_op >> compare_mapping_with_model_op >> get_source_files_op >> load_data_op