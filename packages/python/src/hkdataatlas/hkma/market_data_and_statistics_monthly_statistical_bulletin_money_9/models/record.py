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
        pay_on_dem_money_call_hkd (float | Unset):
        pay_on_dem_money_call_fc (float | Unset):
        pay_on_dem_money_call_total (float | Unset):
        repay_or_call_in_3m_hkd (float | Unset):
        repay_or_call_in_3m_fc (float | Unset):
        repay_or_call_in_3m_total (float | Unset):
        repay_or_call_oth_than_3m_hkd (float | Unset):
        repay_or_call_oth_than_3m_fc (float | Unset):
        repay_or_call_oth_than_3m_total (float | Unset):
        total_loans_hkd (float | Unset):
        total_loans_fc (float | Unset):
        total_loans (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    pay_on_dem_money_call_hkd: float | Unset = UNSET
    pay_on_dem_money_call_fc: float | Unset = UNSET
    pay_on_dem_money_call_total: float | Unset = UNSET
    repay_or_call_in_3m_hkd: float | Unset = UNSET
    repay_or_call_in_3m_fc: float | Unset = UNSET
    repay_or_call_in_3m_total: float | Unset = UNSET
    repay_or_call_oth_than_3m_hkd: float | Unset = UNSET
    repay_or_call_oth_than_3m_fc: float | Unset = UNSET
    repay_or_call_oth_than_3m_total: float | Unset = UNSET
    total_loans_hkd: float | Unset = UNSET
    total_loans_fc: float | Unset = UNSET
    total_loans: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        pay_on_dem_money_call_hkd = self.pay_on_dem_money_call_hkd

        pay_on_dem_money_call_fc = self.pay_on_dem_money_call_fc

        pay_on_dem_money_call_total = self.pay_on_dem_money_call_total

        repay_or_call_in_3m_hkd = self.repay_or_call_in_3m_hkd

        repay_or_call_in_3m_fc = self.repay_or_call_in_3m_fc

        repay_or_call_in_3m_total = self.repay_or_call_in_3m_total

        repay_or_call_oth_than_3m_hkd = self.repay_or_call_oth_than_3m_hkd

        repay_or_call_oth_than_3m_fc = self.repay_or_call_oth_than_3m_fc

        repay_or_call_oth_than_3m_total = self.repay_or_call_oth_than_3m_total

        total_loans_hkd = self.total_loans_hkd

        total_loans_fc = self.total_loans_fc

        total_loans = self.total_loans

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if pay_on_dem_money_call_hkd is not UNSET:
            field_dict["pay_on_dem_money_call_hkd"] = pay_on_dem_money_call_hkd
        if pay_on_dem_money_call_fc is not UNSET:
            field_dict["pay_on_dem_money_call_fc"] = pay_on_dem_money_call_fc
        if pay_on_dem_money_call_total is not UNSET:
            field_dict["pay_on_dem_money_call_total"] = pay_on_dem_money_call_total
        if repay_or_call_in_3m_hkd is not UNSET:
            field_dict["repay_or_call_in_3m_hkd"] = repay_or_call_in_3m_hkd
        if repay_or_call_in_3m_fc is not UNSET:
            field_dict["repay_or_call_in_3m_fc"] = repay_or_call_in_3m_fc
        if repay_or_call_in_3m_total is not UNSET:
            field_dict["repay_or_call_in_3m_total"] = repay_or_call_in_3m_total
        if repay_or_call_oth_than_3m_hkd is not UNSET:
            field_dict["repay_or_call_oth_than_3m_hkd"] = repay_or_call_oth_than_3m_hkd
        if repay_or_call_oth_than_3m_fc is not UNSET:
            field_dict["repay_or_call_oth_than_3m_fc"] = repay_or_call_oth_than_3m_fc
        if repay_or_call_oth_than_3m_total is not UNSET:
            field_dict["repay_or_call_oth_than_3m_total"] = (
                repay_or_call_oth_than_3m_total
            )
        if total_loans_hkd is not UNSET:
            field_dict["total_loans_hkd"] = total_loans_hkd
        if total_loans_fc is not UNSET:
            field_dict["total_loans_fc"] = total_loans_fc
        if total_loans is not UNSET:
            field_dict["total_loans"] = total_loans

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

        pay_on_dem_money_call_hkd = d.pop("pay_on_dem_money_call_hkd", UNSET)

        pay_on_dem_money_call_fc = d.pop("pay_on_dem_money_call_fc", UNSET)

        pay_on_dem_money_call_total = d.pop("pay_on_dem_money_call_total", UNSET)

        repay_or_call_in_3m_hkd = d.pop("repay_or_call_in_3m_hkd", UNSET)

        repay_or_call_in_3m_fc = d.pop("repay_or_call_in_3m_fc", UNSET)

        repay_or_call_in_3m_total = d.pop("repay_or_call_in_3m_total", UNSET)

        repay_or_call_oth_than_3m_hkd = d.pop("repay_or_call_oth_than_3m_hkd", UNSET)

        repay_or_call_oth_than_3m_fc = d.pop("repay_or_call_oth_than_3m_fc", UNSET)

        repay_or_call_oth_than_3m_total = d.pop(
            "repay_or_call_oth_than_3m_total", UNSET
        )

        total_loans_hkd = d.pop("total_loans_hkd", UNSET)

        total_loans_fc = d.pop("total_loans_fc", UNSET)

        total_loans = d.pop("total_loans", UNSET)

        record = cls(
            end_of_month=end_of_month,
            pay_on_dem_money_call_hkd=pay_on_dem_money_call_hkd,
            pay_on_dem_money_call_fc=pay_on_dem_money_call_fc,
            pay_on_dem_money_call_total=pay_on_dem_money_call_total,
            repay_or_call_in_3m_hkd=repay_or_call_in_3m_hkd,
            repay_or_call_in_3m_fc=repay_or_call_in_3m_fc,
            repay_or_call_in_3m_total=repay_or_call_in_3m_total,
            repay_or_call_oth_than_3m_hkd=repay_or_call_oth_than_3m_hkd,
            repay_or_call_oth_than_3m_fc=repay_or_call_oth_than_3m_fc,
            repay_or_call_oth_than_3m_total=repay_or_call_oth_than_3m_total,
            total_loans_hkd=total_loans_hkd,
            total_loans_fc=total_loans_fc,
            total_loans=total_loans,
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
