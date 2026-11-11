from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        name (str | Unset):
        local_address (str | Unset):
        licence_no (str | Unset):
        effective_date (datetime.date | Unset):
    """

    name: str | Unset = UNSET
    local_address: str | Unset = UNSET
    licence_no: str | Unset = UNSET
    effective_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        local_address = self.local_address

        licence_no = self.licence_no

        effective_date: str | Unset = UNSET
        if not isinstance(self.effective_date, Unset):
            effective_date = self.effective_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if local_address is not UNSET:
            field_dict["local_address"] = local_address
        if licence_no is not UNSET:
            field_dict["licence_no"] = licence_no
        if effective_date is not UNSET:
            field_dict["effective_date"] = effective_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        local_address = d.pop("local_address", UNSET)

        licence_no = d.pop("licence_no", UNSET)

        _effective_date = d.pop("effective_date", UNSET)
        effective_date: datetime.date | Unset
        if isinstance(_effective_date, Unset):
            effective_date = UNSET
        else:
            effective_date = datetime.date.fromisoformat(_effective_date)

        record = cls(
            name=name,
            local_address=local_address,
            licence_no=licence_no,
            effective_date=effective_date,
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
