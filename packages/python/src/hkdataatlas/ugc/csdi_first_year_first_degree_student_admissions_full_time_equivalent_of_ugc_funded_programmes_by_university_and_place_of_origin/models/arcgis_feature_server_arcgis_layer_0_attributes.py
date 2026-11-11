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
        fyfd_student_admissions_fte (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        place_of_origin_en (None | str | Unset): Publisher field type: esriFieldTypeString
        place_of_origin_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        university_en (None | str | Unset): Publisher field type: esriFieldTypeString
        university_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    academic_year: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    fyfd_student_admissions_fte: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    place_of_origin_en: None | str | Unset = UNSET
    place_of_origin_tc: None | str | Unset = UNSET
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

        fyfd_student_admissions_fte: float | None | Unset
        if isinstance(self.fyfd_student_admissions_fte, Unset):
            fyfd_student_admissions_fte = UNSET
        else:
            fyfd_student_admissions_fte = self.fyfd_student_admissions_fte

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

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        place_of_origin_en: None | str | Unset
        if isinstance(self.place_of_origin_en, Unset):
            place_of_origin_en = UNSET
        else:
            place_of_origin_en = self.place_of_origin_en

        place_of_origin_tc: None | str | Unset
        if isinstance(self.place_of_origin_tc, Unset):
            place_of_origin_tc = UNSET
        else:
            place_of_origin_tc = self.place_of_origin_tc

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
        if fyfd_student_admissions_fte is not UNSET:
            field_dict["FYFD_Student_Admissions_FTE"] = fyfd_student_admissions_fte
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if place_of_origin_en is not UNSET:
            field_dict["Place_of_Origin_EN"] = place_of_origin_en
        if place_of_origin_tc is not UNSET:
            field_dict["Place_of_Origin_TC"] = place_of_origin_tc
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

        def _parse_fyfd_student_admissions_fte(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fyfd_student_admissions_fte = _parse_fyfd_student_admissions_fte(
            d.pop("FYFD_Student_Admissions_FTE", UNSET)
        )

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

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_place_of_origin_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_of_origin_en = _parse_place_of_origin_en(
            d.pop("Place_of_Origin_EN", UNSET)
        )

        def _parse_place_of_origin_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_of_origin_tc = _parse_place_of_origin_tc(
            d.pop("Place_of_Origin_TC", UNSET)
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
            fyfd_student_admissions_fte=fyfd_student_admissions_fte,
            latitude=latitude,
            longitude=longitude,
            northing=northing,
            place_of_origin_en=place_of_origin_en,
            place_of_origin_tc=place_of_origin_tc,
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
