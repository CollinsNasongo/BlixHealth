from etl.transforms.transform_functions import (
    upper,
    lower,
    strip,
    to_datetime,
    to_integer,
    substring,
)

SYSTEM_TRANSFORMS = {
    "autoincrement"
}

TRANSFORM_REGISTRY = {
    "upper": upper,
    "lower": lower,
    "strip": strip,
    "trim": strip,
    "to_datetime": to_datetime,
    "to_integer": to_integer,
    "substring": substring,
}