from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GracePeriod")


@_attrs_define
class GracePeriod:
    """
    Attributes:
        minutes (float): Number of minutes the user may park for free.
        remark (str | Unset): Condition to which this grace period applies; localized responses provide the remark in
            the specified locale.
    """

    minutes: float
    remark: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        minutes = self.minutes

        remark = self.remark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "minutes": minutes,
            }
        )
        if remark is not UNSET:
            field_dict["remark"] = remark

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        minutes = d.pop("minutes")

        remark = d.pop("remark", UNSET)

        grace_period = cls(
            minutes=minutes,
            remark=remark,
        )

        grace_period.additional_properties = d
        return grace_period

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
