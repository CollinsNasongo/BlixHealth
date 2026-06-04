import pandas as pd

# String transformations
def upper(source: pd.Series) -> pd.Series:
    return (
        source
        .astype(str)
        .str.upper()
    )


def lower(source: pd.Series) -> pd.Series:
    return (
        source
        .astype(str)
        .str.lower()
    )


def strip(source: pd.Series) -> pd.Series:
    return (
        source
        .astype(str)
        .str.strip()
    )

def substring(source: pd.Series, start: int, length: int) -> pd.Series:

    return (
        source
        .astype(str)
        .str.strip()
        .str[start:start + length]
    )


# Data type transformations
def to_datetime(source: pd.Series) -> pd.Series:
    return pd.to_datetime(source)

def to_date(source: pd.Series) -> pd.Series:
    return pd.to_datetime(
        source,
        format="mixed",
        dayfirst=True,
        errors="coerce"
    ).dt.date

def to_integer(source: pd.Series) -> pd.Series:
    return pd.to_numeric(
        source,
        errors="coerce"
    ).astype("Int64")

def to_decimal(source: pd.Series) -> pd.Series:
    return pd.to_numeric(
        source,
        errors="coerce"
    ).astype("float")  

def to_string(source: pd.Series) -> pd.Series:
    return source.astype(str)

def to_boolean(source: pd.Series) -> pd.Series:

    true_values = {
        "true", "t", "yes", "y", "1"
    }

    false_values = {
        "false", "f", "no", "n", "0"
    }

    def convert(value):

        if pd.isna(value):
            return None

        value = str(value).strip().lower()

        if value == "":
            return None

        if value in true_values:
            return True

        if value in false_values:
            return False

        raise ValueError(
            f"Cannot convert '{value}' to boolean"
        )

    return source.apply(convert)


# Verify length of string
def verify_length(source: pd.Series, expected_length: int) -> pd.Series:
    return source.astype(str).str.len() == expected_length