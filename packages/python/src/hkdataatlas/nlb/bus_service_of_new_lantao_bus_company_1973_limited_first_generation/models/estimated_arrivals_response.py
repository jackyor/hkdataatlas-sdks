from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.estimated_arrival import EstimatedArrival


T = TypeVar("T", bound="EstimatedArrivalsResponse")


@_attrs_define
class EstimatedArrivalsResponse:
    """
    Attributes:
        estimated_arrivals (list[EstimatedArrival] | Unset): This property does not exist if the bus estimated arrival
            time of the route is currently unavailable.
        message (str | Unset):
    """

    estimated_arrivals: list[EstimatedArrival] | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        estimated_arrivals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.estimated_arrivals, Unset):
            estimated_arrivals = []
            for estimated_arrivals_item_data in self.estimated_arrivals:
                estimated_arrivals_item = estimated_arrivals_item_data.to_dict()
                estimated_arrivals.append(estimated_arrivals_item)

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if estimated_arrivals is not UNSET:
            field_dict["estimatedArrivals"] = estimated_arrivals
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.estimated_arrival import EstimatedArrival

        d = dict(src_dict)
        _estimated_arrivals = d.pop("estimatedArrivals", UNSET)
        estimated_arrivals: list[EstimatedArrival] | Unset = UNSET
        if _estimated_arrivals is not UNSET:
            estimated_arrivals = []
            for estimated_arrivals_item_data in _estimated_arrivals:
                estimated_arrivals_item = EstimatedArrival.from_dict(
                    estimated_arrivals_item_data
                )

                estimated_arrivals.append(estimated_arrivals_item)

        message = d.pop("message", UNSET)

        estimated_arrivals_response = cls(
            estimated_arrivals=estimated_arrivals,
            message=message,
        )

        estimated_arrivals_response.additional_properties = d
        return estimated_arrivals_response

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
