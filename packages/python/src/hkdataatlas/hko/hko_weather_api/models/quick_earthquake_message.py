from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuickEarthquakeMessage")


@_attrs_define
class QuickEarthquakeMessage:
    """Quick Earthquake Messages (qem).

    Attributes:
        lat (float | Unset): Latitude.
        lon (float | Unset): Longitude.
        mag (float | Unset): Richter magnitude scale.
        ptime (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
        region (str | Unset): Region.
        update_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
    """

    lat: float | Unset = UNSET
    lon: float | Unset = UNSET
    mag: float | Unset = UNSET
    ptime: str | Unset = UNSET
    region: str | Unset = UNSET
    update_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lat = self.lat

        lon = self.lon

        mag = self.mag

        ptime = self.ptime

        region = self.region

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lon is not UNSET:
            field_dict["lon"] = lon
        if mag is not UNSET:
            field_dict["mag"] = mag
        if ptime is not UNSET:
            field_dict["ptime"] = ptime
        if region is not UNSET:
            field_dict["region"] = region
        if update_time is not UNSET:
            field_dict["updateTime"] = update_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lat = d.pop("lat", UNSET)

        lon = d.pop("lon", UNSET)

        mag = d.pop("mag", UNSET)

        ptime = d.pop("ptime", UNSET)

        region = d.pop("region", UNSET)

        update_time = d.pop("updateTime", UNSET)

        quick_earthquake_message = cls(
            lat=lat,
            lon=lon,
            mag=mag,
            ptime=ptime,
            region=region,
            update_time=update_time,
        )

        quick_earthquake_message.additional_properties = d
        return quick_earthquake_message

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
