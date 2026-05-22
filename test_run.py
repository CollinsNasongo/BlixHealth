from etl.bronze_to_silver.build_silver_table import load_mapping
from models.registry import get_model


def test_get_model():
    model = get_model("silver", "practitioner")
    assert model.__name__ == "Practitioner"
    print(model.__name__)

def test_load_mapping():
    mapping = load_mapping("state")
    assert mapping is not None
    print(mapping.head())


if __name__ == "__main__":
    #test_get_model()
    test_load_mapping()