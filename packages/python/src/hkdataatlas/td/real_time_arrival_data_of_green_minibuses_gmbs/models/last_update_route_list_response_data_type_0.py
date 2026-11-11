from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.last_update_route import LastUpdateRoute


T = TypeVar("T", bound="LastUpdateRouteListResponseDataType0")


@_attrs_define
class LastUpdateRouteListResponseDataType0:
    """
    Attributes:
        data_timestamp (list[LastUpdateRoute] | Unset): Route updates. The source names this property `data_timestamp`
            in the field table and examples.
    """

    data_timestamp: list[LastUpdateRoute] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_timestamp: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = []
            for data_timestamp_item_data in self.data_timestamp:
                data_timestamp_item = data_timestamp_item_data.to_dict()
                data_timestamp.append(data_timestamp_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.last_update_route import LastUpdateRoute

        d = dict(src_dict)
        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: list[LastUpdateRoute] | Unset = UNSET
        if _data_timestamp is not UNSET:
            data_timestamp = []
            for data_timestamp_item_data in _data_timestamp:
                data_timestamp_item = LastUpdateRoute.from_dict(
                    data_timestamp_item_data
                )

                data_timestamp.append(data_timestamp_item)

        last_update_route_list_response_data_type_0 = cls(
            data_timestamp=data_timestamp,
        )

        last_update_route_list_response_data_type_0.additional_properties = d
        return last_update_route_list_response_data_type_0

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
