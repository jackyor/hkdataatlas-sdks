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
        fax_number (None | str | Unset): Publisher field type: esriFieldTypeString
        inclement_weather_special_arrangements (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_number (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address: None | str | Unset = UNSET
    fax_number: None | str | Unset = UNSET
    inclement_weather_special_arrangements: None | str | Unset = UNSET
    opening_hours: None | str | Unset = UNSET
    telephone_number: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        fax_number: None | str | Unset
        if isinstance(self.fax_number, Unset):
            fax_number = UNSET
        else:
            fax_number = self.fax_number

        inclement_weather_special_arrangements: None | str | Unset
        if isinstance(self.inclement_weather_special_arrangements, Unset):
            inclement_weather_special_arrangements = UNSET
        else:
            inclement_weather_special_arrangements = (
                self.inclement_weather_special_arrangements
            )

        opening_hours: None | str | Unset
        if isinstance(self.opening_hours, Unset):
            opening_hours = UNSET
        else:
            opening_hours = self.opening_hours

        telephone_number: None | str | Unset
        if isinstance(self.telephone_number, Unset):
            telephone_number = UNSET
        else:
            telephone_number = self.telephone_number

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if fax_number is not UNSET:
            field_dict["Fax_number"] = fax_number
        if inclement_weather_special_arrangements is not UNSET:
            field_dict["Inclement_weather_special_arrangements"] = (
                inclement_weather_special_arrangements
            )
        if opening_hours is not UNSET:
            field_dict["Opening_hours"] = opening_hours
        if telephone_number is not UNSET:
            field_dict["Telephone_number"] = telephone_number
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

        def _parse_fax_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number = _parse_fax_number(d.pop("Fax_number", UNSET))

        def _parse_inclement_weather_special_arrangements(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        inclement_weather_special_arrangements = (
            _parse_inclement_weather_special_arrangements(
                d.pop("Inclement_weather_special_arrangements", UNSET)
            )
        )

        def _parse_opening_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours = _parse_opening_hours(d.pop("Opening_hours", UNSET))

        def _parse_telephone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_number = _parse_telephone_number(d.pop("Telephone_number", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address=address,
            fax_number=fax_number,
            inclement_weather_special_arrangements=inclement_weather_special_arrangements,
            opening_hours=opening_hours,
            telephone_number=telephone_number,
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
