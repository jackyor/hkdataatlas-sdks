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
        end_of_day (datetime.date | Unset):
        market_activities (float | Unset):
        interest_payment (float | Unset):
        discount_window_reversal (float | Unset):
        discount_window_activities (float | Unset):
        closing_balance (float | Unset):
    """

    end_of_day: datetime.date | Unset = UNSET
    market_activities: float | Unset = UNSET
    interest_payment: float | Unset = UNSET
    discount_window_reversal: float | Unset = UNSET
    discount_window_activities: float | Unset = UNSET
    closing_balance: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_day: str | Unset = UNSET
        if not isinstance(self.end_of_day, Unset):
            end_of_day = self.end_of_day.isoformat()

        market_activities = self.market_activities

        interest_payment = self.interest_payment

        discount_window_reversal = self.discount_window_reversal

        discount_window_activities = self.discount_window_activities

        closing_balance = self.closing_balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_day is not UNSET:
            field_dict["end_of_day"] = end_of_day
        if market_activities is not UNSET:
            field_dict["market_activities"] = market_activities
        if interest_payment is not UNSET:
            field_dict["interest_payment"] = interest_payment
        if discount_window_reversal is not UNSET:
            field_dict["discount_window_reversal"] = discount_window_reversal
        if discount_window_activities is not UNSET:
            field_dict["discount_window_activities"] = discount_window_activities
        if closing_balance is not UNSET:
            field_dict["closing_balance"] = closing_balance

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_day = d.pop("end_of_day", UNSET)
        end_of_day: datetime.date | Unset
        if isinstance(_end_of_day, Unset):
            end_of_day = UNSET
        else:
            end_of_day = datetime.date.fromisoformat(_end_of_day)

        market_activities = d.pop("market_activities", UNSET)

        interest_payment = d.pop("interest_payment", UNSET)

        discount_window_reversal = d.pop("discount_window_reversal", UNSET)

        discount_window_activities = d.pop("discount_window_activities", UNSET)

        closing_balance = d.pop("closing_balance", UNSET)

        record = cls(
            end_of_day=end_of_day,
            market_activities=market_activities,
            interest_payment=interest_payment,
            discount_window_reversal=discount_window_reversal,
            discount_window_activities=discount_window_activities,
            closing_balance=closing_balance,
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
