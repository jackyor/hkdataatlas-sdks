from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observed_flight_record import ObservedFlightRecord


T = TypeVar("T", bound="ObservedDayGroup")


@_attrs_define
class ObservedDayGroup:
    """Permissive structure of the observed day-group object; no properties are required by this observation.

    Attributes:
        arrival (Any | Unset): Observed key. The official documentation describes whether records are arrival or
            departure flights.
        cargo (Any | Unset): Observed key. The official documentation describes whether records are cargo or passenger
            flights.
        date (Any | Unset): Observed key. The official documentation describes a target date.
        last_updated_time (Any | Unset): Key and value observed in the bounded excerpt.
        list_ (list[ObservedFlightRecord] | Unset): Observed key. The official documentation describes a list of flight
            records; documented record details depend on flight category.
    """

    arrival: Any | Unset = UNSET
    cargo: Any | Unset = UNSET
    date: Any | Unset = UNSET
    last_updated_time: Any | Unset = UNSET
    list_: list[ObservedFlightRecord] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arrival = self.arrival

        cargo = self.cargo

        date = self.date

        last_updated_time = self.last_updated_time

        list_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.list_, Unset):
            list_ = []
            for list_item_data in self.list_:
                list_item = list_item_data.to_dict()
                list_.append(list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arrival is not UNSET:
            field_dict["arrival"] = arrival
        if cargo is not UNSET:
            field_dict["cargo"] = cargo
        if date is not UNSET:
            field_dict["date"] = date
        if last_updated_time is not UNSET:
            field_dict["lastUpdatedTime"] = last_updated_time
        if list_ is not UNSET:
            field_dict["list"] = list_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.observed_flight_record import ObservedFlightRecord

        d = dict(src_dict)
        arrival = d.pop("arrival", UNSET)

        cargo = d.pop("cargo", UNSET)

        date = d.pop("date", UNSET)

        last_updated_time = d.pop("lastUpdatedTime", UNSET)

        _list_ = d.pop("list", UNSET)
        list_: list[ObservedFlightRecord] | Unset = UNSET
        if _list_ is not UNSET:
            list_ = []
            for list_item_data in _list_:
                list_item = ObservedFlightRecord.from_dict(list_item_data)

                list_.append(list_item)

        observed_day_group = cls(
            arrival=arrival,
            cargo=cargo,
            date=date,
            last_updated_time=last_updated_time,
            list_=list_,
        )

        observed_day_group.additional_properties = d
        return observed_day_group

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
