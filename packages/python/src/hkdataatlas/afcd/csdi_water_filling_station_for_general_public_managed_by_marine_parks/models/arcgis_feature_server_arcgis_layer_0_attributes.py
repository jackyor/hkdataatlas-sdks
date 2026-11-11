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
        name_of_facility_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_facility_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        address_of_facility_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_of_facility_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        address_of_facility_district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_of_facility_district_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        address_of_facility_region_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_of_facility_region_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        location_of_facility_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_of_facility_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    name_of_facility_en: None | str | Unset = UNSET
    name_of_facility_chi: None | str | Unset = UNSET
    address_of_facility_en: None | str | Unset = UNSET
    address_of_facility_chi: None | str | Unset = UNSET
    address_of_facility_district_en: None | str | Unset = UNSET
    address_of_facility_district_chi: None | str | Unset = UNSET
    address_of_facility_region_en: None | str | Unset = UNSET
    address_of_facility_region_chi: None | str | Unset = UNSET
    location_of_facility_en: None | str | Unset = UNSET
    location_of_facility_chi: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_of_facility_en: None | str | Unset
        if isinstance(self.name_of_facility_en, Unset):
            name_of_facility_en = UNSET
        else:
            name_of_facility_en = self.name_of_facility_en

        name_of_facility_chi: None | str | Unset
        if isinstance(self.name_of_facility_chi, Unset):
            name_of_facility_chi = UNSET
        else:
            name_of_facility_chi = self.name_of_facility_chi

        address_of_facility_en: None | str | Unset
        if isinstance(self.address_of_facility_en, Unset):
            address_of_facility_en = UNSET
        else:
            address_of_facility_en = self.address_of_facility_en

        address_of_facility_chi: None | str | Unset
        if isinstance(self.address_of_facility_chi, Unset):
            address_of_facility_chi = UNSET
        else:
            address_of_facility_chi = self.address_of_facility_chi

        address_of_facility_district_en: None | str | Unset
        if isinstance(self.address_of_facility_district_en, Unset):
            address_of_facility_district_en = UNSET
        else:
            address_of_facility_district_en = self.address_of_facility_district_en

        address_of_facility_district_chi: None | str | Unset
        if isinstance(self.address_of_facility_district_chi, Unset):
            address_of_facility_district_chi = UNSET
        else:
            address_of_facility_district_chi = self.address_of_facility_district_chi

        address_of_facility_region_en: None | str | Unset
        if isinstance(self.address_of_facility_region_en, Unset):
            address_of_facility_region_en = UNSET
        else:
            address_of_facility_region_en = self.address_of_facility_region_en

        address_of_facility_region_chi: None | str | Unset
        if isinstance(self.address_of_facility_region_chi, Unset):
            address_of_facility_region_chi = UNSET
        else:
            address_of_facility_region_chi = self.address_of_facility_region_chi

        location_of_facility_en: None | str | Unset
        if isinstance(self.location_of_facility_en, Unset):
            location_of_facility_en = UNSET
        else:
            location_of_facility_en = self.location_of_facility_en

        location_of_facility_chi: None | str | Unset
        if isinstance(self.location_of_facility_chi, Unset):
            location_of_facility_chi = UNSET
        else:
            location_of_facility_chi = self.location_of_facility_chi

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_of_facility_en is not UNSET:
            field_dict["NAME_OF_FACILITY_EN"] = name_of_facility_en
        if name_of_facility_chi is not UNSET:
            field_dict["NAME_OF_FACILITY_CHI"] = name_of_facility_chi
        if address_of_facility_en is not UNSET:
            field_dict["ADDRESS_OF_FACILITY_EN"] = address_of_facility_en
        if address_of_facility_chi is not UNSET:
            field_dict["ADDRESS_OF_FACILITY_CHI"] = address_of_facility_chi
        if address_of_facility_district_en is not UNSET:
            field_dict["ADDRESS_OF_FACILITY_DISTRICT_EN"] = (
                address_of_facility_district_en
            )
        if address_of_facility_district_chi is not UNSET:
            field_dict["ADDRESS_OF_FACILITY_DISTRICT_CHI"] = (
                address_of_facility_district_chi
            )
        if address_of_facility_region_en is not UNSET:
            field_dict["ADDRESS_OF_FACILITY_REGION_EN"] = address_of_facility_region_en
        if address_of_facility_region_chi is not UNSET:
            field_dict["ADDRESS_OF_FACILITY_REGION_CHI"] = (
                address_of_facility_region_chi
            )
        if location_of_facility_en is not UNSET:
            field_dict["LOCATION_OF_FACILITY_EN"] = location_of_facility_en
        if location_of_facility_chi is not UNSET:
            field_dict["LOCATION_OF_FACILITY_CHI"] = location_of_facility_chi
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_name_of_facility_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_facility_en = _parse_name_of_facility_en(
            d.pop("NAME_OF_FACILITY_EN", UNSET)
        )

        def _parse_name_of_facility_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_facility_chi = _parse_name_of_facility_chi(
            d.pop("NAME_OF_FACILITY_CHI", UNSET)
        )

        def _parse_address_of_facility_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_facility_en = _parse_address_of_facility_en(
            d.pop("ADDRESS_OF_FACILITY_EN", UNSET)
        )

        def _parse_address_of_facility_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_facility_chi = _parse_address_of_facility_chi(
            d.pop("ADDRESS_OF_FACILITY_CHI", UNSET)
        )

        def _parse_address_of_facility_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_facility_district_en = _parse_address_of_facility_district_en(
            d.pop("ADDRESS_OF_FACILITY_DISTRICT_EN", UNSET)
        )

        def _parse_address_of_facility_district_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_facility_district_chi = _parse_address_of_facility_district_chi(
            d.pop("ADDRESS_OF_FACILITY_DISTRICT_CHI", UNSET)
        )

        def _parse_address_of_facility_region_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_facility_region_en = _parse_address_of_facility_region_en(
            d.pop("ADDRESS_OF_FACILITY_REGION_EN", UNSET)
        )

        def _parse_address_of_facility_region_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_facility_region_chi = _parse_address_of_facility_region_chi(
            d.pop("ADDRESS_OF_FACILITY_REGION_CHI", UNSET)
        )

        def _parse_location_of_facility_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_of_facility_en = _parse_location_of_facility_en(
            d.pop("LOCATION_OF_FACILITY_EN", UNSET)
        )

        def _parse_location_of_facility_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_of_facility_chi = _parse_location_of_facility_chi(
            d.pop("LOCATION_OF_FACILITY_CHI", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            name_of_facility_en=name_of_facility_en,
            name_of_facility_chi=name_of_facility_chi,
            address_of_facility_en=address_of_facility_en,
            address_of_facility_chi=address_of_facility_chi,
            address_of_facility_district_en=address_of_facility_district_en,
            address_of_facility_district_chi=address_of_facility_district_chi,
            address_of_facility_region_en=address_of_facility_region_en,
            address_of_facility_region_chi=address_of_facility_region_chi,
            location_of_facility_en=location_of_facility_en,
            location_of_facility_chi=location_of_facility_chi,
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
