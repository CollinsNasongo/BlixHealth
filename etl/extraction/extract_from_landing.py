import uuid
from etl.utils.writter import write_to_bronze, get_dataset_files, already_processed_check

def extract_dataset_to_bronze(dataset: str) -> None:

    run_id = str(uuid.uuid4())

    source_files = get_dataset_files(dataset)

    for source_file in source_files:

        if already_processed_check(
            dataset,
            source_file.name
        ):
            continue

        write_to_bronze(
            run_id=run_id,
            dataset=dataset,
            source_file=source_file
        )