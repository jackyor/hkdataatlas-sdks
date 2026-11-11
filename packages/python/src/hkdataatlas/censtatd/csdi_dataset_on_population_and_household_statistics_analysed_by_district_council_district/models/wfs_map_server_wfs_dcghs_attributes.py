from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsDCGHSAttributes")


@_attrs_define
class WfsMapServerWfsDCGHSAttributes:
    """
    Attributes:
        adhz (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dc (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dc_chi (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dc_class (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dc_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dh_ea (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dh_ei (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dha_oth (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dha_othpctn (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dha_wf (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dha_wfpctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhi_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dhi_1pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhi_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dhi_2pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhi_3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dhi_3pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhi_e1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhi_e1pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhi_e2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhi_e2pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhi_e3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhi_e3pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dht_oo (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dht_oopctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dht_oth (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dht_othpctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        dht_st (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dht_stpctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhz_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dhz_1pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhz_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dhz_2pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhz_3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dhz_3pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhz_4 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dhz_4pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhz_5 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dhz_5_6 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhz_5_6pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        dhz_5pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        dhz_6 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        dhz_6pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp15_edu_age_1pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_age_2pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_age_3pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_age_4pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_age_5pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_age_6pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_age_7pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_age_8pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_deg (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_deg_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_deg_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_deg_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_deg_pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_deg_pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_lsed (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_lsed_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_lsed_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_lsed_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_lsed_pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_edu_lsed_pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_edu_ndeg (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_ndeg_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_ndeg_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_ndeg_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_ndeg_pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_edu_ndeg_pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_edu_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_prepri (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_prepri_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_prepri_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_prepri_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_edu_prepri_pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_edu_prepri_pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_edu_psec (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_psec_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_psec_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_psec_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_psec_pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_edu_psec_pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_edu_usec (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_usec_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_usec_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_usec_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_edu_usec_pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_edu_usec_pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp15_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp15_ms_divsep (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_divsep_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_divsep_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_divsep_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_divsep_pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_ms_divsep_pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        lbnp15_ms_ma (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_ma_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_ma_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_ma_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_ma_pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_ma_pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_nm (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_nm_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_nm_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_nm_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_nm_pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_nm_pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_win (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_win_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_win_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_win_pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_win_pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp15_ms_win_pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_act_eapctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_act_eipctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_act_ftstpctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_act_hmpctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_act_othpctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_age_1_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_1_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_1pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_1pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_1pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_age_2_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_2_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_2pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_2pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_2pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_age_3_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_3_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_3pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_3pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_3pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_4 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_age_4_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_4_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_4pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_4pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_4pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_5 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_age_5_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_5_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_5pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_5pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_5pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_6 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_age_6_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_6_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_6pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_6pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_6pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_7 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_age_7_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_7_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_7pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_7pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_7pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_8 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_age_8_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_8_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_8pctn (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_8pctn_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_age_8pctn_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_ea (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_ei (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_ftst (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_hm (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_ma_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_ma_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_ma_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_ma_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_ma_t (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_ma_t_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_odr (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_odr_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lbnp_oth (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_sr (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lbnp_sr_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_1_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_1_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_1_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_1_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_1_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_2_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_2_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_2_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_2_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_2_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_3_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_3_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_3_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_3_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_3_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_4 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_4_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_4_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_4_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_4_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_4_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_5 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_5_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_5_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_5_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_5_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_5_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_6 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_6_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_6_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_6_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_age_6_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_age_6_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        lf_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        lf_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_ma_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_ma_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_ma_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_ma_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_ma_t (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lf_ma_t_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lf_sr (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        lf_sr_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lfpr_age_1 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lfpr_age_1_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_1_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_1_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_1_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_1_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_2 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lfpr_age_2_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_2_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_2_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_2_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_2_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_3 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lfpr_age_3_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_3_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_3_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_3_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_3_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_4 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lfpr_age_4_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_4_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_4_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_4_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_4_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_5 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lfpr_age_5_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_5_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_5_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_5_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_5_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_6 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lfpr_age_6_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_6_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_6_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_6_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_age_6_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_f (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lfpr_f_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        lfpr_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lfpr_m_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        ma_econhh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        ma_econhh_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        ma_hh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        my_lp (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        t_lbnp (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        t_lbnp15 (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        t_lf (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        t_lf_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        t_lfpr (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        t_lfpr_xfdh (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        year (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    adhz: float | None | Unset = UNSET
    dc: float | None | Unset = UNSET
    dc_chi: None | str | Unset = UNSET
    dc_class: None | str | Unset = UNSET
    dc_eng: None | str | Unset = UNSET
    dh: float | None | Unset = UNSET
    dh_ea: float | None | Unset = UNSET
    dh_ei: float | None | Unset = UNSET
    dha_oth: None | str | Unset = UNSET
    dha_othpctn: None | str | Unset = UNSET
    dha_wf: float | None | Unset = UNSET
    dha_wfpctn: float | None | Unset = UNSET
    dhi_1: float | None | Unset = UNSET
    dhi_1pctn: float | None | Unset = UNSET
    dhi_2: float | None | Unset = UNSET
    dhi_2pctn: float | None | Unset = UNSET
    dhi_3: float | None | Unset = UNSET
    dhi_3pctn: float | None | Unset = UNSET
    dhi_e1: float | None | Unset = UNSET
    dhi_e1pctn: float | None | Unset = UNSET
    dhi_e2: float | None | Unset = UNSET
    dhi_e2pctn: float | None | Unset = UNSET
    dhi_e3: float | None | Unset = UNSET
    dhi_e3pctn: float | None | Unset = UNSET
    dht_oo: float | None | Unset = UNSET
    dht_oopctn: float | None | Unset = UNSET
    dht_oth: float | None | Unset = UNSET
    dht_othpctn: float | None | Unset = UNSET
    dht_st: float | None | Unset = UNSET
    dht_stpctn: float | None | Unset = UNSET
    dhz_1: float | None | Unset = UNSET
    dhz_1pctn: float | None | Unset = UNSET
    dhz_2: float | None | Unset = UNSET
    dhz_2pctn: float | None | Unset = UNSET
    dhz_3: float | None | Unset = UNSET
    dhz_3pctn: float | None | Unset = UNSET
    dhz_4: float | None | Unset = UNSET
    dhz_4pctn: float | None | Unset = UNSET
    dhz_5: float | None | Unset = UNSET
    dhz_5_6: float | None | Unset = UNSET
    dhz_5_6pctn: float | None | Unset = UNSET
    dhz_5pctn: float | None | Unset = UNSET
    dhz_6: float | None | Unset = UNSET
    dhz_6pctn: float | None | Unset = UNSET
    lbnp15_edu_age_1pctn: float | None | Unset = UNSET
    lbnp15_edu_age_2pctn: float | None | Unset = UNSET
    lbnp15_edu_age_3pctn: float | None | Unset = UNSET
    lbnp15_edu_age_4pctn: float | None | Unset = UNSET
    lbnp15_edu_age_5pctn: float | None | Unset = UNSET
    lbnp15_edu_age_6pctn: float | None | Unset = UNSET
    lbnp15_edu_age_7pctn: float | None | Unset = UNSET
    lbnp15_edu_age_8pctn: float | None | Unset = UNSET
    lbnp15_edu_deg: float | None | Unset = UNSET
    lbnp15_edu_deg_f: float | None | Unset = UNSET
    lbnp15_edu_deg_m: float | None | Unset = UNSET
    lbnp15_edu_deg_pctn: float | None | Unset = UNSET
    lbnp15_edu_deg_pctn_f: float | None | Unset = UNSET
    lbnp15_edu_deg_pctn_m: float | None | Unset = UNSET
    lbnp15_edu_lsed: float | None | Unset = UNSET
    lbnp15_edu_lsed_f: float | None | Unset = UNSET
    lbnp15_edu_lsed_m: float | None | Unset = UNSET
    lbnp15_edu_lsed_pctn: float | None | Unset = UNSET
    lbnp15_edu_lsed_pctn_f: float | None | Unset = UNSET
    lbnp15_edu_lsed_pctn_m: float | None | Unset = UNSET
    lbnp15_edu_ndeg: float | None | Unset = UNSET
    lbnp15_edu_ndeg_f: float | None | Unset = UNSET
    lbnp15_edu_ndeg_m: float | None | Unset = UNSET
    lbnp15_edu_ndeg_pctn: float | None | Unset = UNSET
    lbnp15_edu_ndeg_pctn_f: float | None | Unset = UNSET
    lbnp15_edu_ndeg_pctn_m: float | None | Unset = UNSET
    lbnp15_edu_pctn: float | None | Unset = UNSET
    lbnp15_edu_prepri: float | None | Unset = UNSET
    lbnp15_edu_prepri_f: float | None | Unset = UNSET
    lbnp15_edu_prepri_m: float | None | Unset = UNSET
    lbnp15_edu_prepri_pctn: float | None | Unset = UNSET
    lbnp15_edu_prepri_pctn_f: float | None | Unset = UNSET
    lbnp15_edu_prepri_pctn_m: float | None | Unset = UNSET
    lbnp15_edu_psec: float | None | Unset = UNSET
    lbnp15_edu_psec_f: float | None | Unset = UNSET
    lbnp15_edu_psec_m: float | None | Unset = UNSET
    lbnp15_edu_psec_pctn: float | None | Unset = UNSET
    lbnp15_edu_psec_pctn_f: float | None | Unset = UNSET
    lbnp15_edu_psec_pctn_m: float | None | Unset = UNSET
    lbnp15_edu_usec: float | None | Unset = UNSET
    lbnp15_edu_usec_f: float | None | Unset = UNSET
    lbnp15_edu_usec_m: float | None | Unset = UNSET
    lbnp15_edu_usec_pctn: float | None | Unset = UNSET
    lbnp15_edu_usec_pctn_f: float | None | Unset = UNSET
    lbnp15_edu_usec_pctn_m: float | None | Unset = UNSET
    lbnp15_f: float | None | Unset = UNSET
    lbnp15_m: float | None | Unset = UNSET
    lbnp15_ms_divsep: float | None | Unset = UNSET
    lbnp15_ms_divsep_f: float | None | Unset = UNSET
    lbnp15_ms_divsep_m: float | None | Unset = UNSET
    lbnp15_ms_divsep_pctn: float | None | Unset = UNSET
    lbnp15_ms_divsep_pctn_f: float | None | Unset = UNSET
    lbnp15_ms_divsep_pctn_m: float | None | Unset = UNSET
    lbnp15_ms_ma: float | None | Unset = UNSET
    lbnp15_ms_ma_f: float | None | Unset = UNSET
    lbnp15_ms_ma_m: float | None | Unset = UNSET
    lbnp15_ms_ma_pctn: float | None | Unset = UNSET
    lbnp15_ms_ma_pctn_f: float | None | Unset = UNSET
    lbnp15_ms_ma_pctn_m: float | None | Unset = UNSET
    lbnp15_ms_nm: float | None | Unset = UNSET
    lbnp15_ms_nm_f: float | None | Unset = UNSET
    lbnp15_ms_nm_m: float | None | Unset = UNSET
    lbnp15_ms_nm_pctn: float | None | Unset = UNSET
    lbnp15_ms_nm_pctn_f: float | None | Unset = UNSET
    lbnp15_ms_nm_pctn_m: float | None | Unset = UNSET
    lbnp15_ms_win: float | None | Unset = UNSET
    lbnp15_ms_win_f: float | None | Unset = UNSET
    lbnp15_ms_win_m: float | None | Unset = UNSET
    lbnp15_ms_win_pctn: float | None | Unset = UNSET
    lbnp15_ms_win_pctn_f: float | None | Unset = UNSET
    lbnp15_ms_win_pctn_m: float | None | Unset = UNSET
    lbnp_act_eapctn: float | None | Unset = UNSET
    lbnp_act_eipctn: float | None | Unset = UNSET
    lbnp_act_ftstpctn: float | None | Unset = UNSET
    lbnp_act_hmpctn: float | None | Unset = UNSET
    lbnp_act_othpctn: float | None | Unset = UNSET
    lbnp_age_1: float | None | Unset = UNSET
    lbnp_age_1_f: float | None | Unset = UNSET
    lbnp_age_1_m: float | None | Unset = UNSET
    lbnp_age_1pctn: float | None | Unset = UNSET
    lbnp_age_1pctn_f: float | None | Unset = UNSET
    lbnp_age_1pctn_m: float | None | Unset = UNSET
    lbnp_age_2: float | None | Unset = UNSET
    lbnp_age_2_f: float | None | Unset = UNSET
    lbnp_age_2_m: float | None | Unset = UNSET
    lbnp_age_2pctn: float | None | Unset = UNSET
    lbnp_age_2pctn_f: float | None | Unset = UNSET
    lbnp_age_2pctn_m: float | None | Unset = UNSET
    lbnp_age_3: float | None | Unset = UNSET
    lbnp_age_3_f: float | None | Unset = UNSET
    lbnp_age_3_m: float | None | Unset = UNSET
    lbnp_age_3pctn: float | None | Unset = UNSET
    lbnp_age_3pctn_f: float | None | Unset = UNSET
    lbnp_age_3pctn_m: float | None | Unset = UNSET
    lbnp_age_4: float | None | Unset = UNSET
    lbnp_age_4_f: float | None | Unset = UNSET
    lbnp_age_4_m: float | None | Unset = UNSET
    lbnp_age_4pctn: float | None | Unset = UNSET
    lbnp_age_4pctn_f: float | None | Unset = UNSET
    lbnp_age_4pctn_m: float | None | Unset = UNSET
    lbnp_age_5: float | None | Unset = UNSET
    lbnp_age_5_f: float | None | Unset = UNSET
    lbnp_age_5_m: float | None | Unset = UNSET
    lbnp_age_5pctn: float | None | Unset = UNSET
    lbnp_age_5pctn_f: float | None | Unset = UNSET
    lbnp_age_5pctn_m: float | None | Unset = UNSET
    lbnp_age_6: float | None | Unset = UNSET
    lbnp_age_6_f: float | None | Unset = UNSET
    lbnp_age_6_m: float | None | Unset = UNSET
    lbnp_age_6pctn: float | None | Unset = UNSET
    lbnp_age_6pctn_f: float | None | Unset = UNSET
    lbnp_age_6pctn_m: float | None | Unset = UNSET
    lbnp_age_7: float | None | Unset = UNSET
    lbnp_age_7_f: float | None | Unset = UNSET
    lbnp_age_7_m: float | None | Unset = UNSET
    lbnp_age_7pctn: float | None | Unset = UNSET
    lbnp_age_7pctn_f: float | None | Unset = UNSET
    lbnp_age_7pctn_m: float | None | Unset = UNSET
    lbnp_age_8: float | None | Unset = UNSET
    lbnp_age_8_f: float | None | Unset = UNSET
    lbnp_age_8_m: float | None | Unset = UNSET
    lbnp_age_8pctn: float | None | Unset = UNSET
    lbnp_age_8pctn_f: float | None | Unset = UNSET
    lbnp_age_8pctn_m: float | None | Unset = UNSET
    lbnp_ea: float | None | Unset = UNSET
    lbnp_ei: float | None | Unset = UNSET
    lbnp_f: float | None | Unset = UNSET
    lbnp_ftst: float | None | Unset = UNSET
    lbnp_hm: float | None | Unset = UNSET
    lbnp_m: float | None | Unset = UNSET
    lbnp_ma_f: float | None | Unset = UNSET
    lbnp_ma_f_xfdh: float | None | Unset = UNSET
    lbnp_ma_m: float | None | Unset = UNSET
    lbnp_ma_m_xfdh: float | None | Unset = UNSET
    lbnp_ma_t: float | None | Unset = UNSET
    lbnp_ma_t_xfdh: float | None | Unset = UNSET
    lbnp_odr: float | None | Unset = UNSET
    lbnp_odr_xfdh: float | None | Unset = UNSET
    lbnp_oth: float | None | Unset = UNSET
    lbnp_sr: float | None | Unset = UNSET
    lbnp_sr_xfdh: float | None | Unset = UNSET
    lf_age_1: float | None | Unset = UNSET
    lf_age_1_f: float | None | Unset = UNSET
    lf_age_1_f_xfdh: float | None | Unset = UNSET
    lf_age_1_m: float | None | Unset = UNSET
    lf_age_1_m_xfdh: float | None | Unset = UNSET
    lf_age_1_xfdh: float | None | Unset = UNSET
    lf_age_2: float | None | Unset = UNSET
    lf_age_2_f: float | None | Unset = UNSET
    lf_age_2_f_xfdh: float | None | Unset = UNSET
    lf_age_2_m: float | None | Unset = UNSET
    lf_age_2_m_xfdh: float | None | Unset = UNSET
    lf_age_2_xfdh: float | None | Unset = UNSET
    lf_age_3: float | None | Unset = UNSET
    lf_age_3_f: float | None | Unset = UNSET
    lf_age_3_f_xfdh: float | None | Unset = UNSET
    lf_age_3_m: float | None | Unset = UNSET
    lf_age_3_m_xfdh: float | None | Unset = UNSET
    lf_age_3_xfdh: float | None | Unset = UNSET
    lf_age_4: float | None | Unset = UNSET
    lf_age_4_f: float | None | Unset = UNSET
    lf_age_4_f_xfdh: float | None | Unset = UNSET
    lf_age_4_m: float | None | Unset = UNSET
    lf_age_4_m_xfdh: float | None | Unset = UNSET
    lf_age_4_xfdh: float | None | Unset = UNSET
    lf_age_5: float | None | Unset = UNSET
    lf_age_5_f: float | None | Unset = UNSET
    lf_age_5_f_xfdh: float | None | Unset = UNSET
    lf_age_5_m: float | None | Unset = UNSET
    lf_age_5_m_xfdh: float | None | Unset = UNSET
    lf_age_5_xfdh: float | None | Unset = UNSET
    lf_age_6: float | None | Unset = UNSET
    lf_age_6_f: float | None | Unset = UNSET
    lf_age_6_f_xfdh: float | None | Unset = UNSET
    lf_age_6_m: float | None | Unset = UNSET
    lf_age_6_m_xfdh: float | None | Unset = UNSET
    lf_age_6_xfdh: float | None | Unset = UNSET
    lf_f: float | None | Unset = UNSET
    lf_f_xfdh: float | None | Unset = UNSET
    lf_m: float | None | Unset = UNSET
    lf_m_xfdh: float | None | Unset = UNSET
    lf_ma_f: float | None | Unset = UNSET
    lf_ma_f_xfdh: float | None | Unset = UNSET
    lf_ma_m: float | None | Unset = UNSET
    lf_ma_m_xfdh: float | None | Unset = UNSET
    lf_ma_t: float | None | Unset = UNSET
    lf_ma_t_xfdh: float | None | Unset = UNSET
    lf_sr: float | None | Unset = UNSET
    lf_sr_xfdh: float | None | Unset = UNSET
    lfpr_age_1: float | None | Unset = UNSET
    lfpr_age_1_f: float | None | Unset = UNSET
    lfpr_age_1_f_xfdh: float | None | Unset = UNSET
    lfpr_age_1_m: float | None | Unset = UNSET
    lfpr_age_1_m_xfdh: float | None | Unset = UNSET
    lfpr_age_1_xfdh: float | None | Unset = UNSET
    lfpr_age_2: float | None | Unset = UNSET
    lfpr_age_2_f: float | None | Unset = UNSET
    lfpr_age_2_f_xfdh: float | None | Unset = UNSET
    lfpr_age_2_m: float | None | Unset = UNSET
    lfpr_age_2_m_xfdh: float | None | Unset = UNSET
    lfpr_age_2_xfdh: float | None | Unset = UNSET
    lfpr_age_3: float | None | Unset = UNSET
    lfpr_age_3_f: float | None | Unset = UNSET
    lfpr_age_3_f_xfdh: float | None | Unset = UNSET
    lfpr_age_3_m: float | None | Unset = UNSET
    lfpr_age_3_m_xfdh: float | None | Unset = UNSET
    lfpr_age_3_xfdh: float | None | Unset = UNSET
    lfpr_age_4: float | None | Unset = UNSET
    lfpr_age_4_f: float | None | Unset = UNSET
    lfpr_age_4_f_xfdh: float | None | Unset = UNSET
    lfpr_age_4_m: float | None | Unset = UNSET
    lfpr_age_4_m_xfdh: float | None | Unset = UNSET
    lfpr_age_4_xfdh: float | None | Unset = UNSET
    lfpr_age_5: float | None | Unset = UNSET
    lfpr_age_5_f: float | None | Unset = UNSET
    lfpr_age_5_f_xfdh: float | None | Unset = UNSET
    lfpr_age_5_m: float | None | Unset = UNSET
    lfpr_age_5_m_xfdh: float | None | Unset = UNSET
    lfpr_age_5_xfdh: float | None | Unset = UNSET
    lfpr_age_6: float | None | Unset = UNSET
    lfpr_age_6_f: float | None | Unset = UNSET
    lfpr_age_6_f_xfdh: float | None | Unset = UNSET
    lfpr_age_6_m: float | None | Unset = UNSET
    lfpr_age_6_m_xfdh: float | None | Unset = UNSET
    lfpr_age_6_xfdh: float | None | Unset = UNSET
    lfpr_f: float | None | Unset = UNSET
    lfpr_f_xfdh: float | None | Unset = UNSET
    lfpr_m: float | None | Unset = UNSET
    lfpr_m_xfdh: float | None | Unset = UNSET
    ma_econhh: float | None | Unset = UNSET
    ma_econhh_xfdh: float | None | Unset = UNSET
    ma_hh: float | None | Unset = UNSET
    my_lp: float | None | Unset = UNSET
    t_lbnp: float | None | Unset = UNSET
    t_lbnp15: float | None | Unset = UNSET
    t_lf: float | None | Unset = UNSET
    t_lf_xfdh: float | None | Unset = UNSET
    t_lfpr: float | None | Unset = UNSET
    t_lfpr_xfdh: float | None | Unset = UNSET
    year: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adhz: float | None | Unset
        if isinstance(self.adhz, Unset):
            adhz = UNSET
        else:
            adhz = self.adhz

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

        dh_ea: float | None | Unset
        if isinstance(self.dh_ea, Unset):
            dh_ea = UNSET
        else:
            dh_ea = self.dh_ea

        dh_ei: float | None | Unset
        if isinstance(self.dh_ei, Unset):
            dh_ei = UNSET
        else:
            dh_ei = self.dh_ei

        dha_oth: None | str | Unset
        if isinstance(self.dha_oth, Unset):
            dha_oth = UNSET
        else:
            dha_oth = self.dha_oth

        dha_othpctn: None | str | Unset
        if isinstance(self.dha_othpctn, Unset):
            dha_othpctn = UNSET
        else:
            dha_othpctn = self.dha_othpctn

        dha_wf: float | None | Unset
        if isinstance(self.dha_wf, Unset):
            dha_wf = UNSET
        else:
            dha_wf = self.dha_wf

        dha_wfpctn: float | None | Unset
        if isinstance(self.dha_wfpctn, Unset):
            dha_wfpctn = UNSET
        else:
            dha_wfpctn = self.dha_wfpctn

        dhi_1: float | None | Unset
        if isinstance(self.dhi_1, Unset):
            dhi_1 = UNSET
        else:
            dhi_1 = self.dhi_1

        dhi_1pctn: float | None | Unset
        if isinstance(self.dhi_1pctn, Unset):
            dhi_1pctn = UNSET
        else:
            dhi_1pctn = self.dhi_1pctn

        dhi_2: float | None | Unset
        if isinstance(self.dhi_2, Unset):
            dhi_2 = UNSET
        else:
            dhi_2 = self.dhi_2

        dhi_2pctn: float | None | Unset
        if isinstance(self.dhi_2pctn, Unset):
            dhi_2pctn = UNSET
        else:
            dhi_2pctn = self.dhi_2pctn

        dhi_3: float | None | Unset
        if isinstance(self.dhi_3, Unset):
            dhi_3 = UNSET
        else:
            dhi_3 = self.dhi_3

        dhi_3pctn: float | None | Unset
        if isinstance(self.dhi_3pctn, Unset):
            dhi_3pctn = UNSET
        else:
            dhi_3pctn = self.dhi_3pctn

        dhi_e1: float | None | Unset
        if isinstance(self.dhi_e1, Unset):
            dhi_e1 = UNSET
        else:
            dhi_e1 = self.dhi_e1

        dhi_e1pctn: float | None | Unset
        if isinstance(self.dhi_e1pctn, Unset):
            dhi_e1pctn = UNSET
        else:
            dhi_e1pctn = self.dhi_e1pctn

        dhi_e2: float | None | Unset
        if isinstance(self.dhi_e2, Unset):
            dhi_e2 = UNSET
        else:
            dhi_e2 = self.dhi_e2

        dhi_e2pctn: float | None | Unset
        if isinstance(self.dhi_e2pctn, Unset):
            dhi_e2pctn = UNSET
        else:
            dhi_e2pctn = self.dhi_e2pctn

        dhi_e3: float | None | Unset
        if isinstance(self.dhi_e3, Unset):
            dhi_e3 = UNSET
        else:
            dhi_e3 = self.dhi_e3

        dhi_e3pctn: float | None | Unset
        if isinstance(self.dhi_e3pctn, Unset):
            dhi_e3pctn = UNSET
        else:
            dhi_e3pctn = self.dhi_e3pctn

        dht_oo: float | None | Unset
        if isinstance(self.dht_oo, Unset):
            dht_oo = UNSET
        else:
            dht_oo = self.dht_oo

        dht_oopctn: float | None | Unset
        if isinstance(self.dht_oopctn, Unset):
            dht_oopctn = UNSET
        else:
            dht_oopctn = self.dht_oopctn

        dht_oth: float | None | Unset
        if isinstance(self.dht_oth, Unset):
            dht_oth = UNSET
        else:
            dht_oth = self.dht_oth

        dht_othpctn: float | None | Unset
        if isinstance(self.dht_othpctn, Unset):
            dht_othpctn = UNSET
        else:
            dht_othpctn = self.dht_othpctn

        dht_st: float | None | Unset
        if isinstance(self.dht_st, Unset):
            dht_st = UNSET
        else:
            dht_st = self.dht_st

        dht_stpctn: float | None | Unset
        if isinstance(self.dht_stpctn, Unset):
            dht_stpctn = UNSET
        else:
            dht_stpctn = self.dht_stpctn

        dhz_1: float | None | Unset
        if isinstance(self.dhz_1, Unset):
            dhz_1 = UNSET
        else:
            dhz_1 = self.dhz_1

        dhz_1pctn: float | None | Unset
        if isinstance(self.dhz_1pctn, Unset):
            dhz_1pctn = UNSET
        else:
            dhz_1pctn = self.dhz_1pctn

        dhz_2: float | None | Unset
        if isinstance(self.dhz_2, Unset):
            dhz_2 = UNSET
        else:
            dhz_2 = self.dhz_2

        dhz_2pctn: float | None | Unset
        if isinstance(self.dhz_2pctn, Unset):
            dhz_2pctn = UNSET
        else:
            dhz_2pctn = self.dhz_2pctn

        dhz_3: float | None | Unset
        if isinstance(self.dhz_3, Unset):
            dhz_3 = UNSET
        else:
            dhz_3 = self.dhz_3

        dhz_3pctn: float | None | Unset
        if isinstance(self.dhz_3pctn, Unset):
            dhz_3pctn = UNSET
        else:
            dhz_3pctn = self.dhz_3pctn

        dhz_4: float | None | Unset
        if isinstance(self.dhz_4, Unset):
            dhz_4 = UNSET
        else:
            dhz_4 = self.dhz_4

        dhz_4pctn: float | None | Unset
        if isinstance(self.dhz_4pctn, Unset):
            dhz_4pctn = UNSET
        else:
            dhz_4pctn = self.dhz_4pctn

        dhz_5: float | None | Unset
        if isinstance(self.dhz_5, Unset):
            dhz_5 = UNSET
        else:
            dhz_5 = self.dhz_5

        dhz_5_6: float | None | Unset
        if isinstance(self.dhz_5_6, Unset):
            dhz_5_6 = UNSET
        else:
            dhz_5_6 = self.dhz_5_6

        dhz_5_6pctn: float | None | Unset
        if isinstance(self.dhz_5_6pctn, Unset):
            dhz_5_6pctn = UNSET
        else:
            dhz_5_6pctn = self.dhz_5_6pctn

        dhz_5pctn: float | None | Unset
        if isinstance(self.dhz_5pctn, Unset):
            dhz_5pctn = UNSET
        else:
            dhz_5pctn = self.dhz_5pctn

        dhz_6: float | None | Unset
        if isinstance(self.dhz_6, Unset):
            dhz_6 = UNSET
        else:
            dhz_6 = self.dhz_6

        dhz_6pctn: float | None | Unset
        if isinstance(self.dhz_6pctn, Unset):
            dhz_6pctn = UNSET
        else:
            dhz_6pctn = self.dhz_6pctn

        lbnp15_edu_age_1pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_age_1pctn, Unset):
            lbnp15_edu_age_1pctn = UNSET
        else:
            lbnp15_edu_age_1pctn = self.lbnp15_edu_age_1pctn

        lbnp15_edu_age_2pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_age_2pctn, Unset):
            lbnp15_edu_age_2pctn = UNSET
        else:
            lbnp15_edu_age_2pctn = self.lbnp15_edu_age_2pctn

        lbnp15_edu_age_3pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_age_3pctn, Unset):
            lbnp15_edu_age_3pctn = UNSET
        else:
            lbnp15_edu_age_3pctn = self.lbnp15_edu_age_3pctn

        lbnp15_edu_age_4pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_age_4pctn, Unset):
            lbnp15_edu_age_4pctn = UNSET
        else:
            lbnp15_edu_age_4pctn = self.lbnp15_edu_age_4pctn

        lbnp15_edu_age_5pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_age_5pctn, Unset):
            lbnp15_edu_age_5pctn = UNSET
        else:
            lbnp15_edu_age_5pctn = self.lbnp15_edu_age_5pctn

        lbnp15_edu_age_6pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_age_6pctn, Unset):
            lbnp15_edu_age_6pctn = UNSET
        else:
            lbnp15_edu_age_6pctn = self.lbnp15_edu_age_6pctn

        lbnp15_edu_age_7pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_age_7pctn, Unset):
            lbnp15_edu_age_7pctn = UNSET
        else:
            lbnp15_edu_age_7pctn = self.lbnp15_edu_age_7pctn

        lbnp15_edu_age_8pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_age_8pctn, Unset):
            lbnp15_edu_age_8pctn = UNSET
        else:
            lbnp15_edu_age_8pctn = self.lbnp15_edu_age_8pctn

        lbnp15_edu_deg: float | None | Unset
        if isinstance(self.lbnp15_edu_deg, Unset):
            lbnp15_edu_deg = UNSET
        else:
            lbnp15_edu_deg = self.lbnp15_edu_deg

        lbnp15_edu_deg_f: float | None | Unset
        if isinstance(self.lbnp15_edu_deg_f, Unset):
            lbnp15_edu_deg_f = UNSET
        else:
            lbnp15_edu_deg_f = self.lbnp15_edu_deg_f

        lbnp15_edu_deg_m: float | None | Unset
        if isinstance(self.lbnp15_edu_deg_m, Unset):
            lbnp15_edu_deg_m = UNSET
        else:
            lbnp15_edu_deg_m = self.lbnp15_edu_deg_m

        lbnp15_edu_deg_pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_deg_pctn, Unset):
            lbnp15_edu_deg_pctn = UNSET
        else:
            lbnp15_edu_deg_pctn = self.lbnp15_edu_deg_pctn

        lbnp15_edu_deg_pctn_f: float | None | Unset
        if isinstance(self.lbnp15_edu_deg_pctn_f, Unset):
            lbnp15_edu_deg_pctn_f = UNSET
        else:
            lbnp15_edu_deg_pctn_f = self.lbnp15_edu_deg_pctn_f

        lbnp15_edu_deg_pctn_m: float | None | Unset
        if isinstance(self.lbnp15_edu_deg_pctn_m, Unset):
            lbnp15_edu_deg_pctn_m = UNSET
        else:
            lbnp15_edu_deg_pctn_m = self.lbnp15_edu_deg_pctn_m

        lbnp15_edu_lsed: float | None | Unset
        if isinstance(self.lbnp15_edu_lsed, Unset):
            lbnp15_edu_lsed = UNSET
        else:
            lbnp15_edu_lsed = self.lbnp15_edu_lsed

        lbnp15_edu_lsed_f: float | None | Unset
        if isinstance(self.lbnp15_edu_lsed_f, Unset):
            lbnp15_edu_lsed_f = UNSET
        else:
            lbnp15_edu_lsed_f = self.lbnp15_edu_lsed_f

        lbnp15_edu_lsed_m: float | None | Unset
        if isinstance(self.lbnp15_edu_lsed_m, Unset):
            lbnp15_edu_lsed_m = UNSET
        else:
            lbnp15_edu_lsed_m = self.lbnp15_edu_lsed_m

        lbnp15_edu_lsed_pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_lsed_pctn, Unset):
            lbnp15_edu_lsed_pctn = UNSET
        else:
            lbnp15_edu_lsed_pctn = self.lbnp15_edu_lsed_pctn

        lbnp15_edu_lsed_pctn_f: float | None | Unset
        if isinstance(self.lbnp15_edu_lsed_pctn_f, Unset):
            lbnp15_edu_lsed_pctn_f = UNSET
        else:
            lbnp15_edu_lsed_pctn_f = self.lbnp15_edu_lsed_pctn_f

        lbnp15_edu_lsed_pctn_m: float | None | Unset
        if isinstance(self.lbnp15_edu_lsed_pctn_m, Unset):
            lbnp15_edu_lsed_pctn_m = UNSET
        else:
            lbnp15_edu_lsed_pctn_m = self.lbnp15_edu_lsed_pctn_m

        lbnp15_edu_ndeg: float | None | Unset
        if isinstance(self.lbnp15_edu_ndeg, Unset):
            lbnp15_edu_ndeg = UNSET
        else:
            lbnp15_edu_ndeg = self.lbnp15_edu_ndeg

        lbnp15_edu_ndeg_f: float | None | Unset
        if isinstance(self.lbnp15_edu_ndeg_f, Unset):
            lbnp15_edu_ndeg_f = UNSET
        else:
            lbnp15_edu_ndeg_f = self.lbnp15_edu_ndeg_f

        lbnp15_edu_ndeg_m: float | None | Unset
        if isinstance(self.lbnp15_edu_ndeg_m, Unset):
            lbnp15_edu_ndeg_m = UNSET
        else:
            lbnp15_edu_ndeg_m = self.lbnp15_edu_ndeg_m

        lbnp15_edu_ndeg_pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_ndeg_pctn, Unset):
            lbnp15_edu_ndeg_pctn = UNSET
        else:
            lbnp15_edu_ndeg_pctn = self.lbnp15_edu_ndeg_pctn

        lbnp15_edu_ndeg_pctn_f: float | None | Unset
        if isinstance(self.lbnp15_edu_ndeg_pctn_f, Unset):
            lbnp15_edu_ndeg_pctn_f = UNSET
        else:
            lbnp15_edu_ndeg_pctn_f = self.lbnp15_edu_ndeg_pctn_f

        lbnp15_edu_ndeg_pctn_m: float | None | Unset
        if isinstance(self.lbnp15_edu_ndeg_pctn_m, Unset):
            lbnp15_edu_ndeg_pctn_m = UNSET
        else:
            lbnp15_edu_ndeg_pctn_m = self.lbnp15_edu_ndeg_pctn_m

        lbnp15_edu_pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_pctn, Unset):
            lbnp15_edu_pctn = UNSET
        else:
            lbnp15_edu_pctn = self.lbnp15_edu_pctn

        lbnp15_edu_prepri: float | None | Unset
        if isinstance(self.lbnp15_edu_prepri, Unset):
            lbnp15_edu_prepri = UNSET
        else:
            lbnp15_edu_prepri = self.lbnp15_edu_prepri

        lbnp15_edu_prepri_f: float | None | Unset
        if isinstance(self.lbnp15_edu_prepri_f, Unset):
            lbnp15_edu_prepri_f = UNSET
        else:
            lbnp15_edu_prepri_f = self.lbnp15_edu_prepri_f

        lbnp15_edu_prepri_m: float | None | Unset
        if isinstance(self.lbnp15_edu_prepri_m, Unset):
            lbnp15_edu_prepri_m = UNSET
        else:
            lbnp15_edu_prepri_m = self.lbnp15_edu_prepri_m

        lbnp15_edu_prepri_pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_prepri_pctn, Unset):
            lbnp15_edu_prepri_pctn = UNSET
        else:
            lbnp15_edu_prepri_pctn = self.lbnp15_edu_prepri_pctn

        lbnp15_edu_prepri_pctn_f: float | None | Unset
        if isinstance(self.lbnp15_edu_prepri_pctn_f, Unset):
            lbnp15_edu_prepri_pctn_f = UNSET
        else:
            lbnp15_edu_prepri_pctn_f = self.lbnp15_edu_prepri_pctn_f

        lbnp15_edu_prepri_pctn_m: float | None | Unset
        if isinstance(self.lbnp15_edu_prepri_pctn_m, Unset):
            lbnp15_edu_prepri_pctn_m = UNSET
        else:
            lbnp15_edu_prepri_pctn_m = self.lbnp15_edu_prepri_pctn_m

        lbnp15_edu_psec: float | None | Unset
        if isinstance(self.lbnp15_edu_psec, Unset):
            lbnp15_edu_psec = UNSET
        else:
            lbnp15_edu_psec = self.lbnp15_edu_psec

        lbnp15_edu_psec_f: float | None | Unset
        if isinstance(self.lbnp15_edu_psec_f, Unset):
            lbnp15_edu_psec_f = UNSET
        else:
            lbnp15_edu_psec_f = self.lbnp15_edu_psec_f

        lbnp15_edu_psec_m: float | None | Unset
        if isinstance(self.lbnp15_edu_psec_m, Unset):
            lbnp15_edu_psec_m = UNSET
        else:
            lbnp15_edu_psec_m = self.lbnp15_edu_psec_m

        lbnp15_edu_psec_pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_psec_pctn, Unset):
            lbnp15_edu_psec_pctn = UNSET
        else:
            lbnp15_edu_psec_pctn = self.lbnp15_edu_psec_pctn

        lbnp15_edu_psec_pctn_f: float | None | Unset
        if isinstance(self.lbnp15_edu_psec_pctn_f, Unset):
            lbnp15_edu_psec_pctn_f = UNSET
        else:
            lbnp15_edu_psec_pctn_f = self.lbnp15_edu_psec_pctn_f

        lbnp15_edu_psec_pctn_m: float | None | Unset
        if isinstance(self.lbnp15_edu_psec_pctn_m, Unset):
            lbnp15_edu_psec_pctn_m = UNSET
        else:
            lbnp15_edu_psec_pctn_m = self.lbnp15_edu_psec_pctn_m

        lbnp15_edu_usec: float | None | Unset
        if isinstance(self.lbnp15_edu_usec, Unset):
            lbnp15_edu_usec = UNSET
        else:
            lbnp15_edu_usec = self.lbnp15_edu_usec

        lbnp15_edu_usec_f: float | None | Unset
        if isinstance(self.lbnp15_edu_usec_f, Unset):
            lbnp15_edu_usec_f = UNSET
        else:
            lbnp15_edu_usec_f = self.lbnp15_edu_usec_f

        lbnp15_edu_usec_m: float | None | Unset
        if isinstance(self.lbnp15_edu_usec_m, Unset):
            lbnp15_edu_usec_m = UNSET
        else:
            lbnp15_edu_usec_m = self.lbnp15_edu_usec_m

        lbnp15_edu_usec_pctn: float | None | Unset
        if isinstance(self.lbnp15_edu_usec_pctn, Unset):
            lbnp15_edu_usec_pctn = UNSET
        else:
            lbnp15_edu_usec_pctn = self.lbnp15_edu_usec_pctn

        lbnp15_edu_usec_pctn_f: float | None | Unset
        if isinstance(self.lbnp15_edu_usec_pctn_f, Unset):
            lbnp15_edu_usec_pctn_f = UNSET
        else:
            lbnp15_edu_usec_pctn_f = self.lbnp15_edu_usec_pctn_f

        lbnp15_edu_usec_pctn_m: float | None | Unset
        if isinstance(self.lbnp15_edu_usec_pctn_m, Unset):
            lbnp15_edu_usec_pctn_m = UNSET
        else:
            lbnp15_edu_usec_pctn_m = self.lbnp15_edu_usec_pctn_m

        lbnp15_f: float | None | Unset
        if isinstance(self.lbnp15_f, Unset):
            lbnp15_f = UNSET
        else:
            lbnp15_f = self.lbnp15_f

        lbnp15_m: float | None | Unset
        if isinstance(self.lbnp15_m, Unset):
            lbnp15_m = UNSET
        else:
            lbnp15_m = self.lbnp15_m

        lbnp15_ms_divsep: float | None | Unset
        if isinstance(self.lbnp15_ms_divsep, Unset):
            lbnp15_ms_divsep = UNSET
        else:
            lbnp15_ms_divsep = self.lbnp15_ms_divsep

        lbnp15_ms_divsep_f: float | None | Unset
        if isinstance(self.lbnp15_ms_divsep_f, Unset):
            lbnp15_ms_divsep_f = UNSET
        else:
            lbnp15_ms_divsep_f = self.lbnp15_ms_divsep_f

        lbnp15_ms_divsep_m: float | None | Unset
        if isinstance(self.lbnp15_ms_divsep_m, Unset):
            lbnp15_ms_divsep_m = UNSET
        else:
            lbnp15_ms_divsep_m = self.lbnp15_ms_divsep_m

        lbnp15_ms_divsep_pctn: float | None | Unset
        if isinstance(self.lbnp15_ms_divsep_pctn, Unset):
            lbnp15_ms_divsep_pctn = UNSET
        else:
            lbnp15_ms_divsep_pctn = self.lbnp15_ms_divsep_pctn

        lbnp15_ms_divsep_pctn_f: float | None | Unset
        if isinstance(self.lbnp15_ms_divsep_pctn_f, Unset):
            lbnp15_ms_divsep_pctn_f = UNSET
        else:
            lbnp15_ms_divsep_pctn_f = self.lbnp15_ms_divsep_pctn_f

        lbnp15_ms_divsep_pctn_m: float | None | Unset
        if isinstance(self.lbnp15_ms_divsep_pctn_m, Unset):
            lbnp15_ms_divsep_pctn_m = UNSET
        else:
            lbnp15_ms_divsep_pctn_m = self.lbnp15_ms_divsep_pctn_m

        lbnp15_ms_ma: float | None | Unset
        if isinstance(self.lbnp15_ms_ma, Unset):
            lbnp15_ms_ma = UNSET
        else:
            lbnp15_ms_ma = self.lbnp15_ms_ma

        lbnp15_ms_ma_f: float | None | Unset
        if isinstance(self.lbnp15_ms_ma_f, Unset):
            lbnp15_ms_ma_f = UNSET
        else:
            lbnp15_ms_ma_f = self.lbnp15_ms_ma_f

        lbnp15_ms_ma_m: float | None | Unset
        if isinstance(self.lbnp15_ms_ma_m, Unset):
            lbnp15_ms_ma_m = UNSET
        else:
            lbnp15_ms_ma_m = self.lbnp15_ms_ma_m

        lbnp15_ms_ma_pctn: float | None | Unset
        if isinstance(self.lbnp15_ms_ma_pctn, Unset):
            lbnp15_ms_ma_pctn = UNSET
        else:
            lbnp15_ms_ma_pctn = self.lbnp15_ms_ma_pctn

        lbnp15_ms_ma_pctn_f: float | None | Unset
        if isinstance(self.lbnp15_ms_ma_pctn_f, Unset):
            lbnp15_ms_ma_pctn_f = UNSET
        else:
            lbnp15_ms_ma_pctn_f = self.lbnp15_ms_ma_pctn_f

        lbnp15_ms_ma_pctn_m: float | None | Unset
        if isinstance(self.lbnp15_ms_ma_pctn_m, Unset):
            lbnp15_ms_ma_pctn_m = UNSET
        else:
            lbnp15_ms_ma_pctn_m = self.lbnp15_ms_ma_pctn_m

        lbnp15_ms_nm: float | None | Unset
        if isinstance(self.lbnp15_ms_nm, Unset):
            lbnp15_ms_nm = UNSET
        else:
            lbnp15_ms_nm = self.lbnp15_ms_nm

        lbnp15_ms_nm_f: float | None | Unset
        if isinstance(self.lbnp15_ms_nm_f, Unset):
            lbnp15_ms_nm_f = UNSET
        else:
            lbnp15_ms_nm_f = self.lbnp15_ms_nm_f

        lbnp15_ms_nm_m: float | None | Unset
        if isinstance(self.lbnp15_ms_nm_m, Unset):
            lbnp15_ms_nm_m = UNSET
        else:
            lbnp15_ms_nm_m = self.lbnp15_ms_nm_m

        lbnp15_ms_nm_pctn: float | None | Unset
        if isinstance(self.lbnp15_ms_nm_pctn, Unset):
            lbnp15_ms_nm_pctn = UNSET
        else:
            lbnp15_ms_nm_pctn = self.lbnp15_ms_nm_pctn

        lbnp15_ms_nm_pctn_f: float | None | Unset
        if isinstance(self.lbnp15_ms_nm_pctn_f, Unset):
            lbnp15_ms_nm_pctn_f = UNSET
        else:
            lbnp15_ms_nm_pctn_f = self.lbnp15_ms_nm_pctn_f

        lbnp15_ms_nm_pctn_m: float | None | Unset
        if isinstance(self.lbnp15_ms_nm_pctn_m, Unset):
            lbnp15_ms_nm_pctn_m = UNSET
        else:
            lbnp15_ms_nm_pctn_m = self.lbnp15_ms_nm_pctn_m

        lbnp15_ms_win: float | None | Unset
        if isinstance(self.lbnp15_ms_win, Unset):
            lbnp15_ms_win = UNSET
        else:
            lbnp15_ms_win = self.lbnp15_ms_win

        lbnp15_ms_win_f: float | None | Unset
        if isinstance(self.lbnp15_ms_win_f, Unset):
            lbnp15_ms_win_f = UNSET
        else:
            lbnp15_ms_win_f = self.lbnp15_ms_win_f

        lbnp15_ms_win_m: float | None | Unset
        if isinstance(self.lbnp15_ms_win_m, Unset):
            lbnp15_ms_win_m = UNSET
        else:
            lbnp15_ms_win_m = self.lbnp15_ms_win_m

        lbnp15_ms_win_pctn: float | None | Unset
        if isinstance(self.lbnp15_ms_win_pctn, Unset):
            lbnp15_ms_win_pctn = UNSET
        else:
            lbnp15_ms_win_pctn = self.lbnp15_ms_win_pctn

        lbnp15_ms_win_pctn_f: float | None | Unset
        if isinstance(self.lbnp15_ms_win_pctn_f, Unset):
            lbnp15_ms_win_pctn_f = UNSET
        else:
            lbnp15_ms_win_pctn_f = self.lbnp15_ms_win_pctn_f

        lbnp15_ms_win_pctn_m: float | None | Unset
        if isinstance(self.lbnp15_ms_win_pctn_m, Unset):
            lbnp15_ms_win_pctn_m = UNSET
        else:
            lbnp15_ms_win_pctn_m = self.lbnp15_ms_win_pctn_m

        lbnp_act_eapctn: float | None | Unset
        if isinstance(self.lbnp_act_eapctn, Unset):
            lbnp_act_eapctn = UNSET
        else:
            lbnp_act_eapctn = self.lbnp_act_eapctn

        lbnp_act_eipctn: float | None | Unset
        if isinstance(self.lbnp_act_eipctn, Unset):
            lbnp_act_eipctn = UNSET
        else:
            lbnp_act_eipctn = self.lbnp_act_eipctn

        lbnp_act_ftstpctn: float | None | Unset
        if isinstance(self.lbnp_act_ftstpctn, Unset):
            lbnp_act_ftstpctn = UNSET
        else:
            lbnp_act_ftstpctn = self.lbnp_act_ftstpctn

        lbnp_act_hmpctn: float | None | Unset
        if isinstance(self.lbnp_act_hmpctn, Unset):
            lbnp_act_hmpctn = UNSET
        else:
            lbnp_act_hmpctn = self.lbnp_act_hmpctn

        lbnp_act_othpctn: float | None | Unset
        if isinstance(self.lbnp_act_othpctn, Unset):
            lbnp_act_othpctn = UNSET
        else:
            lbnp_act_othpctn = self.lbnp_act_othpctn

        lbnp_age_1: float | None | Unset
        if isinstance(self.lbnp_age_1, Unset):
            lbnp_age_1 = UNSET
        else:
            lbnp_age_1 = self.lbnp_age_1

        lbnp_age_1_f: float | None | Unset
        if isinstance(self.lbnp_age_1_f, Unset):
            lbnp_age_1_f = UNSET
        else:
            lbnp_age_1_f = self.lbnp_age_1_f

        lbnp_age_1_m: float | None | Unset
        if isinstance(self.lbnp_age_1_m, Unset):
            lbnp_age_1_m = UNSET
        else:
            lbnp_age_1_m = self.lbnp_age_1_m

        lbnp_age_1pctn: float | None | Unset
        if isinstance(self.lbnp_age_1pctn, Unset):
            lbnp_age_1pctn = UNSET
        else:
            lbnp_age_1pctn = self.lbnp_age_1pctn

        lbnp_age_1pctn_f: float | None | Unset
        if isinstance(self.lbnp_age_1pctn_f, Unset):
            lbnp_age_1pctn_f = UNSET
        else:
            lbnp_age_1pctn_f = self.lbnp_age_1pctn_f

        lbnp_age_1pctn_m: float | None | Unset
        if isinstance(self.lbnp_age_1pctn_m, Unset):
            lbnp_age_1pctn_m = UNSET
        else:
            lbnp_age_1pctn_m = self.lbnp_age_1pctn_m

        lbnp_age_2: float | None | Unset
        if isinstance(self.lbnp_age_2, Unset):
            lbnp_age_2 = UNSET
        else:
            lbnp_age_2 = self.lbnp_age_2

        lbnp_age_2_f: float | None | Unset
        if isinstance(self.lbnp_age_2_f, Unset):
            lbnp_age_2_f = UNSET
        else:
            lbnp_age_2_f = self.lbnp_age_2_f

        lbnp_age_2_m: float | None | Unset
        if isinstance(self.lbnp_age_2_m, Unset):
            lbnp_age_2_m = UNSET
        else:
            lbnp_age_2_m = self.lbnp_age_2_m

        lbnp_age_2pctn: float | None | Unset
        if isinstance(self.lbnp_age_2pctn, Unset):
            lbnp_age_2pctn = UNSET
        else:
            lbnp_age_2pctn = self.lbnp_age_2pctn

        lbnp_age_2pctn_f: float | None | Unset
        if isinstance(self.lbnp_age_2pctn_f, Unset):
            lbnp_age_2pctn_f = UNSET
        else:
            lbnp_age_2pctn_f = self.lbnp_age_2pctn_f

        lbnp_age_2pctn_m: float | None | Unset
        if isinstance(self.lbnp_age_2pctn_m, Unset):
            lbnp_age_2pctn_m = UNSET
        else:
            lbnp_age_2pctn_m = self.lbnp_age_2pctn_m

        lbnp_age_3: float | None | Unset
        if isinstance(self.lbnp_age_3, Unset):
            lbnp_age_3 = UNSET
        else:
            lbnp_age_3 = self.lbnp_age_3

        lbnp_age_3_f: float | None | Unset
        if isinstance(self.lbnp_age_3_f, Unset):
            lbnp_age_3_f = UNSET
        else:
            lbnp_age_3_f = self.lbnp_age_3_f

        lbnp_age_3_m: float | None | Unset
        if isinstance(self.lbnp_age_3_m, Unset):
            lbnp_age_3_m = UNSET
        else:
            lbnp_age_3_m = self.lbnp_age_3_m

        lbnp_age_3pctn: float | None | Unset
        if isinstance(self.lbnp_age_3pctn, Unset):
            lbnp_age_3pctn = UNSET
        else:
            lbnp_age_3pctn = self.lbnp_age_3pctn

        lbnp_age_3pctn_f: float | None | Unset
        if isinstance(self.lbnp_age_3pctn_f, Unset):
            lbnp_age_3pctn_f = UNSET
        else:
            lbnp_age_3pctn_f = self.lbnp_age_3pctn_f

        lbnp_age_3pctn_m: float | None | Unset
        if isinstance(self.lbnp_age_3pctn_m, Unset):
            lbnp_age_3pctn_m = UNSET
        else:
            lbnp_age_3pctn_m = self.lbnp_age_3pctn_m

        lbnp_age_4: float | None | Unset
        if isinstance(self.lbnp_age_4, Unset):
            lbnp_age_4 = UNSET
        else:
            lbnp_age_4 = self.lbnp_age_4

        lbnp_age_4_f: float | None | Unset
        if isinstance(self.lbnp_age_4_f, Unset):
            lbnp_age_4_f = UNSET
        else:
            lbnp_age_4_f = self.lbnp_age_4_f

        lbnp_age_4_m: float | None | Unset
        if isinstance(self.lbnp_age_4_m, Unset):
            lbnp_age_4_m = UNSET
        else:
            lbnp_age_4_m = self.lbnp_age_4_m

        lbnp_age_4pctn: float | None | Unset
        if isinstance(self.lbnp_age_4pctn, Unset):
            lbnp_age_4pctn = UNSET
        else:
            lbnp_age_4pctn = self.lbnp_age_4pctn

        lbnp_age_4pctn_f: float | None | Unset
        if isinstance(self.lbnp_age_4pctn_f, Unset):
            lbnp_age_4pctn_f = UNSET
        else:
            lbnp_age_4pctn_f = self.lbnp_age_4pctn_f

        lbnp_age_4pctn_m: float | None | Unset
        if isinstance(self.lbnp_age_4pctn_m, Unset):
            lbnp_age_4pctn_m = UNSET
        else:
            lbnp_age_4pctn_m = self.lbnp_age_4pctn_m

        lbnp_age_5: float | None | Unset
        if isinstance(self.lbnp_age_5, Unset):
            lbnp_age_5 = UNSET
        else:
            lbnp_age_5 = self.lbnp_age_5

        lbnp_age_5_f: float | None | Unset
        if isinstance(self.lbnp_age_5_f, Unset):
            lbnp_age_5_f = UNSET
        else:
            lbnp_age_5_f = self.lbnp_age_5_f

        lbnp_age_5_m: float | None | Unset
        if isinstance(self.lbnp_age_5_m, Unset):
            lbnp_age_5_m = UNSET
        else:
            lbnp_age_5_m = self.lbnp_age_5_m

        lbnp_age_5pctn: float | None | Unset
        if isinstance(self.lbnp_age_5pctn, Unset):
            lbnp_age_5pctn = UNSET
        else:
            lbnp_age_5pctn = self.lbnp_age_5pctn

        lbnp_age_5pctn_f: float | None | Unset
        if isinstance(self.lbnp_age_5pctn_f, Unset):
            lbnp_age_5pctn_f = UNSET
        else:
            lbnp_age_5pctn_f = self.lbnp_age_5pctn_f

        lbnp_age_5pctn_m: float | None | Unset
        if isinstance(self.lbnp_age_5pctn_m, Unset):
            lbnp_age_5pctn_m = UNSET
        else:
            lbnp_age_5pctn_m = self.lbnp_age_5pctn_m

        lbnp_age_6: float | None | Unset
        if isinstance(self.lbnp_age_6, Unset):
            lbnp_age_6 = UNSET
        else:
            lbnp_age_6 = self.lbnp_age_6

        lbnp_age_6_f: float | None | Unset
        if isinstance(self.lbnp_age_6_f, Unset):
            lbnp_age_6_f = UNSET
        else:
            lbnp_age_6_f = self.lbnp_age_6_f

        lbnp_age_6_m: float | None | Unset
        if isinstance(self.lbnp_age_6_m, Unset):
            lbnp_age_6_m = UNSET
        else:
            lbnp_age_6_m = self.lbnp_age_6_m

        lbnp_age_6pctn: float | None | Unset
        if isinstance(self.lbnp_age_6pctn, Unset):
            lbnp_age_6pctn = UNSET
        else:
            lbnp_age_6pctn = self.lbnp_age_6pctn

        lbnp_age_6pctn_f: float | None | Unset
        if isinstance(self.lbnp_age_6pctn_f, Unset):
            lbnp_age_6pctn_f = UNSET
        else:
            lbnp_age_6pctn_f = self.lbnp_age_6pctn_f

        lbnp_age_6pctn_m: float | None | Unset
        if isinstance(self.lbnp_age_6pctn_m, Unset):
            lbnp_age_6pctn_m = UNSET
        else:
            lbnp_age_6pctn_m = self.lbnp_age_6pctn_m

        lbnp_age_7: float | None | Unset
        if isinstance(self.lbnp_age_7, Unset):
            lbnp_age_7 = UNSET
        else:
            lbnp_age_7 = self.lbnp_age_7

        lbnp_age_7_f: float | None | Unset
        if isinstance(self.lbnp_age_7_f, Unset):
            lbnp_age_7_f = UNSET
        else:
            lbnp_age_7_f = self.lbnp_age_7_f

        lbnp_age_7_m: float | None | Unset
        if isinstance(self.lbnp_age_7_m, Unset):
            lbnp_age_7_m = UNSET
        else:
            lbnp_age_7_m = self.lbnp_age_7_m

        lbnp_age_7pctn: float | None | Unset
        if isinstance(self.lbnp_age_7pctn, Unset):
            lbnp_age_7pctn = UNSET
        else:
            lbnp_age_7pctn = self.lbnp_age_7pctn

        lbnp_age_7pctn_f: float | None | Unset
        if isinstance(self.lbnp_age_7pctn_f, Unset):
            lbnp_age_7pctn_f = UNSET
        else:
            lbnp_age_7pctn_f = self.lbnp_age_7pctn_f

        lbnp_age_7pctn_m: float | None | Unset
        if isinstance(self.lbnp_age_7pctn_m, Unset):
            lbnp_age_7pctn_m = UNSET
        else:
            lbnp_age_7pctn_m = self.lbnp_age_7pctn_m

        lbnp_age_8: float | None | Unset
        if isinstance(self.lbnp_age_8, Unset):
            lbnp_age_8 = UNSET
        else:
            lbnp_age_8 = self.lbnp_age_8

        lbnp_age_8_f: float | None | Unset
        if isinstance(self.lbnp_age_8_f, Unset):
            lbnp_age_8_f = UNSET
        else:
            lbnp_age_8_f = self.lbnp_age_8_f

        lbnp_age_8_m: float | None | Unset
        if isinstance(self.lbnp_age_8_m, Unset):
            lbnp_age_8_m = UNSET
        else:
            lbnp_age_8_m = self.lbnp_age_8_m

        lbnp_age_8pctn: float | None | Unset
        if isinstance(self.lbnp_age_8pctn, Unset):
            lbnp_age_8pctn = UNSET
        else:
            lbnp_age_8pctn = self.lbnp_age_8pctn

        lbnp_age_8pctn_f: float | None | Unset
        if isinstance(self.lbnp_age_8pctn_f, Unset):
            lbnp_age_8pctn_f = UNSET
        else:
            lbnp_age_8pctn_f = self.lbnp_age_8pctn_f

        lbnp_age_8pctn_m: float | None | Unset
        if isinstance(self.lbnp_age_8pctn_m, Unset):
            lbnp_age_8pctn_m = UNSET
        else:
            lbnp_age_8pctn_m = self.lbnp_age_8pctn_m

        lbnp_ea: float | None | Unset
        if isinstance(self.lbnp_ea, Unset):
            lbnp_ea = UNSET
        else:
            lbnp_ea = self.lbnp_ea

        lbnp_ei: float | None | Unset
        if isinstance(self.lbnp_ei, Unset):
            lbnp_ei = UNSET
        else:
            lbnp_ei = self.lbnp_ei

        lbnp_f: float | None | Unset
        if isinstance(self.lbnp_f, Unset):
            lbnp_f = UNSET
        else:
            lbnp_f = self.lbnp_f

        lbnp_ftst: float | None | Unset
        if isinstance(self.lbnp_ftst, Unset):
            lbnp_ftst = UNSET
        else:
            lbnp_ftst = self.lbnp_ftst

        lbnp_hm: float | None | Unset
        if isinstance(self.lbnp_hm, Unset):
            lbnp_hm = UNSET
        else:
            lbnp_hm = self.lbnp_hm

        lbnp_m: float | None | Unset
        if isinstance(self.lbnp_m, Unset):
            lbnp_m = UNSET
        else:
            lbnp_m = self.lbnp_m

        lbnp_ma_f: float | None | Unset
        if isinstance(self.lbnp_ma_f, Unset):
            lbnp_ma_f = UNSET
        else:
            lbnp_ma_f = self.lbnp_ma_f

        lbnp_ma_f_xfdh: float | None | Unset
        if isinstance(self.lbnp_ma_f_xfdh, Unset):
            lbnp_ma_f_xfdh = UNSET
        else:
            lbnp_ma_f_xfdh = self.lbnp_ma_f_xfdh

        lbnp_ma_m: float | None | Unset
        if isinstance(self.lbnp_ma_m, Unset):
            lbnp_ma_m = UNSET
        else:
            lbnp_ma_m = self.lbnp_ma_m

        lbnp_ma_m_xfdh: float | None | Unset
        if isinstance(self.lbnp_ma_m_xfdh, Unset):
            lbnp_ma_m_xfdh = UNSET
        else:
            lbnp_ma_m_xfdh = self.lbnp_ma_m_xfdh

        lbnp_ma_t: float | None | Unset
        if isinstance(self.lbnp_ma_t, Unset):
            lbnp_ma_t = UNSET
        else:
            lbnp_ma_t = self.lbnp_ma_t

        lbnp_ma_t_xfdh: float | None | Unset
        if isinstance(self.lbnp_ma_t_xfdh, Unset):
            lbnp_ma_t_xfdh = UNSET
        else:
            lbnp_ma_t_xfdh = self.lbnp_ma_t_xfdh

        lbnp_odr: float | None | Unset
        if isinstance(self.lbnp_odr, Unset):
            lbnp_odr = UNSET
        else:
            lbnp_odr = self.lbnp_odr

        lbnp_odr_xfdh: float | None | Unset
        if isinstance(self.lbnp_odr_xfdh, Unset):
            lbnp_odr_xfdh = UNSET
        else:
            lbnp_odr_xfdh = self.lbnp_odr_xfdh

        lbnp_oth: float | None | Unset
        if isinstance(self.lbnp_oth, Unset):
            lbnp_oth = UNSET
        else:
            lbnp_oth = self.lbnp_oth

        lbnp_sr: float | None | Unset
        if isinstance(self.lbnp_sr, Unset):
            lbnp_sr = UNSET
        else:
            lbnp_sr = self.lbnp_sr

        lbnp_sr_xfdh: float | None | Unset
        if isinstance(self.lbnp_sr_xfdh, Unset):
            lbnp_sr_xfdh = UNSET
        else:
            lbnp_sr_xfdh = self.lbnp_sr_xfdh

        lf_age_1: float | None | Unset
        if isinstance(self.lf_age_1, Unset):
            lf_age_1 = UNSET
        else:
            lf_age_1 = self.lf_age_1

        lf_age_1_f: float | None | Unset
        if isinstance(self.lf_age_1_f, Unset):
            lf_age_1_f = UNSET
        else:
            lf_age_1_f = self.lf_age_1_f

        lf_age_1_f_xfdh: float | None | Unset
        if isinstance(self.lf_age_1_f_xfdh, Unset):
            lf_age_1_f_xfdh = UNSET
        else:
            lf_age_1_f_xfdh = self.lf_age_1_f_xfdh

        lf_age_1_m: float | None | Unset
        if isinstance(self.lf_age_1_m, Unset):
            lf_age_1_m = UNSET
        else:
            lf_age_1_m = self.lf_age_1_m

        lf_age_1_m_xfdh: float | None | Unset
        if isinstance(self.lf_age_1_m_xfdh, Unset):
            lf_age_1_m_xfdh = UNSET
        else:
            lf_age_1_m_xfdh = self.lf_age_1_m_xfdh

        lf_age_1_xfdh: float | None | Unset
        if isinstance(self.lf_age_1_xfdh, Unset):
            lf_age_1_xfdh = UNSET
        else:
            lf_age_1_xfdh = self.lf_age_1_xfdh

        lf_age_2: float | None | Unset
        if isinstance(self.lf_age_2, Unset):
            lf_age_2 = UNSET
        else:
            lf_age_2 = self.lf_age_2

        lf_age_2_f: float | None | Unset
        if isinstance(self.lf_age_2_f, Unset):
            lf_age_2_f = UNSET
        else:
            lf_age_2_f = self.lf_age_2_f

        lf_age_2_f_xfdh: float | None | Unset
        if isinstance(self.lf_age_2_f_xfdh, Unset):
            lf_age_2_f_xfdh = UNSET
        else:
            lf_age_2_f_xfdh = self.lf_age_2_f_xfdh

        lf_age_2_m: float | None | Unset
        if isinstance(self.lf_age_2_m, Unset):
            lf_age_2_m = UNSET
        else:
            lf_age_2_m = self.lf_age_2_m

        lf_age_2_m_xfdh: float | None | Unset
        if isinstance(self.lf_age_2_m_xfdh, Unset):
            lf_age_2_m_xfdh = UNSET
        else:
            lf_age_2_m_xfdh = self.lf_age_2_m_xfdh

        lf_age_2_xfdh: float | None | Unset
        if isinstance(self.lf_age_2_xfdh, Unset):
            lf_age_2_xfdh = UNSET
        else:
            lf_age_2_xfdh = self.lf_age_2_xfdh

        lf_age_3: float | None | Unset
        if isinstance(self.lf_age_3, Unset):
            lf_age_3 = UNSET
        else:
            lf_age_3 = self.lf_age_3

        lf_age_3_f: float | None | Unset
        if isinstance(self.lf_age_3_f, Unset):
            lf_age_3_f = UNSET
        else:
            lf_age_3_f = self.lf_age_3_f

        lf_age_3_f_xfdh: float | None | Unset
        if isinstance(self.lf_age_3_f_xfdh, Unset):
            lf_age_3_f_xfdh = UNSET
        else:
            lf_age_3_f_xfdh = self.lf_age_3_f_xfdh

        lf_age_3_m: float | None | Unset
        if isinstance(self.lf_age_3_m, Unset):
            lf_age_3_m = UNSET
        else:
            lf_age_3_m = self.lf_age_3_m

        lf_age_3_m_xfdh: float | None | Unset
        if isinstance(self.lf_age_3_m_xfdh, Unset):
            lf_age_3_m_xfdh = UNSET
        else:
            lf_age_3_m_xfdh = self.lf_age_3_m_xfdh

        lf_age_3_xfdh: float | None | Unset
        if isinstance(self.lf_age_3_xfdh, Unset):
            lf_age_3_xfdh = UNSET
        else:
            lf_age_3_xfdh = self.lf_age_3_xfdh

        lf_age_4: float | None | Unset
        if isinstance(self.lf_age_4, Unset):
            lf_age_4 = UNSET
        else:
            lf_age_4 = self.lf_age_4

        lf_age_4_f: float | None | Unset
        if isinstance(self.lf_age_4_f, Unset):
            lf_age_4_f = UNSET
        else:
            lf_age_4_f = self.lf_age_4_f

        lf_age_4_f_xfdh: float | None | Unset
        if isinstance(self.lf_age_4_f_xfdh, Unset):
            lf_age_4_f_xfdh = UNSET
        else:
            lf_age_4_f_xfdh = self.lf_age_4_f_xfdh

        lf_age_4_m: float | None | Unset
        if isinstance(self.lf_age_4_m, Unset):
            lf_age_4_m = UNSET
        else:
            lf_age_4_m = self.lf_age_4_m

        lf_age_4_m_xfdh: float | None | Unset
        if isinstance(self.lf_age_4_m_xfdh, Unset):
            lf_age_4_m_xfdh = UNSET
        else:
            lf_age_4_m_xfdh = self.lf_age_4_m_xfdh

        lf_age_4_xfdh: float | None | Unset
        if isinstance(self.lf_age_4_xfdh, Unset):
            lf_age_4_xfdh = UNSET
        else:
            lf_age_4_xfdh = self.lf_age_4_xfdh

        lf_age_5: float | None | Unset
        if isinstance(self.lf_age_5, Unset):
            lf_age_5 = UNSET
        else:
            lf_age_5 = self.lf_age_5

        lf_age_5_f: float | None | Unset
        if isinstance(self.lf_age_5_f, Unset):
            lf_age_5_f = UNSET
        else:
            lf_age_5_f = self.lf_age_5_f

        lf_age_5_f_xfdh: float | None | Unset
        if isinstance(self.lf_age_5_f_xfdh, Unset):
            lf_age_5_f_xfdh = UNSET
        else:
            lf_age_5_f_xfdh = self.lf_age_5_f_xfdh

        lf_age_5_m: float | None | Unset
        if isinstance(self.lf_age_5_m, Unset):
            lf_age_5_m = UNSET
        else:
            lf_age_5_m = self.lf_age_5_m

        lf_age_5_m_xfdh: float | None | Unset
        if isinstance(self.lf_age_5_m_xfdh, Unset):
            lf_age_5_m_xfdh = UNSET
        else:
            lf_age_5_m_xfdh = self.lf_age_5_m_xfdh

        lf_age_5_xfdh: float | None | Unset
        if isinstance(self.lf_age_5_xfdh, Unset):
            lf_age_5_xfdh = UNSET
        else:
            lf_age_5_xfdh = self.lf_age_5_xfdh

        lf_age_6: float | None | Unset
        if isinstance(self.lf_age_6, Unset):
            lf_age_6 = UNSET
        else:
            lf_age_6 = self.lf_age_6

        lf_age_6_f: float | None | Unset
        if isinstance(self.lf_age_6_f, Unset):
            lf_age_6_f = UNSET
        else:
            lf_age_6_f = self.lf_age_6_f

        lf_age_6_f_xfdh: float | None | Unset
        if isinstance(self.lf_age_6_f_xfdh, Unset):
            lf_age_6_f_xfdh = UNSET
        else:
            lf_age_6_f_xfdh = self.lf_age_6_f_xfdh

        lf_age_6_m: float | None | Unset
        if isinstance(self.lf_age_6_m, Unset):
            lf_age_6_m = UNSET
        else:
            lf_age_6_m = self.lf_age_6_m

        lf_age_6_m_xfdh: float | None | Unset
        if isinstance(self.lf_age_6_m_xfdh, Unset):
            lf_age_6_m_xfdh = UNSET
        else:
            lf_age_6_m_xfdh = self.lf_age_6_m_xfdh

        lf_age_6_xfdh: float | None | Unset
        if isinstance(self.lf_age_6_xfdh, Unset):
            lf_age_6_xfdh = UNSET
        else:
            lf_age_6_xfdh = self.lf_age_6_xfdh

        lf_f: float | None | Unset
        if isinstance(self.lf_f, Unset):
            lf_f = UNSET
        else:
            lf_f = self.lf_f

        lf_f_xfdh: float | None | Unset
        if isinstance(self.lf_f_xfdh, Unset):
            lf_f_xfdh = UNSET
        else:
            lf_f_xfdh = self.lf_f_xfdh

        lf_m: float | None | Unset
        if isinstance(self.lf_m, Unset):
            lf_m = UNSET
        else:
            lf_m = self.lf_m

        lf_m_xfdh: float | None | Unset
        if isinstance(self.lf_m_xfdh, Unset):
            lf_m_xfdh = UNSET
        else:
            lf_m_xfdh = self.lf_m_xfdh

        lf_ma_f: float | None | Unset
        if isinstance(self.lf_ma_f, Unset):
            lf_ma_f = UNSET
        else:
            lf_ma_f = self.lf_ma_f

        lf_ma_f_xfdh: float | None | Unset
        if isinstance(self.lf_ma_f_xfdh, Unset):
            lf_ma_f_xfdh = UNSET
        else:
            lf_ma_f_xfdh = self.lf_ma_f_xfdh

        lf_ma_m: float | None | Unset
        if isinstance(self.lf_ma_m, Unset):
            lf_ma_m = UNSET
        else:
            lf_ma_m = self.lf_ma_m

        lf_ma_m_xfdh: float | None | Unset
        if isinstance(self.lf_ma_m_xfdh, Unset):
            lf_ma_m_xfdh = UNSET
        else:
            lf_ma_m_xfdh = self.lf_ma_m_xfdh

        lf_ma_t: float | None | Unset
        if isinstance(self.lf_ma_t, Unset):
            lf_ma_t = UNSET
        else:
            lf_ma_t = self.lf_ma_t

        lf_ma_t_xfdh: float | None | Unset
        if isinstance(self.lf_ma_t_xfdh, Unset):
            lf_ma_t_xfdh = UNSET
        else:
            lf_ma_t_xfdh = self.lf_ma_t_xfdh

        lf_sr: float | None | Unset
        if isinstance(self.lf_sr, Unset):
            lf_sr = UNSET
        else:
            lf_sr = self.lf_sr

        lf_sr_xfdh: float | None | Unset
        if isinstance(self.lf_sr_xfdh, Unset):
            lf_sr_xfdh = UNSET
        else:
            lf_sr_xfdh = self.lf_sr_xfdh

        lfpr_age_1: float | None | Unset
        if isinstance(self.lfpr_age_1, Unset):
            lfpr_age_1 = UNSET
        else:
            lfpr_age_1 = self.lfpr_age_1

        lfpr_age_1_f: float | None | Unset
        if isinstance(self.lfpr_age_1_f, Unset):
            lfpr_age_1_f = UNSET
        else:
            lfpr_age_1_f = self.lfpr_age_1_f

        lfpr_age_1_f_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_1_f_xfdh, Unset):
            lfpr_age_1_f_xfdh = UNSET
        else:
            lfpr_age_1_f_xfdh = self.lfpr_age_1_f_xfdh

        lfpr_age_1_m: float | None | Unset
        if isinstance(self.lfpr_age_1_m, Unset):
            lfpr_age_1_m = UNSET
        else:
            lfpr_age_1_m = self.lfpr_age_1_m

        lfpr_age_1_m_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_1_m_xfdh, Unset):
            lfpr_age_1_m_xfdh = UNSET
        else:
            lfpr_age_1_m_xfdh = self.lfpr_age_1_m_xfdh

        lfpr_age_1_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_1_xfdh, Unset):
            lfpr_age_1_xfdh = UNSET
        else:
            lfpr_age_1_xfdh = self.lfpr_age_1_xfdh

        lfpr_age_2: float | None | Unset
        if isinstance(self.lfpr_age_2, Unset):
            lfpr_age_2 = UNSET
        else:
            lfpr_age_2 = self.lfpr_age_2

        lfpr_age_2_f: float | None | Unset
        if isinstance(self.lfpr_age_2_f, Unset):
            lfpr_age_2_f = UNSET
        else:
            lfpr_age_2_f = self.lfpr_age_2_f

        lfpr_age_2_f_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_2_f_xfdh, Unset):
            lfpr_age_2_f_xfdh = UNSET
        else:
            lfpr_age_2_f_xfdh = self.lfpr_age_2_f_xfdh

        lfpr_age_2_m: float | None | Unset
        if isinstance(self.lfpr_age_2_m, Unset):
            lfpr_age_2_m = UNSET
        else:
            lfpr_age_2_m = self.lfpr_age_2_m

        lfpr_age_2_m_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_2_m_xfdh, Unset):
            lfpr_age_2_m_xfdh = UNSET
        else:
            lfpr_age_2_m_xfdh = self.lfpr_age_2_m_xfdh

        lfpr_age_2_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_2_xfdh, Unset):
            lfpr_age_2_xfdh = UNSET
        else:
            lfpr_age_2_xfdh = self.lfpr_age_2_xfdh

        lfpr_age_3: float | None | Unset
        if isinstance(self.lfpr_age_3, Unset):
            lfpr_age_3 = UNSET
        else:
            lfpr_age_3 = self.lfpr_age_3

        lfpr_age_3_f: float | None | Unset
        if isinstance(self.lfpr_age_3_f, Unset):
            lfpr_age_3_f = UNSET
        else:
            lfpr_age_3_f = self.lfpr_age_3_f

        lfpr_age_3_f_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_3_f_xfdh, Unset):
            lfpr_age_3_f_xfdh = UNSET
        else:
            lfpr_age_3_f_xfdh = self.lfpr_age_3_f_xfdh

        lfpr_age_3_m: float | None | Unset
        if isinstance(self.lfpr_age_3_m, Unset):
            lfpr_age_3_m = UNSET
        else:
            lfpr_age_3_m = self.lfpr_age_3_m

        lfpr_age_3_m_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_3_m_xfdh, Unset):
            lfpr_age_3_m_xfdh = UNSET
        else:
            lfpr_age_3_m_xfdh = self.lfpr_age_3_m_xfdh

        lfpr_age_3_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_3_xfdh, Unset):
            lfpr_age_3_xfdh = UNSET
        else:
            lfpr_age_3_xfdh = self.lfpr_age_3_xfdh

        lfpr_age_4: float | None | Unset
        if isinstance(self.lfpr_age_4, Unset):
            lfpr_age_4 = UNSET
        else:
            lfpr_age_4 = self.lfpr_age_4

        lfpr_age_4_f: float | None | Unset
        if isinstance(self.lfpr_age_4_f, Unset):
            lfpr_age_4_f = UNSET
        else:
            lfpr_age_4_f = self.lfpr_age_4_f

        lfpr_age_4_f_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_4_f_xfdh, Unset):
            lfpr_age_4_f_xfdh = UNSET
        else:
            lfpr_age_4_f_xfdh = self.lfpr_age_4_f_xfdh

        lfpr_age_4_m: float | None | Unset
        if isinstance(self.lfpr_age_4_m, Unset):
            lfpr_age_4_m = UNSET
        else:
            lfpr_age_4_m = self.lfpr_age_4_m

        lfpr_age_4_m_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_4_m_xfdh, Unset):
            lfpr_age_4_m_xfdh = UNSET
        else:
            lfpr_age_4_m_xfdh = self.lfpr_age_4_m_xfdh

        lfpr_age_4_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_4_xfdh, Unset):
            lfpr_age_4_xfdh = UNSET
        else:
            lfpr_age_4_xfdh = self.lfpr_age_4_xfdh

        lfpr_age_5: float | None | Unset
        if isinstance(self.lfpr_age_5, Unset):
            lfpr_age_5 = UNSET
        else:
            lfpr_age_5 = self.lfpr_age_5

        lfpr_age_5_f: float | None | Unset
        if isinstance(self.lfpr_age_5_f, Unset):
            lfpr_age_5_f = UNSET
        else:
            lfpr_age_5_f = self.lfpr_age_5_f

        lfpr_age_5_f_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_5_f_xfdh, Unset):
            lfpr_age_5_f_xfdh = UNSET
        else:
            lfpr_age_5_f_xfdh = self.lfpr_age_5_f_xfdh

        lfpr_age_5_m: float | None | Unset
        if isinstance(self.lfpr_age_5_m, Unset):
            lfpr_age_5_m = UNSET
        else:
            lfpr_age_5_m = self.lfpr_age_5_m

        lfpr_age_5_m_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_5_m_xfdh, Unset):
            lfpr_age_5_m_xfdh = UNSET
        else:
            lfpr_age_5_m_xfdh = self.lfpr_age_5_m_xfdh

        lfpr_age_5_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_5_xfdh, Unset):
            lfpr_age_5_xfdh = UNSET
        else:
            lfpr_age_5_xfdh = self.lfpr_age_5_xfdh

        lfpr_age_6: float | None | Unset
        if isinstance(self.lfpr_age_6, Unset):
            lfpr_age_6 = UNSET
        else:
            lfpr_age_6 = self.lfpr_age_6

        lfpr_age_6_f: float | None | Unset
        if isinstance(self.lfpr_age_6_f, Unset):
            lfpr_age_6_f = UNSET
        else:
            lfpr_age_6_f = self.lfpr_age_6_f

        lfpr_age_6_f_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_6_f_xfdh, Unset):
            lfpr_age_6_f_xfdh = UNSET
        else:
            lfpr_age_6_f_xfdh = self.lfpr_age_6_f_xfdh

        lfpr_age_6_m: float | None | Unset
        if isinstance(self.lfpr_age_6_m, Unset):
            lfpr_age_6_m = UNSET
        else:
            lfpr_age_6_m = self.lfpr_age_6_m

        lfpr_age_6_m_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_6_m_xfdh, Unset):
            lfpr_age_6_m_xfdh = UNSET
        else:
            lfpr_age_6_m_xfdh = self.lfpr_age_6_m_xfdh

        lfpr_age_6_xfdh: float | None | Unset
        if isinstance(self.lfpr_age_6_xfdh, Unset):
            lfpr_age_6_xfdh = UNSET
        else:
            lfpr_age_6_xfdh = self.lfpr_age_6_xfdh

        lfpr_f: float | None | Unset
        if isinstance(self.lfpr_f, Unset):
            lfpr_f = UNSET
        else:
            lfpr_f = self.lfpr_f

        lfpr_f_xfdh: float | None | Unset
        if isinstance(self.lfpr_f_xfdh, Unset):
            lfpr_f_xfdh = UNSET
        else:
            lfpr_f_xfdh = self.lfpr_f_xfdh

        lfpr_m: float | None | Unset
        if isinstance(self.lfpr_m, Unset):
            lfpr_m = UNSET
        else:
            lfpr_m = self.lfpr_m

        lfpr_m_xfdh: float | None | Unset
        if isinstance(self.lfpr_m_xfdh, Unset):
            lfpr_m_xfdh = UNSET
        else:
            lfpr_m_xfdh = self.lfpr_m_xfdh

        ma_econhh: float | None | Unset
        if isinstance(self.ma_econhh, Unset):
            ma_econhh = UNSET
        else:
            ma_econhh = self.ma_econhh

        ma_econhh_xfdh: float | None | Unset
        if isinstance(self.ma_econhh_xfdh, Unset):
            ma_econhh_xfdh = UNSET
        else:
            ma_econhh_xfdh = self.ma_econhh_xfdh

        ma_hh: float | None | Unset
        if isinstance(self.ma_hh, Unset):
            ma_hh = UNSET
        else:
            ma_hh = self.ma_hh

        my_lp: float | None | Unset
        if isinstance(self.my_lp, Unset):
            my_lp = UNSET
        else:
            my_lp = self.my_lp

        t_lbnp: float | None | Unset
        if isinstance(self.t_lbnp, Unset):
            t_lbnp = UNSET
        else:
            t_lbnp = self.t_lbnp

        t_lbnp15: float | None | Unset
        if isinstance(self.t_lbnp15, Unset):
            t_lbnp15 = UNSET
        else:
            t_lbnp15 = self.t_lbnp15

        t_lf: float | None | Unset
        if isinstance(self.t_lf, Unset):
            t_lf = UNSET
        else:
            t_lf = self.t_lf

        t_lf_xfdh: float | None | Unset
        if isinstance(self.t_lf_xfdh, Unset):
            t_lf_xfdh = UNSET
        else:
            t_lf_xfdh = self.t_lf_xfdh

        t_lfpr: float | None | Unset
        if isinstance(self.t_lfpr, Unset):
            t_lfpr = UNSET
        else:
            t_lfpr = self.t_lfpr

        t_lfpr_xfdh: float | None | Unset
        if isinstance(self.t_lfpr_xfdh, Unset):
            t_lfpr_xfdh = UNSET
        else:
            t_lfpr_xfdh = self.t_lfpr_xfdh

        year: float | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

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
        if adhz is not UNSET:
            field_dict["adhz"] = adhz
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
        if dh_ea is not UNSET:
            field_dict["dh_ea"] = dh_ea
        if dh_ei is not UNSET:
            field_dict["dh_ei"] = dh_ei
        if dha_oth is not UNSET:
            field_dict["dha_oth"] = dha_oth
        if dha_othpctn is not UNSET:
            field_dict["dha_othpctn"] = dha_othpctn
        if dha_wf is not UNSET:
            field_dict["dha_wf"] = dha_wf
        if dha_wfpctn is not UNSET:
            field_dict["dha_wfpctn"] = dha_wfpctn
        if dhi_1 is not UNSET:
            field_dict["dhi_1"] = dhi_1
        if dhi_1pctn is not UNSET:
            field_dict["dhi_1pctn"] = dhi_1pctn
        if dhi_2 is not UNSET:
            field_dict["dhi_2"] = dhi_2
        if dhi_2pctn is not UNSET:
            field_dict["dhi_2pctn"] = dhi_2pctn
        if dhi_3 is not UNSET:
            field_dict["dhi_3"] = dhi_3
        if dhi_3pctn is not UNSET:
            field_dict["dhi_3pctn"] = dhi_3pctn
        if dhi_e1 is not UNSET:
            field_dict["dhi_e1"] = dhi_e1
        if dhi_e1pctn is not UNSET:
            field_dict["dhi_e1pctn"] = dhi_e1pctn
        if dhi_e2 is not UNSET:
            field_dict["dhi_e2"] = dhi_e2
        if dhi_e2pctn is not UNSET:
            field_dict["dhi_e2pctn"] = dhi_e2pctn
        if dhi_e3 is not UNSET:
            field_dict["dhi_e3"] = dhi_e3
        if dhi_e3pctn is not UNSET:
            field_dict["dhi_e3pctn"] = dhi_e3pctn
        if dht_oo is not UNSET:
            field_dict["dht_oo"] = dht_oo
        if dht_oopctn is not UNSET:
            field_dict["dht_oopctn"] = dht_oopctn
        if dht_oth is not UNSET:
            field_dict["dht_oth"] = dht_oth
        if dht_othpctn is not UNSET:
            field_dict["dht_othpctn"] = dht_othpctn
        if dht_st is not UNSET:
            field_dict["dht_st"] = dht_st
        if dht_stpctn is not UNSET:
            field_dict["dht_stpctn"] = dht_stpctn
        if dhz_1 is not UNSET:
            field_dict["dhz_1"] = dhz_1
        if dhz_1pctn is not UNSET:
            field_dict["dhz_1pctn"] = dhz_1pctn
        if dhz_2 is not UNSET:
            field_dict["dhz_2"] = dhz_2
        if dhz_2pctn is not UNSET:
            field_dict["dhz_2pctn"] = dhz_2pctn
        if dhz_3 is not UNSET:
            field_dict["dhz_3"] = dhz_3
        if dhz_3pctn is not UNSET:
            field_dict["dhz_3pctn"] = dhz_3pctn
        if dhz_4 is not UNSET:
            field_dict["dhz_4"] = dhz_4
        if dhz_4pctn is not UNSET:
            field_dict["dhz_4pctn"] = dhz_4pctn
        if dhz_5 is not UNSET:
            field_dict["dhz_5"] = dhz_5
        if dhz_5_6 is not UNSET:
            field_dict["dhz_5_6"] = dhz_5_6
        if dhz_5_6pctn is not UNSET:
            field_dict["dhz_5_6pctn"] = dhz_5_6pctn
        if dhz_5pctn is not UNSET:
            field_dict["dhz_5pctn"] = dhz_5pctn
        if dhz_6 is not UNSET:
            field_dict["dhz_6"] = dhz_6
        if dhz_6pctn is not UNSET:
            field_dict["dhz_6pctn"] = dhz_6pctn
        if lbnp15_edu_age_1pctn is not UNSET:
            field_dict["lbnp15_edu_age_1pctn"] = lbnp15_edu_age_1pctn
        if lbnp15_edu_age_2pctn is not UNSET:
            field_dict["lbnp15_edu_age_2pctn"] = lbnp15_edu_age_2pctn
        if lbnp15_edu_age_3pctn is not UNSET:
            field_dict["lbnp15_edu_age_3pctn"] = lbnp15_edu_age_3pctn
        if lbnp15_edu_age_4pctn is not UNSET:
            field_dict["lbnp15_edu_age_4pctn"] = lbnp15_edu_age_4pctn
        if lbnp15_edu_age_5pctn is not UNSET:
            field_dict["lbnp15_edu_age_5pctn"] = lbnp15_edu_age_5pctn
        if lbnp15_edu_age_6pctn is not UNSET:
            field_dict["lbnp15_edu_age_6pctn"] = lbnp15_edu_age_6pctn
        if lbnp15_edu_age_7pctn is not UNSET:
            field_dict["lbnp15_edu_age_7pctn"] = lbnp15_edu_age_7pctn
        if lbnp15_edu_age_8pctn is not UNSET:
            field_dict["lbnp15_edu_age_8pctn"] = lbnp15_edu_age_8pctn
        if lbnp15_edu_deg is not UNSET:
            field_dict["lbnp15_edu_deg"] = lbnp15_edu_deg
        if lbnp15_edu_deg_f is not UNSET:
            field_dict["lbnp15_edu_deg_f"] = lbnp15_edu_deg_f
        if lbnp15_edu_deg_m is not UNSET:
            field_dict["lbnp15_edu_deg_m"] = lbnp15_edu_deg_m
        if lbnp15_edu_deg_pctn is not UNSET:
            field_dict["lbnp15_edu_deg_pctn"] = lbnp15_edu_deg_pctn
        if lbnp15_edu_deg_pctn_f is not UNSET:
            field_dict["lbnp15_edu_deg_pctn_f"] = lbnp15_edu_deg_pctn_f
        if lbnp15_edu_deg_pctn_m is not UNSET:
            field_dict["lbnp15_edu_deg_pctn_m"] = lbnp15_edu_deg_pctn_m
        if lbnp15_edu_lsed is not UNSET:
            field_dict["lbnp15_edu_lsed"] = lbnp15_edu_lsed
        if lbnp15_edu_lsed_f is not UNSET:
            field_dict["lbnp15_edu_lsed_f"] = lbnp15_edu_lsed_f
        if lbnp15_edu_lsed_m is not UNSET:
            field_dict["lbnp15_edu_lsed_m"] = lbnp15_edu_lsed_m
        if lbnp15_edu_lsed_pctn is not UNSET:
            field_dict["lbnp15_edu_lsed_pctn"] = lbnp15_edu_lsed_pctn
        if lbnp15_edu_lsed_pctn_f is not UNSET:
            field_dict["lbnp15_edu_lsed_pctn_f"] = lbnp15_edu_lsed_pctn_f
        if lbnp15_edu_lsed_pctn_m is not UNSET:
            field_dict["lbnp15_edu_lsed_pctn_m"] = lbnp15_edu_lsed_pctn_m
        if lbnp15_edu_ndeg is not UNSET:
            field_dict["lbnp15_edu_ndeg"] = lbnp15_edu_ndeg
        if lbnp15_edu_ndeg_f is not UNSET:
            field_dict["lbnp15_edu_ndeg_f"] = lbnp15_edu_ndeg_f
        if lbnp15_edu_ndeg_m is not UNSET:
            field_dict["lbnp15_edu_ndeg_m"] = lbnp15_edu_ndeg_m
        if lbnp15_edu_ndeg_pctn is not UNSET:
            field_dict["lbnp15_edu_ndeg_pctn"] = lbnp15_edu_ndeg_pctn
        if lbnp15_edu_ndeg_pctn_f is not UNSET:
            field_dict["lbnp15_edu_ndeg_pctn_f"] = lbnp15_edu_ndeg_pctn_f
        if lbnp15_edu_ndeg_pctn_m is not UNSET:
            field_dict["lbnp15_edu_ndeg_pctn_m"] = lbnp15_edu_ndeg_pctn_m
        if lbnp15_edu_pctn is not UNSET:
            field_dict["lbnp15_edu_pctn"] = lbnp15_edu_pctn
        if lbnp15_edu_prepri is not UNSET:
            field_dict["lbnp15_edu_prepri"] = lbnp15_edu_prepri
        if lbnp15_edu_prepri_f is not UNSET:
            field_dict["lbnp15_edu_prepri_f"] = lbnp15_edu_prepri_f
        if lbnp15_edu_prepri_m is not UNSET:
            field_dict["lbnp15_edu_prepri_m"] = lbnp15_edu_prepri_m
        if lbnp15_edu_prepri_pctn is not UNSET:
            field_dict["lbnp15_edu_prepri_pctn"] = lbnp15_edu_prepri_pctn
        if lbnp15_edu_prepri_pctn_f is not UNSET:
            field_dict["lbnp15_edu_prepri_pctn_f"] = lbnp15_edu_prepri_pctn_f
        if lbnp15_edu_prepri_pctn_m is not UNSET:
            field_dict["lbnp15_edu_prepri_pctn_m"] = lbnp15_edu_prepri_pctn_m
        if lbnp15_edu_psec is not UNSET:
            field_dict["lbnp15_edu_psec"] = lbnp15_edu_psec
        if lbnp15_edu_psec_f is not UNSET:
            field_dict["lbnp15_edu_psec_f"] = lbnp15_edu_psec_f
        if lbnp15_edu_psec_m is not UNSET:
            field_dict["lbnp15_edu_psec_m"] = lbnp15_edu_psec_m
        if lbnp15_edu_psec_pctn is not UNSET:
            field_dict["lbnp15_edu_psec_pctn"] = lbnp15_edu_psec_pctn
        if lbnp15_edu_psec_pctn_f is not UNSET:
            field_dict["lbnp15_edu_psec_pctn_f"] = lbnp15_edu_psec_pctn_f
        if lbnp15_edu_psec_pctn_m is not UNSET:
            field_dict["lbnp15_edu_psec_pctn_m"] = lbnp15_edu_psec_pctn_m
        if lbnp15_edu_usec is not UNSET:
            field_dict["lbnp15_edu_usec"] = lbnp15_edu_usec
        if lbnp15_edu_usec_f is not UNSET:
            field_dict["lbnp15_edu_usec_f"] = lbnp15_edu_usec_f
        if lbnp15_edu_usec_m is not UNSET:
            field_dict["lbnp15_edu_usec_m"] = lbnp15_edu_usec_m
        if lbnp15_edu_usec_pctn is not UNSET:
            field_dict["lbnp15_edu_usec_pctn"] = lbnp15_edu_usec_pctn
        if lbnp15_edu_usec_pctn_f is not UNSET:
            field_dict["lbnp15_edu_usec_pctn_f"] = lbnp15_edu_usec_pctn_f
        if lbnp15_edu_usec_pctn_m is not UNSET:
            field_dict["lbnp15_edu_usec_pctn_m"] = lbnp15_edu_usec_pctn_m
        if lbnp15_f is not UNSET:
            field_dict["lbnp15_f"] = lbnp15_f
        if lbnp15_m is not UNSET:
            field_dict["lbnp15_m"] = lbnp15_m
        if lbnp15_ms_divsep is not UNSET:
            field_dict["lbnp15_ms_divsep"] = lbnp15_ms_divsep
        if lbnp15_ms_divsep_f is not UNSET:
            field_dict["lbnp15_ms_divsep_f"] = lbnp15_ms_divsep_f
        if lbnp15_ms_divsep_m is not UNSET:
            field_dict["lbnp15_ms_divsep_m"] = lbnp15_ms_divsep_m
        if lbnp15_ms_divsep_pctn is not UNSET:
            field_dict["lbnp15_ms_divsep_pctn"] = lbnp15_ms_divsep_pctn
        if lbnp15_ms_divsep_pctn_f is not UNSET:
            field_dict["lbnp15_ms_divsep_pctn_f"] = lbnp15_ms_divsep_pctn_f
        if lbnp15_ms_divsep_pctn_m is not UNSET:
            field_dict["lbnp15_ms_divsep_pctn_m"] = lbnp15_ms_divsep_pctn_m
        if lbnp15_ms_ma is not UNSET:
            field_dict["lbnp15_ms_ma"] = lbnp15_ms_ma
        if lbnp15_ms_ma_f is not UNSET:
            field_dict["lbnp15_ms_ma_f"] = lbnp15_ms_ma_f
        if lbnp15_ms_ma_m is not UNSET:
            field_dict["lbnp15_ms_ma_m"] = lbnp15_ms_ma_m
        if lbnp15_ms_ma_pctn is not UNSET:
            field_dict["lbnp15_ms_ma_pctn"] = lbnp15_ms_ma_pctn
        if lbnp15_ms_ma_pctn_f is not UNSET:
            field_dict["lbnp15_ms_ma_pctn_f"] = lbnp15_ms_ma_pctn_f
        if lbnp15_ms_ma_pctn_m is not UNSET:
            field_dict["lbnp15_ms_ma_pctn_m"] = lbnp15_ms_ma_pctn_m
        if lbnp15_ms_nm is not UNSET:
            field_dict["lbnp15_ms_nm"] = lbnp15_ms_nm
        if lbnp15_ms_nm_f is not UNSET:
            field_dict["lbnp15_ms_nm_f"] = lbnp15_ms_nm_f
        if lbnp15_ms_nm_m is not UNSET:
            field_dict["lbnp15_ms_nm_m"] = lbnp15_ms_nm_m
        if lbnp15_ms_nm_pctn is not UNSET:
            field_dict["lbnp15_ms_nm_pctn"] = lbnp15_ms_nm_pctn
        if lbnp15_ms_nm_pctn_f is not UNSET:
            field_dict["lbnp15_ms_nm_pctn_f"] = lbnp15_ms_nm_pctn_f
        if lbnp15_ms_nm_pctn_m is not UNSET:
            field_dict["lbnp15_ms_nm_pctn_m"] = lbnp15_ms_nm_pctn_m
        if lbnp15_ms_win is not UNSET:
            field_dict["lbnp15_ms_win"] = lbnp15_ms_win
        if lbnp15_ms_win_f is not UNSET:
            field_dict["lbnp15_ms_win_f"] = lbnp15_ms_win_f
        if lbnp15_ms_win_m is not UNSET:
            field_dict["lbnp15_ms_win_m"] = lbnp15_ms_win_m
        if lbnp15_ms_win_pctn is not UNSET:
            field_dict["lbnp15_ms_win_pctn"] = lbnp15_ms_win_pctn
        if lbnp15_ms_win_pctn_f is not UNSET:
            field_dict["lbnp15_ms_win_pctn_f"] = lbnp15_ms_win_pctn_f
        if lbnp15_ms_win_pctn_m is not UNSET:
            field_dict["lbnp15_ms_win_pctn_m"] = lbnp15_ms_win_pctn_m
        if lbnp_act_eapctn is not UNSET:
            field_dict["lbnp_act_eapctn"] = lbnp_act_eapctn
        if lbnp_act_eipctn is not UNSET:
            field_dict["lbnp_act_eipctn"] = lbnp_act_eipctn
        if lbnp_act_ftstpctn is not UNSET:
            field_dict["lbnp_act_ftstpctn"] = lbnp_act_ftstpctn
        if lbnp_act_hmpctn is not UNSET:
            field_dict["lbnp_act_hmpctn"] = lbnp_act_hmpctn
        if lbnp_act_othpctn is not UNSET:
            field_dict["lbnp_act_othpctn"] = lbnp_act_othpctn
        if lbnp_age_1 is not UNSET:
            field_dict["lbnp_age_1"] = lbnp_age_1
        if lbnp_age_1_f is not UNSET:
            field_dict["lbnp_age_1_f"] = lbnp_age_1_f
        if lbnp_age_1_m is not UNSET:
            field_dict["lbnp_age_1_m"] = lbnp_age_1_m
        if lbnp_age_1pctn is not UNSET:
            field_dict["lbnp_age_1pctn"] = lbnp_age_1pctn
        if lbnp_age_1pctn_f is not UNSET:
            field_dict["lbnp_age_1pctn_f"] = lbnp_age_1pctn_f
        if lbnp_age_1pctn_m is not UNSET:
            field_dict["lbnp_age_1pctn_m"] = lbnp_age_1pctn_m
        if lbnp_age_2 is not UNSET:
            field_dict["lbnp_age_2"] = lbnp_age_2
        if lbnp_age_2_f is not UNSET:
            field_dict["lbnp_age_2_f"] = lbnp_age_2_f
        if lbnp_age_2_m is not UNSET:
            field_dict["lbnp_age_2_m"] = lbnp_age_2_m
        if lbnp_age_2pctn is not UNSET:
            field_dict["lbnp_age_2pctn"] = lbnp_age_2pctn
        if lbnp_age_2pctn_f is not UNSET:
            field_dict["lbnp_age_2pctn_f"] = lbnp_age_2pctn_f
        if lbnp_age_2pctn_m is not UNSET:
            field_dict["lbnp_age_2pctn_m"] = lbnp_age_2pctn_m
        if lbnp_age_3 is not UNSET:
            field_dict["lbnp_age_3"] = lbnp_age_3
        if lbnp_age_3_f is not UNSET:
            field_dict["lbnp_age_3_f"] = lbnp_age_3_f
        if lbnp_age_3_m is not UNSET:
            field_dict["lbnp_age_3_m"] = lbnp_age_3_m
        if lbnp_age_3pctn is not UNSET:
            field_dict["lbnp_age_3pctn"] = lbnp_age_3pctn
        if lbnp_age_3pctn_f is not UNSET:
            field_dict["lbnp_age_3pctn_f"] = lbnp_age_3pctn_f
        if lbnp_age_3pctn_m is not UNSET:
            field_dict["lbnp_age_3pctn_m"] = lbnp_age_3pctn_m
        if lbnp_age_4 is not UNSET:
            field_dict["lbnp_age_4"] = lbnp_age_4
        if lbnp_age_4_f is not UNSET:
            field_dict["lbnp_age_4_f"] = lbnp_age_4_f
        if lbnp_age_4_m is not UNSET:
            field_dict["lbnp_age_4_m"] = lbnp_age_4_m
        if lbnp_age_4pctn is not UNSET:
            field_dict["lbnp_age_4pctn"] = lbnp_age_4pctn
        if lbnp_age_4pctn_f is not UNSET:
            field_dict["lbnp_age_4pctn_f"] = lbnp_age_4pctn_f
        if lbnp_age_4pctn_m is not UNSET:
            field_dict["lbnp_age_4pctn_m"] = lbnp_age_4pctn_m
        if lbnp_age_5 is not UNSET:
            field_dict["lbnp_age_5"] = lbnp_age_5
        if lbnp_age_5_f is not UNSET:
            field_dict["lbnp_age_5_f"] = lbnp_age_5_f
        if lbnp_age_5_m is not UNSET:
            field_dict["lbnp_age_5_m"] = lbnp_age_5_m
        if lbnp_age_5pctn is not UNSET:
            field_dict["lbnp_age_5pctn"] = lbnp_age_5pctn
        if lbnp_age_5pctn_f is not UNSET:
            field_dict["lbnp_age_5pctn_f"] = lbnp_age_5pctn_f
        if lbnp_age_5pctn_m is not UNSET:
            field_dict["lbnp_age_5pctn_m"] = lbnp_age_5pctn_m
        if lbnp_age_6 is not UNSET:
            field_dict["lbnp_age_6"] = lbnp_age_6
        if lbnp_age_6_f is not UNSET:
            field_dict["lbnp_age_6_f"] = lbnp_age_6_f
        if lbnp_age_6_m is not UNSET:
            field_dict["lbnp_age_6_m"] = lbnp_age_6_m
        if lbnp_age_6pctn is not UNSET:
            field_dict["lbnp_age_6pctn"] = lbnp_age_6pctn
        if lbnp_age_6pctn_f is not UNSET:
            field_dict["lbnp_age_6pctn_f"] = lbnp_age_6pctn_f
        if lbnp_age_6pctn_m is not UNSET:
            field_dict["lbnp_age_6pctn_m"] = lbnp_age_6pctn_m
        if lbnp_age_7 is not UNSET:
            field_dict["lbnp_age_7"] = lbnp_age_7
        if lbnp_age_7_f is not UNSET:
            field_dict["lbnp_age_7_f"] = lbnp_age_7_f
        if lbnp_age_7_m is not UNSET:
            field_dict["lbnp_age_7_m"] = lbnp_age_7_m
        if lbnp_age_7pctn is not UNSET:
            field_dict["lbnp_age_7pctn"] = lbnp_age_7pctn
        if lbnp_age_7pctn_f is not UNSET:
            field_dict["lbnp_age_7pctn_f"] = lbnp_age_7pctn_f
        if lbnp_age_7pctn_m is not UNSET:
            field_dict["lbnp_age_7pctn_m"] = lbnp_age_7pctn_m
        if lbnp_age_8 is not UNSET:
            field_dict["lbnp_age_8"] = lbnp_age_8
        if lbnp_age_8_f is not UNSET:
            field_dict["lbnp_age_8_f"] = lbnp_age_8_f
        if lbnp_age_8_m is not UNSET:
            field_dict["lbnp_age_8_m"] = lbnp_age_8_m
        if lbnp_age_8pctn is not UNSET:
            field_dict["lbnp_age_8pctn"] = lbnp_age_8pctn
        if lbnp_age_8pctn_f is not UNSET:
            field_dict["lbnp_age_8pctn_f"] = lbnp_age_8pctn_f
        if lbnp_age_8pctn_m is not UNSET:
            field_dict["lbnp_age_8pctn_m"] = lbnp_age_8pctn_m
        if lbnp_ea is not UNSET:
            field_dict["lbnp_ea"] = lbnp_ea
        if lbnp_ei is not UNSET:
            field_dict["lbnp_ei"] = lbnp_ei
        if lbnp_f is not UNSET:
            field_dict["lbnp_f"] = lbnp_f
        if lbnp_ftst is not UNSET:
            field_dict["lbnp_ftst"] = lbnp_ftst
        if lbnp_hm is not UNSET:
            field_dict["lbnp_hm"] = lbnp_hm
        if lbnp_m is not UNSET:
            field_dict["lbnp_m"] = lbnp_m
        if lbnp_ma_f is not UNSET:
            field_dict["lbnp_ma_f"] = lbnp_ma_f
        if lbnp_ma_f_xfdh is not UNSET:
            field_dict["lbnp_ma_f_xfdh"] = lbnp_ma_f_xfdh
        if lbnp_ma_m is not UNSET:
            field_dict["lbnp_ma_m"] = lbnp_ma_m
        if lbnp_ma_m_xfdh is not UNSET:
            field_dict["lbnp_ma_m_xfdh"] = lbnp_ma_m_xfdh
        if lbnp_ma_t is not UNSET:
            field_dict["lbnp_ma_t"] = lbnp_ma_t
        if lbnp_ma_t_xfdh is not UNSET:
            field_dict["lbnp_ma_t_xfdh"] = lbnp_ma_t_xfdh
        if lbnp_odr is not UNSET:
            field_dict["lbnp_odr"] = lbnp_odr
        if lbnp_odr_xfdh is not UNSET:
            field_dict["lbnp_odr_xfdh"] = lbnp_odr_xfdh
        if lbnp_oth is not UNSET:
            field_dict["lbnp_oth"] = lbnp_oth
        if lbnp_sr is not UNSET:
            field_dict["lbnp_sr"] = lbnp_sr
        if lbnp_sr_xfdh is not UNSET:
            field_dict["lbnp_sr_xfdh"] = lbnp_sr_xfdh
        if lf_age_1 is not UNSET:
            field_dict["lf_age_1"] = lf_age_1
        if lf_age_1_f is not UNSET:
            field_dict["lf_age_1_f"] = lf_age_1_f
        if lf_age_1_f_xfdh is not UNSET:
            field_dict["lf_age_1_f_xfdh"] = lf_age_1_f_xfdh
        if lf_age_1_m is not UNSET:
            field_dict["lf_age_1_m"] = lf_age_1_m
        if lf_age_1_m_xfdh is not UNSET:
            field_dict["lf_age_1_m_xfdh"] = lf_age_1_m_xfdh
        if lf_age_1_xfdh is not UNSET:
            field_dict["lf_age_1_xfdh"] = lf_age_1_xfdh
        if lf_age_2 is not UNSET:
            field_dict["lf_age_2"] = lf_age_2
        if lf_age_2_f is not UNSET:
            field_dict["lf_age_2_f"] = lf_age_2_f
        if lf_age_2_f_xfdh is not UNSET:
            field_dict["lf_age_2_f_xfdh"] = lf_age_2_f_xfdh
        if lf_age_2_m is not UNSET:
            field_dict["lf_age_2_m"] = lf_age_2_m
        if lf_age_2_m_xfdh is not UNSET:
            field_dict["lf_age_2_m_xfdh"] = lf_age_2_m_xfdh
        if lf_age_2_xfdh is not UNSET:
            field_dict["lf_age_2_xfdh"] = lf_age_2_xfdh
        if lf_age_3 is not UNSET:
            field_dict["lf_age_3"] = lf_age_3
        if lf_age_3_f is not UNSET:
            field_dict["lf_age_3_f"] = lf_age_3_f
        if lf_age_3_f_xfdh is not UNSET:
            field_dict["lf_age_3_f_xfdh"] = lf_age_3_f_xfdh
        if lf_age_3_m is not UNSET:
            field_dict["lf_age_3_m"] = lf_age_3_m
        if lf_age_3_m_xfdh is not UNSET:
            field_dict["lf_age_3_m_xfdh"] = lf_age_3_m_xfdh
        if lf_age_3_xfdh is not UNSET:
            field_dict["lf_age_3_xfdh"] = lf_age_3_xfdh
        if lf_age_4 is not UNSET:
            field_dict["lf_age_4"] = lf_age_4
        if lf_age_4_f is not UNSET:
            field_dict["lf_age_4_f"] = lf_age_4_f
        if lf_age_4_f_xfdh is not UNSET:
            field_dict["lf_age_4_f_xfdh"] = lf_age_4_f_xfdh
        if lf_age_4_m is not UNSET:
            field_dict["lf_age_4_m"] = lf_age_4_m
        if lf_age_4_m_xfdh is not UNSET:
            field_dict["lf_age_4_m_xfdh"] = lf_age_4_m_xfdh
        if lf_age_4_xfdh is not UNSET:
            field_dict["lf_age_4_xfdh"] = lf_age_4_xfdh
        if lf_age_5 is not UNSET:
            field_dict["lf_age_5"] = lf_age_5
        if lf_age_5_f is not UNSET:
            field_dict["lf_age_5_f"] = lf_age_5_f
        if lf_age_5_f_xfdh is not UNSET:
            field_dict["lf_age_5_f_xfdh"] = lf_age_5_f_xfdh
        if lf_age_5_m is not UNSET:
            field_dict["lf_age_5_m"] = lf_age_5_m
        if lf_age_5_m_xfdh is not UNSET:
            field_dict["lf_age_5_m_xfdh"] = lf_age_5_m_xfdh
        if lf_age_5_xfdh is not UNSET:
            field_dict["lf_age_5_xfdh"] = lf_age_5_xfdh
        if lf_age_6 is not UNSET:
            field_dict["lf_age_6"] = lf_age_6
        if lf_age_6_f is not UNSET:
            field_dict["lf_age_6_f"] = lf_age_6_f
        if lf_age_6_f_xfdh is not UNSET:
            field_dict["lf_age_6_f_xfdh"] = lf_age_6_f_xfdh
        if lf_age_6_m is not UNSET:
            field_dict["lf_age_6_m"] = lf_age_6_m
        if lf_age_6_m_xfdh is not UNSET:
            field_dict["lf_age_6_m_xfdh"] = lf_age_6_m_xfdh
        if lf_age_6_xfdh is not UNSET:
            field_dict["lf_age_6_xfdh"] = lf_age_6_xfdh
        if lf_f is not UNSET:
            field_dict["lf_f"] = lf_f
        if lf_f_xfdh is not UNSET:
            field_dict["lf_f_xfdh"] = lf_f_xfdh
        if lf_m is not UNSET:
            field_dict["lf_m"] = lf_m
        if lf_m_xfdh is not UNSET:
            field_dict["lf_m_xfdh"] = lf_m_xfdh
        if lf_ma_f is not UNSET:
            field_dict["lf_ma_f"] = lf_ma_f
        if lf_ma_f_xfdh is not UNSET:
            field_dict["lf_ma_f_xfdh"] = lf_ma_f_xfdh
        if lf_ma_m is not UNSET:
            field_dict["lf_ma_m"] = lf_ma_m
        if lf_ma_m_xfdh is not UNSET:
            field_dict["lf_ma_m_xfdh"] = lf_ma_m_xfdh
        if lf_ma_t is not UNSET:
            field_dict["lf_ma_t"] = lf_ma_t
        if lf_ma_t_xfdh is not UNSET:
            field_dict["lf_ma_t_xfdh"] = lf_ma_t_xfdh
        if lf_sr is not UNSET:
            field_dict["lf_sr"] = lf_sr
        if lf_sr_xfdh is not UNSET:
            field_dict["lf_sr_xfdh"] = lf_sr_xfdh
        if lfpr_age_1 is not UNSET:
            field_dict["lfpr_age_1"] = lfpr_age_1
        if lfpr_age_1_f is not UNSET:
            field_dict["lfpr_age_1_f"] = lfpr_age_1_f
        if lfpr_age_1_f_xfdh is not UNSET:
            field_dict["lfpr_age_1_f_xfdh"] = lfpr_age_1_f_xfdh
        if lfpr_age_1_m is not UNSET:
            field_dict["lfpr_age_1_m"] = lfpr_age_1_m
        if lfpr_age_1_m_xfdh is not UNSET:
            field_dict["lfpr_age_1_m_xfdh"] = lfpr_age_1_m_xfdh
        if lfpr_age_1_xfdh is not UNSET:
            field_dict["lfpr_age_1_xfdh"] = lfpr_age_1_xfdh
        if lfpr_age_2 is not UNSET:
            field_dict["lfpr_age_2"] = lfpr_age_2
        if lfpr_age_2_f is not UNSET:
            field_dict["lfpr_age_2_f"] = lfpr_age_2_f
        if lfpr_age_2_f_xfdh is not UNSET:
            field_dict["lfpr_age_2_f_xfdh"] = lfpr_age_2_f_xfdh
        if lfpr_age_2_m is not UNSET:
            field_dict["lfpr_age_2_m"] = lfpr_age_2_m
        if lfpr_age_2_m_xfdh is not UNSET:
            field_dict["lfpr_age_2_m_xfdh"] = lfpr_age_2_m_xfdh
        if lfpr_age_2_xfdh is not UNSET:
            field_dict["lfpr_age_2_xfdh"] = lfpr_age_2_xfdh
        if lfpr_age_3 is not UNSET:
            field_dict["lfpr_age_3"] = lfpr_age_3
        if lfpr_age_3_f is not UNSET:
            field_dict["lfpr_age_3_f"] = lfpr_age_3_f
        if lfpr_age_3_f_xfdh is not UNSET:
            field_dict["lfpr_age_3_f_xfdh"] = lfpr_age_3_f_xfdh
        if lfpr_age_3_m is not UNSET:
            field_dict["lfpr_age_3_m"] = lfpr_age_3_m
        if lfpr_age_3_m_xfdh is not UNSET:
            field_dict["lfpr_age_3_m_xfdh"] = lfpr_age_3_m_xfdh
        if lfpr_age_3_xfdh is not UNSET:
            field_dict["lfpr_age_3_xfdh"] = lfpr_age_3_xfdh
        if lfpr_age_4 is not UNSET:
            field_dict["lfpr_age_4"] = lfpr_age_4
        if lfpr_age_4_f is not UNSET:
            field_dict["lfpr_age_4_f"] = lfpr_age_4_f
        if lfpr_age_4_f_xfdh is not UNSET:
            field_dict["lfpr_age_4_f_xfdh"] = lfpr_age_4_f_xfdh
        if lfpr_age_4_m is not UNSET:
            field_dict["lfpr_age_4_m"] = lfpr_age_4_m
        if lfpr_age_4_m_xfdh is not UNSET:
            field_dict["lfpr_age_4_m_xfdh"] = lfpr_age_4_m_xfdh
        if lfpr_age_4_xfdh is not UNSET:
            field_dict["lfpr_age_4_xfdh"] = lfpr_age_4_xfdh
        if lfpr_age_5 is not UNSET:
            field_dict["lfpr_age_5"] = lfpr_age_5
        if lfpr_age_5_f is not UNSET:
            field_dict["lfpr_age_5_f"] = lfpr_age_5_f
        if lfpr_age_5_f_xfdh is not UNSET:
            field_dict["lfpr_age_5_f_xfdh"] = lfpr_age_5_f_xfdh
        if lfpr_age_5_m is not UNSET:
            field_dict["lfpr_age_5_m"] = lfpr_age_5_m
        if lfpr_age_5_m_xfdh is not UNSET:
            field_dict["lfpr_age_5_m_xfdh"] = lfpr_age_5_m_xfdh
        if lfpr_age_5_xfdh is not UNSET:
            field_dict["lfpr_age_5_xfdh"] = lfpr_age_5_xfdh
        if lfpr_age_6 is not UNSET:
            field_dict["lfpr_age_6"] = lfpr_age_6
        if lfpr_age_6_f is not UNSET:
            field_dict["lfpr_age_6_f"] = lfpr_age_6_f
        if lfpr_age_6_f_xfdh is not UNSET:
            field_dict["lfpr_age_6_f_xfdh"] = lfpr_age_6_f_xfdh
        if lfpr_age_6_m is not UNSET:
            field_dict["lfpr_age_6_m"] = lfpr_age_6_m
        if lfpr_age_6_m_xfdh is not UNSET:
            field_dict["lfpr_age_6_m_xfdh"] = lfpr_age_6_m_xfdh
        if lfpr_age_6_xfdh is not UNSET:
            field_dict["lfpr_age_6_xfdh"] = lfpr_age_6_xfdh
        if lfpr_f is not UNSET:
            field_dict["lfpr_f"] = lfpr_f
        if lfpr_f_xfdh is not UNSET:
            field_dict["lfpr_f_xfdh"] = lfpr_f_xfdh
        if lfpr_m is not UNSET:
            field_dict["lfpr_m"] = lfpr_m
        if lfpr_m_xfdh is not UNSET:
            field_dict["lfpr_m_xfdh"] = lfpr_m_xfdh
        if ma_econhh is not UNSET:
            field_dict["ma_econhh"] = ma_econhh
        if ma_econhh_xfdh is not UNSET:
            field_dict["ma_econhh_xfdh"] = ma_econhh_xfdh
        if ma_hh is not UNSET:
            field_dict["ma_hh"] = ma_hh
        if my_lp is not UNSET:
            field_dict["my_lp"] = my_lp
        if t_lbnp is not UNSET:
            field_dict["t_lbnp"] = t_lbnp
        if t_lbnp15 is not UNSET:
            field_dict["t_lbnp15"] = t_lbnp15
        if t_lf is not UNSET:
            field_dict["t_lf"] = t_lf
        if t_lf_xfdh is not UNSET:
            field_dict["t_lf_xfdh"] = t_lf_xfdh
        if t_lfpr is not UNSET:
            field_dict["t_lfpr"] = t_lfpr
        if t_lfpr_xfdh is not UNSET:
            field_dict["t_lfpr_xfdh"] = t_lfpr_xfdh
        if year is not UNSET:
            field_dict["year"] = year
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

        def _parse_adhz(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        adhz = _parse_adhz(d.pop("adhz", UNSET))

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

        def _parse_dh_ea(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_ea = _parse_dh_ea(d.pop("dh_ea", UNSET))

        def _parse_dh_ei(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dh_ei = _parse_dh_ei(d.pop("dh_ei", UNSET))

        def _parse_dha_oth(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dha_oth = _parse_dha_oth(d.pop("dha_oth", UNSET))

        def _parse_dha_othpctn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dha_othpctn = _parse_dha_othpctn(d.pop("dha_othpctn", UNSET))

        def _parse_dha_wf(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dha_wf = _parse_dha_wf(d.pop("dha_wf", UNSET))

        def _parse_dha_wfpctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dha_wfpctn = _parse_dha_wfpctn(d.pop("dha_wfpctn", UNSET))

        def _parse_dhi_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_1 = _parse_dhi_1(d.pop("dhi_1", UNSET))

        def _parse_dhi_1pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_1pctn = _parse_dhi_1pctn(d.pop("dhi_1pctn", UNSET))

        def _parse_dhi_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_2 = _parse_dhi_2(d.pop("dhi_2", UNSET))

        def _parse_dhi_2pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_2pctn = _parse_dhi_2pctn(d.pop("dhi_2pctn", UNSET))

        def _parse_dhi_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_3 = _parse_dhi_3(d.pop("dhi_3", UNSET))

        def _parse_dhi_3pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_3pctn = _parse_dhi_3pctn(d.pop("dhi_3pctn", UNSET))

        def _parse_dhi_e1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e1 = _parse_dhi_e1(d.pop("dhi_e1", UNSET))

        def _parse_dhi_e1pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e1pctn = _parse_dhi_e1pctn(d.pop("dhi_e1pctn", UNSET))

        def _parse_dhi_e2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e2 = _parse_dhi_e2(d.pop("dhi_e2", UNSET))

        def _parse_dhi_e2pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e2pctn = _parse_dhi_e2pctn(d.pop("dhi_e2pctn", UNSET))

        def _parse_dhi_e3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e3 = _parse_dhi_e3(d.pop("dhi_e3", UNSET))

        def _parse_dhi_e3pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhi_e3pctn = _parse_dhi_e3pctn(d.pop("dhi_e3pctn", UNSET))

        def _parse_dht_oo(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dht_oo = _parse_dht_oo(d.pop("dht_oo", UNSET))

        def _parse_dht_oopctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dht_oopctn = _parse_dht_oopctn(d.pop("dht_oopctn", UNSET))

        def _parse_dht_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dht_oth = _parse_dht_oth(d.pop("dht_oth", UNSET))

        def _parse_dht_othpctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dht_othpctn = _parse_dht_othpctn(d.pop("dht_othpctn", UNSET))

        def _parse_dht_st(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dht_st = _parse_dht_st(d.pop("dht_st", UNSET))

        def _parse_dht_stpctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dht_stpctn = _parse_dht_stpctn(d.pop("dht_stpctn", UNSET))

        def _parse_dhz_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_1 = _parse_dhz_1(d.pop("dhz_1", UNSET))

        def _parse_dhz_1pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_1pctn = _parse_dhz_1pctn(d.pop("dhz_1pctn", UNSET))

        def _parse_dhz_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_2 = _parse_dhz_2(d.pop("dhz_2", UNSET))

        def _parse_dhz_2pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_2pctn = _parse_dhz_2pctn(d.pop("dhz_2pctn", UNSET))

        def _parse_dhz_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_3 = _parse_dhz_3(d.pop("dhz_3", UNSET))

        def _parse_dhz_3pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_3pctn = _parse_dhz_3pctn(d.pop("dhz_3pctn", UNSET))

        def _parse_dhz_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_4 = _parse_dhz_4(d.pop("dhz_4", UNSET))

        def _parse_dhz_4pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_4pctn = _parse_dhz_4pctn(d.pop("dhz_4pctn", UNSET))

        def _parse_dhz_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_5 = _parse_dhz_5(d.pop("dhz_5", UNSET))

        def _parse_dhz_5_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_5_6 = _parse_dhz_5_6(d.pop("dhz_5_6", UNSET))

        def _parse_dhz_5_6pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_5_6pctn = _parse_dhz_5_6pctn(d.pop("dhz_5_6pctn", UNSET))

        def _parse_dhz_5pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_5pctn = _parse_dhz_5pctn(d.pop("dhz_5pctn", UNSET))

        def _parse_dhz_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_6 = _parse_dhz_6(d.pop("dhz_6", UNSET))

        def _parse_dhz_6pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dhz_6pctn = _parse_dhz_6pctn(d.pop("dhz_6pctn", UNSET))

        def _parse_lbnp15_edu_age_1pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_age_1pctn = _parse_lbnp15_edu_age_1pctn(
            d.pop("lbnp15_edu_age_1pctn", UNSET)
        )

        def _parse_lbnp15_edu_age_2pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_age_2pctn = _parse_lbnp15_edu_age_2pctn(
            d.pop("lbnp15_edu_age_2pctn", UNSET)
        )

        def _parse_lbnp15_edu_age_3pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_age_3pctn = _parse_lbnp15_edu_age_3pctn(
            d.pop("lbnp15_edu_age_3pctn", UNSET)
        )

        def _parse_lbnp15_edu_age_4pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_age_4pctn = _parse_lbnp15_edu_age_4pctn(
            d.pop("lbnp15_edu_age_4pctn", UNSET)
        )

        def _parse_lbnp15_edu_age_5pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_age_5pctn = _parse_lbnp15_edu_age_5pctn(
            d.pop("lbnp15_edu_age_5pctn", UNSET)
        )

        def _parse_lbnp15_edu_age_6pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_age_6pctn = _parse_lbnp15_edu_age_6pctn(
            d.pop("lbnp15_edu_age_6pctn", UNSET)
        )

        def _parse_lbnp15_edu_age_7pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_age_7pctn = _parse_lbnp15_edu_age_7pctn(
            d.pop("lbnp15_edu_age_7pctn", UNSET)
        )

        def _parse_lbnp15_edu_age_8pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_age_8pctn = _parse_lbnp15_edu_age_8pctn(
            d.pop("lbnp15_edu_age_8pctn", UNSET)
        )

        def _parse_lbnp15_edu_deg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_deg = _parse_lbnp15_edu_deg(d.pop("lbnp15_edu_deg", UNSET))

        def _parse_lbnp15_edu_deg_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_deg_f = _parse_lbnp15_edu_deg_f(d.pop("lbnp15_edu_deg_f", UNSET))

        def _parse_lbnp15_edu_deg_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_deg_m = _parse_lbnp15_edu_deg_m(d.pop("lbnp15_edu_deg_m", UNSET))

        def _parse_lbnp15_edu_deg_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_deg_pctn = _parse_lbnp15_edu_deg_pctn(
            d.pop("lbnp15_edu_deg_pctn", UNSET)
        )

        def _parse_lbnp15_edu_deg_pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_deg_pctn_f = _parse_lbnp15_edu_deg_pctn_f(
            d.pop("lbnp15_edu_deg_pctn_f", UNSET)
        )

        def _parse_lbnp15_edu_deg_pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_deg_pctn_m = _parse_lbnp15_edu_deg_pctn_m(
            d.pop("lbnp15_edu_deg_pctn_m", UNSET)
        )

        def _parse_lbnp15_edu_lsed(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_lsed = _parse_lbnp15_edu_lsed(d.pop("lbnp15_edu_lsed", UNSET))

        def _parse_lbnp15_edu_lsed_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_lsed_f = _parse_lbnp15_edu_lsed_f(d.pop("lbnp15_edu_lsed_f", UNSET))

        def _parse_lbnp15_edu_lsed_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_lsed_m = _parse_lbnp15_edu_lsed_m(d.pop("lbnp15_edu_lsed_m", UNSET))

        def _parse_lbnp15_edu_lsed_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_lsed_pctn = _parse_lbnp15_edu_lsed_pctn(
            d.pop("lbnp15_edu_lsed_pctn", UNSET)
        )

        def _parse_lbnp15_edu_lsed_pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_lsed_pctn_f = _parse_lbnp15_edu_lsed_pctn_f(
            d.pop("lbnp15_edu_lsed_pctn_f", UNSET)
        )

        def _parse_lbnp15_edu_lsed_pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_lsed_pctn_m = _parse_lbnp15_edu_lsed_pctn_m(
            d.pop("lbnp15_edu_lsed_pctn_m", UNSET)
        )

        def _parse_lbnp15_edu_ndeg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_ndeg = _parse_lbnp15_edu_ndeg(d.pop("lbnp15_edu_ndeg", UNSET))

        def _parse_lbnp15_edu_ndeg_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_ndeg_f = _parse_lbnp15_edu_ndeg_f(d.pop("lbnp15_edu_ndeg_f", UNSET))

        def _parse_lbnp15_edu_ndeg_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_ndeg_m = _parse_lbnp15_edu_ndeg_m(d.pop("lbnp15_edu_ndeg_m", UNSET))

        def _parse_lbnp15_edu_ndeg_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_ndeg_pctn = _parse_lbnp15_edu_ndeg_pctn(
            d.pop("lbnp15_edu_ndeg_pctn", UNSET)
        )

        def _parse_lbnp15_edu_ndeg_pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_ndeg_pctn_f = _parse_lbnp15_edu_ndeg_pctn_f(
            d.pop("lbnp15_edu_ndeg_pctn_f", UNSET)
        )

        def _parse_lbnp15_edu_ndeg_pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_ndeg_pctn_m = _parse_lbnp15_edu_ndeg_pctn_m(
            d.pop("lbnp15_edu_ndeg_pctn_m", UNSET)
        )

        def _parse_lbnp15_edu_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_pctn = _parse_lbnp15_edu_pctn(d.pop("lbnp15_edu_pctn", UNSET))

        def _parse_lbnp15_edu_prepri(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_prepri = _parse_lbnp15_edu_prepri(d.pop("lbnp15_edu_prepri", UNSET))

        def _parse_lbnp15_edu_prepri_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_prepri_f = _parse_lbnp15_edu_prepri_f(
            d.pop("lbnp15_edu_prepri_f", UNSET)
        )

        def _parse_lbnp15_edu_prepri_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_prepri_m = _parse_lbnp15_edu_prepri_m(
            d.pop("lbnp15_edu_prepri_m", UNSET)
        )

        def _parse_lbnp15_edu_prepri_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_prepri_pctn = _parse_lbnp15_edu_prepri_pctn(
            d.pop("lbnp15_edu_prepri_pctn", UNSET)
        )

        def _parse_lbnp15_edu_prepri_pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_prepri_pctn_f = _parse_lbnp15_edu_prepri_pctn_f(
            d.pop("lbnp15_edu_prepri_pctn_f", UNSET)
        )

        def _parse_lbnp15_edu_prepri_pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_prepri_pctn_m = _parse_lbnp15_edu_prepri_pctn_m(
            d.pop("lbnp15_edu_prepri_pctn_m", UNSET)
        )

        def _parse_lbnp15_edu_psec(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_psec = _parse_lbnp15_edu_psec(d.pop("lbnp15_edu_psec", UNSET))

        def _parse_lbnp15_edu_psec_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_psec_f = _parse_lbnp15_edu_psec_f(d.pop("lbnp15_edu_psec_f", UNSET))

        def _parse_lbnp15_edu_psec_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_psec_m = _parse_lbnp15_edu_psec_m(d.pop("lbnp15_edu_psec_m", UNSET))

        def _parse_lbnp15_edu_psec_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_psec_pctn = _parse_lbnp15_edu_psec_pctn(
            d.pop("lbnp15_edu_psec_pctn", UNSET)
        )

        def _parse_lbnp15_edu_psec_pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_psec_pctn_f = _parse_lbnp15_edu_psec_pctn_f(
            d.pop("lbnp15_edu_psec_pctn_f", UNSET)
        )

        def _parse_lbnp15_edu_psec_pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_psec_pctn_m = _parse_lbnp15_edu_psec_pctn_m(
            d.pop("lbnp15_edu_psec_pctn_m", UNSET)
        )

        def _parse_lbnp15_edu_usec(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_usec = _parse_lbnp15_edu_usec(d.pop("lbnp15_edu_usec", UNSET))

        def _parse_lbnp15_edu_usec_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_usec_f = _parse_lbnp15_edu_usec_f(d.pop("lbnp15_edu_usec_f", UNSET))

        def _parse_lbnp15_edu_usec_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_usec_m = _parse_lbnp15_edu_usec_m(d.pop("lbnp15_edu_usec_m", UNSET))

        def _parse_lbnp15_edu_usec_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_usec_pctn = _parse_lbnp15_edu_usec_pctn(
            d.pop("lbnp15_edu_usec_pctn", UNSET)
        )

        def _parse_lbnp15_edu_usec_pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_usec_pctn_f = _parse_lbnp15_edu_usec_pctn_f(
            d.pop("lbnp15_edu_usec_pctn_f", UNSET)
        )

        def _parse_lbnp15_edu_usec_pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_edu_usec_pctn_m = _parse_lbnp15_edu_usec_pctn_m(
            d.pop("lbnp15_edu_usec_pctn_m", UNSET)
        )

        def _parse_lbnp15_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_f = _parse_lbnp15_f(d.pop("lbnp15_f", UNSET))

        def _parse_lbnp15_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_m = _parse_lbnp15_m(d.pop("lbnp15_m", UNSET))

        def _parse_lbnp15_ms_divsep(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_divsep = _parse_lbnp15_ms_divsep(d.pop("lbnp15_ms_divsep", UNSET))

        def _parse_lbnp15_ms_divsep_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_divsep_f = _parse_lbnp15_ms_divsep_f(
            d.pop("lbnp15_ms_divsep_f", UNSET)
        )

        def _parse_lbnp15_ms_divsep_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_divsep_m = _parse_lbnp15_ms_divsep_m(
            d.pop("lbnp15_ms_divsep_m", UNSET)
        )

        def _parse_lbnp15_ms_divsep_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_divsep_pctn = _parse_lbnp15_ms_divsep_pctn(
            d.pop("lbnp15_ms_divsep_pctn", UNSET)
        )

        def _parse_lbnp15_ms_divsep_pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_divsep_pctn_f = _parse_lbnp15_ms_divsep_pctn_f(
            d.pop("lbnp15_ms_divsep_pctn_f", UNSET)
        )

        def _parse_lbnp15_ms_divsep_pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_divsep_pctn_m = _parse_lbnp15_ms_divsep_pctn_m(
            d.pop("lbnp15_ms_divsep_pctn_m", UNSET)
        )

        def _parse_lbnp15_ms_ma(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_ma = _parse_lbnp15_ms_ma(d.pop("lbnp15_ms_ma", UNSET))

        def _parse_lbnp15_ms_ma_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_ma_f = _parse_lbnp15_ms_ma_f(d.pop("lbnp15_ms_ma_f", UNSET))

        def _parse_lbnp15_ms_ma_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_ma_m = _parse_lbnp15_ms_ma_m(d.pop("lbnp15_ms_ma_m", UNSET))

        def _parse_lbnp15_ms_ma_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_ma_pctn = _parse_lbnp15_ms_ma_pctn(d.pop("lbnp15_ms_ma_pctn", UNSET))

        def _parse_lbnp15_ms_ma_pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_ma_pctn_f = _parse_lbnp15_ms_ma_pctn_f(
            d.pop("lbnp15_ms_ma_pctn_f", UNSET)
        )

        def _parse_lbnp15_ms_ma_pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_ma_pctn_m = _parse_lbnp15_ms_ma_pctn_m(
            d.pop("lbnp15_ms_ma_pctn_m", UNSET)
        )

        def _parse_lbnp15_ms_nm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_nm = _parse_lbnp15_ms_nm(d.pop("lbnp15_ms_nm", UNSET))

        def _parse_lbnp15_ms_nm_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_nm_f = _parse_lbnp15_ms_nm_f(d.pop("lbnp15_ms_nm_f", UNSET))

        def _parse_lbnp15_ms_nm_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_nm_m = _parse_lbnp15_ms_nm_m(d.pop("lbnp15_ms_nm_m", UNSET))

        def _parse_lbnp15_ms_nm_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_nm_pctn = _parse_lbnp15_ms_nm_pctn(d.pop("lbnp15_ms_nm_pctn", UNSET))

        def _parse_lbnp15_ms_nm_pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_nm_pctn_f = _parse_lbnp15_ms_nm_pctn_f(
            d.pop("lbnp15_ms_nm_pctn_f", UNSET)
        )

        def _parse_lbnp15_ms_nm_pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_nm_pctn_m = _parse_lbnp15_ms_nm_pctn_m(
            d.pop("lbnp15_ms_nm_pctn_m", UNSET)
        )

        def _parse_lbnp15_ms_win(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_win = _parse_lbnp15_ms_win(d.pop("lbnp15_ms_win", UNSET))

        def _parse_lbnp15_ms_win_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_win_f = _parse_lbnp15_ms_win_f(d.pop("lbnp15_ms_win_f", UNSET))

        def _parse_lbnp15_ms_win_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_win_m = _parse_lbnp15_ms_win_m(d.pop("lbnp15_ms_win_m", UNSET))

        def _parse_lbnp15_ms_win_pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_win_pctn = _parse_lbnp15_ms_win_pctn(
            d.pop("lbnp15_ms_win_pctn", UNSET)
        )

        def _parse_lbnp15_ms_win_pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_win_pctn_f = _parse_lbnp15_ms_win_pctn_f(
            d.pop("lbnp15_ms_win_pctn_f", UNSET)
        )

        def _parse_lbnp15_ms_win_pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp15_ms_win_pctn_m = _parse_lbnp15_ms_win_pctn_m(
            d.pop("lbnp15_ms_win_pctn_m", UNSET)
        )

        def _parse_lbnp_act_eapctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_act_eapctn = _parse_lbnp_act_eapctn(d.pop("lbnp_act_eapctn", UNSET))

        def _parse_lbnp_act_eipctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_act_eipctn = _parse_lbnp_act_eipctn(d.pop("lbnp_act_eipctn", UNSET))

        def _parse_lbnp_act_ftstpctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_act_ftstpctn = _parse_lbnp_act_ftstpctn(d.pop("lbnp_act_ftstpctn", UNSET))

        def _parse_lbnp_act_hmpctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_act_hmpctn = _parse_lbnp_act_hmpctn(d.pop("lbnp_act_hmpctn", UNSET))

        def _parse_lbnp_act_othpctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_act_othpctn = _parse_lbnp_act_othpctn(d.pop("lbnp_act_othpctn", UNSET))

        def _parse_lbnp_age_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_1 = _parse_lbnp_age_1(d.pop("lbnp_age_1", UNSET))

        def _parse_lbnp_age_1_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_1_f = _parse_lbnp_age_1_f(d.pop("lbnp_age_1_f", UNSET))

        def _parse_lbnp_age_1_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_1_m = _parse_lbnp_age_1_m(d.pop("lbnp_age_1_m", UNSET))

        def _parse_lbnp_age_1pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_1pctn = _parse_lbnp_age_1pctn(d.pop("lbnp_age_1pctn", UNSET))

        def _parse_lbnp_age_1pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_1pctn_f = _parse_lbnp_age_1pctn_f(d.pop("lbnp_age_1pctn_f", UNSET))

        def _parse_lbnp_age_1pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_1pctn_m = _parse_lbnp_age_1pctn_m(d.pop("lbnp_age_1pctn_m", UNSET))

        def _parse_lbnp_age_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_2 = _parse_lbnp_age_2(d.pop("lbnp_age_2", UNSET))

        def _parse_lbnp_age_2_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_2_f = _parse_lbnp_age_2_f(d.pop("lbnp_age_2_f", UNSET))

        def _parse_lbnp_age_2_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_2_m = _parse_lbnp_age_2_m(d.pop("lbnp_age_2_m", UNSET))

        def _parse_lbnp_age_2pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_2pctn = _parse_lbnp_age_2pctn(d.pop("lbnp_age_2pctn", UNSET))

        def _parse_lbnp_age_2pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_2pctn_f = _parse_lbnp_age_2pctn_f(d.pop("lbnp_age_2pctn_f", UNSET))

        def _parse_lbnp_age_2pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_2pctn_m = _parse_lbnp_age_2pctn_m(d.pop("lbnp_age_2pctn_m", UNSET))

        def _parse_lbnp_age_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_3 = _parse_lbnp_age_3(d.pop("lbnp_age_3", UNSET))

        def _parse_lbnp_age_3_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_3_f = _parse_lbnp_age_3_f(d.pop("lbnp_age_3_f", UNSET))

        def _parse_lbnp_age_3_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_3_m = _parse_lbnp_age_3_m(d.pop("lbnp_age_3_m", UNSET))

        def _parse_lbnp_age_3pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_3pctn = _parse_lbnp_age_3pctn(d.pop("lbnp_age_3pctn", UNSET))

        def _parse_lbnp_age_3pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_3pctn_f = _parse_lbnp_age_3pctn_f(d.pop("lbnp_age_3pctn_f", UNSET))

        def _parse_lbnp_age_3pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_3pctn_m = _parse_lbnp_age_3pctn_m(d.pop("lbnp_age_3pctn_m", UNSET))

        def _parse_lbnp_age_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_4 = _parse_lbnp_age_4(d.pop("lbnp_age_4", UNSET))

        def _parse_lbnp_age_4_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_4_f = _parse_lbnp_age_4_f(d.pop("lbnp_age_4_f", UNSET))

        def _parse_lbnp_age_4_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_4_m = _parse_lbnp_age_4_m(d.pop("lbnp_age_4_m", UNSET))

        def _parse_lbnp_age_4pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_4pctn = _parse_lbnp_age_4pctn(d.pop("lbnp_age_4pctn", UNSET))

        def _parse_lbnp_age_4pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_4pctn_f = _parse_lbnp_age_4pctn_f(d.pop("lbnp_age_4pctn_f", UNSET))

        def _parse_lbnp_age_4pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_4pctn_m = _parse_lbnp_age_4pctn_m(d.pop("lbnp_age_4pctn_m", UNSET))

        def _parse_lbnp_age_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_5 = _parse_lbnp_age_5(d.pop("lbnp_age_5", UNSET))

        def _parse_lbnp_age_5_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_5_f = _parse_lbnp_age_5_f(d.pop("lbnp_age_5_f", UNSET))

        def _parse_lbnp_age_5_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_5_m = _parse_lbnp_age_5_m(d.pop("lbnp_age_5_m", UNSET))

        def _parse_lbnp_age_5pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_5pctn = _parse_lbnp_age_5pctn(d.pop("lbnp_age_5pctn", UNSET))

        def _parse_lbnp_age_5pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_5pctn_f = _parse_lbnp_age_5pctn_f(d.pop("lbnp_age_5pctn_f", UNSET))

        def _parse_lbnp_age_5pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_5pctn_m = _parse_lbnp_age_5pctn_m(d.pop("lbnp_age_5pctn_m", UNSET))

        def _parse_lbnp_age_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_6 = _parse_lbnp_age_6(d.pop("lbnp_age_6", UNSET))

        def _parse_lbnp_age_6_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_6_f = _parse_lbnp_age_6_f(d.pop("lbnp_age_6_f", UNSET))

        def _parse_lbnp_age_6_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_6_m = _parse_lbnp_age_6_m(d.pop("lbnp_age_6_m", UNSET))

        def _parse_lbnp_age_6pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_6pctn = _parse_lbnp_age_6pctn(d.pop("lbnp_age_6pctn", UNSET))

        def _parse_lbnp_age_6pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_6pctn_f = _parse_lbnp_age_6pctn_f(d.pop("lbnp_age_6pctn_f", UNSET))

        def _parse_lbnp_age_6pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_6pctn_m = _parse_lbnp_age_6pctn_m(d.pop("lbnp_age_6pctn_m", UNSET))

        def _parse_lbnp_age_7(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_7 = _parse_lbnp_age_7(d.pop("lbnp_age_7", UNSET))

        def _parse_lbnp_age_7_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_7_f = _parse_lbnp_age_7_f(d.pop("lbnp_age_7_f", UNSET))

        def _parse_lbnp_age_7_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_7_m = _parse_lbnp_age_7_m(d.pop("lbnp_age_7_m", UNSET))

        def _parse_lbnp_age_7pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_7pctn = _parse_lbnp_age_7pctn(d.pop("lbnp_age_7pctn", UNSET))

        def _parse_lbnp_age_7pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_7pctn_f = _parse_lbnp_age_7pctn_f(d.pop("lbnp_age_7pctn_f", UNSET))

        def _parse_lbnp_age_7pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_7pctn_m = _parse_lbnp_age_7pctn_m(d.pop("lbnp_age_7pctn_m", UNSET))

        def _parse_lbnp_age_8(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_8 = _parse_lbnp_age_8(d.pop("lbnp_age_8", UNSET))

        def _parse_lbnp_age_8_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_8_f = _parse_lbnp_age_8_f(d.pop("lbnp_age_8_f", UNSET))

        def _parse_lbnp_age_8_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_8_m = _parse_lbnp_age_8_m(d.pop("lbnp_age_8_m", UNSET))

        def _parse_lbnp_age_8pctn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_8pctn = _parse_lbnp_age_8pctn(d.pop("lbnp_age_8pctn", UNSET))

        def _parse_lbnp_age_8pctn_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_8pctn_f = _parse_lbnp_age_8pctn_f(d.pop("lbnp_age_8pctn_f", UNSET))

        def _parse_lbnp_age_8pctn_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_age_8pctn_m = _parse_lbnp_age_8pctn_m(d.pop("lbnp_age_8pctn_m", UNSET))

        def _parse_lbnp_ea(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_ea = _parse_lbnp_ea(d.pop("lbnp_ea", UNSET))

        def _parse_lbnp_ei(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_ei = _parse_lbnp_ei(d.pop("lbnp_ei", UNSET))

        def _parse_lbnp_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_f = _parse_lbnp_f(d.pop("lbnp_f", UNSET))

        def _parse_lbnp_ftst(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_ftst = _parse_lbnp_ftst(d.pop("lbnp_ftst", UNSET))

        def _parse_lbnp_hm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_hm = _parse_lbnp_hm(d.pop("lbnp_hm", UNSET))

        def _parse_lbnp_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_m = _parse_lbnp_m(d.pop("lbnp_m", UNSET))

        def _parse_lbnp_ma_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_ma_f = _parse_lbnp_ma_f(d.pop("lbnp_ma_f", UNSET))

        def _parse_lbnp_ma_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_ma_f_xfdh = _parse_lbnp_ma_f_xfdh(d.pop("lbnp_ma_f_xfdh", UNSET))

        def _parse_lbnp_ma_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_ma_m = _parse_lbnp_ma_m(d.pop("lbnp_ma_m", UNSET))

        def _parse_lbnp_ma_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_ma_m_xfdh = _parse_lbnp_ma_m_xfdh(d.pop("lbnp_ma_m_xfdh", UNSET))

        def _parse_lbnp_ma_t(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_ma_t = _parse_lbnp_ma_t(d.pop("lbnp_ma_t", UNSET))

        def _parse_lbnp_ma_t_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_ma_t_xfdh = _parse_lbnp_ma_t_xfdh(d.pop("lbnp_ma_t_xfdh", UNSET))

        def _parse_lbnp_odr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_odr = _parse_lbnp_odr(d.pop("lbnp_odr", UNSET))

        def _parse_lbnp_odr_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_odr_xfdh = _parse_lbnp_odr_xfdh(d.pop("lbnp_odr_xfdh", UNSET))

        def _parse_lbnp_oth(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_oth = _parse_lbnp_oth(d.pop("lbnp_oth", UNSET))

        def _parse_lbnp_sr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_sr = _parse_lbnp_sr(d.pop("lbnp_sr", UNSET))

        def _parse_lbnp_sr_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lbnp_sr_xfdh = _parse_lbnp_sr_xfdh(d.pop("lbnp_sr_xfdh", UNSET))

        def _parse_lf_age_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_1 = _parse_lf_age_1(d.pop("lf_age_1", UNSET))

        def _parse_lf_age_1_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_1_f = _parse_lf_age_1_f(d.pop("lf_age_1_f", UNSET))

        def _parse_lf_age_1_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_1_f_xfdh = _parse_lf_age_1_f_xfdh(d.pop("lf_age_1_f_xfdh", UNSET))

        def _parse_lf_age_1_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_1_m = _parse_lf_age_1_m(d.pop("lf_age_1_m", UNSET))

        def _parse_lf_age_1_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_1_m_xfdh = _parse_lf_age_1_m_xfdh(d.pop("lf_age_1_m_xfdh", UNSET))

        def _parse_lf_age_1_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_1_xfdh = _parse_lf_age_1_xfdh(d.pop("lf_age_1_xfdh", UNSET))

        def _parse_lf_age_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_2 = _parse_lf_age_2(d.pop("lf_age_2", UNSET))

        def _parse_lf_age_2_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_2_f = _parse_lf_age_2_f(d.pop("lf_age_2_f", UNSET))

        def _parse_lf_age_2_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_2_f_xfdh = _parse_lf_age_2_f_xfdh(d.pop("lf_age_2_f_xfdh", UNSET))

        def _parse_lf_age_2_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_2_m = _parse_lf_age_2_m(d.pop("lf_age_2_m", UNSET))

        def _parse_lf_age_2_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_2_m_xfdh = _parse_lf_age_2_m_xfdh(d.pop("lf_age_2_m_xfdh", UNSET))

        def _parse_lf_age_2_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_2_xfdh = _parse_lf_age_2_xfdh(d.pop("lf_age_2_xfdh", UNSET))

        def _parse_lf_age_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_3 = _parse_lf_age_3(d.pop("lf_age_3", UNSET))

        def _parse_lf_age_3_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_3_f = _parse_lf_age_3_f(d.pop("lf_age_3_f", UNSET))

        def _parse_lf_age_3_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_3_f_xfdh = _parse_lf_age_3_f_xfdh(d.pop("lf_age_3_f_xfdh", UNSET))

        def _parse_lf_age_3_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_3_m = _parse_lf_age_3_m(d.pop("lf_age_3_m", UNSET))

        def _parse_lf_age_3_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_3_m_xfdh = _parse_lf_age_3_m_xfdh(d.pop("lf_age_3_m_xfdh", UNSET))

        def _parse_lf_age_3_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_3_xfdh = _parse_lf_age_3_xfdh(d.pop("lf_age_3_xfdh", UNSET))

        def _parse_lf_age_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_4 = _parse_lf_age_4(d.pop("lf_age_4", UNSET))

        def _parse_lf_age_4_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_4_f = _parse_lf_age_4_f(d.pop("lf_age_4_f", UNSET))

        def _parse_lf_age_4_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_4_f_xfdh = _parse_lf_age_4_f_xfdh(d.pop("lf_age_4_f_xfdh", UNSET))

        def _parse_lf_age_4_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_4_m = _parse_lf_age_4_m(d.pop("lf_age_4_m", UNSET))

        def _parse_lf_age_4_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_4_m_xfdh = _parse_lf_age_4_m_xfdh(d.pop("lf_age_4_m_xfdh", UNSET))

        def _parse_lf_age_4_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_4_xfdh = _parse_lf_age_4_xfdh(d.pop("lf_age_4_xfdh", UNSET))

        def _parse_lf_age_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_5 = _parse_lf_age_5(d.pop("lf_age_5", UNSET))

        def _parse_lf_age_5_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_5_f = _parse_lf_age_5_f(d.pop("lf_age_5_f", UNSET))

        def _parse_lf_age_5_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_5_f_xfdh = _parse_lf_age_5_f_xfdh(d.pop("lf_age_5_f_xfdh", UNSET))

        def _parse_lf_age_5_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_5_m = _parse_lf_age_5_m(d.pop("lf_age_5_m", UNSET))

        def _parse_lf_age_5_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_5_m_xfdh = _parse_lf_age_5_m_xfdh(d.pop("lf_age_5_m_xfdh", UNSET))

        def _parse_lf_age_5_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_5_xfdh = _parse_lf_age_5_xfdh(d.pop("lf_age_5_xfdh", UNSET))

        def _parse_lf_age_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_6 = _parse_lf_age_6(d.pop("lf_age_6", UNSET))

        def _parse_lf_age_6_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_6_f = _parse_lf_age_6_f(d.pop("lf_age_6_f", UNSET))

        def _parse_lf_age_6_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_6_f_xfdh = _parse_lf_age_6_f_xfdh(d.pop("lf_age_6_f_xfdh", UNSET))

        def _parse_lf_age_6_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_6_m = _parse_lf_age_6_m(d.pop("lf_age_6_m", UNSET))

        def _parse_lf_age_6_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_6_m_xfdh = _parse_lf_age_6_m_xfdh(d.pop("lf_age_6_m_xfdh", UNSET))

        def _parse_lf_age_6_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_age_6_xfdh = _parse_lf_age_6_xfdh(d.pop("lf_age_6_xfdh", UNSET))

        def _parse_lf_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_f = _parse_lf_f(d.pop("lf_f", UNSET))

        def _parse_lf_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_f_xfdh = _parse_lf_f_xfdh(d.pop("lf_f_xfdh", UNSET))

        def _parse_lf_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_m = _parse_lf_m(d.pop("lf_m", UNSET))

        def _parse_lf_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_m_xfdh = _parse_lf_m_xfdh(d.pop("lf_m_xfdh", UNSET))

        def _parse_lf_ma_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_ma_f = _parse_lf_ma_f(d.pop("lf_ma_f", UNSET))

        def _parse_lf_ma_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_ma_f_xfdh = _parse_lf_ma_f_xfdh(d.pop("lf_ma_f_xfdh", UNSET))

        def _parse_lf_ma_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_ma_m = _parse_lf_ma_m(d.pop("lf_ma_m", UNSET))

        def _parse_lf_ma_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_ma_m_xfdh = _parse_lf_ma_m_xfdh(d.pop("lf_ma_m_xfdh", UNSET))

        def _parse_lf_ma_t(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_ma_t = _parse_lf_ma_t(d.pop("lf_ma_t", UNSET))

        def _parse_lf_ma_t_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_ma_t_xfdh = _parse_lf_ma_t_xfdh(d.pop("lf_ma_t_xfdh", UNSET))

        def _parse_lf_sr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_sr = _parse_lf_sr(d.pop("lf_sr", UNSET))

        def _parse_lf_sr_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lf_sr_xfdh = _parse_lf_sr_xfdh(d.pop("lf_sr_xfdh", UNSET))

        def _parse_lfpr_age_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_1 = _parse_lfpr_age_1(d.pop("lfpr_age_1", UNSET))

        def _parse_lfpr_age_1_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_1_f = _parse_lfpr_age_1_f(d.pop("lfpr_age_1_f", UNSET))

        def _parse_lfpr_age_1_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_1_f_xfdh = _parse_lfpr_age_1_f_xfdh(d.pop("lfpr_age_1_f_xfdh", UNSET))

        def _parse_lfpr_age_1_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_1_m = _parse_lfpr_age_1_m(d.pop("lfpr_age_1_m", UNSET))

        def _parse_lfpr_age_1_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_1_m_xfdh = _parse_lfpr_age_1_m_xfdh(d.pop("lfpr_age_1_m_xfdh", UNSET))

        def _parse_lfpr_age_1_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_1_xfdh = _parse_lfpr_age_1_xfdh(d.pop("lfpr_age_1_xfdh", UNSET))

        def _parse_lfpr_age_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_2 = _parse_lfpr_age_2(d.pop("lfpr_age_2", UNSET))

        def _parse_lfpr_age_2_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_2_f = _parse_lfpr_age_2_f(d.pop("lfpr_age_2_f", UNSET))

        def _parse_lfpr_age_2_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_2_f_xfdh = _parse_lfpr_age_2_f_xfdh(d.pop("lfpr_age_2_f_xfdh", UNSET))

        def _parse_lfpr_age_2_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_2_m = _parse_lfpr_age_2_m(d.pop("lfpr_age_2_m", UNSET))

        def _parse_lfpr_age_2_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_2_m_xfdh = _parse_lfpr_age_2_m_xfdh(d.pop("lfpr_age_2_m_xfdh", UNSET))

        def _parse_lfpr_age_2_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_2_xfdh = _parse_lfpr_age_2_xfdh(d.pop("lfpr_age_2_xfdh", UNSET))

        def _parse_lfpr_age_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_3 = _parse_lfpr_age_3(d.pop("lfpr_age_3", UNSET))

        def _parse_lfpr_age_3_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_3_f = _parse_lfpr_age_3_f(d.pop("lfpr_age_3_f", UNSET))

        def _parse_lfpr_age_3_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_3_f_xfdh = _parse_lfpr_age_3_f_xfdh(d.pop("lfpr_age_3_f_xfdh", UNSET))

        def _parse_lfpr_age_3_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_3_m = _parse_lfpr_age_3_m(d.pop("lfpr_age_3_m", UNSET))

        def _parse_lfpr_age_3_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_3_m_xfdh = _parse_lfpr_age_3_m_xfdh(d.pop("lfpr_age_3_m_xfdh", UNSET))

        def _parse_lfpr_age_3_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_3_xfdh = _parse_lfpr_age_3_xfdh(d.pop("lfpr_age_3_xfdh", UNSET))

        def _parse_lfpr_age_4(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_4 = _parse_lfpr_age_4(d.pop("lfpr_age_4", UNSET))

        def _parse_lfpr_age_4_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_4_f = _parse_lfpr_age_4_f(d.pop("lfpr_age_4_f", UNSET))

        def _parse_lfpr_age_4_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_4_f_xfdh = _parse_lfpr_age_4_f_xfdh(d.pop("lfpr_age_4_f_xfdh", UNSET))

        def _parse_lfpr_age_4_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_4_m = _parse_lfpr_age_4_m(d.pop("lfpr_age_4_m", UNSET))

        def _parse_lfpr_age_4_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_4_m_xfdh = _parse_lfpr_age_4_m_xfdh(d.pop("lfpr_age_4_m_xfdh", UNSET))

        def _parse_lfpr_age_4_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_4_xfdh = _parse_lfpr_age_4_xfdh(d.pop("lfpr_age_4_xfdh", UNSET))

        def _parse_lfpr_age_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_5 = _parse_lfpr_age_5(d.pop("lfpr_age_5", UNSET))

        def _parse_lfpr_age_5_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_5_f = _parse_lfpr_age_5_f(d.pop("lfpr_age_5_f", UNSET))

        def _parse_lfpr_age_5_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_5_f_xfdh = _parse_lfpr_age_5_f_xfdh(d.pop("lfpr_age_5_f_xfdh", UNSET))

        def _parse_lfpr_age_5_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_5_m = _parse_lfpr_age_5_m(d.pop("lfpr_age_5_m", UNSET))

        def _parse_lfpr_age_5_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_5_m_xfdh = _parse_lfpr_age_5_m_xfdh(d.pop("lfpr_age_5_m_xfdh", UNSET))

        def _parse_lfpr_age_5_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_5_xfdh = _parse_lfpr_age_5_xfdh(d.pop("lfpr_age_5_xfdh", UNSET))

        def _parse_lfpr_age_6(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_6 = _parse_lfpr_age_6(d.pop("lfpr_age_6", UNSET))

        def _parse_lfpr_age_6_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_6_f = _parse_lfpr_age_6_f(d.pop("lfpr_age_6_f", UNSET))

        def _parse_lfpr_age_6_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_6_f_xfdh = _parse_lfpr_age_6_f_xfdh(d.pop("lfpr_age_6_f_xfdh", UNSET))

        def _parse_lfpr_age_6_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_6_m = _parse_lfpr_age_6_m(d.pop("lfpr_age_6_m", UNSET))

        def _parse_lfpr_age_6_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_6_m_xfdh = _parse_lfpr_age_6_m_xfdh(d.pop("lfpr_age_6_m_xfdh", UNSET))

        def _parse_lfpr_age_6_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_age_6_xfdh = _parse_lfpr_age_6_xfdh(d.pop("lfpr_age_6_xfdh", UNSET))

        def _parse_lfpr_f(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_f = _parse_lfpr_f(d.pop("lfpr_f", UNSET))

        def _parse_lfpr_f_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_f_xfdh = _parse_lfpr_f_xfdh(d.pop("lfpr_f_xfdh", UNSET))

        def _parse_lfpr_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_m = _parse_lfpr_m(d.pop("lfpr_m", UNSET))

        def _parse_lfpr_m_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lfpr_m_xfdh = _parse_lfpr_m_xfdh(d.pop("lfpr_m_xfdh", UNSET))

        def _parse_ma_econhh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ma_econhh = _parse_ma_econhh(d.pop("ma_econhh", UNSET))

        def _parse_ma_econhh_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ma_econhh_xfdh = _parse_ma_econhh_xfdh(d.pop("ma_econhh_xfdh", UNSET))

        def _parse_ma_hh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ma_hh = _parse_ma_hh(d.pop("ma_hh", UNSET))

        def _parse_my_lp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        my_lp = _parse_my_lp(d.pop("my_lp", UNSET))

        def _parse_t_lbnp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_lbnp = _parse_t_lbnp(d.pop("t_lbnp", UNSET))

        def _parse_t_lbnp15(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_lbnp15 = _parse_t_lbnp15(d.pop("t_lbnp15", UNSET))

        def _parse_t_lf(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_lf = _parse_t_lf(d.pop("t_lf", UNSET))

        def _parse_t_lf_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_lf_xfdh = _parse_t_lf_xfdh(d.pop("t_lf_xfdh", UNSET))

        def _parse_t_lfpr(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_lfpr = _parse_t_lfpr(d.pop("t_lfpr", UNSET))

        def _parse_t_lfpr_xfdh(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        t_lfpr_xfdh = _parse_t_lfpr_xfdh(d.pop("t_lfpr_xfdh", UNSET))

        def _parse_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year = _parse_year(d.pop("year", UNSET))

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

        wfs_map_server_wfs_dcghs_attributes = cls(
            adhz=adhz,
            dc=dc,
            dc_chi=dc_chi,
            dc_class=dc_class,
            dc_eng=dc_eng,
            dh=dh,
            dh_ea=dh_ea,
            dh_ei=dh_ei,
            dha_oth=dha_oth,
            dha_othpctn=dha_othpctn,
            dha_wf=dha_wf,
            dha_wfpctn=dha_wfpctn,
            dhi_1=dhi_1,
            dhi_1pctn=dhi_1pctn,
            dhi_2=dhi_2,
            dhi_2pctn=dhi_2pctn,
            dhi_3=dhi_3,
            dhi_3pctn=dhi_3pctn,
            dhi_e1=dhi_e1,
            dhi_e1pctn=dhi_e1pctn,
            dhi_e2=dhi_e2,
            dhi_e2pctn=dhi_e2pctn,
            dhi_e3=dhi_e3,
            dhi_e3pctn=dhi_e3pctn,
            dht_oo=dht_oo,
            dht_oopctn=dht_oopctn,
            dht_oth=dht_oth,
            dht_othpctn=dht_othpctn,
            dht_st=dht_st,
            dht_stpctn=dht_stpctn,
            dhz_1=dhz_1,
            dhz_1pctn=dhz_1pctn,
            dhz_2=dhz_2,
            dhz_2pctn=dhz_2pctn,
            dhz_3=dhz_3,
            dhz_3pctn=dhz_3pctn,
            dhz_4=dhz_4,
            dhz_4pctn=dhz_4pctn,
            dhz_5=dhz_5,
            dhz_5_6=dhz_5_6,
            dhz_5_6pctn=dhz_5_6pctn,
            dhz_5pctn=dhz_5pctn,
            dhz_6=dhz_6,
            dhz_6pctn=dhz_6pctn,
            lbnp15_edu_age_1pctn=lbnp15_edu_age_1pctn,
            lbnp15_edu_age_2pctn=lbnp15_edu_age_2pctn,
            lbnp15_edu_age_3pctn=lbnp15_edu_age_3pctn,
            lbnp15_edu_age_4pctn=lbnp15_edu_age_4pctn,
            lbnp15_edu_age_5pctn=lbnp15_edu_age_5pctn,
            lbnp15_edu_age_6pctn=lbnp15_edu_age_6pctn,
            lbnp15_edu_age_7pctn=lbnp15_edu_age_7pctn,
            lbnp15_edu_age_8pctn=lbnp15_edu_age_8pctn,
            lbnp15_edu_deg=lbnp15_edu_deg,
            lbnp15_edu_deg_f=lbnp15_edu_deg_f,
            lbnp15_edu_deg_m=lbnp15_edu_deg_m,
            lbnp15_edu_deg_pctn=lbnp15_edu_deg_pctn,
            lbnp15_edu_deg_pctn_f=lbnp15_edu_deg_pctn_f,
            lbnp15_edu_deg_pctn_m=lbnp15_edu_deg_pctn_m,
            lbnp15_edu_lsed=lbnp15_edu_lsed,
            lbnp15_edu_lsed_f=lbnp15_edu_lsed_f,
            lbnp15_edu_lsed_m=lbnp15_edu_lsed_m,
            lbnp15_edu_lsed_pctn=lbnp15_edu_lsed_pctn,
            lbnp15_edu_lsed_pctn_f=lbnp15_edu_lsed_pctn_f,
            lbnp15_edu_lsed_pctn_m=lbnp15_edu_lsed_pctn_m,
            lbnp15_edu_ndeg=lbnp15_edu_ndeg,
            lbnp15_edu_ndeg_f=lbnp15_edu_ndeg_f,
            lbnp15_edu_ndeg_m=lbnp15_edu_ndeg_m,
            lbnp15_edu_ndeg_pctn=lbnp15_edu_ndeg_pctn,
            lbnp15_edu_ndeg_pctn_f=lbnp15_edu_ndeg_pctn_f,
            lbnp15_edu_ndeg_pctn_m=lbnp15_edu_ndeg_pctn_m,
            lbnp15_edu_pctn=lbnp15_edu_pctn,
            lbnp15_edu_prepri=lbnp15_edu_prepri,
            lbnp15_edu_prepri_f=lbnp15_edu_prepri_f,
            lbnp15_edu_prepri_m=lbnp15_edu_prepri_m,
            lbnp15_edu_prepri_pctn=lbnp15_edu_prepri_pctn,
            lbnp15_edu_prepri_pctn_f=lbnp15_edu_prepri_pctn_f,
            lbnp15_edu_prepri_pctn_m=lbnp15_edu_prepri_pctn_m,
            lbnp15_edu_psec=lbnp15_edu_psec,
            lbnp15_edu_psec_f=lbnp15_edu_psec_f,
            lbnp15_edu_psec_m=lbnp15_edu_psec_m,
            lbnp15_edu_psec_pctn=lbnp15_edu_psec_pctn,
            lbnp15_edu_psec_pctn_f=lbnp15_edu_psec_pctn_f,
            lbnp15_edu_psec_pctn_m=lbnp15_edu_psec_pctn_m,
            lbnp15_edu_usec=lbnp15_edu_usec,
            lbnp15_edu_usec_f=lbnp15_edu_usec_f,
            lbnp15_edu_usec_m=lbnp15_edu_usec_m,
            lbnp15_edu_usec_pctn=lbnp15_edu_usec_pctn,
            lbnp15_edu_usec_pctn_f=lbnp15_edu_usec_pctn_f,
            lbnp15_edu_usec_pctn_m=lbnp15_edu_usec_pctn_m,
            lbnp15_f=lbnp15_f,
            lbnp15_m=lbnp15_m,
            lbnp15_ms_divsep=lbnp15_ms_divsep,
            lbnp15_ms_divsep_f=lbnp15_ms_divsep_f,
            lbnp15_ms_divsep_m=lbnp15_ms_divsep_m,
            lbnp15_ms_divsep_pctn=lbnp15_ms_divsep_pctn,
            lbnp15_ms_divsep_pctn_f=lbnp15_ms_divsep_pctn_f,
            lbnp15_ms_divsep_pctn_m=lbnp15_ms_divsep_pctn_m,
            lbnp15_ms_ma=lbnp15_ms_ma,
            lbnp15_ms_ma_f=lbnp15_ms_ma_f,
            lbnp15_ms_ma_m=lbnp15_ms_ma_m,
            lbnp15_ms_ma_pctn=lbnp15_ms_ma_pctn,
            lbnp15_ms_ma_pctn_f=lbnp15_ms_ma_pctn_f,
            lbnp15_ms_ma_pctn_m=lbnp15_ms_ma_pctn_m,
            lbnp15_ms_nm=lbnp15_ms_nm,
            lbnp15_ms_nm_f=lbnp15_ms_nm_f,
            lbnp15_ms_nm_m=lbnp15_ms_nm_m,
            lbnp15_ms_nm_pctn=lbnp15_ms_nm_pctn,
            lbnp15_ms_nm_pctn_f=lbnp15_ms_nm_pctn_f,
            lbnp15_ms_nm_pctn_m=lbnp15_ms_nm_pctn_m,
            lbnp15_ms_win=lbnp15_ms_win,
            lbnp15_ms_win_f=lbnp15_ms_win_f,
            lbnp15_ms_win_m=lbnp15_ms_win_m,
            lbnp15_ms_win_pctn=lbnp15_ms_win_pctn,
            lbnp15_ms_win_pctn_f=lbnp15_ms_win_pctn_f,
            lbnp15_ms_win_pctn_m=lbnp15_ms_win_pctn_m,
            lbnp_act_eapctn=lbnp_act_eapctn,
            lbnp_act_eipctn=lbnp_act_eipctn,
            lbnp_act_ftstpctn=lbnp_act_ftstpctn,
            lbnp_act_hmpctn=lbnp_act_hmpctn,
            lbnp_act_othpctn=lbnp_act_othpctn,
            lbnp_age_1=lbnp_age_1,
            lbnp_age_1_f=lbnp_age_1_f,
            lbnp_age_1_m=lbnp_age_1_m,
            lbnp_age_1pctn=lbnp_age_1pctn,
            lbnp_age_1pctn_f=lbnp_age_1pctn_f,
            lbnp_age_1pctn_m=lbnp_age_1pctn_m,
            lbnp_age_2=lbnp_age_2,
            lbnp_age_2_f=lbnp_age_2_f,
            lbnp_age_2_m=lbnp_age_2_m,
            lbnp_age_2pctn=lbnp_age_2pctn,
            lbnp_age_2pctn_f=lbnp_age_2pctn_f,
            lbnp_age_2pctn_m=lbnp_age_2pctn_m,
            lbnp_age_3=lbnp_age_3,
            lbnp_age_3_f=lbnp_age_3_f,
            lbnp_age_3_m=lbnp_age_3_m,
            lbnp_age_3pctn=lbnp_age_3pctn,
            lbnp_age_3pctn_f=lbnp_age_3pctn_f,
            lbnp_age_3pctn_m=lbnp_age_3pctn_m,
            lbnp_age_4=lbnp_age_4,
            lbnp_age_4_f=lbnp_age_4_f,
            lbnp_age_4_m=lbnp_age_4_m,
            lbnp_age_4pctn=lbnp_age_4pctn,
            lbnp_age_4pctn_f=lbnp_age_4pctn_f,
            lbnp_age_4pctn_m=lbnp_age_4pctn_m,
            lbnp_age_5=lbnp_age_5,
            lbnp_age_5_f=lbnp_age_5_f,
            lbnp_age_5_m=lbnp_age_5_m,
            lbnp_age_5pctn=lbnp_age_5pctn,
            lbnp_age_5pctn_f=lbnp_age_5pctn_f,
            lbnp_age_5pctn_m=lbnp_age_5pctn_m,
            lbnp_age_6=lbnp_age_6,
            lbnp_age_6_f=lbnp_age_6_f,
            lbnp_age_6_m=lbnp_age_6_m,
            lbnp_age_6pctn=lbnp_age_6pctn,
            lbnp_age_6pctn_f=lbnp_age_6pctn_f,
            lbnp_age_6pctn_m=lbnp_age_6pctn_m,
            lbnp_age_7=lbnp_age_7,
            lbnp_age_7_f=lbnp_age_7_f,
            lbnp_age_7_m=lbnp_age_7_m,
            lbnp_age_7pctn=lbnp_age_7pctn,
            lbnp_age_7pctn_f=lbnp_age_7pctn_f,
            lbnp_age_7pctn_m=lbnp_age_7pctn_m,
            lbnp_age_8=lbnp_age_8,
            lbnp_age_8_f=lbnp_age_8_f,
            lbnp_age_8_m=lbnp_age_8_m,
            lbnp_age_8pctn=lbnp_age_8pctn,
            lbnp_age_8pctn_f=lbnp_age_8pctn_f,
            lbnp_age_8pctn_m=lbnp_age_8pctn_m,
            lbnp_ea=lbnp_ea,
            lbnp_ei=lbnp_ei,
            lbnp_f=lbnp_f,
            lbnp_ftst=lbnp_ftst,
            lbnp_hm=lbnp_hm,
            lbnp_m=lbnp_m,
            lbnp_ma_f=lbnp_ma_f,
            lbnp_ma_f_xfdh=lbnp_ma_f_xfdh,
            lbnp_ma_m=lbnp_ma_m,
            lbnp_ma_m_xfdh=lbnp_ma_m_xfdh,
            lbnp_ma_t=lbnp_ma_t,
            lbnp_ma_t_xfdh=lbnp_ma_t_xfdh,
            lbnp_odr=lbnp_odr,
            lbnp_odr_xfdh=lbnp_odr_xfdh,
            lbnp_oth=lbnp_oth,
            lbnp_sr=lbnp_sr,
            lbnp_sr_xfdh=lbnp_sr_xfdh,
            lf_age_1=lf_age_1,
            lf_age_1_f=lf_age_1_f,
            lf_age_1_f_xfdh=lf_age_1_f_xfdh,
            lf_age_1_m=lf_age_1_m,
            lf_age_1_m_xfdh=lf_age_1_m_xfdh,
            lf_age_1_xfdh=lf_age_1_xfdh,
            lf_age_2=lf_age_2,
            lf_age_2_f=lf_age_2_f,
            lf_age_2_f_xfdh=lf_age_2_f_xfdh,
            lf_age_2_m=lf_age_2_m,
            lf_age_2_m_xfdh=lf_age_2_m_xfdh,
            lf_age_2_xfdh=lf_age_2_xfdh,
            lf_age_3=lf_age_3,
            lf_age_3_f=lf_age_3_f,
            lf_age_3_f_xfdh=lf_age_3_f_xfdh,
            lf_age_3_m=lf_age_3_m,
            lf_age_3_m_xfdh=lf_age_3_m_xfdh,
            lf_age_3_xfdh=lf_age_3_xfdh,
            lf_age_4=lf_age_4,
            lf_age_4_f=lf_age_4_f,
            lf_age_4_f_xfdh=lf_age_4_f_xfdh,
            lf_age_4_m=lf_age_4_m,
            lf_age_4_m_xfdh=lf_age_4_m_xfdh,
            lf_age_4_xfdh=lf_age_4_xfdh,
            lf_age_5=lf_age_5,
            lf_age_5_f=lf_age_5_f,
            lf_age_5_f_xfdh=lf_age_5_f_xfdh,
            lf_age_5_m=lf_age_5_m,
            lf_age_5_m_xfdh=lf_age_5_m_xfdh,
            lf_age_5_xfdh=lf_age_5_xfdh,
            lf_age_6=lf_age_6,
            lf_age_6_f=lf_age_6_f,
            lf_age_6_f_xfdh=lf_age_6_f_xfdh,
            lf_age_6_m=lf_age_6_m,
            lf_age_6_m_xfdh=lf_age_6_m_xfdh,
            lf_age_6_xfdh=lf_age_6_xfdh,
            lf_f=lf_f,
            lf_f_xfdh=lf_f_xfdh,
            lf_m=lf_m,
            lf_m_xfdh=lf_m_xfdh,
            lf_ma_f=lf_ma_f,
            lf_ma_f_xfdh=lf_ma_f_xfdh,
            lf_ma_m=lf_ma_m,
            lf_ma_m_xfdh=lf_ma_m_xfdh,
            lf_ma_t=lf_ma_t,
            lf_ma_t_xfdh=lf_ma_t_xfdh,
            lf_sr=lf_sr,
            lf_sr_xfdh=lf_sr_xfdh,
            lfpr_age_1=lfpr_age_1,
            lfpr_age_1_f=lfpr_age_1_f,
            lfpr_age_1_f_xfdh=lfpr_age_1_f_xfdh,
            lfpr_age_1_m=lfpr_age_1_m,
            lfpr_age_1_m_xfdh=lfpr_age_1_m_xfdh,
            lfpr_age_1_xfdh=lfpr_age_1_xfdh,
            lfpr_age_2=lfpr_age_2,
            lfpr_age_2_f=lfpr_age_2_f,
            lfpr_age_2_f_xfdh=lfpr_age_2_f_xfdh,
            lfpr_age_2_m=lfpr_age_2_m,
            lfpr_age_2_m_xfdh=lfpr_age_2_m_xfdh,
            lfpr_age_2_xfdh=lfpr_age_2_xfdh,
            lfpr_age_3=lfpr_age_3,
            lfpr_age_3_f=lfpr_age_3_f,
            lfpr_age_3_f_xfdh=lfpr_age_3_f_xfdh,
            lfpr_age_3_m=lfpr_age_3_m,
            lfpr_age_3_m_xfdh=lfpr_age_3_m_xfdh,
            lfpr_age_3_xfdh=lfpr_age_3_xfdh,
            lfpr_age_4=lfpr_age_4,
            lfpr_age_4_f=lfpr_age_4_f,
            lfpr_age_4_f_xfdh=lfpr_age_4_f_xfdh,
            lfpr_age_4_m=lfpr_age_4_m,
            lfpr_age_4_m_xfdh=lfpr_age_4_m_xfdh,
            lfpr_age_4_xfdh=lfpr_age_4_xfdh,
            lfpr_age_5=lfpr_age_5,
            lfpr_age_5_f=lfpr_age_5_f,
            lfpr_age_5_f_xfdh=lfpr_age_5_f_xfdh,
            lfpr_age_5_m=lfpr_age_5_m,
            lfpr_age_5_m_xfdh=lfpr_age_5_m_xfdh,
            lfpr_age_5_xfdh=lfpr_age_5_xfdh,
            lfpr_age_6=lfpr_age_6,
            lfpr_age_6_f=lfpr_age_6_f,
            lfpr_age_6_f_xfdh=lfpr_age_6_f_xfdh,
            lfpr_age_6_m=lfpr_age_6_m,
            lfpr_age_6_m_xfdh=lfpr_age_6_m_xfdh,
            lfpr_age_6_xfdh=lfpr_age_6_xfdh,
            lfpr_f=lfpr_f,
            lfpr_f_xfdh=lfpr_f_xfdh,
            lfpr_m=lfpr_m,
            lfpr_m_xfdh=lfpr_m_xfdh,
            ma_econhh=ma_econhh,
            ma_econhh_xfdh=ma_econhh_xfdh,
            ma_hh=ma_hh,
            my_lp=my_lp,
            t_lbnp=t_lbnp,
            t_lbnp15=t_lbnp15,
            t_lf=t_lf,
            t_lf_xfdh=t_lf_xfdh,
            t_lfpr=t_lfpr,
            t_lfpr_xfdh=t_lfpr_xfdh,
            year=year,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_dcghs_attributes.additional_properties = d
        return wfs_map_server_wfs_dcghs_attributes

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
