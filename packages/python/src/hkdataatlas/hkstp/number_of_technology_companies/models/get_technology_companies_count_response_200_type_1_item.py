from typing import Literal

GetTechnologyCompaniesCountResponse200Type1Item = Literal[""]

GET_TECHNOLOGY_COMPANIES_COUNT_RESPONSE_200_TYPE_1_ITEM_VALUES: set[
    GetTechnologyCompaniesCountResponse200Type1Item
] = {
    "",
}


def check_get_technology_companies_count_response_200_type_1_item(
    value: str,
) -> GetTechnologyCompaniesCountResponse200Type1Item:
    if value in GET_TECHNOLOGY_COMPANIES_COUNT_RESPONSE_200_TYPE_1_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_TECHNOLOGY_COMPANIES_COUNT_RESPONSE_200_TYPE_1_ITEM_VALUES!r}"
    )
