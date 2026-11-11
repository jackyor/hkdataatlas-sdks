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
        chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        company_address_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        company_address_english (None | str | Unset): Publisher field type: esriFieldTypeString
        english_name (None | str | Unset): Publisher field type: esriFieldTypeString
        expiry_date (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_no (float | None | Unset): Publisher field type: esriFieldTypeDouble
        link_id (float | None | Unset): Publisher field type: esriFieldTypeDouble
        phone_no (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    chinese_name: None | str | Unset = UNSET
    company_address_chinese: None | str | Unset = UNSET
    company_address_english: None | str | Unset = UNSET
    english_name: None | str | Unset = UNSET
    expiry_date: None | str | Unset = UNSET
    fax_no: float | None | Unset = UNSET
    link_id: float | None | Unset = UNSET
    phone_no: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chinese_name: None | str | Unset
        if isinstance(self.chinese_name, Unset):
            chinese_name = UNSET
        else:
            chinese_name = self.chinese_name

        company_address_chinese: None | str | Unset
        if isinstance(self.company_address_chinese, Unset):
            company_address_chinese = UNSET
        else:
            company_address_chinese = self.company_address_chinese

        company_address_english: None | str | Unset
        if isinstance(self.company_address_english, Unset):
            company_address_english = UNSET
        else:
            company_address_english = self.company_address_english

        english_name: None | str | Unset
        if isinstance(self.english_name, Unset):
            english_name = UNSET
        else:
            english_name = self.english_name

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = self.expiry_date

        fax_no: float | None | Unset
        if isinstance(self.fax_no, Unset):
            fax_no = UNSET
        else:
            fax_no = self.fax_no

        link_id: float | None | Unset
        if isinstance(self.link_id, Unset):
            link_id = UNSET
        else:
            link_id = self.link_id

        phone_no: float | None | Unset
        if isinstance(self.phone_no, Unset):
            phone_no = UNSET
        else:
            phone_no = self.phone_no

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chinese_name is not UNSET:
            field_dict["Chinese_Name"] = chinese_name
        if company_address_chinese is not UNSET:
            field_dict["Company_Address_Chinese"] = company_address_chinese
        if company_address_english is not UNSET:
            field_dict["Company_Address_English"] = company_address_english
        if english_name is not UNSET:
            field_dict["English_Name"] = english_name
        if expiry_date is not UNSET:
            field_dict["Expiry_Date"] = expiry_date
        if fax_no is not UNSET:
            field_dict["Fax_No"] = fax_no
        if link_id is not UNSET:
            field_dict["Link_ID"] = link_id
        if phone_no is not UNSET:
            field_dict["Phone_No"] = phone_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name = _parse_chinese_name(d.pop("Chinese_Name", UNSET))

        def _parse_company_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_address_chinese = _parse_company_address_chinese(
            d.pop("Company_Address_Chinese", UNSET)
        )

        def _parse_company_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_address_english = _parse_company_address_english(
            d.pop("Company_Address_English", UNSET)
        )

        def _parse_english_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_name = _parse_english_name(d.pop("English_Name", UNSET))

        def _parse_expiry_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("Expiry_Date", UNSET))

        def _parse_fax_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fax_no = _parse_fax_no(d.pop("Fax_No", UNSET))

        def _parse_link_id(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        link_id = _parse_link_id(d.pop("Link_ID", UNSET))

        def _parse_phone_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        phone_no = _parse_phone_no(d.pop("Phone_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            chinese_name=chinese_name,
            company_address_chinese=company_address_chinese,
            company_address_english=company_address_english,
            english_name=english_name,
            expiry_date=expiry_date,
            fax_no=fax_no,
            link_id=link_id,
            phone_no=phone_no,
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
