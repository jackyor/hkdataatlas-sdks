from typing import Literal

ResponseStatusCode = Literal[0, 1, 2, 3, 4]

RESPONSE_STATUS_CODE_VALUES: set[ResponseStatusCode] = {
    0,
    1,
    2,
    3,
    4,
}


def check_response_status_code(value: int) -> ResponseStatusCode:
    if value in RESPONSE_STATUS_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_STATUS_CODE_VALUES!r}"
    )
