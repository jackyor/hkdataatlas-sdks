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
        pwp_fbean_a (float | Unset):
        pwp_fbeef_a (float | Unset):
        pwp_fbrice_a (float | Unset):
        pwp_fcmilk_a (float | Unset):
        pwp_fegg_a (float | Unset):
        pwp_ffruit_a (float | Unset):
        pwp_flard_a (float | Unset):
        pwp_fmutn_a (float | Unset):
        pwp_fonion_a (float | Unset):
        pwp_food_a (float | Unset):
        pwp_fpoil_a (float | Unset):
        pwp_fpork_a (float | Unset):
        pwp_fpotatoes_a (float | Unset):
        pwp_fpoul_a (float | Unset):
        pwp_frsug_a (float | Unset):
        pwp_fsfish_a (float | Unset):
        pwp_fvegt_a (float | Unset):
        pwp_fverm_a (float | Unset):
        pwp_fwflour_a (float | Unset):
        pwp_fwrice_a (float | Unset):
        pwp_mebsh_a (float | Unset):
        pwp_mecoal_a (float | Unset):
        pwp_meisbar_a (float | Unset):
        pwp_meisnail_a (float | Unset):
        pwp_meisplate_a (float | Unset):
        pwp_mekero_a (float | Unset):
        pwp_meluoil_a (float | Unset):
        pwp_meoil_a (float | Unset):
        pwp_mepetr_a (float | Unset):
        pwp_meplead_a (float | Unset):
        pwp_metal_a (float | Unset):
        pwp_metin_a (float | Unset):
        pwp_meymshe_a (float | Unset):
        pwp_miasul_a (float | Unset):
        pwp_mibhide_a (float | Unset):
        pwp_micem_a (float | Unset):
        pwp_michar_a (float | Unset):
        pwp_michide_a (float | Unset):
        pwp_micpap_a (float | Unset):
        pwp_midfea_a (float | Unset):
        pwp_mifwood_a (float | Unset):
        pwp_mihwood_a (float | Unset):
        pwp_miratn_a (float | Unset):
        pwp_misacid_a (float | Unset):
        pwp_misalp_a (float | Unset):
        pwp_misash_a (float | Unset):
        pwp_miscell_a (float | Unset):
        pwp_mislea_a (float | Unset):
        pwp_miswood_a (float | Unset):
        pwp_tasilk_a (float | Unset):
        pwp_tdfpita_a (float | Unset):
        pwp_tdpcot_a (float | Unset):
        pwp_textiles_a (float | Unset):
        pwp_tflan_a (float | Unset):
        pwp_tgbag_a (float | Unset):
        pwp_thcloth_a (float | Unset):
        pwp_tmhemp_a (float | Unset):
        pwp_tsilkp_a (float | Unset):
        pwp_twshirt_a (float | Unset):
        pwp_twstw_a (float | Unset):
        pwp_twublan_a (float | Unset):
        pwp_year (datetime.date | Unset):
    """

    pwp_fbean_a: float | Unset = UNSET
    pwp_fbeef_a: float | Unset = UNSET
    pwp_fbrice_a: float | Unset = UNSET
    pwp_fcmilk_a: float | Unset = UNSET
    pwp_fegg_a: float | Unset = UNSET
    pwp_ffruit_a: float | Unset = UNSET
    pwp_flard_a: float | Unset = UNSET
    pwp_fmutn_a: float | Unset = UNSET
    pwp_fonion_a: float | Unset = UNSET
    pwp_food_a: float | Unset = UNSET
    pwp_fpoil_a: float | Unset = UNSET
    pwp_fpork_a: float | Unset = UNSET
    pwp_fpotatoes_a: float | Unset = UNSET
    pwp_fpoul_a: float | Unset = UNSET
    pwp_frsug_a: float | Unset = UNSET
    pwp_fsfish_a: float | Unset = UNSET
    pwp_fvegt_a: float | Unset = UNSET
    pwp_fverm_a: float | Unset = UNSET
    pwp_fwflour_a: float | Unset = UNSET
    pwp_fwrice_a: float | Unset = UNSET
    pwp_mebsh_a: float | Unset = UNSET
    pwp_mecoal_a: float | Unset = UNSET
    pwp_meisbar_a: float | Unset = UNSET
    pwp_meisnail_a: float | Unset = UNSET
    pwp_meisplate_a: float | Unset = UNSET
    pwp_mekero_a: float | Unset = UNSET
    pwp_meluoil_a: float | Unset = UNSET
    pwp_meoil_a: float | Unset = UNSET
    pwp_mepetr_a: float | Unset = UNSET
    pwp_meplead_a: float | Unset = UNSET
    pwp_metal_a: float | Unset = UNSET
    pwp_metin_a: float | Unset = UNSET
    pwp_meymshe_a: float | Unset = UNSET
    pwp_miasul_a: float | Unset = UNSET
    pwp_mibhide_a: float | Unset = UNSET
    pwp_micem_a: float | Unset = UNSET
    pwp_michar_a: float | Unset = UNSET
    pwp_michide_a: float | Unset = UNSET
    pwp_micpap_a: float | Unset = UNSET
    pwp_midfea_a: float | Unset = UNSET
    pwp_mifwood_a: float | Unset = UNSET
    pwp_mihwood_a: float | Unset = UNSET
    pwp_miratn_a: float | Unset = UNSET
    pwp_misacid_a: float | Unset = UNSET
    pwp_misalp_a: float | Unset = UNSET
    pwp_misash_a: float | Unset = UNSET
    pwp_miscell_a: float | Unset = UNSET
    pwp_mislea_a: float | Unset = UNSET
    pwp_miswood_a: float | Unset = UNSET
    pwp_tasilk_a: float | Unset = UNSET
    pwp_tdfpita_a: float | Unset = UNSET
    pwp_tdpcot_a: float | Unset = UNSET
    pwp_textiles_a: float | Unset = UNSET
    pwp_tflan_a: float | Unset = UNSET
    pwp_tgbag_a: float | Unset = UNSET
    pwp_thcloth_a: float | Unset = UNSET
    pwp_tmhemp_a: float | Unset = UNSET
    pwp_tsilkp_a: float | Unset = UNSET
    pwp_twshirt_a: float | Unset = UNSET
    pwp_twstw_a: float | Unset = UNSET
    pwp_twublan_a: float | Unset = UNSET
    pwp_year: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pwp_fbean_a = self.pwp_fbean_a

        pwp_fbeef_a = self.pwp_fbeef_a

        pwp_fbrice_a = self.pwp_fbrice_a

        pwp_fcmilk_a = self.pwp_fcmilk_a

        pwp_fegg_a = self.pwp_fegg_a

        pwp_ffruit_a = self.pwp_ffruit_a

        pwp_flard_a = self.pwp_flard_a

        pwp_fmutn_a = self.pwp_fmutn_a

        pwp_fonion_a = self.pwp_fonion_a

        pwp_food_a = self.pwp_food_a

        pwp_fpoil_a = self.pwp_fpoil_a

        pwp_fpork_a = self.pwp_fpork_a

        pwp_fpotatoes_a = self.pwp_fpotatoes_a

        pwp_fpoul_a = self.pwp_fpoul_a

        pwp_frsug_a = self.pwp_frsug_a

        pwp_fsfish_a = self.pwp_fsfish_a

        pwp_fvegt_a = self.pwp_fvegt_a

        pwp_fverm_a = self.pwp_fverm_a

        pwp_fwflour_a = self.pwp_fwflour_a

        pwp_fwrice_a = self.pwp_fwrice_a

        pwp_mebsh_a = self.pwp_mebsh_a

        pwp_mecoal_a = self.pwp_mecoal_a

        pwp_meisbar_a = self.pwp_meisbar_a

        pwp_meisnail_a = self.pwp_meisnail_a

        pwp_meisplate_a = self.pwp_meisplate_a

        pwp_mekero_a = self.pwp_mekero_a

        pwp_meluoil_a = self.pwp_meluoil_a

        pwp_meoil_a = self.pwp_meoil_a

        pwp_mepetr_a = self.pwp_mepetr_a

        pwp_meplead_a = self.pwp_meplead_a

        pwp_metal_a = self.pwp_metal_a

        pwp_metin_a = self.pwp_metin_a

        pwp_meymshe_a = self.pwp_meymshe_a

        pwp_miasul_a = self.pwp_miasul_a

        pwp_mibhide_a = self.pwp_mibhide_a

        pwp_micem_a = self.pwp_micem_a

        pwp_michar_a = self.pwp_michar_a

        pwp_michide_a = self.pwp_michide_a

        pwp_micpap_a = self.pwp_micpap_a

        pwp_midfea_a = self.pwp_midfea_a

        pwp_mifwood_a = self.pwp_mifwood_a

        pwp_mihwood_a = self.pwp_mihwood_a

        pwp_miratn_a = self.pwp_miratn_a

        pwp_misacid_a = self.pwp_misacid_a

        pwp_misalp_a = self.pwp_misalp_a

        pwp_misash_a = self.pwp_misash_a

        pwp_miscell_a = self.pwp_miscell_a

        pwp_mislea_a = self.pwp_mislea_a

        pwp_miswood_a = self.pwp_miswood_a

        pwp_tasilk_a = self.pwp_tasilk_a

        pwp_tdfpita_a = self.pwp_tdfpita_a

        pwp_tdpcot_a = self.pwp_tdpcot_a

        pwp_textiles_a = self.pwp_textiles_a

        pwp_tflan_a = self.pwp_tflan_a

        pwp_tgbag_a = self.pwp_tgbag_a

        pwp_thcloth_a = self.pwp_thcloth_a

        pwp_tmhemp_a = self.pwp_tmhemp_a

        pwp_tsilkp_a = self.pwp_tsilkp_a

        pwp_twshirt_a = self.pwp_twshirt_a

        pwp_twstw_a = self.pwp_twstw_a

        pwp_twublan_a = self.pwp_twublan_a

        pwp_year: str | Unset = UNSET
        if not isinstance(self.pwp_year, Unset):
            pwp_year = self.pwp_year.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pwp_fbean_a is not UNSET:
            field_dict["Pwp_fbean_a"] = pwp_fbean_a
        if pwp_fbeef_a is not UNSET:
            field_dict["Pwp_fbeef_a"] = pwp_fbeef_a
        if pwp_fbrice_a is not UNSET:
            field_dict["Pwp_fbrice_a"] = pwp_fbrice_a
        if pwp_fcmilk_a is not UNSET:
            field_dict["Pwp_fcmilk_a"] = pwp_fcmilk_a
        if pwp_fegg_a is not UNSET:
            field_dict["Pwp_fegg_a"] = pwp_fegg_a
        if pwp_ffruit_a is not UNSET:
            field_dict["Pwp_ffruit_a"] = pwp_ffruit_a
        if pwp_flard_a is not UNSET:
            field_dict["Pwp_flard_a"] = pwp_flard_a
        if pwp_fmutn_a is not UNSET:
            field_dict["Pwp_fmutn_a"] = pwp_fmutn_a
        if pwp_fonion_a is not UNSET:
            field_dict["Pwp_fonion_a"] = pwp_fonion_a
        if pwp_food_a is not UNSET:
            field_dict["Pwp_food_a"] = pwp_food_a
        if pwp_fpoil_a is not UNSET:
            field_dict["Pwp_fpoil_a"] = pwp_fpoil_a
        if pwp_fpork_a is not UNSET:
            field_dict["Pwp_fpork_a"] = pwp_fpork_a
        if pwp_fpotatoes_a is not UNSET:
            field_dict["Pwp_fpotatoes_a"] = pwp_fpotatoes_a
        if pwp_fpoul_a is not UNSET:
            field_dict["Pwp_fpoul_a"] = pwp_fpoul_a
        if pwp_frsug_a is not UNSET:
            field_dict["Pwp_frsug_a"] = pwp_frsug_a
        if pwp_fsfish_a is not UNSET:
            field_dict["Pwp_fsfish_a"] = pwp_fsfish_a
        if pwp_fvegt_a is not UNSET:
            field_dict["Pwp_fvegt_a"] = pwp_fvegt_a
        if pwp_fverm_a is not UNSET:
            field_dict["Pwp_fverm_a"] = pwp_fverm_a
        if pwp_fwflour_a is not UNSET:
            field_dict["Pwp_fwflour_a"] = pwp_fwflour_a
        if pwp_fwrice_a is not UNSET:
            field_dict["Pwp_fwrice_a"] = pwp_fwrice_a
        if pwp_mebsh_a is not UNSET:
            field_dict["Pwp_mebsh_a"] = pwp_mebsh_a
        if pwp_mecoal_a is not UNSET:
            field_dict["Pwp_mecoal_a"] = pwp_mecoal_a
        if pwp_meisbar_a is not UNSET:
            field_dict["Pwp_meisbar_a"] = pwp_meisbar_a
        if pwp_meisnail_a is not UNSET:
            field_dict["Pwp_meisnail_a"] = pwp_meisnail_a
        if pwp_meisplate_a is not UNSET:
            field_dict["Pwp_meisplate_a"] = pwp_meisplate_a
        if pwp_mekero_a is not UNSET:
            field_dict["Pwp_mekero_a"] = pwp_mekero_a
        if pwp_meluoil_a is not UNSET:
            field_dict["Pwp_meluoil_a"] = pwp_meluoil_a
        if pwp_meoil_a is not UNSET:
            field_dict["Pwp_meoil_a"] = pwp_meoil_a
        if pwp_mepetr_a is not UNSET:
            field_dict["Pwp_mepetr_a"] = pwp_mepetr_a
        if pwp_meplead_a is not UNSET:
            field_dict["Pwp_meplead_a"] = pwp_meplead_a
        if pwp_metal_a is not UNSET:
            field_dict["Pwp_metal_a"] = pwp_metal_a
        if pwp_metin_a is not UNSET:
            field_dict["Pwp_metin_a"] = pwp_metin_a
        if pwp_meymshe_a is not UNSET:
            field_dict["Pwp_meymshe_a"] = pwp_meymshe_a
        if pwp_miasul_a is not UNSET:
            field_dict["Pwp_miasul_a"] = pwp_miasul_a
        if pwp_mibhide_a is not UNSET:
            field_dict["Pwp_mibhide_a"] = pwp_mibhide_a
        if pwp_micem_a is not UNSET:
            field_dict["Pwp_micem_a"] = pwp_micem_a
        if pwp_michar_a is not UNSET:
            field_dict["Pwp_michar_a"] = pwp_michar_a
        if pwp_michide_a is not UNSET:
            field_dict["Pwp_michide_a"] = pwp_michide_a
        if pwp_micpap_a is not UNSET:
            field_dict["Pwp_micpap_a"] = pwp_micpap_a
        if pwp_midfea_a is not UNSET:
            field_dict["Pwp_midfea_a"] = pwp_midfea_a
        if pwp_mifwood_a is not UNSET:
            field_dict["Pwp_mifwood_a"] = pwp_mifwood_a
        if pwp_mihwood_a is not UNSET:
            field_dict["Pwp_mihwood_a"] = pwp_mihwood_a
        if pwp_miratn_a is not UNSET:
            field_dict["Pwp_miratn_a"] = pwp_miratn_a
        if pwp_misacid_a is not UNSET:
            field_dict["Pwp_misacid_a"] = pwp_misacid_a
        if pwp_misalp_a is not UNSET:
            field_dict["Pwp_misalp_a"] = pwp_misalp_a
        if pwp_misash_a is not UNSET:
            field_dict["Pwp_misash_a"] = pwp_misash_a
        if pwp_miscell_a is not UNSET:
            field_dict["Pwp_miscell_a"] = pwp_miscell_a
        if pwp_mislea_a is not UNSET:
            field_dict["Pwp_mislea_a"] = pwp_mislea_a
        if pwp_miswood_a is not UNSET:
            field_dict["Pwp_miswood_a"] = pwp_miswood_a
        if pwp_tasilk_a is not UNSET:
            field_dict["Pwp_tasilk_a"] = pwp_tasilk_a
        if pwp_tdfpita_a is not UNSET:
            field_dict["Pwp_tdfpita_a"] = pwp_tdfpita_a
        if pwp_tdpcot_a is not UNSET:
            field_dict["Pwp_tdpcot_a"] = pwp_tdpcot_a
        if pwp_textiles_a is not UNSET:
            field_dict["Pwp_textiles_a"] = pwp_textiles_a
        if pwp_tflan_a is not UNSET:
            field_dict["Pwp_tflan_a"] = pwp_tflan_a
        if pwp_tgbag_a is not UNSET:
            field_dict["Pwp_tgbag_a"] = pwp_tgbag_a
        if pwp_thcloth_a is not UNSET:
            field_dict["Pwp_thcloth_a"] = pwp_thcloth_a
        if pwp_tmhemp_a is not UNSET:
            field_dict["Pwp_tmhemp_a"] = pwp_tmhemp_a
        if pwp_tsilkp_a is not UNSET:
            field_dict["Pwp_tsilkp_a"] = pwp_tsilkp_a
        if pwp_twshirt_a is not UNSET:
            field_dict["Pwp_twshirt_a"] = pwp_twshirt_a
        if pwp_twstw_a is not UNSET:
            field_dict["Pwp_twstw_a"] = pwp_twstw_a
        if pwp_twublan_a is not UNSET:
            field_dict["Pwp_twublan_a"] = pwp_twublan_a
        if pwp_year is not UNSET:
            field_dict["Pwp_year"] = pwp_year

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pwp_fbean_a = d.pop("Pwp_fbean_a", UNSET)

        pwp_fbeef_a = d.pop("Pwp_fbeef_a", UNSET)

        pwp_fbrice_a = d.pop("Pwp_fbrice_a", UNSET)

        pwp_fcmilk_a = d.pop("Pwp_fcmilk_a", UNSET)

        pwp_fegg_a = d.pop("Pwp_fegg_a", UNSET)

        pwp_ffruit_a = d.pop("Pwp_ffruit_a", UNSET)

        pwp_flard_a = d.pop("Pwp_flard_a", UNSET)

        pwp_fmutn_a = d.pop("Pwp_fmutn_a", UNSET)

        pwp_fonion_a = d.pop("Pwp_fonion_a", UNSET)

        pwp_food_a = d.pop("Pwp_food_a", UNSET)

        pwp_fpoil_a = d.pop("Pwp_fpoil_a", UNSET)

        pwp_fpork_a = d.pop("Pwp_fpork_a", UNSET)

        pwp_fpotatoes_a = d.pop("Pwp_fpotatoes_a", UNSET)

        pwp_fpoul_a = d.pop("Pwp_fpoul_a", UNSET)

        pwp_frsug_a = d.pop("Pwp_frsug_a", UNSET)

        pwp_fsfish_a = d.pop("Pwp_fsfish_a", UNSET)

        pwp_fvegt_a = d.pop("Pwp_fvegt_a", UNSET)

        pwp_fverm_a = d.pop("Pwp_fverm_a", UNSET)

        pwp_fwflour_a = d.pop("Pwp_fwflour_a", UNSET)

        pwp_fwrice_a = d.pop("Pwp_fwrice_a", UNSET)

        pwp_mebsh_a = d.pop("Pwp_mebsh_a", UNSET)

        pwp_mecoal_a = d.pop("Pwp_mecoal_a", UNSET)

        pwp_meisbar_a = d.pop("Pwp_meisbar_a", UNSET)

        pwp_meisnail_a = d.pop("Pwp_meisnail_a", UNSET)

        pwp_meisplate_a = d.pop("Pwp_meisplate_a", UNSET)

        pwp_mekero_a = d.pop("Pwp_mekero_a", UNSET)

        pwp_meluoil_a = d.pop("Pwp_meluoil_a", UNSET)

        pwp_meoil_a = d.pop("Pwp_meoil_a", UNSET)

        pwp_mepetr_a = d.pop("Pwp_mepetr_a", UNSET)

        pwp_meplead_a = d.pop("Pwp_meplead_a", UNSET)

        pwp_metal_a = d.pop("Pwp_metal_a", UNSET)

        pwp_metin_a = d.pop("Pwp_metin_a", UNSET)

        pwp_meymshe_a = d.pop("Pwp_meymshe_a", UNSET)

        pwp_miasul_a = d.pop("Pwp_miasul_a", UNSET)

        pwp_mibhide_a = d.pop("Pwp_mibhide_a", UNSET)

        pwp_micem_a = d.pop("Pwp_micem_a", UNSET)

        pwp_michar_a = d.pop("Pwp_michar_a", UNSET)

        pwp_michide_a = d.pop("Pwp_michide_a", UNSET)

        pwp_micpap_a = d.pop("Pwp_micpap_a", UNSET)

        pwp_midfea_a = d.pop("Pwp_midfea_a", UNSET)

        pwp_mifwood_a = d.pop("Pwp_mifwood_a", UNSET)

        pwp_mihwood_a = d.pop("Pwp_mihwood_a", UNSET)

        pwp_miratn_a = d.pop("Pwp_miratn_a", UNSET)

        pwp_misacid_a = d.pop("Pwp_misacid_a", UNSET)

        pwp_misalp_a = d.pop("Pwp_misalp_a", UNSET)

        pwp_misash_a = d.pop("Pwp_misash_a", UNSET)

        pwp_miscell_a = d.pop("Pwp_miscell_a", UNSET)

        pwp_mislea_a = d.pop("Pwp_mislea_a", UNSET)

        pwp_miswood_a = d.pop("Pwp_miswood_a", UNSET)

        pwp_tasilk_a = d.pop("Pwp_tasilk_a", UNSET)

        pwp_tdfpita_a = d.pop("Pwp_tdfpita_a", UNSET)

        pwp_tdpcot_a = d.pop("Pwp_tdpcot_a", UNSET)

        pwp_textiles_a = d.pop("Pwp_textiles_a", UNSET)

        pwp_tflan_a = d.pop("Pwp_tflan_a", UNSET)

        pwp_tgbag_a = d.pop("Pwp_tgbag_a", UNSET)

        pwp_thcloth_a = d.pop("Pwp_thcloth_a", UNSET)

        pwp_tmhemp_a = d.pop("Pwp_tmhemp_a", UNSET)

        pwp_tsilkp_a = d.pop("Pwp_tsilkp_a", UNSET)

        pwp_twshirt_a = d.pop("Pwp_twshirt_a", UNSET)

        pwp_twstw_a = d.pop("Pwp_twstw_a", UNSET)

        pwp_twublan_a = d.pop("Pwp_twublan_a", UNSET)

        _pwp_year = d.pop("Pwp_year", UNSET)
        pwp_year: datetime.date | Unset
        if isinstance(_pwp_year, Unset):
            pwp_year = UNSET
        else:
            pwp_year = datetime.date.fromisoformat(_pwp_year)

        record = cls(
            pwp_fbean_a=pwp_fbean_a,
            pwp_fbeef_a=pwp_fbeef_a,
            pwp_fbrice_a=pwp_fbrice_a,
            pwp_fcmilk_a=pwp_fcmilk_a,
            pwp_fegg_a=pwp_fegg_a,
            pwp_ffruit_a=pwp_ffruit_a,
            pwp_flard_a=pwp_flard_a,
            pwp_fmutn_a=pwp_fmutn_a,
            pwp_fonion_a=pwp_fonion_a,
            pwp_food_a=pwp_food_a,
            pwp_fpoil_a=pwp_fpoil_a,
            pwp_fpork_a=pwp_fpork_a,
            pwp_fpotatoes_a=pwp_fpotatoes_a,
            pwp_fpoul_a=pwp_fpoul_a,
            pwp_frsug_a=pwp_frsug_a,
            pwp_fsfish_a=pwp_fsfish_a,
            pwp_fvegt_a=pwp_fvegt_a,
            pwp_fverm_a=pwp_fverm_a,
            pwp_fwflour_a=pwp_fwflour_a,
            pwp_fwrice_a=pwp_fwrice_a,
            pwp_mebsh_a=pwp_mebsh_a,
            pwp_mecoal_a=pwp_mecoal_a,
            pwp_meisbar_a=pwp_meisbar_a,
            pwp_meisnail_a=pwp_meisnail_a,
            pwp_meisplate_a=pwp_meisplate_a,
            pwp_mekero_a=pwp_mekero_a,
            pwp_meluoil_a=pwp_meluoil_a,
            pwp_meoil_a=pwp_meoil_a,
            pwp_mepetr_a=pwp_mepetr_a,
            pwp_meplead_a=pwp_meplead_a,
            pwp_metal_a=pwp_metal_a,
            pwp_metin_a=pwp_metin_a,
            pwp_meymshe_a=pwp_meymshe_a,
            pwp_miasul_a=pwp_miasul_a,
            pwp_mibhide_a=pwp_mibhide_a,
            pwp_micem_a=pwp_micem_a,
            pwp_michar_a=pwp_michar_a,
            pwp_michide_a=pwp_michide_a,
            pwp_micpap_a=pwp_micpap_a,
            pwp_midfea_a=pwp_midfea_a,
            pwp_mifwood_a=pwp_mifwood_a,
            pwp_mihwood_a=pwp_mihwood_a,
            pwp_miratn_a=pwp_miratn_a,
            pwp_misacid_a=pwp_misacid_a,
            pwp_misalp_a=pwp_misalp_a,
            pwp_misash_a=pwp_misash_a,
            pwp_miscell_a=pwp_miscell_a,
            pwp_mislea_a=pwp_mislea_a,
            pwp_miswood_a=pwp_miswood_a,
            pwp_tasilk_a=pwp_tasilk_a,
            pwp_tdfpita_a=pwp_tdfpita_a,
            pwp_tdpcot_a=pwp_tdpcot_a,
            pwp_textiles_a=pwp_textiles_a,
            pwp_tflan_a=pwp_tflan_a,
            pwp_tgbag_a=pwp_tgbag_a,
            pwp_thcloth_a=pwp_thcloth_a,
            pwp_tmhemp_a=pwp_tmhemp_a,
            pwp_tsilkp_a=pwp_tsilkp_a,
            pwp_twshirt_a=pwp_twshirt_a,
            pwp_twstw_a=pwp_twstw_a,
            pwp_twublan_a=pwp_twublan_a,
            pwp_year=pwp_year,
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
