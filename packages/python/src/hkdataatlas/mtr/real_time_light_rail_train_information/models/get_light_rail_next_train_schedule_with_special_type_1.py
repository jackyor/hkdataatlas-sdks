from typing import Literal

GetLightRailNextTrainScheduleWithSpecialType1 = Literal[1]

GET_LIGHT_RAIL_NEXT_TRAIN_SCHEDULE_WITH_SPECIAL_TYPE_1_VALUES: set[
    GetLightRailNextTrainScheduleWithSpecialType1
] = {
    1,
}


def check_get_light_rail_next_train_schedule_with_special_type_1(
    value: int,
) -> GetLightRailNextTrainScheduleWithSpecialType1:
    if value in GET_LIGHT_RAIL_NEXT_TRAIN_SCHEDULE_WITH_SPECIAL_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LIGHT_RAIL_NEXT_TRAIN_SCHEDULE_WITH_SPECIAL_TYPE_1_VALUES!r}"
    )
