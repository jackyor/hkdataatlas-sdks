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
        legal_tender_notes_coins_in_pub (float | Unset):
        demand_deposits_with_lb (float | Unset):
        m1_supply (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    legal_tender_notes_coins_in_pub: float | Unset = UNSET
    demand_deposits_with_lb: float | Unset = UNSET
    m1_supply: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        legal_tender_notes_coins_in_pub = self.legal_tender_notes_coins_in_pub

        demand_deposits_with_lb = self.demand_deposits_with_lb

        m1_supply = self.m1_supply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if legal_tender_notes_coins_in_pub is not UNSET:
            field_dict["legal_tender_notes_coins_in_pub"] = (
                legal_tender_notes_coins_in_pub
            )
        if demand_deposits_with_lb is not UNSET:
            field_dict["demand_deposits_with_lb"] = demand_deposits_with_lb
        if m1_supply is not UNSET:
            field_dict["m1_supply"] = m1_supply

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

        legal_tender_notes_coins_in_pub = d.pop(
            "legal_tender_notes_coins_in_pub", UNSET
        )

        demand_deposits_with_lb = d.pop("demand_deposits_with_lb", UNSET)

        m1_supply = d.pop("m1_supply", UNSET)

        record = cls(
            end_of_month=end_of_month,
            legal_tender_notes_coins_in_pub=legal_tender_notes_coins_in_pub,
            demand_deposits_with_lb=demand_deposits_with_lb,
            m1_supply=m1_supply,
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
