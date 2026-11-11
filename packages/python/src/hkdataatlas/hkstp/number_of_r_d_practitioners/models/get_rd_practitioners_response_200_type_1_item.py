from typing import Literal

GetRdPractitionersResponse200Type1Item = Literal[""]

GET_RD_PRACTITIONERS_RESPONSE_200_TYPE_1_ITEM_VALUES: set[
    GetRdPractitionersResponse200Type1Item
] = {
    "",
}


def check_get_rd_practitioners_response_200_type_1_item(
    value: str,
) -> GetRdPractitionersResponse200Type1Item:
    if value in GET_RD_PRACTITIONERS_RESPONSE_200_TYPE_1_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_RD_PRACTITIONERS_RESPONSE_200_TYPE_1_ITEM_VALUES!r}"
    )
