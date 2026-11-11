from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusSearch")


@_attrs_define
class RadiusSearch:
    """
    Attributes:
        lat (float): Latitude in decimal degrees (WGS84). Example: 22.291563.
        long (float): Longitude in decimal degrees (WGS84). Example: 114.301471.
        range_ (int | Unset): Search radius in metres. Default: 2000 (2 km). Default: 2000. Example: 1000.
    """

    lat: float
    long: float
    range_: int | Unset = 2000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lat = self.lat

        long = self.long

        range_ = self.range_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lat": lat,
                "long": long,
            }
        )
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lat = d.pop("lat")

        long = d.pop("long")

        range_ = d.pop("range", UNSET)

        radius_search = cls(
            lat=lat,
            long=long,
            range_=range_,
        )

        radius_search.additional_properties = d
        return radius_search

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
