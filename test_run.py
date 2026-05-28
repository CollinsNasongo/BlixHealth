from uuid import uuid4

from sqlalchemy.orm import Session

from etl.database_conn.conn import get_engine
from etl.utils.logger import log_dataset_run


def main():

    try:

        engine = get_engine()

        run_id = str(uuid4())

        with Session(engine) as session:

            # =====================================================
            # RETRY 1 - FAILURE
            # =====================================================

            log_dataset_run(
                session=session,
                run_id=run_id,
                dataset="member",
                source_file="member.csv",
                target_file="bronze.member",
                status="FAILED",
                records_processed=0,
                error_message="Connection timeout while reading source file.",
            )

            print("Retry 1 logged.")

            # =====================================================
            # RETRY 2 - FAILURE
            # =====================================================

            log_dataset_run(
                session=session,
                run_id=run_id,
                dataset="member",
                source_file="member.csv",
                target_file="bronze.member",
                status="FAILED",
                records_processed=25,
                error_message="Primary key violation during insert.",
            )

            print("Retry 2 logged.")

            # =====================================================
            # RETRY 3 - SUCCESS
            # =====================================================

            log_dataset_run(
                session=session,
                run_id=run_id,
                dataset="member",
                source_file="member.csv",
                target_file="bronze.member",
                status="SUCCESS",
                records_processed=100,
                error_message=None,
            )

            print("Final retry logged successfully.")

        print(f"Pipeline run completed: {run_id}")

    except Exception as e:

        print(
            f"[TEST LOGGER ERROR] "
            f"Failed to write log: {e}"
        )


if __name__ == "__main__":
    main()