from typing import Literal

TaxiOpStatus = Literal["N", "O", "V"]

TAXI_OP_STATUS_VALUES: set[TaxiOpStatus] = {
    "N",
    "O",
    "V",
}


def check_taxi_op_status(value: str) -> TaxiOpStatus:
    if value in TAXI_OP_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TAXI_OP_STATUS_VALUES!r}"
    )
