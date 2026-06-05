from dotenv import load_dotenv
import os

from .database_config import (
    DatabaseConfig,
    DatabaseDialect,
)

load_dotenv()


BLIX_HEALTH_CONFIG = DatabaseConfig(
    dialect=DatabaseDialect.MSSQL,
    username=os.environ["MSSQL_USER"],
    password=os.environ["MSSQL_PASSWORD"],
    server=os.environ["MSSQL_HOST"],
    database_name=os.environ["MSSQL_DATABASE"],
    port=int(os.getenv("MSSQL_PORT", "1433")),
    parameters={
        "driver": "ODBC Driver 18 for SQL Server",
        "TrustServerCertificate": "yes",
    },
)