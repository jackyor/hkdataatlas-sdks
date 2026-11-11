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
        name_of_building_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_building_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        address_of_building_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_of_building_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        district_of_building_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_of_building_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hour_en (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hour_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    name_of_building_en: None | str | Unset = UNSET
    name_of_building_chi: None | str | Unset = UNSET
    address_of_building_en: None | str | Unset = UNSET
    address_of_building_chi: None | str | Unset = UNSET
    district_of_building_en: None | str | Unset = UNSET
    district_of_building_chi: None | str | Unset = UNSET
    service_hour_en: None | str | Unset = UNSET
    service_hour_chi: None | str | Unset = UNSET
    remark_en: None | str | Unset = UNSET
    remark_chi: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_of_building_en: None | str | Unset
        if isinstance(self.name_of_building_en, Unset):
            name_of_building_en = UNSET
        else:
            name_of_building_en = self.name_of_building_en

        name_of_building_chi: None | str | Unset
        if isinstance(self.name_of_building_chi, Unset):
            name_of_building_chi = UNSET
        else:
            name_of_building_chi = self.name_of_building_chi

        address_of_building_en: None | str | Unset
        if isinstance(self.address_of_building_en, Unset):
            address_of_building_en = UNSET
        else:
            address_of_building_en = self.address_of_building_en

        address_of_building_chi: None | str | Unset
        if isinstance(self.address_of_building_chi, Unset):
            address_of_building_chi = UNSET
        else:
            address_of_building_chi = self.address_of_building_chi

        district_of_building_en: None | str | Unset
        if isinstance(self.district_of_building_en, Unset):
            district_of_building_en = UNSET
        else:
            district_of_building_en = self.district_of_building_en

        district_of_building_chi: None | str | Unset
        if isinstance(self.district_of_building_chi, Unset):
            district_of_building_chi = UNSET
        else:
            district_of_building_chi = self.district_of_building_chi

        service_hour_en: None | str | Unset
        if isinstance(self.service_hour_en, Unset):
            service_hour_en = UNSET
        else:
            service_hour_en = self.service_hour_en

        service_hour_chi: None | str | Unset
        if isinstance(self.service_hour_chi, Unset):
            service_hour_chi = UNSET
        else:
            service_hour_chi = self.service_hour_chi

        remark_en: None | str | Unset
        if isinstance(self.remark_en, Unset):
            remark_en = UNSET
        else:
            remark_en = self.remark_en

        remark_chi: None | str | Unset
        if isinstance(self.remark_chi, Unset):
            remark_chi = UNSET
        else:
            remark_chi = self.remark_chi

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_of_building_en is not UNSET:
            field_dict["Name_of_Building_EN"] = name_of_building_en
        if name_of_building_chi is not UNSET:
            field_dict["Name_of_Building_CHI"] = name_of_building_chi
        if address_of_building_en is not UNSET:
            field_dict["Address_of_Building_EN"] = address_of_building_en
        if address_of_building_chi is not UNSET:
            field_dict["Address_of_Building_CHI"] = address_of_building_chi
        if district_of_building_en is not UNSET:
            field_dict["District_of_Building_EN"] = district_of_building_en
        if district_of_building_chi is not UNSET:
            field_dict["District_of_Building_CHI"] = district_of_building_chi
        if service_hour_en is not UNSET:
            field_dict["Service_Hour_EN"] = service_hour_en
        if service_hour_chi is not UNSET:
            field_dict["Service_Hour_CHI"] = service_hour_chi
        if remark_en is not UNSET:
            field_dict["Remark_EN"] = remark_en
        if remark_chi is not UNSET:
            field_dict["Remark_CHI"] = remark_chi
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_name_of_building_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_building_en = _parse_name_of_building_en(
            d.pop("Name_of_Building_EN", UNSET)
        )

        def _parse_name_of_building_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_building_chi = _parse_name_of_building_chi(
            d.pop("Name_of_Building_CHI", UNSET)
        )

        def _parse_address_of_building_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_building_en = _parse_address_of_building_en(
            d.pop("Address_of_Building_EN", UNSET)
        )

        def _parse_address_of_building_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_building_chi = _parse_address_of_building_chi(
            d.pop("Address_of_Building_CHI", UNSET)
        )

        def _parse_district_of_building_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_of_building_en = _parse_district_of_building_en(
            d.pop("District_of_Building_EN", UNSET)
        )

        def _parse_district_of_building_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_of_building_chi = _parse_district_of_building_chi(
            d.pop("District_of_Building_CHI", UNSET)
        )

        def _parse_service_hour_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hour_en = _parse_service_hour_en(d.pop("Service_Hour_EN", UNSET))

        def _parse_service_hour_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hour_chi = _parse_service_hour_chi(d.pop("Service_Hour_CHI", UNSET))

        def _parse_remark_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_en = _parse_remark_en(d.pop("Remark_EN", UNSET))

        def _parse_remark_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_chi = _parse_remark_chi(d.pop("Remark_CHI", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            name_of_building_en=name_of_building_en,
            name_of_building_chi=name_of_building_chi,
            address_of_building_en=address_of_building_en,
            address_of_building_chi=address_of_building_chi,
            district_of_building_en=district_of_building_en,
            district_of_building_chi=district_of_building_chi,
            service_hour_en=service_hour_en,
            service_hour_chi=service_hour_chi,
            remark_en=remark_en,
            remark_chi=remark_chi,
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
