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
        unaudited_figures (str | Unset):
        assets_cash_money_at_call (float | Unset):
        assets_pla_bank_oth_fi_instit (float | Unset):
        assets_investments (float | Unset):
        assets_fixed_assets (float | Unset):
        assets_other_assets (float | Unset):
        assets_total (float | Unset):
        liab_cert_of_indebt (float | Unset):
        liab_gov_iss_curr_notes (float | Unset):
        liab_banking_system_bal (float | Unset):
        liab_ef_bills_notes_iss (float | Unset):
        liab_other_instit (float | Unset):
        liab_pla_bank_oth_fi_instit (float | Unset):
        liab_govfunds_statubodies (float | Unset):
        liab_fiscal_resv (float | Unset):
        liab_subsidiaries (float | Unset):
        liab_other (float | Unset):
        liab_total (float | Unset):
        fund_equity (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    unaudited_figures: str | Unset = UNSET
    assets_cash_money_at_call: float | Unset = UNSET
    assets_pla_bank_oth_fi_instit: float | Unset = UNSET
    assets_investments: float | Unset = UNSET
    assets_fixed_assets: float | Unset = UNSET
    assets_other_assets: float | Unset = UNSET
    assets_total: float | Unset = UNSET
    liab_cert_of_indebt: float | Unset = UNSET
    liab_gov_iss_curr_notes: float | Unset = UNSET
    liab_banking_system_bal: float | Unset = UNSET
    liab_ef_bills_notes_iss: float | Unset = UNSET
    liab_other_instit: float | Unset = UNSET
    liab_pla_bank_oth_fi_instit: float | Unset = UNSET
    liab_govfunds_statubodies: float | Unset = UNSET
    liab_fiscal_resv: float | Unset = UNSET
    liab_subsidiaries: float | Unset = UNSET
    liab_other: float | Unset = UNSET
    liab_total: float | Unset = UNSET
    fund_equity: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        unaudited_figures = self.unaudited_figures

        assets_cash_money_at_call = self.assets_cash_money_at_call

        assets_pla_bank_oth_fi_instit = self.assets_pla_bank_oth_fi_instit

        assets_investments = self.assets_investments

        assets_fixed_assets = self.assets_fixed_assets

        assets_other_assets = self.assets_other_assets

        assets_total = self.assets_total

        liab_cert_of_indebt = self.liab_cert_of_indebt

        liab_gov_iss_curr_notes = self.liab_gov_iss_curr_notes

        liab_banking_system_bal = self.liab_banking_system_bal

        liab_ef_bills_notes_iss = self.liab_ef_bills_notes_iss

        liab_other_instit = self.liab_other_instit

        liab_pla_bank_oth_fi_instit = self.liab_pla_bank_oth_fi_instit

        liab_govfunds_statubodies = self.liab_govfunds_statubodies

        liab_fiscal_resv = self.liab_fiscal_resv

        liab_subsidiaries = self.liab_subsidiaries

        liab_other = self.liab_other

        liab_total = self.liab_total

        fund_equity = self.fund_equity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if unaudited_figures is not UNSET:
            field_dict["unaudited_figures"] = unaudited_figures
        if assets_cash_money_at_call is not UNSET:
            field_dict["assets_cash_money_at_call"] = assets_cash_money_at_call
        if assets_pla_bank_oth_fi_instit is not UNSET:
            field_dict["assets_pla_bank_oth_fi_instit"] = assets_pla_bank_oth_fi_instit
        if assets_investments is not UNSET:
            field_dict["assets_investments"] = assets_investments
        if assets_fixed_assets is not UNSET:
            field_dict["assets_fixed_assets"] = assets_fixed_assets
        if assets_other_assets is not UNSET:
            field_dict["assets_other_assets"] = assets_other_assets
        if assets_total is not UNSET:
            field_dict["assets_total"] = assets_total
        if liab_cert_of_indebt is not UNSET:
            field_dict["liab_cert_of_indebt"] = liab_cert_of_indebt
        if liab_gov_iss_curr_notes is not UNSET:
            field_dict["liab_gov_iss_curr_notes"] = liab_gov_iss_curr_notes
        if liab_banking_system_bal is not UNSET:
            field_dict["liab_banking_system_bal"] = liab_banking_system_bal
        if liab_ef_bills_notes_iss is not UNSET:
            field_dict["liab_ef_bills_notes_iss"] = liab_ef_bills_notes_iss
        if liab_other_instit is not UNSET:
            field_dict["liab_other_instit"] = liab_other_instit
        if liab_pla_bank_oth_fi_instit is not UNSET:
            field_dict["liab_pla_bank_oth_fi_instit"] = liab_pla_bank_oth_fi_instit
        if liab_govfunds_statubodies is not UNSET:
            field_dict["liab_govfunds_statubodies"] = liab_govfunds_statubodies
        if liab_fiscal_resv is not UNSET:
            field_dict["liab_fiscal_resv"] = liab_fiscal_resv
        if liab_subsidiaries is not UNSET:
            field_dict["liab_subsidiaries"] = liab_subsidiaries
        if liab_other is not UNSET:
            field_dict["liab_other"] = liab_other
        if liab_total is not UNSET:
            field_dict["liab_total"] = liab_total
        if fund_equity is not UNSET:
            field_dict["fund_equity"] = fund_equity

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

        unaudited_figures = d.pop("unaudited_figures", UNSET)

        assets_cash_money_at_call = d.pop("assets_cash_money_at_call", UNSET)

        assets_pla_bank_oth_fi_instit = d.pop("assets_pla_bank_oth_fi_instit", UNSET)

        assets_investments = d.pop("assets_investments", UNSET)

        assets_fixed_assets = d.pop("assets_fixed_assets", UNSET)

        assets_other_assets = d.pop("assets_other_assets", UNSET)

        assets_total = d.pop("assets_total", UNSET)

        liab_cert_of_indebt = d.pop("liab_cert_of_indebt", UNSET)

        liab_gov_iss_curr_notes = d.pop("liab_gov_iss_curr_notes", UNSET)

        liab_banking_system_bal = d.pop("liab_banking_system_bal", UNSET)

        liab_ef_bills_notes_iss = d.pop("liab_ef_bills_notes_iss", UNSET)

        liab_other_instit = d.pop("liab_other_instit", UNSET)

        liab_pla_bank_oth_fi_instit = d.pop("liab_pla_bank_oth_fi_instit", UNSET)

        liab_govfunds_statubodies = d.pop("liab_govfunds_statubodies", UNSET)

        liab_fiscal_resv = d.pop("liab_fiscal_resv", UNSET)

        liab_subsidiaries = d.pop("liab_subsidiaries", UNSET)

        liab_other = d.pop("liab_other", UNSET)

        liab_total = d.pop("liab_total", UNSET)

        fund_equity = d.pop("fund_equity", UNSET)

        record = cls(
            end_of_month=end_of_month,
            unaudited_figures=unaudited_figures,
            assets_cash_money_at_call=assets_cash_money_at_call,
            assets_pla_bank_oth_fi_instit=assets_pla_bank_oth_fi_instit,
            assets_investments=assets_investments,
            assets_fixed_assets=assets_fixed_assets,
            assets_other_assets=assets_other_assets,
            assets_total=assets_total,
            liab_cert_of_indebt=liab_cert_of_indebt,
            liab_gov_iss_curr_notes=liab_gov_iss_curr_notes,
            liab_banking_system_bal=liab_banking_system_bal,
            liab_ef_bills_notes_iss=liab_ef_bills_notes_iss,
            liab_other_instit=liab_other_instit,
            liab_pla_bank_oth_fi_instit=liab_pla_bank_oth_fi_instit,
            liab_govfunds_statubodies=liab_govfunds_statubodies,
            liab_fiscal_resv=liab_fiscal_resv,
            liab_subsidiaries=liab_subsidiaries,
            liab_other=liab_other,
            liab_total=liab_total,
            fund_equity=fund_equity,
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
