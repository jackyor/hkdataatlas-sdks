from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseCount")


@_attrs_define
class ResponseCount:
    """
    Attributes:
        duration_seconds (float | Unset):
        finished (datetime.datetime | Unset):
        no_of_records (int | Unset):
        started (datetime.datetime | Unset):
    """

    duration_seconds: float | Unset = UNSET
    finished: datetime.datetime | Unset = UNSET
    no_of_records: int | Unset = UNSET
    started: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_seconds = self.duration_seconds

        finished: str | Unset = UNSET
        if not isinstance(self.finished, Unset):
            finished = self.finished.isoformat()

        no_of_records = self.no_of_records

        started: str | Unset = UNSET
        if not isinstance(self.started, Unset):
            started = self.started.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds
        if finished is not UNSET:
            field_dict["finished"] = finished
        if no_of_records is not UNSET:
            field_dict["noOfRecords"] = no_of_records
        if started is not UNSET:
            field_dict["started"] = started

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        duration_seconds = d.pop("durationSeconds", UNSET)

        _finished = d.pop("finished", UNSET)
        finished: datetime.datetime | Unset
        if isinstance(_finished, Unset):
            finished = UNSET
        else:
            finished = datetime.datetime.fromisoformat(_finished)

        no_of_records = d.pop("noOfRecords", UNSET)

        _started = d.pop("started", UNSET)
        started: datetime.datetime | Unset
        if isinstance(_started, Unset):
            started = UNSET
        else:
            started = datetime.datetime.fromisoformat(_started)

        response_count = cls(
            duration_seconds=duration_seconds,
            finished=finished,
            no_of_records=no_of_records,
            started=started,
        )

        response_count.additional_properties = d
        return response_count

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
