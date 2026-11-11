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
        bank_issues (float | Unset):
        gov_issues (float | Unset):
        total_issues (float | Unset):
        ais_hold_notes_coins (float | Unset):
        public_hold_notes_coins (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    bank_issues: float | Unset = UNSET
    gov_issues: float | Unset = UNSET
    total_issues: float | Unset = UNSET
    ais_hold_notes_coins: float | Unset = UNSET
    public_hold_notes_coins: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        bank_issues = self.bank_issues

        gov_issues = self.gov_issues

        total_issues = self.total_issues

        ais_hold_notes_coins = self.ais_hold_notes_coins

        public_hold_notes_coins = self.public_hold_notes_coins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if bank_issues is not UNSET:
            field_dict["bank_issues"] = bank_issues
        if gov_issues is not UNSET:
            field_dict["gov_issues"] = gov_issues
        if total_issues is not UNSET:
            field_dict["total_issues"] = total_issues
        if ais_hold_notes_coins is not UNSET:
            field_dict["ais_hold_notes_coins"] = ais_hold_notes_coins
        if public_hold_notes_coins is not UNSET:
            field_dict["public_hold_notes_coins"] = public_hold_notes_coins

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

        bank_issues = d.pop("bank_issues", UNSET)

        gov_issues = d.pop("gov_issues", UNSET)

        total_issues = d.pop("total_issues", UNSET)

        ais_hold_notes_coins = d.pop("ais_hold_notes_coins", UNSET)

        public_hold_notes_coins = d.pop("public_hold_notes_coins", UNSET)

        record = cls(
            end_of_month=end_of_month,
            bank_issues=bank_issues,
            gov_issues=gov_issues,
            total_issues=total_issues,
            ais_hold_notes_coins=ais_hold_notes_coins,
            public_hold_notes_coins=public_hold_notes_coins,
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
