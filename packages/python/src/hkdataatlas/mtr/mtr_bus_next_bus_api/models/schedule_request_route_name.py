from typing import Literal

ScheduleRequestRouteName = Literal[
    "506",
    "K12",
    "K14",
    "K17",
    "K18",
    "K51",
    "K51A",
    "K52",
    "K52A",
    "K52P",
    "K53",
    "K53S",
    "K54",
    "K54A",
    "K58",
    "K65",
    "K65A",
    "K66",
    "K68",
    "K73",
    "K74",
    "K75A",
    "K75P",
    "K75S",
    "K76",
    "K76S",
]

SCHEDULE_REQUEST_ROUTE_NAME_VALUES: set[ScheduleRequestRouteName] = {
    "506",
    "K12",
    "K14",
    "K17",
    "K18",
    "K51",
    "K51A",
    "K52",
    "K52A",
    "K52P",
    "K53",
    "K53S",
    "K54",
    "K54A",
    "K58",
    "K65",
    "K65A",
    "K66",
    "K68",
    "K73",
    "K74",
    "K75A",
    "K75P",
    "K75S",
    "K76",
    "K76S",
}


def check_schedule_request_route_name(value: str) -> ScheduleRequestRouteName:
    if value in SCHEDULE_REQUEST_ROUTE_NAME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEDULE_REQUEST_ROUTE_NAME_VALUES!r}"
    )
