from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publisher_dictionary_student_enrolment_headcount_data_dictionary_academic_programme_category_en import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryEN,
    check_publisher_dictionary_student_enrolment_headcount_data_dictionary_academic_programme_category_en,
)
from ..models.publisher_dictionary_student_enrolment_headcount_data_dictionary_academic_programme_category_tc import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryTC,
    check_publisher_dictionary_student_enrolment_headcount_data_dictionary_academic_programme_category_tc,
)
from ..models.publisher_dictionary_student_enrolment_headcount_data_dictionary_level_of_study_en import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyEN,
    check_publisher_dictionary_student_enrolment_headcount_data_dictionary_level_of_study_en,
)
from ..models.publisher_dictionary_student_enrolment_headcount_data_dictionary_level_of_study_tc import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyTC,
    check_publisher_dictionary_student_enrolment_headcount_data_dictionary_level_of_study_tc,
)
from ..models.publisher_dictionary_student_enrolment_headcount_data_dictionary_mode_of_study_en import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyEN,
    check_publisher_dictionary_student_enrolment_headcount_data_dictionary_mode_of_study_en,
)
from ..models.publisher_dictionary_student_enrolment_headcount_data_dictionary_mode_of_study_tc import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyTC,
    check_publisher_dictionary_student_enrolment_headcount_data_dictionary_mode_of_study_tc,
)
from ..models.publisher_dictionary_student_enrolment_headcount_data_dictionary_university_en import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityEN,
    check_publisher_dictionary_student_enrolment_headcount_data_dictionary_university_en,
)
from ..models.publisher_dictionary_student_enrolment_headcount_data_dictionary_university_tc import (
    PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityTC,
    check_publisher_dictionary_student_enrolment_headcount_data_dictionary_university_tc,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublisherDictionaryStudentEnrolmentHeadcountDataDictionary")


@_attrs_define
class PublisherDictionaryStudentEnrolmentHeadcountDataDictionary:
    """Dictionary for Student Enrolment (Headcount) of UGC-funded Programmes by University, Level of Study, Mode of Study
    and Academic Programme Category. This describes data fields, not a documented HTTP response schema. Supporting
    semantic context from the publisher DOCX dictionary
    https://www.ugcs.gov.hk/datagovhk/Students3_data_dictionary_en.docx. Native ArcGIS/WFS wire names and types remain
    in their own operation schemas; a dictionary-to-wire mapping is not asserted.

        Attributes:
            academic_programme_category_en
                (PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryEN | Unset): Academic
                Programme Category in English.
            academic_programme_category_tc
                (PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryTC | Unset): Academic
                Programme Category in Traditional Chinese.
            academic_year (str | Unset): Academic year in YYYY/YY format (for example, 2018/19).
            level_of_study_en (PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyEN | Unset): Level of
                study in English.
            level_of_study_tc (PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyTC | Unset): Level of
                study in Traditional Chinese.
            mode_of_study_en (PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyEN | Unset): Mode of
                study in English.
            mode_of_study_tc (PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyTC | Unset): Mode of
                study in Traditional Chinese.
            student_enrolment_headcount (int | Unset): Student enrolment headcount. The dictionary declares an Integer
                format. Some UGC-funded programmes map to multiple academic programme categories and are allocated across those
                categories on a pro rata basis; the resulting figures may be decimal. Figures in this table are rounded to the
                nearest whole number and may not add up to corresponding totals.
            university_en (PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityEN | Unset): University name
                in English.
            university_tc (PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityTC | Unset): University name
                in Traditional Chinese.
    """

    academic_programme_category_en: (
        PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryEN
        | Unset
    ) = UNSET
    academic_programme_category_tc: (
        PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryTC
        | Unset
    ) = UNSET
    academic_year: str | Unset = UNSET
    level_of_study_en: (
        PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyEN | Unset
    ) = UNSET
    level_of_study_tc: (
        PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyTC | Unset
    ) = UNSET
    mode_of_study_en: (
        PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyEN | Unset
    ) = UNSET
    mode_of_study_tc: (
        PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyTC | Unset
    ) = UNSET
    student_enrolment_headcount: int | Unset = UNSET
    university_en: (
        PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityEN | Unset
    ) = UNSET
    university_tc: (
        PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityTC | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        academic_programme_category_en: str | Unset = UNSET
        if not isinstance(self.academic_programme_category_en, Unset):
            academic_programme_category_en = self.academic_programme_category_en

        academic_programme_category_tc: str | Unset = UNSET
        if not isinstance(self.academic_programme_category_tc, Unset):
            academic_programme_category_tc = self.academic_programme_category_tc

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
        if academic_programme_category_en is not UNSET:
            field_dict["Academic Programme Category_EN"] = (
                academic_programme_category_en
            )
        if academic_programme_category_tc is not UNSET:
            field_dict["Academic Programme Category_TC"] = (
                academic_programme_category_tc
            )
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
        _academic_programme_category_en = d.pop("Academic Programme Category_EN", UNSET)
        academic_programme_category_en: (
            PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryEN
            | Unset
        )
        if isinstance(_academic_programme_category_en, Unset):
            academic_programme_category_en = UNSET
        else:
            academic_programme_category_en = check_publisher_dictionary_student_enrolment_headcount_data_dictionary_academic_programme_category_en(
                _academic_programme_category_en
            )

        _academic_programme_category_tc = d.pop("Academic Programme Category_TC", UNSET)
        academic_programme_category_tc: (
            PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryAcademicProgrammeCategoryTC
            | Unset
        )
        if isinstance(_academic_programme_category_tc, Unset):
            academic_programme_category_tc = UNSET
        else:
            academic_programme_category_tc = check_publisher_dictionary_student_enrolment_headcount_data_dictionary_academic_programme_category_tc(
                _academic_programme_category_tc
            )

        academic_year = d.pop("Academic Year", UNSET)

        _level_of_study_en = d.pop("Level of study_EN", UNSET)
        level_of_study_en: (
            PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyEN
            | Unset
        )
        if isinstance(_level_of_study_en, Unset):
            level_of_study_en = UNSET
        else:
            level_of_study_en = check_publisher_dictionary_student_enrolment_headcount_data_dictionary_level_of_study_en(
                _level_of_study_en
            )

        _level_of_study_tc = d.pop("Level of study_TC", UNSET)
        level_of_study_tc: (
            PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryLevelOfStudyTC
            | Unset
        )
        if isinstance(_level_of_study_tc, Unset):
            level_of_study_tc = UNSET
        else:
            level_of_study_tc = check_publisher_dictionary_student_enrolment_headcount_data_dictionary_level_of_study_tc(
                _level_of_study_tc
            )

        _mode_of_study_en = d.pop("Mode of study_EN", UNSET)
        mode_of_study_en: (
            PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyEN
            | Unset
        )
        if isinstance(_mode_of_study_en, Unset):
            mode_of_study_en = UNSET
        else:
            mode_of_study_en = check_publisher_dictionary_student_enrolment_headcount_data_dictionary_mode_of_study_en(
                _mode_of_study_en
            )

        _mode_of_study_tc = d.pop("Mode of study_TC", UNSET)
        mode_of_study_tc: (
            PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryModeOfStudyTC
            | Unset
        )
        if isinstance(_mode_of_study_tc, Unset):
            mode_of_study_tc = UNSET
        else:
            mode_of_study_tc = check_publisher_dictionary_student_enrolment_headcount_data_dictionary_mode_of_study_tc(
                _mode_of_study_tc
            )

        student_enrolment_headcount = d.pop("Student Enrolment (Headcount)", UNSET)

        _university_en = d.pop("University_EN", UNSET)
        university_en: (
            PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityEN
            | Unset
        )
        if isinstance(_university_en, Unset):
            university_en = UNSET
        else:
            university_en = check_publisher_dictionary_student_enrolment_headcount_data_dictionary_university_en(
                _university_en
            )

        _university_tc = d.pop("University_TC", UNSET)
        university_tc: (
            PublisherDictionaryStudentEnrolmentHeadcountDataDictionaryUniversityTC
            | Unset
        )
        if isinstance(_university_tc, Unset):
            university_tc = UNSET
        else:
            university_tc = check_publisher_dictionary_student_enrolment_headcount_data_dictionary_university_tc(
                _university_tc
            )

        publisher_dictionary_student_enrolment_headcount_data_dictionary = cls(
            academic_programme_category_en=academic_programme_category_en,
            academic_programme_category_tc=academic_programme_category_tc,
            academic_year=academic_year,
            level_of_study_en=level_of_study_en,
            level_of_study_tc=level_of_study_tc,
            mode_of_study_en=mode_of_study_en,
            mode_of_study_tc=mode_of_study_tc,
            student_enrolment_headcount=student_enrolment_headcount,
            university_en=university_en,
            university_tc=university_tc,
        )

        publisher_dictionary_student_enrolment_headcount_data_dictionary.additional_properties = d
        return publisher_dictionary_student_enrolment_headcount_data_dictionary

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
