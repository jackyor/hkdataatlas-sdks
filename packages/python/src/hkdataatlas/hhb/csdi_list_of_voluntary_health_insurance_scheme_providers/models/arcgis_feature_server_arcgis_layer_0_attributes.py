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
        company_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        company_name_zh_hk (None | str | Unset): Publisher field type: esriFieldTypeString
        company_name_zh_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_effective_date_en (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_effective_date_zh_hk (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_effective_date_zh_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_number (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_zh_hk (None | str | Unset): Publisher field type: esriFieldTypeString
        address_zh_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        website_link_en (None | str | Unset): Publisher field type: esriFieldTypeString
        website_link_zh_hk (None | str | Unset): Publisher field type: esriFieldTypeString
        website_link_zh_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        website_domain_en (None | str | Unset): Publisher field type: esriFieldTypeString
        website_domain_zh_hk (None | str | Unset): Publisher field type: esriFieldTypeString
        website_domain_zh_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    company_name_en: None | str | Unset = UNSET
    company_name_zh_hk: None | str | Unset = UNSET
    company_name_zh_ch: None | str | Unset = UNSET
    registration_effective_date_en: None | str | Unset = UNSET
    registration_effective_date_zh_hk: None | str | Unset = UNSET
    registration_effective_date_zh_ch: None | str | Unset = UNSET
    registration_number: None | str | Unset = UNSET
    telephone_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_zh_hk: None | str | Unset = UNSET
    address_zh_ch: None | str | Unset = UNSET
    website_link_en: None | str | Unset = UNSET
    website_link_zh_hk: None | str | Unset = UNSET
    website_link_zh_ch: None | str | Unset = UNSET
    website_domain_en: None | str | Unset = UNSET
    website_domain_zh_hk: None | str | Unset = UNSET
    website_domain_zh_ch: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name_en: None | str | Unset
        if isinstance(self.company_name_en, Unset):
            company_name_en = UNSET
        else:
            company_name_en = self.company_name_en

        company_name_zh_hk: None | str | Unset
        if isinstance(self.company_name_zh_hk, Unset):
            company_name_zh_hk = UNSET
        else:
            company_name_zh_hk = self.company_name_zh_hk

        company_name_zh_ch: None | str | Unset
        if isinstance(self.company_name_zh_ch, Unset):
            company_name_zh_ch = UNSET
        else:
            company_name_zh_ch = self.company_name_zh_ch

        registration_effective_date_en: None | str | Unset
        if isinstance(self.registration_effective_date_en, Unset):
            registration_effective_date_en = UNSET
        else:
            registration_effective_date_en = self.registration_effective_date_en

        registration_effective_date_zh_hk: None | str | Unset
        if isinstance(self.registration_effective_date_zh_hk, Unset):
            registration_effective_date_zh_hk = UNSET
        else:
            registration_effective_date_zh_hk = self.registration_effective_date_zh_hk

        registration_effective_date_zh_ch: None | str | Unset
        if isinstance(self.registration_effective_date_zh_ch, Unset):
            registration_effective_date_zh_ch = UNSET
        else:
            registration_effective_date_zh_ch = self.registration_effective_date_zh_ch

        registration_number: None | str | Unset
        if isinstance(self.registration_number, Unset):
            registration_number = UNSET
        else:
            registration_number = self.registration_number

        telephone_en: None | str | Unset
        if isinstance(self.telephone_en, Unset):
            telephone_en = UNSET
        else:
            telephone_en = self.telephone_en

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_zh_hk: None | str | Unset
        if isinstance(self.address_zh_hk, Unset):
            address_zh_hk = UNSET
        else:
            address_zh_hk = self.address_zh_hk

        address_zh_ch: None | str | Unset
        if isinstance(self.address_zh_ch, Unset):
            address_zh_ch = UNSET
        else:
            address_zh_ch = self.address_zh_ch

        website_link_en: None | str | Unset
        if isinstance(self.website_link_en, Unset):
            website_link_en = UNSET
        else:
            website_link_en = self.website_link_en

        website_link_zh_hk: None | str | Unset
        if isinstance(self.website_link_zh_hk, Unset):
            website_link_zh_hk = UNSET
        else:
            website_link_zh_hk = self.website_link_zh_hk

        website_link_zh_ch: None | str | Unset
        if isinstance(self.website_link_zh_ch, Unset):
            website_link_zh_ch = UNSET
        else:
            website_link_zh_ch = self.website_link_zh_ch

        website_domain_en: None | str | Unset
        if isinstance(self.website_domain_en, Unset):
            website_domain_en = UNSET
        else:
            website_domain_en = self.website_domain_en

        website_domain_zh_hk: None | str | Unset
        if isinstance(self.website_domain_zh_hk, Unset):
            website_domain_zh_hk = UNSET
        else:
            website_domain_zh_hk = self.website_domain_zh_hk

        website_domain_zh_ch: None | str | Unset
        if isinstance(self.website_domain_zh_ch, Unset):
            website_domain_zh_ch = UNSET
        else:
            website_domain_zh_ch = self.website_domain_zh_ch

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_name_en is not UNSET:
            field_dict["company_name_en"] = company_name_en
        if company_name_zh_hk is not UNSET:
            field_dict["company_name_zh_hk"] = company_name_zh_hk
        if company_name_zh_ch is not UNSET:
            field_dict["company_name_zh_ch"] = company_name_zh_ch
        if registration_effective_date_en is not UNSET:
            field_dict["registration_effective_date_en"] = (
                registration_effective_date_en
            )
        if registration_effective_date_zh_hk is not UNSET:
            field_dict["registration_effective_date_zh_hk"] = (
                registration_effective_date_zh_hk
            )
        if registration_effective_date_zh_ch is not UNSET:
            field_dict["registration_effective_date_zh_ch"] = (
                registration_effective_date_zh_ch
            )
        if registration_number is not UNSET:
            field_dict["registration_number"] = registration_number
        if telephone_en is not UNSET:
            field_dict["telephone_en"] = telephone_en
        if address_en is not UNSET:
            field_dict["address_en"] = address_en
        if address_zh_hk is not UNSET:
            field_dict["address_zh_hk"] = address_zh_hk
        if address_zh_ch is not UNSET:
            field_dict["address_zh_ch"] = address_zh_ch
        if website_link_en is not UNSET:
            field_dict["website_link_en"] = website_link_en
        if website_link_zh_hk is not UNSET:
            field_dict["website_link_zh_hk"] = website_link_zh_hk
        if website_link_zh_ch is not UNSET:
            field_dict["website_link_zh_ch"] = website_link_zh_ch
        if website_domain_en is not UNSET:
            field_dict["website_domain_en"] = website_domain_en
        if website_domain_zh_hk is not UNSET:
            field_dict["website_domain_zh_hk"] = website_domain_zh_hk
        if website_domain_zh_ch is not UNSET:
            field_dict["website_domain_zh_ch"] = website_domain_zh_ch
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_company_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_en = _parse_company_name_en(d.pop("company_name_en", UNSET))

        def _parse_company_name_zh_hk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_zh_hk = _parse_company_name_zh_hk(
            d.pop("company_name_zh_hk", UNSET)
        )

        def _parse_company_name_zh_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_zh_ch = _parse_company_name_zh_ch(
            d.pop("company_name_zh_ch", UNSET)
        )

        def _parse_registration_effective_date_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_effective_date_en = _parse_registration_effective_date_en(
            d.pop("registration_effective_date_en", UNSET)
        )

        def _parse_registration_effective_date_zh_hk(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_effective_date_zh_hk = _parse_registration_effective_date_zh_hk(
            d.pop("registration_effective_date_zh_hk", UNSET)
        )

        def _parse_registration_effective_date_zh_ch(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_effective_date_zh_ch = _parse_registration_effective_date_zh_ch(
            d.pop("registration_effective_date_zh_ch", UNSET)
        )

        def _parse_registration_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number = _parse_registration_number(
            d.pop("registration_number", UNSET)
        )

        def _parse_telephone_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_en = _parse_telephone_en(d.pop("telephone_en", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("address_en", UNSET))

        def _parse_address_zh_hk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_zh_hk = _parse_address_zh_hk(d.pop("address_zh_hk", UNSET))

        def _parse_address_zh_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_zh_ch = _parse_address_zh_ch(d.pop("address_zh_ch", UNSET))

        def _parse_website_link_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_link_en = _parse_website_link_en(d.pop("website_link_en", UNSET))

        def _parse_website_link_zh_hk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_link_zh_hk = _parse_website_link_zh_hk(
            d.pop("website_link_zh_hk", UNSET)
        )

        def _parse_website_link_zh_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_link_zh_ch = _parse_website_link_zh_ch(
            d.pop("website_link_zh_ch", UNSET)
        )

        def _parse_website_domain_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_domain_en = _parse_website_domain_en(d.pop("website_domain_en", UNSET))

        def _parse_website_domain_zh_hk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_domain_zh_hk = _parse_website_domain_zh_hk(
            d.pop("website_domain_zh_hk", UNSET)
        )

        def _parse_website_domain_zh_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_domain_zh_ch = _parse_website_domain_zh_ch(
            d.pop("website_domain_zh_ch", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            company_name_en=company_name_en,
            company_name_zh_hk=company_name_zh_hk,
            company_name_zh_ch=company_name_zh_ch,
            registration_effective_date_en=registration_effective_date_en,
            registration_effective_date_zh_hk=registration_effective_date_zh_hk,
            registration_effective_date_zh_ch=registration_effective_date_zh_ch,
            registration_number=registration_number,
            telephone_en=telephone_en,
            address_en=address_en,
            address_zh_hk=address_zh_hk,
            address_zh_ch=address_zh_ch,
            website_link_en=website_link_en,
            website_link_zh_hk=website_link_zh_hk,
            website_link_zh_ch=website_link_zh_ch,
            website_domain_en=website_domain_en,
            website_domain_zh_hk=website_domain_zh_hk,
            website_domain_zh_ch=website_domain_zh_ch,
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
