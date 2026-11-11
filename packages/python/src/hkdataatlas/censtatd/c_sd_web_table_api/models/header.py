from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.count import Count
    from ..models.status import Status


T = TypeVar("T", bound="Header")


@_attrs_define
class Header:
    """
    Attributes:
        status (Status):
        count (Count):
        title (str | Unset): Web Table Title
        tablenote (list[str] | Unset): Footnotes and explanatory notes (language-dependent)
        source (str | Unset): Data source and contact information
    """

    status: Status
    count: Count
    title: str | Unset = UNSET
    tablenote: list[str] | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.to_dict()

        count = self.count.to_dict()

        title = self.title

        tablenote: list[str] | Unset = UNSET
        if not isinstance(self.tablenote, Unset):
            tablenote = self.tablenote

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "count": count,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if tablenote is not UNSET:
            field_dict["tablenote"] = tablenote
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.count import Count
        from ..models.status import Status

        d = dict(src_dict)
        status = Status.from_dict(d.pop("status"))

        count = Count.from_dict(d.pop("count"))

        title = d.pop("title", UNSET)

        tablenote = cast(list[str], d.pop("tablenote", UNSET))

        source = d.pop("source", UNSET)

        header = cls(
            status=status,
            count=count,
            title=title,
            tablenote=tablenote,
            source=source,
        )

        header.additional_properties = d
        return header

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
