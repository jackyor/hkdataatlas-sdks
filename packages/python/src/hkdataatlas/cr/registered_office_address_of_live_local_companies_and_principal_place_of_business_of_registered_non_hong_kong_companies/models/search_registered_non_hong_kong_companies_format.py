from typing import Literal

SearchRegisteredNonHongKongCompaniesFormat = Literal["csv", "json", "xml"]

SEARCH_REGISTERED_NON_HONG_KONG_COMPANIES_FORMAT_VALUES: set[
    SearchRegisteredNonHongKongCompaniesFormat
] = {
    "csv",
    "json",
    "xml",
}


def check_search_registered_non_hong_kong_companies_format(
    value: str,
) -> SearchRegisteredNonHongKongCompaniesFormat:
    if value in SEARCH_REGISTERED_NON_HONG_KONG_COMPANIES_FORMAT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_REGISTERED_NON_HONG_KONG_COMPANIES_FORMAT_VALUES!r}"
    )
