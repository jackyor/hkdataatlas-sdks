from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Restaurant")


@_attrs_define
class Restaurant:
    """
    Attributes:
        id (str | Unset): Identifier of the restaurant. The documentation labels this field `Id`, while its example uses
            the wire key `id`; the example identifier is a string.
        location_item_en (str | Unset): Address of Shop (English).
        location_item_sc (str | Unset): Address of Shop (Simplified Chinese).
        location_item_tc (str | Unset): Address of Shop (Traditional Chinese).
        shop_title_en (str | Unset): Name of Shop (English).
        shop_title_sc (str | Unset): Name of Shop (Simplified Chinese).
        shop_title_tc (str | Unset): Name of Shop (Traditional Chinese).
    """

    id: str | Unset = UNSET
    location_item_en: str | Unset = UNSET
    location_item_sc: str | Unset = UNSET
    location_item_tc: str | Unset = UNSET
    shop_title_en: str | Unset = UNSET
    shop_title_sc: str | Unset = UNSET
    shop_title_tc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        location_item_en = self.location_item_en

        location_item_sc = self.location_item_sc

        location_item_tc = self.location_item_tc

        shop_title_en = self.shop_title_en

        shop_title_sc = self.shop_title_sc

        shop_title_tc = self.shop_title_tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if location_item_en is not UNSET:
            field_dict["locationItem_en"] = location_item_en
        if location_item_sc is not UNSET:
            field_dict["locationItem_sc"] = location_item_sc
        if location_item_tc is not UNSET:
            field_dict["locationItem_tc"] = location_item_tc
        if shop_title_en is not UNSET:
            field_dict["shopTitle_en"] = shop_title_en
        if shop_title_sc is not UNSET:
            field_dict["shopTitle_sc"] = shop_title_sc
        if shop_title_tc is not UNSET:
            field_dict["shopTitle_tc"] = shop_title_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("Id", UNSET)

        location_item_en = d.pop("locationItem_en", UNSET)

        location_item_sc = d.pop("locationItem_sc", UNSET)

        location_item_tc = d.pop("locationItem_tc", UNSET)

        shop_title_en = d.pop("shopTitle_en", UNSET)

        shop_title_sc = d.pop("shopTitle_sc", UNSET)

        shop_title_tc = d.pop("shopTitle_tc", UNSET)

        restaurant = cls(
            id=id,
            location_item_en=location_item_en,
            location_item_sc=location_item_sc,
            location_item_tc=location_item_tc,
            shop_title_en=shop_title_en,
            shop_title_sc=shop_title_sc,
            shop_title_tc=shop_title_tc,
        )

        restaurant.additional_properties = d
        return restaurant

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
