from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.publisher_dictionary_student_enrolment_record_level_of_study_en import (
    PublisherDictionaryStudentEnrolmentRecordLevelOfStudyEN,
    check_publisher_dictionary_student_enrolment_record_level_of_study_en,
)
from ..models.publisher_dictionary_student_enrolment_record_level_of_study_tc import (
    PublisherDictionaryStudentEnrolmentRecordLevelOfStudyTC,
    check_publisher_dictionary_student_enrolment_record_level_of_study_tc,
)
from ..models.publisher_dictionary_student_enrolment_record_mode_of_study_en import (
    PublisherDictionaryStudentEnrolmentRecordModeOfStudyEN,
    check_publisher_dictionary_student_enrolment_record_mode_of_study_en,
)
from ..models.publisher_dictionary_student_enrolment_record_mode_of_study_tc import (
    PublisherDictionaryStudentEnrolmentRecordModeOfStudyTC,
    check_publisher_dictionary_student_enrolment_record_mode_of_study_tc,
)
from ..models.publisher_dictionary_student_enrolment_record_sex_en import (
    PublisherDictionaryStudentEnrolmentRecordSexEN,
    check_publisher_dictionary_student_enrolment_record_sex_en,
)
from ..models.publisher_dictionary_student_enrolment_record_sex_tc import (
    PublisherDictionaryStudentEnrolmentRecordSexTC,
    check_publisher_dictionary_student_enrolment_record_sex_tc,
)
from ..models.publisher_dictionary_student_enrolment_record_university_en import (
    PublisherDictionaryStudentEnrolmentRecordUniversityEN,
    check_publisher_dictionary_student_enrolment_record_university_en,
)
from ..models.publisher_dictionary_student_enrolment_record_university_tc import (
    PublisherDictionaryStudentEnrolmentRecordUniversityTC,
    check_publisher_dictionary_student_enrolment_record_university_tc,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PublisherDictionaryStudentEnrolmentRecord")


@_attrs_define
class PublisherDictionaryStudentEnrolmentRecord:
    """Fields listed in the publisher data dictionary for student enrolment headcount. The dictionary specifies field
    formats and admissible values, but does not define a complete API response structure. Supporting semantic context
    from the publisher DOCX dictionary https://www.ugcs.gov.hk/datagovhk/Students2_data_dictionary_en.docx. Native
    ArcGIS/WFS wire names and types remain in their own operation schemas; a dictionary-to-wire mapping is not asserted.

        Attributes:
            academic_year (str | Unset): Academic year, in the format YYYY/YY (for example, 2018/19).
            level_of_study_en (PublisherDictionaryStudentEnrolmentRecordLevelOfStudyEN | Unset): Level of study in English.
            level_of_study_tc (PublisherDictionaryStudentEnrolmentRecordLevelOfStudyTC | Unset): Level of study in
                Traditional Chinese.
            mode_of_study_en (PublisherDictionaryStudentEnrolmentRecordModeOfStudyEN | Unset): Mode of study in English.
            mode_of_study_tc (PublisherDictionaryStudentEnrolmentRecordModeOfStudyTC | Unset): Mode of study in Traditional
                Chinese.
            sex_en (PublisherDictionaryStudentEnrolmentRecordSexEN | Unset): Sex in English.
            sex_tc (PublisherDictionaryStudentEnrolmentRecordSexTC | Unset): Sex in Traditional Chinese.
            student_enrolment_headcount (int | Unset): Student enrolment headcount.
            university_en (PublisherDictionaryStudentEnrolmentRecordUniversityEN | Unset): University name in English.
            university_tc (PublisherDictionaryStudentEnrolmentRecordUniversityTC | Unset): University name in Traditional
                Chinese, corresponding to the English university names listed by the dictionary.
    """

    academic_year: str | Unset = UNSET
    level_of_study_en: (
        PublisherDictionaryStudentEnrolmentRecordLevelOfStudyEN | Unset
    ) = UNSET
    level_of_study_tc: (
        PublisherDictionaryStudentEnrolmentRecordLevelOfStudyTC | Unset
    ) = UNSET
    mode_of_study_en: PublisherDictionaryStudentEnrolmentRecordModeOfStudyEN | Unset = (
        UNSET
    )
    mode_of_study_tc: PublisherDictionaryStudentEnrolmentRecordModeOfStudyTC | Unset = (
        UNSET
    )
    sex_en: PublisherDictionaryStudentEnrolmentRecordSexEN | Unset = UNSET
    sex_tc: PublisherDictionaryStudentEnrolmentRecordSexTC | Unset = UNSET
    student_enrolment_headcount: int | Unset = UNSET
    university_en: PublisherDictionaryStudentEnrolmentRecordUniversityEN | Unset = UNSET
    university_tc: PublisherDictionaryStudentEnrolmentRecordUniversityTC | Unset = UNSET
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

        sex_en: str | Unset = UNSET
        if not isinstance(self.sex_en, Unset):
            sex_en = self.sex_en

        sex_tc: str | Unset = UNSET
        if not isinstance(self.sex_tc, Unset):
            sex_tc = self.sex_tc

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
        if sex_en is not UNSET:
            field_dict["Sex_EN"] = sex_en
        if sex_tc is not UNSET:
            field_dict["Sex_TC"] = sex_tc
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
            PublisherDictionaryStudentEnrolmentRecordLevelOfStudyEN | Unset
        )
        if isinstance(_level_of_study_en, Unset):
            level_of_study_en = UNSET
        else:
            level_of_study_en = (
                check_publisher_dictionary_student_enrolment_record_level_of_study_en(
                    _level_of_study_en
                )
            )

        _level_of_study_tc = d.pop("Level of study_TC", UNSET)
        level_of_study_tc: (
            PublisherDictionaryStudentEnrolmentRecordLevelOfStudyTC | Unset
        )
        if isinstance(_level_of_study_tc, Unset):
            level_of_study_tc = UNSET
        else:
            level_of_study_tc = (
                check_publisher_dictionary_student_enrolment_record_level_of_study_tc(
                    _level_of_study_tc
                )
            )

        _mode_of_study_en = d.pop("Mode of study_EN", UNSET)
        mode_of_study_en: PublisherDictionaryStudentEnrolmentRecordModeOfStudyEN | Unset
        if isinstance(_mode_of_study_en, Unset):
            mode_of_study_en = UNSET
        else:
            mode_of_study_en = (
                check_publisher_dictionary_student_enrolment_record_mode_of_study_en(
                    _mode_of_study_en
                )
            )

        _mode_of_study_tc = d.pop("Mode of study_TC", UNSET)
        mode_of_study_tc: PublisherDictionaryStudentEnrolmentRecordModeOfStudyTC | Unset
        if isinstance(_mode_of_study_tc, Unset):
            mode_of_study_tc = UNSET
        else:
            mode_of_study_tc = (
                check_publisher_dictionary_student_enrolment_record_mode_of_study_tc(
                    _mode_of_study_tc
                )
            )

        _sex_en = d.pop("Sex_EN", UNSET)
        sex_en: PublisherDictionaryStudentEnrolmentRecordSexEN | Unset
        if isinstance(_sex_en, Unset):
            sex_en = UNSET
        else:
            sex_en = check_publisher_dictionary_student_enrolment_record_sex_en(_sex_en)

        _sex_tc = d.pop("Sex_TC", UNSET)
        sex_tc: PublisherDictionaryStudentEnrolmentRecordSexTC | Unset
        if isinstance(_sex_tc, Unset):
            sex_tc = UNSET
        else:
            sex_tc = check_publisher_dictionary_student_enrolment_record_sex_tc(_sex_tc)

        student_enrolment_headcount = d.pop("Student Enrolment (Headcount)", UNSET)

        _university_en = d.pop("University_EN", UNSET)
        university_en: PublisherDictionaryStudentEnrolmentRecordUniversityEN | Unset
        if isinstance(_university_en, Unset):
            university_en = UNSET
        else:
            university_en = (
                check_publisher_dictionary_student_enrolment_record_university_en(
                    _university_en
                )
            )

        _university_tc = d.pop("University_TC", UNSET)
        university_tc: PublisherDictionaryStudentEnrolmentRecordUniversityTC | Unset
        if isinstance(_university_tc, Unset):
            university_tc = UNSET
        else:
            university_tc = (
                check_publisher_dictionary_student_enrolment_record_university_tc(
                    _university_tc
                )
            )

        publisher_dictionary_student_enrolment_record = cls(
            academic_year=academic_year,
            level_of_study_en=level_of_study_en,
            level_of_study_tc=level_of_study_tc,
            mode_of_study_en=mode_of_study_en,
            mode_of_study_tc=mode_of_study_tc,
            sex_en=sex_en,
            sex_tc=sex_tc,
            student_enrolment_headcount=student_enrolment_headcount,
            university_en=university_en,
            university_tc=university_tc,
        )

        publisher_dictionary_student_enrolment_record.additional_properties = d
        return publisher_dictionary_student_enrolment_record

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
