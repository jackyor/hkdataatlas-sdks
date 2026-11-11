from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pier import Pier


T = TypeVar("T", bound="PierResponse")


@_attrs_define
class PierResponse:
    """
    Attributes:
        data (Pier | Unset):
        generated_timestamp (datetime.datetime | Unset): Initial generated time of the response before it is cached;
            date and time with time zone in ISO 8601 format. Example: 2021-08-01T08:51:44+08:00.
        type_ (str | Unset): Corresponding API name; the dictionary says the value is always Pier. Example: Pier.
        version (str | Unset): Version number in major and minor versioning format. Example: 1.2.
    """

    data: Pier | Unset = UNSET
    generated_timestamp: datetime.datetime | Unset = UNSET
    type_: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        generated_timestamp: str | Unset = UNSET
        if not isinstance(self.generated_timestamp, Unset):
            generated_timestamp = self.generated_timestamp.isoformat()

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
        from ..models.pier import Pier

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Pier | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = Pier.from_dict(_data)

        _generated_timestamp = d.pop("generated_timestamp", UNSET)
        generated_timestamp: datetime.datetime | Unset
        if isinstance(_generated_timestamp, Unset):
            generated_timestamp = UNSET
        else:
            generated_timestamp = datetime.datetime.fromisoformat(_generated_timestamp)

        type_ = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        pier_response = cls(
            data=data,
            generated_timestamp=generated_timestamp,
            type_=type_,
            version=version,
        )

        pier_response.additional_properties = d
        return pier_response

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
