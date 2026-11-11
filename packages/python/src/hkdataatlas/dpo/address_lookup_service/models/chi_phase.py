from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChiPhase")


@_attrs_define
class ChiPhase:
    """
    Attributes:
        phase_name (str | Unset):
        phase_no (float | Unset): Phase number.
    """

    phase_name: str | Unset = UNSET
    phase_no: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phase_name = self.phase_name

        phase_no = self.phase_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase_name is not UNSET:
            field_dict["PhaseName"] = phase_name
        if phase_no is not UNSET:
            field_dict["PhaseNo"] = phase_no

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        phase_name = d.pop("PhaseName", UNSET)

        phase_no = d.pop("PhaseNo", UNSET)

        chi_phase = cls(
            phase_name=phase_name,
            phase_no=phase_no,
        )

        chi_phase.additional_properties = d
        return chi_phase

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
