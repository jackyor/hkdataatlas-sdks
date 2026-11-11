from typing import Literal

TaxiFleetTdSlimRecordOpStatus = Literal["N", "O", "V"]

TAXI_FLEET_TD_SLIM_RECORD_OP_STATUS_VALUES: set[TaxiFleetTdSlimRecordOpStatus] = {
    "N",
    "O",
    "V",
}


def check_taxi_fleet_td_slim_record_op_status(
    value: str,
) -> TaxiFleetTdSlimRecordOpStatus:
    if value in TAXI_FLEET_TD_SLIM_RECORD_OP_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TAXI_FLEET_TD_SLIM_RECORD_OP_STATUS_VALUES!r}"
    )
