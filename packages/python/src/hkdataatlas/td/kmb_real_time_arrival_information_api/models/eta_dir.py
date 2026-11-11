from typing import Literal

EtaDir = Literal["I", "O"]

ETA_DIR_VALUES: set[EtaDir] = {
    "I",
    "O",
}


def check_eta_dir(value: str) -> EtaDir:
    if value in ETA_DIR_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ETA_DIR_VALUES!r}")
