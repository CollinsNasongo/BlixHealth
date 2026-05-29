from urllib.parse import quote_plus

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine

from etl.setup.settings import (
    MSSQL_HOST,
    MSSQL_PORT,
    MSSQL_DATABASE,
    MSSQL_USER,
    MSSQL_PASSWORD,
    MSSQL_DRIVER,
)


def get_engine() -> Engine:

    password = quote_plus(MSSQL_PASSWORD)

    conn_string = (
        f"mssql+pyodbc://{MSSQL_USER}:{password}"
        f"@{MSSQL_HOST}:{MSSQL_PORT}"
        f"/{MSSQL_DATABASE}"
        f"?driver={MSSQL_DRIVER.replace(' ', '+')}"
        f"&TrustServerCertificate=yes"
    )

    return create_engine(
        conn_string,
        future=True,
        fast_executemany=True,
    )