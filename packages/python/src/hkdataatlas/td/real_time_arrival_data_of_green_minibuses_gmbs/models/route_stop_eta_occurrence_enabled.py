from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eta import Eta


T = TypeVar("T", bound="RouteStopEtaOccurrenceEnabled")


@_attrs_define
class RouteStopEtaOccurrenceEnabled:
    """ETA-enabled occurrence of the stop along the route.

    Attributes:
        enabled (bool | Unset): Whether ETA service is enabled for this route-stop combination.
        eta (list[Eta] | Unset): ETA list.
        route_seq (int | Unset): Route sequence.
        stop_seq (int | Unset): Stop sequence.
    """

    enabled: bool | Unset = UNSET
    eta: list[Eta] | Unset = UNSET
    route_seq: int | Unset = UNSET
    stop_seq: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        eta: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.eta, Unset):
            eta = []
            for eta_item_data in self.eta:
                eta_item = eta_item_data.to_dict()
                eta.append(eta_item)

        route_seq = self.route_seq

        stop_seq = self.stop_seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if eta is not UNSET:
            field_dict["eta"] = eta
        if route_seq is not UNSET:
            field_dict["route_seq"] = route_seq
        if stop_seq is not UNSET:
            field_dict["stop_seq"] = stop_seq

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eta import Eta

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        _eta = d.pop("eta", UNSET)
        eta: list[Eta] | Unset = UNSET
        if _eta is not UNSET:
            eta = []
            for eta_item_data in _eta:
                eta_item = Eta.from_dict(eta_item_data)

                eta.append(eta_item)

        route_seq = d.pop("route_seq", UNSET)

        stop_seq = d.pop("stop_seq", UNSET)

        route_stop_eta_occurrence_enabled = cls(
            enabled=enabled,
            eta=eta,
            route_seq=route_seq,
            stop_seq=stop_seq,
        )

        route_stop_eta_occurrence_enabled.additional_properties = d
        return route_stop_eta_occurrence_enabled

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
