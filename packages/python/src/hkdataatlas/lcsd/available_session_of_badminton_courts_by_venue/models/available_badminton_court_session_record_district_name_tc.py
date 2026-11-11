from typing import Literal

AvailableBadmintonCourtSessionRecordDistrictNameTC = Literal[
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

AVAILABLE_BADMINTON_COURT_SESSION_RECORD_DISTRICT_NAME_TC_VALUES: set[
    AvailableBadmintonCourtSessionRecordDistrictNameTC
] = {
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


def check_available_badminton_court_session_record_district_name_tc(
    value: str,
) -> AvailableBadmintonCourtSessionRecordDistrictNameTC:
    if value in AVAILABLE_BADMINTON_COURT_SESSION_RECORD_DISTRICT_NAME_TC_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AVAILABLE_BADMINTON_COURT_SESSION_RECORD_DISTRICT_NAME_TC_VALUES!r}"
    )
