from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bus import Bus


T = TypeVar("T", bound="BusStop")


@_attrs_define
class BusStop:
    """Data within each bus stop in the selected route.

    Attributes:
        bus (list[Bus] | Unset): Array of buses.
        bus_icon (None | str | Unset): Deprecated. The example contains null.
        bus_stop_id (str | Unset): Bus stop ID.
        bus_stop_remark (None | str | Unset): Deprecated. The example contains null.
        bus_stop_status (None | str | Unset): Deprecated. The example contains null.
        bus_stop_status_remark_content (None | str | Unset): Deprecated. The example contains null.
        bus_stop_status_remark_title (None | str | Unset): Deprecated. The example contains null.
        bus_stop_status_time (None | str | Unset): Deprecated. The dictionary describes a date-time string with format
            `yyyy-MM-dd HH:mm`; the example contains null.
        is_suspended (str | Unset): Indicates whether service is suspended: `1` = suspended; `0` = normal service.
    """

    bus: list[Bus] | Unset = UNSET
    bus_icon: None | str | Unset = UNSET
    bus_stop_id: str | Unset = UNSET
    bus_stop_remark: None | str | Unset = UNSET
    bus_stop_status: None | str | Unset = UNSET
    bus_stop_status_remark_content: None | str | Unset = UNSET
    bus_stop_status_remark_title: None | str | Unset = UNSET
    bus_stop_status_time: None | str | Unset = UNSET
    is_suspended: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bus, Unset):
            bus = []
            for bus_item_data in self.bus:
                bus_item = bus_item_data.to_dict()
                bus.append(bus_item)

        bus_icon: None | str | Unset
        if isinstance(self.bus_icon, Unset):
            bus_icon = UNSET
        else:
            bus_icon = self.bus_icon

        bus_stop_id = self.bus_stop_id

        bus_stop_remark: None | str | Unset
        if isinstance(self.bus_stop_remark, Unset):
            bus_stop_remark = UNSET
        else:
            bus_stop_remark = self.bus_stop_remark

        bus_stop_status: None | str | Unset
        if isinstance(self.bus_stop_status, Unset):
            bus_stop_status = UNSET
        else:
            bus_stop_status = self.bus_stop_status

        bus_stop_status_remark_content: None | str | Unset
        if isinstance(self.bus_stop_status_remark_content, Unset):
            bus_stop_status_remark_content = UNSET
        else:
            bus_stop_status_remark_content = self.bus_stop_status_remark_content

        bus_stop_status_remark_title: None | str | Unset
        if isinstance(self.bus_stop_status_remark_title, Unset):
            bus_stop_status_remark_title = UNSET
        else:
            bus_stop_status_remark_title = self.bus_stop_status_remark_title

        bus_stop_status_time: None | str | Unset
        if isinstance(self.bus_stop_status_time, Unset):
            bus_stop_status_time = UNSET
        else:
            bus_stop_status_time = self.bus_stop_status_time

        is_suspended = self.is_suspended

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bus is not UNSET:
            field_dict["bus"] = bus
        if bus_icon is not UNSET:
            field_dict["busIcon"] = bus_icon
        if bus_stop_id is not UNSET:
            field_dict["busStopId"] = bus_stop_id
        if bus_stop_remark is not UNSET:
            field_dict["busStopRemark"] = bus_stop_remark
        if bus_stop_status is not UNSET:
            field_dict["busStopStatus"] = bus_stop_status
        if bus_stop_status_remark_content is not UNSET:
            field_dict["busStopStatusRemarkContent"] = bus_stop_status_remark_content
        if bus_stop_status_remark_title is not UNSET:
            field_dict["busStopStatusRemarkTitle"] = bus_stop_status_remark_title
        if bus_stop_status_time is not UNSET:
            field_dict["busStopStatusTime"] = bus_stop_status_time
        if is_suspended is not UNSET:
            field_dict["isSuspended"] = is_suspended

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bus import Bus

        d = dict(src_dict)
        _bus = d.pop("bus", UNSET)
        bus: list[Bus] | Unset = UNSET
        if _bus is not UNSET:
            bus = []
            for bus_item_data in _bus:
                bus_item = Bus.from_dict(bus_item_data)

                bus.append(bus_item)

        def _parse_bus_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bus_icon = _parse_bus_icon(d.pop("busIcon", UNSET))

        bus_stop_id = d.pop("busStopId", UNSET)

        def _parse_bus_stop_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bus_stop_remark = _parse_bus_stop_remark(d.pop("busStopRemark", UNSET))

        def _parse_bus_stop_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bus_stop_status = _parse_bus_stop_status(d.pop("busStopStatus", UNSET))

        def _parse_bus_stop_status_remark_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bus_stop_status_remark_content = _parse_bus_stop_status_remark_content(
            d.pop("busStopStatusRemarkContent", UNSET)
        )

        def _parse_bus_stop_status_remark_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bus_stop_status_remark_title = _parse_bus_stop_status_remark_title(
            d.pop("busStopStatusRemarkTitle", UNSET)
        )

        def _parse_bus_stop_status_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bus_stop_status_time = _parse_bus_stop_status_time(
            d.pop("busStopStatusTime", UNSET)
        )

        is_suspended = d.pop("isSuspended", UNSET)

        bus_stop = cls(
            bus=bus,
            bus_icon=bus_icon,
            bus_stop_id=bus_stop_id,
            bus_stop_remark=bus_stop_remark,
            bus_stop_status=bus_stop_status,
            bus_stop_status_remark_content=bus_stop_status_remark_content,
            bus_stop_status_remark_title=bus_stop_status_remark_title,
            bus_stop_status_time=bus_stop_status_time,
            is_suspended=is_suspended,
        )

        bus_stop.additional_properties = d
        return bus_stop

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
