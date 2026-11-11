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
        end_of_month (datetime.date | Unset):
        specific_data (str | Unset):
        market_activities_injection (float | Unset):
        market_activities_withdrawal (float | Unset):
        interest_payment (float | Unset):
        discount_window_reversal_injection (float | Unset):
        discount_window_reversal_withdrawal (float | Unset):
        discount_window_activities_lending (float | Unset):
        discount_window_activities_borrowing (float | Unset):
        closing_balance (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    specific_data: str | Unset = UNSET
    market_activities_injection: float | Unset = UNSET
    market_activities_withdrawal: float | Unset = UNSET
    interest_payment: float | Unset = UNSET
    discount_window_reversal_injection: float | Unset = UNSET
    discount_window_reversal_withdrawal: float | Unset = UNSET
    discount_window_activities_lending: float | Unset = UNSET
    discount_window_activities_borrowing: float | Unset = UNSET
    closing_balance: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        specific_data = self.specific_data

        market_activities_injection = self.market_activities_injection

        market_activities_withdrawal = self.market_activities_withdrawal

        interest_payment = self.interest_payment

        discount_window_reversal_injection = self.discount_window_reversal_injection

        discount_window_reversal_withdrawal = self.discount_window_reversal_withdrawal

        discount_window_activities_lending = self.discount_window_activities_lending

        discount_window_activities_borrowing = self.discount_window_activities_borrowing

        closing_balance = self.closing_balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if specific_data is not UNSET:
            field_dict["specific_data"] = specific_data
        if market_activities_injection is not UNSET:
            field_dict["market_activities_injection"] = market_activities_injection
        if market_activities_withdrawal is not UNSET:
            field_dict["market_activities_withdrawal"] = market_activities_withdrawal
        if interest_payment is not UNSET:
            field_dict["interest_payment"] = interest_payment
        if discount_window_reversal_injection is not UNSET:
            field_dict["discount_window_reversal_injection"] = (
                discount_window_reversal_injection
            )
        if discount_window_reversal_withdrawal is not UNSET:
            field_dict["discount_window_reversal_withdrawal"] = (
                discount_window_reversal_withdrawal
            )
        if discount_window_activities_lending is not UNSET:
            field_dict["discount_window_activities_lending"] = (
                discount_window_activities_lending
            )
        if discount_window_activities_borrowing is not UNSET:
            field_dict["discount_window_activities_borrowing"] = (
                discount_window_activities_borrowing
            )
        if closing_balance is not UNSET:
            field_dict["closing_balance"] = closing_balance

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_month = d.pop("end_of_month", UNSET)
        end_of_month: datetime.date | Unset
        if isinstance(_end_of_month, Unset):
            end_of_month = UNSET
        else:
            end_of_month = datetime.date.fromisoformat(_end_of_month)

        specific_data = d.pop("specific_data", UNSET)

        market_activities_injection = d.pop("market_activities_injection", UNSET)

        market_activities_withdrawal = d.pop("market_activities_withdrawal", UNSET)

        interest_payment = d.pop("interest_payment", UNSET)

        discount_window_reversal_injection = d.pop(
            "discount_window_reversal_injection", UNSET
        )

        discount_window_reversal_withdrawal = d.pop(
            "discount_window_reversal_withdrawal", UNSET
        )

        discount_window_activities_lending = d.pop(
            "discount_window_activities_lending", UNSET
        )

        discount_window_activities_borrowing = d.pop(
            "discount_window_activities_borrowing", UNSET
        )

        closing_balance = d.pop("closing_balance", UNSET)

        record = cls(
            end_of_month=end_of_month,
            specific_data=specific_data,
            market_activities_injection=market_activities_injection,
            market_activities_withdrawal=market_activities_withdrawal,
            interest_payment=interest_payment,
            discount_window_reversal_injection=discount_window_reversal_injection,
            discount_window_reversal_withdrawal=discount_window_reversal_withdrawal,
            discount_window_activities_lending=discount_window_activities_lending,
            discount_window_activities_borrowing=discount_window_activities_borrowing,
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
