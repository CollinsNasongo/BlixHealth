from pathlib import Path
import os

# =========================
# PROJECT ROOT DIRECTORY
# =========================

PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

# =========================
# BASE DATA DIRECTORY
# =========================
DATA_DIR = Path(os.getenv("DATA_DIR", PROJECT_DIR / "data"))

# =========================
# MAPPINGS DIRECTORY
# =========================
MAPPINGS_DIR = Path(os.getenv("MAPPINGS_DIR", PROJECT_DIR / "mappings"))

# =========================
# LAYER DIRECTORIES
# =========================
LANDING_DIR = DATA_DIR / "landing"
SOURCE_TO_BRONZE_MAPPINGS_DIR = MAPPINGS_DIR / "source_to_bronze"
BRONZE_TO_SILVER_MAPPINGS_DIR = MAPPINGS_DIR / "bronze_to_silver"
SILVER_TO_GOLD_MAPPINGS_DIR = MAPPINGS_DIR / "silver_to_gold"

# =========================
# FILE HELPERS
# =========================
def landing_file(dataset: str, filename: str) -> Path:
    return LANDING_DIR / dataset / filename


# =========================
# MAPPING HELPERS
# =========================

def bronze_to_silver_mapping_file(
    dataset: str
) -> Path:
    return (
        BRONZE_TO_SILVER_MAPPINGS_DIR
        / f"{dataset}.csv"
    )


def silver_to_gold_mapping_file(
    dataset: str
) -> Path:
    return (
        SILVER_TO_GOLD_MAPPINGS_DIR
        / f"{dataset}.csv"
    )


# =========================
# DEBUG HELPER
# =========================
def debug_paths():
    print("DATA_DIR  :", DATA_DIR)
    print("LANDING_DIR:", LANDING_DIR)
    print("MAPPINGS_DIR  :", MAPPINGS_DIR)
    print("BRONZE_TO_SILVER_MAPPINGS_DIR  :", BRONZE_TO_SILVER_MAPPINGS_DIR)
    print("SILVER_TO_GOLD_MAPPINGS_DIR  :", SILVER_TO_GOLD_MAPPINGS_DIR)