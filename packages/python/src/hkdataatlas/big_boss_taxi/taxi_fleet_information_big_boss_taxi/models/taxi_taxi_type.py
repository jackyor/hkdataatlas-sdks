from typing import Literal

TaxiTaxiType = Literal["O", "P", "W"]

TAXI_TAXI_TYPE_VALUES: set[TaxiTaxiType] = {
    "O",
    "P",
    "W",
}


def check_taxi_taxi_type(value: str) -> TaxiTaxiType:
    if value in TAXI_TAXI_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TAXI_TAXI_TYPE_VALUES!r}"
    )
