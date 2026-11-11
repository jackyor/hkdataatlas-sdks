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
        parking_id (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (None | str | Unset): Publisher field type: esriFieldTypeString
        basic_info_en (None | str | Unset): Publisher field type: esriFieldTypeString
        basic_info_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        parking_vacancy (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    parking_id: int | None | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_ch: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    basic_info_en: None | str | Unset = UNSET
    basic_info_ch: None | str | Unset = UNSET
    parking_vacancy: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        parking_id: int | None | Unset
        if isinstance(self.parking_id, Unset):
            parking_id = UNSET
        else:
            parking_id = self.parking_id

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_ch: None | str | Unset
        if isinstance(self.name_ch, Unset):
            name_ch = UNSET
        else:
            name_ch = self.name_ch

        easting: None | str | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: None | str | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        basic_info_en: None | str | Unset
        if isinstance(self.basic_info_en, Unset):
            basic_info_en = UNSET
        else:
            basic_info_en = self.basic_info_en

        basic_info_ch: None | str | Unset
        if isinstance(self.basic_info_ch, Unset):
            basic_info_ch = UNSET
        else:
            basic_info_ch = self.basic_info_ch

        parking_vacancy: None | str | Unset
        if isinstance(self.parking_vacancy, Unset):
            parking_vacancy = UNSET
        else:
            parking_vacancy = self.parking_vacancy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if parking_id is not UNSET:
            field_dict["PARKING_ID"] = parking_id
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if name_ch is not UNSET:
            field_dict["NAME_CH"] = name_ch
        if easting is not UNSET:
            field_dict["EASTING"] = easting
        if northing is not UNSET:
            field_dict["NORTHING"] = northing
        if basic_info_en is not UNSET:
            field_dict["BASIC_INFO_EN"] = basic_info_en
        if basic_info_ch is not UNSET:
            field_dict["BASIC_INFO_CH"] = basic_info_ch
        if parking_vacancy is not UNSET:
            field_dict["PARKING_VACANCY"] = parking_vacancy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_parking_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parking_id = _parse_parking_id(d.pop("PARKING_ID", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NAME_EN", UNSET))

        def _parse_name_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_ch = _parse_name_ch(d.pop("NAME_CH", UNSET))

        def _parse_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

        def _parse_basic_info_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        basic_info_en = _parse_basic_info_en(d.pop("BASIC_INFO_EN", UNSET))

        def _parse_basic_info_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        basic_info_ch = _parse_basic_info_ch(d.pop("BASIC_INFO_CH", UNSET))

        def _parse_parking_vacancy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parking_vacancy = _parse_parking_vacancy(d.pop("PARKING_VACANCY", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            parking_id=parking_id,
            name_en=name_en,
            name_ch=name_ch,
            easting=easting,
            northing=northing,
            basic_info_en=basic_info_en,
            basic_info_ch=basic_info_ch,
            parking_vacancy=parking_vacancy,
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
