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
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_cn (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_cn (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_cn (None | str | Unset): Publisher field type: esriFieldTypeString
        gihs (None | str | Unset): Publisher field type: esriFieldTypeString
        facilities_en (None | str | Unset): Publisher field type: esriFieldTypeString
        facilities_b_5 (None | str | Unset): Publisher field type: esriFieldTypeString
        phone (None | str | Unset): Publisher field type: esriFieldTypeString
        photo_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        photo_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        photo_3 (None | str | Unset): Publisher field type: esriFieldTypeString
        photo_4 (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude_dec (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude_dec (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    district_en: None | str | Unset = UNSET
    district_cn: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_cn: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_cn: None | str | Unset = UNSET
    gihs: None | str | Unset = UNSET
    facilities_en: None | str | Unset = UNSET
    facilities_b_5: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    photo_1: None | str | Unset = UNSET
    photo_2: None | str | Unset = UNSET
    photo_3: None | str | Unset = UNSET
    photo_4: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude_dec: None | str | Unset = UNSET
    latitude_dec: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_cn: None | str | Unset
        if isinstance(self.district_cn, Unset):
            district_cn = UNSET
        else:
            district_cn = self.district_cn

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_cn: None | str | Unset
        if isinstance(self.name_cn, Unset):
            name_cn = UNSET
        else:
            name_cn = self.name_cn

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_cn: None | str | Unset
        if isinstance(self.address_cn, Unset):
            address_cn = UNSET
        else:
            address_cn = self.address_cn

        gihs: None | str | Unset
        if isinstance(self.gihs, Unset):
            gihs = UNSET
        else:
            gihs = self.gihs

        facilities_en: None | str | Unset
        if isinstance(self.facilities_en, Unset):
            facilities_en = UNSET
        else:
            facilities_en = self.facilities_en

        facilities_b_5: None | str | Unset
        if isinstance(self.facilities_b_5, Unset):
            facilities_b_5 = UNSET
        else:
            facilities_b_5 = self.facilities_b_5

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        photo_1: None | str | Unset
        if isinstance(self.photo_1, Unset):
            photo_1 = UNSET
        else:
            photo_1 = self.photo_1

        photo_2: None | str | Unset
        if isinstance(self.photo_2, Unset):
            photo_2 = UNSET
        else:
            photo_2 = self.photo_2

        photo_3: None | str | Unset
        if isinstance(self.photo_3, Unset):
            photo_3 = UNSET
        else:
            photo_3 = self.photo_3

        photo_4: None | str | Unset
        if isinstance(self.photo_4, Unset):
            photo_4 = UNSET
        else:
            photo_4 = self.photo_4

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude_dec: None | str | Unset
        if isinstance(self.longitude_dec, Unset):
            longitude_dec = UNSET
        else:
            longitude_dec = self.longitude_dec

        latitude_dec: None | str | Unset
        if isinstance(self.latitude_dec, Unset):
            latitude_dec = UNSET
        else:
            latitude_dec = self.latitude_dec

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if district_en is not UNSET:
            field_dict["District_en"] = district_en
        if district_cn is not UNSET:
            field_dict["District_cn"] = district_cn
        if name_en is not UNSET:
            field_dict["Name_en"] = name_en
        if name_cn is not UNSET:
            field_dict["Name_cn"] = name_cn
        if address_en is not UNSET:
            field_dict["Address_en"] = address_en
        if address_cn is not UNSET:
            field_dict["Address_cn"] = address_cn
        if gihs is not UNSET:
            field_dict["GIHS"] = gihs
        if facilities_en is not UNSET:
            field_dict["Facilities_en"] = facilities_en
        if facilities_b_5 is not UNSET:
            field_dict["Facilities_b5"] = facilities_b_5
        if phone is not UNSET:
            field_dict["Phone"] = phone
        if photo_1 is not UNSET:
            field_dict["Photo_1"] = photo_1
        if photo_2 is not UNSET:
            field_dict["Photo_2"] = photo_2
        if photo_3 is not UNSET:
            field_dict["Photo_3"] = photo_3
        if photo_4 is not UNSET:
            field_dict["Photo_4"] = photo_4
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude_dec is not UNSET:
            field_dict["Longitude_dec"] = longitude_dec
        if latitude_dec is not UNSET:
            field_dict["Latitude_dec"] = latitude_dec
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_en", UNSET))

        def _parse_district_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_cn = _parse_district_cn(d.pop("District_cn", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("Name_en", UNSET))

        def _parse_name_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_cn = _parse_name_cn(d.pop("Name_cn", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_en", UNSET))

        def _parse_address_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_cn = _parse_address_cn(d.pop("Address_cn", UNSET))

        def _parse_gihs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gihs = _parse_gihs(d.pop("GIHS", UNSET))

        def _parse_facilities_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facilities_en = _parse_facilities_en(d.pop("Facilities_en", UNSET))

        def _parse_facilities_b_5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facilities_b_5 = _parse_facilities_b_5(d.pop("Facilities_b5", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("Phone", UNSET))

        def _parse_photo_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_1 = _parse_photo_1(d.pop("Photo_1", UNSET))

        def _parse_photo_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_2 = _parse_photo_2(d.pop("Photo_2", UNSET))

        def _parse_photo_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_3 = _parse_photo_3(d.pop("Photo_3", UNSET))

        def _parse_photo_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_4 = _parse_photo_4(d.pop("Photo_4", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude_dec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude_dec = _parse_longitude_dec(d.pop("Longitude_dec", UNSET))

        def _parse_latitude_dec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude_dec = _parse_latitude_dec(d.pop("Latitude_dec", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            district_en=district_en,
            district_cn=district_cn,
            name_en=name_en,
            name_cn=name_cn,
            address_en=address_en,
            address_cn=address_cn,
            gihs=gihs,
            facilities_en=facilities_en,
            facilities_b_5=facilities_b_5,
            phone=phone,
            photo_1=photo_1,
            photo_2=photo_2,
            photo_3=photo_3,
            photo_4=photo_4,
            longitude=longitude,
            latitude=latitude,
            longitude_dec=longitude_dec,
            latitude_dec=latitude_dec,
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
