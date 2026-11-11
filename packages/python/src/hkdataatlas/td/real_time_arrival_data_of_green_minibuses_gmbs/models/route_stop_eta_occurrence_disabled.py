from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteStopEtaOccurrenceDisabled")


@_attrs_define
class RouteStopEtaOccurrenceDisabled:
    """ETA-disabled occurrence of the stop along the route.

    Attributes:
        description_en (str | Unset): English reason ETA service is unavailable.
        description_sc (str | Unset): Simplified Chinese reason ETA service is unavailable.
        description_tc (str | Unset): Traditional Chinese reason ETA service is unavailable.
        enabled (bool | Unset): Whether ETA service is enabled for this route-stop combination.
        route_seq (int | Unset): Route sequence.
        stop_seq (int | Unset): Stop sequence.
    """

    description_en: str | Unset = UNSET
    description_sc: str | Unset = UNSET
    description_tc: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    route_seq: int | Unset = UNSET
    stop_seq: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description_en = self.description_en

        description_sc = self.description_sc

        description_tc = self.description_tc

        enabled = self.enabled

        route_seq = self.route_seq

        stop_seq = self.stop_seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description_en is not UNSET:
            field_dict["description_en"] = description_en
        if description_sc is not UNSET:
            field_dict["description_sc"] = description_sc
        if description_tc is not UNSET:
            field_dict["description_tc"] = description_tc
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if route_seq is not UNSET:
            field_dict["route_seq"] = route_seq
        if stop_seq is not UNSET:
            field_dict["stop_seq"] = stop_seq

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description_en = d.pop("description_en", UNSET)

        description_sc = d.pop("description_sc", UNSET)

        description_tc = d.pop("description_tc", UNSET)

        enabled = d.pop("enabled", UNSET)

        route_seq = d.pop("route_seq", UNSET)

        stop_seq = d.pop("stop_seq", UNSET)

        route_stop_eta_occurrence_disabled = cls(
            description_en=description_en,
            description_sc=description_sc,
            description_tc=description_tc,
            enabled=enabled,
            route_seq=route_seq,
            stop_seq=stop_seq,
        )

        route_stop_eta_occurrence_disabled.additional_properties = d
        return route_stop_eta_occurrence_disabled

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
