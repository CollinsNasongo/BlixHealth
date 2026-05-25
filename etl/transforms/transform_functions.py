import pandas as pd


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


def to_datetime(source: pd.Series) -> pd.Series:
    return pd.to_datetime(source)


def to_integer(source: pd.Series) -> pd.Series:
    return pd.to_numeric(
        source,
        errors="coerce"
    ).astype("Int64")


def substring(
    source: pd.Series,
    start: int,
    length: int
) -> pd.Series:

    return (
        source
        .astype(str)
        .str.strip()
        .str[start:start + length]
    )