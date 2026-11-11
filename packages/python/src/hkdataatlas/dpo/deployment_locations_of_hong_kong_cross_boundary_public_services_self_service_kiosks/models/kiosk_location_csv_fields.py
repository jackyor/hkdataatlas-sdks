from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KioskLocationCsvFields")


@_attrs_define
class KioskLocationCsvFields:
    """Field dictionary for the CSV dataset; these fields describe CSV columns, not a guaranteed API response schema.

    Attributes:
        address (str | Unset): Address of the Hong Kong Cross-boundary Public Services self-service kiosk.
        latitude (float | Unset): Latitude of the Hong Kong Cross-boundary Public Services self-service kiosk.
        location (str | Unset): Location of the Hong Kong Cross-boundary Public Services self-service kiosk.
        longitude (float | Unset): Longitude of the Hong Kong Cross-boundary Public Services self-service kiosk.
        opening_hours (str | Unset): Opening hours of the Hong Kong Cross-boundary Public Services self-service kiosk.
    """

    address: str | Unset = UNSET
    latitude: float | Unset = UNSET
    location: str | Unset = UNSET
    longitude: float | Unset = UNSET
    opening_hours: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        latitude = self.latitude

        location = self.location

        longitude = self.longitude

        opening_hours = self.opening_hours

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if location is not UNSET:
            field_dict["Location"] = location
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if opening_hours is not UNSET:
            field_dict["Opening Hours"] = opening_hours

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address = d.pop("Address", UNSET)

        latitude = d.pop("Latitude", UNSET)

        location = d.pop("Location", UNSET)

        longitude = d.pop("Longitude", UNSET)

        opening_hours = d.pop("Opening Hours", UNSET)

        kiosk_location_csv_fields = cls(
            address=address,
            latitude=latitude,
            location=location,
            longitude=longitude,
            opening_hours=opening_hours,
        )

        kiosk_location_csv_fields.additional_properties = d
        return kiosk_location_csv_fields

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
