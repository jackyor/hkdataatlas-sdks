from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.taxi_op_status import TaxiOpStatus, check_taxi_op_status
from ..models.taxi_taxi_type import TaxiTaxiType, check_taxi_taxi_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="Taxi")


@_attrs_define
class Taxi:
    """
    Attributes:
        lat (float | Unset): Server-corrected latitude (WGS84), documented to 6 decimal places. Example: 22.291563.
        long (float | Unset): Server-corrected longitude (WGS84), documented to 6 decimal places. Example: 114.301471.
        op_status (TaxiOpStatus | Unset): Operating status.
        passenger_cap (int | Unset): Maximum passenger capacity, in seats. Example: 5.
        taxi_type (TaxiTaxiType | Unset): Taxi category.
        time_stamp (datetime.datetime | Unset): Server-side timestamp of the data record (ISO 8601). Example:
            2024-11-20T08:33:19+08:00.
        veh_id (str | Unset): Daily-regenerated vehicle identifier, documented format: 3-character fleet prefix plus 9
            random digits (for example, BBT013050630). The same physical vehicle has the same identifier within a calendar
            day; identifiers are reassigned at midnight and cannot be used to track a vehicle across days. Example:
            BBT013050630.
    """

    lat: float | Unset = UNSET
    long: float | Unset = UNSET
    op_status: TaxiOpStatus | Unset = UNSET
    passenger_cap: int | Unset = UNSET
    taxi_type: TaxiTaxiType | Unset = UNSET
    time_stamp: datetime.datetime | Unset = UNSET
    veh_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lat = self.lat

        long = self.long

        op_status: str | Unset = UNSET
        if not isinstance(self.op_status, Unset):
            op_status = self.op_status

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
        lat = d.pop("lat", UNSET)

        long = d.pop("long", UNSET)

        _op_status = d.pop("op_status", UNSET)
        op_status: TaxiOpStatus | Unset
        if isinstance(_op_status, Unset):
            op_status = UNSET
        else:
            op_status = check_taxi_op_status(_op_status)

        passenger_cap = d.pop("passenger_cap", UNSET)

        _taxi_type = d.pop("taxi_type", UNSET)
        taxi_type: TaxiTaxiType | Unset
        if isinstance(_taxi_type, Unset):
            taxi_type = UNSET
        else:
            taxi_type = check_taxi_taxi_type(_taxi_type)

        _time_stamp = d.pop("time_stamp", UNSET)
        time_stamp: datetime.datetime | Unset
        if isinstance(_time_stamp, Unset):
            time_stamp = UNSET
        else:
            time_stamp = datetime.datetime.fromisoformat(_time_stamp)

        veh_id = d.pop("veh_id", UNSET)

        taxi = cls(
            lat=lat,
            long=long,
            op_status=op_status,
            passenger_cap=passenger_cap,
            taxi_type=taxi_type,
            time_stamp=time_stamp,
            veh_id=veh_id,
        )

        taxi.additional_properties = d
        return taxi

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
