from typing import Literal

GetRegisterAmbsLang = Literal["en", "tc"]

GET_REGISTER_AMBS_LANG_VALUES: set[GetRegisterAmbsLang] = {
    "en",
    "tc",
}


def check_get_register_ambs_lang(value: str) -> GetRegisterAmbsLang:
    if value in GET_REGISTER_AMBS_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_REGISTER_AMBS_LANG_VALUES!r}"
    )
