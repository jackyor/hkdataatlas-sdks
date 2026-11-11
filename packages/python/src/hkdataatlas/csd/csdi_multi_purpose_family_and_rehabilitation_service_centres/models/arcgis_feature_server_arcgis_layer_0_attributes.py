from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        address (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours (None | str | Unset): Publisher field type: esriFieldTypeString
        service_centres (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_numbers (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address: None | str | Unset = UNSET
    opening_hours: None | str | Unset = UNSET
    service_centres: None | str | Unset = UNSET
    telephone_numbers: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        opening_hours: None | str | Unset
        if isinstance(self.opening_hours, Unset):
            opening_hours = UNSET
        else:
            opening_hours = self.opening_hours

        service_centres: None | str | Unset
        if isinstance(self.service_centres, Unset):
            service_centres = UNSET
        else:
            service_centres = self.service_centres

        telephone_numbers: None | str | Unset
        if isinstance(self.telephone_numbers, Unset):
            telephone_numbers = UNSET
        else:
            telephone_numbers = self.telephone_numbers

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if opening_hours is not UNSET:
            field_dict["Opening_hours"] = opening_hours
        if service_centres is not UNSET:
            field_dict["Service_centres"] = service_centres
        if telephone_numbers is not UNSET:
            field_dict["Telephone_numbers"] = telephone_numbers
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("Address", UNSET))

        def _parse_opening_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours = _parse_opening_hours(d.pop("Opening_hours", UNSET))

        def _parse_service_centres(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_centres = _parse_service_centres(d.pop("Service_centres", UNSET))

        def _parse_telephone_numbers(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_numbers = _parse_telephone_numbers(d.pop("Telephone_numbers", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address=address,
            opening_hours=opening_hours,
            service_centres=service_centres,
            telephone_numbers=telephone_numbers,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
