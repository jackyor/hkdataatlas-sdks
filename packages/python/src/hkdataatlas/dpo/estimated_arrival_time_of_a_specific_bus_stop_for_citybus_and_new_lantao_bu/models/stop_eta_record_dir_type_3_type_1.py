from typing import Literal

StopEtaRecordDirType3Type1 = Literal["I", "O"]

STOP_ETA_RECORD_DIR_TYPE_3_TYPE_1_VALUES: set[StopEtaRecordDirType3Type1] = {
    "I",
    "O",
}


def check_stop_eta_record_dir_type_3_type_1(value: str) -> StopEtaRecordDirType3Type1:
    if value in STOP_ETA_RECORD_DIR_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STOP_ETA_RECORD_DIR_TYPE_3_TYPE_1_VALUES!r}"
    )
