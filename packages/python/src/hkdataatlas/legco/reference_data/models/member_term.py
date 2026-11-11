from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberTerm")


@_attrs_define
class MemberTerm:
    """Member-term association record. Requiredness is not specified.

    Attributes:
        member_id (float | Unset): Member identifier. Example: 187.
        member_term_id (float | Unset): Record identifier. Example: 3581716.
        term_id (float | Unset): Term identifier. Example: 5.
    """

    member_id: float | Unset = UNSET
    member_term_id: float | Unset = UNSET
    term_id: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_id = self.member_id

        member_term_id = self.member_term_id

        term_id = self.term_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if member_term_id is not UNSET:
            field_dict["member_term_id"] = member_term_id
        if term_id is not UNSET:
            field_dict["term_id"] = term_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        member_id = d.pop("member_id", UNSET)

        member_term_id = d.pop("member_term_id", UNSET)

        term_id = d.pop("term_id", UNSET)

        member_term = cls(
            member_id=member_id,
            member_term_id=member_term_id,
            term_id=term_id,
        )

        member_term.additional_properties = d
        return member_term

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
