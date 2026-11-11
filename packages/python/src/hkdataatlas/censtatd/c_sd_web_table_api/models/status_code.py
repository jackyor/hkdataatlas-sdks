from typing import Literal

StatusCode = Literal[0, 1]

STATUS_CODE_VALUES: set[StatusCode] = {
    0,
    1,
}


def check_status_code(value: int) -> StatusCode:
    if value in STATUS_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STATUS_CODE_VALUES!r}"
    )
