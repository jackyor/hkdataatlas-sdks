from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateCarUtilization")


@_attrs_define
class PrivateCarUtilization:
    """Enclosed elements include vacancy, vacancyEV (if applicable), and totalParkingSpace.

    Attributes:
        total_parking_space (float | Unset): Total parking space in the carpark (including EV and Non-EV).
        vacancy (float | Unset): Available parking spaces for public (excluding EV).
        vacancy_ev (float | Unset): Available EV parking spaces for public. Included if applicable.
    """

    total_parking_space: float | Unset = UNSET
    vacancy: float | Unset = UNSET
    vacancy_ev: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_parking_space = self.total_parking_space

        vacancy = self.vacancy

        vacancy_ev = self.vacancy_ev

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_parking_space is not UNSET:
            field_dict["totalParkingSpace"] = total_parking_space
        if vacancy is not UNSET:
            field_dict["vacancy"] = vacancy
        if vacancy_ev is not UNSET:
            field_dict["vacancyEV"] = vacancy_ev

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_parking_space = d.pop("totalParkingSpace", UNSET)

        vacancy = d.pop("vacancy", UNSET)

        vacancy_ev = d.pop("vacancyEV", UNSET)

        private_car_utilization = cls(
            total_parking_space=total_parking_space,
            vacancy=vacancy,
            vacancy_ev=vacancy_ev,
        )

        private_car_utilization.additional_properties = d
        return private_car_utilization

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
