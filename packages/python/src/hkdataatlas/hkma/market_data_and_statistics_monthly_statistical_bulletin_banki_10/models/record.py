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
        mfg_textiles (float | Unset):
        mfg_footwear (float | Unset):
        mfg_metalengr (float | Unset):
        mfg_rubbplastchem (float | Unset):
        mfg_shipbuildrepair (float | Unset):
        mfg_ee (float | Unset):
        mfg_ee_teleequip (float | Unset):
        mfg_ee_other (float | Unset):
        mfg_food (float | Unset):
        mfg_bevtob (float | Unset):
        mfg_printpub (float | Unset):
        mfg_misc (float | Unset):
        af (float | Unset):
        af_fisheries (float | Unset):
        af_livestock (float | Unset):
        af_veghort (float | Unset):
        tran (float | Unset):
        tran_shipping (float | Unset):
        tran_airtran (float | Unset):
        tran_taxisplb (float | Unset):
        tran_taxisplb_taxis (float | Unset):
        tran_taxisplb_plb (float | Unset):
        tran_other (float | Unset):
        egt (float | Unset):
        eg (float | Unset):
        rec (float | Unset):
        it (float | Unset):
        it_telecom (float | Unset):
        it_other (float | Unset):
        bcpi (float | Unset):
        bcpi_propdev (float | Unset):
        bcpi_propdev_ind (float | Unset):
        bcpi_propdev_res (float | Unset):
        bcpi_propdev_comm (float | Unset):
        bcpi_propdev_other (float | Unset):
        bcpi_other (float | Unset):
        wsale (float | Unset):
        mine (float | Unset):
        misc (float | Unset):
        misc_hotelcater (float | Unset):
        misc_fin (float | Unset):
        misc_fin_inv (float | Unset):
        misc_fin_ins (float | Unset):
        misc_fin_futbrok (float | Unset):
        misc_fin_finother (float | Unset):
        misc_stockbrok (float | Unset):
        misc_prof (float | Unset):
        misc_prof_purschflat (float | Unset):
        misc_prof_purother (float | Unset):
        misc_prof_other (float | Unset):
        misc_allother (float | Unset):
        loan_inhk (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    mfg: float | Unset = UNSET
    mfg_textiles: float | Unset = UNSET
    mfg_footwear: float | Unset = UNSET
    mfg_metalengr: float | Unset = UNSET
    mfg_rubbplastchem: float | Unset = UNSET
    mfg_shipbuildrepair: float | Unset = UNSET
    mfg_ee: float | Unset = UNSET
    mfg_ee_teleequip: float | Unset = UNSET
    mfg_ee_other: float | Unset = UNSET
    mfg_food: float | Unset = UNSET
    mfg_bevtob: float | Unset = UNSET
    mfg_printpub: float | Unset = UNSET
    mfg_misc: float | Unset = UNSET
    af: float | Unset = UNSET
    af_fisheries: float | Unset = UNSET
    af_livestock: float | Unset = UNSET
    af_veghort: float | Unset = UNSET
    tran: float | Unset = UNSET
    tran_shipping: float | Unset = UNSET
    tran_airtran: float | Unset = UNSET
    tran_taxisplb: float | Unset = UNSET
    tran_taxisplb_taxis: float | Unset = UNSET
    tran_taxisplb_plb: float | Unset = UNSET
    tran_other: float | Unset = UNSET
    egt: float | Unset = UNSET
    eg: float | Unset = UNSET
    rec: float | Unset = UNSET
    it: float | Unset = UNSET
    it_telecom: float | Unset = UNSET
    it_other: float | Unset = UNSET
    bcpi: float | Unset = UNSET
    bcpi_propdev: float | Unset = UNSET
    bcpi_propdev_ind: float | Unset = UNSET
    bcpi_propdev_res: float | Unset = UNSET
    bcpi_propdev_comm: float | Unset = UNSET
    bcpi_propdev_other: float | Unset = UNSET
    bcpi_other: float | Unset = UNSET
    wsale: float | Unset = UNSET
    mine: float | Unset = UNSET
    misc: float | Unset = UNSET
    misc_hotelcater: float | Unset = UNSET
    misc_fin: float | Unset = UNSET
    misc_fin_inv: float | Unset = UNSET
    misc_fin_ins: float | Unset = UNSET
    misc_fin_futbrok: float | Unset = UNSET
    misc_fin_finother: float | Unset = UNSET
    misc_stockbrok: float | Unset = UNSET
    misc_prof: float | Unset = UNSET
    misc_prof_purschflat: float | Unset = UNSET
    misc_prof_purother: float | Unset = UNSET
    misc_prof_other: float | Unset = UNSET
    misc_allother: float | Unset = UNSET
    loan_inhk: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        mfg = self.mfg

        mfg_textiles = self.mfg_textiles

        mfg_footwear = self.mfg_footwear

        mfg_metalengr = self.mfg_metalengr

        mfg_rubbplastchem = self.mfg_rubbplastchem

        mfg_shipbuildrepair = self.mfg_shipbuildrepair

        mfg_ee = self.mfg_ee

        mfg_ee_teleequip = self.mfg_ee_teleequip

        mfg_ee_other = self.mfg_ee_other

        mfg_food = self.mfg_food

        mfg_bevtob = self.mfg_bevtob

        mfg_printpub = self.mfg_printpub

        mfg_misc = self.mfg_misc

        af = self.af

        af_fisheries = self.af_fisheries

        af_livestock = self.af_livestock

        af_veghort = self.af_veghort

        tran = self.tran

        tran_shipping = self.tran_shipping

        tran_airtran = self.tran_airtran

        tran_taxisplb = self.tran_taxisplb

        tran_taxisplb_taxis = self.tran_taxisplb_taxis

        tran_taxisplb_plb = self.tran_taxisplb_plb

        tran_other = self.tran_other

        egt = self.egt

        eg = self.eg

        rec = self.rec

        it = self.it

        it_telecom = self.it_telecom

        it_other = self.it_other

        bcpi = self.bcpi

        bcpi_propdev = self.bcpi_propdev

        bcpi_propdev_ind = self.bcpi_propdev_ind

        bcpi_propdev_res = self.bcpi_propdev_res

        bcpi_propdev_comm = self.bcpi_propdev_comm

        bcpi_propdev_other = self.bcpi_propdev_other

        bcpi_other = self.bcpi_other

        wsale = self.wsale

        mine = self.mine

        misc = self.misc

        misc_hotelcater = self.misc_hotelcater

        misc_fin = self.misc_fin

        misc_fin_inv = self.misc_fin_inv

        misc_fin_ins = self.misc_fin_ins

        misc_fin_futbrok = self.misc_fin_futbrok

        misc_fin_finother = self.misc_fin_finother

        misc_stockbrok = self.misc_stockbrok

        misc_prof = self.misc_prof

        misc_prof_purschflat = self.misc_prof_purschflat

        misc_prof_purother = self.misc_prof_purother

        misc_prof_other = self.misc_prof_other

        misc_allother = self.misc_allother

        loan_inhk = self.loan_inhk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if mfg is not UNSET:
            field_dict["mfg"] = mfg
        if mfg_textiles is not UNSET:
            field_dict["mfg_textiles"] = mfg_textiles
        if mfg_footwear is not UNSET:
            field_dict["mfg_footwear"] = mfg_footwear
        if mfg_metalengr is not UNSET:
            field_dict["mfg_metalengr"] = mfg_metalengr
        if mfg_rubbplastchem is not UNSET:
            field_dict["mfg_rubbplastchem"] = mfg_rubbplastchem
        if mfg_shipbuildrepair is not UNSET:
            field_dict["mfg_shipbuildrepair"] = mfg_shipbuildrepair
        if mfg_ee is not UNSET:
            field_dict["mfg_ee"] = mfg_ee
        if mfg_ee_teleequip is not UNSET:
            field_dict["mfg_ee_teleequip"] = mfg_ee_teleequip
        if mfg_ee_other is not UNSET:
            field_dict["mfg_ee_other"] = mfg_ee_other
        if mfg_food is not UNSET:
            field_dict["mfg_food"] = mfg_food
        if mfg_bevtob is not UNSET:
            field_dict["mfg_bevtob"] = mfg_bevtob
        if mfg_printpub is not UNSET:
            field_dict["mfg_printpub"] = mfg_printpub
        if mfg_misc is not UNSET:
            field_dict["mfg_misc"] = mfg_misc
        if af is not UNSET:
            field_dict["af"] = af
        if af_fisheries is not UNSET:
            field_dict["af_fisheries"] = af_fisheries
        if af_livestock is not UNSET:
            field_dict["af_livestock"] = af_livestock
        if af_veghort is not UNSET:
            field_dict["af_veghort"] = af_veghort
        if tran is not UNSET:
            field_dict["tran"] = tran
        if tran_shipping is not UNSET:
            field_dict["tran_shipping"] = tran_shipping
        if tran_airtran is not UNSET:
            field_dict["tran_airtran"] = tran_airtran
        if tran_taxisplb is not UNSET:
            field_dict["tran_taxisplb"] = tran_taxisplb
        if tran_taxisplb_taxis is not UNSET:
            field_dict["tran_taxisplb_taxis"] = tran_taxisplb_taxis
        if tran_taxisplb_plb is not UNSET:
            field_dict["tran_taxisplb_plb"] = tran_taxisplb_plb
        if tran_other is not UNSET:
            field_dict["tran_other"] = tran_other
        if egt is not UNSET:
            field_dict["egt"] = egt
        if eg is not UNSET:
            field_dict["eg"] = eg
        if rec is not UNSET:
            field_dict["rec"] = rec
        if it is not UNSET:
            field_dict["it"] = it
        if it_telecom is not UNSET:
            field_dict["it_telecom"] = it_telecom
        if it_other is not UNSET:
            field_dict["it_other"] = it_other
        if bcpi is not UNSET:
            field_dict["bcpi"] = bcpi
        if bcpi_propdev is not UNSET:
            field_dict["bcpi_propdev"] = bcpi_propdev
        if bcpi_propdev_ind is not UNSET:
            field_dict["bcpi_propdev_ind"] = bcpi_propdev_ind
        if bcpi_propdev_res is not UNSET:
            field_dict["bcpi_propdev_res"] = bcpi_propdev_res
        if bcpi_propdev_comm is not UNSET:
            field_dict["bcpi_propdev_comm"] = bcpi_propdev_comm
        if bcpi_propdev_other is not UNSET:
            field_dict["bcpi_propdev_other"] = bcpi_propdev_other
        if bcpi_other is not UNSET:
            field_dict["bcpi_other"] = bcpi_other
        if wsale is not UNSET:
            field_dict["wsale"] = wsale
        if mine is not UNSET:
            field_dict["mine"] = mine
        if misc is not UNSET:
            field_dict["misc"] = misc
        if misc_hotelcater is not UNSET:
            field_dict["misc_hotelcater"] = misc_hotelcater
        if misc_fin is not UNSET:
            field_dict["misc_fin"] = misc_fin
        if misc_fin_inv is not UNSET:
            field_dict["misc_fin_inv"] = misc_fin_inv
        if misc_fin_ins is not UNSET:
            field_dict["misc_fin_ins"] = misc_fin_ins
        if misc_fin_futbrok is not UNSET:
            field_dict["misc_fin_futbrok"] = misc_fin_futbrok
        if misc_fin_finother is not UNSET:
            field_dict["misc_fin_finother"] = misc_fin_finother
        if misc_stockbrok is not UNSET:
            field_dict["misc_stockbrok"] = misc_stockbrok
        if misc_prof is not UNSET:
            field_dict["misc_prof"] = misc_prof
        if misc_prof_purschflat is not UNSET:
            field_dict["misc_prof_purschflat"] = misc_prof_purschflat
        if misc_prof_purother is not UNSET:
            field_dict["misc_prof_purother"] = misc_prof_purother
        if misc_prof_other is not UNSET:
            field_dict["misc_prof_other"] = misc_prof_other
        if misc_allother is not UNSET:
            field_dict["misc_allother"] = misc_allother
        if loan_inhk is not UNSET:
            field_dict["loan_inhk"] = loan_inhk

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

        mfg_textiles = d.pop("mfg_textiles", UNSET)

        mfg_footwear = d.pop("mfg_footwear", UNSET)

        mfg_metalengr = d.pop("mfg_metalengr", UNSET)

        mfg_rubbplastchem = d.pop("mfg_rubbplastchem", UNSET)

        mfg_shipbuildrepair = d.pop("mfg_shipbuildrepair", UNSET)

        mfg_ee = d.pop("mfg_ee", UNSET)

        mfg_ee_teleequip = d.pop("mfg_ee_teleequip", UNSET)

        mfg_ee_other = d.pop("mfg_ee_other", UNSET)

        mfg_food = d.pop("mfg_food", UNSET)

        mfg_bevtob = d.pop("mfg_bevtob", UNSET)

        mfg_printpub = d.pop("mfg_printpub", UNSET)

        mfg_misc = d.pop("mfg_misc", UNSET)

        af = d.pop("af", UNSET)

        af_fisheries = d.pop("af_fisheries", UNSET)

        af_livestock = d.pop("af_livestock", UNSET)

        af_veghort = d.pop("af_veghort", UNSET)

        tran = d.pop("tran", UNSET)

        tran_shipping = d.pop("tran_shipping", UNSET)

        tran_airtran = d.pop("tran_airtran", UNSET)

        tran_taxisplb = d.pop("tran_taxisplb", UNSET)

        tran_taxisplb_taxis = d.pop("tran_taxisplb_taxis", UNSET)

        tran_taxisplb_plb = d.pop("tran_taxisplb_plb", UNSET)

        tran_other = d.pop("tran_other", UNSET)

        egt = d.pop("egt", UNSET)

        eg = d.pop("eg", UNSET)

        rec = d.pop("rec", UNSET)

        it = d.pop("it", UNSET)

        it_telecom = d.pop("it_telecom", UNSET)

        it_other = d.pop("it_other", UNSET)

        bcpi = d.pop("bcpi", UNSET)

        bcpi_propdev = d.pop("bcpi_propdev", UNSET)

        bcpi_propdev_ind = d.pop("bcpi_propdev_ind", UNSET)

        bcpi_propdev_res = d.pop("bcpi_propdev_res", UNSET)

        bcpi_propdev_comm = d.pop("bcpi_propdev_comm", UNSET)

        bcpi_propdev_other = d.pop("bcpi_propdev_other", UNSET)

        bcpi_other = d.pop("bcpi_other", UNSET)

        wsale = d.pop("wsale", UNSET)

        mine = d.pop("mine", UNSET)

        misc = d.pop("misc", UNSET)

        misc_hotelcater = d.pop("misc_hotelcater", UNSET)

        misc_fin = d.pop("misc_fin", UNSET)

        misc_fin_inv = d.pop("misc_fin_inv", UNSET)

        misc_fin_ins = d.pop("misc_fin_ins", UNSET)

        misc_fin_futbrok = d.pop("misc_fin_futbrok", UNSET)

        misc_fin_finother = d.pop("misc_fin_finother", UNSET)

        misc_stockbrok = d.pop("misc_stockbrok", UNSET)

        misc_prof = d.pop("misc_prof", UNSET)

        misc_prof_purschflat = d.pop("misc_prof_purschflat", UNSET)

        misc_prof_purother = d.pop("misc_prof_purother", UNSET)

        misc_prof_other = d.pop("misc_prof_other", UNSET)

        misc_allother = d.pop("misc_allother", UNSET)

        loan_inhk = d.pop("loan_inhk", UNSET)

        record = cls(
            end_of_month=end_of_month,
            mfg=mfg,
            mfg_textiles=mfg_textiles,
            mfg_footwear=mfg_footwear,
            mfg_metalengr=mfg_metalengr,
            mfg_rubbplastchem=mfg_rubbplastchem,
            mfg_shipbuildrepair=mfg_shipbuildrepair,
            mfg_ee=mfg_ee,
            mfg_ee_teleequip=mfg_ee_teleequip,
            mfg_ee_other=mfg_ee_other,
            mfg_food=mfg_food,
            mfg_bevtob=mfg_bevtob,
            mfg_printpub=mfg_printpub,
            mfg_misc=mfg_misc,
            af=af,
            af_fisheries=af_fisheries,
            af_livestock=af_livestock,
            af_veghort=af_veghort,
            tran=tran,
            tran_shipping=tran_shipping,
            tran_airtran=tran_airtran,
            tran_taxisplb=tran_taxisplb,
            tran_taxisplb_taxis=tran_taxisplb_taxis,
            tran_taxisplb_plb=tran_taxisplb_plb,
            tran_other=tran_other,
            egt=egt,
            eg=eg,
            rec=rec,
            it=it,
            it_telecom=it_telecom,
            it_other=it_other,
            bcpi=bcpi,
            bcpi_propdev=bcpi_propdev,
            bcpi_propdev_ind=bcpi_propdev_ind,
            bcpi_propdev_res=bcpi_propdev_res,
            bcpi_propdev_comm=bcpi_propdev_comm,
            bcpi_propdev_other=bcpi_propdev_other,
            bcpi_other=bcpi_other,
            wsale=wsale,
            mine=mine,
            misc=misc,
            misc_hotelcater=misc_hotelcater,
            misc_fin=misc_fin,
            misc_fin_inv=misc_fin_inv,
            misc_fin_ins=misc_fin_ins,
            misc_fin_futbrok=misc_fin_futbrok,
            misc_fin_finother=misc_fin_finother,
            misc_stockbrok=misc_stockbrok,
            misc_prof=misc_prof,
            misc_prof_purschflat=misc_prof_purschflat,
            misc_prof_purother=misc_prof_purother,
            misc_prof_other=misc_prof_other,
            misc_allother=misc_allother,
            loan_inhk=loan_inhk,
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
