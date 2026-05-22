from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from etl.config.conn import (
    get_engine,
    test_connection,
)


def test_bronze_connection():

    engine = get_engine("bronze")

    test_connection(engine)


def test_silver_connection():

    engine = get_engine("silver")

    test_connection(engine)


def test_gold_connection():

    engine = get_engine("gold")

    test_connection(engine)


with DAG(
    dag_id="test_database_connections",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["testing", "database"],
) as dag:

    bronze = PythonOperator(
        task_id="test_bronze_connection",
        python_callable=test_bronze_connection,
    )

    silver = PythonOperator(
        task_id="test_silver_connection",
        python_callable=test_silver_connection,
    )

    gold = PythonOperator(
        task_id="test_gold_connection",
        python_callable=test_gold_connection,
    )

    bronze >> silver >> gold