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
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        school_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    school_address_en: None | str | Unset = UNSET
    school_address_sc: None | str | Unset = UNSET
    school_address_tc: None | str | Unset = UNSET
    school_name_en: None | str | Unset = UNSET
    school_name_sc: None | str | Unset = UNSET
    school_name_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        school_address_en: None | str | Unset
        if isinstance(self.school_address_en, Unset):
            school_address_en = UNSET
        else:
            school_address_en = self.school_address_en

        school_address_sc: None | str | Unset
        if isinstance(self.school_address_sc, Unset):
            school_address_sc = UNSET
        else:
            school_address_sc = self.school_address_sc

        school_address_tc: None | str | Unset
        if isinstance(self.school_address_tc, Unset):
            school_address_tc = UNSET
        else:
            school_address_tc = self.school_address_tc

        school_name_en: None | str | Unset
        if isinstance(self.school_name_en, Unset):
            school_name_en = UNSET
        else:
            school_name_en = self.school_name_en

        school_name_sc: None | str | Unset
        if isinstance(self.school_name_sc, Unset):
            school_name_sc = UNSET
        else:
            school_name_sc = self.school_name_sc

        school_name_tc: None | str | Unset
        if isinstance(self.school_name_tc, Unset):
            school_name_tc = UNSET
        else:
            school_name_tc = self.school_name_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if school_address_en is not UNSET:
            field_dict["School_Address_EN"] = school_address_en
        if school_address_sc is not UNSET:
            field_dict["School_Address_SC"] = school_address_sc
        if school_address_tc is not UNSET:
            field_dict["School_Address_TC"] = school_address_tc
        if school_name_en is not UNSET:
            field_dict["School_Name_EN"] = school_name_en
        if school_name_sc is not UNSET:
            field_dict["School_Name_SC"] = school_name_sc
        if school_name_tc is not UNSET:
            field_dict["School_Name_TC"] = school_name_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_school_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_address_en = _parse_school_address_en(d.pop("School_Address_EN", UNSET))

        def _parse_school_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_address_sc = _parse_school_address_sc(d.pop("School_Address_SC", UNSET))

        def _parse_school_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_address_tc = _parse_school_address_tc(d.pop("School_Address_TC", UNSET))

        def _parse_school_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_en = _parse_school_name_en(d.pop("School_Name_EN", UNSET))

        def _parse_school_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_sc = _parse_school_name_sc(d.pop("School_Name_SC", UNSET))

        def _parse_school_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_name_tc = _parse_school_name_tc(d.pop("School_Name_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            latitude=latitude,
            longitude=longitude,
            school_address_en=school_address_en,
            school_address_sc=school_address_sc,
            school_address_tc=school_address_tc,
            school_name_en=school_name_en,
            school_name_sc=school_name_sc,
            school_name_tc=school_name_tc,
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
