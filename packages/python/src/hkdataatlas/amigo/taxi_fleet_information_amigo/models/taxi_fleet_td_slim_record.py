from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taxi_fleet_td_slim_record_op_status import (
    TaxiFleetTdSlimRecordOpStatus,
    check_taxi_fleet_td_slim_record_op_status,
)
from ..models.taxi_fleet_td_slim_record_taxi_type import (
    TaxiFleetTdSlimRecordTaxiType,
    check_taxi_fleet_td_slim_record_taxi_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TaxiFleetTdSlimRecord")


@_attrs_define
class TaxiFleetTdSlimRecord:
    """Slim vehicle record with latest GPS status. Field requiredness is not specified.

    Attributes:
        lat (float | None | Unset): Current latitude, documented to 6 decimal places with accuracy ±0.5%. Preserves
            documented numbers and observed null for an unavailable coordinate; no value is fabricated.
        long (float | None | Unset): Current longitude, documented to 6 decimal places with accuracy ±0.5%. Preserves
            documented numbers and observed null for an unavailable coordinate; no value is fabricated.
        op_status (TaxiFleetTdSlimRecordOpStatus | Unset): Occupied (O), Vacant (V), or No service (N).
        passenger_cap (int | None | Unset): Seating capacity; whole number or null.
        taxi_type (TaxiFleetTdSlimRecordTaxiType | Unset): Vehicle type.
        time_stamp (datetime.datetime | Unset): Data received time in ISO 8601 with +08:00 timezone.
        veh_id (str | Unset): Vehicle ID. Documented format: stable 12-character identifier.
    """

    lat: float | None | Unset = UNSET
    long: float | None | Unset = UNSET
    op_status: TaxiFleetTdSlimRecordOpStatus | Unset = UNSET
    passenger_cap: int | None | Unset = UNSET
    taxi_type: TaxiFleetTdSlimRecordTaxiType | Unset = UNSET
    time_stamp: datetime.datetime | Unset = UNSET
    veh_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lat: float | None | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        long: float | None | Unset
        if isinstance(self.long, Unset):
            long = UNSET
        else:
            long = self.long

        op_status: str | Unset = UNSET
        if not isinstance(self.op_status, Unset):
            op_status = self.op_status

        passenger_cap: int | None | Unset
        if isinstance(self.passenger_cap, Unset):
            passenger_cap = UNSET
        else:
            passenger_cap = self.passenger_cap

        taxi_type: str | Unset = UNSET
        if not isinstance(self.taxi_type, Unset):
            taxi_type = self.taxi_type

        time_stamp: str | Unset = UNSET
        if not isinstance(self.time_stamp, Unset):
            time_stamp = self.time_stamp.isoformat()

        veh_id = self.veh_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lat is not UNSET:
            field_dict["lat"] = lat
        if long is not UNSET:
            field_dict["long"] = long
        if op_status is not UNSET:
            field_dict["op_status"] = op_status
        if passenger_cap is not UNSET:
            field_dict["passenger_cap"] = passenger_cap
        if taxi_type is not UNSET:
            field_dict["taxi_type"] = taxi_type
        if time_stamp is not UNSET:
            field_dict["time_stamp"] = time_stamp
        if veh_id is not UNSET:
            field_dict["veh_id"] = veh_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lat = _parse_lat(d.pop("lat", UNSET))

        def _parse_long(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        long = _parse_long(d.pop("long", UNSET))

        _op_status = d.pop("op_status", UNSET)
        op_status: TaxiFleetTdSlimRecordOpStatus | Unset
        if isinstance(_op_status, Unset):
            op_status = UNSET
        else:
            op_status = check_taxi_fleet_td_slim_record_op_status(_op_status)

        def _parse_passenger_cap(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        passenger_cap = _parse_passenger_cap(d.pop("passenger_cap", UNSET))

        _taxi_type = d.pop("taxi_type", UNSET)
        taxi_type: TaxiFleetTdSlimRecordTaxiType | Unset
        if isinstance(_taxi_type, Unset):
            taxi_type = UNSET
        else:
            taxi_type = check_taxi_fleet_td_slim_record_taxi_type(_taxi_type)

        _time_stamp = d.pop("time_stamp", UNSET)
        time_stamp: datetime.datetime | Unset
        if isinstance(_time_stamp, Unset):
            time_stamp = UNSET
        else:
            time_stamp = datetime.datetime.fromisoformat(_time_stamp)

        veh_id = d.pop("veh_id", UNSET)

        taxi_fleet_td_slim_record = cls(
            lat=lat,
            long=long,
            op_status=op_status,
            passenger_cap=passenger_cap,
            taxi_type=taxi_type,
            time_stamp=time_stamp,
            veh_id=veh_id,
        )

        taxi_fleet_td_slim_record.additional_properties = d
        return taxi_fleet_td_slim_record

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
