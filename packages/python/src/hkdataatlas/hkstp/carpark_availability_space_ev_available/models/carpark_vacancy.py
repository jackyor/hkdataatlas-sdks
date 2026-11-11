from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.carpark_vacancy_private_car import CarparkVacancyPrivateCar


T = TypeVar("T", bound="CarparkVacancy")


@_attrs_define
class CarparkVacancy:
    """
    Attributes:
        carpark (str | Unset): The code of carpark.
        private_car (CarparkVacancyPrivateCar | Unset): Object enclosing EV vacancy information.
    """

    carpark: str | Unset = UNSET
    private_car: CarparkVacancyPrivateCar | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carpark = self.carpark

        private_car: dict[str, Any] | Unset = UNSET
        if not isinstance(self.private_car, Unset):
            private_car = self.private_car.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carpark is not UNSET:
            field_dict["carpark"] = carpark
        if private_car is not UNSET:
            field_dict["privateCar"] = private_car

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.carpark_vacancy_private_car import CarparkVacancyPrivateCar

        d = dict(src_dict)
        carpark = d.pop("carpark", UNSET)

        _private_car = d.pop("privateCar", UNSET)
        private_car: CarparkVacancyPrivateCar | Unset
        if isinstance(_private_car, Unset):
            private_car = UNSET
        else:
            private_car = CarparkVacancyPrivateCar.from_dict(_private_car)

        carpark_vacancy = cls(
            carpark=carpark,
            private_car=private_car,
        )

        carpark_vacancy.additional_properties = d
        return carpark_vacancy

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
