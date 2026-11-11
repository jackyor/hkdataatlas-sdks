from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobVacancy")


@_attrs_define
class JobVacancy:
    """A vacancy record. The documented field dictionary supplies these names and types; it does not specify required
    fields or prohibit additional properties. The example represents date fields as ISO 8601 date-time strings with a
    +08:00 offset, although the dictionary labels them Date.

        Attributes:
            career_level (str | Unset): Career Level
            company_name (str | Unset): Company Name
            education_level (str | Unset): Education Level
            employment_term (str | Unset): Employment Term
            employment_type (str | Unset): Employment Type
            job_industry (str | Unset): Job Industry
            job_position (str | Unset): Job Position
            job_ref_no (None | str | Unset): Job Reference Number
            post_end_date (datetime.datetime | Unset): Post End Date. The dictionary labels this field Date; the published
                example uses an ISO 8601 date-time value with a +08:00 offset.
            post_start_date (datetime.datetime | Unset): Post Start Date. The dictionary labels this field Date; the
                published example uses an ISO 8601 date-time value with a +08:00 offset.
            salary (str | Unset): Salary Range
            work_experience (str | Unset): Work Experience
            work_location (str | Unset): Work Location
    """

    career_level: str | Unset = UNSET
    company_name: str | Unset = UNSET
    education_level: str | Unset = UNSET
    employment_term: str | Unset = UNSET
    employment_type: str | Unset = UNSET
    job_industry: str | Unset = UNSET
    job_position: str | Unset = UNSET
    job_ref_no: None | str | Unset = UNSET
    post_end_date: datetime.datetime | Unset = UNSET
    post_start_date: datetime.datetime | Unset = UNSET
    salary: str | Unset = UNSET
    work_experience: str | Unset = UNSET
    work_location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        career_level = self.career_level

        company_name = self.company_name

        education_level = self.education_level

        employment_term = self.employment_term

        employment_type = self.employment_type

        job_industry = self.job_industry

        job_position = self.job_position

        job_ref_no: None | str | Unset
        if isinstance(self.job_ref_no, Unset):
            job_ref_no = UNSET
        else:
            job_ref_no = self.job_ref_no

        post_end_date: str | Unset = UNSET
        if not isinstance(self.post_end_date, Unset):
            post_end_date = self.post_end_date.isoformat()

        post_start_date: str | Unset = UNSET
        if not isinstance(self.post_start_date, Unset):
            post_start_date = self.post_start_date.isoformat()

        salary = self.salary

        work_experience = self.work_experience

        work_location = self.work_location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if career_level is not UNSET:
            field_dict["Career_Level"] = career_level
        if company_name is not UNSET:
            field_dict["Company_Name"] = company_name
        if education_level is not UNSET:
            field_dict["Education_Level"] = education_level
        if employment_term is not UNSET:
            field_dict["Employment_Term"] = employment_term
        if employment_type is not UNSET:
            field_dict["Employment_Type"] = employment_type
        if job_industry is not UNSET:
            field_dict["Job_Industry"] = job_industry
        if job_position is not UNSET:
            field_dict["Job_Position"] = job_position
        if job_ref_no is not UNSET:
            field_dict["Job_Ref_No"] = job_ref_no
        if post_end_date is not UNSET:
            field_dict["Post_End_Date"] = post_end_date
        if post_start_date is not UNSET:
            field_dict["Post_Start_Date"] = post_start_date
        if salary is not UNSET:
            field_dict["Salary"] = salary
        if work_experience is not UNSET:
            field_dict["Work_Experience"] = work_experience
        if work_location is not UNSET:
            field_dict["Work_Location"] = work_location

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        career_level = d.pop("Career_Level", UNSET)

        company_name = d.pop("Company_Name", UNSET)

        education_level = d.pop("Education_Level", UNSET)

        employment_term = d.pop("Employment_Term", UNSET)

        employment_type = d.pop("Employment_Type", UNSET)

        job_industry = d.pop("Job_Industry", UNSET)

        job_position = d.pop("Job_Position", UNSET)

        def _parse_job_ref_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_ref_no = _parse_job_ref_no(d.pop("Job_Ref_No", UNSET))

        _post_end_date = d.pop("Post_End_Date", UNSET)
        post_end_date: datetime.datetime | Unset
        if isinstance(_post_end_date, Unset):
            post_end_date = UNSET
        else:
            post_end_date = datetime.datetime.fromisoformat(_post_end_date)

        _post_start_date = d.pop("Post_Start_Date", UNSET)
        post_start_date: datetime.datetime | Unset
        if isinstance(_post_start_date, Unset):
            post_start_date = UNSET
        else:
            post_start_date = datetime.datetime.fromisoformat(_post_start_date)

        salary = d.pop("Salary", UNSET)

        work_experience = d.pop("Work_Experience", UNSET)

        work_location = d.pop("Work_Location", UNSET)

        job_vacancy = cls(
            career_level=career_level,
            company_name=company_name,
            education_level=education_level,
            employment_term=employment_term,
            employment_type=employment_type,
            job_industry=job_industry,
            job_position=job_position,
            job_ref_no=job_ref_no,
            post_end_date=post_end_date,
            post_start_date=post_start_date,
            salary=salary,
            work_experience=work_experience,
            work_location=work_location,
        )

        job_vacancy.additional_properties = d
        return job_vacancy

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
