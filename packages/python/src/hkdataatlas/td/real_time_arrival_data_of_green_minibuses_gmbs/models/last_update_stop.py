from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LastUpdateStop")


@_attrs_define
class LastUpdateStop:
    """
    Attributes:
        last_update_date (datetime.datetime | Unset): Last updated timestamp of the stop.
        stop_id (int | Unset): Stop ID.
    """

    last_update_date: datetime.datetime | Unset = UNSET
    stop_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_update_date: str | Unset = UNSET
        if not isinstance(self.last_update_date, Unset):
            last_update_date = self.last_update_date.isoformat()

        stop_id = self.stop_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_update_date is not UNSET:
            field_dict["last_update_date"] = last_update_date
        if stop_id is not UNSET:
            field_dict["stop_id"] = stop_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _last_update_date = d.pop("last_update_date", UNSET)
        last_update_date: datetime.datetime | Unset
        if isinstance(_last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = datetime.datetime.fromisoformat(_last_update_date)

        stop_id = d.pop("stop_id", UNSET)

        last_update_stop = cls(
            last_update_date=last_update_date,
            stop_id=stop_id,
        )

        last_update_stop.additional_properties = d
        return last_update_stop

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
