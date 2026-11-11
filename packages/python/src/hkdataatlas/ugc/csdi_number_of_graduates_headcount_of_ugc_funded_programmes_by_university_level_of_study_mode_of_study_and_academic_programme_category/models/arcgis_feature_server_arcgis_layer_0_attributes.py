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
        academic_programme_category_en (None | str | Unset): Publisher field type: esriFieldTypeString
        academic_programme_category_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        academic_year (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        level_of_study_en (None | str | Unset): Publisher field type: esriFieldTypeString
        level_of_study_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mode_of_study_en (None | str | Unset): Publisher field type: esriFieldTypeString
        mode_of_study_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        number_of_graduates_headcount (float | None | Unset): Publisher field type: esriFieldTypeDouble
        university_en (None | str | Unset): Publisher field type: esriFieldTypeString
        university_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    academic_programme_category_en: None | str | Unset = UNSET
    academic_programme_category_tc: None | str | Unset = UNSET
    academic_year: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    level_of_study_en: None | str | Unset = UNSET
    level_of_study_tc: None | str | Unset = UNSET
    longitude: float | None | Unset = UNSET
    mode_of_study_en: None | str | Unset = UNSET
    mode_of_study_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    number_of_graduates_headcount: float | None | Unset = UNSET
    university_en: None | str | Unset = UNSET
    university_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        academic_programme_category_en: None | str | Unset
        if isinstance(self.academic_programme_category_en, Unset):
            academic_programme_category_en = UNSET
        else:
            academic_programme_category_en = self.academic_programme_category_en

        academic_programme_category_tc: None | str | Unset
        if isinstance(self.academic_programme_category_tc, Unset):
            academic_programme_category_tc = UNSET
        else:
            academic_programme_category_tc = self.academic_programme_category_tc

        academic_year: None | str | Unset
        if isinstance(self.academic_year, Unset):
            academic_year = UNSET
        else:
            academic_year = self.academic_year

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

        number_of_graduates_headcount: float | None | Unset
        if isinstance(self.number_of_graduates_headcount, Unset):
            number_of_graduates_headcount = UNSET
        else:
            number_of_graduates_headcount = self.number_of_graduates_headcount

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
        if academic_programme_category_en is not UNSET:
            field_dict["Academic_Programme_Category_EN"] = (
                academic_programme_category_en
            )
        if academic_programme_category_tc is not UNSET:
            field_dict["Academic_Programme_Category_TC"] = (
                academic_programme_category_tc
            )
        if academic_year is not UNSET:
            field_dict["Academic_Year"] = academic_year
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if level_of_study_en is not UNSET:
            field_dict["Level_of_study_EN"] = level_of_study_en
        if level_of_study_tc is not UNSET:
            field_dict["Level_of_study_TC"] = level_of_study_tc
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if mode_of_study_en is not UNSET:
            field_dict["Mode_of_study_EN"] = mode_of_study_en
        if mode_of_study_tc is not UNSET:
            field_dict["Mode_of_study_TC"] = mode_of_study_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if number_of_graduates_headcount is not UNSET:
            field_dict["Number_of_Graduates_Headcount"] = number_of_graduates_headcount
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

        def _parse_academic_programme_category_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        academic_programme_category_en = _parse_academic_programme_category_en(
            d.pop("Academic_Programme_Category_EN", UNSET)
        )

        def _parse_academic_programme_category_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        academic_programme_category_tc = _parse_academic_programme_category_tc(
            d.pop("Academic_Programme_Category_TC", UNSET)
        )

        def _parse_academic_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        academic_year = _parse_academic_year(d.pop("Academic_Year", UNSET))

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

        level_of_study_en = _parse_level_of_study_en(d.pop("Level_of_study_EN", UNSET))

        def _parse_level_of_study_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        level_of_study_tc = _parse_level_of_study_tc(d.pop("Level_of_study_TC", UNSET))

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

        mode_of_study_en = _parse_mode_of_study_en(d.pop("Mode_of_study_EN", UNSET))

        def _parse_mode_of_study_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode_of_study_tc = _parse_mode_of_study_tc(d.pop("Mode_of_study_TC", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_number_of_graduates_headcount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        number_of_graduates_headcount = _parse_number_of_graduates_headcount(
            d.pop("Number_of_Graduates_Headcount", UNSET)
        )

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
            academic_programme_category_en=academic_programme_category_en,
            academic_programme_category_tc=academic_programme_category_tc,
            academic_year=academic_year,
            easting=easting,
            latitude=latitude,
            level_of_study_en=level_of_study_en,
            level_of_study_tc=level_of_study_tc,
            longitude=longitude,
            mode_of_study_en=mode_of_study_en,
            mode_of_study_tc=mode_of_study_tc,
            northing=northing,
            number_of_graduates_headcount=number_of_graduates_headcount,
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
