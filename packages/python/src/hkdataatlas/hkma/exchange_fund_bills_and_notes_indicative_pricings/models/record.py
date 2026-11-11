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
        end_of_date (datetime.date | Unset):
        term (str | Unset):
        issue_no (datetime.date | Unset):
        yield_ (float | Unset):
        price (float | Unset):
    """

    end_of_date: datetime.date | Unset = UNSET
    term: str | Unset = UNSET
    issue_no: datetime.date | Unset = UNSET
    yield_: float | Unset = UNSET
    price: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_date: str | Unset = UNSET
        if not isinstance(self.end_of_date, Unset):
            end_of_date = self.end_of_date.isoformat()

        term = self.term

        issue_no: str | Unset = UNSET
        if not isinstance(self.issue_no, Unset):
            issue_no = self.issue_no.isoformat()

        yield_ = self.yield_

        price = self.price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_date is not UNSET:
            field_dict["end_of_date"] = end_of_date
        if term is not UNSET:
            field_dict["term"] = term
        if issue_no is not UNSET:
            field_dict["issue_no"] = issue_no
        if yield_ is not UNSET:
            field_dict["yield"] = yield_
        if price is not UNSET:
            field_dict["price"] = price

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_date = d.pop("end_of_date", UNSET)
        end_of_date: datetime.date | Unset
        if isinstance(_end_of_date, Unset):
            end_of_date = UNSET
        else:
            end_of_date = datetime.date.fromisoformat(_end_of_date)

        term = d.pop("term", UNSET)

        _issue_no = d.pop("issue_no", UNSET)
        issue_no: datetime.date | Unset
        if isinstance(_issue_no, Unset):
            issue_no = UNSET
        else:
            issue_no = datetime.date.fromisoformat(_issue_no)

        yield_ = d.pop("yield", UNSET)

        price = d.pop("price", UNSET)

        record = cls(
            end_of_date=end_of_date,
            term=term,
            issue_no=issue_no,
            yield_=yield_,
            price=price,
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
