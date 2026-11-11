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
        ora (float | Unset):
        ora_fcrsv (float | Unset):
        ora_fcrsv_sec (float | Unset):
        ora_fcrsv_sec_hqinhk (float | Unset):
        ora_fcrsv_tcd (float | Unset):
        ora_fcrsv_tcd_cbank (float | Unset):
        ora_fcrsv_tcd_hqinhk (float | Unset):
        ora_fcrsv_tcd_hqinhk_locabd (float | Unset):
        ora_fcrsv_tcd_hqouthk (float | Unset):
        ora_fcrsv_tcd_hqouthk_lochk (float | Unset):
        ora_imfrsvpos (float | Unset):
        ora_sdr (float | Unset):
        ora_gold (float | Unset):
        ora_gold_oz (float | Unset):
        ora_othra (float | Unset):
        ora_othra_finderiv (float | Unset):
        ora_othra_loannonbkresd (float | Unset):
        ora_othra_other (float | Unset):
        ofca (float | Unset):
        ofca_secnotinora (float | Unset):
        ofca_depnotinora (float | Unset):
        ofca_loannotinora (float | Unset):
        ofca_finderivnotinora (float | Unset):
        ofca_goldnotinora (float | Unset):
        ofca_other (float | Unset):
        psnd_fclsd (float | Unset):
        psnd_fclsd_upto1m (float | Unset):
        psnd_fclsd_1mto3m (float | Unset):
        psnd_fclsd_3mto1y (float | Unset):
        psnd_fclsd_ofprin (float | Unset):
        psnd_fclsd_ofprin_upto1m (float | Unset):
        psnd_fclsd_ofprin_1mto3m (float | Unset):
        psnd_fclsd_ofprin_3mto1y (float | Unset):
        psnd_fclsd_ofint (float | Unset):
        psnd_fclsd_ofint_upto1m (float | Unset):
        psnd_fclsd_ofint_1mto3m (float | Unset):
        psnd_fclsd_ofint_3mto1y (float | Unset):
        psnd_fclsd_ifprin (float | Unset):
        psnd_fclsd_ifprin_upto1m (float | Unset):
        psnd_fclsd_ifprin_1mto3m (float | Unset):
        psnd_fclsd_ifprin_3mto1y (float | Unset):
        psnd_fclsd_ifint (float | Unset):
        psnd_fclsd_ifint_upto1m (float | Unset):
        psnd_fclsd_ifint_1mto3m (float | Unset):
        psnd_fclsd_ifint_3mto1y (float | Unset):
        psnd_aslp (float | Unset):
        psnd_aslp_upto1m (float | Unset):
        psnd_aslp_1mto3m (float | Unset):
        psnd_aslp_3mto1y (float | Unset):
        psnd_aslp_shpos (float | Unset):
        psnd_aslp_shpos_upto1m (float | Unset):
        psnd_aslp_shpos_1mto3m (float | Unset):
        psnd_aslp_shpos_3mto1y (float | Unset):
        psnd_aslp_lgpos (float | Unset):
        psnd_aslp_lgpos_upto1m (float | Unset):
        psnd_aslp_lgpos_1mto3m (float | Unset):
        psnd_aslp_lgpos_3mto1y (float | Unset):
        psnd_oth (float | Unset):
        psnd_oth_upto1m (float | Unset):
        psnd_oth_1mto3m (float | Unset):
        psnd_oth_3mto1y (float | Unset):
        psnd_oth_ofrepos (float | Unset):
        psnd_oth_ofrepos_upto1m (float | Unset):
        psnd_oth_ofrepos_1mto3m (float | Unset):
        psnd_oth_ofrepos_3mto1y (float | Unset):
        psnd_oth_ifrrepos (float | Unset):
        psnd_oth_ifrrepos_upto1m (float | Unset):
        psnd_oth_ifrrepos_1mto3m (float | Unset):
        psnd_oth_ifrrepos_3mto1y (float | Unset):
        psnd_oth_tracrneg (float | Unset):
        psnd_oth_tracrneg_upto1m (float | Unset):
        psnd_oth_tracrneg_1mto3m (float | Unset):
        psnd_oth_tracrneg_3mto1y (float | Unset):
        psnd_oth_tracrpos (float | Unset):
        psnd_oth_tracrpos_upto1m (float | Unset):
        psnd_oth_tracrpos_1mto3m (float | Unset):
        psnd_oth_tracrpos_3mto1y (float | Unset):
        psnd_oth_acctpay (float | Unset):
        psnd_oth_acctpay_upto1m (float | Unset):
        psnd_oth_acctpay_1mto3m (float | Unset):
        psnd_oth_acctpay_3mto1y (float | Unset):
        psnd_oth_acctrecv (float | Unset):
        psnd_oth_acctrecv_upto1m (float | Unset):
        psnd_oth_acctrecv_1mto3m (float | Unset):
        psnd_oth_acctrecv_3mto1y (float | Unset):
        csnd_clfc (float | Unset):
        csnd_clfc_upto1m (float | Unset):
        csnd_clfc_1mto3m (float | Unset):
        csnd_clfc_3mto1y (float | Unset):
        csnd_clfc_cgdf1y (float | Unset):
        csnd_clfc_cgdf1y_upto1m (float | Unset):
        csnd_clfc_cgdf1y_1mto3m (float | Unset):
        csnd_clfc_cgdf1y_3mto1y (float | Unset):
        csnd_clfc_othcl (float | Unset):
        csnd_clfc_othcl_upto1m (float | Unset):
        csnd_clfc_othcl_1mto3m (float | Unset):
        csnd_clfc_othcl_3mto1y (float | Unset):
        csnd_fcsecwembopt (float | Unset):
        csnd_uduccrlby (float | Unset):
        csnd_uduccrlby_upto1m (float | Unset):
        csnd_uduccrlby_1mto3m (float | Unset):
        csnd_uduccrlby_3mto1y (float | Unset):
        csnd_uduccrlby_oth (float | Unset):
        csnd_uduccrlby_oth_upto1m (float | Unset):
        csnd_uduccrlby_oth_1mto3m (float | Unset):
        csnd_uduccrlby_oth_3mto1y (float | Unset):
        csnd_uduccrlby_oth_auth (float | Unset):
        csnd_uduccrlby_oth_auth_upto1m (float | Unset):
        csnd_uduccrlby_oth_auth_1mto3m (float | Unset):
        csnd_uduccrlby_oth_auth_3mto1y (float | Unset):
        csnd_uduccrlby_oth_bis (float | Unset):
        csnd_uduccrlby_oth_bis_upto1m (float | Unset):
        csnd_uduccrlby_oth_bis_1mto3m (float | Unset):
        csnd_uduccrlby_oth_bis_3mto1y (float | Unset):
        csnd_uduccrlby_oth_imf (float | Unset):
        csnd_uduccrlby_oth_imf_upto1m (float | Unset):
        csnd_uduccrlby_oth_imf_1mto3m (float | Unset):
        csnd_uduccrlby_oth_imf_3mto1y (float | Unset):
        csnd_uduccrlby_oth_iorg (float | Unset):
        csnd_uduccrlby_oth_iorg_upto1m (float | Unset):
        csnd_uduccrlby_oth_iorg_1mto3m (float | Unset):
        csnd_uduccrlby_oth_iorg_3mto1y (float | Unset):
        csnd_uduccrlby_bkinhk (float | Unset):
        csnd_uduccrlby_bkinhk_upto1m (float | Unset):
        csnd_uduccrlby_bkinhk_1mto3m (float | Unset):
        csnd_uduccrlby_bkinhk_3mto1y (float | Unset):
        csnd_uduccrlby_bkouthk (float | Unset):
        csnd_uduccrlby_bkouthk_upto1m (float | Unset):
        csnd_uduccrlby_bkouthk_1mto3m (float | Unset):
        csnd_uduccrlby_bkouthk_3mto1y (float | Unset):
        csnd_uduccrlto (float | Unset):
        csnd_uduccrlto_upto1m (float | Unset):
        csnd_uduccrlto_1mto3m (float | Unset):
        csnd_uduccrlto_3mto1y (float | Unset):
        csnd_uduccrlto_oth (float | Unset):
        csnd_uduccrlto_oth_upto1m (float | Unset):
        csnd_uduccrlto_oth_1mto3m (float | Unset):
        csnd_uduccrlto_oth_3mto1y (float | Unset):
        csnd_uduccrlto_oth_auth (float | Unset):
        csnd_uduccrlto_oth_auth_upto1m (float | Unset):
        csnd_uduccrlto_oth_auth_1mto3m (float | Unset):
        csnd_uduccrlto_oth_auth_3mto1y (float | Unset):
        csnd_uduccrlto_oth_bis (float | Unset):
        csnd_uduccrlto_oth_bis_upto1m (float | Unset):
        csnd_uduccrlto_oth_bis_1mto3m (float | Unset):
        csnd_uduccrlto_oth_bis_3mto1y (float | Unset):
        csnd_uduccrlto_oth_imf (float | Unset):
        csnd_uduccrlto_oth_imf_upto1m (float | Unset):
        csnd_uduccrlto_oth_imf_1mto3m (float | Unset):
        csnd_uduccrlto_oth_imf_3mto1y (float | Unset):
        csnd_uduccrlto_oth_iorg (float | Unset):
        csnd_uduccrlto_oth_iorg_upto1m (float | Unset):
        csnd_uduccrlto_oth_iorg_1mto3m (float | Unset):
        csnd_uduccrlto_oth_iorg_3mto1y (float | Unset):
        csnd_uduccrlto_bkinhk (float | Unset):
        csnd_uduccrlto_bkinhk_upto1m (float | Unset):
        csnd_uduccrlto_bkinhk_1mto3m (float | Unset):
        csnd_uduccrlto_bkinhk_3mto1y (float | Unset):
        csnd_uduccrlto_bkouthk (float | Unset):
        csnd_uduccrlto_bkouthk_upto1m (float | Unset):
        csnd_uduccrlto_bkouthk_1mto3m (float | Unset):
        csnd_uduccrlto_bkouthk_3mto1y (float | Unset):
        csnd_aslp (float | Unset):
        csnd_aslp_upto1m (float | Unset):
        csnd_aslp_1mto3m (float | Unset):
        csnd_aslp_3mto1y (float | Unset):
        csnd_aslp_sp (float | Unset):
        csnd_aslp_sp_upto1m (float | Unset):
        csnd_aslp_sp_1mto3m (float | Unset):
        csnd_aslp_sp_3mto1y (float | Unset):
        csnd_aslp_sp_bp (float | Unset):
        csnd_aslp_sp_bp_upto1m (float | Unset):
        csnd_aslp_sp_bp_1mto3m (float | Unset):
        csnd_aslp_sp_bp_3mto1y (float | Unset):
        csnd_aslp_sp_wc (float | Unset):
        csnd_aslp_sp_wc_upto1m (float | Unset):
        csnd_aslp_sp_wc_1mto3m (float | Unset):
        csnd_aslp_sp_wc_3mto1y (float | Unset):
        csnd_aslp_lp (float | Unset):
        csnd_aslp_lp_upto1m (float | Unset):
        csnd_aslp_lp_1mto3m (float | Unset):
        csnd_aslp_lp_3mto1y (float | Unset):
        csnd_aslp_lp_bc (float | Unset):
        csnd_aslp_lp_bc_upto1m (float | Unset):
        csnd_aslp_lp_bc_1mto3m (float | Unset):
        csnd_aslp_lp_bc_3mto1y (float | Unset):
        csnd_aslp_lp_wp (float | Unset):
        csnd_aslp_lp_wp_upto1m (float | Unset):
        csnd_aslp_lp_wp_1mto3m (float | Unset):
        csnd_aslp_lp_wp_3mto1y (float | Unset):
        mm_spt_stdcd (float | Unset):
        mm_spt_fid (float | Unset):
        mm_spt_fid_ndf (float | Unset):
        mm_spt_fid_ndf_sp (float | Unset):
        mm_spt_fid_ndf_lp (float | Unset):
        mm_spt_fid_oi (float | Unset):
        mm_spt_pa (float | Unset):
        mm_spt_pa_ra (float | Unset):
        mm_spt_pa_ofca (float | Unset):
        mm_spt_slr (float | Unset):
        mm_spt_slr_lr_insi (float | Unset):
        mm_spt_slr_lr_notinsi (float | Unset):
        mm_spt_slr_ba_insi (float | Unset):
        mm_spt_slr_ba_notinsi (float | Unset):
        mm_spt_fda (float | Unset):
        mm_spt_fda_forw (float | Unset):
        mm_spt_fda_fut (float | Unset):
        mm_spt_fda_swp (float | Unset):
        mm_spt_fda_opt (float | Unset):
        mm_spt_fda_oth (float | Unset):
        mm_spt_dergt1y (float | Unset):
        mm_spt_dergt1y_aslpf (float | Unset):
        mm_spt_dergt1y_aslpf_sp (float | Unset):
        mm_spt_dergt1y_aslpf_lp (float | Unset):
        mm_spt_dergt1y_aslpfo (float | Unset):
        mm_spt_dergt1y_aslpfo_sp (float | Unset):
        mm_spt_dergt1y_aslpfo_sp_bp (float | Unset):
        mm_spt_dergt1y_aslpfo_sp_wc (float | Unset):
        mm_spt_dergt1y_aslpfo_lp (float | Unset):
        mm_spt_dergt1y_aslpfo_lp_bc (float | Unset):
        mm_spt_dergt1y_aslpfo_lp_wp (float | Unset):
        mm_lfd_ccr (float | Unset):
        mm_lfd_ccr_insdr (float | Unset):
        mm_lfd_ccr_insdr_eur (float | Unset):
        mm_lfd_ccr_insdr_jpy (float | Unset):
        mm_lfd_ccr_insdr_gbp (float | Unset):
        mm_lfd_ccr_insdr_usd (float | Unset):
        mm_lfd_ccr_notinsdr (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    ora: float | Unset = UNSET
    ora_fcrsv: float | Unset = UNSET
    ora_fcrsv_sec: float | Unset = UNSET
    ora_fcrsv_sec_hqinhk: float | Unset = UNSET
    ora_fcrsv_tcd: float | Unset = UNSET
    ora_fcrsv_tcd_cbank: float | Unset = UNSET
    ora_fcrsv_tcd_hqinhk: float | Unset = UNSET
    ora_fcrsv_tcd_hqinhk_locabd: float | Unset = UNSET
    ora_fcrsv_tcd_hqouthk: float | Unset = UNSET
    ora_fcrsv_tcd_hqouthk_lochk: float | Unset = UNSET
    ora_imfrsvpos: float | Unset = UNSET
    ora_sdr: float | Unset = UNSET
    ora_gold: float | Unset = UNSET
    ora_gold_oz: float | Unset = UNSET
    ora_othra: float | Unset = UNSET
    ora_othra_finderiv: float | Unset = UNSET
    ora_othra_loannonbkresd: float | Unset = UNSET
    ora_othra_other: float | Unset = UNSET
    ofca: float | Unset = UNSET
    ofca_secnotinora: float | Unset = UNSET
    ofca_depnotinora: float | Unset = UNSET
    ofca_loannotinora: float | Unset = UNSET
    ofca_finderivnotinora: float | Unset = UNSET
    ofca_goldnotinora: float | Unset = UNSET
    ofca_other: float | Unset = UNSET
    psnd_fclsd: float | Unset = UNSET
    psnd_fclsd_upto1m: float | Unset = UNSET
    psnd_fclsd_1mto3m: float | Unset = UNSET
    psnd_fclsd_3mto1y: float | Unset = UNSET
    psnd_fclsd_ofprin: float | Unset = UNSET
    psnd_fclsd_ofprin_upto1m: float | Unset = UNSET
    psnd_fclsd_ofprin_1mto3m: float | Unset = UNSET
    psnd_fclsd_ofprin_3mto1y: float | Unset = UNSET
    psnd_fclsd_ofint: float | Unset = UNSET
    psnd_fclsd_ofint_upto1m: float | Unset = UNSET
    psnd_fclsd_ofint_1mto3m: float | Unset = UNSET
    psnd_fclsd_ofint_3mto1y: float | Unset = UNSET
    psnd_fclsd_ifprin: float | Unset = UNSET
    psnd_fclsd_ifprin_upto1m: float | Unset = UNSET
    psnd_fclsd_ifprin_1mto3m: float | Unset = UNSET
    psnd_fclsd_ifprin_3mto1y: float | Unset = UNSET
    psnd_fclsd_ifint: float | Unset = UNSET
    psnd_fclsd_ifint_upto1m: float | Unset = UNSET
    psnd_fclsd_ifint_1mto3m: float | Unset = UNSET
    psnd_fclsd_ifint_3mto1y: float | Unset = UNSET
    psnd_aslp: float | Unset = UNSET
    psnd_aslp_upto1m: float | Unset = UNSET
    psnd_aslp_1mto3m: float | Unset = UNSET
    psnd_aslp_3mto1y: float | Unset = UNSET
    psnd_aslp_shpos: float | Unset = UNSET
    psnd_aslp_shpos_upto1m: float | Unset = UNSET
    psnd_aslp_shpos_1mto3m: float | Unset = UNSET
    psnd_aslp_shpos_3mto1y: float | Unset = UNSET
    psnd_aslp_lgpos: float | Unset = UNSET
    psnd_aslp_lgpos_upto1m: float | Unset = UNSET
    psnd_aslp_lgpos_1mto3m: float | Unset = UNSET
    psnd_aslp_lgpos_3mto1y: float | Unset = UNSET
    psnd_oth: float | Unset = UNSET
    psnd_oth_upto1m: float | Unset = UNSET
    psnd_oth_1mto3m: float | Unset = UNSET
    psnd_oth_3mto1y: float | Unset = UNSET
    psnd_oth_ofrepos: float | Unset = UNSET
    psnd_oth_ofrepos_upto1m: float | Unset = UNSET
    psnd_oth_ofrepos_1mto3m: float | Unset = UNSET
    psnd_oth_ofrepos_3mto1y: float | Unset = UNSET
    psnd_oth_ifrrepos: float | Unset = UNSET
    psnd_oth_ifrrepos_upto1m: float | Unset = UNSET
    psnd_oth_ifrrepos_1mto3m: float | Unset = UNSET
    psnd_oth_ifrrepos_3mto1y: float | Unset = UNSET
    psnd_oth_tracrneg: float | Unset = UNSET
    psnd_oth_tracrneg_upto1m: float | Unset = UNSET
    psnd_oth_tracrneg_1mto3m: float | Unset = UNSET
    psnd_oth_tracrneg_3mto1y: float | Unset = UNSET
    psnd_oth_tracrpos: float | Unset = UNSET
    psnd_oth_tracrpos_upto1m: float | Unset = UNSET
    psnd_oth_tracrpos_1mto3m: float | Unset = UNSET
    psnd_oth_tracrpos_3mto1y: float | Unset = UNSET
    psnd_oth_acctpay: float | Unset = UNSET
    psnd_oth_acctpay_upto1m: float | Unset = UNSET
    psnd_oth_acctpay_1mto3m: float | Unset = UNSET
    psnd_oth_acctpay_3mto1y: float | Unset = UNSET
    psnd_oth_acctrecv: float | Unset = UNSET
    psnd_oth_acctrecv_upto1m: float | Unset = UNSET
    psnd_oth_acctrecv_1mto3m: float | Unset = UNSET
    psnd_oth_acctrecv_3mto1y: float | Unset = UNSET
    csnd_clfc: float | Unset = UNSET
    csnd_clfc_upto1m: float | Unset = UNSET
    csnd_clfc_1mto3m: float | Unset = UNSET
    csnd_clfc_3mto1y: float | Unset = UNSET
    csnd_clfc_cgdf1y: float | Unset = UNSET
    csnd_clfc_cgdf1y_upto1m: float | Unset = UNSET
    csnd_clfc_cgdf1y_1mto3m: float | Unset = UNSET
    csnd_clfc_cgdf1y_3mto1y: float | Unset = UNSET
    csnd_clfc_othcl: float | Unset = UNSET
    csnd_clfc_othcl_upto1m: float | Unset = UNSET
    csnd_clfc_othcl_1mto3m: float | Unset = UNSET
    csnd_clfc_othcl_3mto1y: float | Unset = UNSET
    csnd_fcsecwembopt: float | Unset = UNSET
    csnd_uduccrlby: float | Unset = UNSET
    csnd_uduccrlby_upto1m: float | Unset = UNSET
    csnd_uduccrlby_1mto3m: float | Unset = UNSET
    csnd_uduccrlby_3mto1y: float | Unset = UNSET
    csnd_uduccrlby_oth: float | Unset = UNSET
    csnd_uduccrlby_oth_upto1m: float | Unset = UNSET
    csnd_uduccrlby_oth_1mto3m: float | Unset = UNSET
    csnd_uduccrlby_oth_3mto1y: float | Unset = UNSET
    csnd_uduccrlby_oth_auth: float | Unset = UNSET
    csnd_uduccrlby_oth_auth_upto1m: float | Unset = UNSET
    csnd_uduccrlby_oth_auth_1mto3m: float | Unset = UNSET
    csnd_uduccrlby_oth_auth_3mto1y: float | Unset = UNSET
    csnd_uduccrlby_oth_bis: float | Unset = UNSET
    csnd_uduccrlby_oth_bis_upto1m: float | Unset = UNSET
    csnd_uduccrlby_oth_bis_1mto3m: float | Unset = UNSET
    csnd_uduccrlby_oth_bis_3mto1y: float | Unset = UNSET
    csnd_uduccrlby_oth_imf: float | Unset = UNSET
    csnd_uduccrlby_oth_imf_upto1m: float | Unset = UNSET
    csnd_uduccrlby_oth_imf_1mto3m: float | Unset = UNSET
    csnd_uduccrlby_oth_imf_3mto1y: float | Unset = UNSET
    csnd_uduccrlby_oth_iorg: float | Unset = UNSET
    csnd_uduccrlby_oth_iorg_upto1m: float | Unset = UNSET
    csnd_uduccrlby_oth_iorg_1mto3m: float | Unset = UNSET
    csnd_uduccrlby_oth_iorg_3mto1y: float | Unset = UNSET
    csnd_uduccrlby_bkinhk: float | Unset = UNSET
    csnd_uduccrlby_bkinhk_upto1m: float | Unset = UNSET
    csnd_uduccrlby_bkinhk_1mto3m: float | Unset = UNSET
    csnd_uduccrlby_bkinhk_3mto1y: float | Unset = UNSET
    csnd_uduccrlby_bkouthk: float | Unset = UNSET
    csnd_uduccrlby_bkouthk_upto1m: float | Unset = UNSET
    csnd_uduccrlby_bkouthk_1mto3m: float | Unset = UNSET
    csnd_uduccrlby_bkouthk_3mto1y: float | Unset = UNSET
    csnd_uduccrlto: float | Unset = UNSET
    csnd_uduccrlto_upto1m: float | Unset = UNSET
    csnd_uduccrlto_1mto3m: float | Unset = UNSET
    csnd_uduccrlto_3mto1y: float | Unset = UNSET
    csnd_uduccrlto_oth: float | Unset = UNSET
    csnd_uduccrlto_oth_upto1m: float | Unset = UNSET
    csnd_uduccrlto_oth_1mto3m: float | Unset = UNSET
    csnd_uduccrlto_oth_3mto1y: float | Unset = UNSET
    csnd_uduccrlto_oth_auth: float | Unset = UNSET
    csnd_uduccrlto_oth_auth_upto1m: float | Unset = UNSET
    csnd_uduccrlto_oth_auth_1mto3m: float | Unset = UNSET
    csnd_uduccrlto_oth_auth_3mto1y: float | Unset = UNSET
    csnd_uduccrlto_oth_bis: float | Unset = UNSET
    csnd_uduccrlto_oth_bis_upto1m: float | Unset = UNSET
    csnd_uduccrlto_oth_bis_1mto3m: float | Unset = UNSET
    csnd_uduccrlto_oth_bis_3mto1y: float | Unset = UNSET
    csnd_uduccrlto_oth_imf: float | Unset = UNSET
    csnd_uduccrlto_oth_imf_upto1m: float | Unset = UNSET
    csnd_uduccrlto_oth_imf_1mto3m: float | Unset = UNSET
    csnd_uduccrlto_oth_imf_3mto1y: float | Unset = UNSET
    csnd_uduccrlto_oth_iorg: float | Unset = UNSET
    csnd_uduccrlto_oth_iorg_upto1m: float | Unset = UNSET
    csnd_uduccrlto_oth_iorg_1mto3m: float | Unset = UNSET
    csnd_uduccrlto_oth_iorg_3mto1y: float | Unset = UNSET
    csnd_uduccrlto_bkinhk: float | Unset = UNSET
    csnd_uduccrlto_bkinhk_upto1m: float | Unset = UNSET
    csnd_uduccrlto_bkinhk_1mto3m: float | Unset = UNSET
    csnd_uduccrlto_bkinhk_3mto1y: float | Unset = UNSET
    csnd_uduccrlto_bkouthk: float | Unset = UNSET
    csnd_uduccrlto_bkouthk_upto1m: float | Unset = UNSET
    csnd_uduccrlto_bkouthk_1mto3m: float | Unset = UNSET
    csnd_uduccrlto_bkouthk_3mto1y: float | Unset = UNSET
    csnd_aslp: float | Unset = UNSET
    csnd_aslp_upto1m: float | Unset = UNSET
    csnd_aslp_1mto3m: float | Unset = UNSET
    csnd_aslp_3mto1y: float | Unset = UNSET
    csnd_aslp_sp: float | Unset = UNSET
    csnd_aslp_sp_upto1m: float | Unset = UNSET
    csnd_aslp_sp_1mto3m: float | Unset = UNSET
    csnd_aslp_sp_3mto1y: float | Unset = UNSET
    csnd_aslp_sp_bp: float | Unset = UNSET
    csnd_aslp_sp_bp_upto1m: float | Unset = UNSET
    csnd_aslp_sp_bp_1mto3m: float | Unset = UNSET
    csnd_aslp_sp_bp_3mto1y: float | Unset = UNSET
    csnd_aslp_sp_wc: float | Unset = UNSET
    csnd_aslp_sp_wc_upto1m: float | Unset = UNSET
    csnd_aslp_sp_wc_1mto3m: float | Unset = UNSET
    csnd_aslp_sp_wc_3mto1y: float | Unset = UNSET
    csnd_aslp_lp: float | Unset = UNSET
    csnd_aslp_lp_upto1m: float | Unset = UNSET
    csnd_aslp_lp_1mto3m: float | Unset = UNSET
    csnd_aslp_lp_3mto1y: float | Unset = UNSET
    csnd_aslp_lp_bc: float | Unset = UNSET
    csnd_aslp_lp_bc_upto1m: float | Unset = UNSET
    csnd_aslp_lp_bc_1mto3m: float | Unset = UNSET
    csnd_aslp_lp_bc_3mto1y: float | Unset = UNSET
    csnd_aslp_lp_wp: float | Unset = UNSET
    csnd_aslp_lp_wp_upto1m: float | Unset = UNSET
    csnd_aslp_lp_wp_1mto3m: float | Unset = UNSET
    csnd_aslp_lp_wp_3mto1y: float | Unset = UNSET
    mm_spt_stdcd: float | Unset = UNSET
    mm_spt_fid: float | Unset = UNSET
    mm_spt_fid_ndf: float | Unset = UNSET
    mm_spt_fid_ndf_sp: float | Unset = UNSET
    mm_spt_fid_ndf_lp: float | Unset = UNSET
    mm_spt_fid_oi: float | Unset = UNSET
    mm_spt_pa: float | Unset = UNSET
    mm_spt_pa_ra: float | Unset = UNSET
    mm_spt_pa_ofca: float | Unset = UNSET
    mm_spt_slr: float | Unset = UNSET
    mm_spt_slr_lr_insi: float | Unset = UNSET
    mm_spt_slr_lr_notinsi: float | Unset = UNSET
    mm_spt_slr_ba_insi: float | Unset = UNSET
    mm_spt_slr_ba_notinsi: float | Unset = UNSET
    mm_spt_fda: float | Unset = UNSET
    mm_spt_fda_forw: float | Unset = UNSET
    mm_spt_fda_fut: float | Unset = UNSET
    mm_spt_fda_swp: float | Unset = UNSET
    mm_spt_fda_opt: float | Unset = UNSET
    mm_spt_fda_oth: float | Unset = UNSET
    mm_spt_dergt1y: float | Unset = UNSET
    mm_spt_dergt1y_aslpf: float | Unset = UNSET
    mm_spt_dergt1y_aslpf_sp: float | Unset = UNSET
    mm_spt_dergt1y_aslpf_lp: float | Unset = UNSET
    mm_spt_dergt1y_aslpfo: float | Unset = UNSET
    mm_spt_dergt1y_aslpfo_sp: float | Unset = UNSET
    mm_spt_dergt1y_aslpfo_sp_bp: float | Unset = UNSET
    mm_spt_dergt1y_aslpfo_sp_wc: float | Unset = UNSET
    mm_spt_dergt1y_aslpfo_lp: float | Unset = UNSET
    mm_spt_dergt1y_aslpfo_lp_bc: float | Unset = UNSET
    mm_spt_dergt1y_aslpfo_lp_wp: float | Unset = UNSET
    mm_lfd_ccr: float | Unset = UNSET
    mm_lfd_ccr_insdr: float | Unset = UNSET
    mm_lfd_ccr_insdr_eur: float | Unset = UNSET
    mm_lfd_ccr_insdr_jpy: float | Unset = UNSET
    mm_lfd_ccr_insdr_gbp: float | Unset = UNSET
    mm_lfd_ccr_insdr_usd: float | Unset = UNSET
    mm_lfd_ccr_notinsdr: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        ora = self.ora

        ora_fcrsv = self.ora_fcrsv

        ora_fcrsv_sec = self.ora_fcrsv_sec

        ora_fcrsv_sec_hqinhk = self.ora_fcrsv_sec_hqinhk

        ora_fcrsv_tcd = self.ora_fcrsv_tcd

        ora_fcrsv_tcd_cbank = self.ora_fcrsv_tcd_cbank

        ora_fcrsv_tcd_hqinhk = self.ora_fcrsv_tcd_hqinhk

        ora_fcrsv_tcd_hqinhk_locabd = self.ora_fcrsv_tcd_hqinhk_locabd

        ora_fcrsv_tcd_hqouthk = self.ora_fcrsv_tcd_hqouthk

        ora_fcrsv_tcd_hqouthk_lochk = self.ora_fcrsv_tcd_hqouthk_lochk

        ora_imfrsvpos = self.ora_imfrsvpos

        ora_sdr = self.ora_sdr

        ora_gold = self.ora_gold

        ora_gold_oz = self.ora_gold_oz

        ora_othra = self.ora_othra

        ora_othra_finderiv = self.ora_othra_finderiv

        ora_othra_loannonbkresd = self.ora_othra_loannonbkresd

        ora_othra_other = self.ora_othra_other

        ofca = self.ofca

        ofca_secnotinora = self.ofca_secnotinora

        ofca_depnotinora = self.ofca_depnotinora

        ofca_loannotinora = self.ofca_loannotinora

        ofca_finderivnotinora = self.ofca_finderivnotinora

        ofca_goldnotinora = self.ofca_goldnotinora

        ofca_other = self.ofca_other

        psnd_fclsd = self.psnd_fclsd

        psnd_fclsd_upto1m = self.psnd_fclsd_upto1m

        psnd_fclsd_1mto3m = self.psnd_fclsd_1mto3m

        psnd_fclsd_3mto1y = self.psnd_fclsd_3mto1y

        psnd_fclsd_ofprin = self.psnd_fclsd_ofprin

        psnd_fclsd_ofprin_upto1m = self.psnd_fclsd_ofprin_upto1m

        psnd_fclsd_ofprin_1mto3m = self.psnd_fclsd_ofprin_1mto3m

        psnd_fclsd_ofprin_3mto1y = self.psnd_fclsd_ofprin_3mto1y

        psnd_fclsd_ofint = self.psnd_fclsd_ofint

        psnd_fclsd_ofint_upto1m = self.psnd_fclsd_ofint_upto1m

        psnd_fclsd_ofint_1mto3m = self.psnd_fclsd_ofint_1mto3m

        psnd_fclsd_ofint_3mto1y = self.psnd_fclsd_ofint_3mto1y

        psnd_fclsd_ifprin = self.psnd_fclsd_ifprin

        psnd_fclsd_ifprin_upto1m = self.psnd_fclsd_ifprin_upto1m

        psnd_fclsd_ifprin_1mto3m = self.psnd_fclsd_ifprin_1mto3m

        psnd_fclsd_ifprin_3mto1y = self.psnd_fclsd_ifprin_3mto1y

        psnd_fclsd_ifint = self.psnd_fclsd_ifint

        psnd_fclsd_ifint_upto1m = self.psnd_fclsd_ifint_upto1m

        psnd_fclsd_ifint_1mto3m = self.psnd_fclsd_ifint_1mto3m

        psnd_fclsd_ifint_3mto1y = self.psnd_fclsd_ifint_3mto1y

        psnd_aslp = self.psnd_aslp

        psnd_aslp_upto1m = self.psnd_aslp_upto1m

        psnd_aslp_1mto3m = self.psnd_aslp_1mto3m

        psnd_aslp_3mto1y = self.psnd_aslp_3mto1y

        psnd_aslp_shpos = self.psnd_aslp_shpos

        psnd_aslp_shpos_upto1m = self.psnd_aslp_shpos_upto1m

        psnd_aslp_shpos_1mto3m = self.psnd_aslp_shpos_1mto3m

        psnd_aslp_shpos_3mto1y = self.psnd_aslp_shpos_3mto1y

        psnd_aslp_lgpos = self.psnd_aslp_lgpos

        psnd_aslp_lgpos_upto1m = self.psnd_aslp_lgpos_upto1m

        psnd_aslp_lgpos_1mto3m = self.psnd_aslp_lgpos_1mto3m

        psnd_aslp_lgpos_3mto1y = self.psnd_aslp_lgpos_3mto1y

        psnd_oth = self.psnd_oth

        psnd_oth_upto1m = self.psnd_oth_upto1m

        psnd_oth_1mto3m = self.psnd_oth_1mto3m

        psnd_oth_3mto1y = self.psnd_oth_3mto1y

        psnd_oth_ofrepos = self.psnd_oth_ofrepos

        psnd_oth_ofrepos_upto1m = self.psnd_oth_ofrepos_upto1m

        psnd_oth_ofrepos_1mto3m = self.psnd_oth_ofrepos_1mto3m

        psnd_oth_ofrepos_3mto1y = self.psnd_oth_ofrepos_3mto1y

        psnd_oth_ifrrepos = self.psnd_oth_ifrrepos

        psnd_oth_ifrrepos_upto1m = self.psnd_oth_ifrrepos_upto1m

        psnd_oth_ifrrepos_1mto3m = self.psnd_oth_ifrrepos_1mto3m

        psnd_oth_ifrrepos_3mto1y = self.psnd_oth_ifrrepos_3mto1y

        psnd_oth_tracrneg = self.psnd_oth_tracrneg

        psnd_oth_tracrneg_upto1m = self.psnd_oth_tracrneg_upto1m

        psnd_oth_tracrneg_1mto3m = self.psnd_oth_tracrneg_1mto3m

        psnd_oth_tracrneg_3mto1y = self.psnd_oth_tracrneg_3mto1y

        psnd_oth_tracrpos = self.psnd_oth_tracrpos

        psnd_oth_tracrpos_upto1m = self.psnd_oth_tracrpos_upto1m

        psnd_oth_tracrpos_1mto3m = self.psnd_oth_tracrpos_1mto3m

        psnd_oth_tracrpos_3mto1y = self.psnd_oth_tracrpos_3mto1y

        psnd_oth_acctpay = self.psnd_oth_acctpay

        psnd_oth_acctpay_upto1m = self.psnd_oth_acctpay_upto1m

        psnd_oth_acctpay_1mto3m = self.psnd_oth_acctpay_1mto3m

        psnd_oth_acctpay_3mto1y = self.psnd_oth_acctpay_3mto1y

        psnd_oth_acctrecv = self.psnd_oth_acctrecv

        psnd_oth_acctrecv_upto1m = self.psnd_oth_acctrecv_upto1m

        psnd_oth_acctrecv_1mto3m = self.psnd_oth_acctrecv_1mto3m

        psnd_oth_acctrecv_3mto1y = self.psnd_oth_acctrecv_3mto1y

        csnd_clfc = self.csnd_clfc

        csnd_clfc_upto1m = self.csnd_clfc_upto1m

        csnd_clfc_1mto3m = self.csnd_clfc_1mto3m

        csnd_clfc_3mto1y = self.csnd_clfc_3mto1y

        csnd_clfc_cgdf1y = self.csnd_clfc_cgdf1y

        csnd_clfc_cgdf1y_upto1m = self.csnd_clfc_cgdf1y_upto1m

        csnd_clfc_cgdf1y_1mto3m = self.csnd_clfc_cgdf1y_1mto3m

        csnd_clfc_cgdf1y_3mto1y = self.csnd_clfc_cgdf1y_3mto1y

        csnd_clfc_othcl = self.csnd_clfc_othcl

        csnd_clfc_othcl_upto1m = self.csnd_clfc_othcl_upto1m

        csnd_clfc_othcl_1mto3m = self.csnd_clfc_othcl_1mto3m

        csnd_clfc_othcl_3mto1y = self.csnd_clfc_othcl_3mto1y

        csnd_fcsecwembopt = self.csnd_fcsecwembopt

        csnd_uduccrlby = self.csnd_uduccrlby

        csnd_uduccrlby_upto1m = self.csnd_uduccrlby_upto1m

        csnd_uduccrlby_1mto3m = self.csnd_uduccrlby_1mto3m

        csnd_uduccrlby_3mto1y = self.csnd_uduccrlby_3mto1y

        csnd_uduccrlby_oth = self.csnd_uduccrlby_oth

        csnd_uduccrlby_oth_upto1m = self.csnd_uduccrlby_oth_upto1m

        csnd_uduccrlby_oth_1mto3m = self.csnd_uduccrlby_oth_1mto3m

        csnd_uduccrlby_oth_3mto1y = self.csnd_uduccrlby_oth_3mto1y

        csnd_uduccrlby_oth_auth = self.csnd_uduccrlby_oth_auth

        csnd_uduccrlby_oth_auth_upto1m = self.csnd_uduccrlby_oth_auth_upto1m

        csnd_uduccrlby_oth_auth_1mto3m = self.csnd_uduccrlby_oth_auth_1mto3m

        csnd_uduccrlby_oth_auth_3mto1y = self.csnd_uduccrlby_oth_auth_3mto1y

        csnd_uduccrlby_oth_bis = self.csnd_uduccrlby_oth_bis

        csnd_uduccrlby_oth_bis_upto1m = self.csnd_uduccrlby_oth_bis_upto1m

        csnd_uduccrlby_oth_bis_1mto3m = self.csnd_uduccrlby_oth_bis_1mto3m

        csnd_uduccrlby_oth_bis_3mto1y = self.csnd_uduccrlby_oth_bis_3mto1y

        csnd_uduccrlby_oth_imf = self.csnd_uduccrlby_oth_imf

        csnd_uduccrlby_oth_imf_upto1m = self.csnd_uduccrlby_oth_imf_upto1m

        csnd_uduccrlby_oth_imf_1mto3m = self.csnd_uduccrlby_oth_imf_1mto3m

        csnd_uduccrlby_oth_imf_3mto1y = self.csnd_uduccrlby_oth_imf_3mto1y

        csnd_uduccrlby_oth_iorg = self.csnd_uduccrlby_oth_iorg

        csnd_uduccrlby_oth_iorg_upto1m = self.csnd_uduccrlby_oth_iorg_upto1m

        csnd_uduccrlby_oth_iorg_1mto3m = self.csnd_uduccrlby_oth_iorg_1mto3m

        csnd_uduccrlby_oth_iorg_3mto1y = self.csnd_uduccrlby_oth_iorg_3mto1y

        csnd_uduccrlby_bkinhk = self.csnd_uduccrlby_bkinhk

        csnd_uduccrlby_bkinhk_upto1m = self.csnd_uduccrlby_bkinhk_upto1m

        csnd_uduccrlby_bkinhk_1mto3m = self.csnd_uduccrlby_bkinhk_1mto3m

        csnd_uduccrlby_bkinhk_3mto1y = self.csnd_uduccrlby_bkinhk_3mto1y

        csnd_uduccrlby_bkouthk = self.csnd_uduccrlby_bkouthk

        csnd_uduccrlby_bkouthk_upto1m = self.csnd_uduccrlby_bkouthk_upto1m

        csnd_uduccrlby_bkouthk_1mto3m = self.csnd_uduccrlby_bkouthk_1mto3m

        csnd_uduccrlby_bkouthk_3mto1y = self.csnd_uduccrlby_bkouthk_3mto1y

        csnd_uduccrlto = self.csnd_uduccrlto

        csnd_uduccrlto_upto1m = self.csnd_uduccrlto_upto1m

        csnd_uduccrlto_1mto3m = self.csnd_uduccrlto_1mto3m

        csnd_uduccrlto_3mto1y = self.csnd_uduccrlto_3mto1y

        csnd_uduccrlto_oth = self.csnd_uduccrlto_oth

        csnd_uduccrlto_oth_upto1m = self.csnd_uduccrlto_oth_upto1m

        csnd_uduccrlto_oth_1mto3m = self.csnd_uduccrlto_oth_1mto3m

        csnd_uduccrlto_oth_3mto1y = self.csnd_uduccrlto_oth_3mto1y

        csnd_uduccrlto_oth_auth = self.csnd_uduccrlto_oth_auth

        csnd_uduccrlto_oth_auth_upto1m = self.csnd_uduccrlto_oth_auth_upto1m

        csnd_uduccrlto_oth_auth_1mto3m = self.csnd_uduccrlto_oth_auth_1mto3m

        csnd_uduccrlto_oth_auth_3mto1y = self.csnd_uduccrlto_oth_auth_3mto1y

        csnd_uduccrlto_oth_bis = self.csnd_uduccrlto_oth_bis

        csnd_uduccrlto_oth_bis_upto1m = self.csnd_uduccrlto_oth_bis_upto1m

        csnd_uduccrlto_oth_bis_1mto3m = self.csnd_uduccrlto_oth_bis_1mto3m

        csnd_uduccrlto_oth_bis_3mto1y = self.csnd_uduccrlto_oth_bis_3mto1y

        csnd_uduccrlto_oth_imf = self.csnd_uduccrlto_oth_imf

        csnd_uduccrlto_oth_imf_upto1m = self.csnd_uduccrlto_oth_imf_upto1m

        csnd_uduccrlto_oth_imf_1mto3m = self.csnd_uduccrlto_oth_imf_1mto3m

        csnd_uduccrlto_oth_imf_3mto1y = self.csnd_uduccrlto_oth_imf_3mto1y

        csnd_uduccrlto_oth_iorg = self.csnd_uduccrlto_oth_iorg

        csnd_uduccrlto_oth_iorg_upto1m = self.csnd_uduccrlto_oth_iorg_upto1m

        csnd_uduccrlto_oth_iorg_1mto3m = self.csnd_uduccrlto_oth_iorg_1mto3m

        csnd_uduccrlto_oth_iorg_3mto1y = self.csnd_uduccrlto_oth_iorg_3mto1y

        csnd_uduccrlto_bkinhk = self.csnd_uduccrlto_bkinhk

        csnd_uduccrlto_bkinhk_upto1m = self.csnd_uduccrlto_bkinhk_upto1m

        csnd_uduccrlto_bkinhk_1mto3m = self.csnd_uduccrlto_bkinhk_1mto3m

        csnd_uduccrlto_bkinhk_3mto1y = self.csnd_uduccrlto_bkinhk_3mto1y

        csnd_uduccrlto_bkouthk = self.csnd_uduccrlto_bkouthk

        csnd_uduccrlto_bkouthk_upto1m = self.csnd_uduccrlto_bkouthk_upto1m

        csnd_uduccrlto_bkouthk_1mto3m = self.csnd_uduccrlto_bkouthk_1mto3m

        csnd_uduccrlto_bkouthk_3mto1y = self.csnd_uduccrlto_bkouthk_3mto1y

        csnd_aslp = self.csnd_aslp

        csnd_aslp_upto1m = self.csnd_aslp_upto1m

        csnd_aslp_1mto3m = self.csnd_aslp_1mto3m

        csnd_aslp_3mto1y = self.csnd_aslp_3mto1y

        csnd_aslp_sp = self.csnd_aslp_sp

        csnd_aslp_sp_upto1m = self.csnd_aslp_sp_upto1m

        csnd_aslp_sp_1mto3m = self.csnd_aslp_sp_1mto3m

        csnd_aslp_sp_3mto1y = self.csnd_aslp_sp_3mto1y

        csnd_aslp_sp_bp = self.csnd_aslp_sp_bp

        csnd_aslp_sp_bp_upto1m = self.csnd_aslp_sp_bp_upto1m

        csnd_aslp_sp_bp_1mto3m = self.csnd_aslp_sp_bp_1mto3m

        csnd_aslp_sp_bp_3mto1y = self.csnd_aslp_sp_bp_3mto1y

        csnd_aslp_sp_wc = self.csnd_aslp_sp_wc

        csnd_aslp_sp_wc_upto1m = self.csnd_aslp_sp_wc_upto1m

        csnd_aslp_sp_wc_1mto3m = self.csnd_aslp_sp_wc_1mto3m

        csnd_aslp_sp_wc_3mto1y = self.csnd_aslp_sp_wc_3mto1y

        csnd_aslp_lp = self.csnd_aslp_lp

        csnd_aslp_lp_upto1m = self.csnd_aslp_lp_upto1m

        csnd_aslp_lp_1mto3m = self.csnd_aslp_lp_1mto3m

        csnd_aslp_lp_3mto1y = self.csnd_aslp_lp_3mto1y

        csnd_aslp_lp_bc = self.csnd_aslp_lp_bc

        csnd_aslp_lp_bc_upto1m = self.csnd_aslp_lp_bc_upto1m

        csnd_aslp_lp_bc_1mto3m = self.csnd_aslp_lp_bc_1mto3m

        csnd_aslp_lp_bc_3mto1y = self.csnd_aslp_lp_bc_3mto1y

        csnd_aslp_lp_wp = self.csnd_aslp_lp_wp

        csnd_aslp_lp_wp_upto1m = self.csnd_aslp_lp_wp_upto1m

        csnd_aslp_lp_wp_1mto3m = self.csnd_aslp_lp_wp_1mto3m

        csnd_aslp_lp_wp_3mto1y = self.csnd_aslp_lp_wp_3mto1y

        mm_spt_stdcd = self.mm_spt_stdcd

        mm_spt_fid = self.mm_spt_fid

        mm_spt_fid_ndf = self.mm_spt_fid_ndf

        mm_spt_fid_ndf_sp = self.mm_spt_fid_ndf_sp

        mm_spt_fid_ndf_lp = self.mm_spt_fid_ndf_lp

        mm_spt_fid_oi = self.mm_spt_fid_oi

        mm_spt_pa = self.mm_spt_pa

        mm_spt_pa_ra = self.mm_spt_pa_ra

        mm_spt_pa_ofca = self.mm_spt_pa_ofca

        mm_spt_slr = self.mm_spt_slr

        mm_spt_slr_lr_insi = self.mm_spt_slr_lr_insi

        mm_spt_slr_lr_notinsi = self.mm_spt_slr_lr_notinsi

        mm_spt_slr_ba_insi = self.mm_spt_slr_ba_insi

        mm_spt_slr_ba_notinsi = self.mm_spt_slr_ba_notinsi

        mm_spt_fda = self.mm_spt_fda

        mm_spt_fda_forw = self.mm_spt_fda_forw

        mm_spt_fda_fut = self.mm_spt_fda_fut

        mm_spt_fda_swp = self.mm_spt_fda_swp

        mm_spt_fda_opt = self.mm_spt_fda_opt

        mm_spt_fda_oth = self.mm_spt_fda_oth

        mm_spt_dergt1y = self.mm_spt_dergt1y

        mm_spt_dergt1y_aslpf = self.mm_spt_dergt1y_aslpf

        mm_spt_dergt1y_aslpf_sp = self.mm_spt_dergt1y_aslpf_sp

        mm_spt_dergt1y_aslpf_lp = self.mm_spt_dergt1y_aslpf_lp

        mm_spt_dergt1y_aslpfo = self.mm_spt_dergt1y_aslpfo

        mm_spt_dergt1y_aslpfo_sp = self.mm_spt_dergt1y_aslpfo_sp

        mm_spt_dergt1y_aslpfo_sp_bp = self.mm_spt_dergt1y_aslpfo_sp_bp

        mm_spt_dergt1y_aslpfo_sp_wc = self.mm_spt_dergt1y_aslpfo_sp_wc

        mm_spt_dergt1y_aslpfo_lp = self.mm_spt_dergt1y_aslpfo_lp

        mm_spt_dergt1y_aslpfo_lp_bc = self.mm_spt_dergt1y_aslpfo_lp_bc

        mm_spt_dergt1y_aslpfo_lp_wp = self.mm_spt_dergt1y_aslpfo_lp_wp

        mm_lfd_ccr = self.mm_lfd_ccr

        mm_lfd_ccr_insdr = self.mm_lfd_ccr_insdr

        mm_lfd_ccr_insdr_eur = self.mm_lfd_ccr_insdr_eur

        mm_lfd_ccr_insdr_jpy = self.mm_lfd_ccr_insdr_jpy

        mm_lfd_ccr_insdr_gbp = self.mm_lfd_ccr_insdr_gbp

        mm_lfd_ccr_insdr_usd = self.mm_lfd_ccr_insdr_usd

        mm_lfd_ccr_notinsdr = self.mm_lfd_ccr_notinsdr

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if ora is not UNSET:
            field_dict["ora"] = ora
        if ora_fcrsv is not UNSET:
            field_dict["ora_fcrsv"] = ora_fcrsv
        if ora_fcrsv_sec is not UNSET:
            field_dict["ora_fcrsv_sec"] = ora_fcrsv_sec
        if ora_fcrsv_sec_hqinhk is not UNSET:
            field_dict["ora_fcrsv_sec_hqinhk"] = ora_fcrsv_sec_hqinhk
        if ora_fcrsv_tcd is not UNSET:
            field_dict["ora_fcrsv_tcd"] = ora_fcrsv_tcd
        if ora_fcrsv_tcd_cbank is not UNSET:
            field_dict["ora_fcrsv_ tcd_cbank"] = ora_fcrsv_tcd_cbank
        if ora_fcrsv_tcd_hqinhk is not UNSET:
            field_dict["ora_fcrsv_tcd_hqinhk"] = ora_fcrsv_tcd_hqinhk
        if ora_fcrsv_tcd_hqinhk_locabd is not UNSET:
            field_dict["ora_fcrsv_tcd_hqinhk_locabd"] = ora_fcrsv_tcd_hqinhk_locabd
        if ora_fcrsv_tcd_hqouthk is not UNSET:
            field_dict["ora_fcrsv_tcd_hqouthk"] = ora_fcrsv_tcd_hqouthk
        if ora_fcrsv_tcd_hqouthk_lochk is not UNSET:
            field_dict["ora_fcrsv_tcd_hqouthk_lochk"] = ora_fcrsv_tcd_hqouthk_lochk
        if ora_imfrsvpos is not UNSET:
            field_dict["ora_imfrsvpos"] = ora_imfrsvpos
        if ora_sdr is not UNSET:
            field_dict["ora_sdr"] = ora_sdr
        if ora_gold is not UNSET:
            field_dict["ora_gold"] = ora_gold
        if ora_gold_oz is not UNSET:
            field_dict["ora_gold_oz"] = ora_gold_oz
        if ora_othra is not UNSET:
            field_dict["ora_othra"] = ora_othra
        if ora_othra_finderiv is not UNSET:
            field_dict["ora_othra_finderiv"] = ora_othra_finderiv
        if ora_othra_loannonbkresd is not UNSET:
            field_dict["ora_othra_loannonbkresd"] = ora_othra_loannonbkresd
        if ora_othra_other is not UNSET:
            field_dict["ora_othra_other"] = ora_othra_other
        if ofca is not UNSET:
            field_dict["ofca"] = ofca
        if ofca_secnotinora is not UNSET:
            field_dict["ofca_secnotinora"] = ofca_secnotinora
        if ofca_depnotinora is not UNSET:
            field_dict["ofca_depnotinora"] = ofca_depnotinora
        if ofca_loannotinora is not UNSET:
            field_dict["ofca_loannotinora"] = ofca_loannotinora
        if ofca_finderivnotinora is not UNSET:
            field_dict["ofca_finderivnotinora"] = ofca_finderivnotinora
        if ofca_goldnotinora is not UNSET:
            field_dict["ofca_goldnotinora"] = ofca_goldnotinora
        if ofca_other is not UNSET:
            field_dict["ofca_other"] = ofca_other
        if psnd_fclsd is not UNSET:
            field_dict["psnd_fclsd"] = psnd_fclsd
        if psnd_fclsd_upto1m is not UNSET:
            field_dict["psnd_fclsd_upto1m"] = psnd_fclsd_upto1m
        if psnd_fclsd_1mto3m is not UNSET:
            field_dict["psnd_fclsd_1mto3m"] = psnd_fclsd_1mto3m
        if psnd_fclsd_3mto1y is not UNSET:
            field_dict["psnd_fclsd_3mto1y"] = psnd_fclsd_3mto1y
        if psnd_fclsd_ofprin is not UNSET:
            field_dict["psnd_fclsd_ofprin"] = psnd_fclsd_ofprin
        if psnd_fclsd_ofprin_upto1m is not UNSET:
            field_dict["psnd_fclsd_ofprin_upto1m"] = psnd_fclsd_ofprin_upto1m
        if psnd_fclsd_ofprin_1mto3m is not UNSET:
            field_dict["psnd_fclsd_ofprin_1mto3m"] = psnd_fclsd_ofprin_1mto3m
        if psnd_fclsd_ofprin_3mto1y is not UNSET:
            field_dict["psnd_fclsd_ofprin_3mto1y"] = psnd_fclsd_ofprin_3mto1y
        if psnd_fclsd_ofint is not UNSET:
            field_dict["psnd_fclsd_ofint"] = psnd_fclsd_ofint
        if psnd_fclsd_ofint_upto1m is not UNSET:
            field_dict["psnd_fclsd_ofint_upto1m"] = psnd_fclsd_ofint_upto1m
        if psnd_fclsd_ofint_1mto3m is not UNSET:
            field_dict["psnd_fclsd_ofint_1mto3m"] = psnd_fclsd_ofint_1mto3m
        if psnd_fclsd_ofint_3mto1y is not UNSET:
            field_dict["psnd_fclsd_ofint_3mto1y"] = psnd_fclsd_ofint_3mto1y
        if psnd_fclsd_ifprin is not UNSET:
            field_dict["psnd_fclsd_ifprin"] = psnd_fclsd_ifprin
        if psnd_fclsd_ifprin_upto1m is not UNSET:
            field_dict["psnd_fclsd_ifprin_upto1m"] = psnd_fclsd_ifprin_upto1m
        if psnd_fclsd_ifprin_1mto3m is not UNSET:
            field_dict["psnd_fclsd_ifprin_1mto3m"] = psnd_fclsd_ifprin_1mto3m
        if psnd_fclsd_ifprin_3mto1y is not UNSET:
            field_dict["psnd_fclsd_ifprin_3mto1y"] = psnd_fclsd_ifprin_3mto1y
        if psnd_fclsd_ifint is not UNSET:
            field_dict["psnd_fclsd_ifint"] = psnd_fclsd_ifint
        if psnd_fclsd_ifint_upto1m is not UNSET:
            field_dict["psnd_fclsd_ifint_upto1m"] = psnd_fclsd_ifint_upto1m
        if psnd_fclsd_ifint_1mto3m is not UNSET:
            field_dict["psnd_fclsd_ifint_1mto3m"] = psnd_fclsd_ifint_1mto3m
        if psnd_fclsd_ifint_3mto1y is not UNSET:
            field_dict["psnd_fclsd_ifint_3mto1y"] = psnd_fclsd_ifint_3mto1y
        if psnd_aslp is not UNSET:
            field_dict["psnd_aslp"] = psnd_aslp
        if psnd_aslp_upto1m is not UNSET:
            field_dict["psnd_aslp_upto1m"] = psnd_aslp_upto1m
        if psnd_aslp_1mto3m is not UNSET:
            field_dict["psnd_aslp_1mto3m"] = psnd_aslp_1mto3m
        if psnd_aslp_3mto1y is not UNSET:
            field_dict["psnd_aslp_3mto1y"] = psnd_aslp_3mto1y
        if psnd_aslp_shpos is not UNSET:
            field_dict["psnd_aslp_shpos"] = psnd_aslp_shpos
        if psnd_aslp_shpos_upto1m is not UNSET:
            field_dict["psnd_aslp_shpos_upto1m"] = psnd_aslp_shpos_upto1m
        if psnd_aslp_shpos_1mto3m is not UNSET:
            field_dict["psnd_aslp_shpos_1mto3m"] = psnd_aslp_shpos_1mto3m
        if psnd_aslp_shpos_3mto1y is not UNSET:
            field_dict["psnd_aslp_shpos_3mto1y"] = psnd_aslp_shpos_3mto1y
        if psnd_aslp_lgpos is not UNSET:
            field_dict["psnd_aslp_lgpos"] = psnd_aslp_lgpos
        if psnd_aslp_lgpos_upto1m is not UNSET:
            field_dict["psnd_aslp_lgpos_upto1m"] = psnd_aslp_lgpos_upto1m
        if psnd_aslp_lgpos_1mto3m is not UNSET:
            field_dict["psnd_aslp_lgpos_1mto3m"] = psnd_aslp_lgpos_1mto3m
        if psnd_aslp_lgpos_3mto1y is not UNSET:
            field_dict["psnd_aslp_lgpos_3mto1y"] = psnd_aslp_lgpos_3mto1y
        if psnd_oth is not UNSET:
            field_dict["psnd_oth"] = psnd_oth
        if psnd_oth_upto1m is not UNSET:
            field_dict["psnd_oth_upto1m"] = psnd_oth_upto1m
        if psnd_oth_1mto3m is not UNSET:
            field_dict["psnd_oth_1mto3m"] = psnd_oth_1mto3m
        if psnd_oth_3mto1y is not UNSET:
            field_dict["psnd_oth_3mto1y"] = psnd_oth_3mto1y
        if psnd_oth_ofrepos is not UNSET:
            field_dict["psnd_oth_ofrepos"] = psnd_oth_ofrepos
        if psnd_oth_ofrepos_upto1m is not UNSET:
            field_dict["psnd_oth_ofrepos_upto1m"] = psnd_oth_ofrepos_upto1m
        if psnd_oth_ofrepos_1mto3m is not UNSET:
            field_dict["psnd_oth_ofrepos_1mto3m"] = psnd_oth_ofrepos_1mto3m
        if psnd_oth_ofrepos_3mto1y is not UNSET:
            field_dict["psnd_oth_ofrepos_3mto1y"] = psnd_oth_ofrepos_3mto1y
        if psnd_oth_ifrrepos is not UNSET:
            field_dict["psnd_oth_ifrrepos"] = psnd_oth_ifrrepos
        if psnd_oth_ifrrepos_upto1m is not UNSET:
            field_dict["psnd_oth_ifrrepos_upto1m"] = psnd_oth_ifrrepos_upto1m
        if psnd_oth_ifrrepos_1mto3m is not UNSET:
            field_dict["psnd_oth_ifrrepos_1mto3m"] = psnd_oth_ifrrepos_1mto3m
        if psnd_oth_ifrrepos_3mto1y is not UNSET:
            field_dict["psnd_oth_ifrrepos_3mto1y"] = psnd_oth_ifrrepos_3mto1y
        if psnd_oth_tracrneg is not UNSET:
            field_dict["psnd_oth_tracrneg"] = psnd_oth_tracrneg
        if psnd_oth_tracrneg_upto1m is not UNSET:
            field_dict["psnd_oth_tracrneg_upto1m"] = psnd_oth_tracrneg_upto1m
        if psnd_oth_tracrneg_1mto3m is not UNSET:
            field_dict["psnd_oth_tracrneg_1mto3m"] = psnd_oth_tracrneg_1mto3m
        if psnd_oth_tracrneg_3mto1y is not UNSET:
            field_dict["psnd_oth_tracrneg_3mto1y"] = psnd_oth_tracrneg_3mto1y
        if psnd_oth_tracrpos is not UNSET:
            field_dict["psnd_oth_tracrpos"] = psnd_oth_tracrpos
        if psnd_oth_tracrpos_upto1m is not UNSET:
            field_dict["psnd_oth_tracrpos_upto1m"] = psnd_oth_tracrpos_upto1m
        if psnd_oth_tracrpos_1mto3m is not UNSET:
            field_dict["psnd_oth_tracrpos_1mto3m"] = psnd_oth_tracrpos_1mto3m
        if psnd_oth_tracrpos_3mto1y is not UNSET:
            field_dict["psnd_oth_tracrpos_3mto1y"] = psnd_oth_tracrpos_3mto1y
        if psnd_oth_acctpay is not UNSET:
            field_dict["psnd_oth_acctpay"] = psnd_oth_acctpay
        if psnd_oth_acctpay_upto1m is not UNSET:
            field_dict["psnd_oth_acctpay_upto1m"] = psnd_oth_acctpay_upto1m
        if psnd_oth_acctpay_1mto3m is not UNSET:
            field_dict["psnd_oth_acctpay_1mto3m"] = psnd_oth_acctpay_1mto3m
        if psnd_oth_acctpay_3mto1y is not UNSET:
            field_dict["psnd_oth_acctpay_3mto1y"] = psnd_oth_acctpay_3mto1y
        if psnd_oth_acctrecv is not UNSET:
            field_dict["psnd_oth_acctrecv"] = psnd_oth_acctrecv
        if psnd_oth_acctrecv_upto1m is not UNSET:
            field_dict["psnd_oth_acctrecv_upto1m"] = psnd_oth_acctrecv_upto1m
        if psnd_oth_acctrecv_1mto3m is not UNSET:
            field_dict["psnd_oth_acctrecv_1mto3m"] = psnd_oth_acctrecv_1mto3m
        if psnd_oth_acctrecv_3mto1y is not UNSET:
            field_dict["psnd_oth_acctrecv_3mto1y"] = psnd_oth_acctrecv_3mto1y
        if csnd_clfc is not UNSET:
            field_dict["csnd_clfc"] = csnd_clfc
        if csnd_clfc_upto1m is not UNSET:
            field_dict["csnd_clfc_upto1m"] = csnd_clfc_upto1m
        if csnd_clfc_1mto3m is not UNSET:
            field_dict["csnd_clfc_1mto3m"] = csnd_clfc_1mto3m
        if csnd_clfc_3mto1y is not UNSET:
            field_dict["csnd_clfc_3mto1y"] = csnd_clfc_3mto1y
        if csnd_clfc_cgdf1y is not UNSET:
            field_dict["csnd_clfc_cgdf1y"] = csnd_clfc_cgdf1y
        if csnd_clfc_cgdf1y_upto1m is not UNSET:
            field_dict["csnd_clfc_cgdf1y_upto1m"] = csnd_clfc_cgdf1y_upto1m
        if csnd_clfc_cgdf1y_1mto3m is not UNSET:
            field_dict["csnd_clfc_cgdf1y_1mto3m"] = csnd_clfc_cgdf1y_1mto3m
        if csnd_clfc_cgdf1y_3mto1y is not UNSET:
            field_dict["csnd_clfc_cgdf1y_3mto1y"] = csnd_clfc_cgdf1y_3mto1y
        if csnd_clfc_othcl is not UNSET:
            field_dict["csnd_clfc_othcl"] = csnd_clfc_othcl
        if csnd_clfc_othcl_upto1m is not UNSET:
            field_dict["csnd_clfc_othcl_upto1m"] = csnd_clfc_othcl_upto1m
        if csnd_clfc_othcl_1mto3m is not UNSET:
            field_dict["csnd_clfc_othcl_1mto3m"] = csnd_clfc_othcl_1mto3m
        if csnd_clfc_othcl_3mto1y is not UNSET:
            field_dict["csnd_clfc_othcl_3mto1y"] = csnd_clfc_othcl_3mto1y
        if csnd_fcsecwembopt is not UNSET:
            field_dict["csnd_fcsecwembopt"] = csnd_fcsecwembopt
        if csnd_uduccrlby is not UNSET:
            field_dict["csnd_uduccrlby"] = csnd_uduccrlby
        if csnd_uduccrlby_upto1m is not UNSET:
            field_dict["csnd_uduccrlby_upto1m"] = csnd_uduccrlby_upto1m
        if csnd_uduccrlby_1mto3m is not UNSET:
            field_dict["csnd_uduccrlby_1mto3m"] = csnd_uduccrlby_1mto3m
        if csnd_uduccrlby_3mto1y is not UNSET:
            field_dict["csnd_uduccrlby_3mto1y"] = csnd_uduccrlby_3mto1y
        if csnd_uduccrlby_oth is not UNSET:
            field_dict["csnd_uduccrlby_oth"] = csnd_uduccrlby_oth
        if csnd_uduccrlby_oth_upto1m is not UNSET:
            field_dict["csnd_uduccrlby_oth_upto1m"] = csnd_uduccrlby_oth_upto1m
        if csnd_uduccrlby_oth_1mto3m is not UNSET:
            field_dict["csnd_uduccrlby_oth_1mto3m"] = csnd_uduccrlby_oth_1mto3m
        if csnd_uduccrlby_oth_3mto1y is not UNSET:
            field_dict["csnd_uduccrlby_oth_3mto1y"] = csnd_uduccrlby_oth_3mto1y
        if csnd_uduccrlby_oth_auth is not UNSET:
            field_dict["csnd_uduccrlby_oth_auth"] = csnd_uduccrlby_oth_auth
        if csnd_uduccrlby_oth_auth_upto1m is not UNSET:
            field_dict["csnd_uduccrlby_oth_auth_upto1m"] = (
                csnd_uduccrlby_oth_auth_upto1m
            )
        if csnd_uduccrlby_oth_auth_1mto3m is not UNSET:
            field_dict["csnd_uduccrlby_oth_auth_1mto3m"] = (
                csnd_uduccrlby_oth_auth_1mto3m
            )
        if csnd_uduccrlby_oth_auth_3mto1y is not UNSET:
            field_dict["csnd_uduccrlby_oth_auth_3mto1y"] = (
                csnd_uduccrlby_oth_auth_3mto1y
            )
        if csnd_uduccrlby_oth_bis is not UNSET:
            field_dict["csnd_uduccrlby_oth_bis"] = csnd_uduccrlby_oth_bis
        if csnd_uduccrlby_oth_bis_upto1m is not UNSET:
            field_dict["csnd_uduccrlby_oth_bis_upto1m"] = csnd_uduccrlby_oth_bis_upto1m
        if csnd_uduccrlby_oth_bis_1mto3m is not UNSET:
            field_dict["csnd_uduccrlby_oth_bis_1mto3m"] = csnd_uduccrlby_oth_bis_1mto3m
        if csnd_uduccrlby_oth_bis_3mto1y is not UNSET:
            field_dict["csnd_uduccrlby_oth_bis_3mto1y"] = csnd_uduccrlby_oth_bis_3mto1y
        if csnd_uduccrlby_oth_imf is not UNSET:
            field_dict["csnd_uduccrlby_oth_imf"] = csnd_uduccrlby_oth_imf
        if csnd_uduccrlby_oth_imf_upto1m is not UNSET:
            field_dict["csnd_uduccrlby_oth_imf_upto1m"] = csnd_uduccrlby_oth_imf_upto1m
        if csnd_uduccrlby_oth_imf_1mto3m is not UNSET:
            field_dict["csnd_uduccrlby_oth_imf_1mto3m"] = csnd_uduccrlby_oth_imf_1mto3m
        if csnd_uduccrlby_oth_imf_3mto1y is not UNSET:
            field_dict["csnd_uduccrlby_oth_imf_3mto1y"] = csnd_uduccrlby_oth_imf_3mto1y
        if csnd_uduccrlby_oth_iorg is not UNSET:
            field_dict["csnd_uduccrlby_oth_iorg"] = csnd_uduccrlby_oth_iorg
        if csnd_uduccrlby_oth_iorg_upto1m is not UNSET:
            field_dict["csnd_uduccrlby_oth_iorg_upto1m"] = (
                csnd_uduccrlby_oth_iorg_upto1m
            )
        if csnd_uduccrlby_oth_iorg_1mto3m is not UNSET:
            field_dict["csnd_uduccrlby_oth_iorg_1mto3m"] = (
                csnd_uduccrlby_oth_iorg_1mto3m
            )
        if csnd_uduccrlby_oth_iorg_3mto1y is not UNSET:
            field_dict["csnd_uduccrlby_oth_iorg_3mto1y"] = (
                csnd_uduccrlby_oth_iorg_3mto1y
            )
        if csnd_uduccrlby_bkinhk is not UNSET:
            field_dict["csnd_uduccrlby_bkinhk"] = csnd_uduccrlby_bkinhk
        if csnd_uduccrlby_bkinhk_upto1m is not UNSET:
            field_dict["csnd_uduccrlby_bkinhk_upto1m"] = csnd_uduccrlby_bkinhk_upto1m
        if csnd_uduccrlby_bkinhk_1mto3m is not UNSET:
            field_dict["csnd_uduccrlby_bkinhk_1mto3m"] = csnd_uduccrlby_bkinhk_1mto3m
        if csnd_uduccrlby_bkinhk_3mto1y is not UNSET:
            field_dict["csnd_uduccrlby_bkinhk_3mto1y"] = csnd_uduccrlby_bkinhk_3mto1y
        if csnd_uduccrlby_bkouthk is not UNSET:
            field_dict["csnd_uduccrlby_bkouthk"] = csnd_uduccrlby_bkouthk
        if csnd_uduccrlby_bkouthk_upto1m is not UNSET:
            field_dict["csnd_uduccrlby_bkouthk_upto1m"] = csnd_uduccrlby_bkouthk_upto1m
        if csnd_uduccrlby_bkouthk_1mto3m is not UNSET:
            field_dict["csnd_uduccrlby_bkouthk_1mto3m"] = csnd_uduccrlby_bkouthk_1mto3m
        if csnd_uduccrlby_bkouthk_3mto1y is not UNSET:
            field_dict["csnd_uduccrlby_bkouthk_3mto1y"] = csnd_uduccrlby_bkouthk_3mto1y
        if csnd_uduccrlto is not UNSET:
            field_dict["csnd_uduccrlto"] = csnd_uduccrlto
        if csnd_uduccrlto_upto1m is not UNSET:
            field_dict["csnd_uduccrlto_upto1m"] = csnd_uduccrlto_upto1m
        if csnd_uduccrlto_1mto3m is not UNSET:
            field_dict["csnd_uduccrlto_1mto3m"] = csnd_uduccrlto_1mto3m
        if csnd_uduccrlto_3mto1y is not UNSET:
            field_dict["csnd_uduccrlto_3mto1y"] = csnd_uduccrlto_3mto1y
        if csnd_uduccrlto_oth is not UNSET:
            field_dict["csnd_uduccrlto_oth"] = csnd_uduccrlto_oth
        if csnd_uduccrlto_oth_upto1m is not UNSET:
            field_dict["csnd_uduccrlto_oth_upto1m"] = csnd_uduccrlto_oth_upto1m
        if csnd_uduccrlto_oth_1mto3m is not UNSET:
            field_dict["csnd_uduccrlto_oth_1mto3m"] = csnd_uduccrlto_oth_1mto3m
        if csnd_uduccrlto_oth_3mto1y is not UNSET:
            field_dict["csnd_uduccrlto_oth_3mto1y"] = csnd_uduccrlto_oth_3mto1y
        if csnd_uduccrlto_oth_auth is not UNSET:
            field_dict["csnd_uduccrlto_oth_auth"] = csnd_uduccrlto_oth_auth
        if csnd_uduccrlto_oth_auth_upto1m is not UNSET:
            field_dict["csnd_uduccrlto_oth_auth_upto1m"] = (
                csnd_uduccrlto_oth_auth_upto1m
            )
        if csnd_uduccrlto_oth_auth_1mto3m is not UNSET:
            field_dict["csnd_uduccrlto_oth_auth_1mto3m"] = (
                csnd_uduccrlto_oth_auth_1mto3m
            )
        if csnd_uduccrlto_oth_auth_3mto1y is not UNSET:
            field_dict["csnd_uduccrlto_oth_auth_3mto1y"] = (
                csnd_uduccrlto_oth_auth_3mto1y
            )
        if csnd_uduccrlto_oth_bis is not UNSET:
            field_dict["csnd_uduccrlto_oth_bis"] = csnd_uduccrlto_oth_bis
        if csnd_uduccrlto_oth_bis_upto1m is not UNSET:
            field_dict["csnd_uduccrlto_oth_bis_upto1m"] = csnd_uduccrlto_oth_bis_upto1m
        if csnd_uduccrlto_oth_bis_1mto3m is not UNSET:
            field_dict["csnd_uduccrlto_oth_bis_1mto3m"] = csnd_uduccrlto_oth_bis_1mto3m
        if csnd_uduccrlto_oth_bis_3mto1y is not UNSET:
            field_dict["csnd_uduccrlto_oth_bis_3mto1y"] = csnd_uduccrlto_oth_bis_3mto1y
        if csnd_uduccrlto_oth_imf is not UNSET:
            field_dict["csnd_uduccrlto_oth_imf"] = csnd_uduccrlto_oth_imf
        if csnd_uduccrlto_oth_imf_upto1m is not UNSET:
            field_dict["csnd_uduccrlto_oth_imf_upto1m"] = csnd_uduccrlto_oth_imf_upto1m
        if csnd_uduccrlto_oth_imf_1mto3m is not UNSET:
            field_dict["csnd_uduccrlto_oth_imf_1mto3m"] = csnd_uduccrlto_oth_imf_1mto3m
        if csnd_uduccrlto_oth_imf_3mto1y is not UNSET:
            field_dict["csnd_uduccrlto_oth_imf_3mto1y"] = csnd_uduccrlto_oth_imf_3mto1y
        if csnd_uduccrlto_oth_iorg is not UNSET:
            field_dict["csnd_uduccrlto_oth_iorg"] = csnd_uduccrlto_oth_iorg
        if csnd_uduccrlto_oth_iorg_upto1m is not UNSET:
            field_dict["csnd_uduccrlto_oth_iorg_upto1m"] = (
                csnd_uduccrlto_oth_iorg_upto1m
            )
        if csnd_uduccrlto_oth_iorg_1mto3m is not UNSET:
            field_dict["csnd_uduccrlto_oth_iorg_1mto3m"] = (
                csnd_uduccrlto_oth_iorg_1mto3m
            )
        if csnd_uduccrlto_oth_iorg_3mto1y is not UNSET:
            field_dict["csnd_uduccrlto_oth_iorg_3mto1y"] = (
                csnd_uduccrlto_oth_iorg_3mto1y
            )
        if csnd_uduccrlto_bkinhk is not UNSET:
            field_dict["csnd_uduccrlto_bkinhk"] = csnd_uduccrlto_bkinhk
        if csnd_uduccrlto_bkinhk_upto1m is not UNSET:
            field_dict["csnd_uduccrlto_bkinhk_upto1m"] = csnd_uduccrlto_bkinhk_upto1m
        if csnd_uduccrlto_bkinhk_1mto3m is not UNSET:
            field_dict["csnd_uduccrlto_bkinhk_1mto3m"] = csnd_uduccrlto_bkinhk_1mto3m
        if csnd_uduccrlto_bkinhk_3mto1y is not UNSET:
            field_dict["csnd_uduccrlto_bkinhk_3mto1y"] = csnd_uduccrlto_bkinhk_3mto1y
        if csnd_uduccrlto_bkouthk is not UNSET:
            field_dict["csnd_uduccrlto_bkouthk"] = csnd_uduccrlto_bkouthk
        if csnd_uduccrlto_bkouthk_upto1m is not UNSET:
            field_dict["csnd_uduccrlto_bkouthk_upto1m"] = csnd_uduccrlto_bkouthk_upto1m
        if csnd_uduccrlto_bkouthk_1mto3m is not UNSET:
            field_dict["csnd_uduccrlto_bkouthk_1mto3m"] = csnd_uduccrlto_bkouthk_1mto3m
        if csnd_uduccrlto_bkouthk_3mto1y is not UNSET:
            field_dict["csnd_uduccrlto_bkouthk_3mto1y"] = csnd_uduccrlto_bkouthk_3mto1y
        if csnd_aslp is not UNSET:
            field_dict["csnd_aslp"] = csnd_aslp
        if csnd_aslp_upto1m is not UNSET:
            field_dict["csnd_aslp_upto1m"] = csnd_aslp_upto1m
        if csnd_aslp_1mto3m is not UNSET:
            field_dict["csnd_aslp_1mto3m"] = csnd_aslp_1mto3m
        if csnd_aslp_3mto1y is not UNSET:
            field_dict["csnd_aslp_3mto1y"] = csnd_aslp_3mto1y
        if csnd_aslp_sp is not UNSET:
            field_dict["csnd_aslp_sp"] = csnd_aslp_sp
        if csnd_aslp_sp_upto1m is not UNSET:
            field_dict["csnd_aslp_sp_upto1m"] = csnd_aslp_sp_upto1m
        if csnd_aslp_sp_1mto3m is not UNSET:
            field_dict["csnd_aslp_sp_1mto3m"] = csnd_aslp_sp_1mto3m
        if csnd_aslp_sp_3mto1y is not UNSET:
            field_dict["csnd_aslp_sp_3mto1y"] = csnd_aslp_sp_3mto1y
        if csnd_aslp_sp_bp is not UNSET:
            field_dict["csnd_aslp_sp_bp"] = csnd_aslp_sp_bp
        if csnd_aslp_sp_bp_upto1m is not UNSET:
            field_dict["csnd_aslp_sp_bp_upto1m"] = csnd_aslp_sp_bp_upto1m
        if csnd_aslp_sp_bp_1mto3m is not UNSET:
            field_dict["csnd_aslp_sp_bp_1mto3m"] = csnd_aslp_sp_bp_1mto3m
        if csnd_aslp_sp_bp_3mto1y is not UNSET:
            field_dict["csnd_aslp_sp_bp_3mto1y"] = csnd_aslp_sp_bp_3mto1y
        if csnd_aslp_sp_wc is not UNSET:
            field_dict["csnd_aslp_sp_wc"] = csnd_aslp_sp_wc
        if csnd_aslp_sp_wc_upto1m is not UNSET:
            field_dict["csnd_aslp_sp_wc_upto1m"] = csnd_aslp_sp_wc_upto1m
        if csnd_aslp_sp_wc_1mto3m is not UNSET:
            field_dict["csnd_aslp_sp_wc_1mto3m"] = csnd_aslp_sp_wc_1mto3m
        if csnd_aslp_sp_wc_3mto1y is not UNSET:
            field_dict["csnd_aslp_sp_wc_3mto1y"] = csnd_aslp_sp_wc_3mto1y
        if csnd_aslp_lp is not UNSET:
            field_dict["csnd_aslp_lp"] = csnd_aslp_lp
        if csnd_aslp_lp_upto1m is not UNSET:
            field_dict["csnd_aslp_lp_upto1m"] = csnd_aslp_lp_upto1m
        if csnd_aslp_lp_1mto3m is not UNSET:
            field_dict["csnd_aslp_lp_1mto3m"] = csnd_aslp_lp_1mto3m
        if csnd_aslp_lp_3mto1y is not UNSET:
            field_dict["csnd_aslp_lp_3mto1y"] = csnd_aslp_lp_3mto1y
        if csnd_aslp_lp_bc is not UNSET:
            field_dict["csnd_aslp_lp_bc"] = csnd_aslp_lp_bc
        if csnd_aslp_lp_bc_upto1m is not UNSET:
            field_dict["csnd_aslp_lp_bc_upto1m"] = csnd_aslp_lp_bc_upto1m
        if csnd_aslp_lp_bc_1mto3m is not UNSET:
            field_dict["csnd_aslp_lp_bc_1mto3m"] = csnd_aslp_lp_bc_1mto3m
        if csnd_aslp_lp_bc_3mto1y is not UNSET:
            field_dict["csnd_aslp_lp_bc_3mto1y"] = csnd_aslp_lp_bc_3mto1y
        if csnd_aslp_lp_wp is not UNSET:
            field_dict["csnd_aslp_lp_wp"] = csnd_aslp_lp_wp
        if csnd_aslp_lp_wp_upto1m is not UNSET:
            field_dict["csnd_aslp_lp_wp_upto1m"] = csnd_aslp_lp_wp_upto1m
        if csnd_aslp_lp_wp_1mto3m is not UNSET:
            field_dict["csnd_aslp_lp_wp_1mto3m"] = csnd_aslp_lp_wp_1mto3m
        if csnd_aslp_lp_wp_3mto1y is not UNSET:
            field_dict["csnd_aslp_lp_wp_3mto1y"] = csnd_aslp_lp_wp_3mto1y
        if mm_spt_stdcd is not UNSET:
            field_dict["mm_spt_stdcd"] = mm_spt_stdcd
        if mm_spt_fid is not UNSET:
            field_dict["mm_spt_fid"] = mm_spt_fid
        if mm_spt_fid_ndf is not UNSET:
            field_dict["mm_spt_fid_ndf"] = mm_spt_fid_ndf
        if mm_spt_fid_ndf_sp is not UNSET:
            field_dict["mm_spt_fid_ndf_sp"] = mm_spt_fid_ndf_sp
        if mm_spt_fid_ndf_lp is not UNSET:
            field_dict["mm_spt_fid_ndf_lp"] = mm_spt_fid_ndf_lp
        if mm_spt_fid_oi is not UNSET:
            field_dict["mm_spt_fid_oi"] = mm_spt_fid_oi
        if mm_spt_pa is not UNSET:
            field_dict["mm_spt_pa"] = mm_spt_pa
        if mm_spt_pa_ra is not UNSET:
            field_dict["mm_spt_pa_ra"] = mm_spt_pa_ra
        if mm_spt_pa_ofca is not UNSET:
            field_dict["mm_spt_pa_ofca"] = mm_spt_pa_ofca
        if mm_spt_slr is not UNSET:
            field_dict["mm_spt_slr"] = mm_spt_slr
        if mm_spt_slr_lr_insi is not UNSET:
            field_dict["mm_spt_slr_lr_insi"] = mm_spt_slr_lr_insi
        if mm_spt_slr_lr_notinsi is not UNSET:
            field_dict["mm_spt_slr_lr_notinsi"] = mm_spt_slr_lr_notinsi
        if mm_spt_slr_ba_insi is not UNSET:
            field_dict["mm_spt_slr_ba_insi"] = mm_spt_slr_ba_insi
        if mm_spt_slr_ba_notinsi is not UNSET:
            field_dict["mm_spt_slr_ba_notinsi"] = mm_spt_slr_ba_notinsi
        if mm_spt_fda is not UNSET:
            field_dict["mm_spt_fda"] = mm_spt_fda
        if mm_spt_fda_forw is not UNSET:
            field_dict["mm_spt_fda_forw"] = mm_spt_fda_forw
        if mm_spt_fda_fut is not UNSET:
            field_dict["mm_spt_fda_fut"] = mm_spt_fda_fut
        if mm_spt_fda_swp is not UNSET:
            field_dict["mm_spt_fda_swp"] = mm_spt_fda_swp
        if mm_spt_fda_opt is not UNSET:
            field_dict["mm_spt_fda_opt"] = mm_spt_fda_opt
        if mm_spt_fda_oth is not UNSET:
            field_dict["mm_spt_fda_oth"] = mm_spt_fda_oth
        if mm_spt_dergt1y is not UNSET:
            field_dict["mm_spt_dergt1y"] = mm_spt_dergt1y
        if mm_spt_dergt1y_aslpf is not UNSET:
            field_dict["mm_spt_dergt1y_aslpf"] = mm_spt_dergt1y_aslpf
        if mm_spt_dergt1y_aslpf_sp is not UNSET:
            field_dict["mm_spt_dergt1y_aslpf_sp"] = mm_spt_dergt1y_aslpf_sp
        if mm_spt_dergt1y_aslpf_lp is not UNSET:
            field_dict["mm_spt_dergt1y_aslpf_lp"] = mm_spt_dergt1y_aslpf_lp
        if mm_spt_dergt1y_aslpfo is not UNSET:
            field_dict["mm_spt_dergt1y_aslpfo"] = mm_spt_dergt1y_aslpfo
        if mm_spt_dergt1y_aslpfo_sp is not UNSET:
            field_dict["mm_spt_dergt1y_aslpfo_sp"] = mm_spt_dergt1y_aslpfo_sp
        if mm_spt_dergt1y_aslpfo_sp_bp is not UNSET:
            field_dict["mm_spt_dergt1y_aslpfo_sp_bp"] = mm_spt_dergt1y_aslpfo_sp_bp
        if mm_spt_dergt1y_aslpfo_sp_wc is not UNSET:
            field_dict["mm_spt_dergt1y_aslpfo_sp_wc"] = mm_spt_dergt1y_aslpfo_sp_wc
        if mm_spt_dergt1y_aslpfo_lp is not UNSET:
            field_dict["mm_spt_dergt1y_aslpfo_lp"] = mm_spt_dergt1y_aslpfo_lp
        if mm_spt_dergt1y_aslpfo_lp_bc is not UNSET:
            field_dict["mm_spt_dergt1y_aslpfo_lp_bc"] = mm_spt_dergt1y_aslpfo_lp_bc
        if mm_spt_dergt1y_aslpfo_lp_wp is not UNSET:
            field_dict["mm_spt_dergt1y_aslpfo_lp_wp"] = mm_spt_dergt1y_aslpfo_lp_wp
        if mm_lfd_ccr is not UNSET:
            field_dict["mm_lfd_ccr"] = mm_lfd_ccr
        if mm_lfd_ccr_insdr is not UNSET:
            field_dict["mm_lfd_ccr_insdr"] = mm_lfd_ccr_insdr
        if mm_lfd_ccr_insdr_eur is not UNSET:
            field_dict["mm_lfd_ccr_insdr_eur"] = mm_lfd_ccr_insdr_eur
        if mm_lfd_ccr_insdr_jpy is not UNSET:
            field_dict["mm_lfd_ccr_insdr_jpy"] = mm_lfd_ccr_insdr_jpy
        if mm_lfd_ccr_insdr_gbp is not UNSET:
            field_dict["mm_lfd_ccr_insdr_gbp"] = mm_lfd_ccr_insdr_gbp
        if mm_lfd_ccr_insdr_usd is not UNSET:
            field_dict["mm_lfd_ccr_insdr_usd"] = mm_lfd_ccr_insdr_usd
        if mm_lfd_ccr_notinsdr is not UNSET:
            field_dict["mm_lfd_ccr_notinsdr"] = mm_lfd_ccr_notinsdr

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

        ora = d.pop("ora", UNSET)

        ora_fcrsv = d.pop("ora_fcrsv", UNSET)

        ora_fcrsv_sec = d.pop("ora_fcrsv_sec", UNSET)

        ora_fcrsv_sec_hqinhk = d.pop("ora_fcrsv_sec_hqinhk", UNSET)

        ora_fcrsv_tcd = d.pop("ora_fcrsv_tcd", UNSET)

        ora_fcrsv_tcd_cbank = d.pop("ora_fcrsv_ tcd_cbank", UNSET)

        ora_fcrsv_tcd_hqinhk = d.pop("ora_fcrsv_tcd_hqinhk", UNSET)

        ora_fcrsv_tcd_hqinhk_locabd = d.pop("ora_fcrsv_tcd_hqinhk_locabd", UNSET)

        ora_fcrsv_tcd_hqouthk = d.pop("ora_fcrsv_tcd_hqouthk", UNSET)

        ora_fcrsv_tcd_hqouthk_lochk = d.pop("ora_fcrsv_tcd_hqouthk_lochk", UNSET)

        ora_imfrsvpos = d.pop("ora_imfrsvpos", UNSET)

        ora_sdr = d.pop("ora_sdr", UNSET)

        ora_gold = d.pop("ora_gold", UNSET)

        ora_gold_oz = d.pop("ora_gold_oz", UNSET)

        ora_othra = d.pop("ora_othra", UNSET)

        ora_othra_finderiv = d.pop("ora_othra_finderiv", UNSET)

        ora_othra_loannonbkresd = d.pop("ora_othra_loannonbkresd", UNSET)

        ora_othra_other = d.pop("ora_othra_other", UNSET)

        ofca = d.pop("ofca", UNSET)

        ofca_secnotinora = d.pop("ofca_secnotinora", UNSET)

        ofca_depnotinora = d.pop("ofca_depnotinora", UNSET)

        ofca_loannotinora = d.pop("ofca_loannotinora", UNSET)

        ofca_finderivnotinora = d.pop("ofca_finderivnotinora", UNSET)

        ofca_goldnotinora = d.pop("ofca_goldnotinora", UNSET)

        ofca_other = d.pop("ofca_other", UNSET)

        psnd_fclsd = d.pop("psnd_fclsd", UNSET)

        psnd_fclsd_upto1m = d.pop("psnd_fclsd_upto1m", UNSET)

        psnd_fclsd_1mto3m = d.pop("psnd_fclsd_1mto3m", UNSET)

        psnd_fclsd_3mto1y = d.pop("psnd_fclsd_3mto1y", UNSET)

        psnd_fclsd_ofprin = d.pop("psnd_fclsd_ofprin", UNSET)

        psnd_fclsd_ofprin_upto1m = d.pop("psnd_fclsd_ofprin_upto1m", UNSET)

        psnd_fclsd_ofprin_1mto3m = d.pop("psnd_fclsd_ofprin_1mto3m", UNSET)

        psnd_fclsd_ofprin_3mto1y = d.pop("psnd_fclsd_ofprin_3mto1y", UNSET)

        psnd_fclsd_ofint = d.pop("psnd_fclsd_ofint", UNSET)

        psnd_fclsd_ofint_upto1m = d.pop("psnd_fclsd_ofint_upto1m", UNSET)

        psnd_fclsd_ofint_1mto3m = d.pop("psnd_fclsd_ofint_1mto3m", UNSET)

        psnd_fclsd_ofint_3mto1y = d.pop("psnd_fclsd_ofint_3mto1y", UNSET)

        psnd_fclsd_ifprin = d.pop("psnd_fclsd_ifprin", UNSET)

        psnd_fclsd_ifprin_upto1m = d.pop("psnd_fclsd_ifprin_upto1m", UNSET)

        psnd_fclsd_ifprin_1mto3m = d.pop("psnd_fclsd_ifprin_1mto3m", UNSET)

        psnd_fclsd_ifprin_3mto1y = d.pop("psnd_fclsd_ifprin_3mto1y", UNSET)

        psnd_fclsd_ifint = d.pop("psnd_fclsd_ifint", UNSET)

        psnd_fclsd_ifint_upto1m = d.pop("psnd_fclsd_ifint_upto1m", UNSET)

        psnd_fclsd_ifint_1mto3m = d.pop("psnd_fclsd_ifint_1mto3m", UNSET)

        psnd_fclsd_ifint_3mto1y = d.pop("psnd_fclsd_ifint_3mto1y", UNSET)

        psnd_aslp = d.pop("psnd_aslp", UNSET)

        psnd_aslp_upto1m = d.pop("psnd_aslp_upto1m", UNSET)

        psnd_aslp_1mto3m = d.pop("psnd_aslp_1mto3m", UNSET)

        psnd_aslp_3mto1y = d.pop("psnd_aslp_3mto1y", UNSET)

        psnd_aslp_shpos = d.pop("psnd_aslp_shpos", UNSET)

        psnd_aslp_shpos_upto1m = d.pop("psnd_aslp_shpos_upto1m", UNSET)

        psnd_aslp_shpos_1mto3m = d.pop("psnd_aslp_shpos_1mto3m", UNSET)

        psnd_aslp_shpos_3mto1y = d.pop("psnd_aslp_shpos_3mto1y", UNSET)

        psnd_aslp_lgpos = d.pop("psnd_aslp_lgpos", UNSET)

        psnd_aslp_lgpos_upto1m = d.pop("psnd_aslp_lgpos_upto1m", UNSET)

        psnd_aslp_lgpos_1mto3m = d.pop("psnd_aslp_lgpos_1mto3m", UNSET)

        psnd_aslp_lgpos_3mto1y = d.pop("psnd_aslp_lgpos_3mto1y", UNSET)

        psnd_oth = d.pop("psnd_oth", UNSET)

        psnd_oth_upto1m = d.pop("psnd_oth_upto1m", UNSET)

        psnd_oth_1mto3m = d.pop("psnd_oth_1mto3m", UNSET)

        psnd_oth_3mto1y = d.pop("psnd_oth_3mto1y", UNSET)

        psnd_oth_ofrepos = d.pop("psnd_oth_ofrepos", UNSET)

        psnd_oth_ofrepos_upto1m = d.pop("psnd_oth_ofrepos_upto1m", UNSET)

        psnd_oth_ofrepos_1mto3m = d.pop("psnd_oth_ofrepos_1mto3m", UNSET)

        psnd_oth_ofrepos_3mto1y = d.pop("psnd_oth_ofrepos_3mto1y", UNSET)

        psnd_oth_ifrrepos = d.pop("psnd_oth_ifrrepos", UNSET)

        psnd_oth_ifrrepos_upto1m = d.pop("psnd_oth_ifrrepos_upto1m", UNSET)

        psnd_oth_ifrrepos_1mto3m = d.pop("psnd_oth_ifrrepos_1mto3m", UNSET)

        psnd_oth_ifrrepos_3mto1y = d.pop("psnd_oth_ifrrepos_3mto1y", UNSET)

        psnd_oth_tracrneg = d.pop("psnd_oth_tracrneg", UNSET)

        psnd_oth_tracrneg_upto1m = d.pop("psnd_oth_tracrneg_upto1m", UNSET)

        psnd_oth_tracrneg_1mto3m = d.pop("psnd_oth_tracrneg_1mto3m", UNSET)

        psnd_oth_tracrneg_3mto1y = d.pop("psnd_oth_tracrneg_3mto1y", UNSET)

        psnd_oth_tracrpos = d.pop("psnd_oth_tracrpos", UNSET)

        psnd_oth_tracrpos_upto1m = d.pop("psnd_oth_tracrpos_upto1m", UNSET)

        psnd_oth_tracrpos_1mto3m = d.pop("psnd_oth_tracrpos_1mto3m", UNSET)

        psnd_oth_tracrpos_3mto1y = d.pop("psnd_oth_tracrpos_3mto1y", UNSET)

        psnd_oth_acctpay = d.pop("psnd_oth_acctpay", UNSET)

        psnd_oth_acctpay_upto1m = d.pop("psnd_oth_acctpay_upto1m", UNSET)

        psnd_oth_acctpay_1mto3m = d.pop("psnd_oth_acctpay_1mto3m", UNSET)

        psnd_oth_acctpay_3mto1y = d.pop("psnd_oth_acctpay_3mto1y", UNSET)

        psnd_oth_acctrecv = d.pop("psnd_oth_acctrecv", UNSET)

        psnd_oth_acctrecv_upto1m = d.pop("psnd_oth_acctrecv_upto1m", UNSET)

        psnd_oth_acctrecv_1mto3m = d.pop("psnd_oth_acctrecv_1mto3m", UNSET)

        psnd_oth_acctrecv_3mto1y = d.pop("psnd_oth_acctrecv_3mto1y", UNSET)

        csnd_clfc = d.pop("csnd_clfc", UNSET)

        csnd_clfc_upto1m = d.pop("csnd_clfc_upto1m", UNSET)

        csnd_clfc_1mto3m = d.pop("csnd_clfc_1mto3m", UNSET)

        csnd_clfc_3mto1y = d.pop("csnd_clfc_3mto1y", UNSET)

        csnd_clfc_cgdf1y = d.pop("csnd_clfc_cgdf1y", UNSET)

        csnd_clfc_cgdf1y_upto1m = d.pop("csnd_clfc_cgdf1y_upto1m", UNSET)

        csnd_clfc_cgdf1y_1mto3m = d.pop("csnd_clfc_cgdf1y_1mto3m", UNSET)

        csnd_clfc_cgdf1y_3mto1y = d.pop("csnd_clfc_cgdf1y_3mto1y", UNSET)

        csnd_clfc_othcl = d.pop("csnd_clfc_othcl", UNSET)

        csnd_clfc_othcl_upto1m = d.pop("csnd_clfc_othcl_upto1m", UNSET)

        csnd_clfc_othcl_1mto3m = d.pop("csnd_clfc_othcl_1mto3m", UNSET)

        csnd_clfc_othcl_3mto1y = d.pop("csnd_clfc_othcl_3mto1y", UNSET)

        csnd_fcsecwembopt = d.pop("csnd_fcsecwembopt", UNSET)

        csnd_uduccrlby = d.pop("csnd_uduccrlby", UNSET)

        csnd_uduccrlby_upto1m = d.pop("csnd_uduccrlby_upto1m", UNSET)

        csnd_uduccrlby_1mto3m = d.pop("csnd_uduccrlby_1mto3m", UNSET)

        csnd_uduccrlby_3mto1y = d.pop("csnd_uduccrlby_3mto1y", UNSET)

        csnd_uduccrlby_oth = d.pop("csnd_uduccrlby_oth", UNSET)

        csnd_uduccrlby_oth_upto1m = d.pop("csnd_uduccrlby_oth_upto1m", UNSET)

        csnd_uduccrlby_oth_1mto3m = d.pop("csnd_uduccrlby_oth_1mto3m", UNSET)

        csnd_uduccrlby_oth_3mto1y = d.pop("csnd_uduccrlby_oth_3mto1y", UNSET)

        csnd_uduccrlby_oth_auth = d.pop("csnd_uduccrlby_oth_auth", UNSET)

        csnd_uduccrlby_oth_auth_upto1m = d.pop("csnd_uduccrlby_oth_auth_upto1m", UNSET)

        csnd_uduccrlby_oth_auth_1mto3m = d.pop("csnd_uduccrlby_oth_auth_1mto3m", UNSET)

        csnd_uduccrlby_oth_auth_3mto1y = d.pop("csnd_uduccrlby_oth_auth_3mto1y", UNSET)

        csnd_uduccrlby_oth_bis = d.pop("csnd_uduccrlby_oth_bis", UNSET)

        csnd_uduccrlby_oth_bis_upto1m = d.pop("csnd_uduccrlby_oth_bis_upto1m", UNSET)

        csnd_uduccrlby_oth_bis_1mto3m = d.pop("csnd_uduccrlby_oth_bis_1mto3m", UNSET)

        csnd_uduccrlby_oth_bis_3mto1y = d.pop("csnd_uduccrlby_oth_bis_3mto1y", UNSET)

        csnd_uduccrlby_oth_imf = d.pop("csnd_uduccrlby_oth_imf", UNSET)

        csnd_uduccrlby_oth_imf_upto1m = d.pop("csnd_uduccrlby_oth_imf_upto1m", UNSET)

        csnd_uduccrlby_oth_imf_1mto3m = d.pop("csnd_uduccrlby_oth_imf_1mto3m", UNSET)

        csnd_uduccrlby_oth_imf_3mto1y = d.pop("csnd_uduccrlby_oth_imf_3mto1y", UNSET)

        csnd_uduccrlby_oth_iorg = d.pop("csnd_uduccrlby_oth_iorg", UNSET)

        csnd_uduccrlby_oth_iorg_upto1m = d.pop("csnd_uduccrlby_oth_iorg_upto1m", UNSET)

        csnd_uduccrlby_oth_iorg_1mto3m = d.pop("csnd_uduccrlby_oth_iorg_1mto3m", UNSET)

        csnd_uduccrlby_oth_iorg_3mto1y = d.pop("csnd_uduccrlby_oth_iorg_3mto1y", UNSET)

        csnd_uduccrlby_bkinhk = d.pop("csnd_uduccrlby_bkinhk", UNSET)

        csnd_uduccrlby_bkinhk_upto1m = d.pop("csnd_uduccrlby_bkinhk_upto1m", UNSET)

        csnd_uduccrlby_bkinhk_1mto3m = d.pop("csnd_uduccrlby_bkinhk_1mto3m", UNSET)

        csnd_uduccrlby_bkinhk_3mto1y = d.pop("csnd_uduccrlby_bkinhk_3mto1y", UNSET)

        csnd_uduccrlby_bkouthk = d.pop("csnd_uduccrlby_bkouthk", UNSET)

        csnd_uduccrlby_bkouthk_upto1m = d.pop("csnd_uduccrlby_bkouthk_upto1m", UNSET)

        csnd_uduccrlby_bkouthk_1mto3m = d.pop("csnd_uduccrlby_bkouthk_1mto3m", UNSET)

        csnd_uduccrlby_bkouthk_3mto1y = d.pop("csnd_uduccrlby_bkouthk_3mto1y", UNSET)

        csnd_uduccrlto = d.pop("csnd_uduccrlto", UNSET)

        csnd_uduccrlto_upto1m = d.pop("csnd_uduccrlto_upto1m", UNSET)

        csnd_uduccrlto_1mto3m = d.pop("csnd_uduccrlto_1mto3m", UNSET)

        csnd_uduccrlto_3mto1y = d.pop("csnd_uduccrlto_3mto1y", UNSET)

        csnd_uduccrlto_oth = d.pop("csnd_uduccrlto_oth", UNSET)

        csnd_uduccrlto_oth_upto1m = d.pop("csnd_uduccrlto_oth_upto1m", UNSET)

        csnd_uduccrlto_oth_1mto3m = d.pop("csnd_uduccrlto_oth_1mto3m", UNSET)

        csnd_uduccrlto_oth_3mto1y = d.pop("csnd_uduccrlto_oth_3mto1y", UNSET)

        csnd_uduccrlto_oth_auth = d.pop("csnd_uduccrlto_oth_auth", UNSET)

        csnd_uduccrlto_oth_auth_upto1m = d.pop("csnd_uduccrlto_oth_auth_upto1m", UNSET)

        csnd_uduccrlto_oth_auth_1mto3m = d.pop("csnd_uduccrlto_oth_auth_1mto3m", UNSET)

        csnd_uduccrlto_oth_auth_3mto1y = d.pop("csnd_uduccrlto_oth_auth_3mto1y", UNSET)

        csnd_uduccrlto_oth_bis = d.pop("csnd_uduccrlto_oth_bis", UNSET)

        csnd_uduccrlto_oth_bis_upto1m = d.pop("csnd_uduccrlto_oth_bis_upto1m", UNSET)

        csnd_uduccrlto_oth_bis_1mto3m = d.pop("csnd_uduccrlto_oth_bis_1mto3m", UNSET)

        csnd_uduccrlto_oth_bis_3mto1y = d.pop("csnd_uduccrlto_oth_bis_3mto1y", UNSET)

        csnd_uduccrlto_oth_imf = d.pop("csnd_uduccrlto_oth_imf", UNSET)

        csnd_uduccrlto_oth_imf_upto1m = d.pop("csnd_uduccrlto_oth_imf_upto1m", UNSET)

        csnd_uduccrlto_oth_imf_1mto3m = d.pop("csnd_uduccrlto_oth_imf_1mto3m", UNSET)

        csnd_uduccrlto_oth_imf_3mto1y = d.pop("csnd_uduccrlto_oth_imf_3mto1y", UNSET)

        csnd_uduccrlto_oth_iorg = d.pop("csnd_uduccrlto_oth_iorg", UNSET)

        csnd_uduccrlto_oth_iorg_upto1m = d.pop("csnd_uduccrlto_oth_iorg_upto1m", UNSET)

        csnd_uduccrlto_oth_iorg_1mto3m = d.pop("csnd_uduccrlto_oth_iorg_1mto3m", UNSET)

        csnd_uduccrlto_oth_iorg_3mto1y = d.pop("csnd_uduccrlto_oth_iorg_3mto1y", UNSET)

        csnd_uduccrlto_bkinhk = d.pop("csnd_uduccrlto_bkinhk", UNSET)

        csnd_uduccrlto_bkinhk_upto1m = d.pop("csnd_uduccrlto_bkinhk_upto1m", UNSET)

        csnd_uduccrlto_bkinhk_1mto3m = d.pop("csnd_uduccrlto_bkinhk_1mto3m", UNSET)

        csnd_uduccrlto_bkinhk_3mto1y = d.pop("csnd_uduccrlto_bkinhk_3mto1y", UNSET)

        csnd_uduccrlto_bkouthk = d.pop("csnd_uduccrlto_bkouthk", UNSET)

        csnd_uduccrlto_bkouthk_upto1m = d.pop("csnd_uduccrlto_bkouthk_upto1m", UNSET)

        csnd_uduccrlto_bkouthk_1mto3m = d.pop("csnd_uduccrlto_bkouthk_1mto3m", UNSET)

        csnd_uduccrlto_bkouthk_3mto1y = d.pop("csnd_uduccrlto_bkouthk_3mto1y", UNSET)

        csnd_aslp = d.pop("csnd_aslp", UNSET)

        csnd_aslp_upto1m = d.pop("csnd_aslp_upto1m", UNSET)

        csnd_aslp_1mto3m = d.pop("csnd_aslp_1mto3m", UNSET)

        csnd_aslp_3mto1y = d.pop("csnd_aslp_3mto1y", UNSET)

        csnd_aslp_sp = d.pop("csnd_aslp_sp", UNSET)

        csnd_aslp_sp_upto1m = d.pop("csnd_aslp_sp_upto1m", UNSET)

        csnd_aslp_sp_1mto3m = d.pop("csnd_aslp_sp_1mto3m", UNSET)

        csnd_aslp_sp_3mto1y = d.pop("csnd_aslp_sp_3mto1y", UNSET)

        csnd_aslp_sp_bp = d.pop("csnd_aslp_sp_bp", UNSET)

        csnd_aslp_sp_bp_upto1m = d.pop("csnd_aslp_sp_bp_upto1m", UNSET)

        csnd_aslp_sp_bp_1mto3m = d.pop("csnd_aslp_sp_bp_1mto3m", UNSET)

        csnd_aslp_sp_bp_3mto1y = d.pop("csnd_aslp_sp_bp_3mto1y", UNSET)

        csnd_aslp_sp_wc = d.pop("csnd_aslp_sp_wc", UNSET)

        csnd_aslp_sp_wc_upto1m = d.pop("csnd_aslp_sp_wc_upto1m", UNSET)

        csnd_aslp_sp_wc_1mto3m = d.pop("csnd_aslp_sp_wc_1mto3m", UNSET)

        csnd_aslp_sp_wc_3mto1y = d.pop("csnd_aslp_sp_wc_3mto1y", UNSET)

        csnd_aslp_lp = d.pop("csnd_aslp_lp", UNSET)

        csnd_aslp_lp_upto1m = d.pop("csnd_aslp_lp_upto1m", UNSET)

        csnd_aslp_lp_1mto3m = d.pop("csnd_aslp_lp_1mto3m", UNSET)

        csnd_aslp_lp_3mto1y = d.pop("csnd_aslp_lp_3mto1y", UNSET)

        csnd_aslp_lp_bc = d.pop("csnd_aslp_lp_bc", UNSET)

        csnd_aslp_lp_bc_upto1m = d.pop("csnd_aslp_lp_bc_upto1m", UNSET)

        csnd_aslp_lp_bc_1mto3m = d.pop("csnd_aslp_lp_bc_1mto3m", UNSET)

        csnd_aslp_lp_bc_3mto1y = d.pop("csnd_aslp_lp_bc_3mto1y", UNSET)

        csnd_aslp_lp_wp = d.pop("csnd_aslp_lp_wp", UNSET)

        csnd_aslp_lp_wp_upto1m = d.pop("csnd_aslp_lp_wp_upto1m", UNSET)

        csnd_aslp_lp_wp_1mto3m = d.pop("csnd_aslp_lp_wp_1mto3m", UNSET)

        csnd_aslp_lp_wp_3mto1y = d.pop("csnd_aslp_lp_wp_3mto1y", UNSET)

        mm_spt_stdcd = d.pop("mm_spt_stdcd", UNSET)

        mm_spt_fid = d.pop("mm_spt_fid", UNSET)

        mm_spt_fid_ndf = d.pop("mm_spt_fid_ndf", UNSET)

        mm_spt_fid_ndf_sp = d.pop("mm_spt_fid_ndf_sp", UNSET)

        mm_spt_fid_ndf_lp = d.pop("mm_spt_fid_ndf_lp", UNSET)

        mm_spt_fid_oi = d.pop("mm_spt_fid_oi", UNSET)

        mm_spt_pa = d.pop("mm_spt_pa", UNSET)

        mm_spt_pa_ra = d.pop("mm_spt_pa_ra", UNSET)

        mm_spt_pa_ofca = d.pop("mm_spt_pa_ofca", UNSET)

        mm_spt_slr = d.pop("mm_spt_slr", UNSET)

        mm_spt_slr_lr_insi = d.pop("mm_spt_slr_lr_insi", UNSET)

        mm_spt_slr_lr_notinsi = d.pop("mm_spt_slr_lr_notinsi", UNSET)

        mm_spt_slr_ba_insi = d.pop("mm_spt_slr_ba_insi", UNSET)

        mm_spt_slr_ba_notinsi = d.pop("mm_spt_slr_ba_notinsi", UNSET)

        mm_spt_fda = d.pop("mm_spt_fda", UNSET)

        mm_spt_fda_forw = d.pop("mm_spt_fda_forw", UNSET)

        mm_spt_fda_fut = d.pop("mm_spt_fda_fut", UNSET)

        mm_spt_fda_swp = d.pop("mm_spt_fda_swp", UNSET)

        mm_spt_fda_opt = d.pop("mm_spt_fda_opt", UNSET)

        mm_spt_fda_oth = d.pop("mm_spt_fda_oth", UNSET)

        mm_spt_dergt1y = d.pop("mm_spt_dergt1y", UNSET)

        mm_spt_dergt1y_aslpf = d.pop("mm_spt_dergt1y_aslpf", UNSET)

        mm_spt_dergt1y_aslpf_sp = d.pop("mm_spt_dergt1y_aslpf_sp", UNSET)

        mm_spt_dergt1y_aslpf_lp = d.pop("mm_spt_dergt1y_aslpf_lp", UNSET)

        mm_spt_dergt1y_aslpfo = d.pop("mm_spt_dergt1y_aslpfo", UNSET)

        mm_spt_dergt1y_aslpfo_sp = d.pop("mm_spt_dergt1y_aslpfo_sp", UNSET)

        mm_spt_dergt1y_aslpfo_sp_bp = d.pop("mm_spt_dergt1y_aslpfo_sp_bp", UNSET)

        mm_spt_dergt1y_aslpfo_sp_wc = d.pop("mm_spt_dergt1y_aslpfo_sp_wc", UNSET)

        mm_spt_dergt1y_aslpfo_lp = d.pop("mm_spt_dergt1y_aslpfo_lp", UNSET)

        mm_spt_dergt1y_aslpfo_lp_bc = d.pop("mm_spt_dergt1y_aslpfo_lp_bc", UNSET)

        mm_spt_dergt1y_aslpfo_lp_wp = d.pop("mm_spt_dergt1y_aslpfo_lp_wp", UNSET)

        mm_lfd_ccr = d.pop("mm_lfd_ccr", UNSET)

        mm_lfd_ccr_insdr = d.pop("mm_lfd_ccr_insdr", UNSET)

        mm_lfd_ccr_insdr_eur = d.pop("mm_lfd_ccr_insdr_eur", UNSET)

        mm_lfd_ccr_insdr_jpy = d.pop("mm_lfd_ccr_insdr_jpy", UNSET)

        mm_lfd_ccr_insdr_gbp = d.pop("mm_lfd_ccr_insdr_gbp", UNSET)

        mm_lfd_ccr_insdr_usd = d.pop("mm_lfd_ccr_insdr_usd", UNSET)

        mm_lfd_ccr_notinsdr = d.pop("mm_lfd_ccr_notinsdr", UNSET)

        record = cls(
            end_of_month=end_of_month,
            ora=ora,
            ora_fcrsv=ora_fcrsv,
            ora_fcrsv_sec=ora_fcrsv_sec,
            ora_fcrsv_sec_hqinhk=ora_fcrsv_sec_hqinhk,
            ora_fcrsv_tcd=ora_fcrsv_tcd,
            ora_fcrsv_tcd_cbank=ora_fcrsv_tcd_cbank,
            ora_fcrsv_tcd_hqinhk=ora_fcrsv_tcd_hqinhk,
            ora_fcrsv_tcd_hqinhk_locabd=ora_fcrsv_tcd_hqinhk_locabd,
            ora_fcrsv_tcd_hqouthk=ora_fcrsv_tcd_hqouthk,
            ora_fcrsv_tcd_hqouthk_lochk=ora_fcrsv_tcd_hqouthk_lochk,
            ora_imfrsvpos=ora_imfrsvpos,
            ora_sdr=ora_sdr,
            ora_gold=ora_gold,
            ora_gold_oz=ora_gold_oz,
            ora_othra=ora_othra,
            ora_othra_finderiv=ora_othra_finderiv,
            ora_othra_loannonbkresd=ora_othra_loannonbkresd,
            ora_othra_other=ora_othra_other,
            ofca=ofca,
            ofca_secnotinora=ofca_secnotinora,
            ofca_depnotinora=ofca_depnotinora,
            ofca_loannotinora=ofca_loannotinora,
            ofca_finderivnotinora=ofca_finderivnotinora,
            ofca_goldnotinora=ofca_goldnotinora,
            ofca_other=ofca_other,
            psnd_fclsd=psnd_fclsd,
            psnd_fclsd_upto1m=psnd_fclsd_upto1m,
            psnd_fclsd_1mto3m=psnd_fclsd_1mto3m,
            psnd_fclsd_3mto1y=psnd_fclsd_3mto1y,
            psnd_fclsd_ofprin=psnd_fclsd_ofprin,
            psnd_fclsd_ofprin_upto1m=psnd_fclsd_ofprin_upto1m,
            psnd_fclsd_ofprin_1mto3m=psnd_fclsd_ofprin_1mto3m,
            psnd_fclsd_ofprin_3mto1y=psnd_fclsd_ofprin_3mto1y,
            psnd_fclsd_ofint=psnd_fclsd_ofint,
            psnd_fclsd_ofint_upto1m=psnd_fclsd_ofint_upto1m,
            psnd_fclsd_ofint_1mto3m=psnd_fclsd_ofint_1mto3m,
            psnd_fclsd_ofint_3mto1y=psnd_fclsd_ofint_3mto1y,
            psnd_fclsd_ifprin=psnd_fclsd_ifprin,
            psnd_fclsd_ifprin_upto1m=psnd_fclsd_ifprin_upto1m,
            psnd_fclsd_ifprin_1mto3m=psnd_fclsd_ifprin_1mto3m,
            psnd_fclsd_ifprin_3mto1y=psnd_fclsd_ifprin_3mto1y,
            psnd_fclsd_ifint=psnd_fclsd_ifint,
            psnd_fclsd_ifint_upto1m=psnd_fclsd_ifint_upto1m,
            psnd_fclsd_ifint_1mto3m=psnd_fclsd_ifint_1mto3m,
            psnd_fclsd_ifint_3mto1y=psnd_fclsd_ifint_3mto1y,
            psnd_aslp=psnd_aslp,
            psnd_aslp_upto1m=psnd_aslp_upto1m,
            psnd_aslp_1mto3m=psnd_aslp_1mto3m,
            psnd_aslp_3mto1y=psnd_aslp_3mto1y,
            psnd_aslp_shpos=psnd_aslp_shpos,
            psnd_aslp_shpos_upto1m=psnd_aslp_shpos_upto1m,
            psnd_aslp_shpos_1mto3m=psnd_aslp_shpos_1mto3m,
            psnd_aslp_shpos_3mto1y=psnd_aslp_shpos_3mto1y,
            psnd_aslp_lgpos=psnd_aslp_lgpos,
            psnd_aslp_lgpos_upto1m=psnd_aslp_lgpos_upto1m,
            psnd_aslp_lgpos_1mto3m=psnd_aslp_lgpos_1mto3m,
            psnd_aslp_lgpos_3mto1y=psnd_aslp_lgpos_3mto1y,
            psnd_oth=psnd_oth,
            psnd_oth_upto1m=psnd_oth_upto1m,
            psnd_oth_1mto3m=psnd_oth_1mto3m,
            psnd_oth_3mto1y=psnd_oth_3mto1y,
            psnd_oth_ofrepos=psnd_oth_ofrepos,
            psnd_oth_ofrepos_upto1m=psnd_oth_ofrepos_upto1m,
            psnd_oth_ofrepos_1mto3m=psnd_oth_ofrepos_1mto3m,
            psnd_oth_ofrepos_3mto1y=psnd_oth_ofrepos_3mto1y,
            psnd_oth_ifrrepos=psnd_oth_ifrrepos,
            psnd_oth_ifrrepos_upto1m=psnd_oth_ifrrepos_upto1m,
            psnd_oth_ifrrepos_1mto3m=psnd_oth_ifrrepos_1mto3m,
            psnd_oth_ifrrepos_3mto1y=psnd_oth_ifrrepos_3mto1y,
            psnd_oth_tracrneg=psnd_oth_tracrneg,
            psnd_oth_tracrneg_upto1m=psnd_oth_tracrneg_upto1m,
            psnd_oth_tracrneg_1mto3m=psnd_oth_tracrneg_1mto3m,
            psnd_oth_tracrneg_3mto1y=psnd_oth_tracrneg_3mto1y,
            psnd_oth_tracrpos=psnd_oth_tracrpos,
            psnd_oth_tracrpos_upto1m=psnd_oth_tracrpos_upto1m,
            psnd_oth_tracrpos_1mto3m=psnd_oth_tracrpos_1mto3m,
            psnd_oth_tracrpos_3mto1y=psnd_oth_tracrpos_3mto1y,
            psnd_oth_acctpay=psnd_oth_acctpay,
            psnd_oth_acctpay_upto1m=psnd_oth_acctpay_upto1m,
            psnd_oth_acctpay_1mto3m=psnd_oth_acctpay_1mto3m,
            psnd_oth_acctpay_3mto1y=psnd_oth_acctpay_3mto1y,
            psnd_oth_acctrecv=psnd_oth_acctrecv,
            psnd_oth_acctrecv_upto1m=psnd_oth_acctrecv_upto1m,
            psnd_oth_acctrecv_1mto3m=psnd_oth_acctrecv_1mto3m,
            psnd_oth_acctrecv_3mto1y=psnd_oth_acctrecv_3mto1y,
            csnd_clfc=csnd_clfc,
            csnd_clfc_upto1m=csnd_clfc_upto1m,
            csnd_clfc_1mto3m=csnd_clfc_1mto3m,
            csnd_clfc_3mto1y=csnd_clfc_3mto1y,
            csnd_clfc_cgdf1y=csnd_clfc_cgdf1y,
            csnd_clfc_cgdf1y_upto1m=csnd_clfc_cgdf1y_upto1m,
            csnd_clfc_cgdf1y_1mto3m=csnd_clfc_cgdf1y_1mto3m,
            csnd_clfc_cgdf1y_3mto1y=csnd_clfc_cgdf1y_3mto1y,
            csnd_clfc_othcl=csnd_clfc_othcl,
            csnd_clfc_othcl_upto1m=csnd_clfc_othcl_upto1m,
            csnd_clfc_othcl_1mto3m=csnd_clfc_othcl_1mto3m,
            csnd_clfc_othcl_3mto1y=csnd_clfc_othcl_3mto1y,
            csnd_fcsecwembopt=csnd_fcsecwembopt,
            csnd_uduccrlby=csnd_uduccrlby,
            csnd_uduccrlby_upto1m=csnd_uduccrlby_upto1m,
            csnd_uduccrlby_1mto3m=csnd_uduccrlby_1mto3m,
            csnd_uduccrlby_3mto1y=csnd_uduccrlby_3mto1y,
            csnd_uduccrlby_oth=csnd_uduccrlby_oth,
            csnd_uduccrlby_oth_upto1m=csnd_uduccrlby_oth_upto1m,
            csnd_uduccrlby_oth_1mto3m=csnd_uduccrlby_oth_1mto3m,
            csnd_uduccrlby_oth_3mto1y=csnd_uduccrlby_oth_3mto1y,
            csnd_uduccrlby_oth_auth=csnd_uduccrlby_oth_auth,
            csnd_uduccrlby_oth_auth_upto1m=csnd_uduccrlby_oth_auth_upto1m,
            csnd_uduccrlby_oth_auth_1mto3m=csnd_uduccrlby_oth_auth_1mto3m,
            csnd_uduccrlby_oth_auth_3mto1y=csnd_uduccrlby_oth_auth_3mto1y,
            csnd_uduccrlby_oth_bis=csnd_uduccrlby_oth_bis,
            csnd_uduccrlby_oth_bis_upto1m=csnd_uduccrlby_oth_bis_upto1m,
            csnd_uduccrlby_oth_bis_1mto3m=csnd_uduccrlby_oth_bis_1mto3m,
            csnd_uduccrlby_oth_bis_3mto1y=csnd_uduccrlby_oth_bis_3mto1y,
            csnd_uduccrlby_oth_imf=csnd_uduccrlby_oth_imf,
            csnd_uduccrlby_oth_imf_upto1m=csnd_uduccrlby_oth_imf_upto1m,
            csnd_uduccrlby_oth_imf_1mto3m=csnd_uduccrlby_oth_imf_1mto3m,
            csnd_uduccrlby_oth_imf_3mto1y=csnd_uduccrlby_oth_imf_3mto1y,
            csnd_uduccrlby_oth_iorg=csnd_uduccrlby_oth_iorg,
            csnd_uduccrlby_oth_iorg_upto1m=csnd_uduccrlby_oth_iorg_upto1m,
            csnd_uduccrlby_oth_iorg_1mto3m=csnd_uduccrlby_oth_iorg_1mto3m,
            csnd_uduccrlby_oth_iorg_3mto1y=csnd_uduccrlby_oth_iorg_3mto1y,
            csnd_uduccrlby_bkinhk=csnd_uduccrlby_bkinhk,
            csnd_uduccrlby_bkinhk_upto1m=csnd_uduccrlby_bkinhk_upto1m,
            csnd_uduccrlby_bkinhk_1mto3m=csnd_uduccrlby_bkinhk_1mto3m,
            csnd_uduccrlby_bkinhk_3mto1y=csnd_uduccrlby_bkinhk_3mto1y,
            csnd_uduccrlby_bkouthk=csnd_uduccrlby_bkouthk,
            csnd_uduccrlby_bkouthk_upto1m=csnd_uduccrlby_bkouthk_upto1m,
            csnd_uduccrlby_bkouthk_1mto3m=csnd_uduccrlby_bkouthk_1mto3m,
            csnd_uduccrlby_bkouthk_3mto1y=csnd_uduccrlby_bkouthk_3mto1y,
            csnd_uduccrlto=csnd_uduccrlto,
            csnd_uduccrlto_upto1m=csnd_uduccrlto_upto1m,
            csnd_uduccrlto_1mto3m=csnd_uduccrlto_1mto3m,
            csnd_uduccrlto_3mto1y=csnd_uduccrlto_3mto1y,
            csnd_uduccrlto_oth=csnd_uduccrlto_oth,
            csnd_uduccrlto_oth_upto1m=csnd_uduccrlto_oth_upto1m,
            csnd_uduccrlto_oth_1mto3m=csnd_uduccrlto_oth_1mto3m,
            csnd_uduccrlto_oth_3mto1y=csnd_uduccrlto_oth_3mto1y,
            csnd_uduccrlto_oth_auth=csnd_uduccrlto_oth_auth,
            csnd_uduccrlto_oth_auth_upto1m=csnd_uduccrlto_oth_auth_upto1m,
            csnd_uduccrlto_oth_auth_1mto3m=csnd_uduccrlto_oth_auth_1mto3m,
            csnd_uduccrlto_oth_auth_3mto1y=csnd_uduccrlto_oth_auth_3mto1y,
            csnd_uduccrlto_oth_bis=csnd_uduccrlto_oth_bis,
            csnd_uduccrlto_oth_bis_upto1m=csnd_uduccrlto_oth_bis_upto1m,
            csnd_uduccrlto_oth_bis_1mto3m=csnd_uduccrlto_oth_bis_1mto3m,
            csnd_uduccrlto_oth_bis_3mto1y=csnd_uduccrlto_oth_bis_3mto1y,
            csnd_uduccrlto_oth_imf=csnd_uduccrlto_oth_imf,
            csnd_uduccrlto_oth_imf_upto1m=csnd_uduccrlto_oth_imf_upto1m,
            csnd_uduccrlto_oth_imf_1mto3m=csnd_uduccrlto_oth_imf_1mto3m,
            csnd_uduccrlto_oth_imf_3mto1y=csnd_uduccrlto_oth_imf_3mto1y,
            csnd_uduccrlto_oth_iorg=csnd_uduccrlto_oth_iorg,
            csnd_uduccrlto_oth_iorg_upto1m=csnd_uduccrlto_oth_iorg_upto1m,
            csnd_uduccrlto_oth_iorg_1mto3m=csnd_uduccrlto_oth_iorg_1mto3m,
            csnd_uduccrlto_oth_iorg_3mto1y=csnd_uduccrlto_oth_iorg_3mto1y,
            csnd_uduccrlto_bkinhk=csnd_uduccrlto_bkinhk,
            csnd_uduccrlto_bkinhk_upto1m=csnd_uduccrlto_bkinhk_upto1m,
            csnd_uduccrlto_bkinhk_1mto3m=csnd_uduccrlto_bkinhk_1mto3m,
            csnd_uduccrlto_bkinhk_3mto1y=csnd_uduccrlto_bkinhk_3mto1y,
            csnd_uduccrlto_bkouthk=csnd_uduccrlto_bkouthk,
            csnd_uduccrlto_bkouthk_upto1m=csnd_uduccrlto_bkouthk_upto1m,
            csnd_uduccrlto_bkouthk_1mto3m=csnd_uduccrlto_bkouthk_1mto3m,
            csnd_uduccrlto_bkouthk_3mto1y=csnd_uduccrlto_bkouthk_3mto1y,
            csnd_aslp=csnd_aslp,
            csnd_aslp_upto1m=csnd_aslp_upto1m,
            csnd_aslp_1mto3m=csnd_aslp_1mto3m,
            csnd_aslp_3mto1y=csnd_aslp_3mto1y,
            csnd_aslp_sp=csnd_aslp_sp,
            csnd_aslp_sp_upto1m=csnd_aslp_sp_upto1m,
            csnd_aslp_sp_1mto3m=csnd_aslp_sp_1mto3m,
            csnd_aslp_sp_3mto1y=csnd_aslp_sp_3mto1y,
            csnd_aslp_sp_bp=csnd_aslp_sp_bp,
            csnd_aslp_sp_bp_upto1m=csnd_aslp_sp_bp_upto1m,
            csnd_aslp_sp_bp_1mto3m=csnd_aslp_sp_bp_1mto3m,
            csnd_aslp_sp_bp_3mto1y=csnd_aslp_sp_bp_3mto1y,
            csnd_aslp_sp_wc=csnd_aslp_sp_wc,
            csnd_aslp_sp_wc_upto1m=csnd_aslp_sp_wc_upto1m,
            csnd_aslp_sp_wc_1mto3m=csnd_aslp_sp_wc_1mto3m,
            csnd_aslp_sp_wc_3mto1y=csnd_aslp_sp_wc_3mto1y,
            csnd_aslp_lp=csnd_aslp_lp,
            csnd_aslp_lp_upto1m=csnd_aslp_lp_upto1m,
            csnd_aslp_lp_1mto3m=csnd_aslp_lp_1mto3m,
            csnd_aslp_lp_3mto1y=csnd_aslp_lp_3mto1y,
            csnd_aslp_lp_bc=csnd_aslp_lp_bc,
            csnd_aslp_lp_bc_upto1m=csnd_aslp_lp_bc_upto1m,
            csnd_aslp_lp_bc_1mto3m=csnd_aslp_lp_bc_1mto3m,
            csnd_aslp_lp_bc_3mto1y=csnd_aslp_lp_bc_3mto1y,
            csnd_aslp_lp_wp=csnd_aslp_lp_wp,
            csnd_aslp_lp_wp_upto1m=csnd_aslp_lp_wp_upto1m,
            csnd_aslp_lp_wp_1mto3m=csnd_aslp_lp_wp_1mto3m,
            csnd_aslp_lp_wp_3mto1y=csnd_aslp_lp_wp_3mto1y,
            mm_spt_stdcd=mm_spt_stdcd,
            mm_spt_fid=mm_spt_fid,
            mm_spt_fid_ndf=mm_spt_fid_ndf,
            mm_spt_fid_ndf_sp=mm_spt_fid_ndf_sp,
            mm_spt_fid_ndf_lp=mm_spt_fid_ndf_lp,
            mm_spt_fid_oi=mm_spt_fid_oi,
            mm_spt_pa=mm_spt_pa,
            mm_spt_pa_ra=mm_spt_pa_ra,
            mm_spt_pa_ofca=mm_spt_pa_ofca,
            mm_spt_slr=mm_spt_slr,
            mm_spt_slr_lr_insi=mm_spt_slr_lr_insi,
            mm_spt_slr_lr_notinsi=mm_spt_slr_lr_notinsi,
            mm_spt_slr_ba_insi=mm_spt_slr_ba_insi,
            mm_spt_slr_ba_notinsi=mm_spt_slr_ba_notinsi,
            mm_spt_fda=mm_spt_fda,
            mm_spt_fda_forw=mm_spt_fda_forw,
            mm_spt_fda_fut=mm_spt_fda_fut,
            mm_spt_fda_swp=mm_spt_fda_swp,
            mm_spt_fda_opt=mm_spt_fda_opt,
            mm_spt_fda_oth=mm_spt_fda_oth,
            mm_spt_dergt1y=mm_spt_dergt1y,
            mm_spt_dergt1y_aslpf=mm_spt_dergt1y_aslpf,
            mm_spt_dergt1y_aslpf_sp=mm_spt_dergt1y_aslpf_sp,
            mm_spt_dergt1y_aslpf_lp=mm_spt_dergt1y_aslpf_lp,
            mm_spt_dergt1y_aslpfo=mm_spt_dergt1y_aslpfo,
            mm_spt_dergt1y_aslpfo_sp=mm_spt_dergt1y_aslpfo_sp,
            mm_spt_dergt1y_aslpfo_sp_bp=mm_spt_dergt1y_aslpfo_sp_bp,
            mm_spt_dergt1y_aslpfo_sp_wc=mm_spt_dergt1y_aslpfo_sp_wc,
            mm_spt_dergt1y_aslpfo_lp=mm_spt_dergt1y_aslpfo_lp,
            mm_spt_dergt1y_aslpfo_lp_bc=mm_spt_dergt1y_aslpfo_lp_bc,
            mm_spt_dergt1y_aslpfo_lp_wp=mm_spt_dergt1y_aslpfo_lp_wp,
            mm_lfd_ccr=mm_lfd_ccr,
            mm_lfd_ccr_insdr=mm_lfd_ccr_insdr,
            mm_lfd_ccr_insdr_eur=mm_lfd_ccr_insdr_eur,
            mm_lfd_ccr_insdr_jpy=mm_lfd_ccr_insdr_jpy,
            mm_lfd_ccr_insdr_gbp=mm_lfd_ccr_insdr_gbp,
            mm_lfd_ccr_insdr_usd=mm_lfd_ccr_insdr_usd,
            mm_lfd_ccr_notinsdr=mm_lfd_ccr_notinsdr,
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
