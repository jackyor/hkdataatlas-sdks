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
        student_survey_title_en (None | str | Unset): Publisher field type: esriFieldTypeString
        student_survey_title_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        student_survey_table_en (None | str | Unset): Publisher field type: esriFieldTypeString
        student_survey_table_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        year (None | str | Unset): Publisher field type: esriFieldTypeString
        education_level_en_oa (None | str | Unset): Publisher field type: esriFieldTypeString
        education_level_tc_oa (None | str | Unset): Publisher field type: esriFieldTypeString
        estimated_number_oa (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_oa (None | str | Unset): Publisher field type: esriFieldTypeString
        education_level_en_up (None | str | Unset): Publisher field type: esriFieldTypeString
        education_level_tc_up (None | str | Unset): Publisher field type: esriFieldTypeString
        estimated_number_up (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_up (None | str | Unset): Publisher field type: esriFieldTypeString
        education_level_en_se (None | str | Unset): Publisher field type: esriFieldTypeString
        education_level_tc_se (None | str | Unset): Publisher field type: esriFieldTypeString
        estimated_number_se (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_se (None | str | Unset): Publisher field type: esriFieldTypeString
        education_level_en_ps (None | str | Unset): Publisher field type: esriFieldTypeString
        education_level_tc_ps (None | str | Unset): Publisher field type: esriFieldTypeString
        estimated_number_ps (None | str | Unset): Publisher field type: esriFieldTypeString
        percentage_ps (None | str | Unset): Publisher field type: esriFieldTypeString
        fid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    student_survey_title_en: None | str | Unset = UNSET
    student_survey_title_tc: None | str | Unset = UNSET
    student_survey_table_en: None | str | Unset = UNSET
    student_survey_table_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    year: None | str | Unset = UNSET
    education_level_en_oa: None | str | Unset = UNSET
    education_level_tc_oa: None | str | Unset = UNSET
    estimated_number_oa: None | str | Unset = UNSET
    percentage_oa: None | str | Unset = UNSET
    education_level_en_up: None | str | Unset = UNSET
    education_level_tc_up: None | str | Unset = UNSET
    estimated_number_up: None | str | Unset = UNSET
    percentage_up: None | str | Unset = UNSET
    education_level_en_se: None | str | Unset = UNSET
    education_level_tc_se: None | str | Unset = UNSET
    estimated_number_se: None | str | Unset = UNSET
    percentage_se: None | str | Unset = UNSET
    education_level_en_ps: None | str | Unset = UNSET
    education_level_tc_ps: None | str | Unset = UNSET
    estimated_number_ps: None | str | Unset = UNSET
    percentage_ps: None | str | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        student_survey_title_en: None | str | Unset
        if isinstance(self.student_survey_title_en, Unset):
            student_survey_title_en = UNSET
        else:
            student_survey_title_en = self.student_survey_title_en

        student_survey_title_tc: None | str | Unset
        if isinstance(self.student_survey_title_tc, Unset):
            student_survey_title_tc = UNSET
        else:
            student_survey_title_tc = self.student_survey_title_tc

        student_survey_table_en: None | str | Unset
        if isinstance(self.student_survey_table_en, Unset):
            student_survey_table_en = UNSET
        else:
            student_survey_table_en = self.student_survey_table_en

        student_survey_table_tc: None | str | Unset
        if isinstance(self.student_survey_table_tc, Unset):
            student_survey_table_tc = UNSET
        else:
            student_survey_table_tc = self.student_survey_table_tc

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

        year: None | str | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        education_level_en_oa: None | str | Unset
        if isinstance(self.education_level_en_oa, Unset):
            education_level_en_oa = UNSET
        else:
            education_level_en_oa = self.education_level_en_oa

        education_level_tc_oa: None | str | Unset
        if isinstance(self.education_level_tc_oa, Unset):
            education_level_tc_oa = UNSET
        else:
            education_level_tc_oa = self.education_level_tc_oa

        estimated_number_oa: None | str | Unset
        if isinstance(self.estimated_number_oa, Unset):
            estimated_number_oa = UNSET
        else:
            estimated_number_oa = self.estimated_number_oa

        percentage_oa: None | str | Unset
        if isinstance(self.percentage_oa, Unset):
            percentage_oa = UNSET
        else:
            percentage_oa = self.percentage_oa

        education_level_en_up: None | str | Unset
        if isinstance(self.education_level_en_up, Unset):
            education_level_en_up = UNSET
        else:
            education_level_en_up = self.education_level_en_up

        education_level_tc_up: None | str | Unset
        if isinstance(self.education_level_tc_up, Unset):
            education_level_tc_up = UNSET
        else:
            education_level_tc_up = self.education_level_tc_up

        estimated_number_up: None | str | Unset
        if isinstance(self.estimated_number_up, Unset):
            estimated_number_up = UNSET
        else:
            estimated_number_up = self.estimated_number_up

        percentage_up: None | str | Unset
        if isinstance(self.percentage_up, Unset):
            percentage_up = UNSET
        else:
            percentage_up = self.percentage_up

        education_level_en_se: None | str | Unset
        if isinstance(self.education_level_en_se, Unset):
            education_level_en_se = UNSET
        else:
            education_level_en_se = self.education_level_en_se

        education_level_tc_se: None | str | Unset
        if isinstance(self.education_level_tc_se, Unset):
            education_level_tc_se = UNSET
        else:
            education_level_tc_se = self.education_level_tc_se

        estimated_number_se: None | str | Unset
        if isinstance(self.estimated_number_se, Unset):
            estimated_number_se = UNSET
        else:
            estimated_number_se = self.estimated_number_se

        percentage_se: None | str | Unset
        if isinstance(self.percentage_se, Unset):
            percentage_se = UNSET
        else:
            percentage_se = self.percentage_se

        education_level_en_ps: None | str | Unset
        if isinstance(self.education_level_en_ps, Unset):
            education_level_en_ps = UNSET
        else:
            education_level_en_ps = self.education_level_en_ps

        education_level_tc_ps: None | str | Unset
        if isinstance(self.education_level_tc_ps, Unset):
            education_level_tc_ps = UNSET
        else:
            education_level_tc_ps = self.education_level_tc_ps

        estimated_number_ps: None | str | Unset
        if isinstance(self.estimated_number_ps, Unset):
            estimated_number_ps = UNSET
        else:
            estimated_number_ps = self.estimated_number_ps

        percentage_ps: None | str | Unset
        if isinstance(self.percentage_ps, Unset):
            percentage_ps = UNSET
        else:
            percentage_ps = self.percentage_ps

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
        if student_survey_title_en is not UNSET:
            field_dict["Student_survey_title_en"] = student_survey_title_en
        if student_survey_title_tc is not UNSET:
            field_dict["Student_survey_title_tc"] = student_survey_title_tc
        if student_survey_table_en is not UNSET:
            field_dict["Student_survey_table_en"] = student_survey_table_en
        if student_survey_table_tc is not UNSET:
            field_dict["Student_survey_table_tc"] = student_survey_table_tc
        if district_en is not UNSET:
            field_dict["District_en"] = district_en
        if district_tc is not UNSET:
            field_dict["District_tc"] = district_tc
        if year is not UNSET:
            field_dict["Year"] = year
        if education_level_en_oa is not UNSET:
            field_dict["Education_level_en_OA"] = education_level_en_oa
        if education_level_tc_oa is not UNSET:
            field_dict["Education_level_tc_OA"] = education_level_tc_oa
        if estimated_number_oa is not UNSET:
            field_dict["Estimated_number_OA"] = estimated_number_oa
        if percentage_oa is not UNSET:
            field_dict["Percentage_OA"] = percentage_oa
        if education_level_en_up is not UNSET:
            field_dict["Education_level_en_UP"] = education_level_en_up
        if education_level_tc_up is not UNSET:
            field_dict["Education_level_tc_UP"] = education_level_tc_up
        if estimated_number_up is not UNSET:
            field_dict["Estimated_number_UP"] = estimated_number_up
        if percentage_up is not UNSET:
            field_dict["Percentage_UP"] = percentage_up
        if education_level_en_se is not UNSET:
            field_dict["Education_level_en_SE"] = education_level_en_se
        if education_level_tc_se is not UNSET:
            field_dict["Education_level_tc_SE"] = education_level_tc_se
        if estimated_number_se is not UNSET:
            field_dict["Estimated_number_SE"] = estimated_number_se
        if percentage_se is not UNSET:
            field_dict["Percentage_SE"] = percentage_se
        if education_level_en_ps is not UNSET:
            field_dict["Education_level_en_PS"] = education_level_en_ps
        if education_level_tc_ps is not UNSET:
            field_dict["Education_level_tc_PS"] = education_level_tc_ps
        if estimated_number_ps is not UNSET:
            field_dict["Estimated_number_PS"] = estimated_number_ps
        if percentage_ps is not UNSET:
            field_dict["Percentage_PS"] = percentage_ps
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

        def _parse_student_survey_title_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_survey_title_en = _parse_student_survey_title_en(
            d.pop("Student_survey_title_en", UNSET)
        )

        def _parse_student_survey_title_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_survey_title_tc = _parse_student_survey_title_tc(
            d.pop("Student_survey_title_tc", UNSET)
        )

        def _parse_student_survey_table_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_survey_table_en = _parse_student_survey_table_en(
            d.pop("Student_survey_table_en", UNSET)
        )

        def _parse_student_survey_table_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        student_survey_table_tc = _parse_student_survey_table_tc(
            d.pop("Student_survey_table_tc", UNSET)
        )

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_en", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_tc", UNSET))

        def _parse_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year = _parse_year(d.pop("Year", UNSET))

        def _parse_education_level_en_oa(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        education_level_en_oa = _parse_education_level_en_oa(
            d.pop("Education_level_en_OA", UNSET)
        )

        def _parse_education_level_tc_oa(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        education_level_tc_oa = _parse_education_level_tc_oa(
            d.pop("Education_level_tc_OA", UNSET)
        )

        def _parse_estimated_number_oa(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_number_oa = _parse_estimated_number_oa(
            d.pop("Estimated_number_OA", UNSET)
        )

        def _parse_percentage_oa(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_oa = _parse_percentage_oa(d.pop("Percentage_OA", UNSET))

        def _parse_education_level_en_up(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        education_level_en_up = _parse_education_level_en_up(
            d.pop("Education_level_en_UP", UNSET)
        )

        def _parse_education_level_tc_up(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        education_level_tc_up = _parse_education_level_tc_up(
            d.pop("Education_level_tc_UP", UNSET)
        )

        def _parse_estimated_number_up(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_number_up = _parse_estimated_number_up(
            d.pop("Estimated_number_UP", UNSET)
        )

        def _parse_percentage_up(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_up = _parse_percentage_up(d.pop("Percentage_UP", UNSET))

        def _parse_education_level_en_se(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        education_level_en_se = _parse_education_level_en_se(
            d.pop("Education_level_en_SE", UNSET)
        )

        def _parse_education_level_tc_se(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        education_level_tc_se = _parse_education_level_tc_se(
            d.pop("Education_level_tc_SE", UNSET)
        )

        def _parse_estimated_number_se(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_number_se = _parse_estimated_number_se(
            d.pop("Estimated_number_SE", UNSET)
        )

        def _parse_percentage_se(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_se = _parse_percentage_se(d.pop("Percentage_SE", UNSET))

        def _parse_education_level_en_ps(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        education_level_en_ps = _parse_education_level_en_ps(
            d.pop("Education_level_en_PS", UNSET)
        )

        def _parse_education_level_tc_ps(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        education_level_tc_ps = _parse_education_level_tc_ps(
            d.pop("Education_level_tc_PS", UNSET)
        )

        def _parse_estimated_number_ps(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_number_ps = _parse_estimated_number_ps(
            d.pop("Estimated_number_PS", UNSET)
        )

        def _parse_percentage_ps(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        percentage_ps = _parse_percentage_ps(d.pop("Percentage_PS", UNSET))

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
            student_survey_title_en=student_survey_title_en,
            student_survey_title_tc=student_survey_title_tc,
            student_survey_table_en=student_survey_table_en,
            student_survey_table_tc=student_survey_table_tc,
            district_en=district_en,
            district_tc=district_tc,
            year=year,
            education_level_en_oa=education_level_en_oa,
            education_level_tc_oa=education_level_tc_oa,
            estimated_number_oa=estimated_number_oa,
            percentage_oa=percentage_oa,
            education_level_en_up=education_level_en_up,
            education_level_tc_up=education_level_tc_up,
            estimated_number_up=estimated_number_up,
            percentage_up=percentage_up,
            education_level_en_se=education_level_en_se,
            education_level_tc_se=education_level_tc_se,
            estimated_number_se=estimated_number_se,
            percentage_se=percentage_se,
            education_level_en_ps=education_level_en_ps,
            education_level_tc_ps=education_level_tc_ps,
            estimated_number_ps=estimated_number_ps,
            percentage_ps=percentage_ps,
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
