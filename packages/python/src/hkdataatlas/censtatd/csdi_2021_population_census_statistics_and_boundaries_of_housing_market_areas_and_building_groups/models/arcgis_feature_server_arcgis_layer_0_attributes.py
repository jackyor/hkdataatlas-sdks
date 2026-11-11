from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        adhz (float | None | Unset): Publisher field type: esriFieldTypeDouble
        age_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        age_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        age_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        age_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        anr_h (float | None | Unset): Publisher field type: esriFieldTypeDouble
        anr_p (float | None | Unset): Publisher field type: esriFieldTypeDouble
        bg (None | str | Unset): Publisher field type: esriFieldTypeString
        bg_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        bg_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        bg_ind (None | str | Unset): Publisher field type: esriFieldTypeString
        born_chi (float | None | Unset): Publisher field type: esriFieldTypeDouble
        born_else (float | None | Unset): Publisher field type: esriFieldTypeDouble
        born_hk (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_ocm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_ocwm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_old (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_old_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        dh_old_2 (None | str | Unset): Publisher field type: esriFieldTypeString
        dh_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r0 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_st (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_xfdh_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        dhi_xfdh_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_xfdh_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhm_loan (None | str | Unset): Publisher field type: esriFieldTypeString
        dhm_lp (None | str | Unset): Publisher field type: esriFieldTypeString
        dhm_lr (None | str | Unset): Publisher field type: esriFieldTypeString
        dhn_c (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhn_nc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dm_r (None | str | Unset): Publisher field type: esriFieldTypeString
        dmr_ir (None | str | Unset): Publisher field type: esriFieldTypeString
        edu_pri_prepri (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_sec (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_ter (float | None | Unset): Publisher field type: esriFieldTypeDouble
        fa_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        fa_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        fa_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        hma (None | str | Unset): Publisher field type: esriFieldTypeString
        hma_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        hma_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        ma_dhn (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ma_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ma_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfw_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfw_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfw_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nm_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nm_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nwp_nonstu (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nwp_st (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_r1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_r2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_r3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_r4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        s_bus (float | None | Unset): Publisher field type: esriFieldTypeDouble
        s_dc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        s_foot (float | None | Unset): Publisher field type: esriFieldTypeDouble
        s_mtr (float | None | Unset): Publisher field type: esriFieldTypeDouble
        s_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        s_sb (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sr (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_ma (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_nwp (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_pop (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_wp (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ul_can (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ul_eng_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ul_put_othchi (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_xfdh_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_xfdh_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_xfdh_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_a (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_b (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_bus (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_c (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_d (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_dc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_e (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_ee (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_er (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_foot (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_g (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_h (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_i (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_mtr (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_plb (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_se_fw (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    adhz: float | None | Unset = UNSET
    age_1: float | None | Unset = UNSET
    age_2: float | None | Unset = UNSET
    age_3: float | None | Unset = UNSET
    age_4: float | None | Unset = UNSET
    anr_h: float | None | Unset = UNSET
    anr_p: float | None | Unset = UNSET
    bg: None | str | Unset = UNSET
    bg_chi: None | str | Unset = UNSET
    bg_eng: None | str | Unset = UNSET
    bg_ind: None | str | Unset = UNSET
    born_chi: float | None | Unset = UNSET
    born_else: float | None | Unset = UNSET
    born_hk: float | None | Unset = UNSET
    dh_ocm: float | None | Unset = UNSET
    dh_ocwm: float | None | Unset = UNSET
    dh_old: float | None | Unset = UNSET
    dh_old_1: None | str | Unset = UNSET
    dh_old_2: None | str | Unset = UNSET
    dh_oth: float | None | Unset = UNSET
    dh_r0: float | None | Unset = UNSET
    dh_r1: float | None | Unset = UNSET
    dh_r3: float | None | Unset = UNSET
    dh_r4: float | None | Unset = UNSET
    dh_r5: float | None | Unset = UNSET
    dh_st: float | None | Unset = UNSET
    dhc_1: float | None | Unset = UNSET
    dhc_2: float | None | Unset = UNSET
    dhc_3: float | None | Unset = UNSET
    dhi_1: float | None | Unset = UNSET
    dhi_2: float | None | Unset = UNSET
    dhi_3: float | None | Unset = UNSET
    dhi_xfdh_1: None | str | Unset = UNSET
    dhi_xfdh_2: float | None | Unset = UNSET
    dhi_xfdh_3: float | None | Unset = UNSET
    dhm_loan: None | str | Unset = UNSET
    dhm_lp: None | str | Unset = UNSET
    dhm_lr: None | str | Unset = UNSET
    dhn_c: float | None | Unset = UNSET
    dhn_nc: float | None | Unset = UNSET
    dhz_1: float | None | Unset = UNSET
    dhz_2: float | None | Unset = UNSET
    dhz_3: float | None | Unset = UNSET
    dm_r: None | str | Unset = UNSET
    dmr_ir: None | str | Unset = UNSET
    edu_pri_prepri: float | None | Unset = UNSET
    edu_sec: float | None | Unset = UNSET
    edu_ter: float | None | Unset = UNSET
    fa_1: float | None | Unset = UNSET
    fa_2: float | None | Unset = UNSET
    fa_3: float | None | Unset = UNSET
    hma: None | str | Unset = UNSET
    hma_chi: None | str | Unset = UNSET
    hma_eng: None | str | Unset = UNSET
    ma_dhn: float | None | Unset = UNSET
    ma_f: float | None | Unset = UNSET
    ma_m: float | None | Unset = UNSET
    mearn_xfdhfw_1: float | None | Unset = UNSET
    mearn_xfdhfw_2: float | None | Unset = UNSET
    mearn_xfdhfw_3: float | None | Unset = UNSET
    mearn_xfw_1: float | None | Unset = UNSET
    mearn_xfw_2: float | None | Unset = UNSET
    mearn_xfw_3: float | None | Unset = UNSET
    nm_f: float | None | Unset = UNSET
    nm_m: float | None | Unset = UNSET
    nwp_nonstu: float | None | Unset = UNSET
    nwp_st: float | None | Unset = UNSET
    pm_r1: float | None | Unset = UNSET
    pm_r2: float | None | Unset = UNSET
    pm_r3: float | None | Unset = UNSET
    pm_r4: float | None | Unset = UNSET
    s_bus: float | None | Unset = UNSET
    s_dc: float | None | Unset = UNSET
    s_foot: float | None | Unset = UNSET
    s_mtr: float | None | Unset = UNSET
    s_oth: float | None | Unset = UNSET
    s_sb: float | None | Unset = UNSET
    sr: float | None | Unset = UNSET
    t_ma: float | None | Unset = UNSET
    t_nwp: float | None | Unset = UNSET
    t_pop: float | None | Unset = UNSET
    t_wp: float | None | Unset = UNSET
    ul_can: float | None | Unset = UNSET
    ul_eng_oth: float | None | Unset = UNSET
    ul_put_othchi: float | None | Unset = UNSET
    whr_1: float | None | Unset = UNSET
    whr_2: float | None | Unset = UNSET
    whr_3: float | None | Unset = UNSET
    whr_xfdh_1: float | None | Unset = UNSET
    whr_xfdh_2: float | None | Unset = UNSET
    whr_xfdh_3: float | None | Unset = UNSET
    wp_a: float | None | Unset = UNSET
    wp_b: float | None | Unset = UNSET
    wp_bus: float | None | Unset = UNSET
    wp_c: float | None | Unset = UNSET
    wp_d: float | None | Unset = UNSET
    wp_dc: float | None | Unset = UNSET
    wp_e: float | None | Unset = UNSET
    wp_ee: float | None | Unset = UNSET
    wp_er: float | None | Unset = UNSET
    wp_f: float | None | Unset = UNSET
    wp_foot: float | None | Unset = UNSET
    wp_g: float | None | Unset = UNSET
    wp_h: float | None | Unset = UNSET
    wp_i: float | None | Unset = UNSET
    wp_mtr: float | None | Unset = UNSET
    wp_oth: float | None | Unset = UNSET
    wp_plb: float | None | Unset = UNSET
    wp_se_fw: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adhz: float | None | Unset
        if isinstance(self.adhz, Unset):
            adhz = UNSET
        else:
            adhz = self.adhz

        age_1: float | None | Unset
        if isinstance(self.age_1, Unset):
            age_1 = UNSET
        else:
            age_1 = self.age_1

        age_2: float | None | Unset
        if isinstance(self.age_2, Unset):
            age_2 = UNSET
        else:
            age_2 = self.age_2

        age_3: float | None | Unset
        if isinstance(self.age_3, Unset):
            age_3 = UNSET
        else:
            age_3 = self.age_3

        age_4: float | None | Unset
        if isinstance(self.age_4, Unset):
            age_4 = UNSET
        else:
            age_4 = self.age_4

        anr_h: float | None | Unset
        if isinstance(self.anr_h, Unset):
            anr_h = UNSET
        else:
            anr_h = self.anr_h

        anr_p: float | None | Unset
        if isinstance(self.anr_p, Unset):
            anr_p = UNSET
        else:
            anr_p = self.anr_p

        bg: None | str | Unset
        if isinstance(self.bg, Unset):
            bg = UNSET
        else:
            bg = self.bg

        bg_chi: None | str | Unset
        if isinstance(self.bg_chi, Unset):
            bg_chi = UNSET
        else:
            bg_chi = self.bg_chi

        bg_eng: None | str | Unset
        if isinstance(self.bg_eng, Unset):
            bg_eng = UNSET
        else:
            bg_eng = self.bg_eng

        bg_ind: None | str | Unset
        if isinstance(self.bg_ind, Unset):
            bg_ind = UNSET
        else:
            bg_ind = self.bg_ind

        born_chi: float | None | Unset
        if isinstance(self.born_chi, Unset):
            born_chi = UNSET
        else:
            born_chi = self.born_chi

        born_else: float | None | Unset
        if isinstance(self.born_else, Unset):
            born_else = UNSET
        else:
            born_else = self.born_else

        born_hk: float | None | Unset
        if isinstance(self.born_hk, Unset):
            born_hk = UNSET
        else:
            born_hk = self.born_hk

        dh_ocm: float | None | Unset
        if isinstance(self.dh_ocm, Unset):
            dh_ocm = UNSET
        else:
            dh_ocm = self.dh_ocm

        dh_ocwm: float | None | Unset
        if isinstance(self.dh_ocwm, Unset):
            dh_ocwm = UNSET
        else:
            dh_ocwm = self.dh_ocwm

        dh_old: float | None | Unset
        if isinstance(self.dh_old, Unset):
            dh_old = UNSET
        else:
            dh_old = self.dh_old

        dh_old_1: None | str | Unset
        if isinstance(self.dh_old_1, Unset):
            dh_old_1 = UNSET
        else:
            dh_old_1 = self.dh_old_1

        dh_old_2: None | str | Unset
        if isinstance(self.dh_old_2, Unset):
            dh_old_2 = UNSET
        else:
            dh_old_2 = self.dh_old_2

        dh_oth: float | None | Unset
        if isinstance(self.dh_oth, Unset):
            dh_oth = UNSET
        else:
            dh_oth = self.dh_oth

        dh_r0: float | None | Unset
        if isinstance(self.dh_r0, Unset):
            dh_r0 = UNSET
        else:
            dh_r0 = self.dh_r0

        dh_r1: float | None | Unset
        if isinstance(self.dh_r1, Unset):
            dh_r1 = UNSET
        else:
            dh_r1 = self.dh_r1

        dh_r3: float | None | Unset
        if isinstance(self.dh_r3, Unset):
            dh_r3 = UNSET
        else:
            dh_r3 = self.dh_r3

        dh_r4: float | None | Unset
        if isinstance(self.dh_r4, Unset):
            dh_r4 = UNSET
        else:
            dh_r4 = self.dh_r4

        dh_r5: float | None | Unset
        if isinstance(self.dh_r5, Unset):
            dh_r5 = UNSET
        else:
            dh_r5 = self.dh_r5

        dh_st: float | None | Unset
        if isinstance(self.dh_st, Unset):
            dh_st = UNSET
        else:
            dh_st = self.dh_st

        dhc_1: float | None | Unset
        if isinstance(self.dhc_1, Unset):
            dhc_1 = UNSET
        else:
            dhc_1 = self.dhc_1

        dhc_2: float | None | Unset
        if isinstance(self.dhc_2, Unset):
            dhc_2 = UNSET
        else:
            dhc_2 = self.dhc_2

        dhc_3: float | None | Unset
        if isinstance(self.dhc_3, Unset):
            dhc_3 = UNSET
        else:
            dhc_3 = self.dhc_3

        dhi_1: float | None | Unset
        if isinstance(self.dhi_1, Unset):
            dhi_1 = UNSET
        else:
            dhi_1 = self.dhi_1

        dhi_2: float | None | Unset
        if isinstance(self.dhi_2, Unset):
            dhi_2 = UNSET
        else:
            dhi_2 = self.dhi_2

        dhi_3: float | None | Unset
        if isinstance(self.dhi_3, Unset):
            dhi_3 = UNSET
        else:
            dhi_3 = self.dhi_3

        dhi_xfdh_1: None | str | Unset
        if isinstance(self.dhi_xfdh_1, Unset):
            dhi_xfdh_1 = UNSET
        else:
            dhi_xfdh_1 = self.dhi_xfdh_1

        dhi_xfdh_2: float | None | Unset
        if isinstance(self.dhi_xfdh_2, Unset):
            dhi_xfdh_2 = UNSET
        else:
            dhi_xfdh_2 = self.dhi_xfdh_2

        dhi_xfdh_3: float | None | Unset
        if isinstance(self.dhi_xfdh_3, Unset):
            dhi_xfdh_3 = UNSET
        else:
            dhi_xfdh_3 = self.dhi_xfdh_3

        dhm_loan: None | str | Unset
        if isinstance(self.dhm_loan, Unset):
            dhm_loan = UNSET
        else:
            dhm_loan = self.dhm_loan

        dhm_lp: None | str | Unset
        if isinstance(self.dhm_lp, Unset):
            dhm_lp = UNSET
        else:
            dhm_lp = self.dhm_lp

        dhm_lr: None | str | Unset
        if isinstance(self.dhm_lr, Unset):
            dhm_lr = UNSET
        else:
            dhm_lr = self.dhm_lr

        dhn_c: float | None | Unset
        if isinstance(self.dhn_c, Unset):
            dhn_c = UNSET
        else:
            dhn_c = self.dhn_c

        dhn_nc: float | None | Unset
        if isinstance(self.dhn_nc, Unset):
            dhn_nc = UNSET
        else:
            dhn_nc = self.dhn_nc

        dhz_1: float | None | Unset
        if isinstance(self.dhz_1, Unset):
            dhz_1 = UNSET
        else:
            dhz_1 = self.dhz_1

        dhz_2: float | None | Unset
        if isinstance(self.dhz_2, Unset):
            dhz_2 = UNSET
        else:
            dhz_2 = self.dhz_2

        dhz_3: float | None | Unset
        if isinstance(self.dhz_3, Unset):
            dhz_3 = UNSET
        else:
            dhz_3 = self.dhz_3

        dm_r: None | str | Unset
        if isinstance(self.dm_r, Unset):
            dm_r = UNSET
        else:
            dm_r = self.dm_r

        dmr_ir: None | str | Unset
        if isinstance(self.dmr_ir, Unset):
            dmr_ir = UNSET
        else:
            dmr_ir = self.dmr_ir

        edu_pri_prepri: float | None | Unset
        if isinstance(self.edu_pri_prepri, Unset):
            edu_pri_prepri = UNSET
        else:
            edu_pri_prepri = self.edu_pri_prepri

        edu_sec: float | None | Unset
        if isinstance(self.edu_sec, Unset):
            edu_sec = UNSET
        else:
            edu_sec = self.edu_sec

        edu_ter: float | None | Unset
        if isinstance(self.edu_ter, Unset):
            edu_ter = UNSET
        else:
            edu_ter = self.edu_ter

        fa_1: float | None | Unset
        if isinstance(self.fa_1, Unset):
            fa_1 = UNSET
        else:
            fa_1 = self.fa_1

        fa_2: float | None | Unset
        if isinstance(self.fa_2, Unset):
            fa_2 = UNSET
        else:
            fa_2 = self.fa_2

        fa_3: float | None | Unset
        if isinstance(self.fa_3, Unset):
            fa_3 = UNSET
        else:
            fa_3 = self.fa_3

        hma: None | str | Unset
        if isinstance(self.hma, Unset):
            hma = UNSET
        else:
            hma = self.hma

        hma_chi: None | str | Unset
        if isinstance(self.hma_chi, Unset):
            hma_chi = UNSET
        else:
            hma_chi = self.hma_chi

        hma_eng: None | str | Unset
        if isinstance(self.hma_eng, Unset):
            hma_eng = UNSET
        else:
            hma_eng = self.hma_eng

        ma_dhn: float | None | Unset
        if isinstance(self.ma_dhn, Unset):
            ma_dhn = UNSET
        else:
            ma_dhn = self.ma_dhn

        ma_f: float | None | Unset
        if isinstance(self.ma_f, Unset):
            ma_f = UNSET
        else:
            ma_f = self.ma_f

        ma_m: float | None | Unset
        if isinstance(self.ma_m, Unset):
            ma_m = UNSET
        else:
            ma_m = self.ma_m

        mearn_xfdhfw_1: float | None | Unset
        if isinstance(self.mearn_xfdhfw_1, Unset):
            mearn_xfdhfw_1 = UNSET
        else:
            mearn_xfdhfw_1 = self.mearn_xfdhfw_1

        mearn_xfdhfw_2: float | None | Unset
        if isinstance(self.mearn_xfdhfw_2, Unset):
            mearn_xfdhfw_2 = UNSET
        else:
            mearn_xfdhfw_2 = self.mearn_xfdhfw_2

        mearn_xfdhfw_3: float | None | Unset
        if isinstance(self.mearn_xfdhfw_3, Unset):
            mearn_xfdhfw_3 = UNSET
        else:
            mearn_xfdhfw_3 = self.mearn_xfdhfw_3

        mearn_xfw_1: float | None | Unset
        if isinstance(self.mearn_xfw_1, Unset):
            mearn_xfw_1 = UNSET
        else:
            mearn_xfw_1 = self.mearn_xfw_1

        mearn_xfw_2: float | None | Unset
        if isinstance(self.mearn_xfw_2, Unset):
            mearn_xfw_2 = UNSET
        else:
            mearn_xfw_2 = self.mearn_xfw_2

        mearn_xfw_3: float | None | Unset
        if isinstance(self.mearn_xfw_3, Unset):
            mearn_xfw_3 = UNSET
        else:
            mearn_xfw_3 = self.mearn_xfw_3

        nm_f: float | None | Unset
        if isinstance(self.nm_f, Unset):
            nm_f = UNSET
        else:
            nm_f = self.nm_f

        nm_m: float | None | Unset
        if isinstance(self.nm_m, Unset):
            nm_m = UNSET
        else:
            nm_m = self.nm_m

        nwp_nonstu: float | None | Unset
        if isinstance(self.nwp_nonstu, Unset):
            nwp_nonstu = UNSET
        else:
            nwp_nonstu = self.nwp_nonstu

        nwp_st: float | None | Unset
        if isinstance(self.nwp_st, Unset):
            nwp_st = UNSET
        else:
            nwp_st = self.nwp_st

        pm_r1: float | None | Unset
        if isinstance(self.pm_r1, Unset):
            pm_r1 = UNSET
        else:
            pm_r1 = self.pm_r1

        pm_r2: float | None | Unset
        if isinstance(self.pm_r2, Unset):
            pm_r2 = UNSET
        else:
            pm_r2 = self.pm_r2

        pm_r3: float | None | Unset
        if isinstance(self.pm_r3, Unset):
            pm_r3 = UNSET
        else:
            pm_r3 = self.pm_r3

        pm_r4: float | None | Unset
        if isinstance(self.pm_r4, Unset):
            pm_r4 = UNSET
        else:
            pm_r4 = self.pm_r4

        s_bus: float | None | Unset
        if isinstance(self.s_bus, Unset):
            s_bus = UNSET
        else:
            s_bus = self.s_bus

        s_dc: float | None | Unset
        if isinstance(self.s_dc, Unset):
            s_dc = UNSET
        else:
            s_dc = self.s_dc

        s_foot: float | None | Unset
        if isinstance(self.s_foot, Unset):
            s_foot = UNSET
        else:
            s_foot = self.s_foot

        s_mtr: float | None | Unset
        if isinstance(self.s_mtr, Unset):
            s_mtr = UNSET
        else:
            s_mtr = self.s_mtr

        s_oth: float | None | Unset
        if isinstance(self.s_oth, Unset):
            s_oth = UNSET
        else:
            s_oth = self.s_oth

        s_sb: float | None | Unset
        if isinstance(self.s_sb, Unset):
            s_sb = UNSET
        else:
            s_sb = self.s_sb

        sr: float | None | Unset
        if isinstance(self.sr, Unset):
            sr = UNSET
        else:
            sr = self.sr

        t_ma: float | None | Unset
        if isinstance(self.t_ma, Unset):
            t_ma = UNSET
        else:
            t_ma = self.t_ma

        t_nwp: float | None | Unset
        if isinstance(self.t_nwp, Unset):
            t_nwp = UNSET
        else:
            t_nwp = self.t_nwp

        t_pop: float | None | Unset
        if isinstance(self.t_pop, Unset):
            t_pop = UNSET
        else:
            t_pop = self.t_pop

        t_wp: float | None | Unset
        if isinstance(self.t_wp, Unset):
            t_wp = UNSET
        else:
            t_wp = self.t_wp

        ul_can: float | None | Unset
        if isinstance(self.ul_can, Unset):
            ul_can = UNSET
        else:
            ul_can = self.ul_can

        ul_eng_oth: float | None | Unset
        if isinstance(self.ul_eng_oth, Unset):
            ul_eng_oth = UNSET
        else:
            ul_eng_oth = self.ul_eng_oth

        ul_put_othchi: float | None | Unset
        if isinstance(self.ul_put_othchi, Unset):
            ul_put_othchi = UNSET
        else:
            ul_put_othchi = self.ul_put_othchi

        whr_1: float | None | Unset
        if isinstance(self.whr_1, Unset):
            whr_1 = UNSET
        else:
            whr_1 = self.whr_1

        whr_2: float | None | Unset
        if isinstance(self.whr_2, Unset):
            whr_2 = UNSET
        else:
            whr_2 = self.whr_2

        whr_3: float | None | Unset
        if isinstance(self.whr_3, Unset):
            whr_3 = UNSET
        else:
            whr_3 = self.whr_3

        whr_xfdh_1: float | None | Unset
        if isinstance(self.whr_xfdh_1, Unset):
            whr_xfdh_1 = UNSET
        else:
            whr_xfdh_1 = self.whr_xfdh_1

        whr_xfdh_2: float | None | Unset
        if isinstance(self.whr_xfdh_2, Unset):
            whr_xfdh_2 = UNSET
        else:
            whr_xfdh_2 = self.whr_xfdh_2

        whr_xfdh_3: float | None | Unset
        if isinstance(self.whr_xfdh_3, Unset):
            whr_xfdh_3 = UNSET
        else:
            whr_xfdh_3 = self.whr_xfdh_3

        wp_a: float | None | Unset
        if isinstance(self.wp_a, Unset):
            wp_a = UNSET
        else:
            wp_a = self.wp_a

        wp_b: float | None | Unset
        if isinstance(self.wp_b, Unset):
            wp_b = UNSET
        else:
            wp_b = self.wp_b

        wp_bus: float | None | Unset
        if isinstance(self.wp_bus, Unset):
            wp_bus = UNSET
        else:
            wp_bus = self.wp_bus

        wp_c: float | None | Unset
        if isinstance(self.wp_c, Unset):
            wp_c = UNSET
        else:
            wp_c = self.wp_c

        wp_d: float | None | Unset
        if isinstance(self.wp_d, Unset):
            wp_d = UNSET
        else:
            wp_d = self.wp_d

        wp_dc: float | None | Unset
        if isinstance(self.wp_dc, Unset):
            wp_dc = UNSET
        else:
            wp_dc = self.wp_dc

        wp_e: float | None | Unset
        if isinstance(self.wp_e, Unset):
            wp_e = UNSET
        else:
            wp_e = self.wp_e

        wp_ee: float | None | Unset
        if isinstance(self.wp_ee, Unset):
            wp_ee = UNSET
        else:
            wp_ee = self.wp_ee

        wp_er: float | None | Unset
        if isinstance(self.wp_er, Unset):
            wp_er = UNSET
        else:
            wp_er = self.wp_er

        wp_f: float | None | Unset
        if isinstance(self.wp_f, Unset):
            wp_f = UNSET
        else:
            wp_f = self.wp_f

        wp_foot: float | None | Unset
        if isinstance(self.wp_foot, Unset):
            wp_foot = UNSET
        else:
            wp_foot = self.wp_foot

        wp_g: float | None | Unset
        if isinstance(self.wp_g, Unset):
            wp_g = UNSET
        else:
            wp_g = self.wp_g

        wp_h: float | None | Unset
        if isinstance(self.wp_h, Unset):
            wp_h = UNSET
        else:
            wp_h = self.wp_h

        wp_i: float | None | Unset
        if isinstance(self.wp_i, Unset):
            wp_i = UNSET
        else:
            wp_i = self.wp_i

        wp_mtr: float | None | Unset
        if isinstance(self.wp_mtr, Unset):
            wp_mtr = UNSET
        else:
            wp_mtr = self.wp_mtr

        wp_oth: float | None | Unset
        if isinstance(self.wp_oth, Unset):
            wp_oth = UNSET
        else:
            wp_oth = self.wp_oth

        wp_plb: float | None | Unset
        if isinstance(self.wp_plb, Unset):
            wp_plb = UNSET
        else:
            wp_plb = self.wp_plb

        wp_se_fw: float | None | Unset
        if isinstance(self.wp_se_fw, Unset):
            wp_se_fw = UNSET
        else:
            wp_se_fw = self.wp_se_fw

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adhz is not UNSET:
            field_dict["adhz"] = adhz
        if age_1 is not UNSET:
            field_dict["age_1"] = age_1
        if age_2 is not UNSET:
            field_dict["age_2"] = age_2
        if age_3 is not UNSET:
            field_dict["age_3"] = age_3
        if age_4 is not UNSET:
            field_dict["age_4"] = age_4
        if anr_h is not UNSET:
            field_dict["anr_h"] = anr_h
        if anr_p is not UNSET:
            field_dict["anr_p"] = anr_p
        if bg is not UNSET:
            field_dict["bg"] = bg
        if bg_chi is not UNSET:
            field_dict["bg_chi"] = bg_chi
        if bg_eng is not UNSET:
            field_dict["bg_eng"] = bg_eng
        if bg_ind is not UNSET:
            field_dict["bg_ind"] = bg_ind
        if born_chi is not UNSET:
            field_dict["born_chi"] = born_chi
        if born_else is not UNSET:
            field_dict["born_else"] = born_else
        if born_hk is not UNSET:
            field_dict["born_hk"] = born_hk
        if dh_ocm is not UNSET:
            field_dict["dh_ocm"] = dh_ocm
        if dh_ocwm is not UNSET:
            field_dict["dh_ocwm"] = dh_ocwm
        if dh_old is not UNSET:
            field_dict["dh_old"] = dh_old
        if dh_old_1 is not UNSET:
            field_dict["dh_old_1"] = dh_old_1
        if dh_old_2 is not UNSET:
            field_dict["dh_old_2"] = dh_old_2
        if dh_oth is not UNSET:
            field_dict["dh_oth"] = dh_oth
        if dh_r0 is not UNSET:
            field_dict["dh_r0"] = dh_r0
        if dh_r1 is not UNSET:
            field_dict["dh_r1"] = dh_r1
        if dh_r3 is not UNSET:
            field_dict["dh_r3"] = dh_r3
        if dh_r4 is not UNSET:
            field_dict["dh_r4"] = dh_r4
        if dh_r5 is not UNSET:
            field_dict["dh_r5"] = dh_r5
        if dh_st is not UNSET:
            field_dict["dh_st"] = dh_st
        if dhc_1 is not UNSET:
            field_dict["dhc_1"] = dhc_1
        if dhc_2 is not UNSET:
            field_dict["dhc_2"] = dhc_2
        if dhc_3 is not UNSET:
            field_dict["dhc_3"] = dhc_3
        if dhi_1 is not UNSET:
            field_dict["dhi_1"] = dhi_1
        if dhi_2 is not UNSET:
            field_dict["dhi_2"] = dhi_2
        if dhi_3 is not UNSET:
            field_dict["dhi_3"] = dhi_3
        if dhi_xfdh_1 is not UNSET:
            field_dict["dhi_xfdh_1"] = dhi_xfdh_1
        if dhi_xfdh_2 is not UNSET:
            field_dict["dhi_xfdh_2"] = dhi_xfdh_2
        if dhi_xfdh_3 is not UNSET:
            field_dict["dhi_xfdh_3"] = dhi_xfdh_3
        if dhm_loan is not UNSET:
            field_dict["dhm_loan"] = dhm_loan
        if dhm_lp is not UNSET:
            field_dict["dhm_lp"] = dhm_lp
        if dhm_lr is not UNSET:
            field_dict["dhm_lr"] = dhm_lr
        if dhn_c is not UNSET:
            field_dict["dhn_c"] = dhn_c
        if dhn_nc is not UNSET:
            field_dict["dhn_nc"] = dhn_nc
        if dhz_1 is not UNSET:
            field_dict["dhz_1"] = dhz_1
        if dhz_2 is not UNSET:
            field_dict["dhz_2"] = dhz_2
        if dhz_3 is not UNSET:
            field_dict["dhz_3"] = dhz_3
        if dm_r is not UNSET:
            field_dict["dm_r"] = dm_r
        if dmr_ir is not UNSET:
            field_dict["dmr_ir"] = dmr_ir
        if edu_pri_prepri is not UNSET:
            field_dict["edu_pri_prepri"] = edu_pri_prepri
        if edu_sec is not UNSET:
            field_dict["edu_sec"] = edu_sec
        if edu_ter is not UNSET:
            field_dict["edu_ter"] = edu_ter
        if fa_1 is not UNSET:
            field_dict["fa_1"] = fa_1
        if fa_2 is not UNSET:
            field_dict["fa_2"] = fa_2
        if fa_3 is not UNSET:
            field_dict["fa_3"] = fa_3
        if hma is not UNSET:
            field_dict["hma"] = hma
        if hma_chi is not UNSET:
            field_dict["hma_chi"] = hma_chi
        if hma_eng is not UNSET:
            field_dict["hma_eng"] = hma_eng
        if ma_dhn is not UNSET:
            field_dict["ma_dhn"] = ma_dhn
        if ma_f is not UNSET:
            field_dict["ma_f"] = ma_f
        if ma_m is not UNSET:
            field_dict["ma_m"] = ma_m
        if mearn_xfdhfw_1 is not UNSET:
            field_dict["mearn_xfdhfw_1"] = mearn_xfdhfw_1
        if mearn_xfdhfw_2 is not UNSET:
            field_dict["mearn_xfdhfw_2"] = mearn_xfdhfw_2
        if mearn_xfdhfw_3 is not UNSET:
            field_dict["mearn_xfdhfw_3"] = mearn_xfdhfw_3
        if mearn_xfw_1 is not UNSET:
            field_dict["mearn_xfw_1"] = mearn_xfw_1
        if mearn_xfw_2 is not UNSET:
            field_dict["mearn_xfw_2"] = mearn_xfw_2
        if mearn_xfw_3 is not UNSET:
            field_dict["mearn_xfw_3"] = mearn_xfw_3
        if nm_f is not UNSET:
            field_dict["nm_f"] = nm_f
        if nm_m is not UNSET:
            field_dict["nm_m"] = nm_m
        if nwp_nonstu is not UNSET:
            field_dict["nwp_nonstu"] = nwp_nonstu
        if nwp_st is not UNSET:
            field_dict["nwp_st"] = nwp_st
        if pm_r1 is not UNSET:
            field_dict["pm_r1"] = pm_r1
        if pm_r2 is not UNSET:
            field_dict["pm_r2"] = pm_r2
        if pm_r3 is not UNSET:
            field_dict["pm_r3"] = pm_r3
        if pm_r4 is not UNSET:
            field_dict["pm_r4"] = pm_r4
        if s_bus is not UNSET:
            field_dict["s_bus"] = s_bus
        if s_dc is not UNSET:
            field_dict["s_dc"] = s_dc
        if s_foot is not UNSET:
            field_dict["s_foot"] = s_foot
        if s_mtr is not UNSET:
            field_dict["s_mtr"] = s_mtr
        if s_oth is not UNSET:
            field_dict["s_oth"] = s_oth
        if s_sb is not UNSET:
            field_dict["s_sb"] = s_sb
        if sr is not UNSET:
            field_dict["sr"] = sr
        if t_ma is not UNSET:
            field_dict["t_ma"] = t_ma
        if t_nwp is not UNSET:
            field_dict["t_nwp"] = t_nwp
        if t_pop is not UNSET:
            field_dict["t_pop"] = t_pop
        if t_wp is not UNSET:
            field_dict["t_wp"] = t_wp
        if ul_can is not UNSET:
            field_dict["ul_can"] = ul_can
        if ul_eng_oth is not UNSET:
            field_dict["ul_eng_oth"] = ul_eng_oth
        if ul_put_othchi is not UNSET:
            field_dict["ul_put_othchi"] = ul_put_othchi
        if whr_1 is not UNSET:
            field_dict["whr_1"] = whr_1
        if whr_2 is not UNSET:
            field_dict["whr_2"] = whr_2
        if whr_3 is not UNSET:
            field_dict["whr_3"] = whr_3
        if whr_xfdh_1 is not UNSET:
            field_dict["whr_xfdh_1"] = whr_xfdh_1
        if whr_xfdh_2 is not UNSET:
            field_dict["whr_xfdh_2"] = whr_xfdh_2
        if whr_xfdh_3 is not UNSET:
            field_dict["whr_xfdh_3"] = whr_xfdh_3
        if wp_a is not UNSET:
            field_dict["wp_a"] = wp_a
        if wp_b is not UNSET:
            field_dict["wp_b"] = wp_b
        if wp_bus is not UNSET:
            field_dict["wp_bus"] = wp_bus
        if wp_c is not UNSET:
            field_dict["wp_c"] = wp_c
        if wp_d is not UNSET:
            field_dict["wp_d"] = wp_d
        if wp_dc is not UNSET:
            field_dict["wp_dc"] = wp_dc
        if wp_e is not UNSET:
            field_dict["wp_e"] = wp_e
        if wp_ee is not UNSET:
            field_dict["wp_ee"] = wp_ee
        if wp_er is not UNSET:
            field_dict["wp_er"] = wp_er
        if wp_f is not UNSET:
            field_dict["wp_f"] = wp_f
        if wp_foot is not UNSET:
            field_dict["wp_foot"] = wp_foot
        if wp_g is not UNSET:
            field_dict["wp_g"] = wp_g
        if wp_h is not UNSET:
            field_dict["wp_h"] = wp_h
        if wp_i is not UNSET:
            field_dict["wp_i"] = wp_i
        if wp_mtr is not UNSET:
            field_dict["wp_mtr"] = wp_mtr
        if wp_oth is not UNSET:
            field_dict["wp_oth"] = wp_oth
        if wp_plb is not UNSET:
            field_dict["wp_plb"] = wp_plb
        if wp_se_fw is not UNSET:
            field_dict["wp_se_fw"] = wp_se_fw
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_adhz(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        adhz = _parse_adhz(d.pop("adhz", UNSET))

        def _parse_age_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        age_1 = _parse_age_1(d.pop("age_1", UNSET))

        def _parse_age_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        age_2 = _parse_age_2(d.pop("age_2", UNSET))

        def _parse_age_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        age_3 = _parse_age_3(d.pop("age_3", UNSET))

        def _parse_age_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        age_4 = _parse_age_4(d.pop("age_4", UNSET))

        def _parse_anr_h(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        anr_h = _parse_anr_h(d.pop("anr_h", UNSET))

        def _parse_anr_p(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        anr_p = _parse_anr_p(d.pop("anr_p", UNSET))

        def _parse_bg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bg = _parse_bg(d.pop("bg", UNSET))

        def _parse_bg_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bg_chi = _parse_bg_chi(d.pop("bg_chi", UNSET))

        def _parse_bg_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bg_eng = _parse_bg_eng(d.pop("bg_eng", UNSET))

        def _parse_bg_ind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bg_ind = _parse_bg_ind(d.pop("bg_ind", UNSET))

        def _parse_born_chi(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        born_chi = _parse_born_chi(d.pop("born_chi", UNSET))

        def _parse_born_else(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        born_else = _parse_born_else(d.pop("born_else", UNSET))

        def _parse_born_hk(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        born_hk = _parse_born_hk(d.pop("born_hk", UNSET))

        def _parse_dh_ocm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_ocm = _parse_dh_ocm(d.pop("dh_ocm", UNSET))

        def _parse_dh_ocwm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_ocwm = _parse_dh_ocwm(d.pop("dh_ocwm", UNSET))

        def _parse_dh_old(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_old = _parse_dh_old(d.pop("dh_old", UNSET))

        def _parse_dh_old_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_old_1 = _parse_dh_old_1(d.pop("dh_old_1", UNSET))

        def _parse_dh_old_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_old_2 = _parse_dh_old_2(d.pop("dh_old_2", UNSET))

        def _parse_dh_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_oth = _parse_dh_oth(d.pop("dh_oth", UNSET))

        def _parse_dh_r0(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_r0 = _parse_dh_r0(d.pop("dh_r0", UNSET))

        def _parse_dh_r1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_r1 = _parse_dh_r1(d.pop("dh_r1", UNSET))

        def _parse_dh_r3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_r3 = _parse_dh_r3(d.pop("dh_r3", UNSET))

        def _parse_dh_r4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_r4 = _parse_dh_r4(d.pop("dh_r4", UNSET))

        def _parse_dh_r5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_r5 = _parse_dh_r5(d.pop("dh_r5", UNSET))

        def _parse_dh_st(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_st = _parse_dh_st(d.pop("dh_st", UNSET))

        def _parse_dhc_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_1 = _parse_dhc_1(d.pop("dhc_1", UNSET))

        def _parse_dhc_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_2 = _parse_dhc_2(d.pop("dhc_2", UNSET))

        def _parse_dhc_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_3 = _parse_dhc_3(d.pop("dhc_3", UNSET))

        def _parse_dhi_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_1 = _parse_dhi_1(d.pop("dhi_1", UNSET))

        def _parse_dhi_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_2 = _parse_dhi_2(d.pop("dhi_2", UNSET))

        def _parse_dhi_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_3 = _parse_dhi_3(d.pop("dhi_3", UNSET))

        def _parse_dhi_xfdh_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhi_xfdh_1 = _parse_dhi_xfdh_1(d.pop("dhi_xfdh_1", UNSET))

        def _parse_dhi_xfdh_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_xfdh_2 = _parse_dhi_xfdh_2(d.pop("dhi_xfdh_2", UNSET))

        def _parse_dhi_xfdh_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_xfdh_3 = _parse_dhi_xfdh_3(d.pop("dhi_xfdh_3", UNSET))

        def _parse_dhm_loan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhm_loan = _parse_dhm_loan(d.pop("dhm_loan", UNSET))

        def _parse_dhm_lp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhm_lp = _parse_dhm_lp(d.pop("dhm_lp", UNSET))

        def _parse_dhm_lr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhm_lr = _parse_dhm_lr(d.pop("dhm_lr", UNSET))

        def _parse_dhn_c(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhn_c = _parse_dhn_c(d.pop("dhn_c", UNSET))

        def _parse_dhn_nc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhn_nc = _parse_dhn_nc(d.pop("dhn_nc", UNSET))

        def _parse_dhz_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_1 = _parse_dhz_1(d.pop("dhz_1", UNSET))

        def _parse_dhz_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_2 = _parse_dhz_2(d.pop("dhz_2", UNSET))

        def _parse_dhz_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_3 = _parse_dhz_3(d.pop("dhz_3", UNSET))

        def _parse_dm_r(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dm_r = _parse_dm_r(d.pop("dm_r", UNSET))

        def _parse_dmr_ir(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dmr_ir = _parse_dmr_ir(d.pop("dmr_ir", UNSET))

        def _parse_edu_pri_prepri(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_pri_prepri = _parse_edu_pri_prepri(d.pop("edu_pri_prepri", UNSET))

        def _parse_edu_sec(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_sec = _parse_edu_sec(d.pop("edu_sec", UNSET))

        def _parse_edu_ter(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_ter = _parse_edu_ter(d.pop("edu_ter", UNSET))

        def _parse_fa_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fa_1 = _parse_fa_1(d.pop("fa_1", UNSET))

        def _parse_fa_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fa_2 = _parse_fa_2(d.pop("fa_2", UNSET))

        def _parse_fa_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fa_3 = _parse_fa_3(d.pop("fa_3", UNSET))

        def _parse_hma(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hma = _parse_hma(d.pop("hma", UNSET))

        def _parse_hma_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hma_chi = _parse_hma_chi(d.pop("hma_chi", UNSET))

        def _parse_hma_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hma_eng = _parse_hma_eng(d.pop("hma_eng", UNSET))

        def _parse_ma_dhn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ma_dhn = _parse_ma_dhn(d.pop("ma_dhn", UNSET))

        def _parse_ma_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ma_f = _parse_ma_f(d.pop("ma_f", UNSET))

        def _parse_ma_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ma_m = _parse_ma_m(d.pop("ma_m", UNSET))

        def _parse_mearn_xfdhfw_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdhfw_1 = _parse_mearn_xfdhfw_1(d.pop("mearn_xfdhfw_1", UNSET))

        def _parse_mearn_xfdhfw_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdhfw_2 = _parse_mearn_xfdhfw_2(d.pop("mearn_xfdhfw_2", UNSET))

        def _parse_mearn_xfdhfw_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdhfw_3 = _parse_mearn_xfdhfw_3(d.pop("mearn_xfdhfw_3", UNSET))

        def _parse_mearn_xfw_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfw_1 = _parse_mearn_xfw_1(d.pop("mearn_xfw_1", UNSET))

        def _parse_mearn_xfw_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfw_2 = _parse_mearn_xfw_2(d.pop("mearn_xfw_2", UNSET))

        def _parse_mearn_xfw_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfw_3 = _parse_mearn_xfw_3(d.pop("mearn_xfw_3", UNSET))

        def _parse_nm_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nm_f = _parse_nm_f(d.pop("nm_f", UNSET))

        def _parse_nm_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nm_m = _parse_nm_m(d.pop("nm_m", UNSET))

        def _parse_nwp_nonstu(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nwp_nonstu = _parse_nwp_nonstu(d.pop("nwp_nonstu", UNSET))

        def _parse_nwp_st(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nwp_st = _parse_nwp_st(d.pop("nwp_st", UNSET))

        def _parse_pm_r1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_r1 = _parse_pm_r1(d.pop("pm_r1", UNSET))

        def _parse_pm_r2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_r2 = _parse_pm_r2(d.pop("pm_r2", UNSET))

        def _parse_pm_r3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_r3 = _parse_pm_r3(d.pop("pm_r3", UNSET))

        def _parse_pm_r4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_r4 = _parse_pm_r4(d.pop("pm_r4", UNSET))

        def _parse_s_bus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        s_bus = _parse_s_bus(d.pop("s_bus", UNSET))

        def _parse_s_dc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        s_dc = _parse_s_dc(d.pop("s_dc", UNSET))

        def _parse_s_foot(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        s_foot = _parse_s_foot(d.pop("s_foot", UNSET))

        def _parse_s_mtr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        s_mtr = _parse_s_mtr(d.pop("s_mtr", UNSET))

        def _parse_s_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        s_oth = _parse_s_oth(d.pop("s_oth", UNSET))

        def _parse_s_sb(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        s_sb = _parse_s_sb(d.pop("s_sb", UNSET))

        def _parse_sr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sr = _parse_sr(d.pop("sr", UNSET))

        def _parse_t_ma(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_ma = _parse_t_ma(d.pop("t_ma", UNSET))

        def _parse_t_nwp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_nwp = _parse_t_nwp(d.pop("t_nwp", UNSET))

        def _parse_t_pop(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_pop = _parse_t_pop(d.pop("t_pop", UNSET))

        def _parse_t_wp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_wp = _parse_t_wp(d.pop("t_wp", UNSET))

        def _parse_ul_can(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ul_can = _parse_ul_can(d.pop("ul_can", UNSET))

        def _parse_ul_eng_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ul_eng_oth = _parse_ul_eng_oth(d.pop("ul_eng_oth", UNSET))

        def _parse_ul_put_othchi(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ul_put_othchi = _parse_ul_put_othchi(d.pop("ul_put_othchi", UNSET))

        def _parse_whr_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        whr_1 = _parse_whr_1(d.pop("whr_1", UNSET))

        def _parse_whr_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        whr_2 = _parse_whr_2(d.pop("whr_2", UNSET))

        def _parse_whr_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        whr_3 = _parse_whr_3(d.pop("whr_3", UNSET))

        def _parse_whr_xfdh_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        whr_xfdh_1 = _parse_whr_xfdh_1(d.pop("whr_xfdh_1", UNSET))

        def _parse_whr_xfdh_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        whr_xfdh_2 = _parse_whr_xfdh_2(d.pop("whr_xfdh_2", UNSET))

        def _parse_whr_xfdh_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        whr_xfdh_3 = _parse_whr_xfdh_3(d.pop("whr_xfdh_3", UNSET))

        def _parse_wp_a(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_a = _parse_wp_a(d.pop("wp_a", UNSET))

        def _parse_wp_b(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_b = _parse_wp_b(d.pop("wp_b", UNSET))

        def _parse_wp_bus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_bus = _parse_wp_bus(d.pop("wp_bus", UNSET))

        def _parse_wp_c(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_c = _parse_wp_c(d.pop("wp_c", UNSET))

        def _parse_wp_d(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_d = _parse_wp_d(d.pop("wp_d", UNSET))

        def _parse_wp_dc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_dc = _parse_wp_dc(d.pop("wp_dc", UNSET))

        def _parse_wp_e(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_e = _parse_wp_e(d.pop("wp_e", UNSET))

        def _parse_wp_ee(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_ee = _parse_wp_ee(d.pop("wp_ee", UNSET))

        def _parse_wp_er(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_er = _parse_wp_er(d.pop("wp_er", UNSET))

        def _parse_wp_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_f = _parse_wp_f(d.pop("wp_f", UNSET))

        def _parse_wp_foot(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_foot = _parse_wp_foot(d.pop("wp_foot", UNSET))

        def _parse_wp_g(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_g = _parse_wp_g(d.pop("wp_g", UNSET))

        def _parse_wp_h(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_h = _parse_wp_h(d.pop("wp_h", UNSET))

        def _parse_wp_i(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_i = _parse_wp_i(d.pop("wp_i", UNSET))

        def _parse_wp_mtr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_mtr = _parse_wp_mtr(d.pop("wp_mtr", UNSET))

        def _parse_wp_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_oth = _parse_wp_oth(d.pop("wp_oth", UNSET))

        def _parse_wp_plb(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_plb = _parse_wp_plb(d.pop("wp_plb", UNSET))

        def _parse_wp_se_fw(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_se_fw = _parse_wp_se_fw(d.pop("wp_se_fw", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            adhz=adhz,
            age_1=age_1,
            age_2=age_2,
            age_3=age_3,
            age_4=age_4,
            anr_h=anr_h,
            anr_p=anr_p,
            bg=bg,
            bg_chi=bg_chi,
            bg_eng=bg_eng,
            bg_ind=bg_ind,
            born_chi=born_chi,
            born_else=born_else,
            born_hk=born_hk,
            dh_ocm=dh_ocm,
            dh_ocwm=dh_ocwm,
            dh_old=dh_old,
            dh_old_1=dh_old_1,
            dh_old_2=dh_old_2,
            dh_oth=dh_oth,
            dh_r0=dh_r0,
            dh_r1=dh_r1,
            dh_r3=dh_r3,
            dh_r4=dh_r4,
            dh_r5=dh_r5,
            dh_st=dh_st,
            dhc_1=dhc_1,
            dhc_2=dhc_2,
            dhc_3=dhc_3,
            dhi_1=dhi_1,
            dhi_2=dhi_2,
            dhi_3=dhi_3,
            dhi_xfdh_1=dhi_xfdh_1,
            dhi_xfdh_2=dhi_xfdh_2,
            dhi_xfdh_3=dhi_xfdh_3,
            dhm_loan=dhm_loan,
            dhm_lp=dhm_lp,
            dhm_lr=dhm_lr,
            dhn_c=dhn_c,
            dhn_nc=dhn_nc,
            dhz_1=dhz_1,
            dhz_2=dhz_2,
            dhz_3=dhz_3,
            dm_r=dm_r,
            dmr_ir=dmr_ir,
            edu_pri_prepri=edu_pri_prepri,
            edu_sec=edu_sec,
            edu_ter=edu_ter,
            fa_1=fa_1,
            fa_2=fa_2,
            fa_3=fa_3,
            hma=hma,
            hma_chi=hma_chi,
            hma_eng=hma_eng,
            ma_dhn=ma_dhn,
            ma_f=ma_f,
            ma_m=ma_m,
            mearn_xfdhfw_1=mearn_xfdhfw_1,
            mearn_xfdhfw_2=mearn_xfdhfw_2,
            mearn_xfdhfw_3=mearn_xfdhfw_3,
            mearn_xfw_1=mearn_xfw_1,
            mearn_xfw_2=mearn_xfw_2,
            mearn_xfw_3=mearn_xfw_3,
            nm_f=nm_f,
            nm_m=nm_m,
            nwp_nonstu=nwp_nonstu,
            nwp_st=nwp_st,
            pm_r1=pm_r1,
            pm_r2=pm_r2,
            pm_r3=pm_r3,
            pm_r4=pm_r4,
            s_bus=s_bus,
            s_dc=s_dc,
            s_foot=s_foot,
            s_mtr=s_mtr,
            s_oth=s_oth,
            s_sb=s_sb,
            sr=sr,
            t_ma=t_ma,
            t_nwp=t_nwp,
            t_pop=t_pop,
            t_wp=t_wp,
            ul_can=ul_can,
            ul_eng_oth=ul_eng_oth,
            ul_put_othchi=ul_put_othchi,
            whr_1=whr_1,
            whr_2=whr_2,
            whr_3=whr_3,
            whr_xfdh_1=whr_xfdh_1,
            whr_xfdh_2=whr_xfdh_2,
            whr_xfdh_3=whr_xfdh_3,
            wp_a=wp_a,
            wp_b=wp_b,
            wp_bus=wp_bus,
            wp_c=wp_c,
            wp_d=wp_d,
            wp_dc=wp_dc,
            wp_e=wp_e,
            wp_ee=wp_ee,
            wp_er=wp_er,
            wp_f=wp_f,
            wp_foot=wp_foot,
            wp_g=wp_g,
            wp_h=wp_h,
            wp_i=wp_i,
            wp_mtr=wp_mtr,
            wp_oth=wp_oth,
            wp_plb=wp_plb,
            wp_se_fw=wp_se_fw,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
