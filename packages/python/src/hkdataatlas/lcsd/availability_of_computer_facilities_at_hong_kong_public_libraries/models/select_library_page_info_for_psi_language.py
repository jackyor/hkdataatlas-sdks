from typing import Literal

SelectLibraryPageInfoForPsiLanguage = Literal["en-US", "zh-CN", "zh-HK"]

SELECT_LIBRARY_PAGE_INFO_FOR_PSI_LANGUAGE_VALUES: set[
    SelectLibraryPageInfoForPsiLanguage
] = {
    "en-US",
    "zh-CN",
    "zh-HK",
}


def check_select_library_page_info_for_psi_language(
    value: str,
) -> SelectLibraryPageInfoForPsiLanguage:
    if value in SELECT_LIBRARY_PAGE_INFO_FOR_PSI_LANGUAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SELECT_LIBRARY_PAGE_INFO_FOR_PSI_LANGUAGE_VALUES!r}"
    )
