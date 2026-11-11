from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceArrangementResponse")


@_attrs_define
class ServiceArrangementResponse:
    """Response example for a special train services arrangement. Fields shown are documented by example; no closed-object
    guarantee is made.

        Attributes:
            cur_time (str | Unset): Current-time field as shown in the special-arrangement example.
            message (str | Unset): Alert message.
            status (int | Unset): System status code; dictionary maps 0 to error or alert.
            url (str | Unset): URL for special train services arrangement information.
    """

    cur_time: str | Unset = UNSET
    message: str | Unset = UNSET
    status: int | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cur_time = self.cur_time

        message = self.message

        status = self.status

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cur_time is not UNSET:
            field_dict["cur_time"] = cur_time
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cur_time = d.pop("cur_time", UNSET)

        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        url = d.pop("url", UNSET)

        service_arrangement_response = cls(
            cur_time=cur_time,
            message=message,
            status=status,
            url=url,
        )

        service_arrangement_response.additional_properties = d
        return service_arrangement_response

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
