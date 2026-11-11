from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeospatialInformation")


@_attrs_define
class GeospatialInformation:
    """Geospatial information for an address. The companion XML schema describes these values as text; its maximum-length
    restrictions are included.

        Attributes:
            easting (str | Unset): Easting value of HK1980 Grid Coordinates.
            latitude (str | Unset): Latitude degree value of WGS84 Geographical Coordinates.
            longitude (str | Unset): Longitude degree value of WGS84 Geographical Coordinates.
            northing (str | Unset): Northing value of HK1980 Grid Coordinates.
    """

    easting: str | Unset = UNSET
    latitude: str | Unset = UNSET
    longitude: str | Unset = UNSET
    northing: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        easting = self.easting

        latitude = self.latitude

        longitude = self.longitude

        northing = self.northing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if northing is not UNSET:
            field_dict["Northing"] = northing

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        easting = d.pop("Easting", UNSET)

        latitude = d.pop("Latitude", UNSET)

        longitude = d.pop("Longitude", UNSET)

        northing = d.pop("Northing", UNSET)

        geospatial_information = cls(
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            northing=northing,
        )

        geospatial_information.additional_properties = d
        return geospatial_information

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
