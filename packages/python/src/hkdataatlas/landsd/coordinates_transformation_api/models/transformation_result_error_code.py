from typing import Literal

TransformationResultErrorCode = Literal[1, 2, 3, 4, 5, 6, 7]

TRANSFORMATION_RESULT_ERROR_CODE_VALUES: set[TransformationResultErrorCode] = {
    1,
    2,
    3,
    4,
    5,
    6,
    7,
}


def check_transformation_result_error_code(value: int) -> TransformationResultErrorCode:
    if value in TRANSFORMATION_RESULT_ERROR_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRANSFORMATION_RESULT_ERROR_CODE_VALUES!r}"
    )
