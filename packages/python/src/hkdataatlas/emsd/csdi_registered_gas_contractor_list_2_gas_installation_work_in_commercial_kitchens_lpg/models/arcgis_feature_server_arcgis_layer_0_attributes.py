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
        address_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        address_english (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_company_name (None | str | Unset): Publisher field type: esriFieldTypeString
        company_telephone_no (None | str | Unset): Publisher field type: esriFieldTypeString
        english_company_name (None | str | Unset): Publisher field type: esriFieldTypeString
        rgc_no (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_chinese: None | str | Unset = UNSET
    address_english: None | str | Unset = UNSET
    chinese_company_name: None | str | Unset = UNSET
    company_telephone_no: None | str | Unset = UNSET
    english_company_name: None | str | Unset = UNSET
    rgc_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_chinese: None | str | Unset
        if isinstance(self.address_chinese, Unset):
            address_chinese = UNSET
        else:
            address_chinese = self.address_chinese

        address_english: None | str | Unset
        if isinstance(self.address_english, Unset):
            address_english = UNSET
        else:
            address_english = self.address_english

        chinese_company_name: None | str | Unset
        if isinstance(self.chinese_company_name, Unset):
            chinese_company_name = UNSET
        else:
            chinese_company_name = self.chinese_company_name

        company_telephone_no: None | str | Unset
        if isinstance(self.company_telephone_no, Unset):
            company_telephone_no = UNSET
        else:
            company_telephone_no = self.company_telephone_no

        english_company_name: None | str | Unset
        if isinstance(self.english_company_name, Unset):
            english_company_name = UNSET
        else:
            english_company_name = self.english_company_name

        rgc_no: None | str | Unset
        if isinstance(self.rgc_no, Unset):
            rgc_no = UNSET
        else:
            rgc_no = self.rgc_no

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_chinese is not UNSET:
            field_dict["Address_Chinese"] = address_chinese
        if address_english is not UNSET:
            field_dict["Address_English"] = address_english
        if chinese_company_name is not UNSET:
            field_dict["Chinese_Company_Name"] = chinese_company_name
        if company_telephone_no is not UNSET:
            field_dict["Company_Telephone_No"] = company_telephone_no
        if english_company_name is not UNSET:
            field_dict["English_Company_Name"] = english_company_name
        if rgc_no is not UNSET:
            field_dict["RGC_No"] = rgc_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chinese = _parse_address_chinese(d.pop("Address_Chinese", UNSET))

        def _parse_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_english = _parse_address_english(d.pop("Address_English", UNSET))

        def _parse_chinese_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_company_name = _parse_chinese_company_name(
            d.pop("Chinese_Company_Name", UNSET)
        )

        def _parse_company_telephone_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_telephone_no = _parse_company_telephone_no(
            d.pop("Company_Telephone_No", UNSET)
        )

        def _parse_english_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_company_name = _parse_english_company_name(
            d.pop("English_Company_Name", UNSET)
        )

        def _parse_rgc_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rgc_no = _parse_rgc_no(d.pop("RGC_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_chinese=address_chinese,
            address_english=address_english,
            chinese_company_name=chinese_company_name,
            company_telephone_no=company_telephone_no,
            english_company_name=english_company_name,
            rgc_no=rgc_no,
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
