from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.coordinates import Coordinates


T = TypeVar("T", bound="StopCoordinates")


@_attrs_define
class StopCoordinates:
    """Stop position in different coordinate reference systems.

    Attributes:
        hk80 (Coordinates | Unset): Coordinate values for a coordinate reference system.
        wgs84 (Coordinates | Unset): Coordinate values for a coordinate reference system.
    """

    hk80: Coordinates | Unset = UNSET
    wgs84: Coordinates | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hk80: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hk80, Unset):
            hk80 = self.hk80.to_dict()

        wgs84: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wgs84, Unset):
            wgs84 = self.wgs84.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hk80 is not UNSET:
            field_dict["hk80"] = hk80
        if wgs84 is not UNSET:
            field_dict["wgs84"] = wgs84

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.coordinates import Coordinates

        d = dict(src_dict)
        _hk80 = d.pop("hk80", UNSET)
        hk80: Coordinates | Unset
        if isinstance(_hk80, Unset):
            hk80 = UNSET
        else:
            hk80 = Coordinates.from_dict(_hk80)

        _wgs84 = d.pop("wgs84", UNSET)
        wgs84: Coordinates | Unset
        if isinstance(_wgs84, Unset):
            wgs84 = UNSET
        else:
            wgs84 = Coordinates.from_dict(_wgs84)

        stop_coordinates = cls(
            hk80=hk80,
            wgs84=wgs84,
        )

        stop_coordinates.additional_properties = d
        return stop_coordinates

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
