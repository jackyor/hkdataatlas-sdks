from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publisher_dictionary_student_enrolment_data_dictionary_level_of_study_en import (
    PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyEN,
    check_publisher_dictionary_student_enrolment_data_dictionary_level_of_study_en,
)
from ..models.publisher_dictionary_student_enrolment_data_dictionary_level_of_study_tc import (
    PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyTC,
    check_publisher_dictionary_student_enrolment_data_dictionary_level_of_study_tc,
)
from ..models.publisher_dictionary_student_enrolment_data_dictionary_mode_of_study_en import (
    PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyEN,
    check_publisher_dictionary_student_enrolment_data_dictionary_mode_of_study_en,
)
from ..models.publisher_dictionary_student_enrolment_data_dictionary_mode_of_study_tc import (
    PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyTC,
    check_publisher_dictionary_student_enrolment_data_dictionary_mode_of_study_tc,
)
from ..models.publisher_dictionary_student_enrolment_data_dictionary_place_of_origin_en import (
    PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginEN,
    check_publisher_dictionary_student_enrolment_data_dictionary_place_of_origin_en,
)
from ..models.publisher_dictionary_student_enrolment_data_dictionary_place_of_origin_tc import (
    PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginTC,
    check_publisher_dictionary_student_enrolment_data_dictionary_place_of_origin_tc,
)
from ..models.publisher_dictionary_student_enrolment_data_dictionary_university_en import (
    PublisherDictionaryStudentEnrolmentDataDictionaryUniversityEN,
    check_publisher_dictionary_student_enrolment_data_dictionary_university_en,
)
from ..models.publisher_dictionary_student_enrolment_data_dictionary_university_tc import (
    PublisherDictionaryStudentEnrolmentDataDictionaryUniversityTC,
    check_publisher_dictionary_student_enrolment_data_dictionary_university_tc,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublisherDictionaryStudentEnrolmentDataDictionary")


@_attrs_define
class PublisherDictionaryStudentEnrolmentDataDictionary:
    """Data dictionary for Student Enrolment of UGC-funded Programmes by University, Level of Study, Place of Origin and
    Mode of Study. The source describes data items and formats, not a complete API response object. Supporting semantic
    context from the publisher DOCX dictionary https://www.ugcs.gov.hk/datagovhk/Student_data_dictionary_en.docx. Native
    ArcGIS/WFS wire names and types remain in their own operation schemas; a dictionary-to-wire mapping is not asserted.

        Attributes:
            academic_year (str | Unset): Academic year in YYYY/YY format; the source gives 2018/19 as an example.
            level_of_study_en (PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyEN | Unset): Level of study in
                English.
            level_of_study_tc (PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyTC | Unset): Level of study in
                Traditional Chinese.
            mode_of_study_en (PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyEN | Unset): Mode of study in
                English.
            mode_of_study_tc (PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyTC | Unset): Mode of study in
                Traditional Chinese.
            place_of_origin_en (PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginEN | Unset): Place of origin
                in English.
            place_of_origin_tc (PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginTC | Unset): Place of origin
                in Traditional Chinese.
            student_enrolment_headcount (int | Unset): Student enrolment expressed as headcount.
            university_en (PublisherDictionaryStudentEnrolmentDataDictionaryUniversityEN | Unset): University name in
                English.
            university_tc (PublisherDictionaryStudentEnrolmentDataDictionaryUniversityTC | Unset): University name in
                Traditional Chinese.
    """

    academic_year: str | Unset = UNSET
    level_of_study_en: (
        PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyEN | Unset
    ) = UNSET
    level_of_study_tc: (
        PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyTC | Unset
    ) = UNSET
    mode_of_study_en: (
        PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyEN | Unset
    ) = UNSET
    mode_of_study_tc: (
        PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyTC | Unset
    ) = UNSET
    place_of_origin_en: (
        PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginEN | Unset
    ) = UNSET
    place_of_origin_tc: (
        PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginTC | Unset
    ) = UNSET
    student_enrolment_headcount: int | Unset = UNSET
    university_en: (
        PublisherDictionaryStudentEnrolmentDataDictionaryUniversityEN | Unset
    ) = UNSET
    university_tc: (
        PublisherDictionaryStudentEnrolmentDataDictionaryUniversityTC | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        academic_year = self.academic_year

        level_of_study_en: str | Unset = UNSET
        if not isinstance(self.level_of_study_en, Unset):
            level_of_study_en = self.level_of_study_en

        level_of_study_tc: str | Unset = UNSET
        if not isinstance(self.level_of_study_tc, Unset):
            level_of_study_tc = self.level_of_study_tc

        mode_of_study_en: str | Unset = UNSET
        if not isinstance(self.mode_of_study_en, Unset):
            mode_of_study_en = self.mode_of_study_en

        mode_of_study_tc: str | Unset = UNSET
        if not isinstance(self.mode_of_study_tc, Unset):
            mode_of_study_tc = self.mode_of_study_tc

        place_of_origin_en: str | Unset = UNSET
        if not isinstance(self.place_of_origin_en, Unset):
            place_of_origin_en = self.place_of_origin_en

        place_of_origin_tc: str | Unset = UNSET
        if not isinstance(self.place_of_origin_tc, Unset):
            place_of_origin_tc = self.place_of_origin_tc

        student_enrolment_headcount = self.student_enrolment_headcount

        university_en: str | Unset = UNSET
        if not isinstance(self.university_en, Unset):
            university_en = self.university_en

        university_tc: str | Unset = UNSET
        if not isinstance(self.university_tc, Unset):
            university_tc = self.university_tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if academic_year is not UNSET:
            field_dict["Academic Year"] = academic_year
        if level_of_study_en is not UNSET:
            field_dict["Level of study_EN"] = level_of_study_en
        if level_of_study_tc is not UNSET:
            field_dict["Level of study_TC"] = level_of_study_tc
        if mode_of_study_en is not UNSET:
            field_dict["Mode of study_EN"] = mode_of_study_en
        if mode_of_study_tc is not UNSET:
            field_dict["Mode of study_TC"] = mode_of_study_tc
        if place_of_origin_en is not UNSET:
            field_dict["Place of Origin_EN"] = place_of_origin_en
        if place_of_origin_tc is not UNSET:
            field_dict["Place of Origin_TC"] = place_of_origin_tc
        if student_enrolment_headcount is not UNSET:
            field_dict["Student Enrolment (Headcount)"] = student_enrolment_headcount
        if university_en is not UNSET:
            field_dict["University_EN"] = university_en
        if university_tc is not UNSET:
            field_dict["University_TC"] = university_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        academic_year = d.pop("Academic Year", UNSET)

        _level_of_study_en = d.pop("Level of study_EN", UNSET)
        level_of_study_en: (
            PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyEN | Unset
        )
        if isinstance(_level_of_study_en, Unset):
            level_of_study_en = UNSET
        else:
            level_of_study_en = check_publisher_dictionary_student_enrolment_data_dictionary_level_of_study_en(
                _level_of_study_en
            )

        _level_of_study_tc = d.pop("Level of study_TC", UNSET)
        level_of_study_tc: (
            PublisherDictionaryStudentEnrolmentDataDictionaryLevelOfStudyTC | Unset
        )
        if isinstance(_level_of_study_tc, Unset):
            level_of_study_tc = UNSET
        else:
            level_of_study_tc = check_publisher_dictionary_student_enrolment_data_dictionary_level_of_study_tc(
                _level_of_study_tc
            )

        _mode_of_study_en = d.pop("Mode of study_EN", UNSET)
        mode_of_study_en: (
            PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyEN | Unset
        )
        if isinstance(_mode_of_study_en, Unset):
            mode_of_study_en = UNSET
        else:
            mode_of_study_en = check_publisher_dictionary_student_enrolment_data_dictionary_mode_of_study_en(
                _mode_of_study_en
            )

        _mode_of_study_tc = d.pop("Mode of study_TC", UNSET)
        mode_of_study_tc: (
            PublisherDictionaryStudentEnrolmentDataDictionaryModeOfStudyTC | Unset
        )
        if isinstance(_mode_of_study_tc, Unset):
            mode_of_study_tc = UNSET
        else:
            mode_of_study_tc = check_publisher_dictionary_student_enrolment_data_dictionary_mode_of_study_tc(
                _mode_of_study_tc
            )

        _place_of_origin_en = d.pop("Place of Origin_EN", UNSET)
        place_of_origin_en: (
            PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginEN | Unset
        )
        if isinstance(_place_of_origin_en, Unset):
            place_of_origin_en = UNSET
        else:
            place_of_origin_en = check_publisher_dictionary_student_enrolment_data_dictionary_place_of_origin_en(
                _place_of_origin_en
            )

        _place_of_origin_tc = d.pop("Place of Origin_TC", UNSET)
        place_of_origin_tc: (
            PublisherDictionaryStudentEnrolmentDataDictionaryPlaceOfOriginTC | Unset
        )
        if isinstance(_place_of_origin_tc, Unset):
            place_of_origin_tc = UNSET
        else:
            place_of_origin_tc = check_publisher_dictionary_student_enrolment_data_dictionary_place_of_origin_tc(
                _place_of_origin_tc
            )

        student_enrolment_headcount = d.pop("Student Enrolment (Headcount)", UNSET)

        _university_en = d.pop("University_EN", UNSET)
        university_en: (
            PublisherDictionaryStudentEnrolmentDataDictionaryUniversityEN | Unset
        )
        if isinstance(_university_en, Unset):
            university_en = UNSET
        else:
            university_en = check_publisher_dictionary_student_enrolment_data_dictionary_university_en(
                _university_en
            )

        _university_tc = d.pop("University_TC", UNSET)
        university_tc: (
            PublisherDictionaryStudentEnrolmentDataDictionaryUniversityTC | Unset
        )
        if isinstance(_university_tc, Unset):
            university_tc = UNSET
        else:
            university_tc = check_publisher_dictionary_student_enrolment_data_dictionary_university_tc(
                _university_tc
            )

        publisher_dictionary_student_enrolment_data_dictionary = cls(
            academic_year=academic_year,
            level_of_study_en=level_of_study_en,
            level_of_study_tc=level_of_study_tc,
            mode_of_study_en=mode_of_study_en,
            mode_of_study_tc=mode_of_study_tc,
            place_of_origin_en=place_of_origin_en,
            place_of_origin_tc=place_of_origin_tc,
            student_enrolment_headcount=student_enrolment_headcount,
            university_en=university_en,
            university_tc=university_tc,
        )

        publisher_dictionary_student_enrolment_data_dictionary.additional_properties = d
        return publisher_dictionary_student_enrolment_data_dictionary

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
