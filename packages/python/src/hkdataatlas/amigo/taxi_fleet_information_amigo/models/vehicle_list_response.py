from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.taxi_fleet_td_slim_record import TaxiFleetTdSlimRecord


T = TypeVar("T", bound="VehicleListResponse")


@_attrs_define
class VehicleListResponse:
    """
    Attributes:
        taxis (list[TaxiFleetTdSlimRecord] | Unset): TaxiFleetTdSlimRecord entries. The response example uses a
            placeholder for the array contents.
    """

    taxis: list[TaxiFleetTdSlimRecord] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        taxis: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.taxis, Unset):
            taxis = []
            for taxis_item_data in self.taxis:
                taxis_item = taxis_item_data.to_dict()
                taxis.append(taxis_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if taxis is not UNSET:
            field_dict["taxis"] = taxis

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.taxi_fleet_td_slim_record import TaxiFleetTdSlimRecord

        d = dict(src_dict)
        _taxis = d.pop("taxis", UNSET)
        taxis: list[TaxiFleetTdSlimRecord] | Unset = UNSET
        if _taxis is not UNSET:
            taxis = []
            for taxis_item_data in _taxis:
                taxis_item = TaxiFleetTdSlimRecord.from_dict(taxis_item_data)

                taxis.append(taxis_item)

        vehicle_list_response = cls(
            taxis=taxis,
        )

        vehicle_list_response.additional_properties = d
        return vehicle_list_response

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
