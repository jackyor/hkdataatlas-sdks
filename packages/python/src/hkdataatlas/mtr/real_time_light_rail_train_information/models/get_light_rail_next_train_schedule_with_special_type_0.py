from typing import Literal

GetLightRailNextTrainScheduleWithSpecialType0 = Literal[0]

GET_LIGHT_RAIL_NEXT_TRAIN_SCHEDULE_WITH_SPECIAL_TYPE_0_VALUES: set[
    GetLightRailNextTrainScheduleWithSpecialType0
] = {
    0,
}


def check_get_light_rail_next_train_schedule_with_special_type_0(
    value: int,
) -> GetLightRailNextTrainScheduleWithSpecialType0:
    if value in GET_LIGHT_RAIL_NEXT_TRAIN_SCHEDULE_WITH_SPECIAL_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LIGHT_RAIL_NEXT_TRAIN_SCHEDULE_WITH_SPECIAL_TYPE_0_VALUES!r}"
    )
