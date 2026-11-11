from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.train import Train


T = TypeVar("T", bound="StationSchedule")


@_attrs_define
class StationSchedule:
    """Schedule data for one line and station. Direction keys UP and DOWN are arrays of trains for that line. A data-
    absence example includes only current and system time.

        Attributes:
            down (list[Train] | Unset): Upcoming trains in the DOWN direction. Direction destinations vary by line as
                described in the data dictionary.
            up (list[Train] | Unset): Upcoming trains in the UP direction. Direction destinations vary by line as described
                in the data dictionary.
            curr_time (str | Unset): Current date and time; may be "-" in the documented data-absence example.
            sys_time (str | Unset): System date and time; may be "-" in the documented data-absence example.
    """

    down: list[Train] | Unset = UNSET
    up: list[Train] | Unset = UNSET
    curr_time: str | Unset = UNSET
    sys_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        down: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.down, Unset):
            down = []
            for down_item_data in self.down:
                down_item = down_item_data.to_dict()
                down.append(down_item)

        up: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.up, Unset):
            up = []
            for up_item_data in self.up:
                up_item = up_item_data.to_dict()
                up.append(up_item)

        curr_time = self.curr_time

        sys_time = self.sys_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if down is not UNSET:
            field_dict["DOWN"] = down
        if up is not UNSET:
            field_dict["UP"] = up
        if curr_time is not UNSET:
            field_dict["curr_time"] = curr_time
        if sys_time is not UNSET:
            field_dict["sys_time"] = sys_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.train import Train

        d = dict(src_dict)
        _down = d.pop("DOWN", UNSET)
        down: list[Train] | Unset = UNSET
        if _down is not UNSET:
            down = []
            for down_item_data in _down:
                down_item = Train.from_dict(down_item_data)

                down.append(down_item)

        _up = d.pop("UP", UNSET)
        up: list[Train] | Unset = UNSET
        if _up is not UNSET:
            up = []
            for up_item_data in _up:
                up_item = Train.from_dict(up_item_data)

                up.append(up_item)

        curr_time = d.pop("curr_time", UNSET)

        sys_time = d.pop("sys_time", UNSET)

        station_schedule = cls(
            down=down,
            up=up,
            curr_time=curr_time,
            sys_time=sys_time,
        )

        station_schedule.additional_properties = d
        return station_schedule

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
