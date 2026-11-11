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
        end_of_month (str | Unset): The retained complete successful publisher response uses year-month strings (YYYY-
            MM), not full RFC 3339 dates. The publisher Swagger date format is therefore omitted. Further lexical or
            calendar constraints are undocumented; values are preserved without coercion.
        conduct_related_last_mth_p (float | Unset):
        conduct_related_cur_mth_r (float | Unset):
        conduct_related_cur_mth_c (float | Unset):
        conduct_related_cur_mth_p (float | Unset):
        general_bank_last_mth_p (float | Unset):
        general_bank_cur_mth_r (float | Unset):
        general_bank_cur_mth_c (float | Unset):
        general_bank_cur_mth_p (float | Unset):
        total_last_mth_p (float | Unset):
        total_cur_mth_r (float | Unset):
        total_cur_mth_c (float | Unset):
        total_cur_mth_p (float | Unset):
    """

    end_of_month: str | Unset = UNSET
    conduct_related_last_mth_p: float | Unset = UNSET
    conduct_related_cur_mth_r: float | Unset = UNSET
    conduct_related_cur_mth_c: float | Unset = UNSET
    conduct_related_cur_mth_p: float | Unset = UNSET
    general_bank_last_mth_p: float | Unset = UNSET
    general_bank_cur_mth_r: float | Unset = UNSET
    general_bank_cur_mth_c: float | Unset = UNSET
    general_bank_cur_mth_p: float | Unset = UNSET
    total_last_mth_p: float | Unset = UNSET
    total_cur_mth_r: float | Unset = UNSET
    total_cur_mth_c: float | Unset = UNSET
    total_cur_mth_p: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month = self.end_of_month

        conduct_related_last_mth_p = self.conduct_related_last_mth_p

        conduct_related_cur_mth_r = self.conduct_related_cur_mth_r

        conduct_related_cur_mth_c = self.conduct_related_cur_mth_c

        conduct_related_cur_mth_p = self.conduct_related_cur_mth_p

        general_bank_last_mth_p = self.general_bank_last_mth_p

        general_bank_cur_mth_r = self.general_bank_cur_mth_r

        general_bank_cur_mth_c = self.general_bank_cur_mth_c

        general_bank_cur_mth_p = self.general_bank_cur_mth_p

        total_last_mth_p = self.total_last_mth_p

        total_cur_mth_r = self.total_cur_mth_r

        total_cur_mth_c = self.total_cur_mth_c

        total_cur_mth_p = self.total_cur_mth_p

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if conduct_related_last_mth_p is not UNSET:
            field_dict["conduct_related_last_mth_p"] = conduct_related_last_mth_p
        if conduct_related_cur_mth_r is not UNSET:
            field_dict["conduct_related_cur_mth_r"] = conduct_related_cur_mth_r
        if conduct_related_cur_mth_c is not UNSET:
            field_dict["conduct_related_cur_mth_c"] = conduct_related_cur_mth_c
        if conduct_related_cur_mth_p is not UNSET:
            field_dict["conduct_related_cur_mth_p"] = conduct_related_cur_mth_p
        if general_bank_last_mth_p is not UNSET:
            field_dict["general_bank_last_mth_p"] = general_bank_last_mth_p
        if general_bank_cur_mth_r is not UNSET:
            field_dict["general_bank_cur_mth_r"] = general_bank_cur_mth_r
        if general_bank_cur_mth_c is not UNSET:
            field_dict["general_bank_cur_mth_c"] = general_bank_cur_mth_c
        if general_bank_cur_mth_p is not UNSET:
            field_dict["general_bank_cur_mth_p"] = general_bank_cur_mth_p
        if total_last_mth_p is not UNSET:
            field_dict["total_last_mth_p"] = total_last_mth_p
        if total_cur_mth_r is not UNSET:
            field_dict["total_cur_mth_r"] = total_cur_mth_r
        if total_cur_mth_c is not UNSET:
            field_dict["total_cur_mth_c"] = total_cur_mth_c
        if total_cur_mth_p is not UNSET:
            field_dict["total_cur_mth_p"] = total_cur_mth_p

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        end_of_month = d.pop("end_of_month", UNSET)

        conduct_related_last_mth_p = d.pop("conduct_related_last_mth_p", UNSET)

        conduct_related_cur_mth_r = d.pop("conduct_related_cur_mth_r", UNSET)

        conduct_related_cur_mth_c = d.pop("conduct_related_cur_mth_c", UNSET)

        conduct_related_cur_mth_p = d.pop("conduct_related_cur_mth_p", UNSET)

        general_bank_last_mth_p = d.pop("general_bank_last_mth_p", UNSET)

        general_bank_cur_mth_r = d.pop("general_bank_cur_mth_r", UNSET)

        general_bank_cur_mth_c = d.pop("general_bank_cur_mth_c", UNSET)

        general_bank_cur_mth_p = d.pop("general_bank_cur_mth_p", UNSET)

        total_last_mth_p = d.pop("total_last_mth_p", UNSET)

        total_cur_mth_r = d.pop("total_cur_mth_r", UNSET)

        total_cur_mth_c = d.pop("total_cur_mth_c", UNSET)

        total_cur_mth_p = d.pop("total_cur_mth_p", UNSET)

        record = cls(
            end_of_month=end_of_month,
            conduct_related_last_mth_p=conduct_related_last_mth_p,
            conduct_related_cur_mth_r=conduct_related_cur_mth_r,
            conduct_related_cur_mth_c=conduct_related_cur_mth_c,
            conduct_related_cur_mth_p=conduct_related_cur_mth_p,
            general_bank_last_mth_p=general_bank_last_mth_p,
            general_bank_cur_mth_r=general_bank_cur_mth_r,
            general_bank_cur_mth_c=general_bank_cur_mth_c,
            general_bank_cur_mth_p=general_bank_cur_mth_p,
            total_last_mth_p=total_last_mth_p,
            total_cur_mth_r=total_cur_mth_r,
            total_cur_mth_c=total_cur_mth_c,
            total_cur_mth_p=total_cur_mth_p,
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
