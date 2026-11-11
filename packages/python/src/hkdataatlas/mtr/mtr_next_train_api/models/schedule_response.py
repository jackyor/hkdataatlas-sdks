from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_response_data import ScheduleResponseData


T = TypeVar("T", bound="ScheduleResponse")


@_attrs_define
class ScheduleResponse:
    """Normal schedule response. The response dictionary documents the fields below; examples show representative values.
    Example time values use yyyy-MM-dd HH:mm:ss. Sample schedule entries encode fields such as numeric
    status/platform/sequence values as strings, while the dictionary declares platform and sequence as Numbers; both
    representations are allowed to preserve that discrepancy.

        Attributes:
            curr_time (str | Unset): Current date and time. The dictionary describes the format as yyyy-MM-dd HH:mm:ss;
                examples also use "-" when data is absent.
            data (ScheduleResponseData | Unset): Data keyed by a line-station identifier, shown in the example as line code,
                hyphen, and station code (for example, TKL-TKO).
            isdelay (str | Unset): Indicates whether the train is delayed: Y = delayed, N = running on time. Documented as
                optional.
            message (str | Unset): Alert message.
            status (int | Unset): System status code. The dictionary gives 1 = normal and 0 = error or alert.
            sys_time (str | Unset): System date and time. Examples also use "-" when data is absent.
            url (str | Unset): URL for a Special Train Services Arrangement case.
    """

    curr_time: str | Unset = UNSET
    data: ScheduleResponseData | Unset = UNSET
    isdelay: str | Unset = UNSET
    message: str | Unset = UNSET
    status: int | Unset = UNSET
    sys_time: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        curr_time = self.curr_time

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        isdelay = self.isdelay

        message = self.message

        status = self.status

        sys_time = self.sys_time

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if curr_time is not UNSET:
            field_dict["curr_time"] = curr_time
        if data is not UNSET:
            field_dict["data"] = data
        if isdelay is not UNSET:
            field_dict["isdelay"] = isdelay
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if sys_time is not UNSET:
            field_dict["sys_time"] = sys_time
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.schedule_response_data import ScheduleResponseData

        d = dict(src_dict)
        curr_time = d.pop("curr_time", UNSET)

        _data = d.pop("data", UNSET)
        data: ScheduleResponseData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ScheduleResponseData.from_dict(_data)

        isdelay = d.pop("isdelay", UNSET)

        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        sys_time = d.pop("sys_time", UNSET)

        url = d.pop("url", UNSET)

        schedule_response = cls(
            curr_time=curr_time,
            data=data,
            isdelay=isdelay,
            message=message,
            status=status,
            sys_time=sys_time,
            url=url,
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
