from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShopRecord")


@_attrs_define
class ShopRecord:
    """Fields documented for commercial shop listings. The dictionary does not establish a response envelope or which
    fields are present in each record.

        Attributes:
            address_en (str | Unset): Estate address in English. Dictionary storage length: X(500). `|||` denotes a split
                string.
            address_sc (str | Unset): Estate address in Simplified Chinese. Dictionary storage length: X(500). `|||` denotes
                a split string.
            address_tc (str | Unset): Estate address in Traditional Chinese. Dictionary storage length: X(500). `|||`
                denotes a split string.
            area_en (str | Unset): Shop area in English, represented as text. Dictionary storage length: X(255).
            area_sc (str | Unset): Shop area in Simplified Chinese, represented as text. Dictionary storage length: X(255).
            area_tc (str | Unset): Shop area in Traditional Chinese, represented as text. Dictionary storage length: X(255).
            carpark (str | Unset): Number of parking spaces represented as text. Documented examples include `N/A` and a
                numeric-looking value, so it is not restricted to a number.
            enquiries (str | Unset): Contact telephone number for the Estate or Property Management Offices. Dictionary
                storage length: X(45).
            name_en (str | Unset): Name of the estate in English. Dictionary storage length: X(45).
            name_sc (str | Unset): Name of the estate in Simplified Chinese. Dictionary storage length: X(45).
            name_tc (str | Unset): Name of the estate in Traditional Chinese. Dictionary storage length: X(45).
    """

    address_en: str | Unset = UNSET
    address_sc: str | Unset = UNSET
    address_tc: str | Unset = UNSET
    area_en: str | Unset = UNSET
    area_sc: str | Unset = UNSET
    area_tc: str | Unset = UNSET
    carpark: str | Unset = UNSET
    enquiries: str | Unset = UNSET
    name_en: str | Unset = UNSET
    name_sc: str | Unset = UNSET
    name_tc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en = self.address_en

        address_sc = self.address_sc

        address_tc = self.address_tc

        area_en = self.area_en

        area_sc = self.area_sc

        area_tc = self.area_tc

        carpark = self.carpark

        enquiries = self.enquiries

        name_en = self.name_en

        name_sc = self.name_sc

        name_tc = self.name_tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["address_en"] = address_en
        if address_sc is not UNSET:
            field_dict["address_sc"] = address_sc
        if address_tc is not UNSET:
            field_dict["address_tc"] = address_tc
        if area_en is not UNSET:
            field_dict["area_en"] = area_en
        if area_sc is not UNSET:
            field_dict["area_sc"] = area_sc
        if area_tc is not UNSET:
            field_dict["area_tc"] = area_tc
        if carpark is not UNSET:
            field_dict["carpark"] = carpark
        if enquiries is not UNSET:
            field_dict["enquiries"] = enquiries
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if name_sc is not UNSET:
            field_dict["name_sc"] = name_sc
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address_en = d.pop("address_en", UNSET)

        address_sc = d.pop("address_sc", UNSET)

        address_tc = d.pop("address_tc", UNSET)

        area_en = d.pop("area_en", UNSET)

        area_sc = d.pop("area_sc", UNSET)

        area_tc = d.pop("area_tc", UNSET)

        carpark = d.pop("carpark", UNSET)

        enquiries = d.pop("enquiries", UNSET)

        name_en = d.pop("name_en", UNSET)

        name_sc = d.pop("name_sc", UNSET)

        name_tc = d.pop("name_tc", UNSET)

        shop_record = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            area_en=area_en,
            area_sc=area_sc,
            area_tc=area_tc,
            carpark=carpark,
            enquiries=enquiries,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
        )

        shop_record.additional_properties = d
        return shop_record

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
