from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RouteStopEtaSequenceDisabled")


@_attrs_define
class RouteStopEtaSequenceDisabled:
    """ETA-disabled response for the route-stop sequence form.

    Attributes:
        description_en (str | Unset): English reason ETA service is unavailable.
        description_sc (str | Unset): Simplified Chinese reason ETA service is unavailable.
        description_tc (str | Unset): Traditional Chinese reason ETA service is unavailable.
        enabled (bool | Unset): Whether ETA service is enabled for this route-stop combination.
        stop_id (int | Unset): Stop ID.
    """

    description_en: str | Unset = UNSET
    description_sc: str | Unset = UNSET
    description_tc: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    stop_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description_en = self.description_en

        description_sc = self.description_sc

        description_tc = self.description_tc

        enabled = self.enabled

        stop_id = self.stop_id

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
        if stop_id is not UNSET:
            field_dict["stop_id"] = stop_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description_en = d.pop("description_en", UNSET)

        description_sc = d.pop("description_sc", UNSET)

        description_tc = d.pop("description_tc", UNSET)

        enabled = d.pop("enabled", UNSET)

        stop_id = d.pop("stop_id", UNSET)

        route_stop_eta_sequence_disabled = cls(
            description_en=description_en,
            description_sc=description_sc,
            description_tc=description_tc,
            enabled=enabled,
            stop_id=stop_id,
        )

        route_stop_eta_sequence_disabled.additional_properties = d
        return route_stop_eta_sequence_disabled

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
