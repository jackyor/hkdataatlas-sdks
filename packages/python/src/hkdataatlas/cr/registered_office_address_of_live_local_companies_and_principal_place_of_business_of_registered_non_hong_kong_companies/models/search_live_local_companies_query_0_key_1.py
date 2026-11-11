from typing import Literal

SearchLiveLocalCompaniesQuery0Key1 = Literal["Brn", "Comp_name"]

SEARCH_LIVE_LOCAL_COMPANIES_QUERY_0_KEY_1_VALUES: set[
    SearchLiveLocalCompaniesQuery0Key1
] = {
    "Brn",
    "Comp_name",
}


def check_search_live_local_companies_query_0_key_1(
    value: str,
) -> SearchLiveLocalCompaniesQuery0Key1:
    if value in SEARCH_LIVE_LOCAL_COMPANIES_QUERY_0_KEY_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_LIVE_LOCAL_COMPANIES_QUERY_0_KEY_1_VALUES!r}"
    )
