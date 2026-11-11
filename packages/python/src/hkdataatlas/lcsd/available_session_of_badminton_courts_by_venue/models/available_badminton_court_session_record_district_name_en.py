from typing import Literal

AvailableBadmintonCourtSessionRecordDistrictNameEN = Literal[
    "Central & Western",
    "Eastern",
    "Islands",
    "Kowloon City",
    "Kwai Tsing",
    "Kwun Tong",
    "North",
    "Sai Kung",
    "Sha Tin",
    "Sham Shui Po",
    "Southern",
    "Tai Po",
    "Tsuen Wan",
    "Tuen Mun",
    "Wan Chai",
    "Wong Tai Sin",
    "Yau Tsim Mong",
    "Yuen Long",
]

AVAILABLE_BADMINTON_COURT_SESSION_RECORD_DISTRICT_NAME_EN_VALUES: set[
    AvailableBadmintonCourtSessionRecordDistrictNameEN
] = {
    "Central & Western",
    "Eastern",
    "Islands",
    "Kowloon City",
    "Kwai Tsing",
    "Kwun Tong",
    "North",
    "Sai Kung",
    "Sha Tin",
    "Sham Shui Po",
    "Southern",
    "Tai Po",
    "Tsuen Wan",
    "Tuen Mun",
    "Wan Chai",
    "Wong Tai Sin",
    "Yau Tsim Mong",
    "Yuen Long",
}


def check_available_badminton_court_session_record_district_name_en(
    value: str,
) -> AvailableBadmintonCourtSessionRecordDistrictNameEN:
    if value in AVAILABLE_BADMINTON_COURT_SESSION_RECORD_DISTRICT_NAME_EN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AVAILABLE_BADMINTON_COURT_SESSION_RECORD_DISTRICT_NAME_EN_VALUES!r}"
    )
