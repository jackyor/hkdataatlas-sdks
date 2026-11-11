from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrhExportRecord")


@_attrs_define
class PrhExportRecord:
    """Optional current export names and string wire types from retained complete body. Dictionary describes equivalent
    concepts under different JSON names.

        Attributes:
            id (str | Unset):
            inc_ast_lmt_type (str | Unset):
            family_size (str | Unset):
            income_limit (str | Unset):
            asset_limit (str | Unset):
            effective_from (str | Unset):
    """

    id: str | Unset = UNSET
    inc_ast_lmt_type: str | Unset = UNSET
    family_size: str | Unset = UNSET
    income_limit: str | Unset = UNSET
    asset_limit: str | Unset = UNSET
    effective_from: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        inc_ast_lmt_type = self.inc_ast_lmt_type

        family_size = self.family_size

        income_limit = self.income_limit

        asset_limit = self.asset_limit

        effective_from = self.effective_from

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if inc_ast_lmt_type is not UNSET:
            field_dict["inc_ast_lmt_type"] = inc_ast_lmt_type
        if family_size is not UNSET:
            field_dict["family_size"] = family_size
        if income_limit is not UNSET:
            field_dict["income_limit"] = income_limit
        if asset_limit is not UNSET:
            field_dict["asset_limit"] = asset_limit
        if effective_from is not UNSET:
            field_dict["effective_from"] = effective_from

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        inc_ast_lmt_type = d.pop("inc_ast_lmt_type", UNSET)

        family_size = d.pop("family_size", UNSET)

        income_limit = d.pop("income_limit", UNSET)

        asset_limit = d.pop("asset_limit", UNSET)

        effective_from = d.pop("effective_from", UNSET)

        prh_export_record = cls(
            id=id,
            inc_ast_lmt_type=inc_ast_lmt_type,
            family_size=family_size,
            income_limit=income_limit,
            asset_limit=asset_limit,
            effective_from=effective_from,
        )

        prh_export_record.additional_properties = d
        return prh_export_record

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
