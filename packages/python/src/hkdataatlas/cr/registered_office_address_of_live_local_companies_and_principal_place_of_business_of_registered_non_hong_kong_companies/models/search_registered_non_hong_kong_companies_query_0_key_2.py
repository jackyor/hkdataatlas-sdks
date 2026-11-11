from typing import Literal

SearchRegisteredNonHongKongCompaniesQuery0Key2 = Literal["begins_with", "equal"]

SEARCH_REGISTERED_NON_HONG_KONG_COMPANIES_QUERY_0_KEY_2_VALUES: set[
    SearchRegisteredNonHongKongCompaniesQuery0Key2
] = {
    "begins_with",
    "equal",
}


def check_search_registered_non_hong_kong_companies_query_0_key_2(
    value: str,
) -> SearchRegisteredNonHongKongCompaniesQuery0Key2:
    if value in SEARCH_REGISTERED_NON_HONG_KONG_COMPANIES_QUERY_0_KEY_2_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_REGISTERED_NON_HONG_KONG_COMPANIES_QUERY_0_KEY_2_VALUES!r}"
    )
