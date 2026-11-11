from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Taxi")


@_attrs_define
class Taxi:
    """Taxi record. The sample records are illustrative and do not establish that every field is always present.

    Attributes:
        lat (float | None | Unset): Latitude in WGS84 (EPSG:4326), in degrees. May be null.
        long (float | None | Unset): Longitude in WGS84 (EPSG:4326), in degrees. May be null.
        op_status (str | Unset): Current operational status: O = Occupied, V = Vacant, N = Out of Service.
        passenger_cap (int | Unset): Maximum number of passengers. Unit: seats.
        taxi_type (str | Unset): Type of the Taxi: O = Ordinary Taxi, P = Premium Taxi, W = Wheelchair-accessible Taxi.
        time_stamp (datetime.datetime | None | Unset): Server timestamp in ISO 8601 format; may be null.
        veh_id (str | Unset): Unique identifier for each Taxi. May be rotated.
    """

    lat: float | None | Unset = UNSET
    long: float | None | Unset = UNSET
    op_status: str | Unset = UNSET
    passenger_cap: int | Unset = UNSET
    taxi_type: str | Unset = UNSET
    time_stamp: datetime.datetime | None | Unset = UNSET
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

        op_status = self.op_status

        passenger_cap = self.passenger_cap

        taxi_type = self.taxi_type

        time_stamp: None | str | Unset
        if isinstance(self.time_stamp, Unset):
            time_stamp = UNSET
        elif isinstance(self.time_stamp, datetime.datetime):
            time_stamp = self.time_stamp.isoformat()
        else:
            time_stamp = self.time_stamp

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

        op_status = d.pop("op_status", UNSET)

        passenger_cap = d.pop("passenger_cap", UNSET)

        taxi_type = d.pop("taxi_type", UNSET)

        def _parse_time_stamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_stamp_type_0 = datetime.datetime.fromisoformat(data)

                return time_stamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time_stamp = _parse_time_stamp(d.pop("time_stamp", UNSET))

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
