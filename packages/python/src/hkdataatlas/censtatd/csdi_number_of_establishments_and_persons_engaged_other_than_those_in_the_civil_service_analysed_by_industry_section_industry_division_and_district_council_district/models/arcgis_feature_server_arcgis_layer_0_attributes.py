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
        ccyy (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dc_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        dc_class (None | str | Unset): Publisher field type: esriFieldTypeString
        dc_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_08 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_10 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_11 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_12 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_13 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_14 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_15 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_16 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_17 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_18 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_19 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_20 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_21 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_22 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_23 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_24 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_25 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_26 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_27 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_28 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_29 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_30 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_31 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_32 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_33 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_35 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_37 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_38 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_39 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_45 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_46 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_47 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_49 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_50 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_51 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_52 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_53 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_55 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_56 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_58 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_59 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_60 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_61 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_62 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_63 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_64 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_65 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_66 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_68 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_69 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_70 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_71 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_72 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_73 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_74 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_75 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_77 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_78 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_79 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_80 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_81 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_82 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_85 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_86 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_87 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_88 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_90 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_91 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_92 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_93 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_94 (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_95 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_96 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_b (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_b_d_e (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_c (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_d (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_d_e (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_e (None | str | Unset): Publisher field type: esriFieldTypeString
        est_ind_g (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_g45_46 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_g47 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_h (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_i (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_j (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_k (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_l (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_m_n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_p (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_p_s (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_q (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_r (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_s (float | None | Unset): Publisher field type: esriFieldTypeDouble
        est_ind_site (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_08 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_10 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_11 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_12 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_13 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_14 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_15 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_16 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_17 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_18 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_19 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_20 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_21 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_22 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_23 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_24 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_25 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_26 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_27 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_28 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_29 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_30 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_31 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_32 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_33 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_35 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_37 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_38 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_39 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_45 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_46 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_47 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_49 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_50 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_51 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_52 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_53 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_55 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_56 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_58 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_59 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_60 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_61 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_62 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_63 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_64 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_65 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_66 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_68 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_69 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_70 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_71 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_72 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_73 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_74 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_75 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_77 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_78 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_79 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_80 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_81 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_82 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_85 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_86 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_87 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_88 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_90 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_91 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_92 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_93 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_94 (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_95 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_96 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_b (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_b_d_e (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_c (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_d (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_d_e (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_e (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_ind_g (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_g45_46 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_g47 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_h (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_i (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_j (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_k (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_l (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_m_n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_p (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_p_s (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_q (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_r (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_s (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_ind_site (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    ccyy: float | None | Unset = UNSET
    dc: float | None | Unset = UNSET
    dc_chi: None | str | Unset = UNSET
    dc_class: None | str | Unset = UNSET
    dc_eng: None | str | Unset = UNSET
    est_ind_08: None | str | Unset = UNSET
    est_ind_10: None | str | Unset = UNSET
    est_ind_11: None | str | Unset = UNSET
    est_ind_12: None | str | Unset = UNSET
    est_ind_13: None | str | Unset = UNSET
    est_ind_14: None | str | Unset = UNSET
    est_ind_15: None | str | Unset = UNSET
    est_ind_16: None | str | Unset = UNSET
    est_ind_17: None | str | Unset = UNSET
    est_ind_18: None | str | Unset = UNSET
    est_ind_19: None | str | Unset = UNSET
    est_ind_20: None | str | Unset = UNSET
    est_ind_21: None | str | Unset = UNSET
    est_ind_22: None | str | Unset = UNSET
    est_ind_23: None | str | Unset = UNSET
    est_ind_24: None | str | Unset = UNSET
    est_ind_25: None | str | Unset = UNSET
    est_ind_26: None | str | Unset = UNSET
    est_ind_27: None | str | Unset = UNSET
    est_ind_28: None | str | Unset = UNSET
    est_ind_29: None | str | Unset = UNSET
    est_ind_30: None | str | Unset = UNSET
    est_ind_31: None | str | Unset = UNSET
    est_ind_32: None | str | Unset = UNSET
    est_ind_33: None | str | Unset = UNSET
    est_ind_35: None | str | Unset = UNSET
    est_ind_37: None | str | Unset = UNSET
    est_ind_38: None | str | Unset = UNSET
    est_ind_39: None | str | Unset = UNSET
    est_ind_45: float | None | Unset = UNSET
    est_ind_46: float | None | Unset = UNSET
    est_ind_47: float | None | Unset = UNSET
    est_ind_49: None | str | Unset = UNSET
    est_ind_50: None | str | Unset = UNSET
    est_ind_51: None | str | Unset = UNSET
    est_ind_52: float | None | Unset = UNSET
    est_ind_53: None | str | Unset = UNSET
    est_ind_55: None | str | Unset = UNSET
    est_ind_56: float | None | Unset = UNSET
    est_ind_58: None | str | Unset = UNSET
    est_ind_59: float | None | Unset = UNSET
    est_ind_60: None | str | Unset = UNSET
    est_ind_61: None | str | Unset = UNSET
    est_ind_62: float | None | Unset = UNSET
    est_ind_63: None | str | Unset = UNSET
    est_ind_64: float | None | Unset = UNSET
    est_ind_65: None | str | Unset = UNSET
    est_ind_66: float | None | Unset = UNSET
    est_ind_68: float | None | Unset = UNSET
    est_ind_69: float | None | Unset = UNSET
    est_ind_70: float | None | Unset = UNSET
    est_ind_71: float | None | Unset = UNSET
    est_ind_72: None | str | Unset = UNSET
    est_ind_73: None | str | Unset = UNSET
    est_ind_74: None | str | Unset = UNSET
    est_ind_75: float | None | Unset = UNSET
    est_ind_77: None | str | Unset = UNSET
    est_ind_78: float | None | Unset = UNSET
    est_ind_79: None | str | Unset = UNSET
    est_ind_80: None | str | Unset = UNSET
    est_ind_81: None | str | Unset = UNSET
    est_ind_82: None | str | Unset = UNSET
    est_ind_85: float | None | Unset = UNSET
    est_ind_86: float | None | Unset = UNSET
    est_ind_87: None | str | Unset = UNSET
    est_ind_88: None | str | Unset = UNSET
    est_ind_90: None | str | Unset = UNSET
    est_ind_91: None | str | Unset = UNSET
    est_ind_92: None | str | Unset = UNSET
    est_ind_93: None | str | Unset = UNSET
    est_ind_94: None | str | Unset = UNSET
    est_ind_95: float | None | Unset = UNSET
    est_ind_96: float | None | Unset = UNSET
    est_ind_b: None | str | Unset = UNSET
    est_ind_b_d_e: None | str | Unset = UNSET
    est_ind_c: float | None | Unset = UNSET
    est_ind_d: None | str | Unset = UNSET
    est_ind_d_e: None | str | Unset = UNSET
    est_ind_e: None | str | Unset = UNSET
    est_ind_g: float | None | Unset = UNSET
    est_ind_g45_46: float | None | Unset = UNSET
    est_ind_g47: float | None | Unset = UNSET
    est_ind_h: float | None | Unset = UNSET
    est_ind_i: float | None | Unset = UNSET
    est_ind_j: float | None | Unset = UNSET
    est_ind_k: float | None | Unset = UNSET
    est_ind_l: float | None | Unset = UNSET
    est_ind_m: float | None | Unset = UNSET
    est_ind_m_n: float | None | Unset = UNSET
    est_ind_n: float | None | Unset = UNSET
    est_ind_p: float | None | Unset = UNSET
    est_ind_p_s: float | None | Unset = UNSET
    est_ind_q: float | None | Unset = UNSET
    est_ind_r: float | None | Unset = UNSET
    est_ind_s: float | None | Unset = UNSET
    est_ind_site: float | None | Unset = UNSET
    pe_ind_08: None | str | Unset = UNSET
    pe_ind_10: float | None | Unset = UNSET
    pe_ind_11: None | str | Unset = UNSET
    pe_ind_12: None | str | Unset = UNSET
    pe_ind_13: None | str | Unset = UNSET
    pe_ind_14: None | str | Unset = UNSET
    pe_ind_15: None | str | Unset = UNSET
    pe_ind_16: None | str | Unset = UNSET
    pe_ind_17: None | str | Unset = UNSET
    pe_ind_18: None | str | Unset = UNSET
    pe_ind_19: None | str | Unset = UNSET
    pe_ind_20: None | str | Unset = UNSET
    pe_ind_21: None | str | Unset = UNSET
    pe_ind_22: None | str | Unset = UNSET
    pe_ind_23: None | str | Unset = UNSET
    pe_ind_24: None | str | Unset = UNSET
    pe_ind_25: None | str | Unset = UNSET
    pe_ind_26: None | str | Unset = UNSET
    pe_ind_27: None | str | Unset = UNSET
    pe_ind_28: None | str | Unset = UNSET
    pe_ind_29: None | str | Unset = UNSET
    pe_ind_30: None | str | Unset = UNSET
    pe_ind_31: None | str | Unset = UNSET
    pe_ind_32: None | str | Unset = UNSET
    pe_ind_33: None | str | Unset = UNSET
    pe_ind_35: None | str | Unset = UNSET
    pe_ind_37: None | str | Unset = UNSET
    pe_ind_38: None | str | Unset = UNSET
    pe_ind_39: None | str | Unset = UNSET
    pe_ind_45: float | None | Unset = UNSET
    pe_ind_46: float | None | Unset = UNSET
    pe_ind_47: float | None | Unset = UNSET
    pe_ind_49: None | str | Unset = UNSET
    pe_ind_50: None | str | Unset = UNSET
    pe_ind_51: None | str | Unset = UNSET
    pe_ind_52: float | None | Unset = UNSET
    pe_ind_53: None | str | Unset = UNSET
    pe_ind_55: None | str | Unset = UNSET
    pe_ind_56: float | None | Unset = UNSET
    pe_ind_58: None | str | Unset = UNSET
    pe_ind_59: float | None | Unset = UNSET
    pe_ind_60: None | str | Unset = UNSET
    pe_ind_61: None | str | Unset = UNSET
    pe_ind_62: float | None | Unset = UNSET
    pe_ind_63: None | str | Unset = UNSET
    pe_ind_64: float | None | Unset = UNSET
    pe_ind_65: None | str | Unset = UNSET
    pe_ind_66: float | None | Unset = UNSET
    pe_ind_68: float | None | Unset = UNSET
    pe_ind_69: float | None | Unset = UNSET
    pe_ind_70: float | None | Unset = UNSET
    pe_ind_71: float | None | Unset = UNSET
    pe_ind_72: None | str | Unset = UNSET
    pe_ind_73: None | str | Unset = UNSET
    pe_ind_74: float | None | Unset = UNSET
    pe_ind_75: float | None | Unset = UNSET
    pe_ind_77: None | str | Unset = UNSET
    pe_ind_78: float | None | Unset = UNSET
    pe_ind_79: None | str | Unset = UNSET
    pe_ind_80: None | str | Unset = UNSET
    pe_ind_81: None | str | Unset = UNSET
    pe_ind_82: float | None | Unset = UNSET
    pe_ind_85: float | None | Unset = UNSET
    pe_ind_86: float | None | Unset = UNSET
    pe_ind_87: float | None | Unset = UNSET
    pe_ind_88: float | None | Unset = UNSET
    pe_ind_90: float | None | Unset = UNSET
    pe_ind_91: None | str | Unset = UNSET
    pe_ind_92: None | str | Unset = UNSET
    pe_ind_93: float | None | Unset = UNSET
    pe_ind_94: None | str | Unset = UNSET
    pe_ind_95: float | None | Unset = UNSET
    pe_ind_96: float | None | Unset = UNSET
    pe_ind_b: None | str | Unset = UNSET
    pe_ind_b_d_e: None | str | Unset = UNSET
    pe_ind_c: float | None | Unset = UNSET
    pe_ind_d: None | str | Unset = UNSET
    pe_ind_d_e: None | str | Unset = UNSET
    pe_ind_e: None | str | Unset = UNSET
    pe_ind_g: float | None | Unset = UNSET
    pe_ind_g45_46: float | None | Unset = UNSET
    pe_ind_g47: float | None | Unset = UNSET
    pe_ind_h: float | None | Unset = UNSET
    pe_ind_i: float | None | Unset = UNSET
    pe_ind_j: float | None | Unset = UNSET
    pe_ind_k: float | None | Unset = UNSET
    pe_ind_l: float | None | Unset = UNSET
    pe_ind_m: float | None | Unset = UNSET
    pe_ind_m_n: float | None | Unset = UNSET
    pe_ind_n: float | None | Unset = UNSET
    pe_ind_p: float | None | Unset = UNSET
    pe_ind_p_s: float | None | Unset = UNSET
    pe_ind_q: float | None | Unset = UNSET
    pe_ind_r: float | None | Unset = UNSET
    pe_ind_s: float | None | Unset = UNSET
    pe_ind_site: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ccyy: float | None | Unset
        if isinstance(self.ccyy, Unset):
            ccyy = UNSET
        else:
            ccyy = self.ccyy

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

        est_ind_08: None | str | Unset
        if isinstance(self.est_ind_08, Unset):
            est_ind_08 = UNSET
        else:
            est_ind_08 = self.est_ind_08

        est_ind_10: None | str | Unset
        if isinstance(self.est_ind_10, Unset):
            est_ind_10 = UNSET
        else:
            est_ind_10 = self.est_ind_10

        est_ind_11: None | str | Unset
        if isinstance(self.est_ind_11, Unset):
            est_ind_11 = UNSET
        else:
            est_ind_11 = self.est_ind_11

        est_ind_12: None | str | Unset
        if isinstance(self.est_ind_12, Unset):
            est_ind_12 = UNSET
        else:
            est_ind_12 = self.est_ind_12

        est_ind_13: None | str | Unset
        if isinstance(self.est_ind_13, Unset):
            est_ind_13 = UNSET
        else:
            est_ind_13 = self.est_ind_13

        est_ind_14: None | str | Unset
        if isinstance(self.est_ind_14, Unset):
            est_ind_14 = UNSET
        else:
            est_ind_14 = self.est_ind_14

        est_ind_15: None | str | Unset
        if isinstance(self.est_ind_15, Unset):
            est_ind_15 = UNSET
        else:
            est_ind_15 = self.est_ind_15

        est_ind_16: None | str | Unset
        if isinstance(self.est_ind_16, Unset):
            est_ind_16 = UNSET
        else:
            est_ind_16 = self.est_ind_16

        est_ind_17: None | str | Unset
        if isinstance(self.est_ind_17, Unset):
            est_ind_17 = UNSET
        else:
            est_ind_17 = self.est_ind_17

        est_ind_18: None | str | Unset
        if isinstance(self.est_ind_18, Unset):
            est_ind_18 = UNSET
        else:
            est_ind_18 = self.est_ind_18

        est_ind_19: None | str | Unset
        if isinstance(self.est_ind_19, Unset):
            est_ind_19 = UNSET
        else:
            est_ind_19 = self.est_ind_19

        est_ind_20: None | str | Unset
        if isinstance(self.est_ind_20, Unset):
            est_ind_20 = UNSET
        else:
            est_ind_20 = self.est_ind_20

        est_ind_21: None | str | Unset
        if isinstance(self.est_ind_21, Unset):
            est_ind_21 = UNSET
        else:
            est_ind_21 = self.est_ind_21

        est_ind_22: None | str | Unset
        if isinstance(self.est_ind_22, Unset):
            est_ind_22 = UNSET
        else:
            est_ind_22 = self.est_ind_22

        est_ind_23: None | str | Unset
        if isinstance(self.est_ind_23, Unset):
            est_ind_23 = UNSET
        else:
            est_ind_23 = self.est_ind_23

        est_ind_24: None | str | Unset
        if isinstance(self.est_ind_24, Unset):
            est_ind_24 = UNSET
        else:
            est_ind_24 = self.est_ind_24

        est_ind_25: None | str | Unset
        if isinstance(self.est_ind_25, Unset):
            est_ind_25 = UNSET
        else:
            est_ind_25 = self.est_ind_25

        est_ind_26: None | str | Unset
        if isinstance(self.est_ind_26, Unset):
            est_ind_26 = UNSET
        else:
            est_ind_26 = self.est_ind_26

        est_ind_27: None | str | Unset
        if isinstance(self.est_ind_27, Unset):
            est_ind_27 = UNSET
        else:
            est_ind_27 = self.est_ind_27

        est_ind_28: None | str | Unset
        if isinstance(self.est_ind_28, Unset):
            est_ind_28 = UNSET
        else:
            est_ind_28 = self.est_ind_28

        est_ind_29: None | str | Unset
        if isinstance(self.est_ind_29, Unset):
            est_ind_29 = UNSET
        else:
            est_ind_29 = self.est_ind_29

        est_ind_30: None | str | Unset
        if isinstance(self.est_ind_30, Unset):
            est_ind_30 = UNSET
        else:
            est_ind_30 = self.est_ind_30

        est_ind_31: None | str | Unset
        if isinstance(self.est_ind_31, Unset):
            est_ind_31 = UNSET
        else:
            est_ind_31 = self.est_ind_31

        est_ind_32: None | str | Unset
        if isinstance(self.est_ind_32, Unset):
            est_ind_32 = UNSET
        else:
            est_ind_32 = self.est_ind_32

        est_ind_33: None | str | Unset
        if isinstance(self.est_ind_33, Unset):
            est_ind_33 = UNSET
        else:
            est_ind_33 = self.est_ind_33

        est_ind_35: None | str | Unset
        if isinstance(self.est_ind_35, Unset):
            est_ind_35 = UNSET
        else:
            est_ind_35 = self.est_ind_35

        est_ind_37: None | str | Unset
        if isinstance(self.est_ind_37, Unset):
            est_ind_37 = UNSET
        else:
            est_ind_37 = self.est_ind_37

        est_ind_38: None | str | Unset
        if isinstance(self.est_ind_38, Unset):
            est_ind_38 = UNSET
        else:
            est_ind_38 = self.est_ind_38

        est_ind_39: None | str | Unset
        if isinstance(self.est_ind_39, Unset):
            est_ind_39 = UNSET
        else:
            est_ind_39 = self.est_ind_39

        est_ind_45: float | None | Unset
        if isinstance(self.est_ind_45, Unset):
            est_ind_45 = UNSET
        else:
            est_ind_45 = self.est_ind_45

        est_ind_46: float | None | Unset
        if isinstance(self.est_ind_46, Unset):
            est_ind_46 = UNSET
        else:
            est_ind_46 = self.est_ind_46

        est_ind_47: float | None | Unset
        if isinstance(self.est_ind_47, Unset):
            est_ind_47 = UNSET
        else:
            est_ind_47 = self.est_ind_47

        est_ind_49: None | str | Unset
        if isinstance(self.est_ind_49, Unset):
            est_ind_49 = UNSET
        else:
            est_ind_49 = self.est_ind_49

        est_ind_50: None | str | Unset
        if isinstance(self.est_ind_50, Unset):
            est_ind_50 = UNSET
        else:
            est_ind_50 = self.est_ind_50

        est_ind_51: None | str | Unset
        if isinstance(self.est_ind_51, Unset):
            est_ind_51 = UNSET
        else:
            est_ind_51 = self.est_ind_51

        est_ind_52: float | None | Unset
        if isinstance(self.est_ind_52, Unset):
            est_ind_52 = UNSET
        else:
            est_ind_52 = self.est_ind_52

        est_ind_53: None | str | Unset
        if isinstance(self.est_ind_53, Unset):
            est_ind_53 = UNSET
        else:
            est_ind_53 = self.est_ind_53

        est_ind_55: None | str | Unset
        if isinstance(self.est_ind_55, Unset):
            est_ind_55 = UNSET
        else:
            est_ind_55 = self.est_ind_55

        est_ind_56: float | None | Unset
        if isinstance(self.est_ind_56, Unset):
            est_ind_56 = UNSET
        else:
            est_ind_56 = self.est_ind_56

        est_ind_58: None | str | Unset
        if isinstance(self.est_ind_58, Unset):
            est_ind_58 = UNSET
        else:
            est_ind_58 = self.est_ind_58

        est_ind_59: float | None | Unset
        if isinstance(self.est_ind_59, Unset):
            est_ind_59 = UNSET
        else:
            est_ind_59 = self.est_ind_59

        est_ind_60: None | str | Unset
        if isinstance(self.est_ind_60, Unset):
            est_ind_60 = UNSET
        else:
            est_ind_60 = self.est_ind_60

        est_ind_61: None | str | Unset
        if isinstance(self.est_ind_61, Unset):
            est_ind_61 = UNSET
        else:
            est_ind_61 = self.est_ind_61

        est_ind_62: float | None | Unset
        if isinstance(self.est_ind_62, Unset):
            est_ind_62 = UNSET
        else:
            est_ind_62 = self.est_ind_62

        est_ind_63: None | str | Unset
        if isinstance(self.est_ind_63, Unset):
            est_ind_63 = UNSET
        else:
            est_ind_63 = self.est_ind_63

        est_ind_64: float | None | Unset
        if isinstance(self.est_ind_64, Unset):
            est_ind_64 = UNSET
        else:
            est_ind_64 = self.est_ind_64

        est_ind_65: None | str | Unset
        if isinstance(self.est_ind_65, Unset):
            est_ind_65 = UNSET
        else:
            est_ind_65 = self.est_ind_65

        est_ind_66: float | None | Unset
        if isinstance(self.est_ind_66, Unset):
            est_ind_66 = UNSET
        else:
            est_ind_66 = self.est_ind_66

        est_ind_68: float | None | Unset
        if isinstance(self.est_ind_68, Unset):
            est_ind_68 = UNSET
        else:
            est_ind_68 = self.est_ind_68

        est_ind_69: float | None | Unset
        if isinstance(self.est_ind_69, Unset):
            est_ind_69 = UNSET
        else:
            est_ind_69 = self.est_ind_69

        est_ind_70: float | None | Unset
        if isinstance(self.est_ind_70, Unset):
            est_ind_70 = UNSET
        else:
            est_ind_70 = self.est_ind_70

        est_ind_71: float | None | Unset
        if isinstance(self.est_ind_71, Unset):
            est_ind_71 = UNSET
        else:
            est_ind_71 = self.est_ind_71

        est_ind_72: None | str | Unset
        if isinstance(self.est_ind_72, Unset):
            est_ind_72 = UNSET
        else:
            est_ind_72 = self.est_ind_72

        est_ind_73: None | str | Unset
        if isinstance(self.est_ind_73, Unset):
            est_ind_73 = UNSET
        else:
            est_ind_73 = self.est_ind_73

        est_ind_74: None | str | Unset
        if isinstance(self.est_ind_74, Unset):
            est_ind_74 = UNSET
        else:
            est_ind_74 = self.est_ind_74

        est_ind_75: float | None | Unset
        if isinstance(self.est_ind_75, Unset):
            est_ind_75 = UNSET
        else:
            est_ind_75 = self.est_ind_75

        est_ind_77: None | str | Unset
        if isinstance(self.est_ind_77, Unset):
            est_ind_77 = UNSET
        else:
            est_ind_77 = self.est_ind_77

        est_ind_78: float | None | Unset
        if isinstance(self.est_ind_78, Unset):
            est_ind_78 = UNSET
        else:
            est_ind_78 = self.est_ind_78

        est_ind_79: None | str | Unset
        if isinstance(self.est_ind_79, Unset):
            est_ind_79 = UNSET
        else:
            est_ind_79 = self.est_ind_79

        est_ind_80: None | str | Unset
        if isinstance(self.est_ind_80, Unset):
            est_ind_80 = UNSET
        else:
            est_ind_80 = self.est_ind_80

        est_ind_81: None | str | Unset
        if isinstance(self.est_ind_81, Unset):
            est_ind_81 = UNSET
        else:
            est_ind_81 = self.est_ind_81

        est_ind_82: None | str | Unset
        if isinstance(self.est_ind_82, Unset):
            est_ind_82 = UNSET
        else:
            est_ind_82 = self.est_ind_82

        est_ind_85: float | None | Unset
        if isinstance(self.est_ind_85, Unset):
            est_ind_85 = UNSET
        else:
            est_ind_85 = self.est_ind_85

        est_ind_86: float | None | Unset
        if isinstance(self.est_ind_86, Unset):
            est_ind_86 = UNSET
        else:
            est_ind_86 = self.est_ind_86

        est_ind_87: None | str | Unset
        if isinstance(self.est_ind_87, Unset):
            est_ind_87 = UNSET
        else:
            est_ind_87 = self.est_ind_87

        est_ind_88: None | str | Unset
        if isinstance(self.est_ind_88, Unset):
            est_ind_88 = UNSET
        else:
            est_ind_88 = self.est_ind_88

        est_ind_90: None | str | Unset
        if isinstance(self.est_ind_90, Unset):
            est_ind_90 = UNSET
        else:
            est_ind_90 = self.est_ind_90

        est_ind_91: None | str | Unset
        if isinstance(self.est_ind_91, Unset):
            est_ind_91 = UNSET
        else:
            est_ind_91 = self.est_ind_91

        est_ind_92: None | str | Unset
        if isinstance(self.est_ind_92, Unset):
            est_ind_92 = UNSET
        else:
            est_ind_92 = self.est_ind_92

        est_ind_93: None | str | Unset
        if isinstance(self.est_ind_93, Unset):
            est_ind_93 = UNSET
        else:
            est_ind_93 = self.est_ind_93

        est_ind_94: None | str | Unset
        if isinstance(self.est_ind_94, Unset):
            est_ind_94 = UNSET
        else:
            est_ind_94 = self.est_ind_94

        est_ind_95: float | None | Unset
        if isinstance(self.est_ind_95, Unset):
            est_ind_95 = UNSET
        else:
            est_ind_95 = self.est_ind_95

        est_ind_96: float | None | Unset
        if isinstance(self.est_ind_96, Unset):
            est_ind_96 = UNSET
        else:
            est_ind_96 = self.est_ind_96

        est_ind_b: None | str | Unset
        if isinstance(self.est_ind_b, Unset):
            est_ind_b = UNSET
        else:
            est_ind_b = self.est_ind_b

        est_ind_b_d_e: None | str | Unset
        if isinstance(self.est_ind_b_d_e, Unset):
            est_ind_b_d_e = UNSET
        else:
            est_ind_b_d_e = self.est_ind_b_d_e

        est_ind_c: float | None | Unset
        if isinstance(self.est_ind_c, Unset):
            est_ind_c = UNSET
        else:
            est_ind_c = self.est_ind_c

        est_ind_d: None | str | Unset
        if isinstance(self.est_ind_d, Unset):
            est_ind_d = UNSET
        else:
            est_ind_d = self.est_ind_d

        est_ind_d_e: None | str | Unset
        if isinstance(self.est_ind_d_e, Unset):
            est_ind_d_e = UNSET
        else:
            est_ind_d_e = self.est_ind_d_e

        est_ind_e: None | str | Unset
        if isinstance(self.est_ind_e, Unset):
            est_ind_e = UNSET
        else:
            est_ind_e = self.est_ind_e

        est_ind_g: float | None | Unset
        if isinstance(self.est_ind_g, Unset):
            est_ind_g = UNSET
        else:
            est_ind_g = self.est_ind_g

        est_ind_g45_46: float | None | Unset
        if isinstance(self.est_ind_g45_46, Unset):
            est_ind_g45_46 = UNSET
        else:
            est_ind_g45_46 = self.est_ind_g45_46

        est_ind_g47: float | None | Unset
        if isinstance(self.est_ind_g47, Unset):
            est_ind_g47 = UNSET
        else:
            est_ind_g47 = self.est_ind_g47

        est_ind_h: float | None | Unset
        if isinstance(self.est_ind_h, Unset):
            est_ind_h = UNSET
        else:
            est_ind_h = self.est_ind_h

        est_ind_i: float | None | Unset
        if isinstance(self.est_ind_i, Unset):
            est_ind_i = UNSET
        else:
            est_ind_i = self.est_ind_i

        est_ind_j: float | None | Unset
        if isinstance(self.est_ind_j, Unset):
            est_ind_j = UNSET
        else:
            est_ind_j = self.est_ind_j

        est_ind_k: float | None | Unset
        if isinstance(self.est_ind_k, Unset):
            est_ind_k = UNSET
        else:
            est_ind_k = self.est_ind_k

        est_ind_l: float | None | Unset
        if isinstance(self.est_ind_l, Unset):
            est_ind_l = UNSET
        else:
            est_ind_l = self.est_ind_l

        est_ind_m: float | None | Unset
        if isinstance(self.est_ind_m, Unset):
            est_ind_m = UNSET
        else:
            est_ind_m = self.est_ind_m

        est_ind_m_n: float | None | Unset
        if isinstance(self.est_ind_m_n, Unset):
            est_ind_m_n = UNSET
        else:
            est_ind_m_n = self.est_ind_m_n

        est_ind_n: float | None | Unset
        if isinstance(self.est_ind_n, Unset):
            est_ind_n = UNSET
        else:
            est_ind_n = self.est_ind_n

        est_ind_p: float | None | Unset
        if isinstance(self.est_ind_p, Unset):
            est_ind_p = UNSET
        else:
            est_ind_p = self.est_ind_p

        est_ind_p_s: float | None | Unset
        if isinstance(self.est_ind_p_s, Unset):
            est_ind_p_s = UNSET
        else:
            est_ind_p_s = self.est_ind_p_s

        est_ind_q: float | None | Unset
        if isinstance(self.est_ind_q, Unset):
            est_ind_q = UNSET
        else:
            est_ind_q = self.est_ind_q

        est_ind_r: float | None | Unset
        if isinstance(self.est_ind_r, Unset):
            est_ind_r = UNSET
        else:
            est_ind_r = self.est_ind_r

        est_ind_s: float | None | Unset
        if isinstance(self.est_ind_s, Unset):
            est_ind_s = UNSET
        else:
            est_ind_s = self.est_ind_s

        est_ind_site: float | None | Unset
        if isinstance(self.est_ind_site, Unset):
            est_ind_site = UNSET
        else:
            est_ind_site = self.est_ind_site

        pe_ind_08: None | str | Unset
        if isinstance(self.pe_ind_08, Unset):
            pe_ind_08 = UNSET
        else:
            pe_ind_08 = self.pe_ind_08

        pe_ind_10: float | None | Unset
        if isinstance(self.pe_ind_10, Unset):
            pe_ind_10 = UNSET
        else:
            pe_ind_10 = self.pe_ind_10

        pe_ind_11: None | str | Unset
        if isinstance(self.pe_ind_11, Unset):
            pe_ind_11 = UNSET
        else:
            pe_ind_11 = self.pe_ind_11

        pe_ind_12: None | str | Unset
        if isinstance(self.pe_ind_12, Unset):
            pe_ind_12 = UNSET
        else:
            pe_ind_12 = self.pe_ind_12

        pe_ind_13: None | str | Unset
        if isinstance(self.pe_ind_13, Unset):
            pe_ind_13 = UNSET
        else:
            pe_ind_13 = self.pe_ind_13

        pe_ind_14: None | str | Unset
        if isinstance(self.pe_ind_14, Unset):
            pe_ind_14 = UNSET
        else:
            pe_ind_14 = self.pe_ind_14

        pe_ind_15: None | str | Unset
        if isinstance(self.pe_ind_15, Unset):
            pe_ind_15 = UNSET
        else:
            pe_ind_15 = self.pe_ind_15

        pe_ind_16: None | str | Unset
        if isinstance(self.pe_ind_16, Unset):
            pe_ind_16 = UNSET
        else:
            pe_ind_16 = self.pe_ind_16

        pe_ind_17: None | str | Unset
        if isinstance(self.pe_ind_17, Unset):
            pe_ind_17 = UNSET
        else:
            pe_ind_17 = self.pe_ind_17

        pe_ind_18: None | str | Unset
        if isinstance(self.pe_ind_18, Unset):
            pe_ind_18 = UNSET
        else:
            pe_ind_18 = self.pe_ind_18

        pe_ind_19: None | str | Unset
        if isinstance(self.pe_ind_19, Unset):
            pe_ind_19 = UNSET
        else:
            pe_ind_19 = self.pe_ind_19

        pe_ind_20: None | str | Unset
        if isinstance(self.pe_ind_20, Unset):
            pe_ind_20 = UNSET
        else:
            pe_ind_20 = self.pe_ind_20

        pe_ind_21: None | str | Unset
        if isinstance(self.pe_ind_21, Unset):
            pe_ind_21 = UNSET
        else:
            pe_ind_21 = self.pe_ind_21

        pe_ind_22: None | str | Unset
        if isinstance(self.pe_ind_22, Unset):
            pe_ind_22 = UNSET
        else:
            pe_ind_22 = self.pe_ind_22

        pe_ind_23: None | str | Unset
        if isinstance(self.pe_ind_23, Unset):
            pe_ind_23 = UNSET
        else:
            pe_ind_23 = self.pe_ind_23

        pe_ind_24: None | str | Unset
        if isinstance(self.pe_ind_24, Unset):
            pe_ind_24 = UNSET
        else:
            pe_ind_24 = self.pe_ind_24

        pe_ind_25: None | str | Unset
        if isinstance(self.pe_ind_25, Unset):
            pe_ind_25 = UNSET
        else:
            pe_ind_25 = self.pe_ind_25

        pe_ind_26: None | str | Unset
        if isinstance(self.pe_ind_26, Unset):
            pe_ind_26 = UNSET
        else:
            pe_ind_26 = self.pe_ind_26

        pe_ind_27: None | str | Unset
        if isinstance(self.pe_ind_27, Unset):
            pe_ind_27 = UNSET
        else:
            pe_ind_27 = self.pe_ind_27

        pe_ind_28: None | str | Unset
        if isinstance(self.pe_ind_28, Unset):
            pe_ind_28 = UNSET
        else:
            pe_ind_28 = self.pe_ind_28

        pe_ind_29: None | str | Unset
        if isinstance(self.pe_ind_29, Unset):
            pe_ind_29 = UNSET
        else:
            pe_ind_29 = self.pe_ind_29

        pe_ind_30: None | str | Unset
        if isinstance(self.pe_ind_30, Unset):
            pe_ind_30 = UNSET
        else:
            pe_ind_30 = self.pe_ind_30

        pe_ind_31: None | str | Unset
        if isinstance(self.pe_ind_31, Unset):
            pe_ind_31 = UNSET
        else:
            pe_ind_31 = self.pe_ind_31

        pe_ind_32: None | str | Unset
        if isinstance(self.pe_ind_32, Unset):
            pe_ind_32 = UNSET
        else:
            pe_ind_32 = self.pe_ind_32

        pe_ind_33: None | str | Unset
        if isinstance(self.pe_ind_33, Unset):
            pe_ind_33 = UNSET
        else:
            pe_ind_33 = self.pe_ind_33

        pe_ind_35: None | str | Unset
        if isinstance(self.pe_ind_35, Unset):
            pe_ind_35 = UNSET
        else:
            pe_ind_35 = self.pe_ind_35

        pe_ind_37: None | str | Unset
        if isinstance(self.pe_ind_37, Unset):
            pe_ind_37 = UNSET
        else:
            pe_ind_37 = self.pe_ind_37

        pe_ind_38: None | str | Unset
        if isinstance(self.pe_ind_38, Unset):
            pe_ind_38 = UNSET
        else:
            pe_ind_38 = self.pe_ind_38

        pe_ind_39: None | str | Unset
        if isinstance(self.pe_ind_39, Unset):
            pe_ind_39 = UNSET
        else:
            pe_ind_39 = self.pe_ind_39

        pe_ind_45: float | None | Unset
        if isinstance(self.pe_ind_45, Unset):
            pe_ind_45 = UNSET
        else:
            pe_ind_45 = self.pe_ind_45

        pe_ind_46: float | None | Unset
        if isinstance(self.pe_ind_46, Unset):
            pe_ind_46 = UNSET
        else:
            pe_ind_46 = self.pe_ind_46

        pe_ind_47: float | None | Unset
        if isinstance(self.pe_ind_47, Unset):
            pe_ind_47 = UNSET
        else:
            pe_ind_47 = self.pe_ind_47

        pe_ind_49: None | str | Unset
        if isinstance(self.pe_ind_49, Unset):
            pe_ind_49 = UNSET
        else:
            pe_ind_49 = self.pe_ind_49

        pe_ind_50: None | str | Unset
        if isinstance(self.pe_ind_50, Unset):
            pe_ind_50 = UNSET
        else:
            pe_ind_50 = self.pe_ind_50

        pe_ind_51: None | str | Unset
        if isinstance(self.pe_ind_51, Unset):
            pe_ind_51 = UNSET
        else:
            pe_ind_51 = self.pe_ind_51

        pe_ind_52: float | None | Unset
        if isinstance(self.pe_ind_52, Unset):
            pe_ind_52 = UNSET
        else:
            pe_ind_52 = self.pe_ind_52

        pe_ind_53: None | str | Unset
        if isinstance(self.pe_ind_53, Unset):
            pe_ind_53 = UNSET
        else:
            pe_ind_53 = self.pe_ind_53

        pe_ind_55: None | str | Unset
        if isinstance(self.pe_ind_55, Unset):
            pe_ind_55 = UNSET
        else:
            pe_ind_55 = self.pe_ind_55

        pe_ind_56: float | None | Unset
        if isinstance(self.pe_ind_56, Unset):
            pe_ind_56 = UNSET
        else:
            pe_ind_56 = self.pe_ind_56

        pe_ind_58: None | str | Unset
        if isinstance(self.pe_ind_58, Unset):
            pe_ind_58 = UNSET
        else:
            pe_ind_58 = self.pe_ind_58

        pe_ind_59: float | None | Unset
        if isinstance(self.pe_ind_59, Unset):
            pe_ind_59 = UNSET
        else:
            pe_ind_59 = self.pe_ind_59

        pe_ind_60: None | str | Unset
        if isinstance(self.pe_ind_60, Unset):
            pe_ind_60 = UNSET
        else:
            pe_ind_60 = self.pe_ind_60

        pe_ind_61: None | str | Unset
        if isinstance(self.pe_ind_61, Unset):
            pe_ind_61 = UNSET
        else:
            pe_ind_61 = self.pe_ind_61

        pe_ind_62: float | None | Unset
        if isinstance(self.pe_ind_62, Unset):
            pe_ind_62 = UNSET
        else:
            pe_ind_62 = self.pe_ind_62

        pe_ind_63: None | str | Unset
        if isinstance(self.pe_ind_63, Unset):
            pe_ind_63 = UNSET
        else:
            pe_ind_63 = self.pe_ind_63

        pe_ind_64: float | None | Unset
        if isinstance(self.pe_ind_64, Unset):
            pe_ind_64 = UNSET
        else:
            pe_ind_64 = self.pe_ind_64

        pe_ind_65: None | str | Unset
        if isinstance(self.pe_ind_65, Unset):
            pe_ind_65 = UNSET
        else:
            pe_ind_65 = self.pe_ind_65

        pe_ind_66: float | None | Unset
        if isinstance(self.pe_ind_66, Unset):
            pe_ind_66 = UNSET
        else:
            pe_ind_66 = self.pe_ind_66

        pe_ind_68: float | None | Unset
        if isinstance(self.pe_ind_68, Unset):
            pe_ind_68 = UNSET
        else:
            pe_ind_68 = self.pe_ind_68

        pe_ind_69: float | None | Unset
        if isinstance(self.pe_ind_69, Unset):
            pe_ind_69 = UNSET
        else:
            pe_ind_69 = self.pe_ind_69

        pe_ind_70: float | None | Unset
        if isinstance(self.pe_ind_70, Unset):
            pe_ind_70 = UNSET
        else:
            pe_ind_70 = self.pe_ind_70

        pe_ind_71: float | None | Unset
        if isinstance(self.pe_ind_71, Unset):
            pe_ind_71 = UNSET
        else:
            pe_ind_71 = self.pe_ind_71

        pe_ind_72: None | str | Unset
        if isinstance(self.pe_ind_72, Unset):
            pe_ind_72 = UNSET
        else:
            pe_ind_72 = self.pe_ind_72

        pe_ind_73: None | str | Unset
        if isinstance(self.pe_ind_73, Unset):
            pe_ind_73 = UNSET
        else:
            pe_ind_73 = self.pe_ind_73

        pe_ind_74: float | None | Unset
        if isinstance(self.pe_ind_74, Unset):
            pe_ind_74 = UNSET
        else:
            pe_ind_74 = self.pe_ind_74

        pe_ind_75: float | None | Unset
        if isinstance(self.pe_ind_75, Unset):
            pe_ind_75 = UNSET
        else:
            pe_ind_75 = self.pe_ind_75

        pe_ind_77: None | str | Unset
        if isinstance(self.pe_ind_77, Unset):
            pe_ind_77 = UNSET
        else:
            pe_ind_77 = self.pe_ind_77

        pe_ind_78: float | None | Unset
        if isinstance(self.pe_ind_78, Unset):
            pe_ind_78 = UNSET
        else:
            pe_ind_78 = self.pe_ind_78

        pe_ind_79: None | str | Unset
        if isinstance(self.pe_ind_79, Unset):
            pe_ind_79 = UNSET
        else:
            pe_ind_79 = self.pe_ind_79

        pe_ind_80: None | str | Unset
        if isinstance(self.pe_ind_80, Unset):
            pe_ind_80 = UNSET
        else:
            pe_ind_80 = self.pe_ind_80

        pe_ind_81: None | str | Unset
        if isinstance(self.pe_ind_81, Unset):
            pe_ind_81 = UNSET
        else:
            pe_ind_81 = self.pe_ind_81

        pe_ind_82: float | None | Unset
        if isinstance(self.pe_ind_82, Unset):
            pe_ind_82 = UNSET
        else:
            pe_ind_82 = self.pe_ind_82

        pe_ind_85: float | None | Unset
        if isinstance(self.pe_ind_85, Unset):
            pe_ind_85 = UNSET
        else:
            pe_ind_85 = self.pe_ind_85

        pe_ind_86: float | None | Unset
        if isinstance(self.pe_ind_86, Unset):
            pe_ind_86 = UNSET
        else:
            pe_ind_86 = self.pe_ind_86

        pe_ind_87: float | None | Unset
        if isinstance(self.pe_ind_87, Unset):
            pe_ind_87 = UNSET
        else:
            pe_ind_87 = self.pe_ind_87

        pe_ind_88: float | None | Unset
        if isinstance(self.pe_ind_88, Unset):
            pe_ind_88 = UNSET
        else:
            pe_ind_88 = self.pe_ind_88

        pe_ind_90: float | None | Unset
        if isinstance(self.pe_ind_90, Unset):
            pe_ind_90 = UNSET
        else:
            pe_ind_90 = self.pe_ind_90

        pe_ind_91: None | str | Unset
        if isinstance(self.pe_ind_91, Unset):
            pe_ind_91 = UNSET
        else:
            pe_ind_91 = self.pe_ind_91

        pe_ind_92: None | str | Unset
        if isinstance(self.pe_ind_92, Unset):
            pe_ind_92 = UNSET
        else:
            pe_ind_92 = self.pe_ind_92

        pe_ind_93: float | None | Unset
        if isinstance(self.pe_ind_93, Unset):
            pe_ind_93 = UNSET
        else:
            pe_ind_93 = self.pe_ind_93

        pe_ind_94: None | str | Unset
        if isinstance(self.pe_ind_94, Unset):
            pe_ind_94 = UNSET
        else:
            pe_ind_94 = self.pe_ind_94

        pe_ind_95: float | None | Unset
        if isinstance(self.pe_ind_95, Unset):
            pe_ind_95 = UNSET
        else:
            pe_ind_95 = self.pe_ind_95

        pe_ind_96: float | None | Unset
        if isinstance(self.pe_ind_96, Unset):
            pe_ind_96 = UNSET
        else:
            pe_ind_96 = self.pe_ind_96

        pe_ind_b: None | str | Unset
        if isinstance(self.pe_ind_b, Unset):
            pe_ind_b = UNSET
        else:
            pe_ind_b = self.pe_ind_b

        pe_ind_b_d_e: None | str | Unset
        if isinstance(self.pe_ind_b_d_e, Unset):
            pe_ind_b_d_e = UNSET
        else:
            pe_ind_b_d_e = self.pe_ind_b_d_e

        pe_ind_c: float | None | Unset
        if isinstance(self.pe_ind_c, Unset):
            pe_ind_c = UNSET
        else:
            pe_ind_c = self.pe_ind_c

        pe_ind_d: None | str | Unset
        if isinstance(self.pe_ind_d, Unset):
            pe_ind_d = UNSET
        else:
            pe_ind_d = self.pe_ind_d

        pe_ind_d_e: None | str | Unset
        if isinstance(self.pe_ind_d_e, Unset):
            pe_ind_d_e = UNSET
        else:
            pe_ind_d_e = self.pe_ind_d_e

        pe_ind_e: None | str | Unset
        if isinstance(self.pe_ind_e, Unset):
            pe_ind_e = UNSET
        else:
            pe_ind_e = self.pe_ind_e

        pe_ind_g: float | None | Unset
        if isinstance(self.pe_ind_g, Unset):
            pe_ind_g = UNSET
        else:
            pe_ind_g = self.pe_ind_g

        pe_ind_g45_46: float | None | Unset
        if isinstance(self.pe_ind_g45_46, Unset):
            pe_ind_g45_46 = UNSET
        else:
            pe_ind_g45_46 = self.pe_ind_g45_46

        pe_ind_g47: float | None | Unset
        if isinstance(self.pe_ind_g47, Unset):
            pe_ind_g47 = UNSET
        else:
            pe_ind_g47 = self.pe_ind_g47

        pe_ind_h: float | None | Unset
        if isinstance(self.pe_ind_h, Unset):
            pe_ind_h = UNSET
        else:
            pe_ind_h = self.pe_ind_h

        pe_ind_i: float | None | Unset
        if isinstance(self.pe_ind_i, Unset):
            pe_ind_i = UNSET
        else:
            pe_ind_i = self.pe_ind_i

        pe_ind_j: float | None | Unset
        if isinstance(self.pe_ind_j, Unset):
            pe_ind_j = UNSET
        else:
            pe_ind_j = self.pe_ind_j

        pe_ind_k: float | None | Unset
        if isinstance(self.pe_ind_k, Unset):
            pe_ind_k = UNSET
        else:
            pe_ind_k = self.pe_ind_k

        pe_ind_l: float | None | Unset
        if isinstance(self.pe_ind_l, Unset):
            pe_ind_l = UNSET
        else:
            pe_ind_l = self.pe_ind_l

        pe_ind_m: float | None | Unset
        if isinstance(self.pe_ind_m, Unset):
            pe_ind_m = UNSET
        else:
            pe_ind_m = self.pe_ind_m

        pe_ind_m_n: float | None | Unset
        if isinstance(self.pe_ind_m_n, Unset):
            pe_ind_m_n = UNSET
        else:
            pe_ind_m_n = self.pe_ind_m_n

        pe_ind_n: float | None | Unset
        if isinstance(self.pe_ind_n, Unset):
            pe_ind_n = UNSET
        else:
            pe_ind_n = self.pe_ind_n

        pe_ind_p: float | None | Unset
        if isinstance(self.pe_ind_p, Unset):
            pe_ind_p = UNSET
        else:
            pe_ind_p = self.pe_ind_p

        pe_ind_p_s: float | None | Unset
        if isinstance(self.pe_ind_p_s, Unset):
            pe_ind_p_s = UNSET
        else:
            pe_ind_p_s = self.pe_ind_p_s

        pe_ind_q: float | None | Unset
        if isinstance(self.pe_ind_q, Unset):
            pe_ind_q = UNSET
        else:
            pe_ind_q = self.pe_ind_q

        pe_ind_r: float | None | Unset
        if isinstance(self.pe_ind_r, Unset):
            pe_ind_r = UNSET
        else:
            pe_ind_r = self.pe_ind_r

        pe_ind_s: float | None | Unset
        if isinstance(self.pe_ind_s, Unset):
            pe_ind_s = UNSET
        else:
            pe_ind_s = self.pe_ind_s

        pe_ind_site: float | None | Unset
        if isinstance(self.pe_ind_site, Unset):
            pe_ind_site = UNSET
        else:
            pe_ind_site = self.pe_ind_site

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
        if ccyy is not UNSET:
            field_dict["CCYY"] = ccyy
        if dc is not UNSET:
            field_dict["DC"] = dc
        if dc_chi is not UNSET:
            field_dict["DC_CHI"] = dc_chi
        if dc_class is not UNSET:
            field_dict["DC_CLASS"] = dc_class
        if dc_eng is not UNSET:
            field_dict["DC_ENG"] = dc_eng
        if est_ind_08 is not UNSET:
            field_dict["EST_ind_08"] = est_ind_08
        if est_ind_10 is not UNSET:
            field_dict["EST_ind_10"] = est_ind_10
        if est_ind_11 is not UNSET:
            field_dict["EST_ind_11"] = est_ind_11
        if est_ind_12 is not UNSET:
            field_dict["EST_ind_12"] = est_ind_12
        if est_ind_13 is not UNSET:
            field_dict["EST_ind_13"] = est_ind_13
        if est_ind_14 is not UNSET:
            field_dict["EST_ind_14"] = est_ind_14
        if est_ind_15 is not UNSET:
            field_dict["EST_ind_15"] = est_ind_15
        if est_ind_16 is not UNSET:
            field_dict["EST_ind_16"] = est_ind_16
        if est_ind_17 is not UNSET:
            field_dict["EST_ind_17"] = est_ind_17
        if est_ind_18 is not UNSET:
            field_dict["EST_ind_18"] = est_ind_18
        if est_ind_19 is not UNSET:
            field_dict["EST_ind_19"] = est_ind_19
        if est_ind_20 is not UNSET:
            field_dict["EST_ind_20"] = est_ind_20
        if est_ind_21 is not UNSET:
            field_dict["EST_ind_21"] = est_ind_21
        if est_ind_22 is not UNSET:
            field_dict["EST_ind_22"] = est_ind_22
        if est_ind_23 is not UNSET:
            field_dict["EST_ind_23"] = est_ind_23
        if est_ind_24 is not UNSET:
            field_dict["EST_ind_24"] = est_ind_24
        if est_ind_25 is not UNSET:
            field_dict["EST_ind_25"] = est_ind_25
        if est_ind_26 is not UNSET:
            field_dict["EST_ind_26"] = est_ind_26
        if est_ind_27 is not UNSET:
            field_dict["EST_ind_27"] = est_ind_27
        if est_ind_28 is not UNSET:
            field_dict["EST_ind_28"] = est_ind_28
        if est_ind_29 is not UNSET:
            field_dict["EST_ind_29"] = est_ind_29
        if est_ind_30 is not UNSET:
            field_dict["EST_ind_30"] = est_ind_30
        if est_ind_31 is not UNSET:
            field_dict["EST_ind_31"] = est_ind_31
        if est_ind_32 is not UNSET:
            field_dict["EST_ind_32"] = est_ind_32
        if est_ind_33 is not UNSET:
            field_dict["EST_ind_33"] = est_ind_33
        if est_ind_35 is not UNSET:
            field_dict["EST_ind_35"] = est_ind_35
        if est_ind_37 is not UNSET:
            field_dict["EST_ind_37"] = est_ind_37
        if est_ind_38 is not UNSET:
            field_dict["EST_ind_38"] = est_ind_38
        if est_ind_39 is not UNSET:
            field_dict["EST_ind_39"] = est_ind_39
        if est_ind_45 is not UNSET:
            field_dict["EST_ind_45"] = est_ind_45
        if est_ind_46 is not UNSET:
            field_dict["EST_ind_46"] = est_ind_46
        if est_ind_47 is not UNSET:
            field_dict["EST_ind_47"] = est_ind_47
        if est_ind_49 is not UNSET:
            field_dict["EST_ind_49"] = est_ind_49
        if est_ind_50 is not UNSET:
            field_dict["EST_ind_50"] = est_ind_50
        if est_ind_51 is not UNSET:
            field_dict["EST_ind_51"] = est_ind_51
        if est_ind_52 is not UNSET:
            field_dict["EST_ind_52"] = est_ind_52
        if est_ind_53 is not UNSET:
            field_dict["EST_ind_53"] = est_ind_53
        if est_ind_55 is not UNSET:
            field_dict["EST_ind_55"] = est_ind_55
        if est_ind_56 is not UNSET:
            field_dict["EST_ind_56"] = est_ind_56
        if est_ind_58 is not UNSET:
            field_dict["EST_ind_58"] = est_ind_58
        if est_ind_59 is not UNSET:
            field_dict["EST_ind_59"] = est_ind_59
        if est_ind_60 is not UNSET:
            field_dict["EST_ind_60"] = est_ind_60
        if est_ind_61 is not UNSET:
            field_dict["EST_ind_61"] = est_ind_61
        if est_ind_62 is not UNSET:
            field_dict["EST_ind_62"] = est_ind_62
        if est_ind_63 is not UNSET:
            field_dict["EST_ind_63"] = est_ind_63
        if est_ind_64 is not UNSET:
            field_dict["EST_ind_64"] = est_ind_64
        if est_ind_65 is not UNSET:
            field_dict["EST_ind_65"] = est_ind_65
        if est_ind_66 is not UNSET:
            field_dict["EST_ind_66"] = est_ind_66
        if est_ind_68 is not UNSET:
            field_dict["EST_ind_68"] = est_ind_68
        if est_ind_69 is not UNSET:
            field_dict["EST_ind_69"] = est_ind_69
        if est_ind_70 is not UNSET:
            field_dict["EST_ind_70"] = est_ind_70
        if est_ind_71 is not UNSET:
            field_dict["EST_ind_71"] = est_ind_71
        if est_ind_72 is not UNSET:
            field_dict["EST_ind_72"] = est_ind_72
        if est_ind_73 is not UNSET:
            field_dict["EST_ind_73"] = est_ind_73
        if est_ind_74 is not UNSET:
            field_dict["EST_ind_74"] = est_ind_74
        if est_ind_75 is not UNSET:
            field_dict["EST_ind_75"] = est_ind_75
        if est_ind_77 is not UNSET:
            field_dict["EST_ind_77"] = est_ind_77
        if est_ind_78 is not UNSET:
            field_dict["EST_ind_78"] = est_ind_78
        if est_ind_79 is not UNSET:
            field_dict["EST_ind_79"] = est_ind_79
        if est_ind_80 is not UNSET:
            field_dict["EST_ind_80"] = est_ind_80
        if est_ind_81 is not UNSET:
            field_dict["EST_ind_81"] = est_ind_81
        if est_ind_82 is not UNSET:
            field_dict["EST_ind_82"] = est_ind_82
        if est_ind_85 is not UNSET:
            field_dict["EST_ind_85"] = est_ind_85
        if est_ind_86 is not UNSET:
            field_dict["EST_ind_86"] = est_ind_86
        if est_ind_87 is not UNSET:
            field_dict["EST_ind_87"] = est_ind_87
        if est_ind_88 is not UNSET:
            field_dict["EST_ind_88"] = est_ind_88
        if est_ind_90 is not UNSET:
            field_dict["EST_ind_90"] = est_ind_90
        if est_ind_91 is not UNSET:
            field_dict["EST_ind_91"] = est_ind_91
        if est_ind_92 is not UNSET:
            field_dict["EST_ind_92"] = est_ind_92
        if est_ind_93 is not UNSET:
            field_dict["EST_ind_93"] = est_ind_93
        if est_ind_94 is not UNSET:
            field_dict["EST_ind_94"] = est_ind_94
        if est_ind_95 is not UNSET:
            field_dict["EST_ind_95"] = est_ind_95
        if est_ind_96 is not UNSET:
            field_dict["EST_ind_96"] = est_ind_96
        if est_ind_b is not UNSET:
            field_dict["EST_ind_B"] = est_ind_b
        if est_ind_b_d_e is not UNSET:
            field_dict["EST_ind_B_D_E"] = est_ind_b_d_e
        if est_ind_c is not UNSET:
            field_dict["EST_ind_C"] = est_ind_c
        if est_ind_d is not UNSET:
            field_dict["EST_ind_D"] = est_ind_d
        if est_ind_d_e is not UNSET:
            field_dict["EST_ind_D_E"] = est_ind_d_e
        if est_ind_e is not UNSET:
            field_dict["EST_ind_E"] = est_ind_e
        if est_ind_g is not UNSET:
            field_dict["EST_ind_G"] = est_ind_g
        if est_ind_g45_46 is not UNSET:
            field_dict["EST_ind_G45_46"] = est_ind_g45_46
        if est_ind_g47 is not UNSET:
            field_dict["EST_ind_G47"] = est_ind_g47
        if est_ind_h is not UNSET:
            field_dict["EST_ind_H"] = est_ind_h
        if est_ind_i is not UNSET:
            field_dict["EST_ind_I"] = est_ind_i
        if est_ind_j is not UNSET:
            field_dict["EST_ind_J"] = est_ind_j
        if est_ind_k is not UNSET:
            field_dict["EST_ind_K"] = est_ind_k
        if est_ind_l is not UNSET:
            field_dict["EST_ind_L"] = est_ind_l
        if est_ind_m is not UNSET:
            field_dict["EST_ind_M"] = est_ind_m
        if est_ind_m_n is not UNSET:
            field_dict["EST_ind_M_N"] = est_ind_m_n
        if est_ind_n is not UNSET:
            field_dict["EST_ind_N"] = est_ind_n
        if est_ind_p is not UNSET:
            field_dict["EST_ind_P"] = est_ind_p
        if est_ind_p_s is not UNSET:
            field_dict["EST_ind_P_S"] = est_ind_p_s
        if est_ind_q is not UNSET:
            field_dict["EST_ind_Q"] = est_ind_q
        if est_ind_r is not UNSET:
            field_dict["EST_ind_R"] = est_ind_r
        if est_ind_s is not UNSET:
            field_dict["EST_ind_S"] = est_ind_s
        if est_ind_site is not UNSET:
            field_dict["EST_ind_SITE"] = est_ind_site
        if pe_ind_08 is not UNSET:
            field_dict["PE_ind_08"] = pe_ind_08
        if pe_ind_10 is not UNSET:
            field_dict["PE_ind_10"] = pe_ind_10
        if pe_ind_11 is not UNSET:
            field_dict["PE_ind_11"] = pe_ind_11
        if pe_ind_12 is not UNSET:
            field_dict["PE_ind_12"] = pe_ind_12
        if pe_ind_13 is not UNSET:
            field_dict["PE_ind_13"] = pe_ind_13
        if pe_ind_14 is not UNSET:
            field_dict["PE_ind_14"] = pe_ind_14
        if pe_ind_15 is not UNSET:
            field_dict["PE_ind_15"] = pe_ind_15
        if pe_ind_16 is not UNSET:
            field_dict["PE_ind_16"] = pe_ind_16
        if pe_ind_17 is not UNSET:
            field_dict["PE_ind_17"] = pe_ind_17
        if pe_ind_18 is not UNSET:
            field_dict["PE_ind_18"] = pe_ind_18
        if pe_ind_19 is not UNSET:
            field_dict["PE_ind_19"] = pe_ind_19
        if pe_ind_20 is not UNSET:
            field_dict["PE_ind_20"] = pe_ind_20
        if pe_ind_21 is not UNSET:
            field_dict["PE_ind_21"] = pe_ind_21
        if pe_ind_22 is not UNSET:
            field_dict["PE_ind_22"] = pe_ind_22
        if pe_ind_23 is not UNSET:
            field_dict["PE_ind_23"] = pe_ind_23
        if pe_ind_24 is not UNSET:
            field_dict["PE_ind_24"] = pe_ind_24
        if pe_ind_25 is not UNSET:
            field_dict["PE_ind_25"] = pe_ind_25
        if pe_ind_26 is not UNSET:
            field_dict["PE_ind_26"] = pe_ind_26
        if pe_ind_27 is not UNSET:
            field_dict["PE_ind_27"] = pe_ind_27
        if pe_ind_28 is not UNSET:
            field_dict["PE_ind_28"] = pe_ind_28
        if pe_ind_29 is not UNSET:
            field_dict["PE_ind_29"] = pe_ind_29
        if pe_ind_30 is not UNSET:
            field_dict["PE_ind_30"] = pe_ind_30
        if pe_ind_31 is not UNSET:
            field_dict["PE_ind_31"] = pe_ind_31
        if pe_ind_32 is not UNSET:
            field_dict["PE_ind_32"] = pe_ind_32
        if pe_ind_33 is not UNSET:
            field_dict["PE_ind_33"] = pe_ind_33
        if pe_ind_35 is not UNSET:
            field_dict["PE_ind_35"] = pe_ind_35
        if pe_ind_37 is not UNSET:
            field_dict["PE_ind_37"] = pe_ind_37
        if pe_ind_38 is not UNSET:
            field_dict["PE_ind_38"] = pe_ind_38
        if pe_ind_39 is not UNSET:
            field_dict["PE_ind_39"] = pe_ind_39
        if pe_ind_45 is not UNSET:
            field_dict["PE_ind_45"] = pe_ind_45
        if pe_ind_46 is not UNSET:
            field_dict["PE_ind_46"] = pe_ind_46
        if pe_ind_47 is not UNSET:
            field_dict["PE_ind_47"] = pe_ind_47
        if pe_ind_49 is not UNSET:
            field_dict["PE_ind_49"] = pe_ind_49
        if pe_ind_50 is not UNSET:
            field_dict["PE_ind_50"] = pe_ind_50
        if pe_ind_51 is not UNSET:
            field_dict["PE_ind_51"] = pe_ind_51
        if pe_ind_52 is not UNSET:
            field_dict["PE_ind_52"] = pe_ind_52
        if pe_ind_53 is not UNSET:
            field_dict["PE_ind_53"] = pe_ind_53
        if pe_ind_55 is not UNSET:
            field_dict["PE_ind_55"] = pe_ind_55
        if pe_ind_56 is not UNSET:
            field_dict["PE_ind_56"] = pe_ind_56
        if pe_ind_58 is not UNSET:
            field_dict["PE_ind_58"] = pe_ind_58
        if pe_ind_59 is not UNSET:
            field_dict["PE_ind_59"] = pe_ind_59
        if pe_ind_60 is not UNSET:
            field_dict["PE_ind_60"] = pe_ind_60
        if pe_ind_61 is not UNSET:
            field_dict["PE_ind_61"] = pe_ind_61
        if pe_ind_62 is not UNSET:
            field_dict["PE_ind_62"] = pe_ind_62
        if pe_ind_63 is not UNSET:
            field_dict["PE_ind_63"] = pe_ind_63
        if pe_ind_64 is not UNSET:
            field_dict["PE_ind_64"] = pe_ind_64
        if pe_ind_65 is not UNSET:
            field_dict["PE_ind_65"] = pe_ind_65
        if pe_ind_66 is not UNSET:
            field_dict["PE_ind_66"] = pe_ind_66
        if pe_ind_68 is not UNSET:
            field_dict["PE_ind_68"] = pe_ind_68
        if pe_ind_69 is not UNSET:
            field_dict["PE_ind_69"] = pe_ind_69
        if pe_ind_70 is not UNSET:
            field_dict["PE_ind_70"] = pe_ind_70
        if pe_ind_71 is not UNSET:
            field_dict["PE_ind_71"] = pe_ind_71
        if pe_ind_72 is not UNSET:
            field_dict["PE_ind_72"] = pe_ind_72
        if pe_ind_73 is not UNSET:
            field_dict["PE_ind_73"] = pe_ind_73
        if pe_ind_74 is not UNSET:
            field_dict["PE_ind_74"] = pe_ind_74
        if pe_ind_75 is not UNSET:
            field_dict["PE_ind_75"] = pe_ind_75
        if pe_ind_77 is not UNSET:
            field_dict["PE_ind_77"] = pe_ind_77
        if pe_ind_78 is not UNSET:
            field_dict["PE_ind_78"] = pe_ind_78
        if pe_ind_79 is not UNSET:
            field_dict["PE_ind_79"] = pe_ind_79
        if pe_ind_80 is not UNSET:
            field_dict["PE_ind_80"] = pe_ind_80
        if pe_ind_81 is not UNSET:
            field_dict["PE_ind_81"] = pe_ind_81
        if pe_ind_82 is not UNSET:
            field_dict["PE_ind_82"] = pe_ind_82
        if pe_ind_85 is not UNSET:
            field_dict["PE_ind_85"] = pe_ind_85
        if pe_ind_86 is not UNSET:
            field_dict["PE_ind_86"] = pe_ind_86
        if pe_ind_87 is not UNSET:
            field_dict["PE_ind_87"] = pe_ind_87
        if pe_ind_88 is not UNSET:
            field_dict["PE_ind_88"] = pe_ind_88
        if pe_ind_90 is not UNSET:
            field_dict["PE_ind_90"] = pe_ind_90
        if pe_ind_91 is not UNSET:
            field_dict["PE_ind_91"] = pe_ind_91
        if pe_ind_92 is not UNSET:
            field_dict["PE_ind_92"] = pe_ind_92
        if pe_ind_93 is not UNSET:
            field_dict["PE_ind_93"] = pe_ind_93
        if pe_ind_94 is not UNSET:
            field_dict["PE_ind_94"] = pe_ind_94
        if pe_ind_95 is not UNSET:
            field_dict["PE_ind_95"] = pe_ind_95
        if pe_ind_96 is not UNSET:
            field_dict["PE_ind_96"] = pe_ind_96
        if pe_ind_b is not UNSET:
            field_dict["PE_ind_B"] = pe_ind_b
        if pe_ind_b_d_e is not UNSET:
            field_dict["PE_ind_B_D_E"] = pe_ind_b_d_e
        if pe_ind_c is not UNSET:
            field_dict["PE_ind_C"] = pe_ind_c
        if pe_ind_d is not UNSET:
            field_dict["PE_ind_D"] = pe_ind_d
        if pe_ind_d_e is not UNSET:
            field_dict["PE_ind_D_E"] = pe_ind_d_e
        if pe_ind_e is not UNSET:
            field_dict["PE_ind_E"] = pe_ind_e
        if pe_ind_g is not UNSET:
            field_dict["PE_ind_G"] = pe_ind_g
        if pe_ind_g45_46 is not UNSET:
            field_dict["PE_ind_G45_46"] = pe_ind_g45_46
        if pe_ind_g47 is not UNSET:
            field_dict["PE_ind_G47"] = pe_ind_g47
        if pe_ind_h is not UNSET:
            field_dict["PE_ind_H"] = pe_ind_h
        if pe_ind_i is not UNSET:
            field_dict["PE_ind_I"] = pe_ind_i
        if pe_ind_j is not UNSET:
            field_dict["PE_ind_J"] = pe_ind_j
        if pe_ind_k is not UNSET:
            field_dict["PE_ind_K"] = pe_ind_k
        if pe_ind_l is not UNSET:
            field_dict["PE_ind_L"] = pe_ind_l
        if pe_ind_m is not UNSET:
            field_dict["PE_ind_M"] = pe_ind_m
        if pe_ind_m_n is not UNSET:
            field_dict["PE_ind_M_N"] = pe_ind_m_n
        if pe_ind_n is not UNSET:
            field_dict["PE_ind_N"] = pe_ind_n
        if pe_ind_p is not UNSET:
            field_dict["PE_ind_P"] = pe_ind_p
        if pe_ind_p_s is not UNSET:
            field_dict["PE_ind_P_S"] = pe_ind_p_s
        if pe_ind_q is not UNSET:
            field_dict["PE_ind_Q"] = pe_ind_q
        if pe_ind_r is not UNSET:
            field_dict["PE_ind_R"] = pe_ind_r
        if pe_ind_s is not UNSET:
            field_dict["PE_ind_S"] = pe_ind_s
        if pe_ind_site is not UNSET:
            field_dict["PE_ind_SITE"] = pe_ind_site
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

        def _parse_ccyy(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ccyy = _parse_ccyy(d.pop("CCYY", UNSET))

        def _parse_dc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dc = _parse_dc(d.pop("DC", UNSET))

        def _parse_dc_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_chi = _parse_dc_chi(d.pop("DC_CHI", UNSET))

        def _parse_dc_class(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_class = _parse_dc_class(d.pop("DC_CLASS", UNSET))

        def _parse_dc_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_eng = _parse_dc_eng(d.pop("DC_ENG", UNSET))

        def _parse_est_ind_08(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_08 = _parse_est_ind_08(d.pop("EST_ind_08", UNSET))

        def _parse_est_ind_10(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_10 = _parse_est_ind_10(d.pop("EST_ind_10", UNSET))

        def _parse_est_ind_11(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_11 = _parse_est_ind_11(d.pop("EST_ind_11", UNSET))

        def _parse_est_ind_12(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_12 = _parse_est_ind_12(d.pop("EST_ind_12", UNSET))

        def _parse_est_ind_13(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_13 = _parse_est_ind_13(d.pop("EST_ind_13", UNSET))

        def _parse_est_ind_14(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_14 = _parse_est_ind_14(d.pop("EST_ind_14", UNSET))

        def _parse_est_ind_15(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_15 = _parse_est_ind_15(d.pop("EST_ind_15", UNSET))

        def _parse_est_ind_16(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_16 = _parse_est_ind_16(d.pop("EST_ind_16", UNSET))

        def _parse_est_ind_17(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_17 = _parse_est_ind_17(d.pop("EST_ind_17", UNSET))

        def _parse_est_ind_18(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_18 = _parse_est_ind_18(d.pop("EST_ind_18", UNSET))

        def _parse_est_ind_19(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_19 = _parse_est_ind_19(d.pop("EST_ind_19", UNSET))

        def _parse_est_ind_20(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_20 = _parse_est_ind_20(d.pop("EST_ind_20", UNSET))

        def _parse_est_ind_21(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_21 = _parse_est_ind_21(d.pop("EST_ind_21", UNSET))

        def _parse_est_ind_22(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_22 = _parse_est_ind_22(d.pop("EST_ind_22", UNSET))

        def _parse_est_ind_23(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_23 = _parse_est_ind_23(d.pop("EST_ind_23", UNSET))

        def _parse_est_ind_24(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_24 = _parse_est_ind_24(d.pop("EST_ind_24", UNSET))

        def _parse_est_ind_25(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_25 = _parse_est_ind_25(d.pop("EST_ind_25", UNSET))

        def _parse_est_ind_26(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_26 = _parse_est_ind_26(d.pop("EST_ind_26", UNSET))

        def _parse_est_ind_27(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_27 = _parse_est_ind_27(d.pop("EST_ind_27", UNSET))

        def _parse_est_ind_28(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_28 = _parse_est_ind_28(d.pop("EST_ind_28", UNSET))

        def _parse_est_ind_29(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_29 = _parse_est_ind_29(d.pop("EST_ind_29", UNSET))

        def _parse_est_ind_30(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_30 = _parse_est_ind_30(d.pop("EST_ind_30", UNSET))

        def _parse_est_ind_31(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_31 = _parse_est_ind_31(d.pop("EST_ind_31", UNSET))

        def _parse_est_ind_32(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_32 = _parse_est_ind_32(d.pop("EST_ind_32", UNSET))

        def _parse_est_ind_33(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_33 = _parse_est_ind_33(d.pop("EST_ind_33", UNSET))

        def _parse_est_ind_35(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_35 = _parse_est_ind_35(d.pop("EST_ind_35", UNSET))

        def _parse_est_ind_37(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_37 = _parse_est_ind_37(d.pop("EST_ind_37", UNSET))

        def _parse_est_ind_38(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_38 = _parse_est_ind_38(d.pop("EST_ind_38", UNSET))

        def _parse_est_ind_39(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_39 = _parse_est_ind_39(d.pop("EST_ind_39", UNSET))

        def _parse_est_ind_45(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_45 = _parse_est_ind_45(d.pop("EST_ind_45", UNSET))

        def _parse_est_ind_46(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_46 = _parse_est_ind_46(d.pop("EST_ind_46", UNSET))

        def _parse_est_ind_47(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_47 = _parse_est_ind_47(d.pop("EST_ind_47", UNSET))

        def _parse_est_ind_49(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_49 = _parse_est_ind_49(d.pop("EST_ind_49", UNSET))

        def _parse_est_ind_50(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_50 = _parse_est_ind_50(d.pop("EST_ind_50", UNSET))

        def _parse_est_ind_51(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_51 = _parse_est_ind_51(d.pop("EST_ind_51", UNSET))

        def _parse_est_ind_52(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_52 = _parse_est_ind_52(d.pop("EST_ind_52", UNSET))

        def _parse_est_ind_53(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_53 = _parse_est_ind_53(d.pop("EST_ind_53", UNSET))

        def _parse_est_ind_55(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_55 = _parse_est_ind_55(d.pop("EST_ind_55", UNSET))

        def _parse_est_ind_56(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_56 = _parse_est_ind_56(d.pop("EST_ind_56", UNSET))

        def _parse_est_ind_58(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_58 = _parse_est_ind_58(d.pop("EST_ind_58", UNSET))

        def _parse_est_ind_59(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_59 = _parse_est_ind_59(d.pop("EST_ind_59", UNSET))

        def _parse_est_ind_60(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_60 = _parse_est_ind_60(d.pop("EST_ind_60", UNSET))

        def _parse_est_ind_61(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_61 = _parse_est_ind_61(d.pop("EST_ind_61", UNSET))

        def _parse_est_ind_62(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_62 = _parse_est_ind_62(d.pop("EST_ind_62", UNSET))

        def _parse_est_ind_63(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_63 = _parse_est_ind_63(d.pop("EST_ind_63", UNSET))

        def _parse_est_ind_64(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_64 = _parse_est_ind_64(d.pop("EST_ind_64", UNSET))

        def _parse_est_ind_65(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_65 = _parse_est_ind_65(d.pop("EST_ind_65", UNSET))

        def _parse_est_ind_66(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_66 = _parse_est_ind_66(d.pop("EST_ind_66", UNSET))

        def _parse_est_ind_68(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_68 = _parse_est_ind_68(d.pop("EST_ind_68", UNSET))

        def _parse_est_ind_69(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_69 = _parse_est_ind_69(d.pop("EST_ind_69", UNSET))

        def _parse_est_ind_70(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_70 = _parse_est_ind_70(d.pop("EST_ind_70", UNSET))

        def _parse_est_ind_71(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_71 = _parse_est_ind_71(d.pop("EST_ind_71", UNSET))

        def _parse_est_ind_72(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_72 = _parse_est_ind_72(d.pop("EST_ind_72", UNSET))

        def _parse_est_ind_73(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_73 = _parse_est_ind_73(d.pop("EST_ind_73", UNSET))

        def _parse_est_ind_74(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_74 = _parse_est_ind_74(d.pop("EST_ind_74", UNSET))

        def _parse_est_ind_75(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_75 = _parse_est_ind_75(d.pop("EST_ind_75", UNSET))

        def _parse_est_ind_77(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_77 = _parse_est_ind_77(d.pop("EST_ind_77", UNSET))

        def _parse_est_ind_78(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_78 = _parse_est_ind_78(d.pop("EST_ind_78", UNSET))

        def _parse_est_ind_79(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_79 = _parse_est_ind_79(d.pop("EST_ind_79", UNSET))

        def _parse_est_ind_80(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_80 = _parse_est_ind_80(d.pop("EST_ind_80", UNSET))

        def _parse_est_ind_81(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_81 = _parse_est_ind_81(d.pop("EST_ind_81", UNSET))

        def _parse_est_ind_82(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_82 = _parse_est_ind_82(d.pop("EST_ind_82", UNSET))

        def _parse_est_ind_85(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_85 = _parse_est_ind_85(d.pop("EST_ind_85", UNSET))

        def _parse_est_ind_86(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_86 = _parse_est_ind_86(d.pop("EST_ind_86", UNSET))

        def _parse_est_ind_87(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_87 = _parse_est_ind_87(d.pop("EST_ind_87", UNSET))

        def _parse_est_ind_88(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_88 = _parse_est_ind_88(d.pop("EST_ind_88", UNSET))

        def _parse_est_ind_90(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_90 = _parse_est_ind_90(d.pop("EST_ind_90", UNSET))

        def _parse_est_ind_91(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_91 = _parse_est_ind_91(d.pop("EST_ind_91", UNSET))

        def _parse_est_ind_92(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_92 = _parse_est_ind_92(d.pop("EST_ind_92", UNSET))

        def _parse_est_ind_93(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_93 = _parse_est_ind_93(d.pop("EST_ind_93", UNSET))

        def _parse_est_ind_94(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_94 = _parse_est_ind_94(d.pop("EST_ind_94", UNSET))

        def _parse_est_ind_95(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_95 = _parse_est_ind_95(d.pop("EST_ind_95", UNSET))

        def _parse_est_ind_96(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_96 = _parse_est_ind_96(d.pop("EST_ind_96", UNSET))

        def _parse_est_ind_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_b = _parse_est_ind_b(d.pop("EST_ind_B", UNSET))

        def _parse_est_ind_b_d_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_b_d_e = _parse_est_ind_b_d_e(d.pop("EST_ind_B_D_E", UNSET))

        def _parse_est_ind_c(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_c = _parse_est_ind_c(d.pop("EST_ind_C", UNSET))

        def _parse_est_ind_d(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_d = _parse_est_ind_d(d.pop("EST_ind_D", UNSET))

        def _parse_est_ind_d_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_d_e = _parse_est_ind_d_e(d.pop("EST_ind_D_E", UNSET))

        def _parse_est_ind_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        est_ind_e = _parse_est_ind_e(d.pop("EST_ind_E", UNSET))

        def _parse_est_ind_g(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_g = _parse_est_ind_g(d.pop("EST_ind_G", UNSET))

        def _parse_est_ind_g45_46(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_g45_46 = _parse_est_ind_g45_46(d.pop("EST_ind_G45_46", UNSET))

        def _parse_est_ind_g47(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_g47 = _parse_est_ind_g47(d.pop("EST_ind_G47", UNSET))

        def _parse_est_ind_h(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_h = _parse_est_ind_h(d.pop("EST_ind_H", UNSET))

        def _parse_est_ind_i(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_i = _parse_est_ind_i(d.pop("EST_ind_I", UNSET))

        def _parse_est_ind_j(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_j = _parse_est_ind_j(d.pop("EST_ind_J", UNSET))

        def _parse_est_ind_k(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_k = _parse_est_ind_k(d.pop("EST_ind_K", UNSET))

        def _parse_est_ind_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_l = _parse_est_ind_l(d.pop("EST_ind_L", UNSET))

        def _parse_est_ind_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_m = _parse_est_ind_m(d.pop("EST_ind_M", UNSET))

        def _parse_est_ind_m_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_m_n = _parse_est_ind_m_n(d.pop("EST_ind_M_N", UNSET))

        def _parse_est_ind_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_n = _parse_est_ind_n(d.pop("EST_ind_N", UNSET))

        def _parse_est_ind_p(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_p = _parse_est_ind_p(d.pop("EST_ind_P", UNSET))

        def _parse_est_ind_p_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_p_s = _parse_est_ind_p_s(d.pop("EST_ind_P_S", UNSET))

        def _parse_est_ind_q(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_q = _parse_est_ind_q(d.pop("EST_ind_Q", UNSET))

        def _parse_est_ind_r(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_r = _parse_est_ind_r(d.pop("EST_ind_R", UNSET))

        def _parse_est_ind_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_s = _parse_est_ind_s(d.pop("EST_ind_S", UNSET))

        def _parse_est_ind_site(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est_ind_site = _parse_est_ind_site(d.pop("EST_ind_SITE", UNSET))

        def _parse_pe_ind_08(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_08 = _parse_pe_ind_08(d.pop("PE_ind_08", UNSET))

        def _parse_pe_ind_10(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_10 = _parse_pe_ind_10(d.pop("PE_ind_10", UNSET))

        def _parse_pe_ind_11(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_11 = _parse_pe_ind_11(d.pop("PE_ind_11", UNSET))

        def _parse_pe_ind_12(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_12 = _parse_pe_ind_12(d.pop("PE_ind_12", UNSET))

        def _parse_pe_ind_13(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_13 = _parse_pe_ind_13(d.pop("PE_ind_13", UNSET))

        def _parse_pe_ind_14(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_14 = _parse_pe_ind_14(d.pop("PE_ind_14", UNSET))

        def _parse_pe_ind_15(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_15 = _parse_pe_ind_15(d.pop("PE_ind_15", UNSET))

        def _parse_pe_ind_16(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_16 = _parse_pe_ind_16(d.pop("PE_ind_16", UNSET))

        def _parse_pe_ind_17(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_17 = _parse_pe_ind_17(d.pop("PE_ind_17", UNSET))

        def _parse_pe_ind_18(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_18 = _parse_pe_ind_18(d.pop("PE_ind_18", UNSET))

        def _parse_pe_ind_19(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_19 = _parse_pe_ind_19(d.pop("PE_ind_19", UNSET))

        def _parse_pe_ind_20(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_20 = _parse_pe_ind_20(d.pop("PE_ind_20", UNSET))

        def _parse_pe_ind_21(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_21 = _parse_pe_ind_21(d.pop("PE_ind_21", UNSET))

        def _parse_pe_ind_22(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_22 = _parse_pe_ind_22(d.pop("PE_ind_22", UNSET))

        def _parse_pe_ind_23(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_23 = _parse_pe_ind_23(d.pop("PE_ind_23", UNSET))

        def _parse_pe_ind_24(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_24 = _parse_pe_ind_24(d.pop("PE_ind_24", UNSET))

        def _parse_pe_ind_25(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_25 = _parse_pe_ind_25(d.pop("PE_ind_25", UNSET))

        def _parse_pe_ind_26(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_26 = _parse_pe_ind_26(d.pop("PE_ind_26", UNSET))

        def _parse_pe_ind_27(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_27 = _parse_pe_ind_27(d.pop("PE_ind_27", UNSET))

        def _parse_pe_ind_28(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_28 = _parse_pe_ind_28(d.pop("PE_ind_28", UNSET))

        def _parse_pe_ind_29(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_29 = _parse_pe_ind_29(d.pop("PE_ind_29", UNSET))

        def _parse_pe_ind_30(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_30 = _parse_pe_ind_30(d.pop("PE_ind_30", UNSET))

        def _parse_pe_ind_31(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_31 = _parse_pe_ind_31(d.pop("PE_ind_31", UNSET))

        def _parse_pe_ind_32(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_32 = _parse_pe_ind_32(d.pop("PE_ind_32", UNSET))

        def _parse_pe_ind_33(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_33 = _parse_pe_ind_33(d.pop("PE_ind_33", UNSET))

        def _parse_pe_ind_35(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_35 = _parse_pe_ind_35(d.pop("PE_ind_35", UNSET))

        def _parse_pe_ind_37(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_37 = _parse_pe_ind_37(d.pop("PE_ind_37", UNSET))

        def _parse_pe_ind_38(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_38 = _parse_pe_ind_38(d.pop("PE_ind_38", UNSET))

        def _parse_pe_ind_39(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_39 = _parse_pe_ind_39(d.pop("PE_ind_39", UNSET))

        def _parse_pe_ind_45(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_45 = _parse_pe_ind_45(d.pop("PE_ind_45", UNSET))

        def _parse_pe_ind_46(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_46 = _parse_pe_ind_46(d.pop("PE_ind_46", UNSET))

        def _parse_pe_ind_47(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_47 = _parse_pe_ind_47(d.pop("PE_ind_47", UNSET))

        def _parse_pe_ind_49(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_49 = _parse_pe_ind_49(d.pop("PE_ind_49", UNSET))

        def _parse_pe_ind_50(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_50 = _parse_pe_ind_50(d.pop("PE_ind_50", UNSET))

        def _parse_pe_ind_51(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_51 = _parse_pe_ind_51(d.pop("PE_ind_51", UNSET))

        def _parse_pe_ind_52(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_52 = _parse_pe_ind_52(d.pop("PE_ind_52", UNSET))

        def _parse_pe_ind_53(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_53 = _parse_pe_ind_53(d.pop("PE_ind_53", UNSET))

        def _parse_pe_ind_55(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_55 = _parse_pe_ind_55(d.pop("PE_ind_55", UNSET))

        def _parse_pe_ind_56(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_56 = _parse_pe_ind_56(d.pop("PE_ind_56", UNSET))

        def _parse_pe_ind_58(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_58 = _parse_pe_ind_58(d.pop("PE_ind_58", UNSET))

        def _parse_pe_ind_59(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_59 = _parse_pe_ind_59(d.pop("PE_ind_59", UNSET))

        def _parse_pe_ind_60(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_60 = _parse_pe_ind_60(d.pop("PE_ind_60", UNSET))

        def _parse_pe_ind_61(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_61 = _parse_pe_ind_61(d.pop("PE_ind_61", UNSET))

        def _parse_pe_ind_62(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_62 = _parse_pe_ind_62(d.pop("PE_ind_62", UNSET))

        def _parse_pe_ind_63(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_63 = _parse_pe_ind_63(d.pop("PE_ind_63", UNSET))

        def _parse_pe_ind_64(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_64 = _parse_pe_ind_64(d.pop("PE_ind_64", UNSET))

        def _parse_pe_ind_65(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_65 = _parse_pe_ind_65(d.pop("PE_ind_65", UNSET))

        def _parse_pe_ind_66(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_66 = _parse_pe_ind_66(d.pop("PE_ind_66", UNSET))

        def _parse_pe_ind_68(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_68 = _parse_pe_ind_68(d.pop("PE_ind_68", UNSET))

        def _parse_pe_ind_69(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_69 = _parse_pe_ind_69(d.pop("PE_ind_69", UNSET))

        def _parse_pe_ind_70(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_70 = _parse_pe_ind_70(d.pop("PE_ind_70", UNSET))

        def _parse_pe_ind_71(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_71 = _parse_pe_ind_71(d.pop("PE_ind_71", UNSET))

        def _parse_pe_ind_72(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_72 = _parse_pe_ind_72(d.pop("PE_ind_72", UNSET))

        def _parse_pe_ind_73(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_73 = _parse_pe_ind_73(d.pop("PE_ind_73", UNSET))

        def _parse_pe_ind_74(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_74 = _parse_pe_ind_74(d.pop("PE_ind_74", UNSET))

        def _parse_pe_ind_75(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_75 = _parse_pe_ind_75(d.pop("PE_ind_75", UNSET))

        def _parse_pe_ind_77(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_77 = _parse_pe_ind_77(d.pop("PE_ind_77", UNSET))

        def _parse_pe_ind_78(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_78 = _parse_pe_ind_78(d.pop("PE_ind_78", UNSET))

        def _parse_pe_ind_79(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_79 = _parse_pe_ind_79(d.pop("PE_ind_79", UNSET))

        def _parse_pe_ind_80(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_80 = _parse_pe_ind_80(d.pop("PE_ind_80", UNSET))

        def _parse_pe_ind_81(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_81 = _parse_pe_ind_81(d.pop("PE_ind_81", UNSET))

        def _parse_pe_ind_82(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_82 = _parse_pe_ind_82(d.pop("PE_ind_82", UNSET))

        def _parse_pe_ind_85(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_85 = _parse_pe_ind_85(d.pop("PE_ind_85", UNSET))

        def _parse_pe_ind_86(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_86 = _parse_pe_ind_86(d.pop("PE_ind_86", UNSET))

        def _parse_pe_ind_87(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_87 = _parse_pe_ind_87(d.pop("PE_ind_87", UNSET))

        def _parse_pe_ind_88(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_88 = _parse_pe_ind_88(d.pop("PE_ind_88", UNSET))

        def _parse_pe_ind_90(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_90 = _parse_pe_ind_90(d.pop("PE_ind_90", UNSET))

        def _parse_pe_ind_91(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_91 = _parse_pe_ind_91(d.pop("PE_ind_91", UNSET))

        def _parse_pe_ind_92(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_92 = _parse_pe_ind_92(d.pop("PE_ind_92", UNSET))

        def _parse_pe_ind_93(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_93 = _parse_pe_ind_93(d.pop("PE_ind_93", UNSET))

        def _parse_pe_ind_94(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_94 = _parse_pe_ind_94(d.pop("PE_ind_94", UNSET))

        def _parse_pe_ind_95(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_95 = _parse_pe_ind_95(d.pop("PE_ind_95", UNSET))

        def _parse_pe_ind_96(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_96 = _parse_pe_ind_96(d.pop("PE_ind_96", UNSET))

        def _parse_pe_ind_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_b = _parse_pe_ind_b(d.pop("PE_ind_B", UNSET))

        def _parse_pe_ind_b_d_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_b_d_e = _parse_pe_ind_b_d_e(d.pop("PE_ind_B_D_E", UNSET))

        def _parse_pe_ind_c(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_c = _parse_pe_ind_c(d.pop("PE_ind_C", UNSET))

        def _parse_pe_ind_d(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_d = _parse_pe_ind_d(d.pop("PE_ind_D", UNSET))

        def _parse_pe_ind_d_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_d_e = _parse_pe_ind_d_e(d.pop("PE_ind_D_E", UNSET))

        def _parse_pe_ind_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_ind_e = _parse_pe_ind_e(d.pop("PE_ind_E", UNSET))

        def _parse_pe_ind_g(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_g = _parse_pe_ind_g(d.pop("PE_ind_G", UNSET))

        def _parse_pe_ind_g45_46(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_g45_46 = _parse_pe_ind_g45_46(d.pop("PE_ind_G45_46", UNSET))

        def _parse_pe_ind_g47(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_g47 = _parse_pe_ind_g47(d.pop("PE_ind_G47", UNSET))

        def _parse_pe_ind_h(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_h = _parse_pe_ind_h(d.pop("PE_ind_H", UNSET))

        def _parse_pe_ind_i(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_i = _parse_pe_ind_i(d.pop("PE_ind_I", UNSET))

        def _parse_pe_ind_j(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_j = _parse_pe_ind_j(d.pop("PE_ind_J", UNSET))

        def _parse_pe_ind_k(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_k = _parse_pe_ind_k(d.pop("PE_ind_K", UNSET))

        def _parse_pe_ind_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_l = _parse_pe_ind_l(d.pop("PE_ind_L", UNSET))

        def _parse_pe_ind_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_m = _parse_pe_ind_m(d.pop("PE_ind_M", UNSET))

        def _parse_pe_ind_m_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_m_n = _parse_pe_ind_m_n(d.pop("PE_ind_M_N", UNSET))

        def _parse_pe_ind_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_n = _parse_pe_ind_n(d.pop("PE_ind_N", UNSET))

        def _parse_pe_ind_p(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_p = _parse_pe_ind_p(d.pop("PE_ind_P", UNSET))

        def _parse_pe_ind_p_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_p_s = _parse_pe_ind_p_s(d.pop("PE_ind_P_S", UNSET))

        def _parse_pe_ind_q(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_q = _parse_pe_ind_q(d.pop("PE_ind_Q", UNSET))

        def _parse_pe_ind_r(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_r = _parse_pe_ind_r(d.pop("PE_ind_R", UNSET))

        def _parse_pe_ind_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_s = _parse_pe_ind_s(d.pop("PE_ind_S", UNSET))

        def _parse_pe_ind_site(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_ind_site = _parse_pe_ind_site(d.pop("PE_ind_SITE", UNSET))

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
            ccyy=ccyy,
            dc=dc,
            dc_chi=dc_chi,
            dc_class=dc_class,
            dc_eng=dc_eng,
            est_ind_08=est_ind_08,
            est_ind_10=est_ind_10,
            est_ind_11=est_ind_11,
            est_ind_12=est_ind_12,
            est_ind_13=est_ind_13,
            est_ind_14=est_ind_14,
            est_ind_15=est_ind_15,
            est_ind_16=est_ind_16,
            est_ind_17=est_ind_17,
            est_ind_18=est_ind_18,
            est_ind_19=est_ind_19,
            est_ind_20=est_ind_20,
            est_ind_21=est_ind_21,
            est_ind_22=est_ind_22,
            est_ind_23=est_ind_23,
            est_ind_24=est_ind_24,
            est_ind_25=est_ind_25,
            est_ind_26=est_ind_26,
            est_ind_27=est_ind_27,
            est_ind_28=est_ind_28,
            est_ind_29=est_ind_29,
            est_ind_30=est_ind_30,
            est_ind_31=est_ind_31,
            est_ind_32=est_ind_32,
            est_ind_33=est_ind_33,
            est_ind_35=est_ind_35,
            est_ind_37=est_ind_37,
            est_ind_38=est_ind_38,
            est_ind_39=est_ind_39,
            est_ind_45=est_ind_45,
            est_ind_46=est_ind_46,
            est_ind_47=est_ind_47,
            est_ind_49=est_ind_49,
            est_ind_50=est_ind_50,
            est_ind_51=est_ind_51,
            est_ind_52=est_ind_52,
            est_ind_53=est_ind_53,
            est_ind_55=est_ind_55,
            est_ind_56=est_ind_56,
            est_ind_58=est_ind_58,
            est_ind_59=est_ind_59,
            est_ind_60=est_ind_60,
            est_ind_61=est_ind_61,
            est_ind_62=est_ind_62,
            est_ind_63=est_ind_63,
            est_ind_64=est_ind_64,
            est_ind_65=est_ind_65,
            est_ind_66=est_ind_66,
            est_ind_68=est_ind_68,
            est_ind_69=est_ind_69,
            est_ind_70=est_ind_70,
            est_ind_71=est_ind_71,
            est_ind_72=est_ind_72,
            est_ind_73=est_ind_73,
            est_ind_74=est_ind_74,
            est_ind_75=est_ind_75,
            est_ind_77=est_ind_77,
            est_ind_78=est_ind_78,
            est_ind_79=est_ind_79,
            est_ind_80=est_ind_80,
            est_ind_81=est_ind_81,
            est_ind_82=est_ind_82,
            est_ind_85=est_ind_85,
            est_ind_86=est_ind_86,
            est_ind_87=est_ind_87,
            est_ind_88=est_ind_88,
            est_ind_90=est_ind_90,
            est_ind_91=est_ind_91,
            est_ind_92=est_ind_92,
            est_ind_93=est_ind_93,
            est_ind_94=est_ind_94,
            est_ind_95=est_ind_95,
            est_ind_96=est_ind_96,
            est_ind_b=est_ind_b,
            est_ind_b_d_e=est_ind_b_d_e,
            est_ind_c=est_ind_c,
            est_ind_d=est_ind_d,
            est_ind_d_e=est_ind_d_e,
            est_ind_e=est_ind_e,
            est_ind_g=est_ind_g,
            est_ind_g45_46=est_ind_g45_46,
            est_ind_g47=est_ind_g47,
            est_ind_h=est_ind_h,
            est_ind_i=est_ind_i,
            est_ind_j=est_ind_j,
            est_ind_k=est_ind_k,
            est_ind_l=est_ind_l,
            est_ind_m=est_ind_m,
            est_ind_m_n=est_ind_m_n,
            est_ind_n=est_ind_n,
            est_ind_p=est_ind_p,
            est_ind_p_s=est_ind_p_s,
            est_ind_q=est_ind_q,
            est_ind_r=est_ind_r,
            est_ind_s=est_ind_s,
            est_ind_site=est_ind_site,
            pe_ind_08=pe_ind_08,
            pe_ind_10=pe_ind_10,
            pe_ind_11=pe_ind_11,
            pe_ind_12=pe_ind_12,
            pe_ind_13=pe_ind_13,
            pe_ind_14=pe_ind_14,
            pe_ind_15=pe_ind_15,
            pe_ind_16=pe_ind_16,
            pe_ind_17=pe_ind_17,
            pe_ind_18=pe_ind_18,
            pe_ind_19=pe_ind_19,
            pe_ind_20=pe_ind_20,
            pe_ind_21=pe_ind_21,
            pe_ind_22=pe_ind_22,
            pe_ind_23=pe_ind_23,
            pe_ind_24=pe_ind_24,
            pe_ind_25=pe_ind_25,
            pe_ind_26=pe_ind_26,
            pe_ind_27=pe_ind_27,
            pe_ind_28=pe_ind_28,
            pe_ind_29=pe_ind_29,
            pe_ind_30=pe_ind_30,
            pe_ind_31=pe_ind_31,
            pe_ind_32=pe_ind_32,
            pe_ind_33=pe_ind_33,
            pe_ind_35=pe_ind_35,
            pe_ind_37=pe_ind_37,
            pe_ind_38=pe_ind_38,
            pe_ind_39=pe_ind_39,
            pe_ind_45=pe_ind_45,
            pe_ind_46=pe_ind_46,
            pe_ind_47=pe_ind_47,
            pe_ind_49=pe_ind_49,
            pe_ind_50=pe_ind_50,
            pe_ind_51=pe_ind_51,
            pe_ind_52=pe_ind_52,
            pe_ind_53=pe_ind_53,
            pe_ind_55=pe_ind_55,
            pe_ind_56=pe_ind_56,
            pe_ind_58=pe_ind_58,
            pe_ind_59=pe_ind_59,
            pe_ind_60=pe_ind_60,
            pe_ind_61=pe_ind_61,
            pe_ind_62=pe_ind_62,
            pe_ind_63=pe_ind_63,
            pe_ind_64=pe_ind_64,
            pe_ind_65=pe_ind_65,
            pe_ind_66=pe_ind_66,
            pe_ind_68=pe_ind_68,
            pe_ind_69=pe_ind_69,
            pe_ind_70=pe_ind_70,
            pe_ind_71=pe_ind_71,
            pe_ind_72=pe_ind_72,
            pe_ind_73=pe_ind_73,
            pe_ind_74=pe_ind_74,
            pe_ind_75=pe_ind_75,
            pe_ind_77=pe_ind_77,
            pe_ind_78=pe_ind_78,
            pe_ind_79=pe_ind_79,
            pe_ind_80=pe_ind_80,
            pe_ind_81=pe_ind_81,
            pe_ind_82=pe_ind_82,
            pe_ind_85=pe_ind_85,
            pe_ind_86=pe_ind_86,
            pe_ind_87=pe_ind_87,
            pe_ind_88=pe_ind_88,
            pe_ind_90=pe_ind_90,
            pe_ind_91=pe_ind_91,
            pe_ind_92=pe_ind_92,
            pe_ind_93=pe_ind_93,
            pe_ind_94=pe_ind_94,
            pe_ind_95=pe_ind_95,
            pe_ind_96=pe_ind_96,
            pe_ind_b=pe_ind_b,
            pe_ind_b_d_e=pe_ind_b_d_e,
            pe_ind_c=pe_ind_c,
            pe_ind_d=pe_ind_d,
            pe_ind_d_e=pe_ind_d_e,
            pe_ind_e=pe_ind_e,
            pe_ind_g=pe_ind_g,
            pe_ind_g45_46=pe_ind_g45_46,
            pe_ind_g47=pe_ind_g47,
            pe_ind_h=pe_ind_h,
            pe_ind_i=pe_ind_i,
            pe_ind_j=pe_ind_j,
            pe_ind_k=pe_ind_k,
            pe_ind_l=pe_ind_l,
            pe_ind_m=pe_ind_m,
            pe_ind_m_n=pe_ind_m_n,
            pe_ind_n=pe_ind_n,
            pe_ind_p=pe_ind_p,
            pe_ind_p_s=pe_ind_p_s,
            pe_ind_q=pe_ind_q,
            pe_ind_r=pe_ind_r,
            pe_ind_s=pe_ind_s,
            pe_ind_site=pe_ind_site,
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
