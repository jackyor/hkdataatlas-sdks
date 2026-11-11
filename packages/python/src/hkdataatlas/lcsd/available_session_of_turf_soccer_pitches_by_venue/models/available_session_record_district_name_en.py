from typing import Literal

AvailableSessionRecordDistrictNameEN = Literal[
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

AVAILABLE_SESSION_RECORD_DISTRICT_NAME_EN_VALUES: set[
    AvailableSessionRecordDistrictNameEN
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


def check_available_session_record_district_name_en(
    value: str,
) -> AvailableSessionRecordDistrictNameEN:
    if value in AVAILABLE_SESSION_RECORD_DISTRICT_NAME_EN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AVAILABLE_SESSION_RECORD_DISTRICT_NAME_EN_VALUES!r}"
    )
