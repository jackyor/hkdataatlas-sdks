from typing import Literal

SearchLiveLocalCompaniesFormat = Literal["csv", "json", "xml"]

SEARCH_LIVE_LOCAL_COMPANIES_FORMAT_VALUES: set[SearchLiveLocalCompaniesFormat] = {
    "csv",
    "json",
    "xml",
}


def check_search_live_local_companies_format(
    value: str,
) -> SearchLiveLocalCompaniesFormat:
    if value in SEARCH_LIVE_LOCAL_COMPANIES_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_LIVE_LOCAL_COMPANIES_FORMAT_VALUES!r}"
    )
