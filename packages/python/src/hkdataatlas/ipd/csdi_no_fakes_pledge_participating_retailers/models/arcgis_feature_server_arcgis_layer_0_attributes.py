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
        retailer_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        retailer_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        retailer_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        category_of_merchandise_en_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        category_of_merchandise_en_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        category_of_merchandise_tc_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        category_of_merchandise_tc_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        category_of_merchandise_sc_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        category_of_merchandise_sc_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    retailer_name_en: None | str | Unset = UNSET
    retailer_name_tc: None | str | Unset = UNSET
    retailer_name_sc: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    category_of_merchandise_en_1: None | str | Unset = UNSET
    category_of_merchandise_en_2: None | str | Unset = UNSET
    category_of_merchandise_tc_1: None | str | Unset = UNSET
    category_of_merchandise_tc_2: None | str | Unset = UNSET
    category_of_merchandise_sc_1: None | str | Unset = UNSET
    category_of_merchandise_sc_2: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retailer_name_en: None | str | Unset
        if isinstance(self.retailer_name_en, Unset):
            retailer_name_en = UNSET
        else:
            retailer_name_en = self.retailer_name_en

        retailer_name_tc: None | str | Unset
        if isinstance(self.retailer_name_tc, Unset):
            retailer_name_tc = UNSET
        else:
            retailer_name_tc = self.retailer_name_tc

        retailer_name_sc: None | str | Unset
        if isinstance(self.retailer_name_sc, Unset):
            retailer_name_sc = UNSET
        else:
            retailer_name_sc = self.retailer_name_sc

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        category_of_merchandise_en_1: None | str | Unset
        if isinstance(self.category_of_merchandise_en_1, Unset):
            category_of_merchandise_en_1 = UNSET
        else:
            category_of_merchandise_en_1 = self.category_of_merchandise_en_1

        category_of_merchandise_en_2: None | str | Unset
        if isinstance(self.category_of_merchandise_en_2, Unset):
            category_of_merchandise_en_2 = UNSET
        else:
            category_of_merchandise_en_2 = self.category_of_merchandise_en_2

        category_of_merchandise_tc_1: None | str | Unset
        if isinstance(self.category_of_merchandise_tc_1, Unset):
            category_of_merchandise_tc_1 = UNSET
        else:
            category_of_merchandise_tc_1 = self.category_of_merchandise_tc_1

        category_of_merchandise_tc_2: None | str | Unset
        if isinstance(self.category_of_merchandise_tc_2, Unset):
            category_of_merchandise_tc_2 = UNSET
        else:
            category_of_merchandise_tc_2 = self.category_of_merchandise_tc_2

        category_of_merchandise_sc_1: None | str | Unset
        if isinstance(self.category_of_merchandise_sc_1, Unset):
            category_of_merchandise_sc_1 = UNSET
        else:
            category_of_merchandise_sc_1 = self.category_of_merchandise_sc_1

        category_of_merchandise_sc_2: None | str | Unset
        if isinstance(self.category_of_merchandise_sc_2, Unset):
            category_of_merchandise_sc_2 = UNSET
        else:
            category_of_merchandise_sc_2 = self.category_of_merchandise_sc_2

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retailer_name_en is not UNSET:
            field_dict["Retailer_Name_EN"] = retailer_name_en
        if retailer_name_tc is not UNSET:
            field_dict["Retailer_Name_TC"] = retailer_name_tc
        if retailer_name_sc is not UNSET:
            field_dict["Retailer_Name_SC"] = retailer_name_sc
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if address_sc is not UNSET:
            field_dict["Address_SC"] = address_sc
        if telephone is not UNSET:
            field_dict["Telephone"] = telephone
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if category_of_merchandise_en_1 is not UNSET:
            field_dict["Category_of_Merchandise_EN_1"] = category_of_merchandise_en_1
        if category_of_merchandise_en_2 is not UNSET:
            field_dict["Category_of_Merchandise_EN_2"] = category_of_merchandise_en_2
        if category_of_merchandise_tc_1 is not UNSET:
            field_dict["Category_of_Merchandise_TC_1"] = category_of_merchandise_tc_1
        if category_of_merchandise_tc_2 is not UNSET:
            field_dict["Category_of_Merchandise_TC_2"] = category_of_merchandise_tc_2
        if category_of_merchandise_sc_1 is not UNSET:
            field_dict["Category_of_Merchandise_SC_1"] = category_of_merchandise_sc_1
        if category_of_merchandise_sc_2 is not UNSET:
            field_dict["Category_of_Merchandise_SC_2"] = category_of_merchandise_sc_2
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_retailer_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retailer_name_en = _parse_retailer_name_en(d.pop("Retailer_Name_EN", UNSET))

        def _parse_retailer_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retailer_name_tc = _parse_retailer_name_tc(d.pop("Retailer_Name_TC", UNSET))

        def _parse_retailer_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retailer_name_sc = _parse_retailer_name_sc(d.pop("Retailer_Name_SC", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_SC", UNSET))

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("Telephone", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_category_of_merchandise_en_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_of_merchandise_en_1 = _parse_category_of_merchandise_en_1(
            d.pop("Category_of_Merchandise_EN_1", UNSET)
        )

        def _parse_category_of_merchandise_en_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_of_merchandise_en_2 = _parse_category_of_merchandise_en_2(
            d.pop("Category_of_Merchandise_EN_2", UNSET)
        )

        def _parse_category_of_merchandise_tc_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_of_merchandise_tc_1 = _parse_category_of_merchandise_tc_1(
            d.pop("Category_of_Merchandise_TC_1", UNSET)
        )

        def _parse_category_of_merchandise_tc_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_of_merchandise_tc_2 = _parse_category_of_merchandise_tc_2(
            d.pop("Category_of_Merchandise_TC_2", UNSET)
        )

        def _parse_category_of_merchandise_sc_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_of_merchandise_sc_1 = _parse_category_of_merchandise_sc_1(
            d.pop("Category_of_Merchandise_SC_1", UNSET)
        )

        def _parse_category_of_merchandise_sc_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_of_merchandise_sc_2 = _parse_category_of_merchandise_sc_2(
            d.pop("Category_of_Merchandise_SC_2", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            retailer_name_en=retailer_name_en,
            retailer_name_tc=retailer_name_tc,
            retailer_name_sc=retailer_name_sc,
            address_en=address_en,
            address_tc=address_tc,
            address_sc=address_sc,
            telephone=telephone,
            latitude=latitude,
            longitude=longitude,
            category_of_merchandise_en_1=category_of_merchandise_en_1,
            category_of_merchandise_en_2=category_of_merchandise_en_2,
            category_of_merchandise_tc_1=category_of_merchandise_tc_1,
            category_of_merchandise_tc_2=category_of_merchandise_tc_2,
            category_of_merchandise_sc_1=category_of_merchandise_sc_1,
            category_of_merchandise_sc_2=category_of_merchandise_sc_2,
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
