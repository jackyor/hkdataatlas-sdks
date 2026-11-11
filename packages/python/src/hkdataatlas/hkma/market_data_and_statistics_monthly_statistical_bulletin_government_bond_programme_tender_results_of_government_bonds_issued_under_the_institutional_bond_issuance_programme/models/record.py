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
        amount_allotted (float | Unset):
        amount_applied (float | Unset):
        average_yield_accepted (float | Unset):
        bid_to_cover_ratio (float | Unset):
        coupon (float | Unset):
        expected_maturity_date (datetime.date | Unset):
        issue_date (datetime.date | Unset):
        issue_number (str | Unset):
        ni_ro (str | Unset):
    """

    amount_allotted: float | Unset = UNSET
    amount_applied: float | Unset = UNSET
    average_yield_accepted: float | Unset = UNSET
    bid_to_cover_ratio: float | Unset = UNSET
    coupon: float | Unset = UNSET
    expected_maturity_date: datetime.date | Unset = UNSET
    issue_date: datetime.date | Unset = UNSET
    issue_number: str | Unset = UNSET
    ni_ro: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_allotted = self.amount_allotted

        amount_applied = self.amount_applied

        average_yield_accepted = self.average_yield_accepted

        bid_to_cover_ratio = self.bid_to_cover_ratio

        coupon = self.coupon

        expected_maturity_date: str | Unset = UNSET
        if not isinstance(self.expected_maturity_date, Unset):
            expected_maturity_date = self.expected_maturity_date.isoformat()

        issue_date: str | Unset = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        issue_number = self.issue_number

        ni_ro = self.ni_ro

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_allotted is not UNSET:
            field_dict["amount_allotted"] = amount_allotted
        if amount_applied is not UNSET:
            field_dict["amount_applied"] = amount_applied
        if average_yield_accepted is not UNSET:
            field_dict["average_yield_accepted"] = average_yield_accepted
        if bid_to_cover_ratio is not UNSET:
            field_dict["bid-to-cover_ratio"] = bid_to_cover_ratio
        if coupon is not UNSET:
            field_dict["coupon"] = coupon
        if expected_maturity_date is not UNSET:
            field_dict["expected_maturity_date"] = expected_maturity_date
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if issue_number is not UNSET:
            field_dict["issue_number"] = issue_number
        if ni_ro is not UNSET:
            field_dict["ni_ro"] = ni_ro

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_allotted = d.pop("amount_allotted", UNSET)

        amount_applied = d.pop("amount_applied", UNSET)

        average_yield_accepted = d.pop("average_yield_accepted", UNSET)

        bid_to_cover_ratio = d.pop("bid-to-cover_ratio", UNSET)

        coupon = d.pop("coupon", UNSET)

        _expected_maturity_date = d.pop("expected_maturity_date", UNSET)
        expected_maturity_date: datetime.date | Unset
        if isinstance(_expected_maturity_date, Unset):
            expected_maturity_date = UNSET
        else:
            expected_maturity_date = datetime.date.fromisoformat(
                _expected_maturity_date
            )

        _issue_date = d.pop("issue_date", UNSET)
        issue_date: datetime.date | Unset
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = datetime.date.fromisoformat(_issue_date)

        issue_number = d.pop("issue_number", UNSET)

        ni_ro = d.pop("ni_ro", UNSET)

        record = cls(
            amount_allotted=amount_allotted,
            amount_applied=amount_applied,
            average_yield_accepted=average_yield_accepted,
            bid_to_cover_ratio=bid_to_cover_ratio,
            coupon=coupon,
            expected_maturity_date=expected_maturity_date,
            issue_date=issue_date,
            issue_number=issue_number,
            ni_ro=ni_ro,
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
