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
        business_address_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        business_address_english (None | str | Unset): Publisher field type: esriFieldTypeString
        company_name_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        company_name_english (None | str | Unset): Publisher field type: esriFieldTypeString
        expiry_date (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_number (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    business_address_chinese: None | str | Unset = UNSET
    business_address_english: None | str | Unset = UNSET
    company_name_chinese: None | str | Unset = UNSET
    company_name_english: None | str | Unset = UNSET
    expiry_date: None | str | Unset = UNSET
    registration_number: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_address_chinese: None | str | Unset
        if isinstance(self.business_address_chinese, Unset):
            business_address_chinese = UNSET
        else:
            business_address_chinese = self.business_address_chinese

        business_address_english: None | str | Unset
        if isinstance(self.business_address_english, Unset):
            business_address_english = UNSET
        else:
            business_address_english = self.business_address_english

        company_name_chinese: None | str | Unset
        if isinstance(self.company_name_chinese, Unset):
            company_name_chinese = UNSET
        else:
            company_name_chinese = self.company_name_chinese

        company_name_english: None | str | Unset
        if isinstance(self.company_name_english, Unset):
            company_name_english = UNSET
        else:
            company_name_english = self.company_name_english

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = self.expiry_date

        registration_number: None | str | Unset
        if isinstance(self.registration_number, Unset):
            registration_number = UNSET
        else:
            registration_number = self.registration_number

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_address_chinese is not UNSET:
            field_dict["Business_Address_Chinese"] = business_address_chinese
        if business_address_english is not UNSET:
            field_dict["Business_Address_English"] = business_address_english
        if company_name_chinese is not UNSET:
            field_dict["Company_Name_Chinese"] = company_name_chinese
        if company_name_english is not UNSET:
            field_dict["Company_Name_English"] = company_name_english
        if expiry_date is not UNSET:
            field_dict["Expiry_Date"] = expiry_date
        if registration_number is not UNSET:
            field_dict["Registration_Number"] = registration_number
        if telephone is not UNSET:
            field_dict["Telephone"] = telephone
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_business_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        business_address_chinese = _parse_business_address_chinese(
            d.pop("Business_Address_Chinese", UNSET)
        )

        def _parse_business_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        business_address_english = _parse_business_address_english(
            d.pop("Business_Address_English", UNSET)
        )

        def _parse_company_name_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_chinese = _parse_company_name_chinese(
            d.pop("Company_Name_Chinese", UNSET)
        )

        def _parse_company_name_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_english = _parse_company_name_english(
            d.pop("Company_Name_English", UNSET)
        )

        def _parse_expiry_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("Expiry_Date", UNSET))

        def _parse_registration_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number = _parse_registration_number(
            d.pop("Registration_Number", UNSET)
        )

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("Telephone", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            business_address_chinese=business_address_chinese,
            business_address_english=business_address_english,
            company_name_chinese=company_name_chinese,
            company_name_english=company_name_english,
            expiry_date=expiry_date,
            registration_number=registration_number,
            telephone=telephone,
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
