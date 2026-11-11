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
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        level_of_study_en (None | str | Unset): Publisher field type: esriFieldTypeString
        level_of_study_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mode_of_study_en (None | str | Unset): Publisher field type: esriFieldTypeString
        mode_of_study_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        programme_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        programme_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        university_en (None | str | Unset): Publisher field type: esriFieldTypeString
        university_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    level_of_study_en: None | str | Unset = UNSET
    level_of_study_tc: None | str | Unset = UNSET
    longitude: float | None | Unset = UNSET
    mode_of_study_en: None | str | Unset = UNSET
    mode_of_study_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    programme_name_en: None | str | Unset = UNSET
    programme_name_tc: None | str | Unset = UNSET
    university_en: None | str | Unset = UNSET
    university_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        level_of_study_en: None | str | Unset
        if isinstance(self.level_of_study_en, Unset):
            level_of_study_en = UNSET
        else:
            level_of_study_en = self.level_of_study_en

        level_of_study_tc: None | str | Unset
        if isinstance(self.level_of_study_tc, Unset):
            level_of_study_tc = UNSET
        else:
            level_of_study_tc = self.level_of_study_tc

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        mode_of_study_en: None | str | Unset
        if isinstance(self.mode_of_study_en, Unset):
            mode_of_study_en = UNSET
        else:
            mode_of_study_en = self.mode_of_study_en

        mode_of_study_tc: None | str | Unset
        if isinstance(self.mode_of_study_tc, Unset):
            mode_of_study_tc = UNSET
        else:
            mode_of_study_tc = self.mode_of_study_tc

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        programme_name_en: None | str | Unset
        if isinstance(self.programme_name_en, Unset):
            programme_name_en = UNSET
        else:
            programme_name_en = self.programme_name_en

        programme_name_tc: None | str | Unset
        if isinstance(self.programme_name_tc, Unset):
            programme_name_tc = UNSET
        else:
            programme_name_tc = self.programme_name_tc

        university_en: None | str | Unset
        if isinstance(self.university_en, Unset):
            university_en = UNSET
        else:
            university_en = self.university_en

        university_tc: None | str | Unset
        if isinstance(self.university_tc, Unset):
            university_tc = UNSET
        else:
            university_tc = self.university_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if level_of_study_en is not UNSET:
            field_dict["Level_of_Study_EN"] = level_of_study_en
        if level_of_study_tc is not UNSET:
            field_dict["Level_of_Study_TC"] = level_of_study_tc
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if mode_of_study_en is not UNSET:
            field_dict["Mode_of_Study_EN"] = mode_of_study_en
        if mode_of_study_tc is not UNSET:
            field_dict["Mode_of_Study_TC"] = mode_of_study_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if programme_name_en is not UNSET:
            field_dict["Programme_Name_EN"] = programme_name_en
        if programme_name_tc is not UNSET:
            field_dict["Programme_Name_TC"] = programme_name_tc
        if university_en is not UNSET:
            field_dict["University_EN"] = university_en
        if university_tc is not UNSET:
            field_dict["University_TC"] = university_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_level_of_study_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        level_of_study_en = _parse_level_of_study_en(d.pop("Level_of_Study_EN", UNSET))

        def _parse_level_of_study_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        level_of_study_tc = _parse_level_of_study_tc(d.pop("Level_of_Study_TC", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_mode_of_study_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode_of_study_en = _parse_mode_of_study_en(d.pop("Mode_of_Study_EN", UNSET))

        def _parse_mode_of_study_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode_of_study_tc = _parse_mode_of_study_tc(d.pop("Mode_of_Study_TC", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_programme_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programme_name_en = _parse_programme_name_en(d.pop("Programme_Name_EN", UNSET))

        def _parse_programme_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        programme_name_tc = _parse_programme_name_tc(d.pop("Programme_Name_TC", UNSET))

        def _parse_university_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        university_en = _parse_university_en(d.pop("University_EN", UNSET))

        def _parse_university_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        university_tc = _parse_university_tc(d.pop("University_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            easting=easting,
            latitude=latitude,
            level_of_study_en=level_of_study_en,
            level_of_study_tc=level_of_study_tc,
            longitude=longitude,
            mode_of_study_en=mode_of_study_en,
            mode_of_study_tc=mode_of_study_tc,
            northing=northing,
            programme_name_en=programme_name_en,
            programme_name_tc=programme_name_tc,
            university_en=university_en,
            university_tc=university_tc,
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
