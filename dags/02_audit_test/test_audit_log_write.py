from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import Session
from etl.setup.connect import get_engine
from etl.utils.logger import log_dataset_run


# =========================================================
# GLOBAL ENGINE
# =========================================================

engine = get_engine()


# =========================================================
# TEST AUDIT LOGGING
# =========================================================

def test_audit_log_write():

    run_id = str(uuid4())

    retry_events = [

        {
            "status": "FAILED",
            "records_processed": 0,
            "error_message": (
                "Connection timeout while reading source file."
            ),
        },

        {
            "status": "FAILED",
            "records_processed": 25,
            "error_message": (
                "Primary key violation during insert."
            ),
        },

        {
            "status": "SUCCESS",
            "records_processed": 100,
            "error_message": None,
        },
    ]

    for attempt, event in enumerate(retry_events, start=1):

        try:

            with Session(engine) as session:

                log_dataset_run(
                    session=session,
                    run_id=run_id,
                    dataset="member",
                    source_file="member.csv",
                    target_file="bronze.member",
                    status=event["status"],
                    records_processed=event["records_processed"],
                    error_message=event["error_message"],
                )

            print(
                f"[ATTEMPT {attempt}] "
                f"Logged successfully."
            )

        except Exception as e:

            print(
                f"[ATTEMPT {attempt}] "
                f"Failed to log: {e}"
            )

    print(f"Completed pipeline run: {run_id}")


# =========================================================
# DAG
# =========================================================

with DAG(
    dag_id="test_audit_log_write",
    start_date=datetime(2026, 5, 28),
    schedule=None,
    catchup=False,
    tags=["audit", "logging", "testing"],
) as dag:

    test_audit_log_write_task = PythonOperator(
        task_id="test_audit_log_write",
        python_callable=test_audit_log_write,
    )