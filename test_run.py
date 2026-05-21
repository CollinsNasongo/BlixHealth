from etl.extraction.extract_from_landing import extract_dataset_to_bronze


def main():
    print("Calling extract_dataset_to_bronze...")

    result = extract_dataset_to_bronze(
        dataset="providers"
    )

    print(f"Result: {result}")


if __name__ == "__main__":
    print("Starting ETL pipeline...")
    main()
    print("ETL pipeline completed.")