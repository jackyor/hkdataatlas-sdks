from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateCarVacancy")


@_attrs_define
class PrivateCarVacancy:
    """Enclosed elements include the vacancy count for public parking, excluding EV.

    Attributes:
        vacancy (float | Unset): Available parking spaces for public (excluded EV). Example: 57.
    """

    vacancy: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vacancy = self.vacancy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vacancy is not UNSET:
            field_dict["vacancy"] = vacancy

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vacancy = d.pop("vacancy", UNSET)

        private_car_vacancy = cls(
            vacancy=vacancy,
        )

        private_car_vacancy.additional_properties = d
        return private_car_vacancy

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
