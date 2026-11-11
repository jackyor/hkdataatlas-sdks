from typing import Literal

IdentifyFacilityLang = Literal["en", "zh"]

IDENTIFY_FACILITY_LANG_VALUES: set[IdentifyFacilityLang] = {
    "en",
    "zh",
}


def check_identify_facility_lang(value: str) -> IdentifyFacilityLang:
    if value in IDENTIFY_FACILITY_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IDENTIFY_FACILITY_LANG_VALUES!r}"
    )
