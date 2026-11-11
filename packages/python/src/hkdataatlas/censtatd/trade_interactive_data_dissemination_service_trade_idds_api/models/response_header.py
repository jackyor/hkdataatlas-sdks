from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_count import ResponseCount
    from ..models.response_status import ResponseStatus


T = TypeVar("T", bound="ResponseHeader")


@_attrs_define
class ResponseHeader:
    """
    Attributes:
        count (ResponseCount | Unset):
        status (ResponseStatus | Unset): Response status values documented by the publisher.
        tablenote (list[str] | Unset): Table footnotes. The publisher's example notes that monthly sums may differ from
            cumulative totals due to adjustments, totals may differ due to rounding, and countries of consignment with nil
            records are omitted.
        title (str | Unset): Title of the returned table.
    """

    count: ResponseCount | Unset = UNSET
    status: ResponseStatus | Unset = UNSET
    tablenote: list[str] | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count: dict[str, Any] | Unset = UNSET
        if not isinstance(self.count, Unset):
            count = self.count.to_dict()

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        tablenote: list[str] | Unset = UNSET
        if not isinstance(self.tablenote, Unset):
            tablenote = self.tablenote

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if status is not UNSET:
            field_dict["status"] = status
        if tablenote is not UNSET:
            field_dict["tablenote"] = tablenote
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.response_count import ResponseCount
        from ..models.response_status import ResponseStatus

        d = dict(src_dict)
        _count = d.pop("count", UNSET)
        count: ResponseCount | Unset
        if isinstance(_count, Unset):
            count = UNSET
        else:
            count = ResponseCount.from_dict(_count)

        _status = d.pop("status", UNSET)
        status: ResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ResponseStatus.from_dict(_status)

        tablenote = cast(list[str], d.pop("tablenote", UNSET))

        title = d.pop("title", UNSET)

        response_header = cls(
            count=count,
            status=status,
            tablenote=tablenote,
            title=title,
        )

        response_header.additional_properties = d
        return response_header

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
