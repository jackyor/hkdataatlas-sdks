from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.get_incubation_graduates_response_200_type_1_item import (
    GetIncubationGraduatesResponse200Type1Item,
    check_get_incubation_graduates_response_200_type_1_item,
)

T = TypeVar("T", bound="GetIncubationGraduatesResponse200Type1")


@_attrs_define
class GetIncubationGraduatesResponse200Type1:
    """
    Attributes:
        item (GetIncubationGraduatesResponse200Type1Item):
        value (None):
    """

    item: GetIncubationGraduatesResponse200Type1Item
    value: None

    def to_dict(self) -> dict[str, Any]:
        item: str = self.item

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "item": item,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        item = check_get_incubation_graduates_response_200_type_1_item(d.pop("item"))

        value = d.pop("value")

        get_incubation_graduates_response_200_type_1 = cls(
            item=item,
            value=value,
        )

        return get_incubation_graduates_response_200_type_1
