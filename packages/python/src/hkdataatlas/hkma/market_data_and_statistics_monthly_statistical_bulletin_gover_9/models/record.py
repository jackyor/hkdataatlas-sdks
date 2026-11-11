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
        expected_maturity_date (datetime.date | Unset):
        original_maturity (str | Unset):
        issue_number (str | Unset):
        isin_code (str | Unset):
        stock_code (str | Unset):
        coupon (str | Unset):
        outstanding_size (float | Unset):
        institutional_retail (str | Unset):
    """

    expected_maturity_date: datetime.date | Unset = UNSET
    original_maturity: str | Unset = UNSET
    issue_number: str | Unset = UNSET
    isin_code: str | Unset = UNSET
    stock_code: str | Unset = UNSET
    coupon: str | Unset = UNSET
    outstanding_size: float | Unset = UNSET
    institutional_retail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_maturity_date: str | Unset = UNSET
        if not isinstance(self.expected_maturity_date, Unset):
            expected_maturity_date = self.expected_maturity_date.isoformat()

        original_maturity = self.original_maturity

        issue_number = self.issue_number

        isin_code = self.isin_code

        stock_code = self.stock_code

        coupon = self.coupon

        outstanding_size = self.outstanding_size

        institutional_retail = self.institutional_retail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expected_maturity_date is not UNSET:
            field_dict["expected_maturity_date"] = expected_maturity_date
        if original_maturity is not UNSET:
            field_dict["original_maturity"] = original_maturity
        if issue_number is not UNSET:
            field_dict["issue_number"] = issue_number
        if isin_code is not UNSET:
            field_dict["isin_code"] = isin_code
        if stock_code is not UNSET:
            field_dict["stock_code"] = stock_code
        if coupon is not UNSET:
            field_dict["coupon"] = coupon
        if outstanding_size is not UNSET:
            field_dict["outstanding_size"] = outstanding_size
        if institutional_retail is not UNSET:
            field_dict["institutional_retail"] = institutional_retail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _expected_maturity_date = d.pop("expected_maturity_date", UNSET)
        expected_maturity_date: datetime.date | Unset
        if isinstance(_expected_maturity_date, Unset):
            expected_maturity_date = UNSET
        else:
            expected_maturity_date = datetime.date.fromisoformat(
                _expected_maturity_date
            )

        original_maturity = d.pop("original_maturity", UNSET)

        issue_number = d.pop("issue_number", UNSET)

        isin_code = d.pop("isin_code", UNSET)

        stock_code = d.pop("stock_code", UNSET)

        coupon = d.pop("coupon", UNSET)

        outstanding_size = d.pop("outstanding_size", UNSET)

        institutional_retail = d.pop("institutional_retail", UNSET)

        record = cls(
            expected_maturity_date=expected_maturity_date,
            original_maturity=original_maturity,
            issue_number=issue_number,
            isin_code=isin_code,
            stock_code=stock_code,
            coupon=coupon,
            outstanding_size=outstanding_size,
            institutional_retail=institutional_retail,
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
