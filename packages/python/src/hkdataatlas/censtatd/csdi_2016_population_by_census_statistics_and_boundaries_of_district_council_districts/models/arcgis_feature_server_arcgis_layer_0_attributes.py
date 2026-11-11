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
        born_else (float | None | Unset): Publisher field type: esriFieldTypeDouble
        born_hk (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dc_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        dc_class (None | str | Unset): Publisher field type: esriFieldTypeString
        dc_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        dh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_co (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_emp (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_non (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_ocm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_ocwm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_pri (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_pub (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r0 (None | str | Unset): Publisher field type: esriFieldTypeString
        dh_r1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_r6 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_rf (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_s (None | str | Unset): Publisher field type: esriFieldTypeString
        dh_st (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dh_tem (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_6 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_7 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhc_8 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_6 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_7 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_e1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_e2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_e3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_e4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_e5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_e6 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhi_e7 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhm_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhm_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhm_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhm_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhm_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhm_6 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhm_7 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhm_loan (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhm_lr (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhr_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhr_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhr_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhr_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dhz_6 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dm_r (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dmr_ir (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_deg (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_dip (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_lsed (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_prepri (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_pri (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_sub (float | None | Unset): Publisher field type: esriFieldTypeDouble
        edu_usec (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ethn_chi (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ethn_ind (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ethn_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ethn_phi (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ethn_wh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        fa_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lf_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lf_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lfpr_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lfpr_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lfpr_t (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ma_econhh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ma_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ma_hh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ma_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdh_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdh_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdh_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdh_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdh_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdh_6 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdh_7 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_6 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mearn_xfdhfw_7 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mmearn_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mmearn_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mmearn_xfdh_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mmearn_xfdh_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_div_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_div_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_m_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_ma_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_nm_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_nm_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_sep_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_sep_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_win_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_win_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nwp_hm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nwp_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nwp_re (float | None | Unset): Publisher field type: esriFieldTypeDouble
        nwp_st (float | None | Unset): Publisher field type: esriFieldTypeDouble
        oq_non (float | None | Unset): Publisher field type: esriFieldTypeDouble
        oq_pri (float | None | Unset): Publisher field type: esriFieldTypeDouble
        oq_pub (float | None | Unset): Publisher field type: esriFieldTypeDouble
        oq_s (None | str | Unset): Publisher field type: esriFieldTypeString
        oq_tem (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pcfa_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pls_diff_hk (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pls_diff_kln (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pls_diff_nt (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pls_same (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_diff_hk (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_diff_kln (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_diff_nt (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_diff_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_hm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_nofix (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_out (float | None | Unset): Publisher field type: esriFieldTypeDouble
        plw_same (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_hk (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_kln (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_nt (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_out (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_same (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_samearea (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pop_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pop_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pop_non (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pop_pri (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pop_pub (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pop_s (None | str | Unset): Publisher field type: esriFieldTypeString
        pop_tem (float | None | Unset): Publisher field type: esriFieldTypeDouble
        readchi_ablepctn (float | None | Unset): Publisher field type: esriFieldTypeDouble
        readeng_ablepctn (float | None | Unset): Publisher field type: esriFieldTypeDouble
        s_diff_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sr (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_lf (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_ma (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_mmearn (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_mmearn_xfdh (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_nwp (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_pop (float | None | Unset): Publisher field type: esriFieldTypeDouble
        t_wp (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ul_can (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ul_eng (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ul_oth (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ul_othchi (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ul_put (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_4 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        whr_6 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_a (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_b (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_c (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_d (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_e (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_ee (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_er (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_fw (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_g (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_h (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_i (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_j (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_k (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_l (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_o (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_p (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_q (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_r (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_s (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_se (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wp_t (float | None | Unset): Publisher field type: esriFieldTypeDouble
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
    born_else: float | None | Unset = UNSET
    born_hk: float | None | Unset = UNSET
    dc: float | None | Unset = UNSET
    dc_chi: None | str | Unset = UNSET
    dc_class: None | str | Unset = UNSET
    dc_eng: None | str | Unset = UNSET
    dh: float | None | Unset = UNSET
    dh_co: float | None | Unset = UNSET
    dh_emp: float | None | Unset = UNSET
    dh_non: float | None | Unset = UNSET
    dh_ocm: float | None | Unset = UNSET
    dh_ocwm: float | None | Unset = UNSET
    dh_pri: float | None | Unset = UNSET
    dh_pub: float | None | Unset = UNSET
    dh_r0: None | str | Unset = UNSET
    dh_r1: float | None | Unset = UNSET
    dh_r2: float | None | Unset = UNSET
    dh_r3: float | None | Unset = UNSET
    dh_r4: float | None | Unset = UNSET
    dh_r5: float | None | Unset = UNSET
    dh_r6: float | None | Unset = UNSET
    dh_rf: float | None | Unset = UNSET
    dh_s: None | str | Unset = UNSET
    dh_st: float | None | Unset = UNSET
    dh_tem: float | None | Unset = UNSET
    dhc_1: float | None | Unset = UNSET
    dhc_2: float | None | Unset = UNSET
    dhc_3: float | None | Unset = UNSET
    dhc_4: float | None | Unset = UNSET
    dhc_5: float | None | Unset = UNSET
    dhc_6: float | None | Unset = UNSET
    dhc_7: float | None | Unset = UNSET
    dhc_8: float | None | Unset = UNSET
    dhi_1: float | None | Unset = UNSET
    dhi_2: float | None | Unset = UNSET
    dhi_3: float | None | Unset = UNSET
    dhi_4: float | None | Unset = UNSET
    dhi_5: float | None | Unset = UNSET
    dhi_6: float | None | Unset = UNSET
    dhi_7: float | None | Unset = UNSET
    dhi_e1: float | None | Unset = UNSET
    dhi_e2: float | None | Unset = UNSET
    dhi_e3: float | None | Unset = UNSET
    dhi_e4: float | None | Unset = UNSET
    dhi_e5: float | None | Unset = UNSET
    dhi_e6: float | None | Unset = UNSET
    dhi_e7: float | None | Unset = UNSET
    dhm_1: float | None | Unset = UNSET
    dhm_2: float | None | Unset = UNSET
    dhm_3: float | None | Unset = UNSET
    dhm_4: float | None | Unset = UNSET
    dhm_5: float | None | Unset = UNSET
    dhm_6: float | None | Unset = UNSET
    dhm_7: float | None | Unset = UNSET
    dhm_loan: float | None | Unset = UNSET
    dhm_lr: float | None | Unset = UNSET
    dhr_1: float | None | Unset = UNSET
    dhr_2: float | None | Unset = UNSET
    dhr_3: float | None | Unset = UNSET
    dhr_4: float | None | Unset = UNSET
    dhz_1: float | None | Unset = UNSET
    dhz_2: float | None | Unset = UNSET
    dhz_3: float | None | Unset = UNSET
    dhz_4: float | None | Unset = UNSET
    dhz_5: float | None | Unset = UNSET
    dhz_6: float | None | Unset = UNSET
    dm_r: float | None | Unset = UNSET
    dmr_ir: float | None | Unset = UNSET
    edu_deg: float | None | Unset = UNSET
    edu_dip: float | None | Unset = UNSET
    edu_lsed: float | None | Unset = UNSET
    edu_prepri: float | None | Unset = UNSET
    edu_pri: float | None | Unset = UNSET
    edu_sub: float | None | Unset = UNSET
    edu_usec: float | None | Unset = UNSET
    ethn_chi: float | None | Unset = UNSET
    ethn_ind: float | None | Unset = UNSET
    ethn_oth: float | None | Unset = UNSET
    ethn_phi: float | None | Unset = UNSET
    ethn_wh: float | None | Unset = UNSET
    fa_m: float | None | Unset = UNSET
    lf_f: float | None | Unset = UNSET
    lf_m: float | None | Unset = UNSET
    lfpr_f: float | None | Unset = UNSET
    lfpr_m: float | None | Unset = UNSET
    lfpr_t: float | None | Unset = UNSET
    ma_econhh: float | None | Unset = UNSET
    ma_f: float | None | Unset = UNSET
    ma_hh: float | None | Unset = UNSET
    ma_m: float | None | Unset = UNSET
    mearn_xfdh_1: float | None | Unset = UNSET
    mearn_xfdh_2: float | None | Unset = UNSET
    mearn_xfdh_3: float | None | Unset = UNSET
    mearn_xfdh_4: float | None | Unset = UNSET
    mearn_xfdh_5: float | None | Unset = UNSET
    mearn_xfdh_6: float | None | Unset = UNSET
    mearn_xfdh_7: float | None | Unset = UNSET
    mearn_xfdhfw_1: float | None | Unset = UNSET
    mearn_xfdhfw_2: float | None | Unset = UNSET
    mearn_xfdhfw_3: float | None | Unset = UNSET
    mearn_xfdhfw_4: float | None | Unset = UNSET
    mearn_xfdhfw_5: float | None | Unset = UNSET
    mearn_xfdhfw_6: float | None | Unset = UNSET
    mearn_xfdhfw_7: float | None | Unset = UNSET
    mmearn_f: float | None | Unset = UNSET
    mmearn_m: float | None | Unset = UNSET
    mmearn_xfdh_f: float | None | Unset = UNSET
    mmearn_xfdh_m: float | None | Unset = UNSET
    ms_div_f: float | None | Unset = UNSET
    ms_div_m: float | None | Unset = UNSET
    ms_m_f: float | None | Unset = UNSET
    ms_ma_m: float | None | Unset = UNSET
    ms_nm_f: float | None | Unset = UNSET
    ms_nm_m: float | None | Unset = UNSET
    ms_sep_f: float | None | Unset = UNSET
    ms_sep_m: float | None | Unset = UNSET
    ms_win_f: float | None | Unset = UNSET
    ms_win_m: float | None | Unset = UNSET
    nwp_hm: float | None | Unset = UNSET
    nwp_oth: float | None | Unset = UNSET
    nwp_re: float | None | Unset = UNSET
    nwp_st: float | None | Unset = UNSET
    oq_non: float | None | Unset = UNSET
    oq_pri: float | None | Unset = UNSET
    oq_pub: float | None | Unset = UNSET
    oq_s: None | str | Unset = UNSET
    oq_tem: float | None | Unset = UNSET
    pcfa_m: float | None | Unset = UNSET
    pls_diff_hk: float | None | Unset = UNSET
    pls_diff_kln: float | None | Unset = UNSET
    pls_diff_nt: float | None | Unset = UNSET
    pls_same: float | None | Unset = UNSET
    plw_diff_hk: float | None | Unset = UNSET
    plw_diff_kln: float | None | Unset = UNSET
    plw_diff_nt: float | None | Unset = UNSET
    plw_diff_oth: float | None | Unset = UNSET
    plw_hm: float | None | Unset = UNSET
    plw_nofix: float | None | Unset = UNSET
    plw_out: float | None | Unset = UNSET
    plw_same: float | None | Unset = UNSET
    pm_hk: float | None | Unset = UNSET
    pm_kln: float | None | Unset = UNSET
    pm_nt: float | None | Unset = UNSET
    pm_oth: float | None | Unset = UNSET
    pm_out: float | None | Unset = UNSET
    pm_same: float | None | Unset = UNSET
    pm_samearea: float | None | Unset = UNSET
    pop_f: float | None | Unset = UNSET
    pop_m: float | None | Unset = UNSET
    pop_non: float | None | Unset = UNSET
    pop_pri: float | None | Unset = UNSET
    pop_pub: float | None | Unset = UNSET
    pop_s: None | str | Unset = UNSET
    pop_tem: float | None | Unset = UNSET
    readchi_ablepctn: float | None | Unset = UNSET
    readeng_ablepctn: float | None | Unset = UNSET
    s_diff_oth: float | None | Unset = UNSET
    sr: float | None | Unset = UNSET
    t_lf: float | None | Unset = UNSET
    t_ma: float | None | Unset = UNSET
    t_mmearn: float | None | Unset = UNSET
    t_mmearn_xfdh: float | None | Unset = UNSET
    t_nwp: float | None | Unset = UNSET
    t_pop: float | None | Unset = UNSET
    t_wp: float | None | Unset = UNSET
    ul_can: float | None | Unset = UNSET
    ul_eng: float | None | Unset = UNSET
    ul_oth: float | None | Unset = UNSET
    ul_othchi: float | None | Unset = UNSET
    ul_put: float | None | Unset = UNSET
    whr_1: float | None | Unset = UNSET
    whr_2: float | None | Unset = UNSET
    whr_3: float | None | Unset = UNSET
    whr_4: float | None | Unset = UNSET
    whr_5: float | None | Unset = UNSET
    whr_6: float | None | Unset = UNSET
    wp_a: float | None | Unset = UNSET
    wp_b: float | None | Unset = UNSET
    wp_c: float | None | Unset = UNSET
    wp_d: float | None | Unset = UNSET
    wp_e: float | None | Unset = UNSET
    wp_ee: float | None | Unset = UNSET
    wp_er: float | None | Unset = UNSET
    wp_f: float | None | Unset = UNSET
    wp_fw: float | None | Unset = UNSET
    wp_g: float | None | Unset = UNSET
    wp_h: float | None | Unset = UNSET
    wp_i: float | None | Unset = UNSET
    wp_j: float | None | Unset = UNSET
    wp_k: float | None | Unset = UNSET
    wp_l: float | None | Unset = UNSET
    wp_m: float | None | Unset = UNSET
    wp_n: float | None | Unset = UNSET
    wp_o: float | None | Unset = UNSET
    wp_p: float | None | Unset = UNSET
    wp_q: float | None | Unset = UNSET
    wp_r: float | None | Unset = UNSET
    wp_s: float | None | Unset = UNSET
    wp_se: float | None | Unset = UNSET
    wp_t: float | None | Unset = UNSET
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

        dc: float | None | Unset
        if isinstance(self.dc, Unset):
            dc = UNSET
        else:
            dc = self.dc

        dc_chi: None | str | Unset
        if isinstance(self.dc_chi, Unset):
            dc_chi = UNSET
        else:
            dc_chi = self.dc_chi

        dc_class: None | str | Unset
        if isinstance(self.dc_class, Unset):
            dc_class = UNSET
        else:
            dc_class = self.dc_class

        dc_eng: None | str | Unset
        if isinstance(self.dc_eng, Unset):
            dc_eng = UNSET
        else:
            dc_eng = self.dc_eng

        dh: float | None | Unset
        if isinstance(self.dh, Unset):
            dh = UNSET
        else:
            dh = self.dh

        dh_co: float | None | Unset
        if isinstance(self.dh_co, Unset):
            dh_co = UNSET
        else:
            dh_co = self.dh_co

        dh_emp: float | None | Unset
        if isinstance(self.dh_emp, Unset):
            dh_emp = UNSET
        else:
            dh_emp = self.dh_emp

        dh_non: float | None | Unset
        if isinstance(self.dh_non, Unset):
            dh_non = UNSET
        else:
            dh_non = self.dh_non

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

        dh_pri: float | None | Unset
        if isinstance(self.dh_pri, Unset):
            dh_pri = UNSET
        else:
            dh_pri = self.dh_pri

        dh_pub: float | None | Unset
        if isinstance(self.dh_pub, Unset):
            dh_pub = UNSET
        else:
            dh_pub = self.dh_pub

        dh_r0: None | str | Unset
        if isinstance(self.dh_r0, Unset):
            dh_r0 = UNSET
        else:
            dh_r0 = self.dh_r0

        dh_r1: float | None | Unset
        if isinstance(self.dh_r1, Unset):
            dh_r1 = UNSET
        else:
            dh_r1 = self.dh_r1

        dh_r2: float | None | Unset
        if isinstance(self.dh_r2, Unset):
            dh_r2 = UNSET
        else:
            dh_r2 = self.dh_r2

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

        dh_r6: float | None | Unset
        if isinstance(self.dh_r6, Unset):
            dh_r6 = UNSET
        else:
            dh_r6 = self.dh_r6

        dh_rf: float | None | Unset
        if isinstance(self.dh_rf, Unset):
            dh_rf = UNSET
        else:
            dh_rf = self.dh_rf

        dh_s: None | str | Unset
        if isinstance(self.dh_s, Unset):
            dh_s = UNSET
        else:
            dh_s = self.dh_s

        dh_st: float | None | Unset
        if isinstance(self.dh_st, Unset):
            dh_st = UNSET
        else:
            dh_st = self.dh_st

        dh_tem: float | None | Unset
        if isinstance(self.dh_tem, Unset):
            dh_tem = UNSET
        else:
            dh_tem = self.dh_tem

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

        dhc_4: float | None | Unset
        if isinstance(self.dhc_4, Unset):
            dhc_4 = UNSET
        else:
            dhc_4 = self.dhc_4

        dhc_5: float | None | Unset
        if isinstance(self.dhc_5, Unset):
            dhc_5 = UNSET
        else:
            dhc_5 = self.dhc_5

        dhc_6: float | None | Unset
        if isinstance(self.dhc_6, Unset):
            dhc_6 = UNSET
        else:
            dhc_6 = self.dhc_6

        dhc_7: float | None | Unset
        if isinstance(self.dhc_7, Unset):
            dhc_7 = UNSET
        else:
            dhc_7 = self.dhc_7

        dhc_8: float | None | Unset
        if isinstance(self.dhc_8, Unset):
            dhc_8 = UNSET
        else:
            dhc_8 = self.dhc_8

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

        dhi_4: float | None | Unset
        if isinstance(self.dhi_4, Unset):
            dhi_4 = UNSET
        else:
            dhi_4 = self.dhi_4

        dhi_5: float | None | Unset
        if isinstance(self.dhi_5, Unset):
            dhi_5 = UNSET
        else:
            dhi_5 = self.dhi_5

        dhi_6: float | None | Unset
        if isinstance(self.dhi_6, Unset):
            dhi_6 = UNSET
        else:
            dhi_6 = self.dhi_6

        dhi_7: float | None | Unset
        if isinstance(self.dhi_7, Unset):
            dhi_7 = UNSET
        else:
            dhi_7 = self.dhi_7

        dhi_e1: float | None | Unset
        if isinstance(self.dhi_e1, Unset):
            dhi_e1 = UNSET
        else:
            dhi_e1 = self.dhi_e1

        dhi_e2: float | None | Unset
        if isinstance(self.dhi_e2, Unset):
            dhi_e2 = UNSET
        else:
            dhi_e2 = self.dhi_e2

        dhi_e3: float | None | Unset
        if isinstance(self.dhi_e3, Unset):
            dhi_e3 = UNSET
        else:
            dhi_e3 = self.dhi_e3

        dhi_e4: float | None | Unset
        if isinstance(self.dhi_e4, Unset):
            dhi_e4 = UNSET
        else:
            dhi_e4 = self.dhi_e4

        dhi_e5: float | None | Unset
        if isinstance(self.dhi_e5, Unset):
            dhi_e5 = UNSET
        else:
            dhi_e5 = self.dhi_e5

        dhi_e6: float | None | Unset
        if isinstance(self.dhi_e6, Unset):
            dhi_e6 = UNSET
        else:
            dhi_e6 = self.dhi_e6

        dhi_e7: float | None | Unset
        if isinstance(self.dhi_e7, Unset):
            dhi_e7 = UNSET
        else:
            dhi_e7 = self.dhi_e7

        dhm_1: float | None | Unset
        if isinstance(self.dhm_1, Unset):
            dhm_1 = UNSET
        else:
            dhm_1 = self.dhm_1

        dhm_2: float | None | Unset
        if isinstance(self.dhm_2, Unset):
            dhm_2 = UNSET
        else:
            dhm_2 = self.dhm_2

        dhm_3: float | None | Unset
        if isinstance(self.dhm_3, Unset):
            dhm_3 = UNSET
        else:
            dhm_3 = self.dhm_3

        dhm_4: float | None | Unset
        if isinstance(self.dhm_4, Unset):
            dhm_4 = UNSET
        else:
            dhm_4 = self.dhm_4

        dhm_5: float | None | Unset
        if isinstance(self.dhm_5, Unset):
            dhm_5 = UNSET
        else:
            dhm_5 = self.dhm_5

        dhm_6: float | None | Unset
        if isinstance(self.dhm_6, Unset):
            dhm_6 = UNSET
        else:
            dhm_6 = self.dhm_6

        dhm_7: float | None | Unset
        if isinstance(self.dhm_7, Unset):
            dhm_7 = UNSET
        else:
            dhm_7 = self.dhm_7

        dhm_loan: float | None | Unset
        if isinstance(self.dhm_loan, Unset):
            dhm_loan = UNSET
        else:
            dhm_loan = self.dhm_loan

        dhm_lr: float | None | Unset
        if isinstance(self.dhm_lr, Unset):
            dhm_lr = UNSET
        else:
            dhm_lr = self.dhm_lr

        dhr_1: float | None | Unset
        if isinstance(self.dhr_1, Unset):
            dhr_1 = UNSET
        else:
            dhr_1 = self.dhr_1

        dhr_2: float | None | Unset
        if isinstance(self.dhr_2, Unset):
            dhr_2 = UNSET
        else:
            dhr_2 = self.dhr_2

        dhr_3: float | None | Unset
        if isinstance(self.dhr_3, Unset):
            dhr_3 = UNSET
        else:
            dhr_3 = self.dhr_3

        dhr_4: float | None | Unset
        if isinstance(self.dhr_4, Unset):
            dhr_4 = UNSET
        else:
            dhr_4 = self.dhr_4

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

        dhz_5: float | None | Unset
        if isinstance(self.dhz_5, Unset):
            dhz_5 = UNSET
        else:
            dhz_5 = self.dhz_5

        dhz_6: float | None | Unset
        if isinstance(self.dhz_6, Unset):
            dhz_6 = UNSET
        else:
            dhz_6 = self.dhz_6

        dm_r: float | None | Unset
        if isinstance(self.dm_r, Unset):
            dm_r = UNSET
        else:
            dm_r = self.dm_r

        dmr_ir: float | None | Unset
        if isinstance(self.dmr_ir, Unset):
            dmr_ir = UNSET
        else:
            dmr_ir = self.dmr_ir

        edu_deg: float | None | Unset
        if isinstance(self.edu_deg, Unset):
            edu_deg = UNSET
        else:
            edu_deg = self.edu_deg

        edu_dip: float | None | Unset
        if isinstance(self.edu_dip, Unset):
            edu_dip = UNSET
        else:
            edu_dip = self.edu_dip

        edu_lsed: float | None | Unset
        if isinstance(self.edu_lsed, Unset):
            edu_lsed = UNSET
        else:
            edu_lsed = self.edu_lsed

        edu_prepri: float | None | Unset
        if isinstance(self.edu_prepri, Unset):
            edu_prepri = UNSET
        else:
            edu_prepri = self.edu_prepri

        edu_pri: float | None | Unset
        if isinstance(self.edu_pri, Unset):
            edu_pri = UNSET
        else:
            edu_pri = self.edu_pri

        edu_sub: float | None | Unset
        if isinstance(self.edu_sub, Unset):
            edu_sub = UNSET
        else:
            edu_sub = self.edu_sub

        edu_usec: float | None | Unset
        if isinstance(self.edu_usec, Unset):
            edu_usec = UNSET
        else:
            edu_usec = self.edu_usec

        ethn_chi: float | None | Unset
        if isinstance(self.ethn_chi, Unset):
            ethn_chi = UNSET
        else:
            ethn_chi = self.ethn_chi

        ethn_ind: float | None | Unset
        if isinstance(self.ethn_ind, Unset):
            ethn_ind = UNSET
        else:
            ethn_ind = self.ethn_ind

        ethn_oth: float | None | Unset
        if isinstance(self.ethn_oth, Unset):
            ethn_oth = UNSET
        else:
            ethn_oth = self.ethn_oth

        ethn_phi: float | None | Unset
        if isinstance(self.ethn_phi, Unset):
            ethn_phi = UNSET
        else:
            ethn_phi = self.ethn_phi

        ethn_wh: float | None | Unset
        if isinstance(self.ethn_wh, Unset):
            ethn_wh = UNSET
        else:
            ethn_wh = self.ethn_wh

        fa_m: float | None | Unset
        if isinstance(self.fa_m, Unset):
            fa_m = UNSET
        else:
            fa_m = self.fa_m

        lf_f: float | None | Unset
        if isinstance(self.lf_f, Unset):
            lf_f = UNSET
        else:
            lf_f = self.lf_f

        lf_m: float | None | Unset
        if isinstance(self.lf_m, Unset):
            lf_m = UNSET
        else:
            lf_m = self.lf_m

        lfpr_f: float | None | Unset
        if isinstance(self.lfpr_f, Unset):
            lfpr_f = UNSET
        else:
            lfpr_f = self.lfpr_f

        lfpr_m: float | None | Unset
        if isinstance(self.lfpr_m, Unset):
            lfpr_m = UNSET
        else:
            lfpr_m = self.lfpr_m

        lfpr_t: float | None | Unset
        if isinstance(self.lfpr_t, Unset):
            lfpr_t = UNSET
        else:
            lfpr_t = self.lfpr_t

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

        mearn_xfdh_1: float | None | Unset
        if isinstance(self.mearn_xfdh_1, Unset):
            mearn_xfdh_1 = UNSET
        else:
            mearn_xfdh_1 = self.mearn_xfdh_1

        mearn_xfdh_2: float | None | Unset
        if isinstance(self.mearn_xfdh_2, Unset):
            mearn_xfdh_2 = UNSET
        else:
            mearn_xfdh_2 = self.mearn_xfdh_2

        mearn_xfdh_3: float | None | Unset
        if isinstance(self.mearn_xfdh_3, Unset):
            mearn_xfdh_3 = UNSET
        else:
            mearn_xfdh_3 = self.mearn_xfdh_3

        mearn_xfdh_4: float | None | Unset
        if isinstance(self.mearn_xfdh_4, Unset):
            mearn_xfdh_4 = UNSET
        else:
            mearn_xfdh_4 = self.mearn_xfdh_4

        mearn_xfdh_5: float | None | Unset
        if isinstance(self.mearn_xfdh_5, Unset):
            mearn_xfdh_5 = UNSET
        else:
            mearn_xfdh_5 = self.mearn_xfdh_5

        mearn_xfdh_6: float | None | Unset
        if isinstance(self.mearn_xfdh_6, Unset):
            mearn_xfdh_6 = UNSET
        else:
            mearn_xfdh_6 = self.mearn_xfdh_6

        mearn_xfdh_7: float | None | Unset
        if isinstance(self.mearn_xfdh_7, Unset):
            mearn_xfdh_7 = UNSET
        else:
            mearn_xfdh_7 = self.mearn_xfdh_7

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

        mearn_xfdhfw_4: float | None | Unset
        if isinstance(self.mearn_xfdhfw_4, Unset):
            mearn_xfdhfw_4 = UNSET
        else:
            mearn_xfdhfw_4 = self.mearn_xfdhfw_4

        mearn_xfdhfw_5: float | None | Unset
        if isinstance(self.mearn_xfdhfw_5, Unset):
            mearn_xfdhfw_5 = UNSET
        else:
            mearn_xfdhfw_5 = self.mearn_xfdhfw_5

        mearn_xfdhfw_6: float | None | Unset
        if isinstance(self.mearn_xfdhfw_6, Unset):
            mearn_xfdhfw_6 = UNSET
        else:
            mearn_xfdhfw_6 = self.mearn_xfdhfw_6

        mearn_xfdhfw_7: float | None | Unset
        if isinstance(self.mearn_xfdhfw_7, Unset):
            mearn_xfdhfw_7 = UNSET
        else:
            mearn_xfdhfw_7 = self.mearn_xfdhfw_7

        mmearn_f: float | None | Unset
        if isinstance(self.mmearn_f, Unset):
            mmearn_f = UNSET
        else:
            mmearn_f = self.mmearn_f

        mmearn_m: float | None | Unset
        if isinstance(self.mmearn_m, Unset):
            mmearn_m = UNSET
        else:
            mmearn_m = self.mmearn_m

        mmearn_xfdh_f: float | None | Unset
        if isinstance(self.mmearn_xfdh_f, Unset):
            mmearn_xfdh_f = UNSET
        else:
            mmearn_xfdh_f = self.mmearn_xfdh_f

        mmearn_xfdh_m: float | None | Unset
        if isinstance(self.mmearn_xfdh_m, Unset):
            mmearn_xfdh_m = UNSET
        else:
            mmearn_xfdh_m = self.mmearn_xfdh_m

        ms_div_f: float | None | Unset
        if isinstance(self.ms_div_f, Unset):
            ms_div_f = UNSET
        else:
            ms_div_f = self.ms_div_f

        ms_div_m: float | None | Unset
        if isinstance(self.ms_div_m, Unset):
            ms_div_m = UNSET
        else:
            ms_div_m = self.ms_div_m

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

        ms_sep_f: float | None | Unset
        if isinstance(self.ms_sep_f, Unset):
            ms_sep_f = UNSET
        else:
            ms_sep_f = self.ms_sep_f

        ms_sep_m: float | None | Unset
        if isinstance(self.ms_sep_m, Unset):
            ms_sep_m = UNSET
        else:
            ms_sep_m = self.ms_sep_m

        ms_win_f: float | None | Unset
        if isinstance(self.ms_win_f, Unset):
            ms_win_f = UNSET
        else:
            ms_win_f = self.ms_win_f

        ms_win_m: float | None | Unset
        if isinstance(self.ms_win_m, Unset):
            ms_win_m = UNSET
        else:
            ms_win_m = self.ms_win_m

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

        oq_non: float | None | Unset
        if isinstance(self.oq_non, Unset):
            oq_non = UNSET
        else:
            oq_non = self.oq_non

        oq_pri: float | None | Unset
        if isinstance(self.oq_pri, Unset):
            oq_pri = UNSET
        else:
            oq_pri = self.oq_pri

        oq_pub: float | None | Unset
        if isinstance(self.oq_pub, Unset):
            oq_pub = UNSET
        else:
            oq_pub = self.oq_pub

        oq_s: None | str | Unset
        if isinstance(self.oq_s, Unset):
            oq_s = UNSET
        else:
            oq_s = self.oq_s

        oq_tem: float | None | Unset
        if isinstance(self.oq_tem, Unset):
            oq_tem = UNSET
        else:
            oq_tem = self.oq_tem

        pcfa_m: float | None | Unset
        if isinstance(self.pcfa_m, Unset):
            pcfa_m = UNSET
        else:
            pcfa_m = self.pcfa_m

        pls_diff_hk: float | None | Unset
        if isinstance(self.pls_diff_hk, Unset):
            pls_diff_hk = UNSET
        else:
            pls_diff_hk = self.pls_diff_hk

        pls_diff_kln: float | None | Unset
        if isinstance(self.pls_diff_kln, Unset):
            pls_diff_kln = UNSET
        else:
            pls_diff_kln = self.pls_diff_kln

        pls_diff_nt: float | None | Unset
        if isinstance(self.pls_diff_nt, Unset):
            pls_diff_nt = UNSET
        else:
            pls_diff_nt = self.pls_diff_nt

        pls_same: float | None | Unset
        if isinstance(self.pls_same, Unset):
            pls_same = UNSET
        else:
            pls_same = self.pls_same

        plw_diff_hk: float | None | Unset
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

        plw_diff_oth: float | None | Unset
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

        plw_out: float | None | Unset
        if isinstance(self.plw_out, Unset):
            plw_out = UNSET
        else:
            plw_out = self.plw_out

        plw_same: float | None | Unset
        if isinstance(self.plw_same, Unset):
            plw_same = UNSET
        else:
            plw_same = self.plw_same

        pm_hk: float | None | Unset
        if isinstance(self.pm_hk, Unset):
            pm_hk = UNSET
        else:
            pm_hk = self.pm_hk

        pm_kln: float | None | Unset
        if isinstance(self.pm_kln, Unset):
            pm_kln = UNSET
        else:
            pm_kln = self.pm_kln

        pm_nt: float | None | Unset
        if isinstance(self.pm_nt, Unset):
            pm_nt = UNSET
        else:
            pm_nt = self.pm_nt

        pm_oth: float | None | Unset
        if isinstance(self.pm_oth, Unset):
            pm_oth = UNSET
        else:
            pm_oth = self.pm_oth

        pm_out: float | None | Unset
        if isinstance(self.pm_out, Unset):
            pm_out = UNSET
        else:
            pm_out = self.pm_out

        pm_same: float | None | Unset
        if isinstance(self.pm_same, Unset):
            pm_same = UNSET
        else:
            pm_same = self.pm_same

        pm_samearea: float | None | Unset
        if isinstance(self.pm_samearea, Unset):
            pm_samearea = UNSET
        else:
            pm_samearea = self.pm_samearea

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

        pop_non: float | None | Unset
        if isinstance(self.pop_non, Unset):
            pop_non = UNSET
        else:
            pop_non = self.pop_non

        pop_pri: float | None | Unset
        if isinstance(self.pop_pri, Unset):
            pop_pri = UNSET
        else:
            pop_pri = self.pop_pri

        pop_pub: float | None | Unset
        if isinstance(self.pop_pub, Unset):
            pop_pub = UNSET
        else:
            pop_pub = self.pop_pub

        pop_s: None | str | Unset
        if isinstance(self.pop_s, Unset):
            pop_s = UNSET
        else:
            pop_s = self.pop_s

        pop_tem: float | None | Unset
        if isinstance(self.pop_tem, Unset):
            pop_tem = UNSET
        else:
            pop_tem = self.pop_tem

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

        s_diff_oth: float | None | Unset
        if isinstance(self.s_diff_oth, Unset):
            s_diff_oth = UNSET
        else:
            s_diff_oth = self.s_diff_oth

        sr: float | None | Unset
        if isinstance(self.sr, Unset):
            sr = UNSET
        else:
            sr = self.sr

        t_lf: float | None | Unset
        if isinstance(self.t_lf, Unset):
            t_lf = UNSET
        else:
            t_lf = self.t_lf

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

        ul_eng: float | None | Unset
        if isinstance(self.ul_eng, Unset):
            ul_eng = UNSET
        else:
            ul_eng = self.ul_eng

        ul_oth: float | None | Unset
        if isinstance(self.ul_oth, Unset):
            ul_oth = UNSET
        else:
            ul_oth = self.ul_oth

        ul_othchi: float | None | Unset
        if isinstance(self.ul_othchi, Unset):
            ul_othchi = UNSET
        else:
            ul_othchi = self.ul_othchi

        ul_put: float | None | Unset
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

        wp_fw: float | None | Unset
        if isinstance(self.wp_fw, Unset):
            wp_fw = UNSET
        else:
            wp_fw = self.wp_fw

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

        wp_j: float | None | Unset
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

        wp_m: float | None | Unset
        if isinstance(self.wp_m, Unset):
            wp_m = UNSET
        else:
            wp_m = self.wp_m

        wp_n: float | None | Unset
        if isinstance(self.wp_n, Unset):
            wp_n = UNSET
        else:
            wp_n = self.wp_n

        wp_o: float | None | Unset
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

        wp_t: float | None | Unset
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
        if dc is not UNSET:
            field_dict["dc"] = dc
        if dc_chi is not UNSET:
            field_dict["dc_chi"] = dc_chi
        if dc_class is not UNSET:
            field_dict["dc_class"] = dc_class
        if dc_eng is not UNSET:
            field_dict["dc_eng"] = dc_eng
        if dh is not UNSET:
            field_dict["dh"] = dh
        if dh_co is not UNSET:
            field_dict["dh_co"] = dh_co
        if dh_emp is not UNSET:
            field_dict["dh_emp"] = dh_emp
        if dh_non is not UNSET:
            field_dict["dh_non"] = dh_non
        if dh_ocm is not UNSET:
            field_dict["dh_ocm"] = dh_ocm
        if dh_ocwm is not UNSET:
            field_dict["dh_ocwm"] = dh_ocwm
        if dh_pri is not UNSET:
            field_dict["dh_pri"] = dh_pri
        if dh_pub is not UNSET:
            field_dict["dh_pub"] = dh_pub
        if dh_r0 is not UNSET:
            field_dict["dh_r0"] = dh_r0
        if dh_r1 is not UNSET:
            field_dict["dh_r1"] = dh_r1
        if dh_r2 is not UNSET:
            field_dict["dh_r2"] = dh_r2
        if dh_r3 is not UNSET:
            field_dict["dh_r3"] = dh_r3
        if dh_r4 is not UNSET:
            field_dict["dh_r4"] = dh_r4
        if dh_r5 is not UNSET:
            field_dict["dh_r5"] = dh_r5
        if dh_r6 is not UNSET:
            field_dict["dh_r6"] = dh_r6
        if dh_rf is not UNSET:
            field_dict["dh_rf"] = dh_rf
        if dh_s is not UNSET:
            field_dict["dh_s"] = dh_s
        if dh_st is not UNSET:
            field_dict["dh_st"] = dh_st
        if dh_tem is not UNSET:
            field_dict["dh_tem"] = dh_tem
        if dhc_1 is not UNSET:
            field_dict["dhc_1"] = dhc_1
        if dhc_2 is not UNSET:
            field_dict["dhc_2"] = dhc_2
        if dhc_3 is not UNSET:
            field_dict["dhc_3"] = dhc_3
        if dhc_4 is not UNSET:
            field_dict["dhc_4"] = dhc_4
        if dhc_5 is not UNSET:
            field_dict["dhc_5"] = dhc_5
        if dhc_6 is not UNSET:
            field_dict["dhc_6"] = dhc_6
        if dhc_7 is not UNSET:
            field_dict["dhc_7"] = dhc_7
        if dhc_8 is not UNSET:
            field_dict["dhc_8"] = dhc_8
        if dhi_1 is not UNSET:
            field_dict["dhi_1"] = dhi_1
        if dhi_2 is not UNSET:
            field_dict["dhi_2"] = dhi_2
        if dhi_3 is not UNSET:
            field_dict["dhi_3"] = dhi_3
        if dhi_4 is not UNSET:
            field_dict["dhi_4"] = dhi_4
        if dhi_5 is not UNSET:
            field_dict["dhi_5"] = dhi_5
        if dhi_6 is not UNSET:
            field_dict["dhi_6"] = dhi_6
        if dhi_7 is not UNSET:
            field_dict["dhi_7"] = dhi_7
        if dhi_e1 is not UNSET:
            field_dict["dhi_e1"] = dhi_e1
        if dhi_e2 is not UNSET:
            field_dict["dhi_e2"] = dhi_e2
        if dhi_e3 is not UNSET:
            field_dict["dhi_e3"] = dhi_e3
        if dhi_e4 is not UNSET:
            field_dict["dhi_e4"] = dhi_e4
        if dhi_e5 is not UNSET:
            field_dict["dhi_e5"] = dhi_e5
        if dhi_e6 is not UNSET:
            field_dict["dhi_e6"] = dhi_e6
        if dhi_e7 is not UNSET:
            field_dict["dhi_e7"] = dhi_e7
        if dhm_1 is not UNSET:
            field_dict["dhm_1"] = dhm_1
        if dhm_2 is not UNSET:
            field_dict["dhm_2"] = dhm_2
        if dhm_3 is not UNSET:
            field_dict["dhm_3"] = dhm_3
        if dhm_4 is not UNSET:
            field_dict["dhm_4"] = dhm_4
        if dhm_5 is not UNSET:
            field_dict["dhm_5"] = dhm_5
        if dhm_6 is not UNSET:
            field_dict["dhm_6"] = dhm_6
        if dhm_7 is not UNSET:
            field_dict["dhm_7"] = dhm_7
        if dhm_loan is not UNSET:
            field_dict["dhm_loan"] = dhm_loan
        if dhm_lr is not UNSET:
            field_dict["dhm_lr"] = dhm_lr
        if dhr_1 is not UNSET:
            field_dict["dhr_1"] = dhr_1
        if dhr_2 is not UNSET:
            field_dict["dhr_2"] = dhr_2
        if dhr_3 is not UNSET:
            field_dict["dhr_3"] = dhr_3
        if dhr_4 is not UNSET:
            field_dict["dhr_4"] = dhr_4
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
        if edu_deg is not UNSET:
            field_dict["edu_deg"] = edu_deg
        if edu_dip is not UNSET:
            field_dict["edu_dip"] = edu_dip
        if edu_lsed is not UNSET:
            field_dict["edu_lsed"] = edu_lsed
        if edu_prepri is not UNSET:
            field_dict["edu_prepri"] = edu_prepri
        if edu_pri is not UNSET:
            field_dict["edu_pri"] = edu_pri
        if edu_sub is not UNSET:
            field_dict["edu_sub"] = edu_sub
        if edu_usec is not UNSET:
            field_dict["edu_usec"] = edu_usec
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
        if lf_f is not UNSET:
            field_dict["lf_f"] = lf_f
        if lf_m is not UNSET:
            field_dict["lf_m"] = lf_m
        if lfpr_f is not UNSET:
            field_dict["lfpr_f"] = lfpr_f
        if lfpr_m is not UNSET:
            field_dict["lfpr_m"] = lfpr_m
        if lfpr_t is not UNSET:
            field_dict["lfpr_t"] = lfpr_t
        if ma_econhh is not UNSET:
            field_dict["ma_econhh"] = ma_econhh
        if ma_f is not UNSET:
            field_dict["ma_f"] = ma_f
        if ma_hh is not UNSET:
            field_dict["ma_hh"] = ma_hh
        if ma_m is not UNSET:
            field_dict["ma_m"] = ma_m
        if mearn_xfdh_1 is not UNSET:
            field_dict["mearn_xfdh_1"] = mearn_xfdh_1
        if mearn_xfdh_2 is not UNSET:
            field_dict["mearn_xfdh_2"] = mearn_xfdh_2
        if mearn_xfdh_3 is not UNSET:
            field_dict["mearn_xfdh_3"] = mearn_xfdh_3
        if mearn_xfdh_4 is not UNSET:
            field_dict["mearn_xfdh_4"] = mearn_xfdh_4
        if mearn_xfdh_5 is not UNSET:
            field_dict["mearn_xfdh_5"] = mearn_xfdh_5
        if mearn_xfdh_6 is not UNSET:
            field_dict["mearn_xfdh_6"] = mearn_xfdh_6
        if mearn_xfdh_7 is not UNSET:
            field_dict["mearn_xfdh_7"] = mearn_xfdh_7
        if mearn_xfdhfw_1 is not UNSET:
            field_dict["mearn_xfdhfw_1"] = mearn_xfdhfw_1
        if mearn_xfdhfw_2 is not UNSET:
            field_dict["mearn_xfdhfw_2"] = mearn_xfdhfw_2
        if mearn_xfdhfw_3 is not UNSET:
            field_dict["mearn_xfdhfw_3"] = mearn_xfdhfw_3
        if mearn_xfdhfw_4 is not UNSET:
            field_dict["mearn_xfdhfw_4"] = mearn_xfdhfw_4
        if mearn_xfdhfw_5 is not UNSET:
            field_dict["mearn_xfdhfw_5"] = mearn_xfdhfw_5
        if mearn_xfdhfw_6 is not UNSET:
            field_dict["mearn_xfdhfw_6"] = mearn_xfdhfw_6
        if mearn_xfdhfw_7 is not UNSET:
            field_dict["mearn_xfdhfw_7"] = mearn_xfdhfw_7
        if mmearn_f is not UNSET:
            field_dict["mmearn_f"] = mmearn_f
        if mmearn_m is not UNSET:
            field_dict["mmearn_m"] = mmearn_m
        if mmearn_xfdh_f is not UNSET:
            field_dict["mmearn_xfdh_f"] = mmearn_xfdh_f
        if mmearn_xfdh_m is not UNSET:
            field_dict["mmearn_xfdh_m"] = mmearn_xfdh_m
        if ms_div_f is not UNSET:
            field_dict["ms_div_f"] = ms_div_f
        if ms_div_m is not UNSET:
            field_dict["ms_div_m"] = ms_div_m
        if ms_m_f is not UNSET:
            field_dict["ms_m_f"] = ms_m_f
        if ms_ma_m is not UNSET:
            field_dict["ms_ma_m"] = ms_ma_m
        if ms_nm_f is not UNSET:
            field_dict["ms_nm_f"] = ms_nm_f
        if ms_nm_m is not UNSET:
            field_dict["ms_nm_m"] = ms_nm_m
        if ms_sep_f is not UNSET:
            field_dict["ms_sep_f"] = ms_sep_f
        if ms_sep_m is not UNSET:
            field_dict["ms_sep_m"] = ms_sep_m
        if ms_win_f is not UNSET:
            field_dict["ms_win_f"] = ms_win_f
        if ms_win_m is not UNSET:
            field_dict["ms_win_m"] = ms_win_m
        if nwp_hm is not UNSET:
            field_dict["nwp_hm"] = nwp_hm
        if nwp_oth is not UNSET:
            field_dict["nwp_oth"] = nwp_oth
        if nwp_re is not UNSET:
            field_dict["nwp_re"] = nwp_re
        if nwp_st is not UNSET:
            field_dict["nwp_st"] = nwp_st
        if oq_non is not UNSET:
            field_dict["oq_non"] = oq_non
        if oq_pri is not UNSET:
            field_dict["oq_pri"] = oq_pri
        if oq_pub is not UNSET:
            field_dict["oq_pub"] = oq_pub
        if oq_s is not UNSET:
            field_dict["oq_s"] = oq_s
        if oq_tem is not UNSET:
            field_dict["oq_tem"] = oq_tem
        if pcfa_m is not UNSET:
            field_dict["pcfa_m"] = pcfa_m
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
        if pm_hk is not UNSET:
            field_dict["pm_hk"] = pm_hk
        if pm_kln is not UNSET:
            field_dict["pm_kln"] = pm_kln
        if pm_nt is not UNSET:
            field_dict["pm_nt"] = pm_nt
        if pm_oth is not UNSET:
            field_dict["pm_oth"] = pm_oth
        if pm_out is not UNSET:
            field_dict["pm_out"] = pm_out
        if pm_same is not UNSET:
            field_dict["pm_same"] = pm_same
        if pm_samearea is not UNSET:
            field_dict["pm_samearea"] = pm_samearea
        if pop_f is not UNSET:
            field_dict["pop_f"] = pop_f
        if pop_m is not UNSET:
            field_dict["pop_m"] = pop_m
        if pop_non is not UNSET:
            field_dict["pop_non"] = pop_non
        if pop_pri is not UNSET:
            field_dict["pop_pri"] = pop_pri
        if pop_pub is not UNSET:
            field_dict["pop_pub"] = pop_pub
        if pop_s is not UNSET:
            field_dict["pop_s"] = pop_s
        if pop_tem is not UNSET:
            field_dict["pop_tem"] = pop_tem
        if readchi_ablepctn is not UNSET:
            field_dict["readchi_ablepctn"] = readchi_ablepctn
        if readeng_ablepctn is not UNSET:
            field_dict["readeng_ablepctn"] = readeng_ablepctn
        if s_diff_oth is not UNSET:
            field_dict["s_diff_oth"] = s_diff_oth
        if sr is not UNSET:
            field_dict["sr"] = sr
        if t_lf is not UNSET:
            field_dict["t_lf"] = t_lf
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

        def _parse_dc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dc = _parse_dc(d.pop("dc", UNSET))

        def _parse_dc_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_chi = _parse_dc_chi(d.pop("dc_chi", UNSET))

        def _parse_dc_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_class = _parse_dc_class(d.pop("dc_class", UNSET))

        def _parse_dc_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_eng = _parse_dc_eng(d.pop("dc_eng", UNSET))

        def _parse_dh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh = _parse_dh(d.pop("dh", UNSET))

        def _parse_dh_co(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_co = _parse_dh_co(d.pop("dh_co", UNSET))

        def _parse_dh_emp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_emp = _parse_dh_emp(d.pop("dh_emp", UNSET))

        def _parse_dh_non(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_non = _parse_dh_non(d.pop("dh_non", UNSET))

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

        def _parse_dh_pri(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_pri = _parse_dh_pri(d.pop("dh_pri", UNSET))

        def _parse_dh_pub(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_pub = _parse_dh_pub(d.pop("dh_pub", UNSET))

        def _parse_dh_r0(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_r0 = _parse_dh_r0(d.pop("dh_r0", UNSET))

        def _parse_dh_r1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_r1 = _parse_dh_r1(d.pop("dh_r1", UNSET))

        def _parse_dh_r2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_r2 = _parse_dh_r2(d.pop("dh_r2", UNSET))

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

        def _parse_dh_r6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_r6 = _parse_dh_r6(d.pop("dh_r6", UNSET))

        def _parse_dh_rf(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_rf = _parse_dh_rf(d.pop("dh_rf", UNSET))

        def _parse_dh_s(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_s = _parse_dh_s(d.pop("dh_s", UNSET))

        def _parse_dh_st(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_st = _parse_dh_st(d.pop("dh_st", UNSET))

        def _parse_dh_tem(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_tem = _parse_dh_tem(d.pop("dh_tem", UNSET))

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

        def _parse_dhc_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_4 = _parse_dhc_4(d.pop("dhc_4", UNSET))

        def _parse_dhc_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_5 = _parse_dhc_5(d.pop("dhc_5", UNSET))

        def _parse_dhc_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_6 = _parse_dhc_6(d.pop("dhc_6", UNSET))

        def _parse_dhc_7(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_7 = _parse_dhc_7(d.pop("dhc_7", UNSET))

        def _parse_dhc_8(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_8 = _parse_dhc_8(d.pop("dhc_8", UNSET))

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

        def _parse_dhi_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_4 = _parse_dhi_4(d.pop("dhi_4", UNSET))

        def _parse_dhi_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_5 = _parse_dhi_5(d.pop("dhi_5", UNSET))

        def _parse_dhi_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_6 = _parse_dhi_6(d.pop("dhi_6", UNSET))

        def _parse_dhi_7(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_7 = _parse_dhi_7(d.pop("dhi_7", UNSET))

        def _parse_dhi_e1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e1 = _parse_dhi_e1(d.pop("dhi_e1", UNSET))

        def _parse_dhi_e2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e2 = _parse_dhi_e2(d.pop("dhi_e2", UNSET))

        def _parse_dhi_e3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e3 = _parse_dhi_e3(d.pop("dhi_e3", UNSET))

        def _parse_dhi_e4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e4 = _parse_dhi_e4(d.pop("dhi_e4", UNSET))

        def _parse_dhi_e5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e5 = _parse_dhi_e5(d.pop("dhi_e5", UNSET))

        def _parse_dhi_e6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e6 = _parse_dhi_e6(d.pop("dhi_e6", UNSET))

        def _parse_dhi_e7(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e7 = _parse_dhi_e7(d.pop("dhi_e7", UNSET))

        def _parse_dhm_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhm_1 = _parse_dhm_1(d.pop("dhm_1", UNSET))

        def _parse_dhm_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhm_2 = _parse_dhm_2(d.pop("dhm_2", UNSET))

        def _parse_dhm_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhm_3 = _parse_dhm_3(d.pop("dhm_3", UNSET))

        def _parse_dhm_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhm_4 = _parse_dhm_4(d.pop("dhm_4", UNSET))

        def _parse_dhm_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhm_5 = _parse_dhm_5(d.pop("dhm_5", UNSET))

        def _parse_dhm_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhm_6 = _parse_dhm_6(d.pop("dhm_6", UNSET))

        def _parse_dhm_7(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhm_7 = _parse_dhm_7(d.pop("dhm_7", UNSET))

        def _parse_dhm_loan(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhm_loan = _parse_dhm_loan(d.pop("dhm_loan", UNSET))

        def _parse_dhm_lr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhm_lr = _parse_dhm_lr(d.pop("dhm_lr", UNSET))

        def _parse_dhr_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhr_1 = _parse_dhr_1(d.pop("dhr_1", UNSET))

        def _parse_dhr_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhr_2 = _parse_dhr_2(d.pop("dhr_2", UNSET))

        def _parse_dhr_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhr_3 = _parse_dhr_3(d.pop("dhr_3", UNSET))

        def _parse_dhr_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhr_4 = _parse_dhr_4(d.pop("dhr_4", UNSET))

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

        def _parse_dhz_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_5 = _parse_dhz_5(d.pop("dhz_5", UNSET))

        def _parse_dhz_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_6 = _parse_dhz_6(d.pop("dhz_6", UNSET))

        def _parse_dm_r(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dm_r = _parse_dm_r(d.pop("dm_r", UNSET))

        def _parse_dmr_ir(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dmr_ir = _parse_dmr_ir(d.pop("dmr_ir", UNSET))

        def _parse_edu_deg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_deg = _parse_edu_deg(d.pop("edu_deg", UNSET))

        def _parse_edu_dip(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_dip = _parse_edu_dip(d.pop("edu_dip", UNSET))

        def _parse_edu_lsed(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_lsed = _parse_edu_lsed(d.pop("edu_lsed", UNSET))

        def _parse_edu_prepri(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_prepri = _parse_edu_prepri(d.pop("edu_prepri", UNSET))

        def _parse_edu_pri(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_pri = _parse_edu_pri(d.pop("edu_pri", UNSET))

        def _parse_edu_sub(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_sub = _parse_edu_sub(d.pop("edu_sub", UNSET))

        def _parse_edu_usec(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        edu_usec = _parse_edu_usec(d.pop("edu_usec", UNSET))

        def _parse_ethn_chi(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ethn_chi = _parse_ethn_chi(d.pop("ethn_chi", UNSET))

        def _parse_ethn_ind(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ethn_ind = _parse_ethn_ind(d.pop("ethn_ind", UNSET))

        def _parse_ethn_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ethn_oth = _parse_ethn_oth(d.pop("ethn_oth", UNSET))

        def _parse_ethn_phi(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ethn_phi = _parse_ethn_phi(d.pop("ethn_phi", UNSET))

        def _parse_ethn_wh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ethn_wh = _parse_ethn_wh(d.pop("ethn_wh", UNSET))

        def _parse_fa_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fa_m = _parse_fa_m(d.pop("fa_m", UNSET))

        def _parse_lf_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_f = _parse_lf_f(d.pop("lf_f", UNSET))

        def _parse_lf_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_m = _parse_lf_m(d.pop("lf_m", UNSET))

        def _parse_lfpr_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_f = _parse_lfpr_f(d.pop("lfpr_f", UNSET))

        def _parse_lfpr_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_m = _parse_lfpr_m(d.pop("lfpr_m", UNSET))

        def _parse_lfpr_t(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_t = _parse_lfpr_t(d.pop("lfpr_t", UNSET))

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

        def _parse_mearn_xfdh_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdh_1 = _parse_mearn_xfdh_1(d.pop("mearn_xfdh_1", UNSET))

        def _parse_mearn_xfdh_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdh_2 = _parse_mearn_xfdh_2(d.pop("mearn_xfdh_2", UNSET))

        def _parse_mearn_xfdh_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdh_3 = _parse_mearn_xfdh_3(d.pop("mearn_xfdh_3", UNSET))

        def _parse_mearn_xfdh_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdh_4 = _parse_mearn_xfdh_4(d.pop("mearn_xfdh_4", UNSET))

        def _parse_mearn_xfdh_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdh_5 = _parse_mearn_xfdh_5(d.pop("mearn_xfdh_5", UNSET))

        def _parse_mearn_xfdh_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdh_6 = _parse_mearn_xfdh_6(d.pop("mearn_xfdh_6", UNSET))

        def _parse_mearn_xfdh_7(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdh_7 = _parse_mearn_xfdh_7(d.pop("mearn_xfdh_7", UNSET))

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

        def _parse_mearn_xfdhfw_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdhfw_4 = _parse_mearn_xfdhfw_4(d.pop("mearn_xfdhfw_4", UNSET))

        def _parse_mearn_xfdhfw_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdhfw_5 = _parse_mearn_xfdhfw_5(d.pop("mearn_xfdhfw_5", UNSET))

        def _parse_mearn_xfdhfw_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdhfw_6 = _parse_mearn_xfdhfw_6(d.pop("mearn_xfdhfw_6", UNSET))

        def _parse_mearn_xfdhfw_7(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mearn_xfdhfw_7 = _parse_mearn_xfdhfw_7(d.pop("mearn_xfdhfw_7", UNSET))

        def _parse_mmearn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mmearn_f = _parse_mmearn_f(d.pop("mmearn_f", UNSET))

        def _parse_mmearn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mmearn_m = _parse_mmearn_m(d.pop("mmearn_m", UNSET))

        def _parse_mmearn_xfdh_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mmearn_xfdh_f = _parse_mmearn_xfdh_f(d.pop("mmearn_xfdh_f", UNSET))

        def _parse_mmearn_xfdh_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mmearn_xfdh_m = _parse_mmearn_xfdh_m(d.pop("mmearn_xfdh_m", UNSET))

        def _parse_ms_div_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_div_f = _parse_ms_div_f(d.pop("ms_div_f", UNSET))

        def _parse_ms_div_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_div_m = _parse_ms_div_m(d.pop("ms_div_m", UNSET))

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

        def _parse_ms_sep_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_sep_f = _parse_ms_sep_f(d.pop("ms_sep_f", UNSET))

        def _parse_ms_sep_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_sep_m = _parse_ms_sep_m(d.pop("ms_sep_m", UNSET))

        def _parse_ms_win_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_win_f = _parse_ms_win_f(d.pop("ms_win_f", UNSET))

        def _parse_ms_win_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_win_m = _parse_ms_win_m(d.pop("ms_win_m", UNSET))

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

        def _parse_oq_non(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        oq_non = _parse_oq_non(d.pop("oq_non", UNSET))

        def _parse_oq_pri(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        oq_pri = _parse_oq_pri(d.pop("oq_pri", UNSET))

        def _parse_oq_pub(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        oq_pub = _parse_oq_pub(d.pop("oq_pub", UNSET))

        def _parse_oq_s(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        oq_s = _parse_oq_s(d.pop("oq_s", UNSET))

        def _parse_oq_tem(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        oq_tem = _parse_oq_tem(d.pop("oq_tem", UNSET))

        def _parse_pcfa_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pcfa_m = _parse_pcfa_m(d.pop("pcfa_m", UNSET))

        def _parse_pls_diff_hk(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pls_diff_hk = _parse_pls_diff_hk(d.pop("pls_diff_hk", UNSET))

        def _parse_pls_diff_kln(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pls_diff_kln = _parse_pls_diff_kln(d.pop("pls_diff_kln", UNSET))

        def _parse_pls_diff_nt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pls_diff_nt = _parse_pls_diff_nt(d.pop("pls_diff_nt", UNSET))

        def _parse_pls_same(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pls_same = _parse_pls_same(d.pop("pls_same", UNSET))

        def _parse_plw_diff_hk(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

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

        def _parse_plw_diff_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

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

        def _parse_plw_out(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        plw_out = _parse_plw_out(d.pop("plw_out", UNSET))

        def _parse_plw_same(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        plw_same = _parse_plw_same(d.pop("plw_same", UNSET))

        def _parse_pm_hk(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_hk = _parse_pm_hk(d.pop("pm_hk", UNSET))

        def _parse_pm_kln(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_kln = _parse_pm_kln(d.pop("pm_kln", UNSET))

        def _parse_pm_nt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_nt = _parse_pm_nt(d.pop("pm_nt", UNSET))

        def _parse_pm_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_oth = _parse_pm_oth(d.pop("pm_oth", UNSET))

        def _parse_pm_out(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_out = _parse_pm_out(d.pop("pm_out", UNSET))

        def _parse_pm_same(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_same = _parse_pm_same(d.pop("pm_same", UNSET))

        def _parse_pm_samearea(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_samearea = _parse_pm_samearea(d.pop("pm_samearea", UNSET))

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

        def _parse_pop_non(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pop_non = _parse_pop_non(d.pop("pop_non", UNSET))

        def _parse_pop_pri(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pop_pri = _parse_pop_pri(d.pop("pop_pri", UNSET))

        def _parse_pop_pub(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pop_pub = _parse_pop_pub(d.pop("pop_pub", UNSET))

        def _parse_pop_s(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pop_s = _parse_pop_s(d.pop("pop_s", UNSET))

        def _parse_pop_tem(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pop_tem = _parse_pop_tem(d.pop("pop_tem", UNSET))

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

        def _parse_s_diff_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        s_diff_oth = _parse_s_diff_oth(d.pop("s_diff_oth", UNSET))

        def _parse_sr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sr = _parse_sr(d.pop("sr", UNSET))

        def _parse_t_lf(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_lf = _parse_t_lf(d.pop("t_lf", UNSET))

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

        def _parse_ul_eng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ul_eng = _parse_ul_eng(d.pop("ul_eng", UNSET))

        def _parse_ul_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ul_oth = _parse_ul_oth(d.pop("ul_oth", UNSET))

        def _parse_ul_othchi(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ul_othchi = _parse_ul_othchi(d.pop("ul_othchi", UNSET))

        def _parse_ul_put(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

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

        def _parse_wp_fw(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_fw = _parse_wp_fw(d.pop("wp_fw", UNSET))

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

        def _parse_wp_j(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

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

        def _parse_wp_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_m = _parse_wp_m(d.pop("wp_m", UNSET))

        def _parse_wp_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_n = _parse_wp_n(d.pop("wp_n", UNSET))

        def _parse_wp_o(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

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

        def _parse_wp_t(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

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
            dc=dc,
            dc_chi=dc_chi,
            dc_class=dc_class,
            dc_eng=dc_eng,
            dh=dh,
            dh_co=dh_co,
            dh_emp=dh_emp,
            dh_non=dh_non,
            dh_ocm=dh_ocm,
            dh_ocwm=dh_ocwm,
            dh_pri=dh_pri,
            dh_pub=dh_pub,
            dh_r0=dh_r0,
            dh_r1=dh_r1,
            dh_r2=dh_r2,
            dh_r3=dh_r3,
            dh_r4=dh_r4,
            dh_r5=dh_r5,
            dh_r6=dh_r6,
            dh_rf=dh_rf,
            dh_s=dh_s,
            dh_st=dh_st,
            dh_tem=dh_tem,
            dhc_1=dhc_1,
            dhc_2=dhc_2,
            dhc_3=dhc_3,
            dhc_4=dhc_4,
            dhc_5=dhc_5,
            dhc_6=dhc_6,
            dhc_7=dhc_7,
            dhc_8=dhc_8,
            dhi_1=dhi_1,
            dhi_2=dhi_2,
            dhi_3=dhi_3,
            dhi_4=dhi_4,
            dhi_5=dhi_5,
            dhi_6=dhi_6,
            dhi_7=dhi_7,
            dhi_e1=dhi_e1,
            dhi_e2=dhi_e2,
            dhi_e3=dhi_e3,
            dhi_e4=dhi_e4,
            dhi_e5=dhi_e5,
            dhi_e6=dhi_e6,
            dhi_e7=dhi_e7,
            dhm_1=dhm_1,
            dhm_2=dhm_2,
            dhm_3=dhm_3,
            dhm_4=dhm_4,
            dhm_5=dhm_5,
            dhm_6=dhm_6,
            dhm_7=dhm_7,
            dhm_loan=dhm_loan,
            dhm_lr=dhm_lr,
            dhr_1=dhr_1,
            dhr_2=dhr_2,
            dhr_3=dhr_3,
            dhr_4=dhr_4,
            dhz_1=dhz_1,
            dhz_2=dhz_2,
            dhz_3=dhz_3,
            dhz_4=dhz_4,
            dhz_5=dhz_5,
            dhz_6=dhz_6,
            dm_r=dm_r,
            dmr_ir=dmr_ir,
            edu_deg=edu_deg,
            edu_dip=edu_dip,
            edu_lsed=edu_lsed,
            edu_prepri=edu_prepri,
            edu_pri=edu_pri,
            edu_sub=edu_sub,
            edu_usec=edu_usec,
            ethn_chi=ethn_chi,
            ethn_ind=ethn_ind,
            ethn_oth=ethn_oth,
            ethn_phi=ethn_phi,
            ethn_wh=ethn_wh,
            fa_m=fa_m,
            lf_f=lf_f,
            lf_m=lf_m,
            lfpr_f=lfpr_f,
            lfpr_m=lfpr_m,
            lfpr_t=lfpr_t,
            ma_econhh=ma_econhh,
            ma_f=ma_f,
            ma_hh=ma_hh,
            ma_m=ma_m,
            mearn_xfdh_1=mearn_xfdh_1,
            mearn_xfdh_2=mearn_xfdh_2,
            mearn_xfdh_3=mearn_xfdh_3,
            mearn_xfdh_4=mearn_xfdh_4,
            mearn_xfdh_5=mearn_xfdh_5,
            mearn_xfdh_6=mearn_xfdh_6,
            mearn_xfdh_7=mearn_xfdh_7,
            mearn_xfdhfw_1=mearn_xfdhfw_1,
            mearn_xfdhfw_2=mearn_xfdhfw_2,
            mearn_xfdhfw_3=mearn_xfdhfw_3,
            mearn_xfdhfw_4=mearn_xfdhfw_4,
            mearn_xfdhfw_5=mearn_xfdhfw_5,
            mearn_xfdhfw_6=mearn_xfdhfw_6,
            mearn_xfdhfw_7=mearn_xfdhfw_7,
            mmearn_f=mmearn_f,
            mmearn_m=mmearn_m,
            mmearn_xfdh_f=mmearn_xfdh_f,
            mmearn_xfdh_m=mmearn_xfdh_m,
            ms_div_f=ms_div_f,
            ms_div_m=ms_div_m,
            ms_m_f=ms_m_f,
            ms_ma_m=ms_ma_m,
            ms_nm_f=ms_nm_f,
            ms_nm_m=ms_nm_m,
            ms_sep_f=ms_sep_f,
            ms_sep_m=ms_sep_m,
            ms_win_f=ms_win_f,
            ms_win_m=ms_win_m,
            nwp_hm=nwp_hm,
            nwp_oth=nwp_oth,
            nwp_re=nwp_re,
            nwp_st=nwp_st,
            oq_non=oq_non,
            oq_pri=oq_pri,
            oq_pub=oq_pub,
            oq_s=oq_s,
            oq_tem=oq_tem,
            pcfa_m=pcfa_m,
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
            pm_hk=pm_hk,
            pm_kln=pm_kln,
            pm_nt=pm_nt,
            pm_oth=pm_oth,
            pm_out=pm_out,
            pm_same=pm_same,
            pm_samearea=pm_samearea,
            pop_f=pop_f,
            pop_m=pop_m,
            pop_non=pop_non,
            pop_pri=pop_pri,
            pop_pub=pop_pub,
            pop_s=pop_s,
            pop_tem=pop_tem,
            readchi_ablepctn=readchi_ablepctn,
            readeng_ablepctn=readeng_ablepctn,
            s_diff_oth=s_diff_oth,
            sr=sr,
            t_lf=t_lf,
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
