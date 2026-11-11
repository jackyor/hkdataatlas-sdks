from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackPositionCollection")


@_attrs_define
class TrackPositionCollection:
    """A grouping of track-position fields. The dictionary describes these tags but does not fully specify XML cardinality
    or exact nesting for repeated positions; the schema therefore leaves the object permissive.

        Attributes:
            index (int | Unset): Sequence number of positions in the tropical cyclone track. Example: 10.
            intensity (str | Unset): If provided, intensity category: Tropical Depression, Tropical Storm, Severe Tropical
                Storm, Typhoon, Severe Typhoon, Super Typhoon, Low Pressure Area, or Extratropical Low. For unnamed cyclones the
                latest intensity category may be used as the cyclone name.
            latitude (str | Unset): Latitude from 0–90N or 0–90S. Positions without a Time tag represent interpolated
                plotting positions; Intensity and MaximumWind do not apply to these positions. Example: 16.70N.
            longitude (str | Unset): Longitude from 0–180E or 0–180W. Positions without a Time tag represent interpolated
                plotting positions; Intensity and MaximumWind do not apply to these positions. Example: 121.10E.
            maximum_wind (str | Unset): If provided, maximum sustained winds near the cyclone centre. The dictionary gives
                example 145km/h. When Intensity is Extratropical Low, the value is --. Example: 145km/h.
            time (str | Unset): If provided, analysed or forecast time in Coordinated Universal Time (UTC). Example:
                2018-10-30T03:00:00+00:00.
    """

    index: int | Unset = UNSET
    intensity: str | Unset = UNSET
    latitude: str | Unset = UNSET
    longitude: str | Unset = UNSET
    maximum_wind: str | Unset = UNSET
    time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        intensity = self.intensity

        latitude = self.latitude

        longitude = self.longitude

        maximum_wind = self.maximum_wind

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["Index"] = index
        if intensity is not UNSET:
            field_dict["Intensity"] = intensity
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if maximum_wind is not UNSET:
            field_dict["MaximumWind"] = maximum_wind
        if time is not UNSET:
            field_dict["Time"] = time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        index = d.pop("Index", UNSET)

        intensity = d.pop("Intensity", UNSET)

        latitude = d.pop("Latitude", UNSET)

        longitude = d.pop("Longitude", UNSET)

        maximum_wind = d.pop("MaximumWind", UNSET)

        time = d.pop("Time", UNSET)

        track_position_collection = cls(
            index=index,
            intensity=intensity,
            latitude=latitude,
            longitude=longitude,
            maximum_wind=maximum_wind,
            time=time,
        )

        track_position_collection.additional_properties = d
        return track_position_collection

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
