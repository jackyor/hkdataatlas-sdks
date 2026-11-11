from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eta import Eta


T = TypeVar("T", bound="RouteStopEtaSequenceEnabled")


@_attrs_define
class RouteStopEtaSequenceEnabled:
    """ETA-enabled response for the route-stop sequence form.

    Attributes:
        enabled (bool | Unset): Whether ETA service is enabled for this route-stop combination.
        eta (list[Eta] | Unset): ETA list.
        stop_id (int | Unset): Stop ID.
    """

    enabled: bool | Unset = UNSET
    eta: list[Eta] | Unset = UNSET
    stop_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        eta: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.eta, Unset):
            eta = []
            for eta_item_data in self.eta:
                eta_item = eta_item_data.to_dict()
                eta.append(eta_item)

        stop_id = self.stop_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if eta is not UNSET:
            field_dict["eta"] = eta
        if stop_id is not UNSET:
            field_dict["stop_id"] = stop_id

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

        stop_id = d.pop("stop_id", UNSET)

        route_stop_eta_sequence_enabled = cls(
            enabled=enabled,
            eta=eta,
            stop_id=stop_id,
        )

        route_stop_eta_sequence_enabled.additional_properties = d
        return route_stop_eta_sequence_enabled

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
