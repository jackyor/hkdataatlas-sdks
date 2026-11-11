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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    name_eng: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    address_eng: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    district_eng: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        name_eng: None | str | Unset
        if isinstance(self.name_eng, Unset):
            name_eng = UNSET
        else:
            name_eng = self.name_eng

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        address_eng: None | str | Unset
        if isinstance(self.address_eng, Unset):
            address_eng = UNSET
        else:
            address_eng = self.address_eng

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

        district_eng: None | str | Unset
        if isinstance(self.district_eng, Unset):
            district_eng = UNSET
        else:
            district_eng = self.district_eng

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if name_eng is not UNSET:
            field_dict["Name_ENG"] = name_eng
        if name_tc is not UNSET:
            field_dict["Name_TC"] = name_tc
        if name_sc is not UNSET:
            field_dict["Name_SC"] = name_sc
        if address_eng is not UNSET:
            field_dict["Address_ENG"] = address_eng
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if address_sc is not UNSET:
            field_dict["Address_SC"] = address_sc
        if district_eng is not UNSET:
            field_dict["District_ENG"] = district_eng
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if district_sc is not UNSET:
            field_dict["District_SC"] = district_sc
        if telephone is not UNSET:
            field_dict["Telephone"] = telephone
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_eng = _parse_name_eng(d.pop("Name_ENG", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("Name_TC", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("Name_SC", UNSET))

        def _parse_address_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_eng = _parse_address_eng(d.pop("Address_ENG", UNSET))

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

        def _parse_district_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_eng = _parse_district_eng(d.pop("District_ENG", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("District_SC", UNSET))

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

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            name_eng=name_eng,
            name_tc=name_tc,
            name_sc=name_sc,
            address_eng=address_eng,
            address_tc=address_tc,
            address_sc=address_sc,
            district_eng=district_eng,
            district_tc=district_tc,
            district_sc=district_sc,
            telephone=telephone,
            latitude=latitude,
            longitude=longitude,
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
