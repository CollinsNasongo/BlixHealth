import csv
from pathlib import Path
from datetime import datetime, timezone

import pandas as pd

from etl.config.paths import LANDING_DIR, LOGS_DIR, BRONZE_DIR
from etl.utils.logger import log_dataset_run

LOG_PATH = Path(LOGS_DIR) / "dataset_processing_logs.csv"


def get_dataset_files(dataset: str) -> list[Path]:
    dataset_path = Path(LANDING_DIR) / dataset

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset folder not found: {dataset_path}")

    return list(dataset_path.glob("*.csv"))


def already_processed_check(dataset: str, source_file: str) -> bool:
    if not LOG_PATH.exists():
        return False

    with LOG_PATH.open(newline="") as f:
        for row in csv.DictReader(f):
            if (
                row["dataset"] == dataset
                and row["source_file"] == source_file
                and row["status"] == "SUCCESS"
            ):
                return True

    return False



def write_to_bronze( run_id: str, dataset: str, source_file: Path) -> Path:
    try:

        # Read source file
        df = pd.read_csv(source_file)

        # Add bronze metadata
        df["ingest_timestamp"] = (
            datetime.now(timezone.utc).isoformat()
        )

        # Create bronze dataset folder
        bronze_dataset_dir = (
            Path(BRONZE_DIR)
            / dataset
        )

        bronze_dataset_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        # Build bronze filename
        bronze_file = (
            bronze_dataset_dir
            / f"bronze_{source_file.name}"
        )

        # Write bronze file
        df.to_csv(
            bronze_file,
            index=False
        )

        # Log success
        log_dataset_run(
            run_id=run_id,
            dataset=dataset,
            source_file=source_file.name,
            status="SUCCESS",
            records_processed=len(df)
        )

        print(
            f"Written to bronze: "
            f"{bronze_file.name}"
        )

        return bronze_file

    except Exception as e:

        log_dataset_run(
            run_id=run_id,
            dataset=dataset,
            source_file=source_file.name,
            status="FAILED",
            error_message=str(e)
        )

        raise