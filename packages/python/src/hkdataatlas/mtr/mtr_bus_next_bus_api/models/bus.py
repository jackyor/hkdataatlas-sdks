from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bus_location import BusLocation


T = TypeVar("T", bound="Bus")


@_attrs_define
class Bus:
    """Data for each bus in the selected route.

    Attributes:
        arrival_time_in_second (str | Unset): Estimated time of arrival of the bus in seconds. The example represents
            this as a string.
        arrival_time_text (str | Unset): Estimated time of arrival in text. Documented formats include `_ minutes/分鐘`
            for arrival in the stated time, `Arriving / Departed` or `即將到站/已離開` for a bus arriving soon or having departed,
            and no arrival-time text for first stops of non-circular routes.
        bus_id (str | Unset): Unique ID of the bus.
        bus_location (BusLocation | Unset): Coordinates of the bus's current location.
        bus_remark (None | str | Unset): Deprecated. The example contains null.
        departure_time_in_second (str | Unset): Estimated time of departure of the bus in seconds. The example
            represents this as a string and includes negative and zero values.
        departure_time_text (str | Unset): Estimated time of departure in text. Documented formats include `_
            minutes/分鐘` for departure in the stated time and `Departing / Departed` or `即將開出/已離開` when the bus is departing
            soon or has departed.
        is_delayed (str | Unset): Deprecated.
        is_scheduled (str | Unset): Indicates whether the estimated arrival time is based on service schedule: `1` =
            based on service schedule; `0` = based on real-time status.
        line_ref (str | Unset): Route reference name formed by combining the route name and the initial of the
            destination name. For a circular route, the destination initial is `CIR`.
    """

    arrival_time_in_second: str | Unset = UNSET
    arrival_time_text: str | Unset = UNSET
    bus_id: str | Unset = UNSET
    bus_location: BusLocation | Unset = UNSET
    bus_remark: None | str | Unset = UNSET
    departure_time_in_second: str | Unset = UNSET
    departure_time_text: str | Unset = UNSET
    is_delayed: str | Unset = UNSET
    is_scheduled: str | Unset = UNSET
    line_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arrival_time_in_second = self.arrival_time_in_second

        arrival_time_text = self.arrival_time_text

        bus_id = self.bus_id

        bus_location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bus_location, Unset):
            bus_location = self.bus_location.to_dict()

        bus_remark: None | str | Unset
        if isinstance(self.bus_remark, Unset):
            bus_remark = UNSET
        else:
            bus_remark = self.bus_remark

        departure_time_in_second = self.departure_time_in_second

        departure_time_text = self.departure_time_text

        is_delayed = self.is_delayed

        is_scheduled = self.is_scheduled

        line_ref = self.line_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arrival_time_in_second is not UNSET:
            field_dict["arrivalTimeInSecond"] = arrival_time_in_second
        if arrival_time_text is not UNSET:
            field_dict["arrivalTimeText"] = arrival_time_text
        if bus_id is not UNSET:
            field_dict["busId"] = bus_id
        if bus_location is not UNSET:
            field_dict["busLocation"] = bus_location
        if bus_remark is not UNSET:
            field_dict["busRemark"] = bus_remark
        if departure_time_in_second is not UNSET:
            field_dict["departureTimeInSecond"] = departure_time_in_second
        if departure_time_text is not UNSET:
            field_dict["departureTimeText"] = departure_time_text
        if is_delayed is not UNSET:
            field_dict["isDelayed"] = is_delayed
        if is_scheduled is not UNSET:
            field_dict["isScheduled"] = is_scheduled
        if line_ref is not UNSET:
            field_dict["lineRef"] = line_ref

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bus_location import BusLocation

        d = dict(src_dict)
        arrival_time_in_second = d.pop("arrivalTimeInSecond", UNSET)

        arrival_time_text = d.pop("arrivalTimeText", UNSET)

        bus_id = d.pop("busId", UNSET)

        _bus_location = d.pop("busLocation", UNSET)
        bus_location: BusLocation | Unset
        if isinstance(_bus_location, Unset):
            bus_location = UNSET
        else:
            bus_location = BusLocation.from_dict(_bus_location)

        def _parse_bus_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bus_remark = _parse_bus_remark(d.pop("busRemark", UNSET))

        departure_time_in_second = d.pop("departureTimeInSecond", UNSET)

        departure_time_text = d.pop("departureTimeText", UNSET)

        is_delayed = d.pop("isDelayed", UNSET)

        is_scheduled = d.pop("isScheduled", UNSET)

        line_ref = d.pop("lineRef", UNSET)

        bus = cls(
            arrival_time_in_second=arrival_time_in_second,
            arrival_time_text=arrival_time_text,
            bus_id=bus_id,
            bus_location=bus_location,
            bus_remark=bus_remark,
            departure_time_in_second=departure_time_in_second,
            departure_time_text=departure_time_text,
            is_delayed=is_delayed,
            is_scheduled=is_scheduled,
            line_ref=line_ref,
        )

        bus.additional_properties = d
        return bus

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
