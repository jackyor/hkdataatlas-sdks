from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eng_phase import EngPhase


T = TypeVar("T", bound="EngEstate")


@_attrs_define
class EngEstate:
    """Estate name and related information in English.

    Attributes:
        eng_phase (EngPhase | Unset): Phase name and phase number information in English.
        estate_name (str | Unset): Estate name in English.
    """

    eng_phase: EngPhase | Unset = UNSET
    estate_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eng_phase: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_phase, Unset):
            eng_phase = self.eng_phase.to_dict()

        estate_name = self.estate_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eng_phase is not UNSET:
            field_dict["EngPhase"] = eng_phase
        if estate_name is not UNSET:
            field_dict["EstateName"] = estate_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eng_phase import EngPhase

        d = dict(src_dict)
        _eng_phase = d.pop("EngPhase", UNSET)
        eng_phase: EngPhase | Unset
        if isinstance(_eng_phase, Unset):
            eng_phase = UNSET
        else:
            eng_phase = EngPhase.from_dict(_eng_phase)

        estate_name = d.pop("EstateName", UNSET)

        eng_estate = cls(
            eng_phase=eng_phase,
            estate_name=estate_name,
        )

        eng_estate.additional_properties = d
        return eng_estate

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
