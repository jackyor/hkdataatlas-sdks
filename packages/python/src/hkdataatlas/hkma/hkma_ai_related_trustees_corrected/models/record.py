from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        name (str | Unset):
        principal_place (str | Unset):
        official_web (str | Unset):
        associated_ai (str | Unset):
    """

    name: str | Unset = UNSET
    principal_place: str | Unset = UNSET
    official_web: str | Unset = UNSET
    associated_ai: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        principal_place = self.principal_place

        official_web = self.official_web

        associated_ai = self.associated_ai

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if principal_place is not UNSET:
            field_dict["principal_place"] = principal_place
        if official_web is not UNSET:
            field_dict["official_web"] = official_web
        if associated_ai is not UNSET:
            field_dict["associated_ai"] = associated_ai

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        principal_place = d.pop("principal_place", UNSET)

        official_web = d.pop("official_web", UNSET)

        associated_ai = d.pop("associated_ai", UNSET)

        record = cls(
            name=name,
            principal_place=principal_place,
            official_web=official_web,
            associated_ai=associated_ai,
        )

        record.additional_properties = d
        return record

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
