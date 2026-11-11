from typing import Literal

SearchMajorSpeechesLang = Literal["en"]

SEARCH_MAJOR_SPEECHES_LANG_VALUES: set[SearchMajorSpeechesLang] = {
    "en",
}


def check_search_major_speeches_lang(value: str) -> SearchMajorSpeechesLang:
    if value in SEARCH_MAJOR_SPEECHES_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_MAJOR_SPEECHES_LANG_VALUES!r}"
    )
