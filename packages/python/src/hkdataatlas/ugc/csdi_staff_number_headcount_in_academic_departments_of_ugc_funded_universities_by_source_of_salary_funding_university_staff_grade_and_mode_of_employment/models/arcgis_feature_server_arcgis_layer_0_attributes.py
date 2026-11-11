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
        mode_of_employment_en (None | str | Unset): Publisher field type: esriFieldTypeString
        mode_of_employment_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        source_of_salary_funding_en (None | str | Unset): Publisher field type: esriFieldTypeString
        source_of_salary_funding_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        staff_grade_en (None | str | Unset): Publisher field type: esriFieldTypeString
        staff_grade_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        staff_no_headcount (float | None | Unset): Publisher field type: esriFieldTypeDouble
        university_en (None | str | Unset): Publisher field type: esriFieldTypeString
        university_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    academic_year: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    mode_of_employment_en: None | str | Unset = UNSET
    mode_of_employment_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    source_of_salary_funding_en: None | str | Unset = UNSET
    source_of_salary_funding_tc: None | str | Unset = UNSET
    staff_grade_en: None | str | Unset = UNSET
    staff_grade_tc: None | str | Unset = UNSET
    staff_no_headcount: float | None | Unset = UNSET
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

        mode_of_employment_en: None | str | Unset
        if isinstance(self.mode_of_employment_en, Unset):
            mode_of_employment_en = UNSET
        else:
            mode_of_employment_en = self.mode_of_employment_en

        mode_of_employment_tc: None | str | Unset
        if isinstance(self.mode_of_employment_tc, Unset):
            mode_of_employment_tc = UNSET
        else:
            mode_of_employment_tc = self.mode_of_employment_tc

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        source_of_salary_funding_en: None | str | Unset
        if isinstance(self.source_of_salary_funding_en, Unset):
            source_of_salary_funding_en = UNSET
        else:
            source_of_salary_funding_en = self.source_of_salary_funding_en

        source_of_salary_funding_tc: None | str | Unset
        if isinstance(self.source_of_salary_funding_tc, Unset):
            source_of_salary_funding_tc = UNSET
        else:
            source_of_salary_funding_tc = self.source_of_salary_funding_tc

        staff_grade_en: None | str | Unset
        if isinstance(self.staff_grade_en, Unset):
            staff_grade_en = UNSET
        else:
            staff_grade_en = self.staff_grade_en

        staff_grade_tc: None | str | Unset
        if isinstance(self.staff_grade_tc, Unset):
            staff_grade_tc = UNSET
        else:
            staff_grade_tc = self.staff_grade_tc

        staff_no_headcount: float | None | Unset
        if isinstance(self.staff_no_headcount, Unset):
            staff_no_headcount = UNSET
        else:
            staff_no_headcount = self.staff_no_headcount

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
            field_dict["Academic_year"] = academic_year
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if mode_of_employment_en is not UNSET:
            field_dict["Mode_of_Employment_EN"] = mode_of_employment_en
        if mode_of_employment_tc is not UNSET:
            field_dict["Mode_of_Employment_TC"] = mode_of_employment_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if source_of_salary_funding_en is not UNSET:
            field_dict["Source_of_Salary_Funding_EN"] = source_of_salary_funding_en
        if source_of_salary_funding_tc is not UNSET:
            field_dict["Source_of_Salary_Funding_TC"] = source_of_salary_funding_tc
        if staff_grade_en is not UNSET:
            field_dict["Staff_Grade_EN"] = staff_grade_en
        if staff_grade_tc is not UNSET:
            field_dict["Staff_Grade_TC"] = staff_grade_tc
        if staff_no_headcount is not UNSET:
            field_dict["Staff_No_Headcount"] = staff_no_headcount
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

        academic_year = _parse_academic_year(d.pop("Academic_year", UNSET))

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

        def _parse_mode_of_employment_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode_of_employment_en = _parse_mode_of_employment_en(
            d.pop("Mode_of_Employment_EN", UNSET)
        )

        def _parse_mode_of_employment_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mode_of_employment_tc = _parse_mode_of_employment_tc(
            d.pop("Mode_of_Employment_TC", UNSET)
        )

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_source_of_salary_funding_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_of_salary_funding_en = _parse_source_of_salary_funding_en(
            d.pop("Source_of_Salary_Funding_EN", UNSET)
        )

        def _parse_source_of_salary_funding_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_of_salary_funding_tc = _parse_source_of_salary_funding_tc(
            d.pop("Source_of_Salary_Funding_TC", UNSET)
        )

        def _parse_staff_grade_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        staff_grade_en = _parse_staff_grade_en(d.pop("Staff_Grade_EN", UNSET))

        def _parse_staff_grade_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        staff_grade_tc = _parse_staff_grade_tc(d.pop("Staff_Grade_TC", UNSET))

        def _parse_staff_no_headcount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        staff_no_headcount = _parse_staff_no_headcount(
            d.pop("Staff_No_Headcount", UNSET)
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
            mode_of_employment_en=mode_of_employment_en,
            mode_of_employment_tc=mode_of_employment_tc,
            northing=northing,
            source_of_salary_funding_en=source_of_salary_funding_en,
            source_of_salary_funding_tc=source_of_salary_funding_tc,
            staff_grade_en=staff_grade_en,
            staff_grade_tc=staff_grade_tc,
            staff_no_headcount=staff_no_headcount,
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
