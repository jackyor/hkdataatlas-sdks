from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vacancy_record_category import (
    VacancyRecordCategory,
    check_vacancy_record_category,
)
from ..models.vacancy_record_vacancy_type import (
    VacancyRecordVacancyType,
    check_vacancy_record_vacancy_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VacancyRecord")


@_attrs_define
class VacancyRecord:
    """
    Attributes:
        lastupdate (str): Last update date from the car park owner (YYYY-MM-DD HH:MM:SS).
        vacancy (float): Available parking spaces for this vehicle type, including electronic and non-electronic
            vehicles. For type A, 0 means full and -1 means the operator provided no data. For type B, 0 means full, 1 means
            spaces available, and -1 means the operator provided no data. Type C always returns 0.
        vacancy_type (VacancyRecordVacancyType): Vacancy type: A means availability with an actual number; B means
            availability without an actual number; C means the car park is closed.
        category (VacancyRecordCategory | Unset):
        vacancy_dis (float | Unset): Available parking spaces for this electronic vehicle type assigned to disabled
            persons.
        vacancy_ev (float | Unset): Available parking spaces for this electronic vehicle type only.
        vacancy_unl (float | Unset): Available unloading spaces for this electronic vehicle type.
    """

    lastupdate: str
    vacancy: float
    vacancy_type: VacancyRecordVacancyType
    category: VacancyRecordCategory | Unset = UNSET
    vacancy_dis: float | Unset = UNSET
    vacancy_ev: float | Unset = UNSET
    vacancy_unl: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lastupdate = self.lastupdate

        vacancy = self.vacancy

        vacancy_type: str = self.vacancy_type

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        vacancy_dis = self.vacancy_dis

        vacancy_ev = self.vacancy_ev

        vacancy_unl = self.vacancy_unl

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lastupdate": lastupdate,
                "vacancy": vacancy,
                "vacancy_type": vacancy_type,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if vacancy_dis is not UNSET:
            field_dict["vacancyDIS"] = vacancy_dis
        if vacancy_ev is not UNSET:
            field_dict["vacancyEV"] = vacancy_ev
        if vacancy_unl is not UNSET:
            field_dict["vacancyUNL"] = vacancy_unl

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lastupdate = d.pop("lastupdate")

        vacancy = d.pop("vacancy")

        vacancy_type = check_vacancy_record_vacancy_type(d.pop("vacancy_type"))

        _category = d.pop("category", UNSET)
        category: VacancyRecordCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_vacancy_record_category(_category)

        vacancy_dis = d.pop("vacancyDIS", UNSET)

        vacancy_ev = d.pop("vacancyEV", UNSET)

        vacancy_unl = d.pop("vacancyUNL", UNSET)

        vacancy_record = cls(
            lastupdate=lastupdate,
            vacancy=vacancy,
            vacancy_type=vacancy_type,
            category=category,
            vacancy_dis=vacancy_dis,
            vacancy_ev=vacancy_ev,
            vacancy_unl=vacancy_unl,
        )

        vacancy_record.additional_properties = d
        return vacancy_record

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
