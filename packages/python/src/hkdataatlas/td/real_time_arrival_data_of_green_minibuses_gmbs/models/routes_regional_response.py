from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.routes_regional_response_type import (
    RoutesRegionalResponseType,
    check_routes_regional_response_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.routes_regional_response_data import RoutesRegionalResponseData


T = TypeVar("T", bound="RoutesRegionalResponse")


@_attrs_define
class RoutesRegionalResponse:
    """
    Attributes:
        data (RoutesRegionalResponseData | Unset): Object holding the route-code list for the region and its last
            updated timestamp.
        generated_timestamp (datetime.datetime | Unset): Time when the response is generated, in Hong Kong Time (HKT).
        type_ (RoutesRegionalResponseType | Unset): Entity name specified for the payload.
        version (str | Unset): API version of the response.
    """

    data: RoutesRegionalResponseData | Unset = UNSET
    generated_timestamp: datetime.datetime | Unset = UNSET
    type_: RoutesRegionalResponseType | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        generated_timestamp: str | Unset = UNSET
        if not isinstance(self.generated_timestamp, Unset):
            generated_timestamp = self.generated_timestamp.isoformat()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if generated_timestamp is not UNSET:
            field_dict["generated_timestamp"] = generated_timestamp
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.routes_regional_response_data import RoutesRegionalResponseData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: RoutesRegionalResponseData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = RoutesRegionalResponseData.from_dict(_data)

        _generated_timestamp = d.pop("generated_timestamp", UNSET)
        generated_timestamp: datetime.datetime | Unset
        if isinstance(_generated_timestamp, Unset):
            generated_timestamp = UNSET
        else:
            generated_timestamp = datetime.datetime.fromisoformat(_generated_timestamp)

        _type_ = d.pop("type", UNSET)
        type_: RoutesRegionalResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_routes_regional_response_type(_type_)

        version = d.pop("version", UNSET)

        routes_regional_response = cls(
            data=data,
            generated_timestamp=generated_timestamp,
            type_=type_,
            version=version,
        )

        routes_regional_response.additional_properties = d
        return routes_regional_response

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
