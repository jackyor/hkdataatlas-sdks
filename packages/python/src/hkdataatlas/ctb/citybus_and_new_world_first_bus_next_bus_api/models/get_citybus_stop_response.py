from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stop_record import StopRecord


T = TypeVar("T", bound="GetCitybusStopResponse")


@_attrs_define
class GetCitybusStopResponse:
    """
    Attributes:
        type_ (str | Unset):
        version (str | Unset):
        generated_timestamp (str | Unset): ISO 8601 date time with time zone per dictionary; no stronger lexical
            restriction inferred.
        data (StopRecord | Unset):
    """

    type_: str | Unset = UNSET
    version: str | Unset = UNSET
    generated_timestamp: str | Unset = UNSET
    data: StopRecord | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        version = self.version

        generated_timestamp = self.generated_timestamp

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version
        if generated_timestamp is not UNSET:
            field_dict["generated_timestamp"] = generated_timestamp
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.stop_record import StopRecord

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        version = d.pop("version", UNSET)

        generated_timestamp = d.pop("generated_timestamp", UNSET)

        _data = d.pop("data", UNSET)
        data: StopRecord | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = StopRecord.from_dict(_data)

        get_citybus_stop_response = cls(
            type_=type_,
            version=version,
            generated_timestamp=generated_timestamp,
            data=data,
        )

        get_citybus_stop_response.additional_properties = d
        return get_citybus_stop_response

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
