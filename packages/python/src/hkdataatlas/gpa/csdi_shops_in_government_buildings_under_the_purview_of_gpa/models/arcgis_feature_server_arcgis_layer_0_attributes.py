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
        en_property_name (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_property_name (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_property_name (None | str | Unset): Publisher field type: esriFieldTypeString
        en_property_address (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_property_address (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_property_address (None | str | Unset): Publisher field type: esriFieldTypeString
        en_district (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        en_user (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_user (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_user (None | str | Unset): Publisher field type: esriFieldTypeString
        shop_number (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    en_property_name: None | str | Unset = UNSET
    tc_property_name: None | str | Unset = UNSET
    sc_property_name: None | str | Unset = UNSET
    en_property_address: None | str | Unset = UNSET
    tc_property_address: None | str | Unset = UNSET
    sc_property_address: None | str | Unset = UNSET
    en_district: None | str | Unset = UNSET
    tc_district: None | str | Unset = UNSET
    sc_district: None | str | Unset = UNSET
    en_user: None | str | Unset = UNSET
    tc_user: None | str | Unset = UNSET
    sc_user: None | str | Unset = UNSET
    shop_number: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en_property_name: None | str | Unset
        if isinstance(self.en_property_name, Unset):
            en_property_name = UNSET
        else:
            en_property_name = self.en_property_name

        tc_property_name: None | str | Unset
        if isinstance(self.tc_property_name, Unset):
            tc_property_name = UNSET
        else:
            tc_property_name = self.tc_property_name

        sc_property_name: None | str | Unset
        if isinstance(self.sc_property_name, Unset):
            sc_property_name = UNSET
        else:
            sc_property_name = self.sc_property_name

        en_property_address: None | str | Unset
        if isinstance(self.en_property_address, Unset):
            en_property_address = UNSET
        else:
            en_property_address = self.en_property_address

        tc_property_address: None | str | Unset
        if isinstance(self.tc_property_address, Unset):
            tc_property_address = UNSET
        else:
            tc_property_address = self.tc_property_address

        sc_property_address: None | str | Unset
        if isinstance(self.sc_property_address, Unset):
            sc_property_address = UNSET
        else:
            sc_property_address = self.sc_property_address

        en_district: None | str | Unset
        if isinstance(self.en_district, Unset):
            en_district = UNSET
        else:
            en_district = self.en_district

        tc_district: None | str | Unset
        if isinstance(self.tc_district, Unset):
            tc_district = UNSET
        else:
            tc_district = self.tc_district

        sc_district: None | str | Unset
        if isinstance(self.sc_district, Unset):
            sc_district = UNSET
        else:
            sc_district = self.sc_district

        en_user: None | str | Unset
        if isinstance(self.en_user, Unset):
            en_user = UNSET
        else:
            en_user = self.en_user

        tc_user: None | str | Unset
        if isinstance(self.tc_user, Unset):
            tc_user = UNSET
        else:
            tc_user = self.tc_user

        sc_user: None | str | Unset
        if isinstance(self.sc_user, Unset):
            sc_user = UNSET
        else:
            sc_user = self.sc_user

        shop_number: None | str | Unset
        if isinstance(self.shop_number, Unset):
            shop_number = UNSET
        else:
            shop_number = self.shop_number

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en_property_name is not UNSET:
            field_dict["en_property_name"] = en_property_name
        if tc_property_name is not UNSET:
            field_dict["tc_property_name"] = tc_property_name
        if sc_property_name is not UNSET:
            field_dict["sc_property_name"] = sc_property_name
        if en_property_address is not UNSET:
            field_dict["en_property_address"] = en_property_address
        if tc_property_address is not UNSET:
            field_dict["tc_property_address"] = tc_property_address
        if sc_property_address is not UNSET:
            field_dict["sc_property_address"] = sc_property_address
        if en_district is not UNSET:
            field_dict["en_district"] = en_district
        if tc_district is not UNSET:
            field_dict["tc_district"] = tc_district
        if sc_district is not UNSET:
            field_dict["sc_district"] = sc_district
        if en_user is not UNSET:
            field_dict["en_user"] = en_user
        if tc_user is not UNSET:
            field_dict["tc_user"] = tc_user
        if sc_user is not UNSET:
            field_dict["sc_user"] = sc_user
        if shop_number is not UNSET:
            field_dict["shop_number"] = shop_number
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_en_property_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_property_name = _parse_en_property_name(d.pop("en_property_name", UNSET))

        def _parse_tc_property_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_property_name = _parse_tc_property_name(d.pop("tc_property_name", UNSET))

        def _parse_sc_property_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_property_name = _parse_sc_property_name(d.pop("sc_property_name", UNSET))

        def _parse_en_property_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_property_address = _parse_en_property_address(
            d.pop("en_property_address", UNSET)
        )

        def _parse_tc_property_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_property_address = _parse_tc_property_address(
            d.pop("tc_property_address", UNSET)
        )

        def _parse_sc_property_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_property_address = _parse_sc_property_address(
            d.pop("sc_property_address", UNSET)
        )

        def _parse_en_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_district = _parse_en_district(d.pop("en_district", UNSET))

        def _parse_tc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_district = _parse_tc_district(d.pop("tc_district", UNSET))

        def _parse_sc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_district = _parse_sc_district(d.pop("sc_district", UNSET))

        def _parse_en_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_user = _parse_en_user(d.pop("en_user", UNSET))

        def _parse_tc_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_user = _parse_tc_user(d.pop("tc_user", UNSET))

        def _parse_sc_user(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_user = _parse_sc_user(d.pop("sc_user", UNSET))

        def _parse_shop_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shop_number = _parse_shop_number(d.pop("shop_number", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            en_property_name=en_property_name,
            tc_property_name=tc_property_name,
            sc_property_name=sc_property_name,
            en_property_address=en_property_address,
            tc_property_address=tc_property_address,
            sc_property_address=sc_property_address,
            en_district=en_district,
            tc_district=tc_district,
            sc_district=sc_district,
            en_user=en_user,
            tc_user=tc_user,
            sc_user=sc_user,
            shop_number=shop_number,
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
