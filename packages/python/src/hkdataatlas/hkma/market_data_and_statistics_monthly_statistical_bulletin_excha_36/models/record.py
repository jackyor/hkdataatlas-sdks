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
        mb_cert_of_indebt (float | Unset):
        mb_gov_notes_coins_cir (float | Unset):
        mb_efbn_issued (float | Unset):
        mb_interest_payable_efn (float | Unset):
        mb_bal_bank_system (float | Unset):
        mb_net_acc (float | Unset):
        mb_total (float | Unset):
        ba_invest_usd_assets (float | Unset):
        ba_interest_receivable_usd_assets (float | Unset):
        ba_net_acc (float | Unset):
        ba_total (float | Unset):
        backing_ratio (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    mb_cert_of_indebt: float | Unset = UNSET
    mb_gov_notes_coins_cir: float | Unset = UNSET
    mb_efbn_issued: float | Unset = UNSET
    mb_interest_payable_efn: float | Unset = UNSET
    mb_bal_bank_system: float | Unset = UNSET
    mb_net_acc: float | Unset = UNSET
    mb_total: float | Unset = UNSET
    ba_invest_usd_assets: float | Unset = UNSET
    ba_interest_receivable_usd_assets: float | Unset = UNSET
    ba_net_acc: float | Unset = UNSET
    ba_total: float | Unset = UNSET
    backing_ratio: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        mb_cert_of_indebt = self.mb_cert_of_indebt

        mb_gov_notes_coins_cir = self.mb_gov_notes_coins_cir

        mb_efbn_issued = self.mb_efbn_issued

        mb_interest_payable_efn = self.mb_interest_payable_efn

        mb_bal_bank_system = self.mb_bal_bank_system

        mb_net_acc = self.mb_net_acc

        mb_total = self.mb_total

        ba_invest_usd_assets = self.ba_invest_usd_assets

        ba_interest_receivable_usd_assets = self.ba_interest_receivable_usd_assets

        ba_net_acc = self.ba_net_acc

        ba_total = self.ba_total

        backing_ratio = self.backing_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if mb_cert_of_indebt is not UNSET:
            field_dict["mb_cert_of_indebt"] = mb_cert_of_indebt
        if mb_gov_notes_coins_cir is not UNSET:
            field_dict["mb_gov_notes_coins_cir"] = mb_gov_notes_coins_cir
        if mb_efbn_issued is not UNSET:
            field_dict["mb_efbn_issued"] = mb_efbn_issued
        if mb_interest_payable_efn is not UNSET:
            field_dict["mb_interest_payable_efn"] = mb_interest_payable_efn
        if mb_bal_bank_system is not UNSET:
            field_dict["mb_bal_bank_system"] = mb_bal_bank_system
        if mb_net_acc is not UNSET:
            field_dict["mb_net_acc"] = mb_net_acc
        if mb_total is not UNSET:
            field_dict["mb_total"] = mb_total
        if ba_invest_usd_assets is not UNSET:
            field_dict["ba_invest_usd_assets"] = ba_invest_usd_assets
        if ba_interest_receivable_usd_assets is not UNSET:
            field_dict["ba_interest_receivable_usd_assets"] = (
                ba_interest_receivable_usd_assets
            )
        if ba_net_acc is not UNSET:
            field_dict["ba_net_acc"] = ba_net_acc
        if ba_total is not UNSET:
            field_dict["ba_total"] = ba_total
        if backing_ratio is not UNSET:
            field_dict["backing_ratio"] = backing_ratio

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

        mb_cert_of_indebt = d.pop("mb_cert_of_indebt", UNSET)

        mb_gov_notes_coins_cir = d.pop("mb_gov_notes_coins_cir", UNSET)

        mb_efbn_issued = d.pop("mb_efbn_issued", UNSET)

        mb_interest_payable_efn = d.pop("mb_interest_payable_efn", UNSET)

        mb_bal_bank_system = d.pop("mb_bal_bank_system", UNSET)

        mb_net_acc = d.pop("mb_net_acc", UNSET)

        mb_total = d.pop("mb_total", UNSET)

        ba_invest_usd_assets = d.pop("ba_invest_usd_assets", UNSET)

        ba_interest_receivable_usd_assets = d.pop(
            "ba_interest_receivable_usd_assets", UNSET
        )

        ba_net_acc = d.pop("ba_net_acc", UNSET)

        ba_total = d.pop("ba_total", UNSET)

        backing_ratio = d.pop("backing_ratio", UNSET)

        record = cls(
            end_of_month=end_of_month,
            mb_cert_of_indebt=mb_cert_of_indebt,
            mb_gov_notes_coins_cir=mb_gov_notes_coins_cir,
            mb_efbn_issued=mb_efbn_issued,
            mb_interest_payable_efn=mb_interest_payable_efn,
            mb_bal_bank_system=mb_bal_bank_system,
            mb_net_acc=mb_net_acc,
            mb_total=mb_total,
            ba_invest_usd_assets=ba_invest_usd_assets,
            ba_interest_receivable_usd_assets=ba_interest_receivable_usd_assets,
            ba_net_acc=ba_net_acc,
            ba_total=ba_total,
            backing_ratio=backing_ratio,
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
