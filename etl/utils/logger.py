from csv import DictWriter
from datetime import datetime, timezone
from pathlib import Path

from etl.config.paths import LOGS_DIR

# =========================================================
# LOGGING
# =========================================================
LOG_PATH = Path(LOGS_DIR) / "dataset_processing_logs.csv"
LOG_FIELDS = [
    "run_id", "dataset", "source_file", "status",
    "records_processed", "error_message", "run_timestamp",
]
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


def log_dataset_run(
    run_id: str,
    dataset: str,
    source_file: str,
    status: str,
    records_processed: int = 0,
    error_message: str | None = None,
) -> None:
    record = {
        "run_id": run_id,
        "dataset": dataset,
        "source_file": source_file,
        "status": status,
        "records_processed": records_processed,
        "error_message": error_message,
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
    }

    write_header = not LOG_PATH.exists()
    with LOG_PATH.open("a", newline="") as f:
        writer = DictWriter(f, fieldnames=LOG_FIELDS)
        if write_header:
            writer.writeheader()
        writer.writerow(record)