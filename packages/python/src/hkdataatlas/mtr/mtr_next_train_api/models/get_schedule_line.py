from typing import Literal

GetScheduleLine = Literal[
    "AEL", "DRL", "EAL", "ISL", "KTL", "SIL", "TCL", "TKL", "TML", "TWL"
]

GET_SCHEDULE_LINE_VALUES: set[GetScheduleLine] = {
    "AEL",
    "DRL",
    "EAL",
    "ISL",
    "KTL",
    "SIL",
    "TCL",
    "TKL",
    "TML",
    "TWL",
}


def check_get_schedule_line(value: str) -> GetScheduleLine:
    if value in GET_SCHEDULE_LINE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_SCHEDULE_LINE_VALUES!r}"
    )
