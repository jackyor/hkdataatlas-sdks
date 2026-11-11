from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseEnvelope")


@_attrs_define
class ResponseEnvelope:
    """
    Attributes:
        generated_timestamp (datetime.datetime | Unset): Date-time timestamp with time zone in ISO 8601 format.
        type_ (str | Unset): Identifier of the API response.
        version (str | Unset): Version number of the returned JSON, in major.minor format. Example: 1.0.
    """

    generated_timestamp: datetime.datetime | Unset = UNSET
    type_: str | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        generated_timestamp: str | Unset = UNSET
        if not isinstance(self.generated_timestamp, Unset):
            generated_timestamp = self.generated_timestamp.isoformat()

        type_ = self.type_

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generated_timestamp is not UNSET:
            field_dict["generated_timestamp"] = generated_timestamp
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _generated_timestamp = d.pop("generated_timestamp", UNSET)
        generated_timestamp: datetime.datetime | Unset
        if isinstance(_generated_timestamp, Unset):
            generated_timestamp = UNSET
        else:
            generated_timestamp = datetime.datetime.fromisoformat(_generated_timestamp)

        type_ = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        response_envelope = cls(
            generated_timestamp=generated_timestamp,
            type_=type_,
            version=version,
        )

        response_envelope.additional_properties = d
        return response_envelope

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
