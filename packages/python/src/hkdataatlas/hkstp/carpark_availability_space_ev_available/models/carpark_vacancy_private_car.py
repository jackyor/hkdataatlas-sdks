from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CarparkVacancyPrivateCar")


@_attrs_define
class CarparkVacancyPrivateCar:
    """Object enclosing EV vacancy information.

    Attributes:
        vacancy_ev (int | Unset): Number of available EV parking spaces for the public.
    """

    vacancy_ev: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vacancy_ev = self.vacancy_ev

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vacancy_ev is not UNSET:
            field_dict["vacancyEV"] = vacancy_ev

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vacancy_ev = d.pop("vacancyEV", UNSET)

        carpark_vacancy_private_car = cls(
            vacancy_ev=vacancy_ev,
        )

        carpark_vacancy_private_car.additional_properties = d
        return carpark_vacancy_private_car

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
