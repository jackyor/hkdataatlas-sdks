from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        district (str | Unset):
        bank_name (str | Unset):
        branch_name (str | Unset):
        address (str | Unset):
        service_hours (None | str | Unset):
        latitude (float | str | Unset): Upstream documents a number; the preserved live sample uses a numeric decimal
            string. This derivative accepts both evidenced representations without response coercion.
        longitude (float | str | Unset): Upstream documents a number; the preserved live sample uses a numeric decimal
            string. This derivative accepts both evidenced representations without response coercion.
        barrier_free_access (None | str | Unset):
    """

    district: str | Unset = UNSET
    bank_name: str | Unset = UNSET
    branch_name: str | Unset = UNSET
    address: str | Unset = UNSET
    service_hours: None | str | Unset = UNSET
    latitude: float | str | Unset = UNSET
    longitude: float | str | Unset = UNSET
    barrier_free_access: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        district = self.district

        bank_name = self.bank_name

        branch_name = self.branch_name

        address = self.address

        service_hours: None | str | Unset
        if isinstance(self.service_hours, Unset):
            service_hours = UNSET
        else:
            service_hours = self.service_hours

        latitude: float | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        barrier_free_access: None | str | Unset
        if isinstance(self.barrier_free_access, Unset):
            barrier_free_access = UNSET
        else:
            barrier_free_access = self.barrier_free_access

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if district is not UNSET:
            field_dict["district"] = district
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if branch_name is not UNSET:
            field_dict["branch_name"] = branch_name
        if address is not UNSET:
            field_dict["address"] = address
        if service_hours is not UNSET:
            field_dict["service_hours"] = service_hours
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if barrier_free_access is not UNSET:
            field_dict["barrier-free_access"] = barrier_free_access

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        district = d.pop("district", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        branch_name = d.pop("branch_name", UNSET)

        address = d.pop("address", UNSET)

        def _parse_service_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours = _parse_service_hours(d.pop("service_hours", UNSET))

        def _parse_latitude(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_barrier_free_access(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barrier_free_access = _parse_barrier_free_access(
            d.pop("barrier-free_access", UNSET)
        )

        record = cls(
            district=district,
            bank_name=bank_name,
            branch_name=branch_name,
            address=address,
            service_hours=service_hours,
            latitude=latitude,
            longitude=longitude,
            barrier_free_access=barrier_free_access,
        )

        record.additional_properties = d
        return record

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
