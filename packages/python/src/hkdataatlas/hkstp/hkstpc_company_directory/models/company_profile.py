from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyProfile")


@_attrs_define
class CompanyProfile:
    """
    Attributes:
        address_en (None | str | Unset): Company address in English.
        address_sc (None | str | Unset): Company address in Simplified Chinese.
        address_tc (None | str | Unset): Company address in Traditional Chinese.
        cluster (None | str | Unset): Cluster of company in Hong Kong Science Park in English.
        cluster_sc (None | str | Unset): Cluster of company in Hong Kong Science Park in Simplified Chinese.
        cluster_tc (None | str | Unset): Cluster of company in Hong Kong Science Park in Traditional Chinese.
        contact_en (None | str | Unset): Contact name in English.
        contact_sc (None | str | Unset): Contact name in Simplified Chinese.
        contact_tc (None | str | Unset): Contact name in Traditional Chinese.
        email (None | str | Unset): Email address of the company.
        fax (None | str | Unset): Fax number of the company.
        introduction_en (None | str | Unset): Company introduction in English.
        introduction_sc (None | str | Unset): Company introduction in Simplified Chinese.
        introduction_tc (None | str | Unset): Company introduction in Traditional Chinese.
        name_en (None | str | Unset): Company name in English.
        name_sc (None | str | Unset): Company name in Simplified Chinese.
        name_tc (None | str | Unset): Company name in Traditional Chinese.
        product_en (None | str | Unset): Product description in English.
        product_sc (None | str | Unset): Product description in Simplified Chinese. Its placement in the extracted
            documentation is unclear; the field dictionary identifies this name and description.
        product_tc (None | str | Unset): Product description in Traditional Chinese.
        telephone (None | str | Unset): Telephone number of the company.
        type_ (None | str | Unset): Type of company in Hong Kong Science Park in English.
        type_name_en (None | str | Unset): English company type name as shown in the documented example; the field
            dictionary does not list this property.
        type_name_sc (None | str | Unset): Type of company in Hong Kong Science Park in Simplified Chinese.
        type_name_tc (None | str | Unset): Type of company in Hong Kong Science Park in Traditional Chinese.
        website (None | str | Unset): Website URL of the company.
    """

    address_en: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    cluster: None | str | Unset = UNSET
    cluster_sc: None | str | Unset = UNSET
    cluster_tc: None | str | Unset = UNSET
    contact_en: None | str | Unset = UNSET
    contact_sc: None | str | Unset = UNSET
    contact_tc: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    fax: None | str | Unset = UNSET
    introduction_en: None | str | Unset = UNSET
    introduction_sc: None | str | Unset = UNSET
    introduction_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    product_en: None | str | Unset = UNSET
    product_sc: None | str | Unset = UNSET
    product_tc: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    type_name_en: None | str | Unset = UNSET
    type_name_sc: None | str | Unset = UNSET
    type_name_tc: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        cluster: None | str | Unset
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        else:
            cluster = self.cluster

        cluster_sc: None | str | Unset
        if isinstance(self.cluster_sc, Unset):
            cluster_sc = UNSET
        else:
            cluster_sc = self.cluster_sc

        cluster_tc: None | str | Unset
        if isinstance(self.cluster_tc, Unset):
            cluster_tc = UNSET
        else:
            cluster_tc = self.cluster_tc

        contact_en: None | str | Unset
        if isinstance(self.contact_en, Unset):
            contact_en = UNSET
        else:
            contact_en = self.contact_en

        contact_sc: None | str | Unset
        if isinstance(self.contact_sc, Unset):
            contact_sc = UNSET
        else:
            contact_sc = self.contact_sc

        contact_tc: None | str | Unset
        if isinstance(self.contact_tc, Unset):
            contact_tc = UNSET
        else:
            contact_tc = self.contact_tc

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        fax: None | str | Unset
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        introduction_en: None | str | Unset
        if isinstance(self.introduction_en, Unset):
            introduction_en = UNSET
        else:
            introduction_en = self.introduction_en

        introduction_sc: None | str | Unset
        if isinstance(self.introduction_sc, Unset):
            introduction_sc = UNSET
        else:
            introduction_sc = self.introduction_sc

        introduction_tc: None | str | Unset
        if isinstance(self.introduction_tc, Unset):
            introduction_tc = UNSET
        else:
            introduction_tc = self.introduction_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        product_en: None | str | Unset
        if isinstance(self.product_en, Unset):
            product_en = UNSET
        else:
            product_en = self.product_en

        product_sc: None | str | Unset
        if isinstance(self.product_sc, Unset):
            product_sc = UNSET
        else:
            product_sc = self.product_sc

        product_tc: None | str | Unset
        if isinstance(self.product_tc, Unset):
            product_tc = UNSET
        else:
            product_tc = self.product_tc

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        type_name_en: None | str | Unset
        if isinstance(self.type_name_en, Unset):
            type_name_en = UNSET
        else:
            type_name_en = self.type_name_en

        type_name_sc: None | str | Unset
        if isinstance(self.type_name_sc, Unset):
            type_name_sc = UNSET
        else:
            type_name_sc = self.type_name_sc

        type_name_tc: None | str | Unset
        if isinstance(self.type_name_tc, Unset):
            type_name_tc = UNSET
        else:
            type_name_tc = self.type_name_tc

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["address_EN"] = address_en
        if address_sc is not UNSET:
            field_dict["address_SC"] = address_sc
        if address_tc is not UNSET:
            field_dict["address_TC"] = address_tc
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if cluster_sc is not UNSET:
            field_dict["cluster_SC"] = cluster_sc
        if cluster_tc is not UNSET:
            field_dict["cluster_TC"] = cluster_tc
        if contact_en is not UNSET:
            field_dict["contact_EN"] = contact_en
        if contact_sc is not UNSET:
            field_dict["contact_SC"] = contact_sc
        if contact_tc is not UNSET:
            field_dict["contact_TC"] = contact_tc
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if introduction_en is not UNSET:
            field_dict["introduction_EN"] = introduction_en
        if introduction_sc is not UNSET:
            field_dict["introduction_SC"] = introduction_sc
        if introduction_tc is not UNSET:
            field_dict["introduction_TC"] = introduction_tc
        if name_en is not UNSET:
            field_dict["name_EN"] = name_en
        if name_sc is not UNSET:
            field_dict["name_SC"] = name_sc
        if name_tc is not UNSET:
            field_dict["name_TC"] = name_tc
        if product_en is not UNSET:
            field_dict["product_EN"] = product_en
        if product_sc is not UNSET:
            field_dict["product_SC"] = product_sc
        if product_tc is not UNSET:
            field_dict["product_TC"] = product_tc
        if telephone is not UNSET:
            field_dict["telephone"] = telephone
        if type_ is not UNSET:
            field_dict["type"] = type_
        if type_name_en is not UNSET:
            field_dict["type_Name_EN"] = type_name_en
        if type_name_sc is not UNSET:
            field_dict["type_Name_SC"] = type_name_sc
        if type_name_tc is not UNSET:
            field_dict["type_Name_TC"] = type_name_tc
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("address_EN", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("address_SC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("address_TC", UNSET))

        def _parse_cluster(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster = _parse_cluster(d.pop("cluster", UNSET))

        def _parse_cluster_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_sc = _parse_cluster_sc(d.pop("cluster_SC", UNSET))

        def _parse_cluster_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_tc = _parse_cluster_tc(d.pop("cluster_TC", UNSET))

        def _parse_contact_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_en = _parse_contact_en(d.pop("contact_EN", UNSET))

        def _parse_contact_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_sc = _parse_contact_sc(d.pop("contact_SC", UNSET))

        def _parse_contact_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_tc = _parse_contact_tc(d.pop("contact_TC", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax = _parse_fax(d.pop("fax", UNSET))

        def _parse_introduction_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        introduction_en = _parse_introduction_en(d.pop("introduction_EN", UNSET))

        def _parse_introduction_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        introduction_sc = _parse_introduction_sc(d.pop("introduction_SC", UNSET))

        def _parse_introduction_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        introduction_tc = _parse_introduction_tc(d.pop("introduction_TC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("name_EN", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("name_SC", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("name_TC", UNSET))

        def _parse_product_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_en = _parse_product_en(d.pop("product_EN", UNSET))

        def _parse_product_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_sc = _parse_product_sc(d.pop("product_SC", UNSET))

        def _parse_product_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_tc = _parse_product_tc(d.pop("product_TC", UNSET))

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("telephone", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_type_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_name_en = _parse_type_name_en(d.pop("type_Name_EN", UNSET))

        def _parse_type_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_name_sc = _parse_type_name_sc(d.pop("type_Name_SC", UNSET))

        def _parse_type_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_name_tc = _parse_type_name_tc(d.pop("type_Name_TC", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        company_profile = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            cluster=cluster,
            cluster_sc=cluster_sc,
            cluster_tc=cluster_tc,
            contact_en=contact_en,
            contact_sc=contact_sc,
            contact_tc=contact_tc,
            email=email,
            fax=fax,
            introduction_en=introduction_en,
            introduction_sc=introduction_sc,
            introduction_tc=introduction_tc,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            product_en=product_en,
            product_sc=product_sc,
            product_tc=product_tc,
            telephone=telephone,
            type_=type_,
            type_name_en=type_name_en,
            type_name_sc=type_name_sc,
            type_name_tc=type_name_tc,
            website=website,
        )

        company_profile.additional_properties = d
        return company_profile

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
