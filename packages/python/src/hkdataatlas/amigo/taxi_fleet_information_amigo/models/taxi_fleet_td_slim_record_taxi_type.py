from typing import Literal

TaxiFleetTdSlimRecordTaxiType = Literal["O", "P", "W"]

TAXI_FLEET_TD_SLIM_RECORD_TAXI_TYPE_VALUES: set[TaxiFleetTdSlimRecordTaxiType] = {
    "O",
    "P",
    "W",
}


def check_taxi_fleet_td_slim_record_taxi_type(
    value: str,
) -> TaxiFleetTdSlimRecordTaxiType:
    if value in TAXI_FLEET_TD_SLIM_RECORD_TAXI_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TAXI_FLEET_TD_SLIM_RECORD_TAXI_TYPE_VALUES!r}"
    )
