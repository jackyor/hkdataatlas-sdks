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
        liab_amtaisinhk_hkd (float | Unset):
        liab_amtaisinhk_fc (float | Unset):
        liab_amtaisinhk_total (float | Unset):
        liab_amtbanksabroad_hkd (float | Unset):
        liab_amtbanksabroad_fc (float | Unset):
        liab_amtbanksabroad_total (float | Unset):
        liab_depcust_hkd (float | Unset):
        liab_depcust_fc (float | Unset):
        liab_depcust_total (float | Unset):
        liab_ncdepoutst_hkd (float | Unset):
        liab_ncdepoutst_fc (float | Unset):
        liab_ncdepoutst_total (float | Unset):
        liab_othdebtinstoutst_hkd (float | Unset):
        liab_othdebtinstoutst_fc (float | Unset):
        liab_othdebtinstoutst_total (float | Unset):
        liab_capreserv_hkd (float | Unset):
        liab_capreserv_fc (float | Unset):
        liab_capreserv_total (float | Unset):
        liab_total_hkd (float | Unset):
        liab_total_fc (float | Unset):
        liab_total (float | Unset):
        asst_notescoins_hkd (float | Unset):
        asst_notescoins_fc (float | Unset):
        asst_notescoins_total (float | Unset):
        asst_amtaisinhk_hkd (float | Unset):
        asst_amtaisinhk_fc (float | Unset):
        asst_amtaisinhk_total (float | Unset):
        asst_amtbanksabroad_hkd (float | Unset):
        asst_amtbanksabroad_fc (float | Unset):
        asst_amtbanksabroad_total (float | Unset):
        asst_loanadvtocust_hkd (float | Unset):
        asst_loanadvtocust_fc (float | Unset):
        asst_loanadvtocust_total (float | Unset):
        asst_ncdepheld_hkd (float | Unset):
        asst_ncdepheld_fc (float | Unset):
        asst_ncdepheld_total (float | Unset):
        asst_ncdepheld_lb_hkd (float | Unset):
        asst_ncdepheld_lb_fc (float | Unset):
        asst_ncdepheld_lb_total (float | Unset):
        asst_ncdepheld_rlb_hkd (float | Unset):
        asst_ncdepheld_rlb_fc (float | Unset):
        asst_ncdepheld_rlb_total (float | Unset):
        asst_ncdepheld_dtc_hkd (float | Unset):
        asst_ncdepheld_dtc_fc (float | Unset):
        asst_ncdepheld_dtc_total (float | Unset):
        asst_ncdepheld_bkouthk_hkd (float | Unset):
        asst_ncdepheld_bkouthk_fc (float | Unset):
        asst_ncdepheld_bkouthk_total (float | Unset):
        asst_negodebt_hkd (float | Unset):
        asst_negodebt_fc (float | Unset):
        asst_negodebt_total (float | Unset):
        asst_negodebt_accbill_hkd (float | Unset):
        asst_negodebt_accbill_fc (float | Unset):
        asst_negodebt_accbill_total (float | Unset):
        asst_negodebt_fltnote_hkd (float | Unset):
        asst_negodebt_fltnote_fc (float | Unset):
        asst_negodebt_fltnote_total (float | Unset):
        asst_negodebt_gov_hkd (float | Unset):
        asst_negodebt_gov_fc (float | Unset):
        asst_negodebt_gov_total (float | Unset):
        asst_negodebt_other_hkd (float | Unset):
        asst_negodebt_other_fc (float | Unset):
        asst_negodebt_other_total (float | Unset):
        asst_invinshare_hkd (float | Unset):
        asst_invinshare_fc (float | Unset):
        asst_invinshare_total (float | Unset):
        asst_intinland_hkd (float | Unset):
        asst_intinland_fc (float | Unset):
        asst_intinland_total (float | Unset):
        asst_other_hkd (float | Unset):
        asst_other_fc (float | Unset):
        asst_other_total (float | Unset):
        total_asst_hkd (float | Unset):
        total_asst_fc (float | Unset):
        total_asst_total (float | Unset):
        no_of_report_instit (float | Unset):
        no_of_local_branch (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    liab_amtaisinhk_hkd: float | Unset = UNSET
    liab_amtaisinhk_fc: float | Unset = UNSET
    liab_amtaisinhk_total: float | Unset = UNSET
    liab_amtbanksabroad_hkd: float | Unset = UNSET
    liab_amtbanksabroad_fc: float | Unset = UNSET
    liab_amtbanksabroad_total: float | Unset = UNSET
    liab_depcust_hkd: float | Unset = UNSET
    liab_depcust_fc: float | Unset = UNSET
    liab_depcust_total: float | Unset = UNSET
    liab_ncdepoutst_hkd: float | Unset = UNSET
    liab_ncdepoutst_fc: float | Unset = UNSET
    liab_ncdepoutst_total: float | Unset = UNSET
    liab_othdebtinstoutst_hkd: float | Unset = UNSET
    liab_othdebtinstoutst_fc: float | Unset = UNSET
    liab_othdebtinstoutst_total: float | Unset = UNSET
    liab_capreserv_hkd: float | Unset = UNSET
    liab_capreserv_fc: float | Unset = UNSET
    liab_capreserv_total: float | Unset = UNSET
    liab_total_hkd: float | Unset = UNSET
    liab_total_fc: float | Unset = UNSET
    liab_total: float | Unset = UNSET
    asst_notescoins_hkd: float | Unset = UNSET
    asst_notescoins_fc: float | Unset = UNSET
    asst_notescoins_total: float | Unset = UNSET
    asst_amtaisinhk_hkd: float | Unset = UNSET
    asst_amtaisinhk_fc: float | Unset = UNSET
    asst_amtaisinhk_total: float | Unset = UNSET
    asst_amtbanksabroad_hkd: float | Unset = UNSET
    asst_amtbanksabroad_fc: float | Unset = UNSET
    asst_amtbanksabroad_total: float | Unset = UNSET
    asst_loanadvtocust_hkd: float | Unset = UNSET
    asst_loanadvtocust_fc: float | Unset = UNSET
    asst_loanadvtocust_total: float | Unset = UNSET
    asst_ncdepheld_hkd: float | Unset = UNSET
    asst_ncdepheld_fc: float | Unset = UNSET
    asst_ncdepheld_total: float | Unset = UNSET
    asst_ncdepheld_lb_hkd: float | Unset = UNSET
    asst_ncdepheld_lb_fc: float | Unset = UNSET
    asst_ncdepheld_lb_total: float | Unset = UNSET
    asst_ncdepheld_rlb_hkd: float | Unset = UNSET
    asst_ncdepheld_rlb_fc: float | Unset = UNSET
    asst_ncdepheld_rlb_total: float | Unset = UNSET
    asst_ncdepheld_dtc_hkd: float | Unset = UNSET
    asst_ncdepheld_dtc_fc: float | Unset = UNSET
    asst_ncdepheld_dtc_total: float | Unset = UNSET
    asst_ncdepheld_bkouthk_hkd: float | Unset = UNSET
    asst_ncdepheld_bkouthk_fc: float | Unset = UNSET
    asst_ncdepheld_bkouthk_total: float | Unset = UNSET
    asst_negodebt_hkd: float | Unset = UNSET
    asst_negodebt_fc: float | Unset = UNSET
    asst_negodebt_total: float | Unset = UNSET
    asst_negodebt_accbill_hkd: float | Unset = UNSET
    asst_negodebt_accbill_fc: float | Unset = UNSET
    asst_negodebt_accbill_total: float | Unset = UNSET
    asst_negodebt_fltnote_hkd: float | Unset = UNSET
    asst_negodebt_fltnote_fc: float | Unset = UNSET
    asst_negodebt_fltnote_total: float | Unset = UNSET
    asst_negodebt_gov_hkd: float | Unset = UNSET
    asst_negodebt_gov_fc: float | Unset = UNSET
    asst_negodebt_gov_total: float | Unset = UNSET
    asst_negodebt_other_hkd: float | Unset = UNSET
    asst_negodebt_other_fc: float | Unset = UNSET
    asst_negodebt_other_total: float | Unset = UNSET
    asst_invinshare_hkd: float | Unset = UNSET
    asst_invinshare_fc: float | Unset = UNSET
    asst_invinshare_total: float | Unset = UNSET
    asst_intinland_hkd: float | Unset = UNSET
    asst_intinland_fc: float | Unset = UNSET
    asst_intinland_total: float | Unset = UNSET
    asst_other_hkd: float | Unset = UNSET
    asst_other_fc: float | Unset = UNSET
    asst_other_total: float | Unset = UNSET
    total_asst_hkd: float | Unset = UNSET
    total_asst_fc: float | Unset = UNSET
    total_asst_total: float | Unset = UNSET
    no_of_report_instit: float | Unset = UNSET
    no_of_local_branch: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        liab_amtaisinhk_hkd = self.liab_amtaisinhk_hkd

        liab_amtaisinhk_fc = self.liab_amtaisinhk_fc

        liab_amtaisinhk_total = self.liab_amtaisinhk_total

        liab_amtbanksabroad_hkd = self.liab_amtbanksabroad_hkd

        liab_amtbanksabroad_fc = self.liab_amtbanksabroad_fc

        liab_amtbanksabroad_total = self.liab_amtbanksabroad_total

        liab_depcust_hkd = self.liab_depcust_hkd

        liab_depcust_fc = self.liab_depcust_fc

        liab_depcust_total = self.liab_depcust_total

        liab_ncdepoutst_hkd = self.liab_ncdepoutst_hkd

        liab_ncdepoutst_fc = self.liab_ncdepoutst_fc

        liab_ncdepoutst_total = self.liab_ncdepoutst_total

        liab_othdebtinstoutst_hkd = self.liab_othdebtinstoutst_hkd

        liab_othdebtinstoutst_fc = self.liab_othdebtinstoutst_fc

        liab_othdebtinstoutst_total = self.liab_othdebtinstoutst_total

        liab_capreserv_hkd = self.liab_capreserv_hkd

        liab_capreserv_fc = self.liab_capreserv_fc

        liab_capreserv_total = self.liab_capreserv_total

        liab_total_hkd = self.liab_total_hkd

        liab_total_fc = self.liab_total_fc

        liab_total = self.liab_total

        asst_notescoins_hkd = self.asst_notescoins_hkd

        asst_notescoins_fc = self.asst_notescoins_fc

        asst_notescoins_total = self.asst_notescoins_total

        asst_amtaisinhk_hkd = self.asst_amtaisinhk_hkd

        asst_amtaisinhk_fc = self.asst_amtaisinhk_fc

        asst_amtaisinhk_total = self.asst_amtaisinhk_total

        asst_amtbanksabroad_hkd = self.asst_amtbanksabroad_hkd

        asst_amtbanksabroad_fc = self.asst_amtbanksabroad_fc

        asst_amtbanksabroad_total = self.asst_amtbanksabroad_total

        asst_loanadvtocust_hkd = self.asst_loanadvtocust_hkd

        asst_loanadvtocust_fc = self.asst_loanadvtocust_fc

        asst_loanadvtocust_total = self.asst_loanadvtocust_total

        asst_ncdepheld_hkd = self.asst_ncdepheld_hkd

        asst_ncdepheld_fc = self.asst_ncdepheld_fc

        asst_ncdepheld_total = self.asst_ncdepheld_total

        asst_ncdepheld_lb_hkd = self.asst_ncdepheld_lb_hkd

        asst_ncdepheld_lb_fc = self.asst_ncdepheld_lb_fc

        asst_ncdepheld_lb_total = self.asst_ncdepheld_lb_total

        asst_ncdepheld_rlb_hkd = self.asst_ncdepheld_rlb_hkd

        asst_ncdepheld_rlb_fc = self.asst_ncdepheld_rlb_fc

        asst_ncdepheld_rlb_total = self.asst_ncdepheld_rlb_total

        asst_ncdepheld_dtc_hkd = self.asst_ncdepheld_dtc_hkd

        asst_ncdepheld_dtc_fc = self.asst_ncdepheld_dtc_fc

        asst_ncdepheld_dtc_total = self.asst_ncdepheld_dtc_total

        asst_ncdepheld_bkouthk_hkd = self.asst_ncdepheld_bkouthk_hkd

        asst_ncdepheld_bkouthk_fc = self.asst_ncdepheld_bkouthk_fc

        asst_ncdepheld_bkouthk_total = self.asst_ncdepheld_bkouthk_total

        asst_negodebt_hkd = self.asst_negodebt_hkd

        asst_negodebt_fc = self.asst_negodebt_fc

        asst_negodebt_total = self.asst_negodebt_total

        asst_negodebt_accbill_hkd = self.asst_negodebt_accbill_hkd

        asst_negodebt_accbill_fc = self.asst_negodebt_accbill_fc

        asst_negodebt_accbill_total = self.asst_negodebt_accbill_total

        asst_negodebt_fltnote_hkd = self.asst_negodebt_fltnote_hkd

        asst_negodebt_fltnote_fc = self.asst_negodebt_fltnote_fc

        asst_negodebt_fltnote_total = self.asst_negodebt_fltnote_total

        asst_negodebt_gov_hkd = self.asst_negodebt_gov_hkd

        asst_negodebt_gov_fc = self.asst_negodebt_gov_fc

        asst_negodebt_gov_total = self.asst_negodebt_gov_total

        asst_negodebt_other_hkd = self.asst_negodebt_other_hkd

        asst_negodebt_other_fc = self.asst_negodebt_other_fc

        asst_negodebt_other_total = self.asst_negodebt_other_total

        asst_invinshare_hkd = self.asst_invinshare_hkd

        asst_invinshare_fc = self.asst_invinshare_fc

        asst_invinshare_total = self.asst_invinshare_total

        asst_intinland_hkd = self.asst_intinland_hkd

        asst_intinland_fc = self.asst_intinland_fc

        asst_intinland_total = self.asst_intinland_total

        asst_other_hkd = self.asst_other_hkd

        asst_other_fc = self.asst_other_fc

        asst_other_total = self.asst_other_total

        total_asst_hkd = self.total_asst_hkd

        total_asst_fc = self.total_asst_fc

        total_asst_total = self.total_asst_total

        no_of_report_instit = self.no_of_report_instit

        no_of_local_branch = self.no_of_local_branch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if liab_amtaisinhk_hkd is not UNSET:
            field_dict["liab_amtaisinhk_hkd"] = liab_amtaisinhk_hkd
        if liab_amtaisinhk_fc is not UNSET:
            field_dict["liab_amtaisinhk_fc"] = liab_amtaisinhk_fc
        if liab_amtaisinhk_total is not UNSET:
            field_dict["liab_amtaisinhk_total"] = liab_amtaisinhk_total
        if liab_amtbanksabroad_hkd is not UNSET:
            field_dict["liab_amtbanksabroad_hkd"] = liab_amtbanksabroad_hkd
        if liab_amtbanksabroad_fc is not UNSET:
            field_dict["liab_amtbanksabroad_fc"] = liab_amtbanksabroad_fc
        if liab_amtbanksabroad_total is not UNSET:
            field_dict["liab_amtbanksabroad_total"] = liab_amtbanksabroad_total
        if liab_depcust_hkd is not UNSET:
            field_dict["liab_depcust_hkd"] = liab_depcust_hkd
        if liab_depcust_fc is not UNSET:
            field_dict["liab_depcust_fc"] = liab_depcust_fc
        if liab_depcust_total is not UNSET:
            field_dict["liab_depcust_total"] = liab_depcust_total
        if liab_ncdepoutst_hkd is not UNSET:
            field_dict["liab_ncdepoutst_hkd"] = liab_ncdepoutst_hkd
        if liab_ncdepoutst_fc is not UNSET:
            field_dict["liab_ncdepoutst_fc"] = liab_ncdepoutst_fc
        if liab_ncdepoutst_total is not UNSET:
            field_dict["liab_ncdepoutst_total"] = liab_ncdepoutst_total
        if liab_othdebtinstoutst_hkd is not UNSET:
            field_dict["liab_othdebtinstoutst_hkd"] = liab_othdebtinstoutst_hkd
        if liab_othdebtinstoutst_fc is not UNSET:
            field_dict["liab_othdebtinstoutst_fc"] = liab_othdebtinstoutst_fc
        if liab_othdebtinstoutst_total is not UNSET:
            field_dict["liab_othdebtinstoutst_total"] = liab_othdebtinstoutst_total
        if liab_capreserv_hkd is not UNSET:
            field_dict["liab_capreserv_hkd"] = liab_capreserv_hkd
        if liab_capreserv_fc is not UNSET:
            field_dict["liab_capreserv_fc"] = liab_capreserv_fc
        if liab_capreserv_total is not UNSET:
            field_dict["liab_capreserv_total"] = liab_capreserv_total
        if liab_total_hkd is not UNSET:
            field_dict["liab_total_hkd"] = liab_total_hkd
        if liab_total_fc is not UNSET:
            field_dict["liab_total_fc"] = liab_total_fc
        if liab_total is not UNSET:
            field_dict["liab_total"] = liab_total
        if asst_notescoins_hkd is not UNSET:
            field_dict["asst_notescoins_hkd"] = asst_notescoins_hkd
        if asst_notescoins_fc is not UNSET:
            field_dict["asst_notescoins_fc"] = asst_notescoins_fc
        if asst_notescoins_total is not UNSET:
            field_dict["asst_notescoins_total"] = asst_notescoins_total
        if asst_amtaisinhk_hkd is not UNSET:
            field_dict["asst_amtaisinhk_hkd"] = asst_amtaisinhk_hkd
        if asst_amtaisinhk_fc is not UNSET:
            field_dict["asst_amtaisinhk_fc"] = asst_amtaisinhk_fc
        if asst_amtaisinhk_total is not UNSET:
            field_dict["asst_amtaisinhk_total"] = asst_amtaisinhk_total
        if asst_amtbanksabroad_hkd is not UNSET:
            field_dict["asst_amtbanksabroad_hkd"] = asst_amtbanksabroad_hkd
        if asst_amtbanksabroad_fc is not UNSET:
            field_dict["asst_amtbanksabroad_fc"] = asst_amtbanksabroad_fc
        if asst_amtbanksabroad_total is not UNSET:
            field_dict["asst_amtbanksabroad_total"] = asst_amtbanksabroad_total
        if asst_loanadvtocust_hkd is not UNSET:
            field_dict["asst_loanadvtocust_hkd"] = asst_loanadvtocust_hkd
        if asst_loanadvtocust_fc is not UNSET:
            field_dict["asst_loanadvtocust_fc"] = asst_loanadvtocust_fc
        if asst_loanadvtocust_total is not UNSET:
            field_dict["asst_loanadvtocust_total"] = asst_loanadvtocust_total
        if asst_ncdepheld_hkd is not UNSET:
            field_dict["asst_ncdepheld_hkd"] = asst_ncdepheld_hkd
        if asst_ncdepheld_fc is not UNSET:
            field_dict["asst_ncdepheld_fc"] = asst_ncdepheld_fc
        if asst_ncdepheld_total is not UNSET:
            field_dict["asst_ncdepheld_total"] = asst_ncdepheld_total
        if asst_ncdepheld_lb_hkd is not UNSET:
            field_dict["asst_ncdepheld_lb_hkd"] = asst_ncdepheld_lb_hkd
        if asst_ncdepheld_lb_fc is not UNSET:
            field_dict["asst_ncdepheld_lb_fc"] = asst_ncdepheld_lb_fc
        if asst_ncdepheld_lb_total is not UNSET:
            field_dict["asst_ncdepheld_lb_total"] = asst_ncdepheld_lb_total
        if asst_ncdepheld_rlb_hkd is not UNSET:
            field_dict["asst_ncdepheld_rlb_hkd"] = asst_ncdepheld_rlb_hkd
        if asst_ncdepheld_rlb_fc is not UNSET:
            field_dict["asst_ncdepheld_rlb_fc"] = asst_ncdepheld_rlb_fc
        if asst_ncdepheld_rlb_total is not UNSET:
            field_dict["asst_ncdepheld_rlb_total"] = asst_ncdepheld_rlb_total
        if asst_ncdepheld_dtc_hkd is not UNSET:
            field_dict["asst_ncdepheld_dtc_hkd"] = asst_ncdepheld_dtc_hkd
        if asst_ncdepheld_dtc_fc is not UNSET:
            field_dict["asst_ncdepheld_dtc_fc"] = asst_ncdepheld_dtc_fc
        if asst_ncdepheld_dtc_total is not UNSET:
            field_dict["asst_ncdepheld_dtc_total"] = asst_ncdepheld_dtc_total
        if asst_ncdepheld_bkouthk_hkd is not UNSET:
            field_dict["asst_ncdepheld_bkouthk_hkd"] = asst_ncdepheld_bkouthk_hkd
        if asst_ncdepheld_bkouthk_fc is not UNSET:
            field_dict["asst_ncdepheld_bkouthk_fc"] = asst_ncdepheld_bkouthk_fc
        if asst_ncdepheld_bkouthk_total is not UNSET:
            field_dict["asst_ncdepheld_bkouthk_total"] = asst_ncdepheld_bkouthk_total
        if asst_negodebt_hkd is not UNSET:
            field_dict["asst_negodebt_hkd"] = asst_negodebt_hkd
        if asst_negodebt_fc is not UNSET:
            field_dict["asst_negodebt_fc"] = asst_negodebt_fc
        if asst_negodebt_total is not UNSET:
            field_dict["asst_negodebt_total"] = asst_negodebt_total
        if asst_negodebt_accbill_hkd is not UNSET:
            field_dict["asst_negodebt_accbill_hkd"] = asst_negodebt_accbill_hkd
        if asst_negodebt_accbill_fc is not UNSET:
            field_dict["asst_negodebt_accbill_fc"] = asst_negodebt_accbill_fc
        if asst_negodebt_accbill_total is not UNSET:
            field_dict["asst_negodebt_accbill_total"] = asst_negodebt_accbill_total
        if asst_negodebt_fltnote_hkd is not UNSET:
            field_dict["asst_negodebt_fltnote_hkd"] = asst_negodebt_fltnote_hkd
        if asst_negodebt_fltnote_fc is not UNSET:
            field_dict["asst_negodebt_fltnote_fc"] = asst_negodebt_fltnote_fc
        if asst_negodebt_fltnote_total is not UNSET:
            field_dict["asst_negodebt_fltnote_total"] = asst_negodebt_fltnote_total
        if asst_negodebt_gov_hkd is not UNSET:
            field_dict["asst_negodebt_gov_hkd"] = asst_negodebt_gov_hkd
        if asst_negodebt_gov_fc is not UNSET:
            field_dict["asst_negodebt_gov_fc"] = asst_negodebt_gov_fc
        if asst_negodebt_gov_total is not UNSET:
            field_dict["asst_negodebt_gov_total"] = asst_negodebt_gov_total
        if asst_negodebt_other_hkd is not UNSET:
            field_dict["asst_negodebt_other_hkd"] = asst_negodebt_other_hkd
        if asst_negodebt_other_fc is not UNSET:
            field_dict["asst_negodebt_other_fc"] = asst_negodebt_other_fc
        if asst_negodebt_other_total is not UNSET:
            field_dict["asst_negodebt_other_total"] = asst_negodebt_other_total
        if asst_invinshare_hkd is not UNSET:
            field_dict["asst_invinshare_hkd"] = asst_invinshare_hkd
        if asst_invinshare_fc is not UNSET:
            field_dict["asst_invinshare_fc"] = asst_invinshare_fc
        if asst_invinshare_total is not UNSET:
            field_dict["asst_invinshare_total"] = asst_invinshare_total
        if asst_intinland_hkd is not UNSET:
            field_dict["asst_intinland_hkd"] = asst_intinland_hkd
        if asst_intinland_fc is not UNSET:
            field_dict["asst_intinland_fc"] = asst_intinland_fc
        if asst_intinland_total is not UNSET:
            field_dict["asst_intinland_total"] = asst_intinland_total
        if asst_other_hkd is not UNSET:
            field_dict["asst_other_hkd"] = asst_other_hkd
        if asst_other_fc is not UNSET:
            field_dict["asst_other_fc"] = asst_other_fc
        if asst_other_total is not UNSET:
            field_dict["asst_other_total"] = asst_other_total
        if total_asst_hkd is not UNSET:
            field_dict["total_asst_hkd"] = total_asst_hkd
        if total_asst_fc is not UNSET:
            field_dict["total_asst_fc"] = total_asst_fc
        if total_asst_total is not UNSET:
            field_dict["total_asst_total"] = total_asst_total
        if no_of_report_instit is not UNSET:
            field_dict["no_of_report_instit"] = no_of_report_instit
        if no_of_local_branch is not UNSET:
            field_dict["no_of_local_branch"] = no_of_local_branch

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

        liab_amtaisinhk_hkd = d.pop("liab_amtaisinhk_hkd", UNSET)

        liab_amtaisinhk_fc = d.pop("liab_amtaisinhk_fc", UNSET)

        liab_amtaisinhk_total = d.pop("liab_amtaisinhk_total", UNSET)

        liab_amtbanksabroad_hkd = d.pop("liab_amtbanksabroad_hkd", UNSET)

        liab_amtbanksabroad_fc = d.pop("liab_amtbanksabroad_fc", UNSET)

        liab_amtbanksabroad_total = d.pop("liab_amtbanksabroad_total", UNSET)

        liab_depcust_hkd = d.pop("liab_depcust_hkd", UNSET)

        liab_depcust_fc = d.pop("liab_depcust_fc", UNSET)

        liab_depcust_total = d.pop("liab_depcust_total", UNSET)

        liab_ncdepoutst_hkd = d.pop("liab_ncdepoutst_hkd", UNSET)

        liab_ncdepoutst_fc = d.pop("liab_ncdepoutst_fc", UNSET)

        liab_ncdepoutst_total = d.pop("liab_ncdepoutst_total", UNSET)

        liab_othdebtinstoutst_hkd = d.pop("liab_othdebtinstoutst_hkd", UNSET)

        liab_othdebtinstoutst_fc = d.pop("liab_othdebtinstoutst_fc", UNSET)

        liab_othdebtinstoutst_total = d.pop("liab_othdebtinstoutst_total", UNSET)

        liab_capreserv_hkd = d.pop("liab_capreserv_hkd", UNSET)

        liab_capreserv_fc = d.pop("liab_capreserv_fc", UNSET)

        liab_capreserv_total = d.pop("liab_capreserv_total", UNSET)

        liab_total_hkd = d.pop("liab_total_hkd", UNSET)

        liab_total_fc = d.pop("liab_total_fc", UNSET)

        liab_total = d.pop("liab_total", UNSET)

        asst_notescoins_hkd = d.pop("asst_notescoins_hkd", UNSET)

        asst_notescoins_fc = d.pop("asst_notescoins_fc", UNSET)

        asst_notescoins_total = d.pop("asst_notescoins_total", UNSET)

        asst_amtaisinhk_hkd = d.pop("asst_amtaisinhk_hkd", UNSET)

        asst_amtaisinhk_fc = d.pop("asst_amtaisinhk_fc", UNSET)

        asst_amtaisinhk_total = d.pop("asst_amtaisinhk_total", UNSET)

        asst_amtbanksabroad_hkd = d.pop("asst_amtbanksabroad_hkd", UNSET)

        asst_amtbanksabroad_fc = d.pop("asst_amtbanksabroad_fc", UNSET)

        asst_amtbanksabroad_total = d.pop("asst_amtbanksabroad_total", UNSET)

        asst_loanadvtocust_hkd = d.pop("asst_loanadvtocust_hkd", UNSET)

        asst_loanadvtocust_fc = d.pop("asst_loanadvtocust_fc", UNSET)

        asst_loanadvtocust_total = d.pop("asst_loanadvtocust_total", UNSET)

        asst_ncdepheld_hkd = d.pop("asst_ncdepheld_hkd", UNSET)

        asst_ncdepheld_fc = d.pop("asst_ncdepheld_fc", UNSET)

        asst_ncdepheld_total = d.pop("asst_ncdepheld_total", UNSET)

        asst_ncdepheld_lb_hkd = d.pop("asst_ncdepheld_lb_hkd", UNSET)

        asst_ncdepheld_lb_fc = d.pop("asst_ncdepheld_lb_fc", UNSET)

        asst_ncdepheld_lb_total = d.pop("asst_ncdepheld_lb_total", UNSET)

        asst_ncdepheld_rlb_hkd = d.pop("asst_ncdepheld_rlb_hkd", UNSET)

        asst_ncdepheld_rlb_fc = d.pop("asst_ncdepheld_rlb_fc", UNSET)

        asst_ncdepheld_rlb_total = d.pop("asst_ncdepheld_rlb_total", UNSET)

        asst_ncdepheld_dtc_hkd = d.pop("asst_ncdepheld_dtc_hkd", UNSET)

        asst_ncdepheld_dtc_fc = d.pop("asst_ncdepheld_dtc_fc", UNSET)

        asst_ncdepheld_dtc_total = d.pop("asst_ncdepheld_dtc_total", UNSET)

        asst_ncdepheld_bkouthk_hkd = d.pop("asst_ncdepheld_bkouthk_hkd", UNSET)

        asst_ncdepheld_bkouthk_fc = d.pop("asst_ncdepheld_bkouthk_fc", UNSET)

        asst_ncdepheld_bkouthk_total = d.pop("asst_ncdepheld_bkouthk_total", UNSET)

        asst_negodebt_hkd = d.pop("asst_negodebt_hkd", UNSET)

        asst_negodebt_fc = d.pop("asst_negodebt_fc", UNSET)

        asst_negodebt_total = d.pop("asst_negodebt_total", UNSET)

        asst_negodebt_accbill_hkd = d.pop("asst_negodebt_accbill_hkd", UNSET)

        asst_negodebt_accbill_fc = d.pop("asst_negodebt_accbill_fc", UNSET)

        asst_negodebt_accbill_total = d.pop("asst_negodebt_accbill_total", UNSET)

        asst_negodebt_fltnote_hkd = d.pop("asst_negodebt_fltnote_hkd", UNSET)

        asst_negodebt_fltnote_fc = d.pop("asst_negodebt_fltnote_fc", UNSET)

        asst_negodebt_fltnote_total = d.pop("asst_negodebt_fltnote_total", UNSET)

        asst_negodebt_gov_hkd = d.pop("asst_negodebt_gov_hkd", UNSET)

        asst_negodebt_gov_fc = d.pop("asst_negodebt_gov_fc", UNSET)

        asst_negodebt_gov_total = d.pop("asst_negodebt_gov_total", UNSET)

        asst_negodebt_other_hkd = d.pop("asst_negodebt_other_hkd", UNSET)

        asst_negodebt_other_fc = d.pop("asst_negodebt_other_fc", UNSET)

        asst_negodebt_other_total = d.pop("asst_negodebt_other_total", UNSET)

        asst_invinshare_hkd = d.pop("asst_invinshare_hkd", UNSET)

        asst_invinshare_fc = d.pop("asst_invinshare_fc", UNSET)

        asst_invinshare_total = d.pop("asst_invinshare_total", UNSET)

        asst_intinland_hkd = d.pop("asst_intinland_hkd", UNSET)

        asst_intinland_fc = d.pop("asst_intinland_fc", UNSET)

        asst_intinland_total = d.pop("asst_intinland_total", UNSET)

        asst_other_hkd = d.pop("asst_other_hkd", UNSET)

        asst_other_fc = d.pop("asst_other_fc", UNSET)

        asst_other_total = d.pop("asst_other_total", UNSET)

        total_asst_hkd = d.pop("total_asst_hkd", UNSET)

        total_asst_fc = d.pop("total_asst_fc", UNSET)

        total_asst_total = d.pop("total_asst_total", UNSET)

        no_of_report_instit = d.pop("no_of_report_instit", UNSET)

        no_of_local_branch = d.pop("no_of_local_branch", UNSET)

        record = cls(
            end_of_month=end_of_month,
            liab_amtaisinhk_hkd=liab_amtaisinhk_hkd,
            liab_amtaisinhk_fc=liab_amtaisinhk_fc,
            liab_amtaisinhk_total=liab_amtaisinhk_total,
            liab_amtbanksabroad_hkd=liab_amtbanksabroad_hkd,
            liab_amtbanksabroad_fc=liab_amtbanksabroad_fc,
            liab_amtbanksabroad_total=liab_amtbanksabroad_total,
            liab_depcust_hkd=liab_depcust_hkd,
            liab_depcust_fc=liab_depcust_fc,
            liab_depcust_total=liab_depcust_total,
            liab_ncdepoutst_hkd=liab_ncdepoutst_hkd,
            liab_ncdepoutst_fc=liab_ncdepoutst_fc,
            liab_ncdepoutst_total=liab_ncdepoutst_total,
            liab_othdebtinstoutst_hkd=liab_othdebtinstoutst_hkd,
            liab_othdebtinstoutst_fc=liab_othdebtinstoutst_fc,
            liab_othdebtinstoutst_total=liab_othdebtinstoutst_total,
            liab_capreserv_hkd=liab_capreserv_hkd,
            liab_capreserv_fc=liab_capreserv_fc,
            liab_capreserv_total=liab_capreserv_total,
            liab_total_hkd=liab_total_hkd,
            liab_total_fc=liab_total_fc,
            liab_total=liab_total,
            asst_notescoins_hkd=asst_notescoins_hkd,
            asst_notescoins_fc=asst_notescoins_fc,
            asst_notescoins_total=asst_notescoins_total,
            asst_amtaisinhk_hkd=asst_amtaisinhk_hkd,
            asst_amtaisinhk_fc=asst_amtaisinhk_fc,
            asst_amtaisinhk_total=asst_amtaisinhk_total,
            asst_amtbanksabroad_hkd=asst_amtbanksabroad_hkd,
            asst_amtbanksabroad_fc=asst_amtbanksabroad_fc,
            asst_amtbanksabroad_total=asst_amtbanksabroad_total,
            asst_loanadvtocust_hkd=asst_loanadvtocust_hkd,
            asst_loanadvtocust_fc=asst_loanadvtocust_fc,
            asst_loanadvtocust_total=asst_loanadvtocust_total,
            asst_ncdepheld_hkd=asst_ncdepheld_hkd,
            asst_ncdepheld_fc=asst_ncdepheld_fc,
            asst_ncdepheld_total=asst_ncdepheld_total,
            asst_ncdepheld_lb_hkd=asst_ncdepheld_lb_hkd,
            asst_ncdepheld_lb_fc=asst_ncdepheld_lb_fc,
            asst_ncdepheld_lb_total=asst_ncdepheld_lb_total,
            asst_ncdepheld_rlb_hkd=asst_ncdepheld_rlb_hkd,
            asst_ncdepheld_rlb_fc=asst_ncdepheld_rlb_fc,
            asst_ncdepheld_rlb_total=asst_ncdepheld_rlb_total,
            asst_ncdepheld_dtc_hkd=asst_ncdepheld_dtc_hkd,
            asst_ncdepheld_dtc_fc=asst_ncdepheld_dtc_fc,
            asst_ncdepheld_dtc_total=asst_ncdepheld_dtc_total,
            asst_ncdepheld_bkouthk_hkd=asst_ncdepheld_bkouthk_hkd,
            asst_ncdepheld_bkouthk_fc=asst_ncdepheld_bkouthk_fc,
            asst_ncdepheld_bkouthk_total=asst_ncdepheld_bkouthk_total,
            asst_negodebt_hkd=asst_negodebt_hkd,
            asst_negodebt_fc=asst_negodebt_fc,
            asst_negodebt_total=asst_negodebt_total,
            asst_negodebt_accbill_hkd=asst_negodebt_accbill_hkd,
            asst_negodebt_accbill_fc=asst_negodebt_accbill_fc,
            asst_negodebt_accbill_total=asst_negodebt_accbill_total,
            asst_negodebt_fltnote_hkd=asst_negodebt_fltnote_hkd,
            asst_negodebt_fltnote_fc=asst_negodebt_fltnote_fc,
            asst_negodebt_fltnote_total=asst_negodebt_fltnote_total,
            asst_negodebt_gov_hkd=asst_negodebt_gov_hkd,
            asst_negodebt_gov_fc=asst_negodebt_gov_fc,
            asst_negodebt_gov_total=asst_negodebt_gov_total,
            asst_negodebt_other_hkd=asst_negodebt_other_hkd,
            asst_negodebt_other_fc=asst_negodebt_other_fc,
            asst_negodebt_other_total=asst_negodebt_other_total,
            asst_invinshare_hkd=asst_invinshare_hkd,
            asst_invinshare_fc=asst_invinshare_fc,
            asst_invinshare_total=asst_invinshare_total,
            asst_intinland_hkd=asst_intinland_hkd,
            asst_intinland_fc=asst_intinland_fc,
            asst_intinland_total=asst_intinland_total,
            asst_other_hkd=asst_other_hkd,
            asst_other_fc=asst_other_fc,
            asst_other_total=asst_other_total,
            total_asst_hkd=total_asst_hkd,
            total_asst_fc=total_asst_fc,
            total_asst_total=total_asst_total,
            no_of_report_instit=no_of_report_instit,
            no_of_local_branch=no_of_local_branch,
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
