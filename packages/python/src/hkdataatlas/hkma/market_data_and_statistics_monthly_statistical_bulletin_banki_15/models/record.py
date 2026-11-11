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
        outstanding_loans_amt (float | Unset):
        outstanding_loans_amt_mom (float | Unset):
        outstanding_loans_amt_yoy (float | Unset):
        outstanding_loans_cofin_gf_amt (float | Unset):
        outstanding_loans_cofin_gf (float | Unset):
        outstanding_loans_cofin_ps_amt (float | Unset):
        outstanding_loans_cofin_ps (float | Unset):
        delinquency_ratio (float | Unset):
        delinquency_ratio_6mth (float | Unset):
        resch_loan_ratio (float | Unset):
        new_loans_app_received (float | Unset):
        new_loans_app_received_mom (float | Unset):
        new_loans_drawn_amt (float | Unset):
        new_loans_drawn_amt_mom (float | Unset):
        new_loans_drawn (float | Unset):
        new_loans_drawn_mom (float | Unset):
        new_loans_approved_amt (float | Unset):
        new_loans_approved_amt_mom (float | Unset):
        new_loans_approved (float | Unset):
        new_loans_approved_mom (float | Unset):
        new_loans_approved_avg_size (float | Unset):
        new_loans_approved_lv_ratio (float | Unset):
        new_loans_approved_contra_life (float | Unset):
        new_loans_approved_cofin_amt (float | Unset):
        new_loans_approved_cofin (float | Unset):
        new_loans_approved_pt_amt_pri (float | Unset):
        new_loans_approved_pt_amt_sec (float | Unset):
        new_loans_approved_pt_amt_refin (float | Unset):
        new_loans_approved_pt_primkt (float | Unset):
        new_loans_approved_pt_secmkt (float | Unset):
        new_loans_approved_pt_refin (float | Unset):
        new_loans_approved_undrawn_amt (float | Unset):
        new_loans_approved_undrawn (float | Unset):
        ir_new_loans_approved_hibor (float | Unset):
        ir_new_loans_approved_blr (float | Unset):
        ir_new_loans_approved_fixed (float | Unset):
        ir_new_loans_approved_other (float | Unset):
        loan_wo_amt (float | Unset):
        loan_wo_12mth_amt (float | Unset):
        loan_wo_12mth_pa_outstand_loans (str | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    outstanding_loans_amt: float | Unset = UNSET
    outstanding_loans_amt_mom: float | Unset = UNSET
    outstanding_loans_amt_yoy: float | Unset = UNSET
    outstanding_loans_cofin_gf_amt: float | Unset = UNSET
    outstanding_loans_cofin_gf: float | Unset = UNSET
    outstanding_loans_cofin_ps_amt: float | Unset = UNSET
    outstanding_loans_cofin_ps: float | Unset = UNSET
    delinquency_ratio: float | Unset = UNSET
    delinquency_ratio_6mth: float | Unset = UNSET
    resch_loan_ratio: float | Unset = UNSET
    new_loans_app_received: float | Unset = UNSET
    new_loans_app_received_mom: float | Unset = UNSET
    new_loans_drawn_amt: float | Unset = UNSET
    new_loans_drawn_amt_mom: float | Unset = UNSET
    new_loans_drawn: float | Unset = UNSET
    new_loans_drawn_mom: float | Unset = UNSET
    new_loans_approved_amt: float | Unset = UNSET
    new_loans_approved_amt_mom: float | Unset = UNSET
    new_loans_approved: float | Unset = UNSET
    new_loans_approved_mom: float | Unset = UNSET
    new_loans_approved_avg_size: float | Unset = UNSET
    new_loans_approved_lv_ratio: float | Unset = UNSET
    new_loans_approved_contra_life: float | Unset = UNSET
    new_loans_approved_cofin_amt: float | Unset = UNSET
    new_loans_approved_cofin: float | Unset = UNSET
    new_loans_approved_pt_amt_pri: float | Unset = UNSET
    new_loans_approved_pt_amt_sec: float | Unset = UNSET
    new_loans_approved_pt_amt_refin: float | Unset = UNSET
    new_loans_approved_pt_primkt: float | Unset = UNSET
    new_loans_approved_pt_secmkt: float | Unset = UNSET
    new_loans_approved_pt_refin: float | Unset = UNSET
    new_loans_approved_undrawn_amt: float | Unset = UNSET
    new_loans_approved_undrawn: float | Unset = UNSET
    ir_new_loans_approved_hibor: float | Unset = UNSET
    ir_new_loans_approved_blr: float | Unset = UNSET
    ir_new_loans_approved_fixed: float | Unset = UNSET
    ir_new_loans_approved_other: float | Unset = UNSET
    loan_wo_amt: float | Unset = UNSET
    loan_wo_12mth_amt: float | Unset = UNSET
    loan_wo_12mth_pa_outstand_loans: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        outstanding_loans_amt = self.outstanding_loans_amt

        outstanding_loans_amt_mom = self.outstanding_loans_amt_mom

        outstanding_loans_amt_yoy = self.outstanding_loans_amt_yoy

        outstanding_loans_cofin_gf_amt = self.outstanding_loans_cofin_gf_amt

        outstanding_loans_cofin_gf = self.outstanding_loans_cofin_gf

        outstanding_loans_cofin_ps_amt = self.outstanding_loans_cofin_ps_amt

        outstanding_loans_cofin_ps = self.outstanding_loans_cofin_ps

        delinquency_ratio = self.delinquency_ratio

        delinquency_ratio_6mth = self.delinquency_ratio_6mth

        resch_loan_ratio = self.resch_loan_ratio

        new_loans_app_received = self.new_loans_app_received

        new_loans_app_received_mom = self.new_loans_app_received_mom

        new_loans_drawn_amt = self.new_loans_drawn_amt

        new_loans_drawn_amt_mom = self.new_loans_drawn_amt_mom

        new_loans_drawn = self.new_loans_drawn

        new_loans_drawn_mom = self.new_loans_drawn_mom

        new_loans_approved_amt = self.new_loans_approved_amt

        new_loans_approved_amt_mom = self.new_loans_approved_amt_mom

        new_loans_approved = self.new_loans_approved

        new_loans_approved_mom = self.new_loans_approved_mom

        new_loans_approved_avg_size = self.new_loans_approved_avg_size

        new_loans_approved_lv_ratio = self.new_loans_approved_lv_ratio

        new_loans_approved_contra_life = self.new_loans_approved_contra_life

        new_loans_approved_cofin_amt = self.new_loans_approved_cofin_amt

        new_loans_approved_cofin = self.new_loans_approved_cofin

        new_loans_approved_pt_amt_pri = self.new_loans_approved_pt_amt_pri

        new_loans_approved_pt_amt_sec = self.new_loans_approved_pt_amt_sec

        new_loans_approved_pt_amt_refin = self.new_loans_approved_pt_amt_refin

        new_loans_approved_pt_primkt = self.new_loans_approved_pt_primkt

        new_loans_approved_pt_secmkt = self.new_loans_approved_pt_secmkt

        new_loans_approved_pt_refin = self.new_loans_approved_pt_refin

        new_loans_approved_undrawn_amt = self.new_loans_approved_undrawn_amt

        new_loans_approved_undrawn = self.new_loans_approved_undrawn

        ir_new_loans_approved_hibor = self.ir_new_loans_approved_hibor

        ir_new_loans_approved_blr = self.ir_new_loans_approved_blr

        ir_new_loans_approved_fixed = self.ir_new_loans_approved_fixed

        ir_new_loans_approved_other = self.ir_new_loans_approved_other

        loan_wo_amt = self.loan_wo_amt

        loan_wo_12mth_amt = self.loan_wo_12mth_amt

        loan_wo_12mth_pa_outstand_loans = self.loan_wo_12mth_pa_outstand_loans

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if outstanding_loans_amt is not UNSET:
            field_dict["outstanding_loans_amt"] = outstanding_loans_amt
        if outstanding_loans_amt_mom is not UNSET:
            field_dict["outstanding_loans_amt_mom"] = outstanding_loans_amt_mom
        if outstanding_loans_amt_yoy is not UNSET:
            field_dict["outstanding_loans_amt_yoy"] = outstanding_loans_amt_yoy
        if outstanding_loans_cofin_gf_amt is not UNSET:
            field_dict["outstanding_loans_cofin_gf_amt"] = (
                outstanding_loans_cofin_gf_amt
            )
        if outstanding_loans_cofin_gf is not UNSET:
            field_dict["outstanding_loans_cofin_gf"] = outstanding_loans_cofin_gf
        if outstanding_loans_cofin_ps_amt is not UNSET:
            field_dict["outstanding_loans_cofin_ps_amt"] = (
                outstanding_loans_cofin_ps_amt
            )
        if outstanding_loans_cofin_ps is not UNSET:
            field_dict["outstanding_loans_cofin_ps"] = outstanding_loans_cofin_ps
        if delinquency_ratio is not UNSET:
            field_dict["delinquency_ratio"] = delinquency_ratio
        if delinquency_ratio_6mth is not UNSET:
            field_dict["delinquency_ratio_6mth"] = delinquency_ratio_6mth
        if resch_loan_ratio is not UNSET:
            field_dict["resch_loan_ratio"] = resch_loan_ratio
        if new_loans_app_received is not UNSET:
            field_dict["new_loans_app_received"] = new_loans_app_received
        if new_loans_app_received_mom is not UNSET:
            field_dict["new_loans_app_received_mom"] = new_loans_app_received_mom
        if new_loans_drawn_amt is not UNSET:
            field_dict["new_loans_drawn_amt"] = new_loans_drawn_amt
        if new_loans_drawn_amt_mom is not UNSET:
            field_dict["new_loans_drawn_amt_mom"] = new_loans_drawn_amt_mom
        if new_loans_drawn is not UNSET:
            field_dict["new_loans_drawn"] = new_loans_drawn
        if new_loans_drawn_mom is not UNSET:
            field_dict["new_loans_drawn_mom"] = new_loans_drawn_mom
        if new_loans_approved_amt is not UNSET:
            field_dict["new_loans_approved_amt"] = new_loans_approved_amt
        if new_loans_approved_amt_mom is not UNSET:
            field_dict["new_loans_approved_amt_mom"] = new_loans_approved_amt_mom
        if new_loans_approved is not UNSET:
            field_dict["new_loans_approved"] = new_loans_approved
        if new_loans_approved_mom is not UNSET:
            field_dict["new_loans_approved_mom"] = new_loans_approved_mom
        if new_loans_approved_avg_size is not UNSET:
            field_dict["new_loans_approved_avg_size"] = new_loans_approved_avg_size
        if new_loans_approved_lv_ratio is not UNSET:
            field_dict["new_loans_approved_lv_ratio"] = new_loans_approved_lv_ratio
        if new_loans_approved_contra_life is not UNSET:
            field_dict["new_loans_approved_contra_life"] = (
                new_loans_approved_contra_life
            )
        if new_loans_approved_cofin_amt is not UNSET:
            field_dict["new_loans_approved_cofin_amt"] = new_loans_approved_cofin_amt
        if new_loans_approved_cofin is not UNSET:
            field_dict["new_loans_approved_cofin"] = new_loans_approved_cofin
        if new_loans_approved_pt_amt_pri is not UNSET:
            field_dict["new_loans_approved_pt_amt_pri"] = new_loans_approved_pt_amt_pri
        if new_loans_approved_pt_amt_sec is not UNSET:
            field_dict["new_loans_approved_pt_amt_sec"] = new_loans_approved_pt_amt_sec
        if new_loans_approved_pt_amt_refin is not UNSET:
            field_dict["new_loans_approved_pt_amt_refin"] = (
                new_loans_approved_pt_amt_refin
            )
        if new_loans_approved_pt_primkt is not UNSET:
            field_dict["new_loans_approved_pt_primkt"] = new_loans_approved_pt_primkt
        if new_loans_approved_pt_secmkt is not UNSET:
            field_dict["new_loans_approved_pt_secmkt"] = new_loans_approved_pt_secmkt
        if new_loans_approved_pt_refin is not UNSET:
            field_dict["new_loans_approved_pt_refin"] = new_loans_approved_pt_refin
        if new_loans_approved_undrawn_amt is not UNSET:
            field_dict["new_loans_approved_undrawn_amt"] = (
                new_loans_approved_undrawn_amt
            )
        if new_loans_approved_undrawn is not UNSET:
            field_dict["new_loans_approved_undrawn"] = new_loans_approved_undrawn
        if ir_new_loans_approved_hibor is not UNSET:
            field_dict["ir_new_loans_approved_hibor"] = ir_new_loans_approved_hibor
        if ir_new_loans_approved_blr is not UNSET:
            field_dict["ir_new_loans_approved_blr"] = ir_new_loans_approved_blr
        if ir_new_loans_approved_fixed is not UNSET:
            field_dict["ir_new_loans_approved_fixed"] = ir_new_loans_approved_fixed
        if ir_new_loans_approved_other is not UNSET:
            field_dict["ir_new_loans_approved_other"] = ir_new_loans_approved_other
        if loan_wo_amt is not UNSET:
            field_dict["loan_wo_amt"] = loan_wo_amt
        if loan_wo_12mth_amt is not UNSET:
            field_dict["loan_wo_12mth_amt"] = loan_wo_12mth_amt
        if loan_wo_12mth_pa_outstand_loans is not UNSET:
            field_dict["loan_wo_12mth_pa_outstand_loans"] = (
                loan_wo_12mth_pa_outstand_loans
            )

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

        outstanding_loans_amt = d.pop("outstanding_loans_amt", UNSET)

        outstanding_loans_amt_mom = d.pop("outstanding_loans_amt_mom", UNSET)

        outstanding_loans_amt_yoy = d.pop("outstanding_loans_amt_yoy", UNSET)

        outstanding_loans_cofin_gf_amt = d.pop("outstanding_loans_cofin_gf_amt", UNSET)

        outstanding_loans_cofin_gf = d.pop("outstanding_loans_cofin_gf", UNSET)

        outstanding_loans_cofin_ps_amt = d.pop("outstanding_loans_cofin_ps_amt", UNSET)

        outstanding_loans_cofin_ps = d.pop("outstanding_loans_cofin_ps", UNSET)

        delinquency_ratio = d.pop("delinquency_ratio", UNSET)

        delinquency_ratio_6mth = d.pop("delinquency_ratio_6mth", UNSET)

        resch_loan_ratio = d.pop("resch_loan_ratio", UNSET)

        new_loans_app_received = d.pop("new_loans_app_received", UNSET)

        new_loans_app_received_mom = d.pop("new_loans_app_received_mom", UNSET)

        new_loans_drawn_amt = d.pop("new_loans_drawn_amt", UNSET)

        new_loans_drawn_amt_mom = d.pop("new_loans_drawn_amt_mom", UNSET)

        new_loans_drawn = d.pop("new_loans_drawn", UNSET)

        new_loans_drawn_mom = d.pop("new_loans_drawn_mom", UNSET)

        new_loans_approved_amt = d.pop("new_loans_approved_amt", UNSET)

        new_loans_approved_amt_mom = d.pop("new_loans_approved_amt_mom", UNSET)

        new_loans_approved = d.pop("new_loans_approved", UNSET)

        new_loans_approved_mom = d.pop("new_loans_approved_mom", UNSET)

        new_loans_approved_avg_size = d.pop("new_loans_approved_avg_size", UNSET)

        new_loans_approved_lv_ratio = d.pop("new_loans_approved_lv_ratio", UNSET)

        new_loans_approved_contra_life = d.pop("new_loans_approved_contra_life", UNSET)

        new_loans_approved_cofin_amt = d.pop("new_loans_approved_cofin_amt", UNSET)

        new_loans_approved_cofin = d.pop("new_loans_approved_cofin", UNSET)

        new_loans_approved_pt_amt_pri = d.pop("new_loans_approved_pt_amt_pri", UNSET)

        new_loans_approved_pt_amt_sec = d.pop("new_loans_approved_pt_amt_sec", UNSET)

        new_loans_approved_pt_amt_refin = d.pop(
            "new_loans_approved_pt_amt_refin", UNSET
        )

        new_loans_approved_pt_primkt = d.pop("new_loans_approved_pt_primkt", UNSET)

        new_loans_approved_pt_secmkt = d.pop("new_loans_approved_pt_secmkt", UNSET)

        new_loans_approved_pt_refin = d.pop("new_loans_approved_pt_refin", UNSET)

        new_loans_approved_undrawn_amt = d.pop("new_loans_approved_undrawn_amt", UNSET)

        new_loans_approved_undrawn = d.pop("new_loans_approved_undrawn", UNSET)

        ir_new_loans_approved_hibor = d.pop("ir_new_loans_approved_hibor", UNSET)

        ir_new_loans_approved_blr = d.pop("ir_new_loans_approved_blr", UNSET)

        ir_new_loans_approved_fixed = d.pop("ir_new_loans_approved_fixed", UNSET)

        ir_new_loans_approved_other = d.pop("ir_new_loans_approved_other", UNSET)

        loan_wo_amt = d.pop("loan_wo_amt", UNSET)

        loan_wo_12mth_amt = d.pop("loan_wo_12mth_amt", UNSET)

        loan_wo_12mth_pa_outstand_loans = d.pop(
            "loan_wo_12mth_pa_outstand_loans", UNSET
        )

        record = cls(
            end_of_month=end_of_month,
            outstanding_loans_amt=outstanding_loans_amt,
            outstanding_loans_amt_mom=outstanding_loans_amt_mom,
            outstanding_loans_amt_yoy=outstanding_loans_amt_yoy,
            outstanding_loans_cofin_gf_amt=outstanding_loans_cofin_gf_amt,
            outstanding_loans_cofin_gf=outstanding_loans_cofin_gf,
            outstanding_loans_cofin_ps_amt=outstanding_loans_cofin_ps_amt,
            outstanding_loans_cofin_ps=outstanding_loans_cofin_ps,
            delinquency_ratio=delinquency_ratio,
            delinquency_ratio_6mth=delinquency_ratio_6mth,
            resch_loan_ratio=resch_loan_ratio,
            new_loans_app_received=new_loans_app_received,
            new_loans_app_received_mom=new_loans_app_received_mom,
            new_loans_drawn_amt=new_loans_drawn_amt,
            new_loans_drawn_amt_mom=new_loans_drawn_amt_mom,
            new_loans_drawn=new_loans_drawn,
            new_loans_drawn_mom=new_loans_drawn_mom,
            new_loans_approved_amt=new_loans_approved_amt,
            new_loans_approved_amt_mom=new_loans_approved_amt_mom,
            new_loans_approved=new_loans_approved,
            new_loans_approved_mom=new_loans_approved_mom,
            new_loans_approved_avg_size=new_loans_approved_avg_size,
            new_loans_approved_lv_ratio=new_loans_approved_lv_ratio,
            new_loans_approved_contra_life=new_loans_approved_contra_life,
            new_loans_approved_cofin_amt=new_loans_approved_cofin_amt,
            new_loans_approved_cofin=new_loans_approved_cofin,
            new_loans_approved_pt_amt_pri=new_loans_approved_pt_amt_pri,
            new_loans_approved_pt_amt_sec=new_loans_approved_pt_amt_sec,
            new_loans_approved_pt_amt_refin=new_loans_approved_pt_amt_refin,
            new_loans_approved_pt_primkt=new_loans_approved_pt_primkt,
            new_loans_approved_pt_secmkt=new_loans_approved_pt_secmkt,
            new_loans_approved_pt_refin=new_loans_approved_pt_refin,
            new_loans_approved_undrawn_amt=new_loans_approved_undrawn_amt,
            new_loans_approved_undrawn=new_loans_approved_undrawn,
            ir_new_loans_approved_hibor=ir_new_loans_approved_hibor,
            ir_new_loans_approved_blr=ir_new_loans_approved_blr,
            ir_new_loans_approved_fixed=ir_new_loans_approved_fixed,
            ir_new_loans_approved_other=ir_new_loans_approved_other,
            loan_wo_amt=loan_wo_amt,
            loan_wo_12mth_amt=loan_wo_12mth_amt,
            loan_wo_12mth_pa_outstand_loans=loan_wo_12mth_pa_outstand_loans,
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
