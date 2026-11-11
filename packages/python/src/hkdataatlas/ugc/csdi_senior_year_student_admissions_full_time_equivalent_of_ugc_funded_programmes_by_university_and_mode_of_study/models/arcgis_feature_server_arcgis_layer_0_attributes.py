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
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mode_of_study_en (None | str | Unset): Publisher field type: esriFieldTypeString
        mode_of_study_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        senior_year_student_admissions_fte (float | None | Unset): Publisher field type: esriFieldTypeDouble
        university_en (None | str | Unset): Publisher field type: esriFieldTypeString
        university_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    academic_year: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    mode_of_study_en: None | str | Unset = UNSET
    mode_of_study_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    senior_year_student_admissions_fte: float | None | Unset = UNSET
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

        senior_year_student_admissions_fte: float | None | Unset
        if isinstance(self.senior_year_student_admissions_fte, Unset):
            senior_year_student_admissions_fte = UNSET
        else:
            senior_year_student_admissions_fte = self.senior_year_student_admissions_fte

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
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if mode_of_study_en is not UNSET:
            field_dict["Mode_of_study_EN"] = mode_of_study_en
        if mode_of_study_tc is not UNSET:
            field_dict["Mode_of_study_TC"] = mode_of_study_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if senior_year_student_admissions_fte is not UNSET:
            field_dict["Senior_year_Student_Admissions_FTE"] = (
                senior_year_student_admissions_fte
            )
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

        def _parse_senior_year_student_admissions_fte(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        senior_year_student_admissions_fte = _parse_senior_year_student_admissions_fte(
            d.pop("Senior_year_Student_Admissions_FTE", UNSET)
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
            academic_year=academic_year,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            mode_of_study_en=mode_of_study_en,
            mode_of_study_tc=mode_of_study_tc,
            northing=northing,
            senior_year_student_admissions_fte=senior_year_student_admissions_fte,
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
