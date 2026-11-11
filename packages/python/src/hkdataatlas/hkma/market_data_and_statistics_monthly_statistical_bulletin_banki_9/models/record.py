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
        mfg (float | Unset):
        mfg_chg (float | Unset):
        mfg_textiles (float | Unset):
        mfg_textiles_chg (float | Unset):
        mfg_footwear (float | Unset):
        mfg_footwear_chg (float | Unset):
        mfg_metalengr (float | Unset):
        mfg_metalengr_chg (float | Unset):
        mfg_rubbplastchem (float | Unset):
        mfg_rubbplastchem_chg (float | Unset):
        mfg_shipbuildrepair (float | Unset):
        mfg_shipbuildrepair_chg (float | Unset):
        mfg_ee (float | Unset):
        mfg_ee_chg (float | Unset):
        mfg_ee_teleequip (float | Unset):
        mfg_ee_teleequip_chg (float | Unset):
        mfg_ee_other (float | Unset):
        mfg_ee_other_chg (float | Unset):
        mfg_food (float | Unset):
        mfg_food_chg (float | Unset):
        mfg_bevtob (float | Unset):
        mfg_bevtob_chg (float | Unset):
        mfg_printpub (float | Unset):
        mfg_printpub_chg (float | Unset):
        mfg_misc (float | Unset):
        mfg_misc_chg (float | Unset):
        af (float | Unset):
        af_chg (float | Unset):
        af_fisheries (float | Unset):
        af_fisheries_chg (float | Unset):
        af_livestock (float | Unset):
        af_livestock_chg (float | Unset):
        af_veghort (float | Unset):
        af_veghort_chg (float | Unset):
        tran (float | Unset):
        tran_chg (float | Unset):
        tran_shipping (float | Unset):
        tran_shipping_chg (float | Unset):
        tran_airtran (float | Unset):
        tran_airtran_chg (float | Unset):
        tran_taxisplb (float | Unset):
        tran_taxisplb_chg (float | Unset):
        tran_taxisplb_taxis (float | Unset):
        tran_taxisplb_taxis_chg (float | Unset):
        tran_taxisplb_plb (float | Unset):
        tran_taxisplb_plb_chg (float | Unset):
        tran_other (float | Unset):
        tran_other_chg (float | Unset):
        egt (float | Unset):
        egt_chg (float | Unset):
        eg (float | Unset):
        eg_chg (float | Unset):
        rec (float | Unset):
        rec_chg (float | Unset):
        it (float | Unset):
        it_chg (float | Unset):
        it_telecom (float | Unset):
        it_telecom_chg (float | Unset):
        it_other (float | Unset):
        it_other_chg (float | Unset):
        bcpi (float | Unset):
        bcpi_chg (float | Unset):
        bcpi_propdev (float | Unset):
        bcpi_propdev_chg (float | Unset):
        bcpi_propdev_ind (float | Unset):
        bcpi_propdev_ind_chg (float | Unset):
        bcpi_propdev_res (float | Unset):
        bcpi_propdev_res_chg (float | Unset):
        bcpi_propdev_comm (float | Unset):
        bcpi_propdev_comm_chg (float | Unset):
        bcpi_propdev_other (float | Unset):
        bcpi_propdev_other_chg (float | Unset):
        bcpi_other (float | Unset):
        bcpi_other_chg (float | Unset):
        wsale (float | Unset):
        wsale_chg (float | Unset):
        mine (float | Unset):
        mine_chg (float | Unset):
        misc (float | Unset):
        misc_chg (float | Unset):
        misc_hotelcater (float | Unset):
        misc_hotelcater_chg (float | Unset):
        misc_fin (float | Unset):
        misc_fin_chg (float | Unset):
        misc_fin_inv (float | Unset):
        misc_fin_inv_chg (float | Unset):
        misc_fin_ins (float | Unset):
        misc_fin_ins_chg (float | Unset):
        misc_fin_futbrok (float | Unset):
        misc_fin_futbrok_chg (float | Unset):
        misc_fin_finother (float | Unset):
        misc_fin_finother_chg (float | Unset):
        misc_stockbrok (float | Unset):
        misc_stockbrok_chg (float | Unset):
        misc_prof (float | Unset):
        misc_prof_chg (float | Unset):
        misc_prof_purschflat (float | Unset):
        misc_prof_purschflat_chg (float | Unset):
        misc_prof_purother (float | Unset):
        misc_prof_purother_chg (float | Unset):
        misc_prof_ccadv (float | Unset):
        misc_prof_ccadv_chg (float | Unset):
        misc_prof_otherbusi (float | Unset):
        misc_prof_otherbusi_chg (float | Unset):
        misc_prof_otherpvt (float | Unset):
        misc_prof_otherpvt_chg (float | Unset):
        misc_allother (float | Unset):
        misc_allother_chg (float | Unset):
        loan_inhk (float | Unset):
        loan_inhk_chg (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    mfg: float | Unset = UNSET
    mfg_chg: float | Unset = UNSET
    mfg_textiles: float | Unset = UNSET
    mfg_textiles_chg: float | Unset = UNSET
    mfg_footwear: float | Unset = UNSET
    mfg_footwear_chg: float | Unset = UNSET
    mfg_metalengr: float | Unset = UNSET
    mfg_metalengr_chg: float | Unset = UNSET
    mfg_rubbplastchem: float | Unset = UNSET
    mfg_rubbplastchem_chg: float | Unset = UNSET
    mfg_shipbuildrepair: float | Unset = UNSET
    mfg_shipbuildrepair_chg: float | Unset = UNSET
    mfg_ee: float | Unset = UNSET
    mfg_ee_chg: float | Unset = UNSET
    mfg_ee_teleequip: float | Unset = UNSET
    mfg_ee_teleequip_chg: float | Unset = UNSET
    mfg_ee_other: float | Unset = UNSET
    mfg_ee_other_chg: float | Unset = UNSET
    mfg_food: float | Unset = UNSET
    mfg_food_chg: float | Unset = UNSET
    mfg_bevtob: float | Unset = UNSET
    mfg_bevtob_chg: float | Unset = UNSET
    mfg_printpub: float | Unset = UNSET
    mfg_printpub_chg: float | Unset = UNSET
    mfg_misc: float | Unset = UNSET
    mfg_misc_chg: float | Unset = UNSET
    af: float | Unset = UNSET
    af_chg: float | Unset = UNSET
    af_fisheries: float | Unset = UNSET
    af_fisheries_chg: float | Unset = UNSET
    af_livestock: float | Unset = UNSET
    af_livestock_chg: float | Unset = UNSET
    af_veghort: float | Unset = UNSET
    af_veghort_chg: float | Unset = UNSET
    tran: float | Unset = UNSET
    tran_chg: float | Unset = UNSET
    tran_shipping: float | Unset = UNSET
    tran_shipping_chg: float | Unset = UNSET
    tran_airtran: float | Unset = UNSET
    tran_airtran_chg: float | Unset = UNSET
    tran_taxisplb: float | Unset = UNSET
    tran_taxisplb_chg: float | Unset = UNSET
    tran_taxisplb_taxis: float | Unset = UNSET
    tran_taxisplb_taxis_chg: float | Unset = UNSET
    tran_taxisplb_plb: float | Unset = UNSET
    tran_taxisplb_plb_chg: float | Unset = UNSET
    tran_other: float | Unset = UNSET
    tran_other_chg: float | Unset = UNSET
    egt: float | Unset = UNSET
    egt_chg: float | Unset = UNSET
    eg: float | Unset = UNSET
    eg_chg: float | Unset = UNSET
    rec: float | Unset = UNSET
    rec_chg: float | Unset = UNSET
    it: float | Unset = UNSET
    it_chg: float | Unset = UNSET
    it_telecom: float | Unset = UNSET
    it_telecom_chg: float | Unset = UNSET
    it_other: float | Unset = UNSET
    it_other_chg: float | Unset = UNSET
    bcpi: float | Unset = UNSET
    bcpi_chg: float | Unset = UNSET
    bcpi_propdev: float | Unset = UNSET
    bcpi_propdev_chg: float | Unset = UNSET
    bcpi_propdev_ind: float | Unset = UNSET
    bcpi_propdev_ind_chg: float | Unset = UNSET
    bcpi_propdev_res: float | Unset = UNSET
    bcpi_propdev_res_chg: float | Unset = UNSET
    bcpi_propdev_comm: float | Unset = UNSET
    bcpi_propdev_comm_chg: float | Unset = UNSET
    bcpi_propdev_other: float | Unset = UNSET
    bcpi_propdev_other_chg: float | Unset = UNSET
    bcpi_other: float | Unset = UNSET
    bcpi_other_chg: float | Unset = UNSET
    wsale: float | Unset = UNSET
    wsale_chg: float | Unset = UNSET
    mine: float | Unset = UNSET
    mine_chg: float | Unset = UNSET
    misc: float | Unset = UNSET
    misc_chg: float | Unset = UNSET
    misc_hotelcater: float | Unset = UNSET
    misc_hotelcater_chg: float | Unset = UNSET
    misc_fin: float | Unset = UNSET
    misc_fin_chg: float | Unset = UNSET
    misc_fin_inv: float | Unset = UNSET
    misc_fin_inv_chg: float | Unset = UNSET
    misc_fin_ins: float | Unset = UNSET
    misc_fin_ins_chg: float | Unset = UNSET
    misc_fin_futbrok: float | Unset = UNSET
    misc_fin_futbrok_chg: float | Unset = UNSET
    misc_fin_finother: float | Unset = UNSET
    misc_fin_finother_chg: float | Unset = UNSET
    misc_stockbrok: float | Unset = UNSET
    misc_stockbrok_chg: float | Unset = UNSET
    misc_prof: float | Unset = UNSET
    misc_prof_chg: float | Unset = UNSET
    misc_prof_purschflat: float | Unset = UNSET
    misc_prof_purschflat_chg: float | Unset = UNSET
    misc_prof_purother: float | Unset = UNSET
    misc_prof_purother_chg: float | Unset = UNSET
    misc_prof_ccadv: float | Unset = UNSET
    misc_prof_ccadv_chg: float | Unset = UNSET
    misc_prof_otherbusi: float | Unset = UNSET
    misc_prof_otherbusi_chg: float | Unset = UNSET
    misc_prof_otherpvt: float | Unset = UNSET
    misc_prof_otherpvt_chg: float | Unset = UNSET
    misc_allother: float | Unset = UNSET
    misc_allother_chg: float | Unset = UNSET
    loan_inhk: float | Unset = UNSET
    loan_inhk_chg: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        mfg = self.mfg

        mfg_chg = self.mfg_chg

        mfg_textiles = self.mfg_textiles

        mfg_textiles_chg = self.mfg_textiles_chg

        mfg_footwear = self.mfg_footwear

        mfg_footwear_chg = self.mfg_footwear_chg

        mfg_metalengr = self.mfg_metalengr

        mfg_metalengr_chg = self.mfg_metalengr_chg

        mfg_rubbplastchem = self.mfg_rubbplastchem

        mfg_rubbplastchem_chg = self.mfg_rubbplastchem_chg

        mfg_shipbuildrepair = self.mfg_shipbuildrepair

        mfg_shipbuildrepair_chg = self.mfg_shipbuildrepair_chg

        mfg_ee = self.mfg_ee

        mfg_ee_chg = self.mfg_ee_chg

        mfg_ee_teleequip = self.mfg_ee_teleequip

        mfg_ee_teleequip_chg = self.mfg_ee_teleequip_chg

        mfg_ee_other = self.mfg_ee_other

        mfg_ee_other_chg = self.mfg_ee_other_chg

        mfg_food = self.mfg_food

        mfg_food_chg = self.mfg_food_chg

        mfg_bevtob = self.mfg_bevtob

        mfg_bevtob_chg = self.mfg_bevtob_chg

        mfg_printpub = self.mfg_printpub

        mfg_printpub_chg = self.mfg_printpub_chg

        mfg_misc = self.mfg_misc

        mfg_misc_chg = self.mfg_misc_chg

        af = self.af

        af_chg = self.af_chg

        af_fisheries = self.af_fisheries

        af_fisheries_chg = self.af_fisheries_chg

        af_livestock = self.af_livestock

        af_livestock_chg = self.af_livestock_chg

        af_veghort = self.af_veghort

        af_veghort_chg = self.af_veghort_chg

        tran = self.tran

        tran_chg = self.tran_chg

        tran_shipping = self.tran_shipping

        tran_shipping_chg = self.tran_shipping_chg

        tran_airtran = self.tran_airtran

        tran_airtran_chg = self.tran_airtran_chg

        tran_taxisplb = self.tran_taxisplb

        tran_taxisplb_chg = self.tran_taxisplb_chg

        tran_taxisplb_taxis = self.tran_taxisplb_taxis

        tran_taxisplb_taxis_chg = self.tran_taxisplb_taxis_chg

        tran_taxisplb_plb = self.tran_taxisplb_plb

        tran_taxisplb_plb_chg = self.tran_taxisplb_plb_chg

        tran_other = self.tran_other

        tran_other_chg = self.tran_other_chg

        egt = self.egt

        egt_chg = self.egt_chg

        eg = self.eg

        eg_chg = self.eg_chg

        rec = self.rec

        rec_chg = self.rec_chg

        it = self.it

        it_chg = self.it_chg

        it_telecom = self.it_telecom

        it_telecom_chg = self.it_telecom_chg

        it_other = self.it_other

        it_other_chg = self.it_other_chg

        bcpi = self.bcpi

        bcpi_chg = self.bcpi_chg

        bcpi_propdev = self.bcpi_propdev

        bcpi_propdev_chg = self.bcpi_propdev_chg

        bcpi_propdev_ind = self.bcpi_propdev_ind

        bcpi_propdev_ind_chg = self.bcpi_propdev_ind_chg

        bcpi_propdev_res = self.bcpi_propdev_res

        bcpi_propdev_res_chg = self.bcpi_propdev_res_chg

        bcpi_propdev_comm = self.bcpi_propdev_comm

        bcpi_propdev_comm_chg = self.bcpi_propdev_comm_chg

        bcpi_propdev_other = self.bcpi_propdev_other

        bcpi_propdev_other_chg = self.bcpi_propdev_other_chg

        bcpi_other = self.bcpi_other

        bcpi_other_chg = self.bcpi_other_chg

        wsale = self.wsale

        wsale_chg = self.wsale_chg

        mine = self.mine

        mine_chg = self.mine_chg

        misc = self.misc

        misc_chg = self.misc_chg

        misc_hotelcater = self.misc_hotelcater

        misc_hotelcater_chg = self.misc_hotelcater_chg

        misc_fin = self.misc_fin

        misc_fin_chg = self.misc_fin_chg

        misc_fin_inv = self.misc_fin_inv

        misc_fin_inv_chg = self.misc_fin_inv_chg

        misc_fin_ins = self.misc_fin_ins

        misc_fin_ins_chg = self.misc_fin_ins_chg

        misc_fin_futbrok = self.misc_fin_futbrok

        misc_fin_futbrok_chg = self.misc_fin_futbrok_chg

        misc_fin_finother = self.misc_fin_finother

        misc_fin_finother_chg = self.misc_fin_finother_chg

        misc_stockbrok = self.misc_stockbrok

        misc_stockbrok_chg = self.misc_stockbrok_chg

        misc_prof = self.misc_prof

        misc_prof_chg = self.misc_prof_chg

        misc_prof_purschflat = self.misc_prof_purschflat

        misc_prof_purschflat_chg = self.misc_prof_purschflat_chg

        misc_prof_purother = self.misc_prof_purother

        misc_prof_purother_chg = self.misc_prof_purother_chg

        misc_prof_ccadv = self.misc_prof_ccadv

        misc_prof_ccadv_chg = self.misc_prof_ccadv_chg

        misc_prof_otherbusi = self.misc_prof_otherbusi

        misc_prof_otherbusi_chg = self.misc_prof_otherbusi_chg

        misc_prof_otherpvt = self.misc_prof_otherpvt

        misc_prof_otherpvt_chg = self.misc_prof_otherpvt_chg

        misc_allother = self.misc_allother

        misc_allother_chg = self.misc_allother_chg

        loan_inhk = self.loan_inhk

        loan_inhk_chg = self.loan_inhk_chg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if mfg is not UNSET:
            field_dict["mfg"] = mfg
        if mfg_chg is not UNSET:
            field_dict["mfg_chg"] = mfg_chg
        if mfg_textiles is not UNSET:
            field_dict["mfg_textiles"] = mfg_textiles
        if mfg_textiles_chg is not UNSET:
            field_dict["mfg_textiles_chg"] = mfg_textiles_chg
        if mfg_footwear is not UNSET:
            field_dict["mfg_footwear"] = mfg_footwear
        if mfg_footwear_chg is not UNSET:
            field_dict["mfg_footwear_chg"] = mfg_footwear_chg
        if mfg_metalengr is not UNSET:
            field_dict["mfg_metalengr"] = mfg_metalengr
        if mfg_metalengr_chg is not UNSET:
            field_dict["mfg_metalengr_chg"] = mfg_metalengr_chg
        if mfg_rubbplastchem is not UNSET:
            field_dict["mfg_rubbplastchem"] = mfg_rubbplastchem
        if mfg_rubbplastchem_chg is not UNSET:
            field_dict["mfg_rubbplastchem_chg"] = mfg_rubbplastchem_chg
        if mfg_shipbuildrepair is not UNSET:
            field_dict["mfg_shipbuildrepair"] = mfg_shipbuildrepair
        if mfg_shipbuildrepair_chg is not UNSET:
            field_dict["mfg_shipbuildrepair_chg"] = mfg_shipbuildrepair_chg
        if mfg_ee is not UNSET:
            field_dict["mfg_ee"] = mfg_ee
        if mfg_ee_chg is not UNSET:
            field_dict["mfg_ee_chg"] = mfg_ee_chg
        if mfg_ee_teleequip is not UNSET:
            field_dict["mfg_ee_teleequip"] = mfg_ee_teleequip
        if mfg_ee_teleequip_chg is not UNSET:
            field_dict["mfg_ee_teleequip_chg"] = mfg_ee_teleequip_chg
        if mfg_ee_other is not UNSET:
            field_dict["mfg_ee_other"] = mfg_ee_other
        if mfg_ee_other_chg is not UNSET:
            field_dict["mfg_ee_other_chg"] = mfg_ee_other_chg
        if mfg_food is not UNSET:
            field_dict["mfg_food"] = mfg_food
        if mfg_food_chg is not UNSET:
            field_dict["mfg_food_chg"] = mfg_food_chg
        if mfg_bevtob is not UNSET:
            field_dict["mfg_bevtob"] = mfg_bevtob
        if mfg_bevtob_chg is not UNSET:
            field_dict["mfg_bevtob_chg"] = mfg_bevtob_chg
        if mfg_printpub is not UNSET:
            field_dict["mfg_printpub"] = mfg_printpub
        if mfg_printpub_chg is not UNSET:
            field_dict["mfg_printpub_chg"] = mfg_printpub_chg
        if mfg_misc is not UNSET:
            field_dict["mfg_misc"] = mfg_misc
        if mfg_misc_chg is not UNSET:
            field_dict["mfg_misc_chg"] = mfg_misc_chg
        if af is not UNSET:
            field_dict["af"] = af
        if af_chg is not UNSET:
            field_dict["af_chg"] = af_chg
        if af_fisheries is not UNSET:
            field_dict["af_fisheries"] = af_fisheries
        if af_fisheries_chg is not UNSET:
            field_dict["af_fisheries_chg"] = af_fisheries_chg
        if af_livestock is not UNSET:
            field_dict["af_livestock"] = af_livestock
        if af_livestock_chg is not UNSET:
            field_dict["af_livestock_chg"] = af_livestock_chg
        if af_veghort is not UNSET:
            field_dict["af_veghort"] = af_veghort
        if af_veghort_chg is not UNSET:
            field_dict["af_veghort_chg"] = af_veghort_chg
        if tran is not UNSET:
            field_dict["tran"] = tran
        if tran_chg is not UNSET:
            field_dict["tran_chg"] = tran_chg
        if tran_shipping is not UNSET:
            field_dict["tran_shipping"] = tran_shipping
        if tran_shipping_chg is not UNSET:
            field_dict["tran_shipping_chg"] = tran_shipping_chg
        if tran_airtran is not UNSET:
            field_dict["tran_airtran"] = tran_airtran
        if tran_airtran_chg is not UNSET:
            field_dict["tran_airtran_chg"] = tran_airtran_chg
        if tran_taxisplb is not UNSET:
            field_dict["tran_taxisplb"] = tran_taxisplb
        if tran_taxisplb_chg is not UNSET:
            field_dict["tran_taxisplb_chg"] = tran_taxisplb_chg
        if tran_taxisplb_taxis is not UNSET:
            field_dict["tran_taxisplb_taxis"] = tran_taxisplb_taxis
        if tran_taxisplb_taxis_chg is not UNSET:
            field_dict["tran_taxisplb_taxis_chg"] = tran_taxisplb_taxis_chg
        if tran_taxisplb_plb is not UNSET:
            field_dict["tran_taxisplb_plb"] = tran_taxisplb_plb
        if tran_taxisplb_plb_chg is not UNSET:
            field_dict["tran_taxisplb_plb_chg"] = tran_taxisplb_plb_chg
        if tran_other is not UNSET:
            field_dict["tran_other"] = tran_other
        if tran_other_chg is not UNSET:
            field_dict["tran_other_chg"] = tran_other_chg
        if egt is not UNSET:
            field_dict["egt"] = egt
        if egt_chg is not UNSET:
            field_dict["egt_chg"] = egt_chg
        if eg is not UNSET:
            field_dict["eg"] = eg
        if eg_chg is not UNSET:
            field_dict["eg_chg"] = eg_chg
        if rec is not UNSET:
            field_dict["rec"] = rec
        if rec_chg is not UNSET:
            field_dict["rec_chg"] = rec_chg
        if it is not UNSET:
            field_dict["it"] = it
        if it_chg is not UNSET:
            field_dict["it_chg"] = it_chg
        if it_telecom is not UNSET:
            field_dict["it_telecom"] = it_telecom
        if it_telecom_chg is not UNSET:
            field_dict["it_telecom_chg"] = it_telecom_chg
        if it_other is not UNSET:
            field_dict["it_other"] = it_other
        if it_other_chg is not UNSET:
            field_dict["it_other_chg"] = it_other_chg
        if bcpi is not UNSET:
            field_dict["bcpi"] = bcpi
        if bcpi_chg is not UNSET:
            field_dict["bcpi_chg"] = bcpi_chg
        if bcpi_propdev is not UNSET:
            field_dict["bcpi_propdev"] = bcpi_propdev
        if bcpi_propdev_chg is not UNSET:
            field_dict["bcpi_propdev_chg"] = bcpi_propdev_chg
        if bcpi_propdev_ind is not UNSET:
            field_dict["bcpi_propdev_ind"] = bcpi_propdev_ind
        if bcpi_propdev_ind_chg is not UNSET:
            field_dict["bcpi_propdev_ind_chg"] = bcpi_propdev_ind_chg
        if bcpi_propdev_res is not UNSET:
            field_dict["bcpi_propdev_res"] = bcpi_propdev_res
        if bcpi_propdev_res_chg is not UNSET:
            field_dict["bcpi_propdev_res_chg"] = bcpi_propdev_res_chg
        if bcpi_propdev_comm is not UNSET:
            field_dict["bcpi_propdev_comm"] = bcpi_propdev_comm
        if bcpi_propdev_comm_chg is not UNSET:
            field_dict["bcpi_propdev_comm_chg"] = bcpi_propdev_comm_chg
        if bcpi_propdev_other is not UNSET:
            field_dict["bcpi_propdev_other"] = bcpi_propdev_other
        if bcpi_propdev_other_chg is not UNSET:
            field_dict["bcpi_propdev_other_chg"] = bcpi_propdev_other_chg
        if bcpi_other is not UNSET:
            field_dict["bcpi_other"] = bcpi_other
        if bcpi_other_chg is not UNSET:
            field_dict["bcpi_other_chg"] = bcpi_other_chg
        if wsale is not UNSET:
            field_dict["wsale"] = wsale
        if wsale_chg is not UNSET:
            field_dict["wsale_chg"] = wsale_chg
        if mine is not UNSET:
            field_dict["mine"] = mine
        if mine_chg is not UNSET:
            field_dict["mine_chg"] = mine_chg
        if misc is not UNSET:
            field_dict["misc"] = misc
        if misc_chg is not UNSET:
            field_dict["misc_chg"] = misc_chg
        if misc_hotelcater is not UNSET:
            field_dict["misc_hotelcater"] = misc_hotelcater
        if misc_hotelcater_chg is not UNSET:
            field_dict["misc_hotelcater_chg"] = misc_hotelcater_chg
        if misc_fin is not UNSET:
            field_dict["misc_fin"] = misc_fin
        if misc_fin_chg is not UNSET:
            field_dict["misc_fin_chg"] = misc_fin_chg
        if misc_fin_inv is not UNSET:
            field_dict["misc_fin_inv"] = misc_fin_inv
        if misc_fin_inv_chg is not UNSET:
            field_dict["misc_fin_inv_chg"] = misc_fin_inv_chg
        if misc_fin_ins is not UNSET:
            field_dict["misc_fin_ins"] = misc_fin_ins
        if misc_fin_ins_chg is not UNSET:
            field_dict["misc_fin_ins_chg"] = misc_fin_ins_chg
        if misc_fin_futbrok is not UNSET:
            field_dict["misc_fin_futbrok"] = misc_fin_futbrok
        if misc_fin_futbrok_chg is not UNSET:
            field_dict["misc_fin_futbrok_chg"] = misc_fin_futbrok_chg
        if misc_fin_finother is not UNSET:
            field_dict["misc_fin_finother"] = misc_fin_finother
        if misc_fin_finother_chg is not UNSET:
            field_dict["misc_fin_finother_chg"] = misc_fin_finother_chg
        if misc_stockbrok is not UNSET:
            field_dict["misc_stockbrok"] = misc_stockbrok
        if misc_stockbrok_chg is not UNSET:
            field_dict["misc_stockbrok_chg"] = misc_stockbrok_chg
        if misc_prof is not UNSET:
            field_dict["misc_prof"] = misc_prof
        if misc_prof_chg is not UNSET:
            field_dict["misc_prof_chg"] = misc_prof_chg
        if misc_prof_purschflat is not UNSET:
            field_dict["misc_prof_purschflat"] = misc_prof_purschflat
        if misc_prof_purschflat_chg is not UNSET:
            field_dict["misc_prof_purschflat_chg"] = misc_prof_purschflat_chg
        if misc_prof_purother is not UNSET:
            field_dict["misc_prof_purother"] = misc_prof_purother
        if misc_prof_purother_chg is not UNSET:
            field_dict["misc_prof_purother_chg"] = misc_prof_purother_chg
        if misc_prof_ccadv is not UNSET:
            field_dict["misc_prof_ccadv"] = misc_prof_ccadv
        if misc_prof_ccadv_chg is not UNSET:
            field_dict["misc_prof_ccadv_chg"] = misc_prof_ccadv_chg
        if misc_prof_otherbusi is not UNSET:
            field_dict["misc_prof_otherbusi"] = misc_prof_otherbusi
        if misc_prof_otherbusi_chg is not UNSET:
            field_dict["misc_prof_otherbusi_chg"] = misc_prof_otherbusi_chg
        if misc_prof_otherpvt is not UNSET:
            field_dict["misc_prof_otherpvt"] = misc_prof_otherpvt
        if misc_prof_otherpvt_chg is not UNSET:
            field_dict["misc_prof_otherpvt_chg"] = misc_prof_otherpvt_chg
        if misc_allother is not UNSET:
            field_dict["misc_allother"] = misc_allother
        if misc_allother_chg is not UNSET:
            field_dict["misc_allother_chg"] = misc_allother_chg
        if loan_inhk is not UNSET:
            field_dict["loan_inhk"] = loan_inhk
        if loan_inhk_chg is not UNSET:
            field_dict["loan_inhk_chg"] = loan_inhk_chg

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

        mfg = d.pop("mfg", UNSET)

        mfg_chg = d.pop("mfg_chg", UNSET)

        mfg_textiles = d.pop("mfg_textiles", UNSET)

        mfg_textiles_chg = d.pop("mfg_textiles_chg", UNSET)

        mfg_footwear = d.pop("mfg_footwear", UNSET)

        mfg_footwear_chg = d.pop("mfg_footwear_chg", UNSET)

        mfg_metalengr = d.pop("mfg_metalengr", UNSET)

        mfg_metalengr_chg = d.pop("mfg_metalengr_chg", UNSET)

        mfg_rubbplastchem = d.pop("mfg_rubbplastchem", UNSET)

        mfg_rubbplastchem_chg = d.pop("mfg_rubbplastchem_chg", UNSET)

        mfg_shipbuildrepair = d.pop("mfg_shipbuildrepair", UNSET)

        mfg_shipbuildrepair_chg = d.pop("mfg_shipbuildrepair_chg", UNSET)

        mfg_ee = d.pop("mfg_ee", UNSET)

        mfg_ee_chg = d.pop("mfg_ee_chg", UNSET)

        mfg_ee_teleequip = d.pop("mfg_ee_teleequip", UNSET)

        mfg_ee_teleequip_chg = d.pop("mfg_ee_teleequip_chg", UNSET)

        mfg_ee_other = d.pop("mfg_ee_other", UNSET)

        mfg_ee_other_chg = d.pop("mfg_ee_other_chg", UNSET)

        mfg_food = d.pop("mfg_food", UNSET)

        mfg_food_chg = d.pop("mfg_food_chg", UNSET)

        mfg_bevtob = d.pop("mfg_bevtob", UNSET)

        mfg_bevtob_chg = d.pop("mfg_bevtob_chg", UNSET)

        mfg_printpub = d.pop("mfg_printpub", UNSET)

        mfg_printpub_chg = d.pop("mfg_printpub_chg", UNSET)

        mfg_misc = d.pop("mfg_misc", UNSET)

        mfg_misc_chg = d.pop("mfg_misc_chg", UNSET)

        af = d.pop("af", UNSET)

        af_chg = d.pop("af_chg", UNSET)

        af_fisheries = d.pop("af_fisheries", UNSET)

        af_fisheries_chg = d.pop("af_fisheries_chg", UNSET)

        af_livestock = d.pop("af_livestock", UNSET)

        af_livestock_chg = d.pop("af_livestock_chg", UNSET)

        af_veghort = d.pop("af_veghort", UNSET)

        af_veghort_chg = d.pop("af_veghort_chg", UNSET)

        tran = d.pop("tran", UNSET)

        tran_chg = d.pop("tran_chg", UNSET)

        tran_shipping = d.pop("tran_shipping", UNSET)

        tran_shipping_chg = d.pop("tran_shipping_chg", UNSET)

        tran_airtran = d.pop("tran_airtran", UNSET)

        tran_airtran_chg = d.pop("tran_airtran_chg", UNSET)

        tran_taxisplb = d.pop("tran_taxisplb", UNSET)

        tran_taxisplb_chg = d.pop("tran_taxisplb_chg", UNSET)

        tran_taxisplb_taxis = d.pop("tran_taxisplb_taxis", UNSET)

        tran_taxisplb_taxis_chg = d.pop("tran_taxisplb_taxis_chg", UNSET)

        tran_taxisplb_plb = d.pop("tran_taxisplb_plb", UNSET)

        tran_taxisplb_plb_chg = d.pop("tran_taxisplb_plb_chg", UNSET)

        tran_other = d.pop("tran_other", UNSET)

        tran_other_chg = d.pop("tran_other_chg", UNSET)

        egt = d.pop("egt", UNSET)

        egt_chg = d.pop("egt_chg", UNSET)

        eg = d.pop("eg", UNSET)

        eg_chg = d.pop("eg_chg", UNSET)

        rec = d.pop("rec", UNSET)

        rec_chg = d.pop("rec_chg", UNSET)

        it = d.pop("it", UNSET)

        it_chg = d.pop("it_chg", UNSET)

        it_telecom = d.pop("it_telecom", UNSET)

        it_telecom_chg = d.pop("it_telecom_chg", UNSET)

        it_other = d.pop("it_other", UNSET)

        it_other_chg = d.pop("it_other_chg", UNSET)

        bcpi = d.pop("bcpi", UNSET)

        bcpi_chg = d.pop("bcpi_chg", UNSET)

        bcpi_propdev = d.pop("bcpi_propdev", UNSET)

        bcpi_propdev_chg = d.pop("bcpi_propdev_chg", UNSET)

        bcpi_propdev_ind = d.pop("bcpi_propdev_ind", UNSET)

        bcpi_propdev_ind_chg = d.pop("bcpi_propdev_ind_chg", UNSET)

        bcpi_propdev_res = d.pop("bcpi_propdev_res", UNSET)

        bcpi_propdev_res_chg = d.pop("bcpi_propdev_res_chg", UNSET)

        bcpi_propdev_comm = d.pop("bcpi_propdev_comm", UNSET)

        bcpi_propdev_comm_chg = d.pop("bcpi_propdev_comm_chg", UNSET)

        bcpi_propdev_other = d.pop("bcpi_propdev_other", UNSET)

        bcpi_propdev_other_chg = d.pop("bcpi_propdev_other_chg", UNSET)

        bcpi_other = d.pop("bcpi_other", UNSET)

        bcpi_other_chg = d.pop("bcpi_other_chg", UNSET)

        wsale = d.pop("wsale", UNSET)

        wsale_chg = d.pop("wsale_chg", UNSET)

        mine = d.pop("mine", UNSET)

        mine_chg = d.pop("mine_chg", UNSET)

        misc = d.pop("misc", UNSET)

        misc_chg = d.pop("misc_chg", UNSET)

        misc_hotelcater = d.pop("misc_hotelcater", UNSET)

        misc_hotelcater_chg = d.pop("misc_hotelcater_chg", UNSET)

        misc_fin = d.pop("misc_fin", UNSET)

        misc_fin_chg = d.pop("misc_fin_chg", UNSET)

        misc_fin_inv = d.pop("misc_fin_inv", UNSET)

        misc_fin_inv_chg = d.pop("misc_fin_inv_chg", UNSET)

        misc_fin_ins = d.pop("misc_fin_ins", UNSET)

        misc_fin_ins_chg = d.pop("misc_fin_ins_chg", UNSET)

        misc_fin_futbrok = d.pop("misc_fin_futbrok", UNSET)

        misc_fin_futbrok_chg = d.pop("misc_fin_futbrok_chg", UNSET)

        misc_fin_finother = d.pop("misc_fin_finother", UNSET)

        misc_fin_finother_chg = d.pop("misc_fin_finother_chg", UNSET)

        misc_stockbrok = d.pop("misc_stockbrok", UNSET)

        misc_stockbrok_chg = d.pop("misc_stockbrok_chg", UNSET)

        misc_prof = d.pop("misc_prof", UNSET)

        misc_prof_chg = d.pop("misc_prof_chg", UNSET)

        misc_prof_purschflat = d.pop("misc_prof_purschflat", UNSET)

        misc_prof_purschflat_chg = d.pop("misc_prof_purschflat_chg", UNSET)

        misc_prof_purother = d.pop("misc_prof_purother", UNSET)

        misc_prof_purother_chg = d.pop("misc_prof_purother_chg", UNSET)

        misc_prof_ccadv = d.pop("misc_prof_ccadv", UNSET)

        misc_prof_ccadv_chg = d.pop("misc_prof_ccadv_chg", UNSET)

        misc_prof_otherbusi = d.pop("misc_prof_otherbusi", UNSET)

        misc_prof_otherbusi_chg = d.pop("misc_prof_otherbusi_chg", UNSET)

        misc_prof_otherpvt = d.pop("misc_prof_otherpvt", UNSET)

        misc_prof_otherpvt_chg = d.pop("misc_prof_otherpvt_chg", UNSET)

        misc_allother = d.pop("misc_allother", UNSET)

        misc_allother_chg = d.pop("misc_allother_chg", UNSET)

        loan_inhk = d.pop("loan_inhk", UNSET)

        loan_inhk_chg = d.pop("loan_inhk_chg", UNSET)

        record = cls(
            end_of_month=end_of_month,
            mfg=mfg,
            mfg_chg=mfg_chg,
            mfg_textiles=mfg_textiles,
            mfg_textiles_chg=mfg_textiles_chg,
            mfg_footwear=mfg_footwear,
            mfg_footwear_chg=mfg_footwear_chg,
            mfg_metalengr=mfg_metalengr,
            mfg_metalengr_chg=mfg_metalengr_chg,
            mfg_rubbplastchem=mfg_rubbplastchem,
            mfg_rubbplastchem_chg=mfg_rubbplastchem_chg,
            mfg_shipbuildrepair=mfg_shipbuildrepair,
            mfg_shipbuildrepair_chg=mfg_shipbuildrepair_chg,
            mfg_ee=mfg_ee,
            mfg_ee_chg=mfg_ee_chg,
            mfg_ee_teleequip=mfg_ee_teleequip,
            mfg_ee_teleequip_chg=mfg_ee_teleequip_chg,
            mfg_ee_other=mfg_ee_other,
            mfg_ee_other_chg=mfg_ee_other_chg,
            mfg_food=mfg_food,
            mfg_food_chg=mfg_food_chg,
            mfg_bevtob=mfg_bevtob,
            mfg_bevtob_chg=mfg_bevtob_chg,
            mfg_printpub=mfg_printpub,
            mfg_printpub_chg=mfg_printpub_chg,
            mfg_misc=mfg_misc,
            mfg_misc_chg=mfg_misc_chg,
            af=af,
            af_chg=af_chg,
            af_fisheries=af_fisheries,
            af_fisheries_chg=af_fisheries_chg,
            af_livestock=af_livestock,
            af_livestock_chg=af_livestock_chg,
            af_veghort=af_veghort,
            af_veghort_chg=af_veghort_chg,
            tran=tran,
            tran_chg=tran_chg,
            tran_shipping=tran_shipping,
            tran_shipping_chg=tran_shipping_chg,
            tran_airtran=tran_airtran,
            tran_airtran_chg=tran_airtran_chg,
            tran_taxisplb=tran_taxisplb,
            tran_taxisplb_chg=tran_taxisplb_chg,
            tran_taxisplb_taxis=tran_taxisplb_taxis,
            tran_taxisplb_taxis_chg=tran_taxisplb_taxis_chg,
            tran_taxisplb_plb=tran_taxisplb_plb,
            tran_taxisplb_plb_chg=tran_taxisplb_plb_chg,
            tran_other=tran_other,
            tran_other_chg=tran_other_chg,
            egt=egt,
            egt_chg=egt_chg,
            eg=eg,
            eg_chg=eg_chg,
            rec=rec,
            rec_chg=rec_chg,
            it=it,
            it_chg=it_chg,
            it_telecom=it_telecom,
            it_telecom_chg=it_telecom_chg,
            it_other=it_other,
            it_other_chg=it_other_chg,
            bcpi=bcpi,
            bcpi_chg=bcpi_chg,
            bcpi_propdev=bcpi_propdev,
            bcpi_propdev_chg=bcpi_propdev_chg,
            bcpi_propdev_ind=bcpi_propdev_ind,
            bcpi_propdev_ind_chg=bcpi_propdev_ind_chg,
            bcpi_propdev_res=bcpi_propdev_res,
            bcpi_propdev_res_chg=bcpi_propdev_res_chg,
            bcpi_propdev_comm=bcpi_propdev_comm,
            bcpi_propdev_comm_chg=bcpi_propdev_comm_chg,
            bcpi_propdev_other=bcpi_propdev_other,
            bcpi_propdev_other_chg=bcpi_propdev_other_chg,
            bcpi_other=bcpi_other,
            bcpi_other_chg=bcpi_other_chg,
            wsale=wsale,
            wsale_chg=wsale_chg,
            mine=mine,
            mine_chg=mine_chg,
            misc=misc,
            misc_chg=misc_chg,
            misc_hotelcater=misc_hotelcater,
            misc_hotelcater_chg=misc_hotelcater_chg,
            misc_fin=misc_fin,
            misc_fin_chg=misc_fin_chg,
            misc_fin_inv=misc_fin_inv,
            misc_fin_inv_chg=misc_fin_inv_chg,
            misc_fin_ins=misc_fin_ins,
            misc_fin_ins_chg=misc_fin_ins_chg,
            misc_fin_futbrok=misc_fin_futbrok,
            misc_fin_futbrok_chg=misc_fin_futbrok_chg,
            misc_fin_finother=misc_fin_finother,
            misc_fin_finother_chg=misc_fin_finother_chg,
            misc_stockbrok=misc_stockbrok,
            misc_stockbrok_chg=misc_stockbrok_chg,
            misc_prof=misc_prof,
            misc_prof_chg=misc_prof_chg,
            misc_prof_purschflat=misc_prof_purschflat,
            misc_prof_purschflat_chg=misc_prof_purschflat_chg,
            misc_prof_purother=misc_prof_purother,
            misc_prof_purother_chg=misc_prof_purother_chg,
            misc_prof_ccadv=misc_prof_ccadv,
            misc_prof_ccadv_chg=misc_prof_ccadv_chg,
            misc_prof_otherbusi=misc_prof_otherbusi,
            misc_prof_otherbusi_chg=misc_prof_otherbusi_chg,
            misc_prof_otherpvt=misc_prof_otherpvt,
            misc_prof_otherpvt_chg=misc_prof_otherpvt_chg,
            misc_allother=misc_allother,
            misc_allother_chg=misc_allother_chg,
            loan_inhk=loan_inhk,
            loan_inhk_chg=loan_inhk_chg,
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
