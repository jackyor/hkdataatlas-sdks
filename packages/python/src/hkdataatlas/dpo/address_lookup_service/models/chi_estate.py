from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chi_phase import ChiPhase


T = TypeVar("T", bound="ChiEstate")


@_attrs_define
class ChiEstate:
    """Estate name and related information in Chinese.

    Attributes:
        chi_phase (ChiPhase | Unset):
        estate_name (str | Unset):
    """

    chi_phase: ChiPhase | Unset = UNSET
    estate_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chi_phase: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_phase, Unset):
            chi_phase = self.chi_phase.to_dict()

        estate_name = self.estate_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chi_phase is not UNSET:
            field_dict["ChiPhase"] = chi_phase
        if estate_name is not UNSET:
            field_dict["EstateName"] = estate_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.chi_phase import ChiPhase

        d = dict(src_dict)
        _chi_phase = d.pop("ChiPhase", UNSET)
        chi_phase: ChiPhase | Unset
        if isinstance(_chi_phase, Unset):
            chi_phase = UNSET
        else:
            chi_phase = ChiPhase.from_dict(_chi_phase)

        estate_name = d.pop("EstateName", UNSET)

        chi_estate = cls(
            chi_phase=chi_phase,
            estate_name=estate_name,
        )

        chi_estate.additional_properties = d
        return chi_estate

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
