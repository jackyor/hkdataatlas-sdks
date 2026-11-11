from typing import Literal

SearchRegisteredNonHongKongCompaniesQuery0Key1 = Literal["Brn", "Comp_name"]

SEARCH_REGISTERED_NON_HONG_KONG_COMPANIES_QUERY_0_KEY_1_VALUES: set[
    SearchRegisteredNonHongKongCompaniesQuery0Key1
] = {
    "Brn",
    "Comp_name",
}


def check_search_registered_non_hong_kong_companies_query_0_key_1(
    value: str,
) -> SearchRegisteredNonHongKongCompaniesQuery0Key1:
    if value in SEARCH_REGISTERED_NON_HONG_KONG_COMPANIES_QUERY_0_KEY_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_REGISTERED_NON_HONG_KONG_COMPANIES_QUERY_0_KEY_1_VALUES!r}"
    )
