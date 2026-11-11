from typing import Literal

StopEtaRecordCo = Literal["CTB", "NLB"]

STOP_ETA_RECORD_CO_VALUES: set[StopEtaRecordCo] = {
    "CTB",
    "NLB",
}


def check_stop_eta_record_co(value: str) -> StopEtaRecordCo:
    if value in STOP_ETA_RECORD_CO_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ETA_RECORD_CO_VALUES!r}"
    )
