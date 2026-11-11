from typing import Literal

StatusName = Literal["Fail", "Success"]

STATUS_NAME_VALUES: set[StatusName] = {
    "Fail",
    "Success",
}


def check_status_name(value: str) -> StatusName:
    if value in STATUS_NAME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_NAME_VALUES!r}"
    )
