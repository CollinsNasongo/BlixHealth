from etl.bronze_to_silver.build_silver_table import get_bronze_files
from models.registry import get_model


def test_get_bronze_files():
    dataset = "providers"
    files = get_bronze_files(dataset)
    assert len(files) > 0, "No bronze files found for dataset 'providers'"
    print(f"Found {len(files)} bronze files for dataset '{dataset}'.")


if __name__ == "__main__":
    #test_get_model()
    test_get_bronze_files()