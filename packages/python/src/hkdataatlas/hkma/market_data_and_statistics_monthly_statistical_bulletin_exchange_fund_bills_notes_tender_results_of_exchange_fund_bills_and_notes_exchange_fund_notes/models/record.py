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
        amount_applied (float | Unset):
        average_yield_accepted (float | Unset):
        coupon (float | Unset):
        issue_date (datetime.date | Unset):
        over_subscription (float | Unset):
    """

    amount_applied: float | Unset = UNSET
    average_yield_accepted: float | Unset = UNSET
    coupon: float | Unset = UNSET
    issue_date: datetime.date | Unset = UNSET
    over_subscription: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount_applied = self.amount_applied

        average_yield_accepted = self.average_yield_accepted

        coupon = self.coupon

        issue_date: str | Unset = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        over_subscription = self.over_subscription

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount_applied is not UNSET:
            field_dict["amount_applied"] = amount_applied
        if average_yield_accepted is not UNSET:
            field_dict["average_yield_accepted"] = average_yield_accepted
        if coupon is not UNSET:
            field_dict["coupon"] = coupon
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if over_subscription is not UNSET:
            field_dict["over_subscription"] = over_subscription

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        amount_applied = d.pop("amount_applied", UNSET)

        average_yield_accepted = d.pop("average_yield_accepted", UNSET)

        coupon = d.pop("coupon", UNSET)

        _issue_date = d.pop("issue_date", UNSET)
        issue_date: datetime.date | Unset
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = datetime.date.fromisoformat(_issue_date)

        over_subscription = d.pop("over_subscription", UNSET)

        record = cls(
            amount_applied=amount_applied,
            average_yield_accepted=average_yield_accepted,
            coupon=coupon,
            issue_date=issue_date,
            over_subscription=over_subscription,
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
