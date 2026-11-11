from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLSBG16BCAttributes")


@_attrs_define
class WfsMapServerWfsLSBG16BCAttributes:
    """
    Attributes:
        age_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        age_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        age_3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        age_4 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        age_5 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        born_chi (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        born_else (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        born_hk (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dh_oth (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dh_pri (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dh_pub (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dh_r0 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dh_r1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dh_r2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dh_r3 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dh_r4 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dh_r5 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dh_r6 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhc_nc (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhc_oth (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhc_re (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhi_sb_1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhi_sb_2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhi_sb_3 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhi_sb_4 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhm_loan (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhm_lr (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhm_sb_1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhm_sb_2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhm_sb_3 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhm_sb_4 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhr_1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhr_2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhr_3 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhr_4 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhz_1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhz_2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dhz_3plus (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dm_r (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dmr_ir (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        edu_pri_be (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        edu_psec (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        edu_sec (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        ethn_chi (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        ethn_ind (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ethn_oth (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ethn_phi (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ethn_wh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        fa_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        lsbg (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        lsbg_chi (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        lsbg_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ma_hh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        mearn_xfw_sb_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        mearn_xfw_sb_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        mearn_xfw_sb_3 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        ms_em (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        ms_nm (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        oq (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        pcfa_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        plw_hk (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        plw_kln (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        plw_nt (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        plw_oth (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        pop_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        pop_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        sr (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        t_pop (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        t_wp (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        ten_oc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ten_oth (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ten_te (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ul_can (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        ul_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ul_oth (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ul_othchi (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        ul_put (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_a (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_b (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_c (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        wp_d (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_e (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_ee (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        wp_er (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_f (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_fw (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_g (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_h (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        wp_i (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_j (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_k (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_l (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_m (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_n (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_o (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_p (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_q (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_r (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        wp_s (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_se (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        wp_t (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    age_1: float | None | Unset = UNSET
    age_2: float | None | Unset = UNSET
    age_3: float | None | Unset = UNSET
    age_4: float | None | Unset = UNSET
    age_5: float | None | Unset = UNSET
    born_chi: float | None | Unset = UNSET
    born_else: None | str | Unset = UNSET
    born_hk: float | None | Unset = UNSET
    dh: float | None | Unset = UNSET
    dh_oth: None | str | Unset = UNSET
    dh_pri: None | str | Unset = UNSET
    dh_pub: None | str | Unset = UNSET
    dh_r0: None | str | Unset = UNSET
    dh_r1: None | str | Unset = UNSET
    dh_r2: None | str | Unset = UNSET
    dh_r3: None | str | Unset = UNSET
    dh_r4: None | str | Unset = UNSET
    dh_r5: None | str | Unset = UNSET
    dh_r6: None | str | Unset = UNSET
    dhc_nc: float | None | Unset = UNSET
    dhc_oth: None | str | Unset = UNSET
    dhc_re: None | str | Unset = UNSET
    dhi_sb_1: None | str | Unset = UNSET
    dhi_sb_2: None | str | Unset = UNSET
    dhi_sb_3: None | str | Unset = UNSET
    dhi_sb_4: None | str | Unset = UNSET
    dhm_loan: None | str | Unset = UNSET
    dhm_lr: None | str | Unset = UNSET
    dhm_sb_1: None | str | Unset = UNSET
    dhm_sb_2: None | str | Unset = UNSET
    dhm_sb_3: None | str | Unset = UNSET
    dhm_sb_4: None | str | Unset = UNSET
    dhr_1: None | str | Unset = UNSET
    dhr_2: None | str | Unset = UNSET
    dhr_3: None | str | Unset = UNSET
    dhr_4: None | str | Unset = UNSET
    dhz_1: None | str | Unset = UNSET
    dhz_2: None | str | Unset = UNSET
    dhz_3plus: float | None | Unset = UNSET
    dm_r: None | str | Unset = UNSET
    dmr_ir: None | str | Unset = UNSET
    edu_pri_be: float | None | Unset = UNSET
    edu_psec: float | None | Unset = UNSET
    edu_sec: float | None | Unset = UNSET
    ethn_chi: float | None | Unset = UNSET
    ethn_ind: None | str | Unset = UNSET
    ethn_oth: None | str | Unset = UNSET
    ethn_phi: None | str | Unset = UNSET
    ethn_wh: None | str | Unset = UNSET
    fa_m: float | None | Unset = UNSET
    lsbg: None | str | Unset = UNSET
    lsbg_chi: None | str | Unset = UNSET
    lsbg_eng: None | str | Unset = UNSET
    ma_hh: None | str | Unset = UNSET
    mearn_xfw_sb_1: float | None | Unset = UNSET
    mearn_xfw_sb_2: float | None | Unset = UNSET
    mearn_xfw_sb_3: None | str | Unset = UNSET
    ms_em: float | None | Unset = UNSET
    ms_nm: float | None | Unset = UNSET
    oq: float | None | Unset = UNSET
    pcfa_m: float | None | Unset = UNSET
    plw_hk: float | None | Unset = UNSET
    plw_kln: None | str | Unset = UNSET
    plw_nt: None | str | Unset = UNSET
    plw_oth: float | None | Unset = UNSET
    pop_f: float | None | Unset = UNSET
    pop_m: float | None | Unset = UNSET
    sr: float | None | Unset = UNSET
    t_pop: float | None | Unset = UNSET
    t_wp: float | None | Unset = UNSET
    ten_oc: None | str | Unset = UNSET
    ten_oth: None | str | Unset = UNSET
    ten_te: None | str | Unset = UNSET
    ul_can: float | None | Unset = UNSET
    ul_eng: None | str | Unset = UNSET
    ul_oth: None | str | Unset = UNSET
    ul_othchi: None | str | Unset = UNSET
    ul_put: None | str | Unset = UNSET
    wp_a: None | str | Unset = UNSET
    wp_b: None | str | Unset = UNSET
    wp_c: float | None | Unset = UNSET
    wp_d: None | str | Unset = UNSET
    wp_e: None | str | Unset = UNSET
    wp_ee: float | None | Unset = UNSET
    wp_er: None | str | Unset = UNSET
    wp_f: None | str | Unset = UNSET
    wp_fw: None | str | Unset = UNSET
    wp_g: None | str | Unset = UNSET
    wp_h: float | None | Unset = UNSET
    wp_i: None | str | Unset = UNSET
    wp_j: None | str | Unset = UNSET
    wp_k: None | str | Unset = UNSET
    wp_l: None | str | Unset = UNSET
    wp_m: None | str | Unset = UNSET
    wp_n: None | str | Unset = UNSET
    wp_o: None | str | Unset = UNSET
    wp_p: None | str | Unset = UNSET
    wp_q: None | str | Unset = UNSET
    wp_r: float | None | Unset = UNSET
    wp_s: None | str | Unset = UNSET
    wp_se: None | str | Unset = UNSET
    wp_t: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        dh_oth: None | str | Unset
        if isinstance(self.dh_oth, Unset):
            dh_oth = UNSET
        else:
            dh_oth = self.dh_oth

        dh_pri: None | str | Unset
        if isinstance(self.dh_pri, Unset):
            dh_pri = UNSET
        else:
            dh_pri = self.dh_pri

        dh_pub: None | str | Unset
        if isinstance(self.dh_pub, Unset):
            dh_pub = UNSET
        else:
            dh_pub = self.dh_pub

        dh_r0: None | str | Unset
        if isinstance(self.dh_r0, Unset):
            dh_r0 = UNSET
        else:
            dh_r0 = self.dh_r0

        dh_r1: None | str | Unset
        if isinstance(self.dh_r1, Unset):
            dh_r1 = UNSET
        else:
            dh_r1 = self.dh_r1

        dh_r2: None | str | Unset
        if isinstance(self.dh_r2, Unset):
            dh_r2 = UNSET
        else:
            dh_r2 = self.dh_r2

        dh_r3: None | str | Unset
        if isinstance(self.dh_r3, Unset):
            dh_r3 = UNSET
        else:
            dh_r3 = self.dh_r3

        dh_r4: None | str | Unset
        if isinstance(self.dh_r4, Unset):
            dh_r4 = UNSET
        else:
            dh_r4 = self.dh_r4

        dh_r5: None | str | Unset
        if isinstance(self.dh_r5, Unset):
            dh_r5 = UNSET
        else:
            dh_r5 = self.dh_r5

        dh_r6: None | str | Unset
        if isinstance(self.dh_r6, Unset):
            dh_r6 = UNSET
        else:
            dh_r6 = self.dh_r6

        dhc_nc: float | None | Unset
        if isinstance(self.dhc_nc, Unset):
            dhc_nc = UNSET
        else:
            dhc_nc = self.dhc_nc

        dhc_oth: None | str | Unset
        if isinstance(self.dhc_oth, Unset):
            dhc_oth = UNSET
        else:
            dhc_oth = self.dhc_oth

        dhc_re: None | str | Unset
        if isinstance(self.dhc_re, Unset):
            dhc_re = UNSET
        else:
            dhc_re = self.dhc_re

        dhi_sb_1: None | str | Unset
        if isinstance(self.dhi_sb_1, Unset):
            dhi_sb_1 = UNSET
        else:
            dhi_sb_1 = self.dhi_sb_1

        dhi_sb_2: None | str | Unset
        if isinstance(self.dhi_sb_2, Unset):
            dhi_sb_2 = UNSET
        else:
            dhi_sb_2 = self.dhi_sb_2

        dhi_sb_3: None | str | Unset
        if isinstance(self.dhi_sb_3, Unset):
            dhi_sb_3 = UNSET
        else:
            dhi_sb_3 = self.dhi_sb_3

        dhi_sb_4: None | str | Unset
        if isinstance(self.dhi_sb_4, Unset):
            dhi_sb_4 = UNSET
        else:
            dhi_sb_4 = self.dhi_sb_4

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

        dhm_sb_1: None | str | Unset
        if isinstance(self.dhm_sb_1, Unset):
            dhm_sb_1 = UNSET
        else:
            dhm_sb_1 = self.dhm_sb_1

        dhm_sb_2: None | str | Unset
        if isinstance(self.dhm_sb_2, Unset):
            dhm_sb_2 = UNSET
        else:
            dhm_sb_2 = self.dhm_sb_2

        dhm_sb_3: None | str | Unset
        if isinstance(self.dhm_sb_3, Unset):
            dhm_sb_3 = UNSET
        else:
            dhm_sb_3 = self.dhm_sb_3

        dhm_sb_4: None | str | Unset
        if isinstance(self.dhm_sb_4, Unset):
            dhm_sb_4 = UNSET
        else:
            dhm_sb_4 = self.dhm_sb_4

        dhr_1: None | str | Unset
        if isinstance(self.dhr_1, Unset):
            dhr_1 = UNSET
        else:
            dhr_1 = self.dhr_1

        dhr_2: None | str | Unset
        if isinstance(self.dhr_2, Unset):
            dhr_2 = UNSET
        else:
            dhr_2 = self.dhr_2

        dhr_3: None | str | Unset
        if isinstance(self.dhr_3, Unset):
            dhr_3 = UNSET
        else:
            dhr_3 = self.dhr_3

        dhr_4: None | str | Unset
        if isinstance(self.dhr_4, Unset):
            dhr_4 = UNSET
        else:
            dhr_4 = self.dhr_4

        dhz_1: None | str | Unset
        if isinstance(self.dhz_1, Unset):
            dhz_1 = UNSET
        else:
            dhz_1 = self.dhz_1

        dhz_2: None | str | Unset
        if isinstance(self.dhz_2, Unset):
            dhz_2 = UNSET
        else:
            dhz_2 = self.dhz_2

        dhz_3plus: float | None | Unset
        if isinstance(self.dhz_3plus, Unset):
            dhz_3plus = UNSET
        else:
            dhz_3plus = self.dhz_3plus

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

        lsbg: None | str | Unset
        if isinstance(self.lsbg, Unset):
            lsbg = UNSET
        else:
            lsbg = self.lsbg

        lsbg_chi: None | str | Unset
        if isinstance(self.lsbg_chi, Unset):
            lsbg_chi = UNSET
        else:
            lsbg_chi = self.lsbg_chi

        lsbg_eng: None | str | Unset
        if isinstance(self.lsbg_eng, Unset):
            lsbg_eng = UNSET
        else:
            lsbg_eng = self.lsbg_eng

        ma_hh: None | str | Unset
        if isinstance(self.ma_hh, Unset):
            ma_hh = UNSET
        else:
            ma_hh = self.ma_hh

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

        mearn_xfw_sb_3: None | str | Unset
        if isinstance(self.mearn_xfw_sb_3, Unset):
            mearn_xfw_sb_3 = UNSET
        else:
            mearn_xfw_sb_3 = self.mearn_xfw_sb_3

        ms_em: float | None | Unset
        if isinstance(self.ms_em, Unset):
            ms_em = UNSET
        else:
            ms_em = self.ms_em

        ms_nm: float | None | Unset
        if isinstance(self.ms_nm, Unset):
            ms_nm = UNSET
        else:
            ms_nm = self.ms_nm

        oq: float | None | Unset
        if isinstance(self.oq, Unset):
            oq = UNSET
        else:
            oq = self.oq

        pcfa_m: float | None | Unset
        if isinstance(self.pcfa_m, Unset):
            pcfa_m = UNSET
        else:
            pcfa_m = self.pcfa_m

        plw_hk: float | None | Unset
        if isinstance(self.plw_hk, Unset):
            plw_hk = UNSET
        else:
            plw_hk = self.plw_hk

        plw_kln: None | str | Unset
        if isinstance(self.plw_kln, Unset):
            plw_kln = UNSET
        else:
            plw_kln = self.plw_kln

        plw_nt: None | str | Unset
        if isinstance(self.plw_nt, Unset):
            plw_nt = UNSET
        else:
            plw_nt = self.plw_nt

        plw_oth: float | None | Unset
        if isinstance(self.plw_oth, Unset):
            plw_oth = UNSET
        else:
            plw_oth = self.plw_oth

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

        sr: float | None | Unset
        if isinstance(self.sr, Unset):
            sr = UNSET
        else:
            sr = self.sr

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

        ten_oc: None | str | Unset
        if isinstance(self.ten_oc, Unset):
            ten_oc = UNSET
        else:
            ten_oc = self.ten_oc

        ten_oth: None | str | Unset
        if isinstance(self.ten_oth, Unset):
            ten_oth = UNSET
        else:
            ten_oth = self.ten_oth

        ten_te: None | str | Unset
        if isinstance(self.ten_te, Unset):
            ten_te = UNSET
        else:
            ten_te = self.ten_te

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

        wp_d: None | str | Unset
        if isinstance(self.wp_d, Unset):
            wp_d = UNSET
        else:
            wp_d = self.wp_d

        wp_e: None | str | Unset
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

        wp_k: None | str | Unset
        if isinstance(self.wp_k, Unset):
            wp_k = UNSET
        else:
            wp_k = self.wp_k

        wp_l: None | str | Unset
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

        wp_p: None | str | Unset
        if isinstance(self.wp_p, Unset):
            wp_p = UNSET
        else:
            wp_p = self.wp_p

        wp_q: None | str | Unset
        if isinstance(self.wp_q, Unset):
            wp_q = UNSET
        else:
            wp_q = self.wp_q

        wp_r: float | None | Unset
        if isinstance(self.wp_r, Unset):
            wp_r = UNSET
        else:
            wp_r = self.wp_r

        wp_s: None | str | Unset
        if isinstance(self.wp_s, Unset):
            wp_s = UNSET
        else:
            wp_s = self.wp_s

        wp_se: None | str | Unset
        if isinstance(self.wp_se, Unset):
            wp_se = UNSET
        else:
            wp_se = self.wp_se

        wp_t: None | str | Unset
        if isinstance(self.wp_t, Unset):
            wp_t = UNSET
        else:
            wp_t = self.wp_t

        objectid = self.objectid

        shape = self.shape

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
        if dh_oth is not UNSET:
            field_dict["dh_oth"] = dh_oth
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
        if dhm_loan is not UNSET:
            field_dict["dhm_loan"] = dhm_loan
        if dhm_lr is not UNSET:
            field_dict["dhm_lr"] = dhm_lr
        if dhm_sb_1 is not UNSET:
            field_dict["dhm_sb_1"] = dhm_sb_1
        if dhm_sb_2 is not UNSET:
            field_dict["dhm_sb_2"] = dhm_sb_2
        if dhm_sb_3 is not UNSET:
            field_dict["dhm_sb_3"] = dhm_sb_3
        if dhm_sb_4 is not UNSET:
            field_dict["dhm_sb_4"] = dhm_sb_4
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
        if dhz_3plus is not UNSET:
            field_dict["dhz_3plus"] = dhz_3plus
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
        if lsbg is not UNSET:
            field_dict["lsbg"] = lsbg
        if lsbg_chi is not UNSET:
            field_dict["lsbg_chi"] = lsbg_chi
        if lsbg_eng is not UNSET:
            field_dict["lsbg_eng"] = lsbg_eng
        if ma_hh is not UNSET:
            field_dict["ma_hh"] = ma_hh
        if mearn_xfw_sb_1 is not UNSET:
            field_dict["mearn_xfw_sb_1"] = mearn_xfw_sb_1
        if mearn_xfw_sb_2 is not UNSET:
            field_dict["mearn_xfw_sb_2"] = mearn_xfw_sb_2
        if mearn_xfw_sb_3 is not UNSET:
            field_dict["mearn_xfw_sb_3"] = mearn_xfw_sb_3
        if ms_em is not UNSET:
            field_dict["ms_em"] = ms_em
        if ms_nm is not UNSET:
            field_dict["ms_nm"] = ms_nm
        if oq is not UNSET:
            field_dict["oq"] = oq
        if pcfa_m is not UNSET:
            field_dict["pcfa_m"] = pcfa_m
        if plw_hk is not UNSET:
            field_dict["plw_hk"] = plw_hk
        if plw_kln is not UNSET:
            field_dict["plw_kln"] = plw_kln
        if plw_nt is not UNSET:
            field_dict["plw_nt"] = plw_nt
        if plw_oth is not UNSET:
            field_dict["plw_oth"] = plw_oth
        if pop_f is not UNSET:
            field_dict["pop_f"] = pop_f
        if pop_m is not UNSET:
            field_dict["pop_m"] = pop_m
        if sr is not UNSET:
            field_dict["sr"] = sr
        if t_pop is not UNSET:
            field_dict["t_pop"] = t_pop
        if t_wp is not UNSET:
            field_dict["t_wp"] = t_wp
        if ten_oc is not UNSET:
            field_dict["ten_oc"] = ten_oc
        if ten_oth is not UNSET:
            field_dict["ten_oth"] = ten_oth
        if ten_te is not UNSET:
            field_dict["ten_te"] = ten_te
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
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

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

        def _parse_dh_oth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_oth = _parse_dh_oth(d.pop("dh_oth", UNSET))

        def _parse_dh_pri(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_pri = _parse_dh_pri(d.pop("dh_pri", UNSET))

        def _parse_dh_pub(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_pub = _parse_dh_pub(d.pop("dh_pub", UNSET))

        def _parse_dh_r0(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_r0 = _parse_dh_r0(d.pop("dh_r0", UNSET))

        def _parse_dh_r1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_r1 = _parse_dh_r1(d.pop("dh_r1", UNSET))

        def _parse_dh_r2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_r2 = _parse_dh_r2(d.pop("dh_r2", UNSET))

        def _parse_dh_r3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_r3 = _parse_dh_r3(d.pop("dh_r3", UNSET))

        def _parse_dh_r4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_r4 = _parse_dh_r4(d.pop("dh_r4", UNSET))

        def _parse_dh_r5(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_r5 = _parse_dh_r5(d.pop("dh_r5", UNSET))

        def _parse_dh_r6(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dh_r6 = _parse_dh_r6(d.pop("dh_r6", UNSET))

        def _parse_dhc_nc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhc_nc = _parse_dhc_nc(d.pop("dhc_nc", UNSET))

        def _parse_dhc_oth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhc_oth = _parse_dhc_oth(d.pop("dhc_oth", UNSET))

        def _parse_dhc_re(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhc_re = _parse_dhc_re(d.pop("dhc_re", UNSET))

        def _parse_dhi_sb_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhi_sb_1 = _parse_dhi_sb_1(d.pop("dhi_sb_1", UNSET))

        def _parse_dhi_sb_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhi_sb_2 = _parse_dhi_sb_2(d.pop("dhi_sb_2", UNSET))

        def _parse_dhi_sb_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhi_sb_3 = _parse_dhi_sb_3(d.pop("dhi_sb_3", UNSET))

        def _parse_dhi_sb_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhi_sb_4 = _parse_dhi_sb_4(d.pop("dhi_sb_4", UNSET))

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

        def _parse_dhm_sb_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhm_sb_1 = _parse_dhm_sb_1(d.pop("dhm_sb_1", UNSET))

        def _parse_dhm_sb_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhm_sb_2 = _parse_dhm_sb_2(d.pop("dhm_sb_2", UNSET))

        def _parse_dhm_sb_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhm_sb_3 = _parse_dhm_sb_3(d.pop("dhm_sb_3", UNSET))

        def _parse_dhm_sb_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhm_sb_4 = _parse_dhm_sb_4(d.pop("dhm_sb_4", UNSET))

        def _parse_dhr_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhr_1 = _parse_dhr_1(d.pop("dhr_1", UNSET))

        def _parse_dhr_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhr_2 = _parse_dhr_2(d.pop("dhr_2", UNSET))

        def _parse_dhr_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhr_3 = _parse_dhr_3(d.pop("dhr_3", UNSET))

        def _parse_dhr_4(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhr_4 = _parse_dhr_4(d.pop("dhr_4", UNSET))

        def _parse_dhz_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhz_1 = _parse_dhz_1(d.pop("dhz_1", UNSET))

        def _parse_dhz_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dhz_2 = _parse_dhz_2(d.pop("dhz_2", UNSET))

        def _parse_dhz_3plus(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_3plus = _parse_dhz_3plus(d.pop("dhz_3plus", UNSET))

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

        def _parse_lsbg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lsbg = _parse_lsbg(d.pop("lsbg", UNSET))

        def _parse_lsbg_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lsbg_chi = _parse_lsbg_chi(d.pop("lsbg_chi", UNSET))

        def _parse_lsbg_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lsbg_eng = _parse_lsbg_eng(d.pop("lsbg_eng", UNSET))

        def _parse_ma_hh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ma_hh = _parse_ma_hh(d.pop("ma_hh", UNSET))

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

        def _parse_mearn_xfw_sb_3(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mearn_xfw_sb_3 = _parse_mearn_xfw_sb_3(d.pop("mearn_xfw_sb_3", UNSET))

        def _parse_ms_em(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_em = _parse_ms_em(d.pop("ms_em", UNSET))

        def _parse_ms_nm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_nm = _parse_ms_nm(d.pop("ms_nm", UNSET))

        def _parse_oq(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        oq = _parse_oq(d.pop("oq", UNSET))

        def _parse_pcfa_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pcfa_m = _parse_pcfa_m(d.pop("pcfa_m", UNSET))

        def _parse_plw_hk(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        plw_hk = _parse_plw_hk(d.pop("plw_hk", UNSET))

        def _parse_plw_kln(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plw_kln = _parse_plw_kln(d.pop("plw_kln", UNSET))

        def _parse_plw_nt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plw_nt = _parse_plw_nt(d.pop("plw_nt", UNSET))

        def _parse_plw_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        plw_oth = _parse_plw_oth(d.pop("plw_oth", UNSET))

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

        def _parse_sr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sr = _parse_sr(d.pop("sr", UNSET))

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

        def _parse_ten_oc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ten_oc = _parse_ten_oc(d.pop("ten_oc", UNSET))

        def _parse_ten_oth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ten_oth = _parse_ten_oth(d.pop("ten_oth", UNSET))

        def _parse_ten_te(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ten_te = _parse_ten_te(d.pop("ten_te", UNSET))

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

        def _parse_wp_d(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_d = _parse_wp_d(d.pop("wp_d", UNSET))

        def _parse_wp_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

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

        def _parse_wp_k(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_k = _parse_wp_k(d.pop("wp_k", UNSET))

        def _parse_wp_l(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

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

        def _parse_wp_p(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_p = _parse_wp_p(d.pop("wp_p", UNSET))

        def _parse_wp_q(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_q = _parse_wp_q(d.pop("wp_q", UNSET))

        def _parse_wp_r(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wp_r = _parse_wp_r(d.pop("wp_r", UNSET))

        def _parse_wp_s(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_s = _parse_wp_s(d.pop("wp_s", UNSET))

        def _parse_wp_se(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_se = _parse_wp_se(d.pop("wp_se", UNSET))

        def _parse_wp_t(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wp_t = _parse_wp_t(d.pop("wp_t", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("SHAPE_Area", UNSET))

        wfs_map_server_wfs_lsbg16bc_attributes = cls(
            age_1=age_1,
            age_2=age_2,
            age_3=age_3,
            age_4=age_4,
            age_5=age_5,
            born_chi=born_chi,
            born_else=born_else,
            born_hk=born_hk,
            dh=dh,
            dh_oth=dh_oth,
            dh_pri=dh_pri,
            dh_pub=dh_pub,
            dh_r0=dh_r0,
            dh_r1=dh_r1,
            dh_r2=dh_r2,
            dh_r3=dh_r3,
            dh_r4=dh_r4,
            dh_r5=dh_r5,
            dh_r6=dh_r6,
            dhc_nc=dhc_nc,
            dhc_oth=dhc_oth,
            dhc_re=dhc_re,
            dhi_sb_1=dhi_sb_1,
            dhi_sb_2=dhi_sb_2,
            dhi_sb_3=dhi_sb_3,
            dhi_sb_4=dhi_sb_4,
            dhm_loan=dhm_loan,
            dhm_lr=dhm_lr,
            dhm_sb_1=dhm_sb_1,
            dhm_sb_2=dhm_sb_2,
            dhm_sb_3=dhm_sb_3,
            dhm_sb_4=dhm_sb_4,
            dhr_1=dhr_1,
            dhr_2=dhr_2,
            dhr_3=dhr_3,
            dhr_4=dhr_4,
            dhz_1=dhz_1,
            dhz_2=dhz_2,
            dhz_3plus=dhz_3plus,
            dm_r=dm_r,
            dmr_ir=dmr_ir,
            edu_pri_be=edu_pri_be,
            edu_psec=edu_psec,
            edu_sec=edu_sec,
            ethn_chi=ethn_chi,
            ethn_ind=ethn_ind,
            ethn_oth=ethn_oth,
            ethn_phi=ethn_phi,
            ethn_wh=ethn_wh,
            fa_m=fa_m,
            lsbg=lsbg,
            lsbg_chi=lsbg_chi,
            lsbg_eng=lsbg_eng,
            ma_hh=ma_hh,
            mearn_xfw_sb_1=mearn_xfw_sb_1,
            mearn_xfw_sb_2=mearn_xfw_sb_2,
            mearn_xfw_sb_3=mearn_xfw_sb_3,
            ms_em=ms_em,
            ms_nm=ms_nm,
            oq=oq,
            pcfa_m=pcfa_m,
            plw_hk=plw_hk,
            plw_kln=plw_kln,
            plw_nt=plw_nt,
            plw_oth=plw_oth,
            pop_f=pop_f,
            pop_m=pop_m,
            sr=sr,
            t_pop=t_pop,
            t_wp=t_wp,
            ten_oc=ten_oc,
            ten_oth=ten_oth,
            ten_te=ten_te,
            ul_can=ul_can,
            ul_eng=ul_eng,
            ul_oth=ul_oth,
            ul_othchi=ul_othchi,
            ul_put=ul_put,
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
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_lsbg16bc_attributes.additional_properties = d
        return wfs_map_server_wfs_lsbg16bc_attributes

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
