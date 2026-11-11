from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EstimatedArrival")


@_attrs_define
class EstimatedArrival:
    """
    Attributes:
        departed (int | Unset): Indicates whether the departure has departed from the first stop of the route: 1 if yes,
            otherwise 0.
        estimated_arrival_time (str | Unset): Datetime; the documented sample uses YYYY-MM-DD HH:MM:SS.
        generate_time (str | Unset): Datetime; the documented sample uses YYYY-MM-DD HH:MM:SS.
        no_gps (int | Unset): Indicates whether the bus for that departure has GPS positioning equipment installed: 1 if
            installed, otherwise 0.
        route_variant_name (str | Unset):
        wheel_chair (int | Unset): Indicates whether the bus for that departure can be easily accessed by wheelchair: 1
            if it can, otherwise 0.
    """

    departed: int | Unset = UNSET
    estimated_arrival_time: str | Unset = UNSET
    generate_time: str | Unset = UNSET
    no_gps: int | Unset = UNSET
    route_variant_name: str | Unset = UNSET
    wheel_chair: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        departed = self.departed

        estimated_arrival_time = self.estimated_arrival_time

        generate_time = self.generate_time

        no_gps = self.no_gps

        route_variant_name = self.route_variant_name

        wheel_chair = self.wheel_chair

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if departed is not UNSET:
            field_dict["departed"] = departed
        if estimated_arrival_time is not UNSET:
            field_dict["estimatedArrivalTime"] = estimated_arrival_time
        if generate_time is not UNSET:
            field_dict["generateTime"] = generate_time
        if no_gps is not UNSET:
            field_dict["noGPS"] = no_gps
        if route_variant_name is not UNSET:
            field_dict["routeVariantName"] = route_variant_name
        if wheel_chair is not UNSET:
            field_dict["wheelChair"] = wheel_chair

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        departed = d.pop("departed", UNSET)

        estimated_arrival_time = d.pop("estimatedArrivalTime", UNSET)

        generate_time = d.pop("generateTime", UNSET)

        no_gps = d.pop("noGPS", UNSET)

        route_variant_name = d.pop("routeVariantName", UNSET)

        wheel_chair = d.pop("wheelChair", UNSET)

        estimated_arrival = cls(
            departed=departed,
            estimated_arrival_time=estimated_arrival_time,
            generate_time=generate_time,
            no_gps=no_gps,
            route_variant_name=route_variant_name,
            wheel_chair=wheel_chair,
        )

        estimated_arrival.additional_properties = d
        return estimated_arrival

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
