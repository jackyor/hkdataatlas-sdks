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
        liability_bank_jp_hkd (float | Unset):
        liability_bank_jp_fc (float | Unset):
        claim_bank_jp_hkd (float | Unset):
        claim_bank_jp_fc (float | Unset):
        liability_nbc_jp_hkd (float | Unset):
        liability_nbc_jp_fc (float | Unset):
        claim_nbc_jp_hkd (float | Unset):
        claim_nbc_jp_fc (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    liability_bank_jp_hkd: float | Unset = UNSET
    liability_bank_jp_fc: float | Unset = UNSET
    claim_bank_jp_hkd: float | Unset = UNSET
    claim_bank_jp_fc: float | Unset = UNSET
    liability_nbc_jp_hkd: float | Unset = UNSET
    liability_nbc_jp_fc: float | Unset = UNSET
    claim_nbc_jp_hkd: float | Unset = UNSET
    claim_nbc_jp_fc: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        liability_bank_jp_hkd = self.liability_bank_jp_hkd

        liability_bank_jp_fc = self.liability_bank_jp_fc

        claim_bank_jp_hkd = self.claim_bank_jp_hkd

        claim_bank_jp_fc = self.claim_bank_jp_fc

        liability_nbc_jp_hkd = self.liability_nbc_jp_hkd

        liability_nbc_jp_fc = self.liability_nbc_jp_fc

        claim_nbc_jp_hkd = self.claim_nbc_jp_hkd

        claim_nbc_jp_fc = self.claim_nbc_jp_fc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if liability_bank_jp_hkd is not UNSET:
            field_dict["liability_bank_jp_hkd"] = liability_bank_jp_hkd
        if liability_bank_jp_fc is not UNSET:
            field_dict["liability_bank_jp_fc"] = liability_bank_jp_fc
        if claim_bank_jp_hkd is not UNSET:
            field_dict["claim_bank_jp_hkd"] = claim_bank_jp_hkd
        if claim_bank_jp_fc is not UNSET:
            field_dict["claim_bank_jp_fc"] = claim_bank_jp_fc
        if liability_nbc_jp_hkd is not UNSET:
            field_dict["liability_nbc_jp_hkd"] = liability_nbc_jp_hkd
        if liability_nbc_jp_fc is not UNSET:
            field_dict["liability_nbc_jp_fc"] = liability_nbc_jp_fc
        if claim_nbc_jp_hkd is not UNSET:
            field_dict["claim_nbc_jp_hkd"] = claim_nbc_jp_hkd
        if claim_nbc_jp_fc is not UNSET:
            field_dict["claim_nbc_jp_fc"] = claim_nbc_jp_fc

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

        liability_bank_jp_hkd = d.pop("liability_bank_jp_hkd", UNSET)

        liability_bank_jp_fc = d.pop("liability_bank_jp_fc", UNSET)

        claim_bank_jp_hkd = d.pop("claim_bank_jp_hkd", UNSET)

        claim_bank_jp_fc = d.pop("claim_bank_jp_fc", UNSET)

        liability_nbc_jp_hkd = d.pop("liability_nbc_jp_hkd", UNSET)

        liability_nbc_jp_fc = d.pop("liability_nbc_jp_fc", UNSET)

        claim_nbc_jp_hkd = d.pop("claim_nbc_jp_hkd", UNSET)

        claim_nbc_jp_fc = d.pop("claim_nbc_jp_fc", UNSET)

        record = cls(
            end_of_month=end_of_month,
            liability_bank_jp_hkd=liability_bank_jp_hkd,
            liability_bank_jp_fc=liability_bank_jp_fc,
            claim_bank_jp_hkd=claim_bank_jp_hkd,
            claim_bank_jp_fc=claim_bank_jp_fc,
            liability_nbc_jp_hkd=liability_nbc_jp_hkd,
            liability_nbc_jp_fc=liability_nbc_jp_fc,
            claim_nbc_jp_hkd=claim_nbc_jp_hkd,
            claim_nbc_jp_fc=claim_nbc_jp_fc,
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
