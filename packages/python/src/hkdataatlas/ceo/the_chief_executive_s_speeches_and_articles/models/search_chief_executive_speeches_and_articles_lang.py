from typing import Literal

SearchChiefExecutiveSpeechesAndArticlesLang = Literal["en", "sc", "tc"]

SEARCH_CHIEF_EXECUTIVE_SPEECHES_AND_ARTICLES_LANG_VALUES: set[
    SearchChiefExecutiveSpeechesAndArticlesLang
] = {
    "en",
    "sc",
    "tc",
}


def check_search_chief_executive_speeches_and_articles_lang(
    value: str,
) -> SearchChiefExecutiveSpeechesAndArticlesLang:
    if value in SEARCH_CHIEF_EXECUTIVE_SPEECHES_AND_ARTICLES_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_CHIEF_EXECUTIVE_SPEECHES_AND_ARTICLES_LANG_VALUES!r}"
    )
