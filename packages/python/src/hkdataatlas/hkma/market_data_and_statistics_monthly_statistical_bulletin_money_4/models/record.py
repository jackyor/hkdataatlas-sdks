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
        savings_deposits_with_lb (float | Unset):
        time_deposits_with_lb (float | Unset):
        ncds_by_lb_in_pub (float | Unset):
        m2_supply (float | Unset):
        deposits_with_rlbsdtcs (float | Unset):
        ncds_by_rlbsdtcs_in_pub (float | Unset):
        m3_supply (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    legal_tender_notes_coins_in_pub: float | Unset = UNSET
    demand_deposits_with_lb: float | Unset = UNSET
    m1_supply: float | Unset = UNSET
    savings_deposits_with_lb: float | Unset = UNSET
    time_deposits_with_lb: float | Unset = UNSET
    ncds_by_lb_in_pub: float | Unset = UNSET
    m2_supply: float | Unset = UNSET
    deposits_with_rlbsdtcs: float | Unset = UNSET
    ncds_by_rlbsdtcs_in_pub: float | Unset = UNSET
    m3_supply: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        legal_tender_notes_coins_in_pub = self.legal_tender_notes_coins_in_pub

        demand_deposits_with_lb = self.demand_deposits_with_lb

        m1_supply = self.m1_supply

        savings_deposits_with_lb = self.savings_deposits_with_lb

        time_deposits_with_lb = self.time_deposits_with_lb

        ncds_by_lb_in_pub = self.ncds_by_lb_in_pub

        m2_supply = self.m2_supply

        deposits_with_rlbsdtcs = self.deposits_with_rlbsdtcs

        ncds_by_rlbsdtcs_in_pub = self.ncds_by_rlbsdtcs_in_pub

        m3_supply = self.m3_supply

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
        if savings_deposits_with_lb is not UNSET:
            field_dict["savings_deposits_with_lb"] = savings_deposits_with_lb
        if time_deposits_with_lb is not UNSET:
            field_dict["time_deposits_with_lb"] = time_deposits_with_lb
        if ncds_by_lb_in_pub is not UNSET:
            field_dict["ncds_by_lb_in_pub"] = ncds_by_lb_in_pub
        if m2_supply is not UNSET:
            field_dict["m2_supply"] = m2_supply
        if deposits_with_rlbsdtcs is not UNSET:
            field_dict["deposits_with_rlbsdtcs"] = deposits_with_rlbsdtcs
        if ncds_by_rlbsdtcs_in_pub is not UNSET:
            field_dict["ncds_by_rlbsdtcs_in_pub"] = ncds_by_rlbsdtcs_in_pub
        if m3_supply is not UNSET:
            field_dict["m3_supply"] = m3_supply

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

        savings_deposits_with_lb = d.pop("savings_deposits_with_lb", UNSET)

        time_deposits_with_lb = d.pop("time_deposits_with_lb", UNSET)

        ncds_by_lb_in_pub = d.pop("ncds_by_lb_in_pub", UNSET)

        m2_supply = d.pop("m2_supply", UNSET)

        deposits_with_rlbsdtcs = d.pop("deposits_with_rlbsdtcs", UNSET)

        ncds_by_rlbsdtcs_in_pub = d.pop("ncds_by_rlbsdtcs_in_pub", UNSET)

        m3_supply = d.pop("m3_supply", UNSET)

        record = cls(
            end_of_month=end_of_month,
            legal_tender_notes_coins_in_pub=legal_tender_notes_coins_in_pub,
            demand_deposits_with_lb=demand_deposits_with_lb,
            m1_supply=m1_supply,
            savings_deposits_with_lb=savings_deposits_with_lb,
            time_deposits_with_lb=time_deposits_with_lb,
            ncds_by_lb_in_pub=ncds_by_lb_in_pub,
            m2_supply=m2_supply,
            deposits_with_rlbsdtcs=deposits_with_rlbsdtcs,
            ncds_by_rlbsdtcs_in_pub=ncds_by_rlbsdtcs_in_pub,
            m3_supply=m3_supply,
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
