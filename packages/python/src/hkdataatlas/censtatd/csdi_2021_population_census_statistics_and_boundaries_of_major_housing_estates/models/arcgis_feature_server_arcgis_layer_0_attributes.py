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
        age_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        born_chi (float | None | Unset): Publisher field type: esriFieldTypeDouble
        born_else (None | str | Unset): Publisher field type: esriFieldTypeString
        born_hk (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_nc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_re (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_sb_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_sb_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_sb_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_sb_4 (None | str | Unset): Publisher field type: esriFieldTypeString
        dhi_sb_e1 (None | str | Unset): Publisher field type: esriFieldTypeString
        dhi_sb_e2 (None | str | Unset): Publisher field type: esriFieldTypeString
        dhi_sb_e3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_sb_e4 (None | str | Unset): Publisher field type: esriFieldTypeString
        dhm_loan (None | str | Unset): Publisher field type: esriFieldTypeString
        dhm_lr (None | str | Unset): Publisher field type: esriFieldTypeString
        dhz_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_5 (None | str | Unset): Publisher field type: esriFieldTypeString
        dhz_6 (None | str | Unset): Publisher field type: esriFieldTypeString
        dm_r (None | str | Unset): Publisher field type: esriFieldTypeString
        dmr_ir (None | str | Unset): Publisher field type: esriFieldTypeString
        edu_pri_be (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_psec (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_sec (float | None | Unset): Publisher field type: esriFieldTypeDouble
        estate (float | None | Unset): Publisher field type: esriFieldTypeDouble
        estate_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        estate_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        ethn_chi (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ethn_ind (None | str | Unset): Publisher field type: esriFieldTypeString
        ethn_oth (None | str | Unset): Publisher field type: esriFieldTypeString
        ethn_phi (None | str | Unset): Publisher field type: esriFieldTypeString
        ethn_wh (None | str | Unset): Publisher field type: esriFieldTypeString
        fa_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ma_econhh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ma_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ma_hh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ma_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_sb_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_sb_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_sb_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfw_sb_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfw_sb_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfw_sb_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_m_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_ma_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_nm_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_nm_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_wds_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_wds_m (None | str | Unset): Publisher field type: esriFieldTypeString
        nwp_care (None | str | Unset): Publisher field type: esriFieldTypeString
        nwp_hm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nwp_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nwp_re (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nwp_st (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pls_diff_hk (None | str | Unset): Publisher field type: esriFieldTypeString
        pls_diff_kln (None | str | Unset): Publisher field type: esriFieldTypeString
        pls_diff_nt (None | str | Unset): Publisher field type: esriFieldTypeString
        pls_same (None | str | Unset): Publisher field type: esriFieldTypeString
        plw_diff_hk (None | str | Unset): Publisher field type: esriFieldTypeString
        plw_diff_kln (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_diff_nt (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_diff_oth (None | str | Unset): Publisher field type: esriFieldTypeString
        plw_hm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_nofix (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_out (None | str | Unset): Publisher field type: esriFieldTypeString
        plw_same (None | str | Unset): Publisher field type: esriFieldTypeString
        pop_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pop_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        readchi_ablepctn (float | None | Unset): Publisher field type: esriFieldTypeDouble
        readeng_ablepctn (float | None | Unset): Publisher field type: esriFieldTypeDouble
        s_diff_oth (None | str | Unset): Publisher field type: esriFieldTypeString
        sr (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_ma (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_mmearn (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_mmearn_xfdh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_nwp (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_pop (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_wp (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ul_can (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ul_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        ul_oth (None | str | Unset): Publisher field type: esriFieldTypeString
        ul_othchi (None | str | Unset): Publisher field type: esriFieldTypeString
        ul_put (None | str | Unset): Publisher field type: esriFieldTypeString
        whr_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_6 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_a (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_b (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_c (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_d (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_e (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_ee (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_er (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_f (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_fw (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_g (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_h (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_i (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_j (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_k (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_l (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_m (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_n (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_o (None | str | Unset): Publisher field type: esriFieldTypeString
        wp_p (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_q (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_r (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_s (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_se (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_t (None | str | Unset): Publisher field type: esriFieldTypeString
        writechi_ablepctn (float | None | Unset): Publisher field type: esriFieldTypeDouble
        writeeng_ablepctn (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    adhz: float | None | Unset = UNSET
    age_1: float | None | Unset = UNSET
    age_2: float | None | Unset = UNSET
    age_3: float | None | Unset = UNSET
    age_4: float | None | Unset = UNSET
    age_5: float | None | Unset = UNSET
    born_chi: float | None | Unset = UNSET
    born_else: None | str | Unset = UNSET
    born_hk: float | None | Unset = UNSET
    dh: float | None | Unset = UNSET
    dhc_nc: float | None | Unset = UNSET
    dhc_oth: float | None | Unset = UNSET
    dhc_re: float | None | Unset = UNSET
    dhi_sb_1: float | None | Unset = UNSET
    dhi_sb_2: float | None | Unset = UNSET
    dhi_sb_3: float | None | Unset = UNSET
    dhi_sb_4: None | str | Unset = UNSET
    dhi_sb_e1: None | str | Unset = UNSET
    dhi_sb_e2: None | str | Unset = UNSET
    dhi_sb_e3: float | None | Unset = UNSET
    dhi_sb_e4: None | str | Unset = UNSET
    dhm_loan: None | str | Unset = UNSET
    dhm_lr: None | str | Unset = UNSET
    dhz_1: float | None | Unset = UNSET
    dhz_2: float | None | Unset = UNSET
    dhz_3: float | None | Unset = UNSET
    dhz_4: float | None | Unset = UNSET
    dhz_5: None | str | Unset = UNSET
    dhz_6: None | str | Unset = UNSET
    dm_r: None | str | Unset = UNSET
    dmr_ir: None | str | Unset = UNSET
    edu_pri_be: float | None | Unset = UNSET
    edu_psec: float | None | Unset = UNSET
    edu_sec: float | None | Unset = UNSET
    estate: float | None | Unset = UNSET
    estate_chi: None | str | Unset = UNSET
    estate_eng: None | str | Unset = UNSET
    ethn_chi: float | None | Unset = UNSET
    ethn_ind: None | str | Unset = UNSET
    ethn_oth: None | str | Unset = UNSET
    ethn_phi: None | str | Unset = UNSET
    ethn_wh: None | str | Unset = UNSET
    fa_m: float | None | Unset = UNSET
    ma_econhh: float | None | Unset = UNSET
    ma_f: float | None | Unset = UNSET
    ma_hh: float | None | Unset = UNSET
    ma_m: float | None | Unset = UNSET
    mearn_xfdhfw_sb_1: float | None | Unset = UNSET
    mearn_xfdhfw_sb_2: float | None | Unset = UNSET
    mearn_xfdhfw_sb_3: float | None | Unset = UNSET
    mearn_xfw_sb_1: float | None | Unset = UNSET
    mearn_xfw_sb_2: float | None | Unset = UNSET
    mearn_xfw_sb_3: float | None | Unset = UNSET
    ms_m_f: float | None | Unset = UNSET
    ms_ma_m: float | None | Unset = UNSET
    ms_nm_f: float | None | Unset = UNSET
    ms_nm_m: float | None | Unset = UNSET
    ms_wds_f: float | None | Unset = UNSET
    ms_wds_m: None | str | Unset = UNSET
    nwp_care: None | str | Unset = UNSET
    nwp_hm: float | None | Unset = UNSET
    nwp_oth: float | None | Unset = UNSET
    nwp_re: float | None | Unset = UNSET
    nwp_st: float | None | Unset = UNSET
    pls_diff_hk: None | str | Unset = UNSET
    pls_diff_kln: None | str | Unset = UNSET
    pls_diff_nt: None | str | Unset = UNSET
    pls_same: None | str | Unset = UNSET
    plw_diff_hk: None | str | Unset = UNSET
    plw_diff_kln: float | None | Unset = UNSET
    plw_diff_nt: float | None | Unset = UNSET
    plw_diff_oth: None | str | Unset = UNSET
    plw_hm: float | None | Unset = UNSET
    plw_nofix: float | None | Unset = UNSET
    plw_out: None | str | Unset = UNSET
    plw_same: None | str | Unset = UNSET
    pop_f: float | None | Unset = UNSET
    pop_m: float | None | Unset = UNSET
    readchi_ablepctn: float | None | Unset = UNSET
    readeng_ablepctn: float | None | Unset = UNSET
    s_diff_oth: None | str | Unset = UNSET
    sr: float | None | Unset = UNSET
    t_ma: float | None | Unset = UNSET
    t_mmearn: float | None | Unset = UNSET
    t_mmearn_xfdh: float | None | Unset = UNSET
    t_nwp: float | None | Unset = UNSET
    t_pop: float | None | Unset = UNSET
    t_wp: float | None | Unset = UNSET
    ul_can: float | None | Unset = UNSET
    ul_eng: None | str | Unset = UNSET
    ul_oth: None | str | Unset = UNSET
    ul_othchi: None | str | Unset = UNSET
    ul_put: None | str | Unset = UNSET
    whr_1: float | None | Unset = UNSET
    whr_2: float | None | Unset = UNSET
    whr_3: float | None | Unset = UNSET
    whr_4: float | None | Unset = UNSET
    whr_5: float | None | Unset = UNSET
    whr_6: float | None | Unset = UNSET
    wp_a: None | str | Unset = UNSET
    wp_b: None | str | Unset = UNSET
    wp_c: float | None | Unset = UNSET
    wp_d: float | None | Unset = UNSET
    wp_e: float | None | Unset = UNSET
    wp_ee: float | None | Unset = UNSET
    wp_er: None | str | Unset = UNSET
    wp_f: None | str | Unset = UNSET
    wp_fw: None | str | Unset = UNSET
    wp_g: None | str | Unset = UNSET
    wp_h: float | None | Unset = UNSET
    wp_i: None | str | Unset = UNSET
    wp_j: None | str | Unset = UNSET
    wp_k: float | None | Unset = UNSET
    wp_l: float | None | Unset = UNSET
    wp_m: None | str | Unset = UNSET
    wp_n: None | str | Unset = UNSET
    wp_o: None | str | Unset = UNSET
    wp_p: float | None | Unset = UNSET
    wp_q: float | None | Unset = UNSET
    wp_r: float | None | Unset = UNSET
    wp_s: float | None | Unset = UNSET
    wp_se: float | None | Unset = UNSET
    wp_t: None | str | Unset = UNSET
    writechi_ablepctn: float | None | Unset = UNSET
    writeeng_ablepctn: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
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

        age_5: float | None | Unset
        if isinstance(self.age_5, Unset):
            age_5 = UNSET
        else:
            age_5 = self.age_5

        born_chi: float | None | Unset
        if isinstance(self.born_chi, Unset):
            born_chi = UNSET
        else:
            born_chi = self.born_chi

        born_else: None | str | Unset
        if isinstance(self.born_else, Unset):
            born_else = UNSET
        else:
            born_else = self.born_else

        born_hk: float | None | Unset
        if isinstance(self.born_hk, Unset):
            born_hk = UNSET
        else:
            born_hk = self.born_hk

        dh: float | None | Unset
        if isinstance(self.dh, Unset):
            dh = UNSET
        else:
            dh = self.dh

        dhc_nc: float | None | Unset
        if isinstance(self.dhc_nc, Unset):
            dhc_nc = UNSET
        else:
            dhc_nc = self.dhc_nc

        dhc_oth: float | None | Unset
        if isinstance(self.dhc_oth, Unset):
            dhc_oth = UNSET
        else:
            dhc_oth = self.dhc_oth

        dhc_re: float | None | Unset
        if isinstance(self.dhc_re, Unset):
            dhc_re = UNSET
        else:
            dhc_re = self.dhc_re

        dhi_sb_1: float | None | Unset
        if isinstance(self.dhi_sb_1, Unset):
            dhi_sb_1 = UNSET
        else:
            dhi_sb_1 = self.dhi_sb_1

        dhi_sb_2: float | None | Unset
        if isinstance(self.dhi_sb_2, Unset):
            dhi_sb_2 = UNSET
        else:
            dhi_sb_2 = self.dhi_sb_2

        dhi_sb_3: float | None | Unset
        if isinstance(self.dhi_sb_3, Unset):
            dhi_sb_3 = UNSET
        else:
            dhi_sb_3 = self.dhi_sb_3

        dhi_sb_4: None | str | Unset
        if isinstance(self.dhi_sb_4, Unset):
            dhi_sb_4 = UNSET
        else:
            dhi_sb_4 = self.dhi_sb_4

        dhi_sb_e1: None | str | Unset
        if isinstance(self.dhi_sb_e1, Unset):
            dhi_sb_e1 = UNSET
        else:
            dhi_sb_e1 = self.dhi_sb_e1

        dhi_sb_e2: None | str | Unset
        if isinstance(self.dhi_sb_e2, Unset):
            dhi_sb_e2 = UNSET
        else:
            dhi_sb_e2 = self.dhi_sb_e2

        dhi_sb_e3: float | None | Unset
        if isinstance(self.dhi_sb_e3, Unset):
            dhi_sb_e3 = UNSET
        else:
            dhi_sb_e3 = self.dhi_sb_e3

        dhi_sb_e4: None | str | Unset
        if isinstance(self.dhi_sb_e4, Unset):
            dhi_sb_e4 = UNSET
        else:
            dhi_sb_e4 = self.dhi_sb_e4

        dhm_loan: None | str | Unset
        if isinstance(self.dhm_loan, Unset):
            dhm_loan = UNSET
        else:
            dhm_loan = self.dhm_loan

        dhm_lr: None | str | Unset
        if isinstance(self.dhm_lr, Unset):
            dhm_lr = UNSET
        else:
            dhm_lr = self.dhm_lr

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

        dhz_4: float | None | Unset
        if isinstance(self.dhz_4, Unset):
            dhz_4 = UNSET
        else:
            dhz_4 = self.dhz_4

        dhz_5: None | str | Unset
        if isinstance(self.dhz_5, Unset):
            dhz_5 = UNSET
        else:
            dhz_5 = self.dhz_5

        dhz_6: None | str | Unset
        if isinstance(self.dhz_6, Unset):
            dhz_6 = UNSET
        else:
            dhz_6 = self.dhz_6

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

        edu_pri_be: float | None | Unset
        if isinstance(self.edu_pri_be, Unset):
            edu_pri_be = UNSET
        else:
            edu_pri_be = self.edu_pri_be

        edu_psec: float | None | Unset
        if isinstance(self.edu_psec, Unset):
            edu_psec = UNSET
        else:
            edu_psec = self.edu_psec

        edu_sec: float | None | Unset
        if isinstance(self.edu_sec, Unset):
            edu_sec = UNSET
        else:
            edu_sec = self.edu_sec

        estate: float | None | Unset
        if isinstance(self.estate, Unset):
            estate = UNSET
        else:
            estate = self.estate

        estate_chi: None | str | Unset
        if isinstance(self.estate_chi, Unset):
            estate_chi = UNSET
        else:
            estate_chi = self.estate_chi

        estate_eng: None | str | Unset
        if isinstance(self.estate_eng, Unset):
            estate_eng = UNSET
        else:
            estate_eng = self.estate_eng

        ethn_chi: float | None | Unset
        if isinstance(self.ethn_chi, Unset):
            ethn_chi = UNSET
        else:
            ethn_chi = self.ethn_chi

        ethn_ind: None | str | Unset
        if isinstance(self.ethn_ind, Unset):
            ethn_ind = UNSET
        else:
            ethn_ind = self.ethn_ind

        ethn_oth: None | str | Unset
        if isinstance(self.ethn_oth, Unset):
            ethn_oth = UNSET
        else:
            ethn_oth = self.ethn_oth

        ethn_phi: None | str | Unset
        if isinstance(self.ethn_phi, Unset):
            ethn_phi = UNSET
        else:
            ethn_phi = self.ethn_phi

        ethn_wh: None | str | Unset
        if isinstance(self.ethn_wh, Unset):
            ethn_wh = UNSET
        else:
            ethn_wh = self.ethn_wh

        fa_m: float | None | Unset
        if isinstance(self.fa_m, Unset):
            fa_m = UNSET
        else:
            fa_m = self.fa_m

        ma_econhh: float | None | Unset
        if isinstance(self.ma_econhh, Unset):
            ma_econhh = UNSET
        else:
            ma_econhh = self.ma_econhh

        ma_f: float | None | Unset
        if isinstance(self.ma_f, Unset):
            ma_f = UNSET
        else:
            ma_f = self.ma_f

        ma_hh: float | None | Unset
        if isinstance(self.ma_hh, Unset):
            ma_hh = UNSET
        else:
            ma_hh = self.ma_hh

        ma_m: float | None | Unset
        if isinstance(self.ma_m, Unset):
            ma_m = UNSET
        else:
            ma_m = self.ma_m

        mearn_xfdhfw_sb_1: float | None | Unset
        if isinstance(self.mearn_xfdhfw_sb_1, Unset):
            mearn_xfdhfw_sb_1 = UNSET
        else:
            mearn_xfdhfw_sb_1 = self.mearn_xfdhfw_sb_1

        mearn_xfdhfw_sb_2: float | None | Unset
        if isinstance(self.mearn_xfdhfw_sb_2, Unset):
            mearn_xfdhfw_sb_2 = UNSET
        else:
            mearn_xfdhfw_sb_2 = self.mearn_xfdhfw_sb_2

        mearn_xfdhfw_sb_3: float | None | Unset
        if isinstance(self.mearn_xfdhfw_sb_3, Unset):
            mearn_xfdhfw_sb_3 = UNSET
        else:
            mearn_xfdhfw_sb_3 = self.mearn_xfdhfw_sb_3

        mearn_xfw_sb_1: float | None | Unset
        if isinstance(self.mearn_xfw_sb_1, Unset):
            mearn_xfw_sb_1 = UNSET
        else:
            mearn_xfw_sb_1 = self.mearn_xfw_sb_1

        mearn_xfw_sb_2: float | None | Unset
        if isinstance(self.mearn_xfw_sb_2, Unset):
            mearn_xfw_sb_2 = UNSET
        else:
            mearn_xfw_sb_2 = self.mearn_xfw_sb_2

        mearn_xfw_sb_3: float | None | Unset
        if isinstance(self.mearn_xfw_sb_3, Unset):
            mearn_xfw_sb_3 = UNSET
        else:
            mearn_xfw_sb_3 = self.mearn_xfw_sb_3

        ms_m_f: float | None | Unset
        if isinstance(self.ms_m_f, Unset):
            ms_m_f = UNSET
        else:
            ms_m_f = self.ms_m_f

        ms_ma_m: float | None | Unset
        if isinstance(self.ms_ma_m, Unset):
            ms_ma_m = UNSET
        else:
            ms_ma_m = self.ms_ma_m

        ms_nm_f: float | None | Unset
        if isinstance(self.ms_nm_f, Unset):
            ms_nm_f = UNSET
        else:
            ms_nm_f = self.ms_nm_f

        ms_nm_m: float | None | Unset
        if isinstance(self.ms_nm_m, Unset):
            ms_nm_m = UNSET
        else:
            ms_nm_m = self.ms_nm_m

        ms_wds_f: float | None | Unset
        if isinstance(self.ms_wds_f, Unset):
            ms_wds_f = UNSET
        else:
            ms_wds_f = self.ms_wds_f

        ms_wds_m: None | str | Unset
        if isinstance(self.ms_wds_m, Unset):
            ms_wds_m = UNSET
        else:
            ms_wds_m = self.ms_wds_m

        nwp_care: None | str | Unset
        if isinstance(self.nwp_care, Unset):
            nwp_care = UNSET
        else:
            nwp_care = self.nwp_care

        nwp_hm: float | None | Unset
        if isinstance(self.nwp_hm, Unset):
            nwp_hm = UNSET
        else:
            nwp_hm = self.nwp_hm

        nwp_oth: float | None | Unset
        if isinstance(self.nwp_oth, Unset):
            nwp_oth = UNSET
        else:
            nwp_oth = self.nwp_oth

        nwp_re: float | None | Unset
        if isinstance(self.nwp_re, Unset):
            nwp_re = UNSET
        else:
            nwp_re = self.nwp_re

        nwp_st: float | None | Unset
        if isinstance(self.nwp_st, Unset):
            nwp_st = UNSET
        else:
            nwp_st = self.nwp_st

        pls_diff_hk: None | str | Unset
        if isinstance(self.pls_diff_hk, Unset):
            pls_diff_hk = UNSET
        else:
            pls_diff_hk = self.pls_diff_hk

        pls_diff_kln: None | str | Unset
        if isinstance(self.pls_diff_kln, Unset):
            pls_diff_kln = UNSET
        else:
            pls_diff_kln = self.pls_diff_kln

        pls_diff_nt: None | str | Unset
        if isinstance(self.pls_diff_nt, Unset):
            pls_diff_nt = UNSET
        else:
            pls_diff_nt = self.pls_diff_nt

        pls_same: None | str | Unset
        if isinstance(self.pls_same, Unset):
            pls_same = UNSET
        else:
            pls_same = self.pls_same

        plw_diff_hk: None | str | Unset
        if isinstance(self.plw_diff_hk, Unset):
            plw_diff_hk = UNSET
        else:
            plw_diff_hk = self.plw_diff_hk

        plw_diff_kln: float | None | Unset
        if isinstance(self.plw_diff_kln, Unset):
            plw_diff_kln = UNSET
        else:
            plw_diff_kln = self.plw_diff_kln

        plw_diff_nt: float | None | Unset
        if isinstance(self.plw_diff_nt, Unset):
            plw_diff_nt = UNSET
        else:
            plw_diff_nt = self.plw_diff_nt

        plw_diff_oth: None | str | Unset
        if isinstance(self.plw_diff_oth, Unset):
            plw_diff_oth = UNSET
        else:
            plw_diff_oth = self.plw_diff_oth

        plw_hm: float | None | Unset
        if isinstance(self.plw_hm, Unset):
            plw_hm = UNSET
        else:
            plw_hm = self.plw_hm

        plw_nofix: float | None | Unset
        if isinstance(self.plw_nofix, Unset):
            plw_nofix = UNSET
        else:
            plw_nofix = self.plw_nofix

        plw_out: None | str | Unset
        if isinstance(self.plw_out, Unset):
            plw_out = UNSET
        else:
            plw_out = self.plw_out

        plw_same: None | str | Unset
        if isinstance(self.plw_same, Unset):
            plw_same = UNSET
        else:
            plw_same = self.plw_same

        pop_f: float | None | Unset
        if isinstance(self.pop_f, Unset):
            pop_f = UNSET
        else:
            pop_f = self.pop_f

        pop_m: float | None | Unset
        if isinstance(self.pop_m, Unset):
            pop_m = UNSET
        else:
            pop_m = self.pop_m

        readchi_ablepctn: float | None | Unset
        if isinstance(self.readchi_ablepctn, Unset):
            readchi_ablepctn = UNSET
        else:
            readchi_ablepctn = self.readchi_ablepctn

        readeng_ablepctn: float | None | Unset
        if isinstance(self.readeng_ablepctn, Unset):
            readeng_ablepctn = UNSET
        else:
            readeng_ablepctn = self.readeng_ablepctn

        s_diff_oth: None | str | Unset
        if isinstance(self.s_diff_oth, Unset):
            s_diff_oth = UNSET
        else:
            s_diff_oth = self.s_diff_oth

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

        t_mmearn: float | None | Unset
        if isinstance(self.t_mmearn, Unset):
            t_mmearn = UNSET
        else:
            t_mmearn = self.t_mmearn

        t_mmearn_xfdh: float | None | Unset
        if isinstance(self.t_mmearn_xfdh, Unset):
            t_mmearn_xfdh = UNSET
        else:
            t_mmearn_xfdh = self.t_mmearn_xfdh

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

        ul_eng: None | str | Unset
        if isinstance(self.ul_eng, Unset):
            ul_eng = UNSET
        else:
            ul_eng = self.ul_eng

        ul_oth: None | str | Unset
        if isinstance(self.ul_oth, Unset):
            ul_oth = UNSET
        else:
            ul_oth = self.ul_oth

        ul_othchi: None | str | Unset
        if isinstance(self.ul_othchi, Unset):
            ul_othchi = UNSET
        else:
            ul_othchi = self.ul_othchi

        ul_put: None | str | Unset
        if isinstance(self.ul_put, Unset):
            ul_put = UNSET
        else:
            ul_put = self.ul_put

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

        whr_4: float | None | Unset
        if isinstance(self.whr_4, Unset):
            whr_4 = UNSET
        else:
            whr_4 = self.whr_4

        whr_5: float | None | Unset
        if isinstance(self.whr_5, Unset):
            whr_5 = UNSET
        else:
            whr_5 = self.whr_5

        whr_6: float | None | Unset
        if isinstance(self.whr_6, Unset):
            whr_6 = UNSET
        else:
            whr_6 = self.whr_6

        wp_a: None | str | Unset
        if isinstance(self.wp_a, Unset):
            wp_a = UNSET
        else:
            wp_a = self.wp_a

        wp_b: None | str | Unset
        if isinstance(self.wp_b, Unset):
            wp_b = UNSET
        else:
            wp_b = self.wp_b

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

        wp_er: None | str | Unset
        if isinstance(self.wp_er, Unset):
            wp_er = UNSET
        else:
            wp_er = self.wp_er

        wp_f: None | str | Unset
        if isinstance(self.wp_f, Unset):
            wp_f = UNSET
        else:
            wp_f = self.wp_f

        wp_fw: None | str | Unset
        if isinstance(self.wp_fw, Unset):
            wp_fw = UNSET
        else:
            wp_fw = self.wp_fw

        wp_g: None | str | Unset
        if isinstance(self.wp_g, Unset):
            wp_g = UNSET
        else:
            wp_g = self.wp_g

        wp_h: float | None | Unset
        if isinstance(self.wp_h, Unset):
            wp_h = UNSET
        else:
            wp_h = self.wp_h

        wp_i: None | str | Unset
        if isinstance(self.wp_i, Unset):
            wp_i = UNSET
        else:
            wp_i = self.wp_i

        wp_j: None | str | Unset
        if isinstance(self.wp_j, Unset):
            wp_j = UNSET
        else:
            wp_j = self.wp_j

        wp_k: float | None | Unset
        if isinstance(self.wp_k, Unset):
            wp_k = UNSET
        else:
            wp_k = self.wp_k

        wp_l: float | None | Unset
        if isinstance(self.wp_l, Unset):
            wp_l = UNSET
        else:
            wp_l = self.wp_l

        wp_m: None | str | Unset
        if isinstance(self.wp_m, Unset):
            wp_m = UNSET
        else:
            wp_m = self.wp_m

        wp_n: None | str | Unset
        if isinstance(self.wp_n, Unset):
            wp_n = UNSET
        else:
            wp_n = self.wp_n

        wp_o: None | str | Unset
        if isinstance(self.wp_o, Unset):
            wp_o = UNSET
        else:
            wp_o = self.wp_o

        wp_p: float | None | Unset
        if isinstance(self.wp_p, Unset):
            wp_p = UNSET
        else:
            wp_p = self.wp_p

        wp_q: float | None | Unset
        if isinstance(self.wp_q, Unset):
            wp_q = UNSET
        else:
            wp_q = self.wp_q

        wp_r: float | None | Unset
        if isinstance(self.wp_r, Unset):
            wp_r = UNSET
        else:
            wp_r = self.wp_r

        wp_s: float | None | Unset
        if isinstance(self.wp_s, Unset):
            wp_s = UNSET
        else:
            wp_s = self.wp_s

        wp_se: float | None | Unset
        if isinstance(self.wp_se, Unset):
            wp_se = UNSET
        else:
            wp_se = self.wp_se

        wp_t: None | str | Unset
        if isinstance(self.wp_t, Unset):
            wp_t = UNSET
        else:
            wp_t = self.wp_t

        writechi_ablepctn: float | None | Unset
        if isinstance(self.writechi_ablepctn, Unset):
            writechi_ablepctn = UNSET
        else:
            writechi_ablepctn = self.writechi_ablepctn

        writeeng_ablepctn: float | None | Unset
        if isinstance(self.writeeng_ablepctn, Unset):
            writeeng_ablepctn = UNSET
        else:
            writeeng_ablepctn = self.writeeng_ablepctn

        objectid = self.objectid

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

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
        if age_5 is not UNSET:
            field_dict["age_5"] = age_5
        if born_chi is not UNSET:
            field_dict["born_chi"] = born_chi
        if born_else is not UNSET:
            field_dict["born_else"] = born_else
        if born_hk is not UNSET:
            field_dict["born_hk"] = born_hk
        if dh is not UNSET:
            field_dict["dh"] = dh
        if dhc_nc is not UNSET:
            field_dict["dhc_nc"] = dhc_nc
        if dhc_oth is not UNSET:
            field_dict["dhc_oth"] = dhc_oth
        if dhc_re is not UNSET:
            field_dict["dhc_re"] = dhc_re
        if dhi_sb_1 is not UNSET:
            field_dict["dhi_sb_1"] = dhi_sb_1
        if dhi_sb_2 is not UNSET:
            field_dict["dhi_sb_2"] = dhi_sb_2
        if dhi_sb_3 is not UNSET:
            field_dict["dhi_sb_3"] = dhi_sb_3
        if dhi_sb_4 is not UNSET:
            field_dict["dhi_sb_4"] = dhi_sb_4
        if dhi_sb_e1 is not UNSET:
            field_dict["dhi_sb_e1"] = dhi_sb_e1
        if dhi_sb_e2 is not UNSET:
            field_dict["dhi_sb_e2"] = dhi_sb_e2
        if dhi_sb_e3 is not UNSET:
            field_dict["dhi_sb_e3"] = dhi_sb_e3
        if dhi_sb_e4 is not UNSET:
            field_dict["dhi_sb_e4"] = dhi_sb_e4
        if dhm_loan is not UNSET:
            field_dict["dhm_loan"] = dhm_loan
        if dhm_lr is not UNSET:
            field_dict["dhm_lr"] = dhm_lr
        if dhz_1 is not UNSET:
            field_dict["dhz_1"] = dhz_1
        if dhz_2 is not UNSET:
            field_dict["dhz_2"] = dhz_2
        if dhz_3 is not UNSET:
            field_dict["dhz_3"] = dhz_3
        if dhz_4 is not UNSET:
            field_dict["dhz_4"] = dhz_4
        if dhz_5 is not UNSET:
            field_dict["dhz_5"] = dhz_5
        if dhz_6 is not UNSET:
            field_dict["dhz_6"] = dhz_6
        if dm_r is not UNSET:
            field_dict["dm_r"] = dm_r
        if dmr_ir is not UNSET:
            field_dict["dmr_ir"] = dmr_ir
        if edu_pri_be is not UNSET:
            field_dict["edu_pri_be"] = edu_pri_be
        if edu_psec is not UNSET:
            field_dict["edu_psec"] = edu_psec
        if edu_sec is not UNSET:
            field_dict["edu_sec"] = edu_sec
        if estate is not UNSET:
            field_dict["estate"] = estate
        if estate_chi is not UNSET:
            field_dict["estate_chi"] = estate_chi
        if estate_eng is not UNSET:
            field_dict["estate_eng"] = estate_eng
        if ethn_chi is not UNSET:
            field_dict["ethn_chi"] = ethn_chi
        if ethn_ind is not UNSET:
            field_dict["ethn_ind"] = ethn_ind
        if ethn_oth is not UNSET:
            field_dict["ethn_oth"] = ethn_oth
        if ethn_phi is not UNSET:
            field_dict["ethn_phi"] = ethn_phi
        if ethn_wh is not UNSET:
            field_dict["ethn_wh"] = ethn_wh
        if fa_m is not UNSET:
            field_dict["fa_m"] = fa_m
        if ma_econhh is not UNSET:
            field_dict["ma_econhh"] = ma_econhh
        if ma_f is not UNSET:
            field_dict["ma_f"] = ma_f
        if ma_hh is not UNSET:
            field_dict["ma_hh"] = ma_hh
        if ma_m is not UNSET:
            field_dict["ma_m"] = ma_m
        if mearn_xfdhfw_sb_1 is not UNSET:
            field_dict["mearn_xfdhfw_sb_1"] = mearn_xfdhfw_sb_1
        if mearn_xfdhfw_sb_2 is not UNSET:
            field_dict["mearn_xfdhfw_sb_2"] = mearn_xfdhfw_sb_2
        if mearn_xfdhfw_sb_3 is not UNSET:
            field_dict["mearn_xfdhfw_sb_3"] = mearn_xfdhfw_sb_3
        if mearn_xfw_sb_1 is not UNSET:
            field_dict["mearn_xfw_sb_1"] = mearn_xfw_sb_1
        if mearn_xfw_sb_2 is not UNSET:
            field_dict["mearn_xfw_sb_2"] = mearn_xfw_sb_2
        if mearn_xfw_sb_3 is not UNSET:
            field_dict["mearn_xfw_sb_3"] = mearn_xfw_sb_3
        if ms_m_f is not UNSET:
            field_dict["ms_m_f"] = ms_m_f
        if ms_ma_m is not UNSET:
            field_dict["ms_ma_m"] = ms_ma_m
        if ms_nm_f is not UNSET:
            field_dict["ms_nm_f"] = ms_nm_f
        if ms_nm_m is not UNSET:
            field_dict["ms_nm_m"] = ms_nm_m
        if ms_wds_f is not UNSET:
            field_dict["ms_wds_f"] = ms_wds_f
        if ms_wds_m is not UNSET:
            field_dict["ms_wds_m"] = ms_wds_m
        if nwp_care is not UNSET:
            field_dict["nwp_care"] = nwp_care
        if nwp_hm is not UNSET:
            field_dict["nwp_hm"] = nwp_hm
        if nwp_oth is not UNSET:
            field_dict["nwp_oth"] = nwp_oth
        if nwp_re is not UNSET:
            field_dict["nwp_re"] = nwp_re
        if nwp_st is not UNSET:
            field_dict["nwp_st"] = nwp_st
        if pls_diff_hk is not UNSET:
            field_dict["pls_diff_hk"] = pls_diff_hk
        if pls_diff_kln is not UNSET:
            field_dict["pls_diff_kln"] = pls_diff_kln
        if pls_diff_nt is not UNSET:
            field_dict["pls_diff_nt"] = pls_diff_nt
        if pls_same is not UNSET:
            field_dict["pls_same"] = pls_same
        if plw_diff_hk is not UNSET:
            field_dict["plw_diff_hk"] = plw_diff_hk
        if plw_diff_kln is not UNSET:
            field_dict["plw_diff_kln"] = plw_diff_kln
        if plw_diff_nt is not UNSET:
            field_dict["plw_diff_nt"] = plw_diff_nt
        if plw_diff_oth is not UNSET:
            field_dict["plw_diff_oth"] = plw_diff_oth
        if plw_hm is not UNSET:
            field_dict["plw_hm"] = plw_hm
        if plw_nofix is not UNSET:
            field_dict["plw_nofix"] = plw_nofix
        if plw_out is not UNSET:
            field_dict["plw_out"] = plw_out
        if plw_same is not UNSET:
            field_dict["plw_same"] = plw_same
        if pop_f is not UNSET:
            field_dict["pop_f"] = pop_f
        if pop_m is not UNSET:
            field_dict["pop_m"] = pop_m
        if readchi_ablepctn is not UNSET:
            field_dict["readchi_ablepctn"] = readchi_ablepctn
        if readeng_ablepctn is not UNSET:
            field_dict["readeng_ablepctn"] = readeng_ablepctn
        if s_diff_oth is not UNSET:
            field_dict["s_diff_oth"] = s_diff_oth
        if sr is not UNSET:
            field_dict["sr"] = sr
        if t_ma is not UNSET:
            field_dict["t_ma"] = t_ma
        if t_mmearn is not UNSET:
            field_dict["t_mmearn"] = t_mmearn
        if t_mmearn_xfdh is not UNSET:
            field_dict["t_mmearn_xfdh"] = t_mmearn_xfdh
        if t_nwp is not UNSET:
            field_dict["t_nwp"] = t_nwp
        if t_pop is not UNSET:
            field_dict["t_pop"] = t_pop
        if t_wp is not UNSET:
            field_dict["t_wp"] = t_wp
        if ul_can is not UNSET:
            field_dict["ul_can"] = ul_can
        if ul_eng is not UNSET:
            field_dict["ul_eng"] = ul_eng
        if ul_oth is not UNSET:
            field_dict["ul_oth"] = ul_oth
        if ul_othchi is not UNSET:
            field_dict["ul_othchi"] = ul_othchi
        if ul_put is not UNSET:
            field_dict["ul_put"] = ul_put
        if whr_1 is not UNSET:
            field_dict["whr_1"] = whr_1
        if whr_2 is not UNSET:
            field_dict["whr_2"] = whr_2
        if whr_3 is not UNSET:
            field_dict["whr_3"] = whr_3
        if whr_4 is not UNSET:
            field_dict["whr_4"] = whr_4
        if whr_5 is not UNSET:
            field_dict["whr_5"] = whr_5
        if whr_6 is not UNSET:
            field_dict["whr_6"] = whr_6
        if wp_a is not UNSET:
            field_dict["wp_a"] = wp_a
        if wp_b is not UNSET:
            field_dict["wp_b"] = wp_b
        if wp_c is not UNSET:
            field_dict["wp_c"] = wp_c
        if wp_d is not UNSET:
            field_dict["wp_d"] = wp_d
        if wp_e is not UNSET:
            field_dict["wp_e"] = wp_e
        if wp_ee is not UNSET:
            field_dict["wp_ee"] = wp_ee
        if wp_er is not UNSET:
            field_dict["wp_er"] = wp_er
        if wp_f is not UNSET:
            field_dict["wp_f"] = wp_f
        if wp_fw is not UNSET:
            field_dict["wp_fw"] = wp_fw
        if wp_g is not UNSET:
            field_dict["wp_g"] = wp_g
        if wp_h is not UNSET:
            field_dict["wp_h"] = wp_h
        if wp_i is not UNSET:
            field_dict["wp_i"] = wp_i
        if wp_j is not UNSET:
            field_dict["wp_j"] = wp_j
        if wp_k is not UNSET:
            field_dict["wp_k"] = wp_k
        if wp_l is not UNSET:
            field_dict["wp_l"] = wp_l
        if wp_m is not UNSET:
            field_dict["wp_m"] = wp_m
        if wp_n is not UNSET:
            field_dict["wp_n"] = wp_n
        if wp_o is not UNSET:
            field_dict["wp_o"] = wp_o
        if wp_p is not UNSET:
            field_dict["wp_p"] = wp_p
        if wp_q is not UNSET:
            field_dict["wp_q"] = wp_q
        if wp_r is not UNSET:
            field_dict["wp_r"] = wp_r
        if wp_s is not UNSET:
            field_dict["wp_s"] = wp_s
        if wp_se is not UNSET:
            field_dict["wp_se"] = wp_se
        if wp_t is not UNSET:
            field_dict["wp_t"] = wp_t
        if writechi_ablepctn is not UNSET:
            field_dict["writechi_ablepctn"] = writechi_ablepctn
        if writeeng_ablepctn is not UNSET:
            field_dict["writeeng_ablepctn"] = writeeng_ablepctn
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

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

        def _parse_age_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        age_5 = _parse_age_5(d.pop("age_5", UNSET))

        def _parse_born_chi(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        born_chi = _parse_born_chi(d.pop("born_chi", UNSET))

        def _parse_born_else(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        born_else = _parse_born_else(d.pop("born_else", UNSET))

        def _parse_born_hk(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        born_hk = _parse_born_hk(d.pop("born_hk", UNSET))

        def _parse_dh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh = _parse_dh(d.pop("dh", UNSET))

        def _parse_dhc_nc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_nc = _parse_dhc_nc(d.pop("dhc_nc", UNSET))

        def _parse_dhc_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_oth = _parse_dhc_oth(d.pop("dhc_oth", UNSET))

        def _parse_dhc_re(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_re = _parse_dhc_re(d.pop("dhc_re", UNSET))

        def _parse_dhi_sb_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_sb_1 = _parse_dhi_sb_1(d.pop("dhi_sb_1", UNSET))

        def _parse_dhi_sb_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_sb_2 = _parse_dhi_sb_2(d.pop("dhi_sb_2", UNSET))

        def _parse_dhi_sb_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_sb_3 = _parse_dhi_sb_3(d.pop("dhi_sb_3", UNSET))

        def _parse_dhi_sb_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhi_sb_4 = _parse_dhi_sb_4(d.pop("dhi_sb_4", UNSET))

        def _parse_dhi_sb_e1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhi_sb_e1 = _parse_dhi_sb_e1(d.pop("dhi_sb_e1", UNSET))

        def _parse_dhi_sb_e2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhi_sb_e2 = _parse_dhi_sb_e2(d.pop("dhi_sb_e2", UNSET))

        def _parse_dhi_sb_e3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_sb_e3 = _parse_dhi_sb_e3(d.pop("dhi_sb_e3", UNSET))

        def _parse_dhi_sb_e4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhi_sb_e4 = _parse_dhi_sb_e4(d.pop("dhi_sb_e4", UNSET))

        def _parse_dhm_loan(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhm_loan = _parse_dhm_loan(d.pop("dhm_loan", UNSET))

        def _parse_dhm_lr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhm_lr = _parse_dhm_lr(d.pop("dhm_lr", UNSET))

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

        def _parse_dhz_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_4 = _parse_dhz_4(d.pop("dhz_4", UNSET))

        def _parse_dhz_5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhz_5 = _parse_dhz_5(d.pop("dhz_5", UNSET))

        def _parse_dhz_6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhz_6 = _parse_dhz_6(d.pop("dhz_6", UNSET))

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

        def _parse_edu_pri_be(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_pri_be = _parse_edu_pri_be(d.pop("edu_pri_be", UNSET))

        def _parse_edu_psec(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_psec = _parse_edu_psec(d.pop("edu_psec", UNSET))

        def _parse_edu_sec(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_sec = _parse_edu_sec(d.pop("edu_sec", UNSET))

        def _parse_estate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estate = _parse_estate(d.pop("estate", UNSET))

        def _parse_estate_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estate_chi = _parse_estate_chi(d.pop("estate_chi", UNSET))

        def _parse_estate_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estate_eng = _parse_estate_eng(d.pop("estate_eng", UNSET))

        def _parse_ethn_chi(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ethn_chi = _parse_ethn_chi(d.pop("ethn_chi", UNSET))

        def _parse_ethn_ind(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ethn_ind = _parse_ethn_ind(d.pop("ethn_ind", UNSET))

        def _parse_ethn_oth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ethn_oth = _parse_ethn_oth(d.pop("ethn_oth", UNSET))

        def _parse_ethn_phi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ethn_phi = _parse_ethn_phi(d.pop("ethn_phi", UNSET))

        def _parse_ethn_wh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ethn_wh = _parse_ethn_wh(d.pop("ethn_wh", UNSET))

        def _parse_fa_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fa_m = _parse_fa_m(d.pop("fa_m", UNSET))

        def _parse_ma_econhh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ma_econhh = _parse_ma_econhh(d.pop("ma_econhh", UNSET))

        def _parse_ma_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ma_f = _parse_ma_f(d.pop("ma_f", UNSET))

        def _parse_ma_hh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ma_hh = _parse_ma_hh(d.pop("ma_hh", UNSET))

        def _parse_ma_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ma_m = _parse_ma_m(d.pop("ma_m", UNSET))

        def _parse_mearn_xfdhfw_sb_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdhfw_sb_1 = _parse_mearn_xfdhfw_sb_1(d.pop("mearn_xfdhfw_sb_1", UNSET))

        def _parse_mearn_xfdhfw_sb_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdhfw_sb_2 = _parse_mearn_xfdhfw_sb_2(d.pop("mearn_xfdhfw_sb_2", UNSET))

        def _parse_mearn_xfdhfw_sb_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdhfw_sb_3 = _parse_mearn_xfdhfw_sb_3(d.pop("mearn_xfdhfw_sb_3", UNSET))

        def _parse_mearn_xfw_sb_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfw_sb_1 = _parse_mearn_xfw_sb_1(d.pop("mearn_xfw_sb_1", UNSET))

        def _parse_mearn_xfw_sb_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfw_sb_2 = _parse_mearn_xfw_sb_2(d.pop("mearn_xfw_sb_2", UNSET))

        def _parse_mearn_xfw_sb_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfw_sb_3 = _parse_mearn_xfw_sb_3(d.pop("mearn_xfw_sb_3", UNSET))

        def _parse_ms_m_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_m_f = _parse_ms_m_f(d.pop("ms_m_f", UNSET))

        def _parse_ms_ma_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_ma_m = _parse_ms_ma_m(d.pop("ms_ma_m", UNSET))

        def _parse_ms_nm_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_nm_f = _parse_ms_nm_f(d.pop("ms_nm_f", UNSET))

        def _parse_ms_nm_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_nm_m = _parse_ms_nm_m(d.pop("ms_nm_m", UNSET))

        def _parse_ms_wds_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_wds_f = _parse_ms_wds_f(d.pop("ms_wds_f", UNSET))

        def _parse_ms_wds_m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ms_wds_m = _parse_ms_wds_m(d.pop("ms_wds_m", UNSET))

        def _parse_nwp_care(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nwp_care = _parse_nwp_care(d.pop("nwp_care", UNSET))

        def _parse_nwp_hm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nwp_hm = _parse_nwp_hm(d.pop("nwp_hm", UNSET))

        def _parse_nwp_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nwp_oth = _parse_nwp_oth(d.pop("nwp_oth", UNSET))

        def _parse_nwp_re(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nwp_re = _parse_nwp_re(d.pop("nwp_re", UNSET))

        def _parse_nwp_st(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        nwp_st = _parse_nwp_st(d.pop("nwp_st", UNSET))

        def _parse_pls_diff_hk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pls_diff_hk = _parse_pls_diff_hk(d.pop("pls_diff_hk", UNSET))

        def _parse_pls_diff_kln(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pls_diff_kln = _parse_pls_diff_kln(d.pop("pls_diff_kln", UNSET))

        def _parse_pls_diff_nt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pls_diff_nt = _parse_pls_diff_nt(d.pop("pls_diff_nt", UNSET))

        def _parse_pls_same(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pls_same = _parse_pls_same(d.pop("pls_same", UNSET))

        def _parse_plw_diff_hk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plw_diff_hk = _parse_plw_diff_hk(d.pop("plw_diff_hk", UNSET))

        def _parse_plw_diff_kln(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        plw_diff_kln = _parse_plw_diff_kln(d.pop("plw_diff_kln", UNSET))

        def _parse_plw_diff_nt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        plw_diff_nt = _parse_plw_diff_nt(d.pop("plw_diff_nt", UNSET))

        def _parse_plw_diff_oth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plw_diff_oth = _parse_plw_diff_oth(d.pop("plw_diff_oth", UNSET))

        def _parse_plw_hm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        plw_hm = _parse_plw_hm(d.pop("plw_hm", UNSET))

        def _parse_plw_nofix(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        plw_nofix = _parse_plw_nofix(d.pop("plw_nofix", UNSET))

        def _parse_plw_out(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plw_out = _parse_plw_out(d.pop("plw_out", UNSET))

        def _parse_plw_same(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plw_same = _parse_plw_same(d.pop("plw_same", UNSET))

        def _parse_pop_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pop_f = _parse_pop_f(d.pop("pop_f", UNSET))

        def _parse_pop_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pop_m = _parse_pop_m(d.pop("pop_m", UNSET))

        def _parse_readchi_ablepctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        readchi_ablepctn = _parse_readchi_ablepctn(d.pop("readchi_ablepctn", UNSET))

        def _parse_readeng_ablepctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        readeng_ablepctn = _parse_readeng_ablepctn(d.pop("readeng_ablepctn", UNSET))

        def _parse_s_diff_oth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        s_diff_oth = _parse_s_diff_oth(d.pop("s_diff_oth", UNSET))

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

        def _parse_t_mmearn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_mmearn = _parse_t_mmearn(d.pop("t_mmearn", UNSET))

        def _parse_t_mmearn_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_mmearn_xfdh = _parse_t_mmearn_xfdh(d.pop("t_mmearn_xfdh", UNSET))

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

        def _parse_ul_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ul_eng = _parse_ul_eng(d.pop("ul_eng", UNSET))

        def _parse_ul_oth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ul_oth = _parse_ul_oth(d.pop("ul_oth", UNSET))

        def _parse_ul_othchi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ul_othchi = _parse_ul_othchi(d.pop("ul_othchi", UNSET))

        def _parse_ul_put(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ul_put = _parse_ul_put(d.pop("ul_put", UNSET))

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

        def _parse_whr_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        whr_4 = _parse_whr_4(d.pop("whr_4", UNSET))

        def _parse_whr_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        whr_5 = _parse_whr_5(d.pop("whr_5", UNSET))

        def _parse_whr_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        whr_6 = _parse_whr_6(d.pop("whr_6", UNSET))

        def _parse_wp_a(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_a = _parse_wp_a(d.pop("wp_a", UNSET))

        def _parse_wp_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_b = _parse_wp_b(d.pop("wp_b", UNSET))

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

        def _parse_wp_er(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_er = _parse_wp_er(d.pop("wp_er", UNSET))

        def _parse_wp_f(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_f = _parse_wp_f(d.pop("wp_f", UNSET))

        def _parse_wp_fw(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_fw = _parse_wp_fw(d.pop("wp_fw", UNSET))

        def _parse_wp_g(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_g = _parse_wp_g(d.pop("wp_g", UNSET))

        def _parse_wp_h(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_h = _parse_wp_h(d.pop("wp_h", UNSET))

        def _parse_wp_i(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_i = _parse_wp_i(d.pop("wp_i", UNSET))

        def _parse_wp_j(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_j = _parse_wp_j(d.pop("wp_j", UNSET))

        def _parse_wp_k(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_k = _parse_wp_k(d.pop("wp_k", UNSET))

        def _parse_wp_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_l = _parse_wp_l(d.pop("wp_l", UNSET))

        def _parse_wp_m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_m = _parse_wp_m(d.pop("wp_m", UNSET))

        def _parse_wp_n(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_n = _parse_wp_n(d.pop("wp_n", UNSET))

        def _parse_wp_o(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_o = _parse_wp_o(d.pop("wp_o", UNSET))

        def _parse_wp_p(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_p = _parse_wp_p(d.pop("wp_p", UNSET))

        def _parse_wp_q(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_q = _parse_wp_q(d.pop("wp_q", UNSET))

        def _parse_wp_r(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_r = _parse_wp_r(d.pop("wp_r", UNSET))

        def _parse_wp_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_s = _parse_wp_s(d.pop("wp_s", UNSET))

        def _parse_wp_se(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_se = _parse_wp_se(d.pop("wp_se", UNSET))

        def _parse_wp_t(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_t = _parse_wp_t(d.pop("wp_t", UNSET))

        def _parse_writechi_ablepctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        writechi_ablepctn = _parse_writechi_ablepctn(d.pop("writechi_ablepctn", UNSET))

        def _parse_writeeng_ablepctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        writeeng_ablepctn = _parse_writeeng_ablepctn(d.pop("writeeng_ablepctn", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            adhz=adhz,
            age_1=age_1,
            age_2=age_2,
            age_3=age_3,
            age_4=age_4,
            age_5=age_5,
            born_chi=born_chi,
            born_else=born_else,
            born_hk=born_hk,
            dh=dh,
            dhc_nc=dhc_nc,
            dhc_oth=dhc_oth,
            dhc_re=dhc_re,
            dhi_sb_1=dhi_sb_1,
            dhi_sb_2=dhi_sb_2,
            dhi_sb_3=dhi_sb_3,
            dhi_sb_4=dhi_sb_4,
            dhi_sb_e1=dhi_sb_e1,
            dhi_sb_e2=dhi_sb_e2,
            dhi_sb_e3=dhi_sb_e3,
            dhi_sb_e4=dhi_sb_e4,
            dhm_loan=dhm_loan,
            dhm_lr=dhm_lr,
            dhz_1=dhz_1,
            dhz_2=dhz_2,
            dhz_3=dhz_3,
            dhz_4=dhz_4,
            dhz_5=dhz_5,
            dhz_6=dhz_6,
            dm_r=dm_r,
            dmr_ir=dmr_ir,
            edu_pri_be=edu_pri_be,
            edu_psec=edu_psec,
            edu_sec=edu_sec,
            estate=estate,
            estate_chi=estate_chi,
            estate_eng=estate_eng,
            ethn_chi=ethn_chi,
            ethn_ind=ethn_ind,
            ethn_oth=ethn_oth,
            ethn_phi=ethn_phi,
            ethn_wh=ethn_wh,
            fa_m=fa_m,
            ma_econhh=ma_econhh,
            ma_f=ma_f,
            ma_hh=ma_hh,
            ma_m=ma_m,
            mearn_xfdhfw_sb_1=mearn_xfdhfw_sb_1,
            mearn_xfdhfw_sb_2=mearn_xfdhfw_sb_2,
            mearn_xfdhfw_sb_3=mearn_xfdhfw_sb_3,
            mearn_xfw_sb_1=mearn_xfw_sb_1,
            mearn_xfw_sb_2=mearn_xfw_sb_2,
            mearn_xfw_sb_3=mearn_xfw_sb_3,
            ms_m_f=ms_m_f,
            ms_ma_m=ms_ma_m,
            ms_nm_f=ms_nm_f,
            ms_nm_m=ms_nm_m,
            ms_wds_f=ms_wds_f,
            ms_wds_m=ms_wds_m,
            nwp_care=nwp_care,
            nwp_hm=nwp_hm,
            nwp_oth=nwp_oth,
            nwp_re=nwp_re,
            nwp_st=nwp_st,
            pls_diff_hk=pls_diff_hk,
            pls_diff_kln=pls_diff_kln,
            pls_diff_nt=pls_diff_nt,
            pls_same=pls_same,
            plw_diff_hk=plw_diff_hk,
            plw_diff_kln=plw_diff_kln,
            plw_diff_nt=plw_diff_nt,
            plw_diff_oth=plw_diff_oth,
            plw_hm=plw_hm,
            plw_nofix=plw_nofix,
            plw_out=plw_out,
            plw_same=plw_same,
            pop_f=pop_f,
            pop_m=pop_m,
            readchi_ablepctn=readchi_ablepctn,
            readeng_ablepctn=readeng_ablepctn,
            s_diff_oth=s_diff_oth,
            sr=sr,
            t_ma=t_ma,
            t_mmearn=t_mmearn,
            t_mmearn_xfdh=t_mmearn_xfdh,
            t_nwp=t_nwp,
            t_pop=t_pop,
            t_wp=t_wp,
            ul_can=ul_can,
            ul_eng=ul_eng,
            ul_oth=ul_oth,
            ul_othchi=ul_othchi,
            ul_put=ul_put,
            whr_1=whr_1,
            whr_2=whr_2,
            whr_3=whr_3,
            whr_4=whr_4,
            whr_5=whr_5,
            whr_6=whr_6,
            wp_a=wp_a,
            wp_b=wp_b,
            wp_c=wp_c,
            wp_d=wp_d,
            wp_e=wp_e,
            wp_ee=wp_ee,
            wp_er=wp_er,
            wp_f=wp_f,
            wp_fw=wp_fw,
            wp_g=wp_g,
            wp_h=wp_h,
            wp_i=wp_i,
            wp_j=wp_j,
            wp_k=wp_k,
            wp_l=wp_l,
            wp_m=wp_m,
            wp_n=wp_n,
            wp_o=wp_o,
            wp_p=wp_p,
            wp_q=wp_q,
            wp_r=wp_r,
            wp_s=wp_s,
            wp_se=wp_se,
            wp_t=wp_t,
            writechi_ablepctn=writechi_ablepctn,
            writeeng_ablepctn=writeeng_ablepctn,
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
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
