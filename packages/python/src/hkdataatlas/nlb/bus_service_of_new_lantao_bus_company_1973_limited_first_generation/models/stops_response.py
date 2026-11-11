from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stop import Stop


T = TypeVar("T", bound="StopsResponse")


@_attrs_define
class StopsResponse:
    """
    Attributes:
        stops (list[Stop] | Unset): The stops are ordered by stop sequence of the route.
    """

    stops: list[Stop] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stops: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stops, Unset):
            stops = []
            for stops_item_data in self.stops:
                stops_item = stops_item_data.to_dict()
                stops.append(stops_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stops is not UNSET:
            field_dict["stops"] = stops

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.stop import Stop

        d = dict(src_dict)
        _stops = d.pop("stops", UNSET)
        stops: list[Stop] | Unset = UNSET
        if _stops is not UNSET:
            stops = []
            for stops_item_data in _stops:
                stops_item = Stop.from_dict(stops_item_data)

                stops.append(stops_item)

        stops_response = cls(
            stops=stops,
        )

        stops_response.additional_properties = d
        return stops_response

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
