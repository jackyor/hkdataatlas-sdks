from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Term")


@_attrs_define
class Term:
    """Term record fields documented by the reference-data dictionary. Requiredness is not specified.

    Attributes:
        end_date (datetime.datetime | Unset): End date of the term. Documented format: YYYY-MM-DDThh:mm:ss (ISO 8601).
            Example: 2020-09-30T00:00:00.
        start_date (datetime.datetime | Unset): Start date of the term. Documented format: YYYY-MM-DDThh:mm:ss (ISO
            8601). Example: 2016-10-01T00:00:00.
        term (str | Unset): Term of the Legislative Council. Example: 2016-2020.
        term_id (float | Unset): Term identifier. Example: 5.
    """

    end_date: datetime.datetime | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    term: str | Unset = UNSET
    term_id: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_date: str | Unset = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        term = self.term

        term_id = self.term_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if term is not UNSET:
            field_dict["term"] = term
        if term_id is not UNSET:
            field_dict["term_id"] = term_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_date = d.pop("end_date", UNSET)
        end_date: datetime.datetime | Unset
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = datetime.datetime.fromisoformat(_end_date)

        _start_date = d.pop("start_date", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = datetime.datetime.fromisoformat(_start_date)

        term = d.pop("term", UNSET)

        term_id = d.pop("term_id", UNSET)

        term = cls(
            end_date=end_date,
            start_date=start_date,
            term=term,
            term_id=term_id,
        )

        term.additional_properties = d
        return term

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
