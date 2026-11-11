from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ETARecord")


@_attrs_define
class ETARecord:
    """
    Attributes:
        eta (datetime.datetime | Unset): Estimated time of arrival. Example: 2022-09-19T12:49:00+08:00.
        date (str | Unset): Date of the session. Example: 2022-09-19.
        direction (str | Unset): Direction of the route. Example: inbound.
        route_id (int | str | Unset): Route ID. The companion dictionary declares String; the primary API response
            sample represents it as a number.
        session_time (str | Unset): Session time. Example: 12:15:00.
    """

    eta: datetime.datetime | Unset = UNSET
    date: str | Unset = UNSET
    direction: str | Unset = UNSET
    route_id: int | str | Unset = UNSET
    session_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eta: str | Unset = UNSET
        if not isinstance(self.eta, Unset):
            eta = self.eta.isoformat()

        date = self.date

        direction = self.direction

        route_id: int | str | Unset
        if isinstance(self.route_id, Unset):
            route_id = UNSET
        else:
            route_id = self.route_id

        session_time = self.session_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eta is not UNSET:
            field_dict["ETA"] = eta
        if date is not UNSET:
            field_dict["date"] = date
        if direction is not UNSET:
            field_dict["direction"] = direction
        if route_id is not UNSET:
            field_dict["route_id"] = route_id
        if session_time is not UNSET:
            field_dict["session_time"] = session_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _eta = d.pop("ETA", UNSET)
        eta: datetime.datetime | Unset
        if isinstance(_eta, Unset):
            eta = UNSET
        else:
            eta = datetime.datetime.fromisoformat(_eta)

        date = d.pop("date", UNSET)

        direction = d.pop("direction", UNSET)

        def _parse_route_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        route_id = _parse_route_id(d.pop("route_id", UNSET))

        session_time = d.pop("session_time", UNSET)

        eta_record = cls(
            eta=eta,
            date=date,
            direction=direction,
            route_id=route_id,
            session_time=session_time,
        )

        eta_record.additional_properties = d
        return eta_record

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
