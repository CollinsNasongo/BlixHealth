from etl.extraction.extract_from_landing import extract_dataset_to_bronze


def main():

    extract_dataset_to_bronze(
        dataset="providers"
    )


if __name__ == "__main__":
    main()