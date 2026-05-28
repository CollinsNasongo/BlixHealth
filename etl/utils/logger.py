from datetime import datetime, timezone

from sqlalchemy.orm import Session

from models.registry import get_model


# =========================================================
# LOGGING
# =========================================================

def log_dataset_run(
    session: Session,
    run_id: str,
    dataset: str,
    source_file: str,
    target_file: str,
    status: str,
    records_processed: int = 0,
    error_message: str | None = None,
) -> None:

    LogModel = get_model(
        "blix_healthcare_db",
        "audit",
        "data_move_log"
    )

    try:

        log_record = LogModel(
            run_id=run_id,
            dataset=dataset,
            source_file=source_file,
            target_file=target_file,
            status=status,
            records_processed=records_processed,
            error_message=error_message,
            run_timestamp=datetime.now(timezone.utc),
        )

        session.add(log_record)
        session.commit()

    except Exception as e:

        session.rollback()

        print(
            f"[LOGGER ERROR] "
            f"Failed to log pipeline run: {e}"
        )