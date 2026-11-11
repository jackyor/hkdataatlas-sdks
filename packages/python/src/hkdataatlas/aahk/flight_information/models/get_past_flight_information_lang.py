from typing import Literal

GetPastFlightInformationLang = Literal["en", "zh_CN", "zh_HK"]

GET_PAST_FLIGHT_INFORMATION_LANG_VALUES: set[GetPastFlightInformationLang] = {
    "en",
    "zh_CN",
    "zh_HK",
}


def check_get_past_flight_information_lang(value: str) -> GetPastFlightInformationLang:
    if value in GET_PAST_FLIGHT_INFORMATION_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_PAST_FLIGHT_INFORMATION_LANG_VALUES!r}"
    )
