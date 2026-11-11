from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncubationGraduatesResponse")


@_attrs_define
class IncubationGraduatesResponse:
    """The source documents item as the incubation graduates label and value as the total number. Both are declared as
    String. The example value is "620+".

        Attributes:
            item (str | Unset): Incubation graduates item label. Example: incubation graduates since inception.
            value (str | Unset): Total number of incubation graduates. Example: 620+.
    """

    item: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item = self.item

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item is not UNSET:
            field_dict["item"] = item
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        item = d.pop("item", UNSET)

        value = d.pop("value", UNSET)

        incubation_graduates_response = cls(
            item=item,
            value=value,
        )

        incubation_graduates_response.additional_properties = d
        return incubation_graduates_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
