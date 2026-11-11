from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HousingEstateRecord")


@_attrs_define
class HousingEstateRecord:
    """Fields documented for housing estates and projects. The dictionary does not establish a response envelope or which
    fields are present in each record. Text values are provided in Traditional Chinese (`tc`), Simplified Chinese
    (`sc`), and English (`en`) variants where documented. The marker `|||` denotes a split string.

        Attributes:
            address_en (str | Unset): Address in English. Dictionary storage length: X(500). `|||` denotes a split string.
            address_sc (str | Unset): Address in Simplified Chinese. Dictionary storage length: X(500). `|||` denotes a
                split string.
            address_tc (str | Unset): Address in Traditional Chinese. Dictionary storage length: X(500). `|||` denotes a
                split string.
            completionyear_en (str | Unset): Year or years of building completion in English. May include phases or block
                details separated by `|||`. Dictionary storage length: X(255).
            completionyear_sc (str | Unset): Year or years of building completion in Simplified Chinese. May include phases
                or block details separated by `|||`. Dictionary storage length: X(255).
            completionyear_tc (str | Unset): Year or years of building completion in Traditional Chinese. May include phases
                or block details separated by `|||`. Dictionary storage length: X(255).
            facilities_en (str | Unset): Facilities provided by the estate or project in English. Dictionary storage length:
                X(500).
            facilities_sc (str | Unset): Facilities provided by the estate or project in Simplified Chinese. Dictionary
                storage length: X(500).
            facilities_tc (str | Unset): Facilities provided by the estate or project in Traditional Chinese. Dictionary
                storage length: X(500).
            flatarea_en (str | Unset): Flat area in English, represented as text; may include ranges and rental/sale
                distinctions. Dictionary storage length: X(255).
            flatarea_sc (str | Unset): Flat area in Simplified Chinese, represented as text; may include ranges and
                rental/sale distinctions. Dictionary storage length: X(255).
            flatarea_tc (str | Unset): Flat area in Traditional Chinese, represented as text; may include ranges and
                rental/sale distinctions. Dictionary storage length: X(255).
            name_en (str | Unset): Name of the public housing estate or project in English. Dictionary storage length:
                X(45).
            name_sc (str | Unset): Name of the public housing estate or project in Simplified Chinese. Dictionary storage
                length: X(45).
            name_tc (str | Unset): Name of the public housing estate or project in Traditional Chinese. Dictionary storage
                length: X(45).
            noofblocks_en (str | Unset): Number of blocks in English, represented as text; may distinguish rental and sale
                blocks using `|||`. Dictionary storage length: X(255).
            noofblocks_sc (str | Unset): Number of blocks in Simplified Chinese, represented as text; may distinguish rental
                and sale blocks using `|||`. Dictionary storage length: X(255).
            noofblocks_tc (str | Unset): Number of blocks in Traditional Chinese, represented as text; may distinguish
                rental and sale blocks using `|||`. Dictionary storage length: X(255).
            profile_en (str | Unset): Estate or project profile in English. `|||` separates text segments. Dictionary
                storage length: X(1000).
            profile_sc (str | Unset): Estate or project profile in Simplified Chinese. `|||` separates text segments.
                Dictionary storage length: X(1000).
            profile_tc (str | Unset): Estate or project profile in Traditional Chinese. `|||` separates text segments.
                Dictionary storage length: X(1000).
            sitearea_en (str | Unset): Site area in English. Dictionary storage length: X(255).
            sitearea_sc (str | Unset): Site area in Simplified Chinese. Dictionary storage length: X(255).
            sitearea_tc (str | Unset): Site area in Traditional Chinese. Dictionary storage length: X(255).
            totalflat_en (str | Unset): Number of flats in English, represented as text; may include notes, phases, or
                totals. Dictionary storage length: X(255).
            totalflat_sc (str | Unset): Number of flats in Simplified Chinese, represented as text; may include notes,
                phases, or totals. Dictionary storage length: X(255).
            totalflat_tc (str | Unset): Number of flats in Traditional Chinese, represented as text; may include notes,
                phases, or totals. Dictionary storage length: X(255).
    """

    address_en: str | Unset = UNSET
    address_sc: str | Unset = UNSET
    address_tc: str | Unset = UNSET
    completionyear_en: str | Unset = UNSET
    completionyear_sc: str | Unset = UNSET
    completionyear_tc: str | Unset = UNSET
    facilities_en: str | Unset = UNSET
    facilities_sc: str | Unset = UNSET
    facilities_tc: str | Unset = UNSET
    flatarea_en: str | Unset = UNSET
    flatarea_sc: str | Unset = UNSET
    flatarea_tc: str | Unset = UNSET
    name_en: str | Unset = UNSET
    name_sc: str | Unset = UNSET
    name_tc: str | Unset = UNSET
    noofblocks_en: str | Unset = UNSET
    noofblocks_sc: str | Unset = UNSET
    noofblocks_tc: str | Unset = UNSET
    profile_en: str | Unset = UNSET
    profile_sc: str | Unset = UNSET
    profile_tc: str | Unset = UNSET
    sitearea_en: str | Unset = UNSET
    sitearea_sc: str | Unset = UNSET
    sitearea_tc: str | Unset = UNSET
    totalflat_en: str | Unset = UNSET
    totalflat_sc: str | Unset = UNSET
    totalflat_tc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en = self.address_en

        address_sc = self.address_sc

        address_tc = self.address_tc

        completionyear_en = self.completionyear_en

        completionyear_sc = self.completionyear_sc

        completionyear_tc = self.completionyear_tc

        facilities_en = self.facilities_en

        facilities_sc = self.facilities_sc

        facilities_tc = self.facilities_tc

        flatarea_en = self.flatarea_en

        flatarea_sc = self.flatarea_sc

        flatarea_tc = self.flatarea_tc

        name_en = self.name_en

        name_sc = self.name_sc

        name_tc = self.name_tc

        noofblocks_en = self.noofblocks_en

        noofblocks_sc = self.noofblocks_sc

        noofblocks_tc = self.noofblocks_tc

        profile_en = self.profile_en

        profile_sc = self.profile_sc

        profile_tc = self.profile_tc

        sitearea_en = self.sitearea_en

        sitearea_sc = self.sitearea_sc

        sitearea_tc = self.sitearea_tc

        totalflat_en = self.totalflat_en

        totalflat_sc = self.totalflat_sc

        totalflat_tc = self.totalflat_tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["address_en"] = address_en
        if address_sc is not UNSET:
            field_dict["address_sc"] = address_sc
        if address_tc is not UNSET:
            field_dict["address_tc"] = address_tc
        if completionyear_en is not UNSET:
            field_dict["completionyear_en"] = completionyear_en
        if completionyear_sc is not UNSET:
            field_dict["completionyear_sc"] = completionyear_sc
        if completionyear_tc is not UNSET:
            field_dict["completionyear_tc"] = completionyear_tc
        if facilities_en is not UNSET:
            field_dict["facilities_en"] = facilities_en
        if facilities_sc is not UNSET:
            field_dict["facilities_sc"] = facilities_sc
        if facilities_tc is not UNSET:
            field_dict["facilities_tc"] = facilities_tc
        if flatarea_en is not UNSET:
            field_dict["flatarea_en"] = flatarea_en
        if flatarea_sc is not UNSET:
            field_dict["flatarea_sc"] = flatarea_sc
        if flatarea_tc is not UNSET:
            field_dict["flatarea_tc"] = flatarea_tc
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if name_sc is not UNSET:
            field_dict["name_sc"] = name_sc
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc
        if noofblocks_en is not UNSET:
            field_dict["noofblocks_en"] = noofblocks_en
        if noofblocks_sc is not UNSET:
            field_dict["noofblocks_sc"] = noofblocks_sc
        if noofblocks_tc is not UNSET:
            field_dict["noofblocks_tc"] = noofblocks_tc
        if profile_en is not UNSET:
            field_dict["profile_en"] = profile_en
        if profile_sc is not UNSET:
            field_dict["profile_sc"] = profile_sc
        if profile_tc is not UNSET:
            field_dict["profile_tc"] = profile_tc
        if sitearea_en is not UNSET:
            field_dict["sitearea_en"] = sitearea_en
        if sitearea_sc is not UNSET:
            field_dict["sitearea_sc"] = sitearea_sc
        if sitearea_tc is not UNSET:
            field_dict["sitearea_tc"] = sitearea_tc
        if totalflat_en is not UNSET:
            field_dict["totalflat_en"] = totalflat_en
        if totalflat_sc is not UNSET:
            field_dict["totalflat_sc"] = totalflat_sc
        if totalflat_tc is not UNSET:
            field_dict["totalflat_tc"] = totalflat_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address_en = d.pop("address_en", UNSET)

        address_sc = d.pop("address_sc", UNSET)

        address_tc = d.pop("address_tc", UNSET)

        completionyear_en = d.pop("completionyear_en", UNSET)

        completionyear_sc = d.pop("completionyear_sc", UNSET)

        completionyear_tc = d.pop("completionyear_tc", UNSET)

        facilities_en = d.pop("facilities_en", UNSET)

        facilities_sc = d.pop("facilities_sc", UNSET)

        facilities_tc = d.pop("facilities_tc", UNSET)

        flatarea_en = d.pop("flatarea_en", UNSET)

        flatarea_sc = d.pop("flatarea_sc", UNSET)

        flatarea_tc = d.pop("flatarea_tc", UNSET)

        name_en = d.pop("name_en", UNSET)

        name_sc = d.pop("name_sc", UNSET)

        name_tc = d.pop("name_tc", UNSET)

        noofblocks_en = d.pop("noofblocks_en", UNSET)

        noofblocks_sc = d.pop("noofblocks_sc", UNSET)

        noofblocks_tc = d.pop("noofblocks_tc", UNSET)

        profile_en = d.pop("profile_en", UNSET)

        profile_sc = d.pop("profile_sc", UNSET)

        profile_tc = d.pop("profile_tc", UNSET)

        sitearea_en = d.pop("sitearea_en", UNSET)

        sitearea_sc = d.pop("sitearea_sc", UNSET)

        sitearea_tc = d.pop("sitearea_tc", UNSET)

        totalflat_en = d.pop("totalflat_en", UNSET)

        totalflat_sc = d.pop("totalflat_sc", UNSET)

        totalflat_tc = d.pop("totalflat_tc", UNSET)

        housing_estate_record = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            completionyear_en=completionyear_en,
            completionyear_sc=completionyear_sc,
            completionyear_tc=completionyear_tc,
            facilities_en=facilities_en,
            facilities_sc=facilities_sc,
            facilities_tc=facilities_tc,
            flatarea_en=flatarea_en,
            flatarea_sc=flatarea_sc,
            flatarea_tc=flatarea_tc,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            noofblocks_en=noofblocks_en,
            noofblocks_sc=noofblocks_sc,
            noofblocks_tc=noofblocks_tc,
            profile_en=profile_en,
            profile_sc=profile_sc,
            profile_tc=profile_tc,
            sitearea_en=sitearea_en,
            sitearea_sc=sitearea_sc,
            sitearea_tc=sitearea_tc,
            totalflat_en=totalflat_en,
            totalflat_sc=totalflat_sc,
            totalflat_tc=totalflat_tc,
        )

        housing_estate_record.additional_properties = d
        return housing_estate_record

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
