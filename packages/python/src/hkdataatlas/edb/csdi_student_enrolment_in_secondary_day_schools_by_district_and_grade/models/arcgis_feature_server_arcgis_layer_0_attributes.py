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
        dataset_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        school_year (None | str | Unset): Publisher field type: esriFieldTypeString
        all_grades (None | str | Unset): Publisher field type: esriFieldTypeString
        s1 (None | str | Unset): Publisher field type: esriFieldTypeString
        s2 (None | str | Unset): Publisher field type: esriFieldTypeString
        s3 (None | str | Unset): Publisher field type: esriFieldTypeString
        s4 (None | str | Unset): Publisher field type: esriFieldTypeString
        s5 (None | str | Unset): Publisher field type: esriFieldTypeString
        s6 (None | str | Unset): Publisher field type: esriFieldTypeString
        s7 (None | str | Unset): Publisher field type: esriFieldTypeString
        fid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    school_year: None | str | Unset = UNSET
    all_grades: None | str | Unset = UNSET
    s1: None | str | Unset = UNSET
    s2: None | str | Unset = UNSET
    s3: None | str | Unset = UNSET
    s4: None | str | Unset = UNSET
    s5: None | str | Unset = UNSET
    s6: None | str | Unset = UNSET
    s7: None | str | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dataset_en: None | str | Unset
        if isinstance(self.dataset_en, Unset):
            dataset_en = UNSET
        else:
            dataset_en = self.dataset_en

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        school_year: None | str | Unset
        if isinstance(self.school_year, Unset):
            school_year = UNSET
        else:
            school_year = self.school_year

        all_grades: None | str | Unset
        if isinstance(self.all_grades, Unset):
            all_grades = UNSET
        else:
            all_grades = self.all_grades

        s1: None | str | Unset
        if isinstance(self.s1, Unset):
            s1 = UNSET
        else:
            s1 = self.s1

        s2: None | str | Unset
        if isinstance(self.s2, Unset):
            s2 = UNSET
        else:
            s2 = self.s2

        s3: None | str | Unset
        if isinstance(self.s3, Unset):
            s3 = UNSET
        else:
            s3 = self.s3

        s4: None | str | Unset
        if isinstance(self.s4, Unset):
            s4 = UNSET
        else:
            s4 = self.s4

        s5: None | str | Unset
        if isinstance(self.s5, Unset):
            s5 = UNSET
        else:
            s5 = self.s5

        s6: None | str | Unset
        if isinstance(self.s6, Unset):
            s6 = UNSET
        else:
            s6 = self.s6

        s7: None | str | Unset
        if isinstance(self.s7, Unset):
            s7 = UNSET
        else:
            s7 = self.s7

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        objectid = self.objectid

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_en is not UNSET:
            field_dict["DATASET_EN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["DATASET_TC"] = dataset_tc
        if district_en is not UNSET:
            field_dict["DISTRICT_EN"] = district_en
        if district_tc is not UNSET:
            field_dict["DISTRICT_TC"] = district_tc
        if school_year is not UNSET:
            field_dict["SCHOOL_YEAR"] = school_year
        if all_grades is not UNSET:
            field_dict["ALL_GRADES"] = all_grades
        if s1 is not UNSET:
            field_dict["S1"] = s1
        if s2 is not UNSET:
            field_dict["S2"] = s2
        if s3 is not UNSET:
            field_dict["S3"] = s3
        if s4 is not UNSET:
            field_dict["S4"] = s4
        if s5 is not UNSET:
            field_dict["S5"] = s5
        if s6 is not UNSET:
            field_dict["S6"] = s6
        if s7 is not UNSET:
            field_dict["S7"] = s7
        if fid is not UNSET:
            field_dict["fid"] = fid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("DATASET_EN", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DATASET_TC", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("DISTRICT_EN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("DISTRICT_TC", UNSET))

        def _parse_school_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school_year = _parse_school_year(d.pop("SCHOOL_YEAR", UNSET))

        def _parse_all_grades(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        all_grades = _parse_all_grades(d.pop("ALL_GRADES", UNSET))

        def _parse_s1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s1 = _parse_s1(d.pop("S1", UNSET))

        def _parse_s2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s2 = _parse_s2(d.pop("S2", UNSET))

        def _parse_s3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s3 = _parse_s3(d.pop("S3", UNSET))

        def _parse_s4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s4 = _parse_s4(d.pop("S4", UNSET))

        def _parse_s5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s5 = _parse_s5(d.pop("S5", UNSET))

        def _parse_s6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s6 = _parse_s6(d.pop("S6", UNSET))

        def _parse_s7(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s7 = _parse_s7(d.pop("S7", UNSET))

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            district_en=district_en,
            district_tc=district_tc,
            school_year=school_year,
            all_grades=all_grades,
            s1=s1,
            s2=s2,
            s3=s3,
            s4=s4,
            s5=s5,
            s6=s6,
            s7=s7,
            fid=fid,
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
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
