from __future__ import annotations

import datetime
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
        glr_yr (datetime.date | Unset):
        glr_rents_a (float | Unset):
        glr_prem_a (float | Unset):
        glr_other_a (float | Unset):
        glr_plesd_a (float | Unset):
        glr_pldep_a (float | Unset):
        glr_plefe_a (float | Unset):
        glr_recrhk_a (float | Unset):
        glr_recrnt_a (float | Unset):
        glr_relchi_a (float | Unset):
    """

    glr_yr: datetime.date | Unset = UNSET
    glr_rents_a: float | Unset = UNSET
    glr_prem_a: float | Unset = UNSET
    glr_other_a: float | Unset = UNSET
    glr_plesd_a: float | Unset = UNSET
    glr_pldep_a: float | Unset = UNSET
    glr_plefe_a: float | Unset = UNSET
    glr_recrhk_a: float | Unset = UNSET
    glr_recrnt_a: float | Unset = UNSET
    glr_relchi_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        glr_yr: str | Unset = UNSET
        if not isinstance(self.glr_yr, Unset):
            glr_yr = self.glr_yr.isoformat()

        glr_rents_a = self.glr_rents_a

        glr_prem_a = self.glr_prem_a

        glr_other_a = self.glr_other_a

        glr_plesd_a = self.glr_plesd_a

        glr_pldep_a = self.glr_pldep_a

        glr_plefe_a = self.glr_plefe_a

        glr_recrhk_a = self.glr_recrhk_a

        glr_recrnt_a = self.glr_recrnt_a

        glr_relchi_a = self.glr_relchi_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if glr_yr is not UNSET:
            field_dict["Glr_yr"] = glr_yr
        if glr_rents_a is not UNSET:
            field_dict["Glr_rents_a"] = glr_rents_a
        if glr_prem_a is not UNSET:
            field_dict["Glr_prem_a"] = glr_prem_a
        if glr_other_a is not UNSET:
            field_dict["Glr_other_a"] = glr_other_a
        if glr_plesd_a is not UNSET:
            field_dict["Glr_plesd_a"] = glr_plesd_a
        if glr_pldep_a is not UNSET:
            field_dict["Glr_pldep_a"] = glr_pldep_a
        if glr_plefe_a is not UNSET:
            field_dict["Glr_plefe_a"] = glr_plefe_a
        if glr_recrhk_a is not UNSET:
            field_dict["Glr_recrhk_a"] = glr_recrhk_a
        if glr_recrnt_a is not UNSET:
            field_dict["Glr_recrnt_a"] = glr_recrnt_a
        if glr_relchi_a is not UNSET:
            field_dict["Glr_relchi_a"] = glr_relchi_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _glr_yr = d.pop("Glr_yr", UNSET)
        glr_yr: datetime.date | Unset
        if isinstance(_glr_yr, Unset):
            glr_yr = UNSET
        else:
            glr_yr = datetime.date.fromisoformat(_glr_yr)

        glr_rents_a = d.pop("Glr_rents_a", UNSET)

        glr_prem_a = d.pop("Glr_prem_a", UNSET)

        glr_other_a = d.pop("Glr_other_a", UNSET)

        glr_plesd_a = d.pop("Glr_plesd_a", UNSET)

        glr_pldep_a = d.pop("Glr_pldep_a", UNSET)

        glr_plefe_a = d.pop("Glr_plefe_a", UNSET)

        glr_recrhk_a = d.pop("Glr_recrhk_a", UNSET)

        glr_recrnt_a = d.pop("Glr_recrnt_a", UNSET)

        glr_relchi_a = d.pop("Glr_relchi_a", UNSET)

        record = cls(
            glr_yr=glr_yr,
            glr_rents_a=glr_rents_a,
            glr_prem_a=glr_prem_a,
            glr_other_a=glr_other_a,
            glr_plesd_a=glr_plesd_a,
            glr_pldep_a=glr_pldep_a,
            glr_plefe_a=glr_plefe_a,
            glr_recrhk_a=glr_recrhk_a,
            glr_recrnt_a=glr_recrnt_a,
            glr_relchi_a=glr_relchi_a,
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
