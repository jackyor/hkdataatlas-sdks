from typing import Literal

TennisCourtSessionDistrictNameTC = Literal[
    "中西區",
    "九龍城區",
    "元朗區",
    "北區",
    "南區",
    "大埔區",
    "屯門區",
    "東區",
    "沙田區",
    "油尖旺區",
    "深水埗區",
    "灣仔區",
    "荃灣區",
    "葵青區",
    "西貢區",
    "觀塘區",
    "離島區",
    "黃大仙區",
]

TENNIS_COURT_SESSION_DISTRICT_NAME_TC_VALUES: set[TennisCourtSessionDistrictNameTC] = {
    "中西區",
    "九龍城區",
    "元朗區",
    "北區",
    "南區",
    "大埔區",
    "屯門區",
    "東區",
    "沙田區",
    "油尖旺區",
    "深水埗區",
    "灣仔區",
    "荃灣區",
    "葵青區",
    "西貢區",
    "觀塘區",
    "離島區",
    "黃大仙區",
}


def check_tennis_court_session_district_name_tc(
    value: str,
) -> TennisCourtSessionDistrictNameTC:
    if value in TENNIS_COURT_SESSION_DISTRICT_NAME_TC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TENNIS_COURT_SESSION_DISTRICT_NAME_TC_VALUES!r}"
    )
