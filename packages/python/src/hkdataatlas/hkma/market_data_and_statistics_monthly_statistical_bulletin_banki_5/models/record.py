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
        imp_exp_reexp_fromhk_hkd (float | Unset):
        imp_exp_reexp_fromhk_fc (float | Unset):
        imp_exp_reexp_fromhk_total (float | Unset):
        merch_trade_nonhk_hkd (float | Unset):
        merch_trade_nonhk_fc (float | Unset):
        merch_trade_nonhk_total (float | Unset):
        loans_inhk_hkd (float | Unset):
        loans_inhk_fc (float | Unset):
        loans_inhk_total (float | Unset):
        other_loans_outhk_hkd (float | Unset):
        other_loans_outhk_fc (float | Unset):
        other_loans_outhk_total (float | Unset):
        other_loans_unkplace_hkd (float | Unset):
        other_loans_unkplace_fc (float | Unset):
        other_loans_unkplace_total (float | Unset):
        total_loans_hkd (float | Unset):
        total_loans_fc (float | Unset):
        total_loans (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    imp_exp_reexp_fromhk_hkd: float | Unset = UNSET
    imp_exp_reexp_fromhk_fc: float | Unset = UNSET
    imp_exp_reexp_fromhk_total: float | Unset = UNSET
    merch_trade_nonhk_hkd: float | Unset = UNSET
    merch_trade_nonhk_fc: float | Unset = UNSET
    merch_trade_nonhk_total: float | Unset = UNSET
    loans_inhk_hkd: float | Unset = UNSET
    loans_inhk_fc: float | Unset = UNSET
    loans_inhk_total: float | Unset = UNSET
    other_loans_outhk_hkd: float | Unset = UNSET
    other_loans_outhk_fc: float | Unset = UNSET
    other_loans_outhk_total: float | Unset = UNSET
    other_loans_unkplace_hkd: float | Unset = UNSET
    other_loans_unkplace_fc: float | Unset = UNSET
    other_loans_unkplace_total: float | Unset = UNSET
    total_loans_hkd: float | Unset = UNSET
    total_loans_fc: float | Unset = UNSET
    total_loans: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        imp_exp_reexp_fromhk_hkd = self.imp_exp_reexp_fromhk_hkd

        imp_exp_reexp_fromhk_fc = self.imp_exp_reexp_fromhk_fc

        imp_exp_reexp_fromhk_total = self.imp_exp_reexp_fromhk_total

        merch_trade_nonhk_hkd = self.merch_trade_nonhk_hkd

        merch_trade_nonhk_fc = self.merch_trade_nonhk_fc

        merch_trade_nonhk_total = self.merch_trade_nonhk_total

        loans_inhk_hkd = self.loans_inhk_hkd

        loans_inhk_fc = self.loans_inhk_fc

        loans_inhk_total = self.loans_inhk_total

        other_loans_outhk_hkd = self.other_loans_outhk_hkd

        other_loans_outhk_fc = self.other_loans_outhk_fc

        other_loans_outhk_total = self.other_loans_outhk_total

        other_loans_unkplace_hkd = self.other_loans_unkplace_hkd

        other_loans_unkplace_fc = self.other_loans_unkplace_fc

        other_loans_unkplace_total = self.other_loans_unkplace_total

        total_loans_hkd = self.total_loans_hkd

        total_loans_fc = self.total_loans_fc

        total_loans = self.total_loans

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if imp_exp_reexp_fromhk_hkd is not UNSET:
            field_dict["imp_exp_reexp_fromhk_hkd"] = imp_exp_reexp_fromhk_hkd
        if imp_exp_reexp_fromhk_fc is not UNSET:
            field_dict["imp_exp_reexp_fromhk_fc"] = imp_exp_reexp_fromhk_fc
        if imp_exp_reexp_fromhk_total is not UNSET:
            field_dict["imp_exp_reexp_fromhk_total"] = imp_exp_reexp_fromhk_total
        if merch_trade_nonhk_hkd is not UNSET:
            field_dict["merch_trade_nonhk_hkd"] = merch_trade_nonhk_hkd
        if merch_trade_nonhk_fc is not UNSET:
            field_dict["merch_trade_nonhk_fc"] = merch_trade_nonhk_fc
        if merch_trade_nonhk_total is not UNSET:
            field_dict["merch_trade_nonhk_total"] = merch_trade_nonhk_total
        if loans_inhk_hkd is not UNSET:
            field_dict["loans_inhk_hkd"] = loans_inhk_hkd
        if loans_inhk_fc is not UNSET:
            field_dict["loans_inhk_fc"] = loans_inhk_fc
        if loans_inhk_total is not UNSET:
            field_dict["loans_inhk_total"] = loans_inhk_total
        if other_loans_outhk_hkd is not UNSET:
            field_dict["other_loans_outhk_hkd"] = other_loans_outhk_hkd
        if other_loans_outhk_fc is not UNSET:
            field_dict["other_loans_outhk_fc"] = other_loans_outhk_fc
        if other_loans_outhk_total is not UNSET:
            field_dict["other_loans_outhk_total"] = other_loans_outhk_total
        if other_loans_unkplace_hkd is not UNSET:
            field_dict["other_loans_unkplace_hkd"] = other_loans_unkplace_hkd
        if other_loans_unkplace_fc is not UNSET:
            field_dict["other_loans_unkplace_fc"] = other_loans_unkplace_fc
        if other_loans_unkplace_total is not UNSET:
            field_dict["other_loans_unkplace_total"] = other_loans_unkplace_total
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

        imp_exp_reexp_fromhk_hkd = d.pop("imp_exp_reexp_fromhk_hkd", UNSET)

        imp_exp_reexp_fromhk_fc = d.pop("imp_exp_reexp_fromhk_fc", UNSET)

        imp_exp_reexp_fromhk_total = d.pop("imp_exp_reexp_fromhk_total", UNSET)

        merch_trade_nonhk_hkd = d.pop("merch_trade_nonhk_hkd", UNSET)

        merch_trade_nonhk_fc = d.pop("merch_trade_nonhk_fc", UNSET)

        merch_trade_nonhk_total = d.pop("merch_trade_nonhk_total", UNSET)

        loans_inhk_hkd = d.pop("loans_inhk_hkd", UNSET)

        loans_inhk_fc = d.pop("loans_inhk_fc", UNSET)

        loans_inhk_total = d.pop("loans_inhk_total", UNSET)

        other_loans_outhk_hkd = d.pop("other_loans_outhk_hkd", UNSET)

        other_loans_outhk_fc = d.pop("other_loans_outhk_fc", UNSET)

        other_loans_outhk_total = d.pop("other_loans_outhk_total", UNSET)

        other_loans_unkplace_hkd = d.pop("other_loans_unkplace_hkd", UNSET)

        other_loans_unkplace_fc = d.pop("other_loans_unkplace_fc", UNSET)

        other_loans_unkplace_total = d.pop("other_loans_unkplace_total", UNSET)

        total_loans_hkd = d.pop("total_loans_hkd", UNSET)

        total_loans_fc = d.pop("total_loans_fc", UNSET)

        total_loans = d.pop("total_loans", UNSET)

        record = cls(
            end_of_month=end_of_month,
            imp_exp_reexp_fromhk_hkd=imp_exp_reexp_fromhk_hkd,
            imp_exp_reexp_fromhk_fc=imp_exp_reexp_fromhk_fc,
            imp_exp_reexp_fromhk_total=imp_exp_reexp_fromhk_total,
            merch_trade_nonhk_hkd=merch_trade_nonhk_hkd,
            merch_trade_nonhk_fc=merch_trade_nonhk_fc,
            merch_trade_nonhk_total=merch_trade_nonhk_total,
            loans_inhk_hkd=loans_inhk_hkd,
            loans_inhk_fc=loans_inhk_fc,
            loans_inhk_total=loans_inhk_total,
            other_loans_outhk_hkd=other_loans_outhk_hkd,
            other_loans_outhk_fc=other_loans_outhk_fc,
            other_loans_outhk_total=other_loans_outhk_total,
            other_loans_unkplace_hkd=other_loans_unkplace_hkd,
            other_loans_unkplace_fc=other_loans_unkplace_fc,
            other_loans_unkplace_total=other_loans_unkplace_total,
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
