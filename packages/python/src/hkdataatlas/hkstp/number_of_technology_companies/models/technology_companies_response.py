from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TechnologyCompaniesResponse")


@_attrs_define
class TechnologyCompaniesResponse:
    """Response fields documented by the publisher. The example is representative and does not establish that these are the
    only response properties.

        Attributes:
            item (str | Unset): Technology Companies.
            value (str | Unset): Total number, represented as a string in the documented example.
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

        technology_companies_response = cls(
            item=item,
            value=value,
        )

        technology_companies_response.additional_properties = d
        return technology_companies_response

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
