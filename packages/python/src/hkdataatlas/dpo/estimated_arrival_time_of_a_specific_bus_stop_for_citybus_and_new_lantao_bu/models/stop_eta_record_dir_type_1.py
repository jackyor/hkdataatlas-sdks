from typing import Literal

StopEtaRecordDirType1 = Literal["I", "O"]

STOP_ETA_RECORD_DIR_TYPE_1_VALUES: set[StopEtaRecordDirType1] = {
    "I",
    "O",
}


def check_stop_eta_record_dir_type_1(value: str) -> StopEtaRecordDirType1:
    if value in STOP_ETA_RECORD_DIR_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ETA_RECORD_DIR_TYPE_1_VALUES!r}"
    )
