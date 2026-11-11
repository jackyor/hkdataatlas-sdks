from typing import Literal

GetIncubationGraduatesResponse200Type1Item = Literal[""]

GET_INCUBATION_GRADUATES_RESPONSE_200_TYPE_1_ITEM_VALUES: set[
    GetIncubationGraduatesResponse200Type1Item
] = {
    "",
}


def check_get_incubation_graduates_response_200_type_1_item(
    value: str,
) -> GetIncubationGraduatesResponse200Type1Item:
    if value in GET_INCUBATION_GRADUATES_RESPONSE_200_TYPE_1_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_INCUBATION_GRADUATES_RESPONSE_200_TYPE_1_ITEM_VALUES!r}"
    )
