from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from etl.database_conn.conn import get_engine

from models import registry

from models.base import Base


# =========================================================
# INITIALIZE DATABASE TABLES
# =========================================================

def initialize_database():

    engine = get_engine()

    print("\nRegistered Tables:\n")

    for table_name, table in Base.metadata.tables.items():

        print(
            f"{table.schema}.{table.name}"
        )

    print("\nCreating missing tables...\n")

    Base.metadata.create_all(engine)

    print(
        f"\nValidated "
        f"{len(Base.metadata.tables)} tables."
    )


# =========================================================
# DAG
# =========================================================

with DAG(
    dag_id="initialize_database",
    start_date=datetime(2026, 5, 28),
    schedule=None,
    catchup=False,
    tags=["database", "initialization"],
) as dag:

    initialize_database_task = PythonOperator(
        task_id="initialize_database",
        python_callable=initialize_database,
    )