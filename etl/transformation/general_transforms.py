from datetime import datetime, timezone

import pandas as pd


def enrich_dataset_metadata(
    df: pd.DataFrame,
    run_id: str,
    dataset: str,
    source_file: str,
) -> pd.DataFrame:
    df = df.copy()
    df["run_id"] = run_id
    df["dataset"] = dataset
    df["source_file"] = source_file
    df["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()
    return df