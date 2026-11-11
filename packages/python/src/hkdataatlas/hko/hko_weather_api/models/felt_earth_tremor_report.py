from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FeltEarthTremorReport")


@_attrs_define
class FeltEarthTremorReport:
    """Locally Felt Earth Tremor Report (feltearthquake).

    Attributes:
        details (str | Unset): Earthquake details.
        intensity (str | Unset): Intensity of the earthquake.
        lat (float | Unset): Latitude.
        lon (float | Unset): Longitude.
        mag (float | Unset): Richter magnitude scale.
        ptime (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
        region (str | Unset): Region of the earthquake.
        update_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
    """

    details: str | Unset = UNSET
    intensity: str | Unset = UNSET
    lat: float | Unset = UNSET
    lon: float | Unset = UNSET
    mag: float | Unset = UNSET
    ptime: str | Unset = UNSET
    region: str | Unset = UNSET
    update_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        details = self.details

        intensity = self.intensity

        lat = self.lat

        lon = self.lon

        mag = self.mag

        ptime = self.ptime

        region = self.region

        update_time = self.update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if details is not UNSET:
            field_dict["details"] = details
        if intensity is not UNSET:
            field_dict["intensity"] = intensity
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
        details = d.pop("details", UNSET)

        intensity = d.pop("intensity", UNSET)

        lat = d.pop("lat", UNSET)

        lon = d.pop("lon", UNSET)

        mag = d.pop("mag", UNSET)

        ptime = d.pop("ptime", UNSET)

        region = d.pop("region", UNSET)

        update_time = d.pop("updateTime", UNSET)

        felt_earth_tremor_report = cls(
            details=details,
            intensity=intensity,
            lat=lat,
            lon=lon,
            mag=mag,
            ptime=ptime,
            region=region,
            update_time=update_time,
        )

        felt_earth_tremor_report.additional_properties = d
        return felt_earth_tremor_report

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
