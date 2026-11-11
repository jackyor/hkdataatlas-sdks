from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.route_list_response_type import (
    RouteListResponseType,
    check_route_list_response_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.route import Route


T = TypeVar("T", bound="RouteListResponse")


@_attrs_define
class RouteListResponse:
    """
    Attributes:
        generated_timestamp (datetime.datetime | Unset): Date-time timestamp with time zone in ISO 8601 format.
        type_ (RouteListResponseType | Unset): Identifier of the API response.
        version (str | Unset): Version number of the returned JSON, in major.minor format. Example: 1.0.
        data (list[Route] | Unset):
    """

    generated_timestamp: datetime.datetime | Unset = UNSET
    type_: RouteListResponseType | Unset = UNSET
    version: str | Unset = UNSET
    data: list[Route] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        generated_timestamp: str | Unset = UNSET
        if not isinstance(self.generated_timestamp, Unset):
            generated_timestamp = self.generated_timestamp.isoformat()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        version = self.version

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generated_timestamp is not UNSET:
            field_dict["generated_timestamp"] = generated_timestamp
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.route import Route

        d = dict(src_dict)
        _generated_timestamp = d.pop("generated_timestamp", UNSET)
        generated_timestamp: datetime.datetime | Unset
        if isinstance(_generated_timestamp, Unset):
            generated_timestamp = UNSET
        else:
            generated_timestamp = datetime.datetime.fromisoformat(_generated_timestamp)

        _type_ = d.pop("type", UNSET)
        type_: RouteListResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_route_list_response_type(_type_)

        version = d.pop("version", UNSET)

        _data = d.pop("data", UNSET)
        data: list[Route] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = Route.from_dict(data_item_data)

                data.append(data_item)

        route_list_response = cls(
            generated_timestamp=generated_timestamp,
            type_=type_,
            version=version,
            data=data,
        )

        route_list_response.additional_properties = d
        return route_list_response

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
