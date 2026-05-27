from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from etl.config.conn import (
    get_engine,
    test_connection,
)


def test_mssql_connection():

    engine = get_engine()

    test_connection(engine)


with DAG(
    dag_id="test_database_connection",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["testing", "database", "mssql"],
) as dag:

    test_connection_task = PythonOperator(
        task_id="test_mssql_connection",
        python_callable=test_mssql_connection,
    )

test_connection_task