from typing import Literal

TennisCourtSessionDistrictNameEN = Literal[
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

TENNIS_COURT_SESSION_DISTRICT_NAME_EN_VALUES: set[TennisCourtSessionDistrictNameEN] = {
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


def check_tennis_court_session_district_name_en(
    value: str,
) -> TennisCourtSessionDistrictNameEN:
    if value in TENNIS_COURT_SESSION_DISTRICT_NAME_EN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TENNIS_COURT_SESSION_DISTRICT_NAME_EN_VALUES!r}"
    )
