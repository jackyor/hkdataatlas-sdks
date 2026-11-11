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
        usd (float | Unset):
        gbp (float | Unset):
        jpy (float | Unset):
        cad (float | Unset):
        aud (float | Unset):
        sgd (float | Unset):
        twd (float | Unset):
        chf (float | Unset):
        cny (float | Unset):
        krw (float | Unset):
        thb (float | Unset):
        myr (float | Unset):
        dem (float | Unset):
        nlg (float | Unset):
        bef (float | Unset):
        frf (float | Unset):
        itl (float | Unset):
        eur (float | Unset):
        php (float | Unset):
        inr (float | Unset):
        special_drawing_rights (float | Unset):
        neeri_1983_trade_wgt (float | Unset):
        neeri_1983_import_wgt (float | Unset):
        neeri_1983_export_wgt (float | Unset):
        reeri_1983_trade_wgt (float | Unset):
        neeri_2000_trade_wgt (float | Unset):
        neeri_2000_import_wgt (float | Unset):
        neeri_2000_export_wgt (float | Unset):
        reeri_2000_trade_wgt (float | Unset):
        neeri_2010_trade_wgt (float | Unset):
        neeri_2010_import_wgt (float | Unset):
        neeri_2010_export_wgt (float | Unset):
        reeri_2010_trade_wgt (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    usd: float | Unset = UNSET
    gbp: float | Unset = UNSET
    jpy: float | Unset = UNSET
    cad: float | Unset = UNSET
    aud: float | Unset = UNSET
    sgd: float | Unset = UNSET
    twd: float | Unset = UNSET
    chf: float | Unset = UNSET
    cny: float | Unset = UNSET
    krw: float | Unset = UNSET
    thb: float | Unset = UNSET
    myr: float | Unset = UNSET
    dem: float | Unset = UNSET
    nlg: float | Unset = UNSET
    bef: float | Unset = UNSET
    frf: float | Unset = UNSET
    itl: float | Unset = UNSET
    eur: float | Unset = UNSET
    php: float | Unset = UNSET
    inr: float | Unset = UNSET
    special_drawing_rights: float | Unset = UNSET
    neeri_1983_trade_wgt: float | Unset = UNSET
    neeri_1983_import_wgt: float | Unset = UNSET
    neeri_1983_export_wgt: float | Unset = UNSET
    reeri_1983_trade_wgt: float | Unset = UNSET
    neeri_2000_trade_wgt: float | Unset = UNSET
    neeri_2000_import_wgt: float | Unset = UNSET
    neeri_2000_export_wgt: float | Unset = UNSET
    reeri_2000_trade_wgt: float | Unset = UNSET
    neeri_2010_trade_wgt: float | Unset = UNSET
    neeri_2010_import_wgt: float | Unset = UNSET
    neeri_2010_export_wgt: float | Unset = UNSET
    reeri_2010_trade_wgt: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        usd = self.usd

        gbp = self.gbp

        jpy = self.jpy

        cad = self.cad

        aud = self.aud

        sgd = self.sgd

        twd = self.twd

        chf = self.chf

        cny = self.cny

        krw = self.krw

        thb = self.thb

        myr = self.myr

        dem = self.dem

        nlg = self.nlg

        bef = self.bef

        frf = self.frf

        itl = self.itl

        eur = self.eur

        php = self.php

        inr = self.inr

        special_drawing_rights = self.special_drawing_rights

        neeri_1983_trade_wgt = self.neeri_1983_trade_wgt

        neeri_1983_import_wgt = self.neeri_1983_import_wgt

        neeri_1983_export_wgt = self.neeri_1983_export_wgt

        reeri_1983_trade_wgt = self.reeri_1983_trade_wgt

        neeri_2000_trade_wgt = self.neeri_2000_trade_wgt

        neeri_2000_import_wgt = self.neeri_2000_import_wgt

        neeri_2000_export_wgt = self.neeri_2000_export_wgt

        reeri_2000_trade_wgt = self.reeri_2000_trade_wgt

        neeri_2010_trade_wgt = self.neeri_2010_trade_wgt

        neeri_2010_import_wgt = self.neeri_2010_import_wgt

        neeri_2010_export_wgt = self.neeri_2010_export_wgt

        reeri_2010_trade_wgt = self.reeri_2010_trade_wgt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if usd is not UNSET:
            field_dict["usd"] = usd
        if gbp is not UNSET:
            field_dict["gbp"] = gbp
        if jpy is not UNSET:
            field_dict["jpy"] = jpy
        if cad is not UNSET:
            field_dict["cad"] = cad
        if aud is not UNSET:
            field_dict["aud"] = aud
        if sgd is not UNSET:
            field_dict["sgd"] = sgd
        if twd is not UNSET:
            field_dict["twd"] = twd
        if chf is not UNSET:
            field_dict["chf"] = chf
        if cny is not UNSET:
            field_dict["cny"] = cny
        if krw is not UNSET:
            field_dict["krw"] = krw
        if thb is not UNSET:
            field_dict["thb"] = thb
        if myr is not UNSET:
            field_dict["myr"] = myr
        if dem is not UNSET:
            field_dict["dem"] = dem
        if nlg is not UNSET:
            field_dict["nlg"] = nlg
        if bef is not UNSET:
            field_dict["bef"] = bef
        if frf is not UNSET:
            field_dict["frf"] = frf
        if itl is not UNSET:
            field_dict["itl"] = itl
        if eur is not UNSET:
            field_dict["eur"] = eur
        if php is not UNSET:
            field_dict["php"] = php
        if inr is not UNSET:
            field_dict["inr"] = inr
        if special_drawing_rights is not UNSET:
            field_dict["special_drawing_rights"] = special_drawing_rights
        if neeri_1983_trade_wgt is not UNSET:
            field_dict["neeri_1983_trade_wgt"] = neeri_1983_trade_wgt
        if neeri_1983_import_wgt is not UNSET:
            field_dict["neeri_1983_import_wgt"] = neeri_1983_import_wgt
        if neeri_1983_export_wgt is not UNSET:
            field_dict["neeri_1983_export_wgt"] = neeri_1983_export_wgt
        if reeri_1983_trade_wgt is not UNSET:
            field_dict["reeri_1983_trade_wgt"] = reeri_1983_trade_wgt
        if neeri_2000_trade_wgt is not UNSET:
            field_dict["neeri_2000_trade_wgt"] = neeri_2000_trade_wgt
        if neeri_2000_import_wgt is not UNSET:
            field_dict["neeri_2000_import_wgt"] = neeri_2000_import_wgt
        if neeri_2000_export_wgt is not UNSET:
            field_dict["neeri_2000_export_wgt"] = neeri_2000_export_wgt
        if reeri_2000_trade_wgt is not UNSET:
            field_dict["reeri_2000_trade_wgt"] = reeri_2000_trade_wgt
        if neeri_2010_trade_wgt is not UNSET:
            field_dict["neeri_2010_trade_wgt"] = neeri_2010_trade_wgt
        if neeri_2010_import_wgt is not UNSET:
            field_dict["neeri_2010_import_wgt"] = neeri_2010_import_wgt
        if neeri_2010_export_wgt is not UNSET:
            field_dict["neeri_2010_export_wgt"] = neeri_2010_export_wgt
        if reeri_2010_trade_wgt is not UNSET:
            field_dict["reeri_2010_trade_wgt"] = reeri_2010_trade_wgt

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

        usd = d.pop("usd", UNSET)

        gbp = d.pop("gbp", UNSET)

        jpy = d.pop("jpy", UNSET)

        cad = d.pop("cad", UNSET)

        aud = d.pop("aud", UNSET)

        sgd = d.pop("sgd", UNSET)

        twd = d.pop("twd", UNSET)

        chf = d.pop("chf", UNSET)

        cny = d.pop("cny", UNSET)

        krw = d.pop("krw", UNSET)

        thb = d.pop("thb", UNSET)

        myr = d.pop("myr", UNSET)

        dem = d.pop("dem", UNSET)

        nlg = d.pop("nlg", UNSET)

        bef = d.pop("bef", UNSET)

        frf = d.pop("frf", UNSET)

        itl = d.pop("itl", UNSET)

        eur = d.pop("eur", UNSET)

        php = d.pop("php", UNSET)

        inr = d.pop("inr", UNSET)

        special_drawing_rights = d.pop("special_drawing_rights", UNSET)

        neeri_1983_trade_wgt = d.pop("neeri_1983_trade_wgt", UNSET)

        neeri_1983_import_wgt = d.pop("neeri_1983_import_wgt", UNSET)

        neeri_1983_export_wgt = d.pop("neeri_1983_export_wgt", UNSET)

        reeri_1983_trade_wgt = d.pop("reeri_1983_trade_wgt", UNSET)

        neeri_2000_trade_wgt = d.pop("neeri_2000_trade_wgt", UNSET)

        neeri_2000_import_wgt = d.pop("neeri_2000_import_wgt", UNSET)

        neeri_2000_export_wgt = d.pop("neeri_2000_export_wgt", UNSET)

        reeri_2000_trade_wgt = d.pop("reeri_2000_trade_wgt", UNSET)

        neeri_2010_trade_wgt = d.pop("neeri_2010_trade_wgt", UNSET)

        neeri_2010_import_wgt = d.pop("neeri_2010_import_wgt", UNSET)

        neeri_2010_export_wgt = d.pop("neeri_2010_export_wgt", UNSET)

        reeri_2010_trade_wgt = d.pop("reeri_2010_trade_wgt", UNSET)

        record = cls(
            end_of_month=end_of_month,
            usd=usd,
            gbp=gbp,
            jpy=jpy,
            cad=cad,
            aud=aud,
            sgd=sgd,
            twd=twd,
            chf=chf,
            cny=cny,
            krw=krw,
            thb=thb,
            myr=myr,
            dem=dem,
            nlg=nlg,
            bef=bef,
            frf=frf,
            itl=itl,
            eur=eur,
            php=php,
            inr=inr,
            special_drawing_rights=special_drawing_rights,
            neeri_1983_trade_wgt=neeri_1983_trade_wgt,
            neeri_1983_import_wgt=neeri_1983_import_wgt,
            neeri_1983_export_wgt=neeri_1983_export_wgt,
            reeri_1983_trade_wgt=reeri_1983_trade_wgt,
            neeri_2000_trade_wgt=neeri_2000_trade_wgt,
            neeri_2000_import_wgt=neeri_2000_import_wgt,
            neeri_2000_export_wgt=neeri_2000_export_wgt,
            reeri_2000_trade_wgt=reeri_2000_trade_wgt,
            neeri_2010_trade_wgt=neeri_2010_trade_wgt,
            neeri_2010_import_wgt=neeri_2010_import_wgt,
            neeri_2010_export_wgt=neeri_2010_export_wgt,
            reeri_2010_trade_wgt=reeri_2010_trade_wgt,
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
