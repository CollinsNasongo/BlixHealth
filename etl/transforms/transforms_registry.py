from etl.transforms.transform_functions import (
    upper,
    lower,
    strip,
    to_datetime,
    to_integer,
    substring,
    to_decimal,
    to_string,
    verify_length,
)

SYSTEM_TRANSFORMS = {
    "autoincrement"
}

TRANSFORM_REGISTRY = {
    "upper": upper,
    "lower": lower,
    "strip": strip,
    "trim": strip,
    "substring": substring,
    "to_datetime": to_datetime,
    "to_integer": to_integer,
    "to_decimal": to_decimal,
    "to_string": to_string,
    "verify_length": verify_length,
}