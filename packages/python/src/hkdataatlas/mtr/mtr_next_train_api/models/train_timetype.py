from typing import Literal

TrainTimetype = Literal["A", "D"]

TRAIN_TIMETYPE_VALUES: set[TrainTimetype] = {
    "A",
    "D",
}


def check_train_timetype(value: str) -> TrainTimetype:
    if value in TRAIN_TIMETYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRAIN_TIMETYPE_VALUES!r}"
    )
