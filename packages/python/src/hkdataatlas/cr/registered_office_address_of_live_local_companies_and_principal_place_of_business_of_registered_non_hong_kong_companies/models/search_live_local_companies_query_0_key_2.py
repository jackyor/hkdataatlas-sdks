from typing import Literal

SearchLiveLocalCompaniesQuery0Key2 = Literal["begins_with", "equal"]

SEARCH_LIVE_LOCAL_COMPANIES_QUERY_0_KEY_2_VALUES: set[
    SearchLiveLocalCompaniesQuery0Key2
] = {
    "begins_with",
    "equal",
}


def check_search_live_local_companies_query_0_key_2(
    value: str,
) -> SearchLiveLocalCompaniesQuery0Key2:
    if value in SEARCH_LIVE_LOCAL_COMPANIES_QUERY_0_KEY_2_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_LIVE_LOCAL_COMPANIES_QUERY_0_KEY_2_VALUES!r}"
    )
