from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        academic_year (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        level_of_study_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        level_of_study_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        mode_of_study_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        mode_of_study_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        place_of_origin_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        place_of_origin_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        student_enrolment_headcount (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected
            from XML occurrence into all JSON queries.
        university_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        university_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    academic_year: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    level_of_study_en: None | str | Unset = UNSET
    level_of_study_tc: None | str | Unset = UNSET
    longitude: float | None | Unset = UNSET
    mode_of_study_en: None | str | Unset = UNSET
    mode_of_study_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    place_of_origin_en: None | str | Unset = UNSET
    place_of_origin_tc: None | str | Unset = UNSET
    student_enrolment_headcount: float | None | Unset = UNSET
    university_en: None | str | Unset = UNSET
    university_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
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

        student_enrolment_headcount: float | None | Unset
        if isinstance(self.student_enrolment_headcount, Unset):
            student_enrolment_headcount = UNSET
        else:
            student_enrolment_headcount = self.student_enrolment_headcount

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

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if place_of_origin_en is not UNSET:
            field_dict["Place_of_Origin_EN"] = place_of_origin_en
        if place_of_origin_tc is not UNSET:
            field_dict["Place_of_Origin_TC"] = place_of_origin_tc
        if student_enrolment_headcount is not UNSET:
            field_dict["Student_Enrolment_Headcount"] = student_enrolment_headcount
        if university_en is not UNSET:
            field_dict["University_EN"] = university_en
        if university_tc is not UNSET:
            field_dict["University_TC"] = university_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

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

        def _parse_student_enrolment_headcount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        student_enrolment_headcount = _parse_student_enrolment_headcount(
            d.pop("Student_Enrolment_Headcount", UNSET)
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

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            academic_year=academic_year,
            easting=easting,
            latitude=latitude,
            level_of_study_en=level_of_study_en,
            level_of_study_tc=level_of_study_tc,
            longitude=longitude,
            mode_of_study_en=mode_of_study_en,
            mode_of_study_tc=mode_of_study_tc,
            northing=northing,
            place_of_origin_en=place_of_origin_en,
            place_of_origin_tc=place_of_origin_tc,
            student_enrolment_headcount=student_enrolment_headcount,
            university_en=university_en,
            university_tc=university_tc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
