from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.car_park import CarPark


T = TypeVar("T", bound="CarParkResponse")


@_attrs_define
class CarParkResponse:
    """
    Attributes:
        car_parks (list[CarPark] | Unset): All car parks provided by West Kowloon Cultural District.
    """

    car_parks: list[CarPark] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        car_parks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.car_parks, Unset):
            car_parks = []
            for car_parks_item_data in self.car_parks:
                car_parks_item = car_parks_item_data.to_dict()
                car_parks.append(car_parks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if car_parks is not UNSET:
            field_dict["carParks"] = car_parks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.car_park import CarPark

        d = dict(src_dict)
        _car_parks = d.pop("carParks", UNSET)
        car_parks: list[CarPark] | Unset = UNSET
        if _car_parks is not UNSET:
            car_parks = []
            for car_parks_item_data in _car_parks:
                car_parks_item = CarPark.from_dict(car_parks_item_data)

                car_parks.append(car_parks_item)

        car_park_response = cls(
            car_parks=car_parks,
        )

        car_park_response.additional_properties = d
        return car_park_response

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
