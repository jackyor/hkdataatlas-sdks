from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route_endpoint import RouteEndpoint
    from ..models.route_segment import RouteSegment


T = TypeVar("T", bound="RoutePart")


@_attrs_define
class RoutePart:
    """A part of the route.

    Attributes:
        end (RouteEndpoint | Unset): Start or end location for a part of the route.
        segment (list[RouteSegment] | Unset): List of route segments.
        start (RouteEndpoint | Unset): Start or end location for a part of the route.
    """

    end: RouteEndpoint | Unset = UNSET
    segment: list[RouteSegment] | Unset = UNSET
    start: RouteEndpoint | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end: dict[str, Any] | Unset = UNSET
        if not isinstance(self.end, Unset):
            end = self.end.to_dict()

        segment: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.segment, Unset):
            segment = []
            for segment_item_data in self.segment:
                segment_item = segment_item_data.to_dict()
                segment.append(segment_item)

        start: dict[str, Any] | Unset = UNSET
        if not isinstance(self.start, Unset):
            start = self.start.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if segment is not UNSET:
            field_dict["segment"] = segment
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.route_endpoint import RouteEndpoint
        from ..models.route_segment import RouteSegment

        d = dict(src_dict)
        _end = d.pop("end", UNSET)
        end: RouteEndpoint | Unset
        if isinstance(_end, Unset):
            end = UNSET
        else:
            end = RouteEndpoint.from_dict(_end)

        _segment = d.pop("segment", UNSET)
        segment: list[RouteSegment] | Unset = UNSET
        if _segment is not UNSET:
            segment = []
            for segment_item_data in _segment:
                segment_item = RouteSegment.from_dict(segment_item_data)

                segment.append(segment_item)

        _start = d.pop("start", UNSET)
        start: RouteEndpoint | Unset
        if isinstance(_start, Unset):
            start = UNSET
        else:
            start = RouteEndpoint.from_dict(_start)

        route_part = cls(
            end=end,
            segment=segment,
            start=start,
        )

        route_part.additional_properties = d
        return route_part

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
