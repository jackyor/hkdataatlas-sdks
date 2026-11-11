from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observed_flight_number import ObservedFlightNumber


T = TypeVar("T", bound="ObservedFlightRecord")


@_attrs_define
class ObservedFlightRecord:
    """Permissive structure of an observed flight record. The official documentation describes record semantics, not exact
    wire keys or types. Arrival passenger records include documented meanings for port of origin, baggage reclaim belt,
    arrival hall, terminal code, parking stand, arrival time, and flight number list. Departure passenger records
    describe port of destination, terminal code, check-in aisle, boarding gate, time (labelled 'Time of arrival' in the
    source), and flight number list. Cargo arrival records describe port of origin, time of arrival, and flight number
    list. Cargo departure records describe port of destination, time (labelled 'Time of arrival' in the source), and
    flight number list.

        Attributes:
            baggage (Any | Unset): Observed key. The source describes the baggage reclaim belt number for arrival passenger
                records.
            flight (list[ObservedFlightNumber] | Unset): Observed key for flight-number entries. The source describes a
                flight number list.
            hall (Any | Unset): Observed key. The source describes the arrival hall for arrival passenger records.
            origin (Any | Unset): Observed key. The source describes the port of origin for arrival records.
            stand (Any | Unset): Observed key. The source describes the parking stand number for arrival passenger records.
            status (Any | Unset): Observed key. The source describes the latest status of the flight.
            status_code (Any | Unset): Observed key. The source describes a status code whose meaning is included in the
                status field.
            terminal (Any | Unset): Observed key. The source describes a terminal code for arrival passenger and departure
                passenger records.
            time (Any | Unset): Observed key. The source describes time of arrival for arrival records and also labels the
                time field 'Time of arrival' in its departure sections.
    """

    baggage: Any | Unset = UNSET
    flight: list[ObservedFlightNumber] | Unset = UNSET
    hall: Any | Unset = UNSET
    origin: Any | Unset = UNSET
    stand: Any | Unset = UNSET
    status: Any | Unset = UNSET
    status_code: Any | Unset = UNSET
    terminal: Any | Unset = UNSET
    time: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        baggage = self.baggage

        flight: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.flight, Unset):
            flight = []
            for flight_item_data in self.flight:
                flight_item = flight_item_data.to_dict()
                flight.append(flight_item)

        hall = self.hall

        origin = self.origin

        stand = self.stand

        status = self.status

        status_code = self.status_code

        terminal = self.terminal

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if baggage is not UNSET:
            field_dict["baggage"] = baggage
        if flight is not UNSET:
            field_dict["flight"] = flight
        if hall is not UNSET:
            field_dict["hall"] = hall
        if origin is not UNSET:
            field_dict["origin"] = origin
        if stand is not UNSET:
            field_dict["stand"] = stand
        if status is not UNSET:
            field_dict["status"] = status
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if terminal is not UNSET:
            field_dict["terminal"] = terminal
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.observed_flight_number import ObservedFlightNumber

        d = dict(src_dict)
        baggage = d.pop("baggage", UNSET)

        _flight = d.pop("flight", UNSET)
        flight: list[ObservedFlightNumber] | Unset = UNSET
        if _flight is not UNSET:
            flight = []
            for flight_item_data in _flight:
                flight_item = ObservedFlightNumber.from_dict(flight_item_data)

                flight.append(flight_item)

        hall = d.pop("hall", UNSET)

        origin = d.pop("origin", UNSET)

        stand = d.pop("stand", UNSET)

        status = d.pop("status", UNSET)

        status_code = d.pop("statusCode", UNSET)

        terminal = d.pop("terminal", UNSET)

        time = d.pop("time", UNSET)

        observed_flight_record = cls(
            baggage=baggage,
            flight=flight,
            hall=hall,
            origin=origin,
            stand=stand,
            status=status,
            status_code=status_code,
            terminal=terminal,
            time=time,
        )

        observed_flight_record.additional_properties = d
        return observed_flight_record

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
