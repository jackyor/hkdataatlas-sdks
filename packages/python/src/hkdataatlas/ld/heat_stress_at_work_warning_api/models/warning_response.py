from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.heat_stress_at_work_warning import HeatStressAtWorkWarning


T = TypeVar("T", bound="WarningResponse")


@_attrs_define
class WarningResponse:
    """Response object shown when HSWW is issued or within the documented 60-minute period after cancellation.

    Attributes:
        hsww (HeatStressAtWorkWarning | Unset): Heat Stress at Work Warning object.
    """

    hsww: HeatStressAtWorkWarning | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hsww: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hsww, Unset):
            hsww = self.hsww.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hsww is not UNSET:
            field_dict["hsww"] = hsww

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.heat_stress_at_work_warning import HeatStressAtWorkWarning

        d = dict(src_dict)
        _hsww = d.pop("hsww", UNSET)
        hsww: HeatStressAtWorkWarning | Unset
        if isinstance(_hsww, Unset):
            hsww = UNSET
        else:
            hsww = HeatStressAtWorkWarning.from_dict(_hsww)

        warning_response = cls(
            hsww=hsww,
        )

        warning_response.additional_properties = d
        return warning_response

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
