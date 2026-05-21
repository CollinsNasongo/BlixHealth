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
LOGS_DIR = DATA_DIR / "logs"
LANDING_DIR = DATA_DIR / "landing"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR   = DATA_DIR / "gold"
BRONZE_TO_SILVER_MAPPINGS_DIR = MAPPINGS_DIR / "bronze_to_silver"
SILVER_TO_GOLD_MAPPINGS_DIR = MAPPINGS_DIR / "silver_to_gold"

# =========================
# FILE HELPERS
# =========================

def log_file(filename: str) -> Path:
    return LOGS_DIR / filename


def landing_file(dataset: str, filename: str) -> Path:
    return LANDING_DIR / dataset / filename


def bronze_file(dataset: str, filename: str) -> Path:
    return BRONZE_DIR / dataset / filename


def silver_file(dataset: str, filename: str) -> Path:
    return SILVER_DIR / dataset / filename


def gold_file(dataset: str, filename: str) -> Path:
    return GOLD_DIR / dataset / filename


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
    print("BRONZE_DIR:", BRONZE_DIR)
    print("SILVER_DIR:", SILVER_DIR)
    print("GOLD_DIR  :", GOLD_DIR)
    print("LOGS_DIR  :", LOGS_DIR)
    print("MAPPINGS_DIR  :", MAPPINGS_DIR)
    print("BRONZE_TO_SILVER_MAPPINGS_DIR  :", BRONZE_TO_SILVER_MAPPINGS_DIR)
    print("SILVER_TO_GOLD_MAPPINGS_DIR  :", SILVER_TO_GOLD_MAPPINGS_DIR)