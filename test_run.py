from etl.database.settings import BLIX_HEALTH_CONFIG
from etl.database.connection import DatabaseConnector

db = DatabaseConnector.create(BLIX_HEALTH_CONFIG)

#print(db.build_connection_string())

try:
    with db.connect() as conn:
        print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")