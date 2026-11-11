from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Count")


@_attrs_define
class Count:
    """
    Attributes:
        no_of_records (int | Unset): Number of records returned in `dataSet`
        started (datetime.datetime | Unset): Server-side processing start timestamp (ISO 8601 with offset)
        finished (datetime.datetime | Unset): Server-side processing end timestamp (ISO 8601 with offset)
        duration_seconds (float | Unset): Processing duration in seconds
    """

    no_of_records: int | Unset = UNSET
    started: datetime.datetime | Unset = UNSET
    finished: datetime.datetime | Unset = UNSET
    duration_seconds: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no_of_records = self.no_of_records

        started: str | Unset = UNSET
        if not isinstance(self.started, Unset):
            started = self.started.isoformat()

        finished: str | Unset = UNSET
        if not isinstance(self.finished, Unset):
            finished = self.finished.isoformat()

        duration_seconds = self.duration_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no_of_records is not UNSET:
            field_dict["noOfRecords"] = no_of_records
        if started is not UNSET:
            field_dict["started"] = started
        if finished is not UNSET:
            field_dict["finished"] = finished
        if duration_seconds is not UNSET:
            field_dict["durationSeconds"] = duration_seconds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        no_of_records = d.pop("noOfRecords", UNSET)

        _started = d.pop("started", UNSET)
        started: datetime.datetime | Unset
        if isinstance(_started, Unset):
            started = UNSET
        else:
            started = datetime.datetime.fromisoformat(_started)

        _finished = d.pop("finished", UNSET)
        finished: datetime.datetime | Unset
        if isinstance(_finished, Unset):
            finished = UNSET
        else:
            finished = datetime.datetime.fromisoformat(_finished)

        duration_seconds = d.pop("durationSeconds", UNSET)

        count = cls(
            no_of_records=no_of_records,
            started=started,
            finished=finished,
            duration_seconds=duration_seconds,
        )

        count.additional_properties = d
        return count

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
