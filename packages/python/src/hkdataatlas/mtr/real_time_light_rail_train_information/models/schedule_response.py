from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.platform import Platform


T = TypeVar("T", bound="ScheduleResponse")


@_attrs_define
class ScheduleResponse:
    """JSON response with system status, system time, and platform list. The documentation does not declare all properties
    universally required.

        Attributes:
            platform_list (list[Platform] | Unset): Array of platform information.
            status (int | Unset): System status code: 1 means normal; 0 means error or alert.
            system_time (str | Unset): System date and time in yyyy-MM-dd HH:mm:ss format.
    """

    platform_list: list[Platform] | Unset = UNSET
    status: int | Unset = UNSET
    system_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        platform_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.platform_list, Unset):
            platform_list = []
            for platform_list_item_data in self.platform_list:
                platform_list_item = platform_list_item_data.to_dict()
                platform_list.append(platform_list_item)

        status = self.status

        system_time = self.system_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if platform_list is not UNSET:
            field_dict["platform_list"] = platform_list
        if status is not UNSET:
            field_dict["status"] = status
        if system_time is not UNSET:
            field_dict["system_time"] = system_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.platform import Platform

        d = dict(src_dict)
        _platform_list = d.pop("platform_list", UNSET)
        platform_list: list[Platform] | Unset = UNSET
        if _platform_list is not UNSET:
            platform_list = []
            for platform_list_item_data in _platform_list:
                platform_list_item = Platform.from_dict(platform_list_item_data)

                platform_list.append(platform_list_item)

        status = d.pop("status", UNSET)

        system_time = d.pop("system_time", UNSET)

        schedule_response = cls(
            platform_list=platform_list,
            status=status,
            system_time=system_time,
        )

        schedule_response.additional_properties = d
        return schedule_response

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
