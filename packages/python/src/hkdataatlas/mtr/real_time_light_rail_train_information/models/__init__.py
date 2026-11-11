"""Contains all the data models used in inputs/outputs"""

from .get_light_rail_next_train_schedule_with_special_type_0 import (
    GetLightRailNextTrainScheduleWithSpecialType0,
)
from .get_light_rail_next_train_schedule_with_special_type_1 import (
    GetLightRailNextTrainScheduleWithSpecialType1,
)
from .platform import Platform
from .route import Route
from .schedule_response import ScheduleResponse

__all__ = (
    "GetLightRailNextTrainScheduleWithSpecialType0",
    "GetLightRailNextTrainScheduleWithSpecialType1",
    "Platform",
    "Route",
    "ScheduleResponse",
)
