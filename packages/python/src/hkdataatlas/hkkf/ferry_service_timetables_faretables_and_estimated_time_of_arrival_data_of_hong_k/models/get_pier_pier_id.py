from typing import Literal

GetPierPierId = Literal[1, 2, 3, 4, 5, 6]

GET_PIER_PIER_ID_VALUES: set[GetPierPierId] = {
    1,
    2,
    3,
    4,
    5,
    6,
}


def check_get_pier_pier_id(value: int) -> GetPierPierId:
    if value in GET_PIER_PIER_ID_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_PIER_PIER_ID_VALUES!r}"
    )
