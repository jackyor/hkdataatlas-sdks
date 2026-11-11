from typing import Literal

SearchBlogLang = Literal["en", "sc", "tc"]

SEARCH_BLOG_LANG_VALUES: set[SearchBlogLang] = {
    "en",
    "sc",
    "tc",
}


def check_search_blog_lang(value: str) -> SearchBlogLang:
    if value in SEARCH_BLOG_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_BLOG_LANG_VALUES!r}"
    )
