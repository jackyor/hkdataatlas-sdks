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
        type_of_machine (str | Unset):
        function (str | Unset):
        currencies_supported (str | Unset):
        barrier_free_access (str | Unset):
        network (str | Unset):
        address (str | Unset):
        service_hours (str | Unset):
        latitude (float | str | Unset): Compatibility with publisherdocumented numbers and observed string
            representation. Values remain numbers or strings exactly as returned.
        longitude (float | str | Unset): Compatibility with publisherdocumented numbers and observed string
            representation. Values remain numbers or strings exactly as returned.
    """

    district: str | Unset = UNSET
    bank_name: str | Unset = UNSET
    type_of_machine: str | Unset = UNSET
    function: str | Unset = UNSET
    currencies_supported: str | Unset = UNSET
    barrier_free_access: str | Unset = UNSET
    network: str | Unset = UNSET
    address: str | Unset = UNSET
    service_hours: str | Unset = UNSET
    latitude: float | str | Unset = UNSET
    longitude: float | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        district = self.district

        bank_name = self.bank_name

        type_of_machine = self.type_of_machine

        function = self.function

        currencies_supported = self.currencies_supported

        barrier_free_access = self.barrier_free_access

        network = self.network

        address = self.address

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if district is not UNSET:
            field_dict["district"] = district
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if type_of_machine is not UNSET:
            field_dict["type_of_machine"] = type_of_machine
        if function is not UNSET:
            field_dict["function"] = function
        if currencies_supported is not UNSET:
            field_dict["currencies_supported"] = currencies_supported
        if barrier_free_access is not UNSET:
            field_dict["barrier-free_access"] = barrier_free_access
        if network is not UNSET:
            field_dict["network"] = network
        if address is not UNSET:
            field_dict["address"] = address
        if service_hours is not UNSET:
            field_dict["service_hours"] = service_hours
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        district = d.pop("district", UNSET)

        bank_name = d.pop("bank_name", UNSET)

        type_of_machine = d.pop("type_of_machine", UNSET)

        function = d.pop("function", UNSET)

        currencies_supported = d.pop("currencies_supported", UNSET)

        barrier_free_access = d.pop("barrier-free_access", UNSET)

        network = d.pop("network", UNSET)

        address = d.pop("address", UNSET)

        service_hours = d.pop("service_hours", UNSET)

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

        record = cls(
            district=district,
            bank_name=bank_name,
            type_of_machine=type_of_machine,
            function=function,
            currencies_supported=currencies_supported,
            barrier_free_access=barrier_free_access,
            network=network,
            address=address,
            service_hours=service_hours,
            latitude=latitude,
            longitude=longitude,
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
