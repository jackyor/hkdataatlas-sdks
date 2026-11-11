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
        address_cn (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_zh (None | str | Unset): Publisher field type: esriFieldTypeString
        name_cn (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_zh (None | str | Unset): Publisher field type: esriFieldTypeString
        phone_number (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_cn: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_zh: None | str | Unset = UNSET
    name_cn: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_zh: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_cn: None | str | Unset
        if isinstance(self.address_cn, Unset):
            address_cn = UNSET
        else:
            address_cn = self.address_cn

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_zh: None | str | Unset
        if isinstance(self.address_zh, Unset):
            address_zh = UNSET
        else:
            address_zh = self.address_zh

        name_cn: None | str | Unset
        if isinstance(self.name_cn, Unset):
            name_cn = UNSET
        else:
            name_cn = self.name_cn

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_zh: None | str | Unset
        if isinstance(self.name_zh, Unset):
            name_zh = UNSET
        else:
            name_zh = self.name_zh

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_cn is not UNSET:
            field_dict["Address_CN"] = address_cn
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_zh is not UNSET:
            field_dict["Address_ZH"] = address_zh
        if name_cn is not UNSET:
            field_dict["Name_CN"] = name_cn
        if name_en is not UNSET:
            field_dict["Name_EN"] = name_en
        if name_zh is not UNSET:
            field_dict["Name_ZH"] = name_zh
        if phone_number is not UNSET:
            field_dict["PhoneNumber"] = phone_number
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_cn = _parse_address_cn(d.pop("Address_CN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_zh = _parse_address_zh(d.pop("Address_ZH", UNSET))

        def _parse_name_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_cn = _parse_name_cn(d.pop("Name_CN", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("Name_EN", UNSET))

        def _parse_name_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_zh = _parse_name_zh(d.pop("Name_ZH", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("PhoneNumber", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_cn=address_cn,
            address_en=address_en,
            address_zh=address_zh,
            name_cn=name_cn,
            name_en=name_en,
            name_zh=name_zh,
            phone_number=phone_number,
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
