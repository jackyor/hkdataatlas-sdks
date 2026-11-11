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
        academic_year (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        employment_situation_en (None | str | Unset): Publisher field type: esriFieldTypeString
        employment_situation_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        level_of_study_en (None | str | Unset): Publisher field type: esriFieldTypeString
        level_of_study_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        number_of_graduates_headcount (float | None | Unset): Publisher field type: esriFieldTypeDouble
        occupation_en (None | str | Unset): Publisher field type: esriFieldTypeString
        occupation_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        university_en (None | str | Unset): Publisher field type: esriFieldTypeString
        university_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    academic_year: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    employment_situation_en: None | str | Unset = UNSET
    employment_situation_tc: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    level_of_study_en: None | str | Unset = UNSET
    level_of_study_tc: None | str | Unset = UNSET
    longitude: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    number_of_graduates_headcount: float | None | Unset = UNSET
    occupation_en: None | str | Unset = UNSET
    occupation_tc: None | str | Unset = UNSET
    university_en: None | str | Unset = UNSET
    university_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        employment_situation_en: None | str | Unset
        if isinstance(self.employment_situation_en, Unset):
            employment_situation_en = UNSET
        else:
            employment_situation_en = self.employment_situation_en

        employment_situation_tc: None | str | Unset
        if isinstance(self.employment_situation_tc, Unset):
            employment_situation_tc = UNSET
        else:
            employment_situation_tc = self.employment_situation_tc

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

        occupation_en: None | str | Unset
        if isinstance(self.occupation_en, Unset):
            occupation_en = UNSET
        else:
            occupation_en = self.occupation_en

        occupation_tc: None | str | Unset
        if isinstance(self.occupation_tc, Unset):
            occupation_tc = UNSET
        else:
            occupation_tc = self.occupation_tc

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
        if academic_year is not UNSET:
            field_dict["Academic_Year"] = academic_year
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if employment_situation_en is not UNSET:
            field_dict["Employment_Situation_EN"] = employment_situation_en
        if employment_situation_tc is not UNSET:
            field_dict["Employment_Situation_TC"] = employment_situation_tc
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if level_of_study_en is not UNSET:
            field_dict["Level_of_study_EN"] = level_of_study_en
        if level_of_study_tc is not UNSET:
            field_dict["Level_of_study_TC"] = level_of_study_tc
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if number_of_graduates_headcount is not UNSET:
            field_dict["Number_of_Graduates_Headcount"] = number_of_graduates_headcount
        if occupation_en is not UNSET:
            field_dict["Occupation_EN"] = occupation_en
        if occupation_tc is not UNSET:
            field_dict["Occupation_TC"] = occupation_tc
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

        def _parse_employment_situation_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employment_situation_en = _parse_employment_situation_en(
            d.pop("Employment_Situation_EN", UNSET)
        )

        def _parse_employment_situation_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        employment_situation_tc = _parse_employment_situation_tc(
            d.pop("Employment_Situation_TC", UNSET)
        )

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

        def _parse_occupation_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        occupation_en = _parse_occupation_en(d.pop("Occupation_EN", UNSET))

        def _parse_occupation_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        occupation_tc = _parse_occupation_tc(d.pop("Occupation_TC", UNSET))

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
            academic_year=academic_year,
            easting=easting,
            employment_situation_en=employment_situation_en,
            employment_situation_tc=employment_situation_tc,
            latitude=latitude,
            level_of_study_en=level_of_study_en,
            level_of_study_tc=level_of_study_tc,
            longitude=longitude,
            northing=northing,
            number_of_graduates_headcount=number_of_graduates_headcount,
            occupation_en=occupation_en,
            occupation_tc=occupation_tc,
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
