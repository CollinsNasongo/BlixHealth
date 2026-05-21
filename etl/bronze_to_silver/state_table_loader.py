from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from etl.config.paths import BRONZE_DIR, SILVER_DIR
from models.reference.state import State


def load_state() -> None:
    """
    Bronze -> Silver
    us_zips -> state
    """

    source_path = Path(BRONZE_DIR) / "us_zips.parquet"
    target_path = Path(SILVER_DIR) / "state.parquet"

    df = pd.read_parquet(source_path)

    state_df = pd.DataFrame()

    state_df["state_code"] = (
        df["state_id"]
        .astype(str)
        .str.upper()
    )

    state_df["state_name"] = df["state_name"]

    state_df["fips_code"] = (
        df["county_fips"]
        .astype(str)
        .str.strip()
        .str[:2]
    )

    state_df = state_df.drop_duplicates(
        subset=["state_code"]
    )

    # Optional validation against SQLAlchemy model
    expected_columns = {
        column.name
        for column in State.__table__.columns
        if column.name != "state_id"
    }

    missing_columns = expected_columns - set(state_df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    table = pa.Table.from_pandas(
        state_df,
        preserve_index=False,
    )

    pq.write_table(
        table,
        target_path,
    )