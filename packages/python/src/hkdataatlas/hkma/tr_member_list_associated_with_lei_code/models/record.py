from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        tr_code (str | Unset):
        tr_name (str | Unset):
        subscribed_service (str | Unset):
        global_lei (None | str | Unset):
    """

    tr_code: str | Unset = UNSET
    tr_name: str | Unset = UNSET
    subscribed_service: str | Unset = UNSET
    global_lei: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tr_code = self.tr_code

        tr_name = self.tr_name

        subscribed_service = self.subscribed_service

        global_lei: None | str | Unset
        if isinstance(self.global_lei, Unset):
            global_lei = UNSET
        else:
            global_lei = self.global_lei

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tr_code is not UNSET:
            field_dict["tr_code"] = tr_code
        if tr_name is not UNSET:
            field_dict["tr_name"] = tr_name
        if subscribed_service is not UNSET:
            field_dict["subscribed_service"] = subscribed_service
        if global_lei is not UNSET:
            field_dict["global_lei"] = global_lei

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tr_code = d.pop("tr_code", UNSET)

        tr_name = d.pop("tr_name", UNSET)

        subscribed_service = d.pop("subscribed_service", UNSET)

        def _parse_global_lei(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        global_lei = _parse_global_lei(d.pop("global_lei", UNSET))

        record = cls(
            tr_code=tr_code,
            tr_name=tr_name,
            subscribed_service=subscribed_service,
            global_lei=global_lei,
        )

        record.additional_properties = d
        return record

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
