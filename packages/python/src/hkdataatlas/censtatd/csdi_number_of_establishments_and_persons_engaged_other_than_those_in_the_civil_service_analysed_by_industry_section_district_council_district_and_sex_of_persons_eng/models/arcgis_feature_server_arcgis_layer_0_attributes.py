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
        dc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dc_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        dc_class (None | str | Unset): Publisher field type: esriFieldTypeString
        dc_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        est (float | None | Unset): Publisher field type: esriFieldTypeDouble
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
        pe (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_b (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_f_ind_b_d_e (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_f_ind_c (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_d (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_f_ind_d_e (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_f_ind_e (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_f_ind_g (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_g45_46 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_g47 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_h (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_i (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_j (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_k (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_l (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_m_n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_p (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_p_s (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_q (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_r (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_s (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_f_ind_site (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_b (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_m_ind_b_d_e (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_m_ind_c (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_d (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_m_ind_d_e (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_m_ind_e (None | str | Unset): Publisher field type: esriFieldTypeString
        pe_m_ind_g (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_g45_46 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_g47 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_h (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_i (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_j (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_k (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_l (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_m_n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_p (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_p_s (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_q (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_r (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_s (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pe_m_ind_site (float | None | Unset): Publisher field type: esriFieldTypeDouble
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
        yymm (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    dc: float | None | Unset = UNSET
    dc_chi: None | str | Unset = UNSET
    dc_class: None | str | Unset = UNSET
    dc_eng: None | str | Unset = UNSET
    est: float | None | Unset = UNSET
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
    pe: float | None | Unset = UNSET
    pe_f: float | None | Unset = UNSET
    pe_f_ind_b: None | str | Unset = UNSET
    pe_f_ind_b_d_e: None | str | Unset = UNSET
    pe_f_ind_c: float | None | Unset = UNSET
    pe_f_ind_d: None | str | Unset = UNSET
    pe_f_ind_d_e: None | str | Unset = UNSET
    pe_f_ind_e: None | str | Unset = UNSET
    pe_f_ind_g: float | None | Unset = UNSET
    pe_f_ind_g45_46: float | None | Unset = UNSET
    pe_f_ind_g47: float | None | Unset = UNSET
    pe_f_ind_h: float | None | Unset = UNSET
    pe_f_ind_i: float | None | Unset = UNSET
    pe_f_ind_j: float | None | Unset = UNSET
    pe_f_ind_k: float | None | Unset = UNSET
    pe_f_ind_l: float | None | Unset = UNSET
    pe_f_ind_m: float | None | Unset = UNSET
    pe_f_ind_m_n: float | None | Unset = UNSET
    pe_f_ind_n: float | None | Unset = UNSET
    pe_f_ind_p: float | None | Unset = UNSET
    pe_f_ind_p_s: float | None | Unset = UNSET
    pe_f_ind_q: float | None | Unset = UNSET
    pe_f_ind_r: float | None | Unset = UNSET
    pe_f_ind_s: float | None | Unset = UNSET
    pe_f_ind_site: float | None | Unset = UNSET
    pe_m: float | None | Unset = UNSET
    pe_m_ind_b: None | str | Unset = UNSET
    pe_m_ind_b_d_e: None | str | Unset = UNSET
    pe_m_ind_c: float | None | Unset = UNSET
    pe_m_ind_d: None | str | Unset = UNSET
    pe_m_ind_d_e: None | str | Unset = UNSET
    pe_m_ind_e: None | str | Unset = UNSET
    pe_m_ind_g: float | None | Unset = UNSET
    pe_m_ind_g45_46: float | None | Unset = UNSET
    pe_m_ind_g47: float | None | Unset = UNSET
    pe_m_ind_h: float | None | Unset = UNSET
    pe_m_ind_i: float | None | Unset = UNSET
    pe_m_ind_j: float | None | Unset = UNSET
    pe_m_ind_k: float | None | Unset = UNSET
    pe_m_ind_l: float | None | Unset = UNSET
    pe_m_ind_m: float | None | Unset = UNSET
    pe_m_ind_m_n: float | None | Unset = UNSET
    pe_m_ind_n: float | None | Unset = UNSET
    pe_m_ind_p: float | None | Unset = UNSET
    pe_m_ind_p_s: float | None | Unset = UNSET
    pe_m_ind_q: float | None | Unset = UNSET
    pe_m_ind_r: float | None | Unset = UNSET
    pe_m_ind_s: float | None | Unset = UNSET
    pe_m_ind_site: float | None | Unset = UNSET
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
    yymm: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        est: float | None | Unset
        if isinstance(self.est, Unset):
            est = UNSET
        else:
            est = self.est

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

        pe: float | None | Unset
        if isinstance(self.pe, Unset):
            pe = UNSET
        else:
            pe = self.pe

        pe_f: float | None | Unset
        if isinstance(self.pe_f, Unset):
            pe_f = UNSET
        else:
            pe_f = self.pe_f

        pe_f_ind_b: None | str | Unset
        if isinstance(self.pe_f_ind_b, Unset):
            pe_f_ind_b = UNSET
        else:
            pe_f_ind_b = self.pe_f_ind_b

        pe_f_ind_b_d_e: None | str | Unset
        if isinstance(self.pe_f_ind_b_d_e, Unset):
            pe_f_ind_b_d_e = UNSET
        else:
            pe_f_ind_b_d_e = self.pe_f_ind_b_d_e

        pe_f_ind_c: float | None | Unset
        if isinstance(self.pe_f_ind_c, Unset):
            pe_f_ind_c = UNSET
        else:
            pe_f_ind_c = self.pe_f_ind_c

        pe_f_ind_d: None | str | Unset
        if isinstance(self.pe_f_ind_d, Unset):
            pe_f_ind_d = UNSET
        else:
            pe_f_ind_d = self.pe_f_ind_d

        pe_f_ind_d_e: None | str | Unset
        if isinstance(self.pe_f_ind_d_e, Unset):
            pe_f_ind_d_e = UNSET
        else:
            pe_f_ind_d_e = self.pe_f_ind_d_e

        pe_f_ind_e: None | str | Unset
        if isinstance(self.pe_f_ind_e, Unset):
            pe_f_ind_e = UNSET
        else:
            pe_f_ind_e = self.pe_f_ind_e

        pe_f_ind_g: float | None | Unset
        if isinstance(self.pe_f_ind_g, Unset):
            pe_f_ind_g = UNSET
        else:
            pe_f_ind_g = self.pe_f_ind_g

        pe_f_ind_g45_46: float | None | Unset
        if isinstance(self.pe_f_ind_g45_46, Unset):
            pe_f_ind_g45_46 = UNSET
        else:
            pe_f_ind_g45_46 = self.pe_f_ind_g45_46

        pe_f_ind_g47: float | None | Unset
        if isinstance(self.pe_f_ind_g47, Unset):
            pe_f_ind_g47 = UNSET
        else:
            pe_f_ind_g47 = self.pe_f_ind_g47

        pe_f_ind_h: float | None | Unset
        if isinstance(self.pe_f_ind_h, Unset):
            pe_f_ind_h = UNSET
        else:
            pe_f_ind_h = self.pe_f_ind_h

        pe_f_ind_i: float | None | Unset
        if isinstance(self.pe_f_ind_i, Unset):
            pe_f_ind_i = UNSET
        else:
            pe_f_ind_i = self.pe_f_ind_i

        pe_f_ind_j: float | None | Unset
        if isinstance(self.pe_f_ind_j, Unset):
            pe_f_ind_j = UNSET
        else:
            pe_f_ind_j = self.pe_f_ind_j

        pe_f_ind_k: float | None | Unset
        if isinstance(self.pe_f_ind_k, Unset):
            pe_f_ind_k = UNSET
        else:
            pe_f_ind_k = self.pe_f_ind_k

        pe_f_ind_l: float | None | Unset
        if isinstance(self.pe_f_ind_l, Unset):
            pe_f_ind_l = UNSET
        else:
            pe_f_ind_l = self.pe_f_ind_l

        pe_f_ind_m: float | None | Unset
        if isinstance(self.pe_f_ind_m, Unset):
            pe_f_ind_m = UNSET
        else:
            pe_f_ind_m = self.pe_f_ind_m

        pe_f_ind_m_n: float | None | Unset
        if isinstance(self.pe_f_ind_m_n, Unset):
            pe_f_ind_m_n = UNSET
        else:
            pe_f_ind_m_n = self.pe_f_ind_m_n

        pe_f_ind_n: float | None | Unset
        if isinstance(self.pe_f_ind_n, Unset):
            pe_f_ind_n = UNSET
        else:
            pe_f_ind_n = self.pe_f_ind_n

        pe_f_ind_p: float | None | Unset
        if isinstance(self.pe_f_ind_p, Unset):
            pe_f_ind_p = UNSET
        else:
            pe_f_ind_p = self.pe_f_ind_p

        pe_f_ind_p_s: float | None | Unset
        if isinstance(self.pe_f_ind_p_s, Unset):
            pe_f_ind_p_s = UNSET
        else:
            pe_f_ind_p_s = self.pe_f_ind_p_s

        pe_f_ind_q: float | None | Unset
        if isinstance(self.pe_f_ind_q, Unset):
            pe_f_ind_q = UNSET
        else:
            pe_f_ind_q = self.pe_f_ind_q

        pe_f_ind_r: float | None | Unset
        if isinstance(self.pe_f_ind_r, Unset):
            pe_f_ind_r = UNSET
        else:
            pe_f_ind_r = self.pe_f_ind_r

        pe_f_ind_s: float | None | Unset
        if isinstance(self.pe_f_ind_s, Unset):
            pe_f_ind_s = UNSET
        else:
            pe_f_ind_s = self.pe_f_ind_s

        pe_f_ind_site: float | None | Unset
        if isinstance(self.pe_f_ind_site, Unset):
            pe_f_ind_site = UNSET
        else:
            pe_f_ind_site = self.pe_f_ind_site

        pe_m: float | None | Unset
        if isinstance(self.pe_m, Unset):
            pe_m = UNSET
        else:
            pe_m = self.pe_m

        pe_m_ind_b: None | str | Unset
        if isinstance(self.pe_m_ind_b, Unset):
            pe_m_ind_b = UNSET
        else:
            pe_m_ind_b = self.pe_m_ind_b

        pe_m_ind_b_d_e: None | str | Unset
        if isinstance(self.pe_m_ind_b_d_e, Unset):
            pe_m_ind_b_d_e = UNSET
        else:
            pe_m_ind_b_d_e = self.pe_m_ind_b_d_e

        pe_m_ind_c: float | None | Unset
        if isinstance(self.pe_m_ind_c, Unset):
            pe_m_ind_c = UNSET
        else:
            pe_m_ind_c = self.pe_m_ind_c

        pe_m_ind_d: None | str | Unset
        if isinstance(self.pe_m_ind_d, Unset):
            pe_m_ind_d = UNSET
        else:
            pe_m_ind_d = self.pe_m_ind_d

        pe_m_ind_d_e: None | str | Unset
        if isinstance(self.pe_m_ind_d_e, Unset):
            pe_m_ind_d_e = UNSET
        else:
            pe_m_ind_d_e = self.pe_m_ind_d_e

        pe_m_ind_e: None | str | Unset
        if isinstance(self.pe_m_ind_e, Unset):
            pe_m_ind_e = UNSET
        else:
            pe_m_ind_e = self.pe_m_ind_e

        pe_m_ind_g: float | None | Unset
        if isinstance(self.pe_m_ind_g, Unset):
            pe_m_ind_g = UNSET
        else:
            pe_m_ind_g = self.pe_m_ind_g

        pe_m_ind_g45_46: float | None | Unset
        if isinstance(self.pe_m_ind_g45_46, Unset):
            pe_m_ind_g45_46 = UNSET
        else:
            pe_m_ind_g45_46 = self.pe_m_ind_g45_46

        pe_m_ind_g47: float | None | Unset
        if isinstance(self.pe_m_ind_g47, Unset):
            pe_m_ind_g47 = UNSET
        else:
            pe_m_ind_g47 = self.pe_m_ind_g47

        pe_m_ind_h: float | None | Unset
        if isinstance(self.pe_m_ind_h, Unset):
            pe_m_ind_h = UNSET
        else:
            pe_m_ind_h = self.pe_m_ind_h

        pe_m_ind_i: float | None | Unset
        if isinstance(self.pe_m_ind_i, Unset):
            pe_m_ind_i = UNSET
        else:
            pe_m_ind_i = self.pe_m_ind_i

        pe_m_ind_j: float | None | Unset
        if isinstance(self.pe_m_ind_j, Unset):
            pe_m_ind_j = UNSET
        else:
            pe_m_ind_j = self.pe_m_ind_j

        pe_m_ind_k: float | None | Unset
        if isinstance(self.pe_m_ind_k, Unset):
            pe_m_ind_k = UNSET
        else:
            pe_m_ind_k = self.pe_m_ind_k

        pe_m_ind_l: float | None | Unset
        if isinstance(self.pe_m_ind_l, Unset):
            pe_m_ind_l = UNSET
        else:
            pe_m_ind_l = self.pe_m_ind_l

        pe_m_ind_m: float | None | Unset
        if isinstance(self.pe_m_ind_m, Unset):
            pe_m_ind_m = UNSET
        else:
            pe_m_ind_m = self.pe_m_ind_m

        pe_m_ind_m_n: float | None | Unset
        if isinstance(self.pe_m_ind_m_n, Unset):
            pe_m_ind_m_n = UNSET
        else:
            pe_m_ind_m_n = self.pe_m_ind_m_n

        pe_m_ind_n: float | None | Unset
        if isinstance(self.pe_m_ind_n, Unset):
            pe_m_ind_n = UNSET
        else:
            pe_m_ind_n = self.pe_m_ind_n

        pe_m_ind_p: float | None | Unset
        if isinstance(self.pe_m_ind_p, Unset):
            pe_m_ind_p = UNSET
        else:
            pe_m_ind_p = self.pe_m_ind_p

        pe_m_ind_p_s: float | None | Unset
        if isinstance(self.pe_m_ind_p_s, Unset):
            pe_m_ind_p_s = UNSET
        else:
            pe_m_ind_p_s = self.pe_m_ind_p_s

        pe_m_ind_q: float | None | Unset
        if isinstance(self.pe_m_ind_q, Unset):
            pe_m_ind_q = UNSET
        else:
            pe_m_ind_q = self.pe_m_ind_q

        pe_m_ind_r: float | None | Unset
        if isinstance(self.pe_m_ind_r, Unset):
            pe_m_ind_r = UNSET
        else:
            pe_m_ind_r = self.pe_m_ind_r

        pe_m_ind_s: float | None | Unset
        if isinstance(self.pe_m_ind_s, Unset):
            pe_m_ind_s = UNSET
        else:
            pe_m_ind_s = self.pe_m_ind_s

        pe_m_ind_site: float | None | Unset
        if isinstance(self.pe_m_ind_site, Unset):
            pe_m_ind_site = UNSET
        else:
            pe_m_ind_site = self.pe_m_ind_site

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

        yymm: None | str | Unset
        if isinstance(self.yymm, Unset):
            yymm = UNSET
        else:
            yymm = self.yymm

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
        if dc is not UNSET:
            field_dict["DC"] = dc
        if dc_chi is not UNSET:
            field_dict["DC_CHI"] = dc_chi
        if dc_class is not UNSET:
            field_dict["DC_CLASS"] = dc_class
        if dc_eng is not UNSET:
            field_dict["DC_ENG"] = dc_eng
        if est is not UNSET:
            field_dict["EST"] = est
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
            field_dict["EST_ind_Site"] = est_ind_site
        if pe is not UNSET:
            field_dict["PE"] = pe
        if pe_f is not UNSET:
            field_dict["PE_F"] = pe_f
        if pe_f_ind_b is not UNSET:
            field_dict["PE_F_ind_B"] = pe_f_ind_b
        if pe_f_ind_b_d_e is not UNSET:
            field_dict["PE_F_ind_B_D_E"] = pe_f_ind_b_d_e
        if pe_f_ind_c is not UNSET:
            field_dict["PE_F_ind_C"] = pe_f_ind_c
        if pe_f_ind_d is not UNSET:
            field_dict["PE_F_ind_D"] = pe_f_ind_d
        if pe_f_ind_d_e is not UNSET:
            field_dict["PE_F_ind_D_E"] = pe_f_ind_d_e
        if pe_f_ind_e is not UNSET:
            field_dict["PE_F_ind_E"] = pe_f_ind_e
        if pe_f_ind_g is not UNSET:
            field_dict["PE_F_ind_G"] = pe_f_ind_g
        if pe_f_ind_g45_46 is not UNSET:
            field_dict["PE_F_ind_G45_46"] = pe_f_ind_g45_46
        if pe_f_ind_g47 is not UNSET:
            field_dict["PE_F_ind_G47"] = pe_f_ind_g47
        if pe_f_ind_h is not UNSET:
            field_dict["PE_F_ind_H"] = pe_f_ind_h
        if pe_f_ind_i is not UNSET:
            field_dict["PE_F_ind_I"] = pe_f_ind_i
        if pe_f_ind_j is not UNSET:
            field_dict["PE_F_ind_J"] = pe_f_ind_j
        if pe_f_ind_k is not UNSET:
            field_dict["PE_F_ind_K"] = pe_f_ind_k
        if pe_f_ind_l is not UNSET:
            field_dict["PE_F_ind_L"] = pe_f_ind_l
        if pe_f_ind_m is not UNSET:
            field_dict["PE_F_ind_M"] = pe_f_ind_m
        if pe_f_ind_m_n is not UNSET:
            field_dict["PE_F_ind_M_N"] = pe_f_ind_m_n
        if pe_f_ind_n is not UNSET:
            field_dict["PE_F_ind_N"] = pe_f_ind_n
        if pe_f_ind_p is not UNSET:
            field_dict["PE_F_ind_P"] = pe_f_ind_p
        if pe_f_ind_p_s is not UNSET:
            field_dict["PE_F_ind_P_S"] = pe_f_ind_p_s
        if pe_f_ind_q is not UNSET:
            field_dict["PE_F_ind_Q"] = pe_f_ind_q
        if pe_f_ind_r is not UNSET:
            field_dict["PE_F_ind_R"] = pe_f_ind_r
        if pe_f_ind_s is not UNSET:
            field_dict["PE_F_ind_S"] = pe_f_ind_s
        if pe_f_ind_site is not UNSET:
            field_dict["PE_F_ind_Site"] = pe_f_ind_site
        if pe_m is not UNSET:
            field_dict["PE_M"] = pe_m
        if pe_m_ind_b is not UNSET:
            field_dict["PE_M_ind_B"] = pe_m_ind_b
        if pe_m_ind_b_d_e is not UNSET:
            field_dict["PE_M_ind_B_D_E"] = pe_m_ind_b_d_e
        if pe_m_ind_c is not UNSET:
            field_dict["PE_M_ind_C"] = pe_m_ind_c
        if pe_m_ind_d is not UNSET:
            field_dict["PE_M_ind_D"] = pe_m_ind_d
        if pe_m_ind_d_e is not UNSET:
            field_dict["PE_M_ind_D_E"] = pe_m_ind_d_e
        if pe_m_ind_e is not UNSET:
            field_dict["PE_M_ind_E"] = pe_m_ind_e
        if pe_m_ind_g is not UNSET:
            field_dict["PE_M_ind_G"] = pe_m_ind_g
        if pe_m_ind_g45_46 is not UNSET:
            field_dict["PE_M_ind_G45_46"] = pe_m_ind_g45_46
        if pe_m_ind_g47 is not UNSET:
            field_dict["PE_M_ind_G47"] = pe_m_ind_g47
        if pe_m_ind_h is not UNSET:
            field_dict["PE_M_ind_H"] = pe_m_ind_h
        if pe_m_ind_i is not UNSET:
            field_dict["PE_M_ind_I"] = pe_m_ind_i
        if pe_m_ind_j is not UNSET:
            field_dict["PE_M_ind_J"] = pe_m_ind_j
        if pe_m_ind_k is not UNSET:
            field_dict["PE_M_ind_K"] = pe_m_ind_k
        if pe_m_ind_l is not UNSET:
            field_dict["PE_M_ind_L"] = pe_m_ind_l
        if pe_m_ind_m is not UNSET:
            field_dict["PE_M_ind_M"] = pe_m_ind_m
        if pe_m_ind_m_n is not UNSET:
            field_dict["PE_M_ind_M_N"] = pe_m_ind_m_n
        if pe_m_ind_n is not UNSET:
            field_dict["PE_M_ind_N"] = pe_m_ind_n
        if pe_m_ind_p is not UNSET:
            field_dict["PE_M_ind_P"] = pe_m_ind_p
        if pe_m_ind_p_s is not UNSET:
            field_dict["PE_M_ind_P_S"] = pe_m_ind_p_s
        if pe_m_ind_q is not UNSET:
            field_dict["PE_M_ind_Q"] = pe_m_ind_q
        if pe_m_ind_r is not UNSET:
            field_dict["PE_M_ind_R"] = pe_m_ind_r
        if pe_m_ind_s is not UNSET:
            field_dict["PE_M_ind_S"] = pe_m_ind_s
        if pe_m_ind_site is not UNSET:
            field_dict["PE_M_ind_Site"] = pe_m_ind_site
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
            field_dict["PE_ind_Site"] = pe_ind_site
        if yymm is not UNSET:
            field_dict["YYMM"] = yymm
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

        def _parse_est(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        est = _parse_est(d.pop("EST", UNSET))

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

        est_ind_site = _parse_est_ind_site(d.pop("EST_ind_Site", UNSET))

        def _parse_pe(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe = _parse_pe(d.pop("PE", UNSET))

        def _parse_pe_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f = _parse_pe_f(d.pop("PE_F", UNSET))

        def _parse_pe_f_ind_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_f_ind_b = _parse_pe_f_ind_b(d.pop("PE_F_ind_B", UNSET))

        def _parse_pe_f_ind_b_d_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_f_ind_b_d_e = _parse_pe_f_ind_b_d_e(d.pop("PE_F_ind_B_D_E", UNSET))

        def _parse_pe_f_ind_c(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_c = _parse_pe_f_ind_c(d.pop("PE_F_ind_C", UNSET))

        def _parse_pe_f_ind_d(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_f_ind_d = _parse_pe_f_ind_d(d.pop("PE_F_ind_D", UNSET))

        def _parse_pe_f_ind_d_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_f_ind_d_e = _parse_pe_f_ind_d_e(d.pop("PE_F_ind_D_E", UNSET))

        def _parse_pe_f_ind_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_f_ind_e = _parse_pe_f_ind_e(d.pop("PE_F_ind_E", UNSET))

        def _parse_pe_f_ind_g(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_g = _parse_pe_f_ind_g(d.pop("PE_F_ind_G", UNSET))

        def _parse_pe_f_ind_g45_46(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_g45_46 = _parse_pe_f_ind_g45_46(d.pop("PE_F_ind_G45_46", UNSET))

        def _parse_pe_f_ind_g47(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_g47 = _parse_pe_f_ind_g47(d.pop("PE_F_ind_G47", UNSET))

        def _parse_pe_f_ind_h(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_h = _parse_pe_f_ind_h(d.pop("PE_F_ind_H", UNSET))

        def _parse_pe_f_ind_i(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_i = _parse_pe_f_ind_i(d.pop("PE_F_ind_I", UNSET))

        def _parse_pe_f_ind_j(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_j = _parse_pe_f_ind_j(d.pop("PE_F_ind_J", UNSET))

        def _parse_pe_f_ind_k(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_k = _parse_pe_f_ind_k(d.pop("PE_F_ind_K", UNSET))

        def _parse_pe_f_ind_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_l = _parse_pe_f_ind_l(d.pop("PE_F_ind_L", UNSET))

        def _parse_pe_f_ind_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_m = _parse_pe_f_ind_m(d.pop("PE_F_ind_M", UNSET))

        def _parse_pe_f_ind_m_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_m_n = _parse_pe_f_ind_m_n(d.pop("PE_F_ind_M_N", UNSET))

        def _parse_pe_f_ind_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_n = _parse_pe_f_ind_n(d.pop("PE_F_ind_N", UNSET))

        def _parse_pe_f_ind_p(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_p = _parse_pe_f_ind_p(d.pop("PE_F_ind_P", UNSET))

        def _parse_pe_f_ind_p_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_p_s = _parse_pe_f_ind_p_s(d.pop("PE_F_ind_P_S", UNSET))

        def _parse_pe_f_ind_q(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_q = _parse_pe_f_ind_q(d.pop("PE_F_ind_Q", UNSET))

        def _parse_pe_f_ind_r(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_r = _parse_pe_f_ind_r(d.pop("PE_F_ind_R", UNSET))

        def _parse_pe_f_ind_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_s = _parse_pe_f_ind_s(d.pop("PE_F_ind_S", UNSET))

        def _parse_pe_f_ind_site(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_f_ind_site = _parse_pe_f_ind_site(d.pop("PE_F_ind_Site", UNSET))

        def _parse_pe_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m = _parse_pe_m(d.pop("PE_M", UNSET))

        def _parse_pe_m_ind_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_m_ind_b = _parse_pe_m_ind_b(d.pop("PE_M_ind_B", UNSET))

        def _parse_pe_m_ind_b_d_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_m_ind_b_d_e = _parse_pe_m_ind_b_d_e(d.pop("PE_M_ind_B_D_E", UNSET))

        def _parse_pe_m_ind_c(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_c = _parse_pe_m_ind_c(d.pop("PE_M_ind_C", UNSET))

        def _parse_pe_m_ind_d(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_m_ind_d = _parse_pe_m_ind_d(d.pop("PE_M_ind_D", UNSET))

        def _parse_pe_m_ind_d_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_m_ind_d_e = _parse_pe_m_ind_d_e(d.pop("PE_M_ind_D_E", UNSET))

        def _parse_pe_m_ind_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pe_m_ind_e = _parse_pe_m_ind_e(d.pop("PE_M_ind_E", UNSET))

        def _parse_pe_m_ind_g(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_g = _parse_pe_m_ind_g(d.pop("PE_M_ind_G", UNSET))

        def _parse_pe_m_ind_g45_46(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_g45_46 = _parse_pe_m_ind_g45_46(d.pop("PE_M_ind_G45_46", UNSET))

        def _parse_pe_m_ind_g47(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_g47 = _parse_pe_m_ind_g47(d.pop("PE_M_ind_G47", UNSET))

        def _parse_pe_m_ind_h(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_h = _parse_pe_m_ind_h(d.pop("PE_M_ind_H", UNSET))

        def _parse_pe_m_ind_i(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_i = _parse_pe_m_ind_i(d.pop("PE_M_ind_I", UNSET))

        def _parse_pe_m_ind_j(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_j = _parse_pe_m_ind_j(d.pop("PE_M_ind_J", UNSET))

        def _parse_pe_m_ind_k(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_k = _parse_pe_m_ind_k(d.pop("PE_M_ind_K", UNSET))

        def _parse_pe_m_ind_l(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_l = _parse_pe_m_ind_l(d.pop("PE_M_ind_L", UNSET))

        def _parse_pe_m_ind_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_m = _parse_pe_m_ind_m(d.pop("PE_M_ind_M", UNSET))

        def _parse_pe_m_ind_m_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_m_n = _parse_pe_m_ind_m_n(d.pop("PE_M_ind_M_N", UNSET))

        def _parse_pe_m_ind_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_n = _parse_pe_m_ind_n(d.pop("PE_M_ind_N", UNSET))

        def _parse_pe_m_ind_p(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_p = _parse_pe_m_ind_p(d.pop("PE_M_ind_P", UNSET))

        def _parse_pe_m_ind_p_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_p_s = _parse_pe_m_ind_p_s(d.pop("PE_M_ind_P_S", UNSET))

        def _parse_pe_m_ind_q(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_q = _parse_pe_m_ind_q(d.pop("PE_M_ind_Q", UNSET))

        def _parse_pe_m_ind_r(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_r = _parse_pe_m_ind_r(d.pop("PE_M_ind_R", UNSET))

        def _parse_pe_m_ind_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_s = _parse_pe_m_ind_s(d.pop("PE_M_ind_S", UNSET))

        def _parse_pe_m_ind_site(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pe_m_ind_site = _parse_pe_m_ind_site(d.pop("PE_M_ind_Site", UNSET))

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

        pe_ind_site = _parse_pe_ind_site(d.pop("PE_ind_Site", UNSET))

        def _parse_yymm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yymm = _parse_yymm(d.pop("YYMM", UNSET))

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
            dc=dc,
            dc_chi=dc_chi,
            dc_class=dc_class,
            dc_eng=dc_eng,
            est=est,
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
            pe=pe,
            pe_f=pe_f,
            pe_f_ind_b=pe_f_ind_b,
            pe_f_ind_b_d_e=pe_f_ind_b_d_e,
            pe_f_ind_c=pe_f_ind_c,
            pe_f_ind_d=pe_f_ind_d,
            pe_f_ind_d_e=pe_f_ind_d_e,
            pe_f_ind_e=pe_f_ind_e,
            pe_f_ind_g=pe_f_ind_g,
            pe_f_ind_g45_46=pe_f_ind_g45_46,
            pe_f_ind_g47=pe_f_ind_g47,
            pe_f_ind_h=pe_f_ind_h,
            pe_f_ind_i=pe_f_ind_i,
            pe_f_ind_j=pe_f_ind_j,
            pe_f_ind_k=pe_f_ind_k,
            pe_f_ind_l=pe_f_ind_l,
            pe_f_ind_m=pe_f_ind_m,
            pe_f_ind_m_n=pe_f_ind_m_n,
            pe_f_ind_n=pe_f_ind_n,
            pe_f_ind_p=pe_f_ind_p,
            pe_f_ind_p_s=pe_f_ind_p_s,
            pe_f_ind_q=pe_f_ind_q,
            pe_f_ind_r=pe_f_ind_r,
            pe_f_ind_s=pe_f_ind_s,
            pe_f_ind_site=pe_f_ind_site,
            pe_m=pe_m,
            pe_m_ind_b=pe_m_ind_b,
            pe_m_ind_b_d_e=pe_m_ind_b_d_e,
            pe_m_ind_c=pe_m_ind_c,
            pe_m_ind_d=pe_m_ind_d,
            pe_m_ind_d_e=pe_m_ind_d_e,
            pe_m_ind_e=pe_m_ind_e,
            pe_m_ind_g=pe_m_ind_g,
            pe_m_ind_g45_46=pe_m_ind_g45_46,
            pe_m_ind_g47=pe_m_ind_g47,
            pe_m_ind_h=pe_m_ind_h,
            pe_m_ind_i=pe_m_ind_i,
            pe_m_ind_j=pe_m_ind_j,
            pe_m_ind_k=pe_m_ind_k,
            pe_m_ind_l=pe_m_ind_l,
            pe_m_ind_m=pe_m_ind_m,
            pe_m_ind_m_n=pe_m_ind_m_n,
            pe_m_ind_n=pe_m_ind_n,
            pe_m_ind_p=pe_m_ind_p,
            pe_m_ind_p_s=pe_m_ind_p_s,
            pe_m_ind_q=pe_m_ind_q,
            pe_m_ind_r=pe_m_ind_r,
            pe_m_ind_s=pe_m_ind_s,
            pe_m_ind_site=pe_m_ind_site,
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
            yymm=yymm,
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
