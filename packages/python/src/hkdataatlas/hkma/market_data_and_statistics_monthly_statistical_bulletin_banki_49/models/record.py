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
        end_of_quarter (datetime.date | Unset):
        outstanding_loans (float | Unset):
        outstanding_loans_ratio (str | Unset):
        outstanding_loans_amt (float | Unset):
        outstanding_loans_amt_ratio (str | Unset):
        unsecured_portion_amt (float | Unset):
        lv_ratio (float | Unset):
    """

    end_of_quarter: datetime.date | Unset = UNSET
    outstanding_loans: float | Unset = UNSET
    outstanding_loans_ratio: str | Unset = UNSET
    outstanding_loans_amt: float | Unset = UNSET
    outstanding_loans_amt_ratio: str | Unset = UNSET
    unsecured_portion_amt: float | Unset = UNSET
    lv_ratio: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_quarter: str | Unset = UNSET
        if not isinstance(self.end_of_quarter, Unset):
            end_of_quarter = self.end_of_quarter.isoformat()

        outstanding_loans = self.outstanding_loans

        outstanding_loans_ratio = self.outstanding_loans_ratio

        outstanding_loans_amt = self.outstanding_loans_amt

        outstanding_loans_amt_ratio = self.outstanding_loans_amt_ratio

        unsecured_portion_amt = self.unsecured_portion_amt

        lv_ratio = self.lv_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_quarter is not UNSET:
            field_dict["end_of_quarter"] = end_of_quarter
        if outstanding_loans is not UNSET:
            field_dict["outstanding_loans"] = outstanding_loans
        if outstanding_loans_ratio is not UNSET:
            field_dict["outstanding_loans_ratio"] = outstanding_loans_ratio
        if outstanding_loans_amt is not UNSET:
            field_dict["outstanding_loans_amt"] = outstanding_loans_amt
        if outstanding_loans_amt_ratio is not UNSET:
            field_dict["outstanding_loans_amt_ratio"] = outstanding_loans_amt_ratio
        if unsecured_portion_amt is not UNSET:
            field_dict["unsecured_portion_amt"] = unsecured_portion_amt
        if lv_ratio is not UNSET:
            field_dict["lv_ratio"] = lv_ratio

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_quarter = d.pop("end_of_quarter", UNSET)
        end_of_quarter: datetime.date | Unset
        if isinstance(_end_of_quarter, Unset):
            end_of_quarter = UNSET
        else:
            end_of_quarter = datetime.date.fromisoformat(_end_of_quarter)

        outstanding_loans = d.pop("outstanding_loans", UNSET)

        outstanding_loans_ratio = d.pop("outstanding_loans_ratio", UNSET)

        outstanding_loans_amt = d.pop("outstanding_loans_amt", UNSET)

        outstanding_loans_amt_ratio = d.pop("outstanding_loans_amt_ratio", UNSET)

        unsecured_portion_amt = d.pop("unsecured_portion_amt", UNSET)

        lv_ratio = d.pop("lv_ratio", UNSET)

        record = cls(
            end_of_quarter=end_of_quarter,
            outstanding_loans=outstanding_loans,
            outstanding_loans_ratio=outstanding_loans_ratio,
            outstanding_loans_amt=outstanding_loans_amt,
            outstanding_loans_amt_ratio=outstanding_loans_amt_ratio,
            unsecured_portion_amt=unsecured_portion_amt,
            lv_ratio=lv_ratio,
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
