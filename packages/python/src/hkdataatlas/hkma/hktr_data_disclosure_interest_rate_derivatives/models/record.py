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
        end_of_date (datetime.date | Unset):
        on_total_asset_class (float | Unset):
        on_prod_b_swap (float | Unset):
        on_prod_ff (float | Unset):
        on_prod_oi_swap (float | Unset):
        on_prod_intend_clear_b_swap (float | Unset):
        on_prod_intend_clear_ff (float | Unset):
        on_prod_intend_clear_oi_swap (float | Unset):
        on_prod_not_intend_clear_b_swap (float | Unset):
        on_prod_not_intend_clear_ff (float | Unset):
        on_prod_not_intend_clear_oi_swap (float | Unset):
        on_prod_usd_b_swap (float | Unset):
        on_prod_usd_ff (float | Unset):
        on_prod_usd_oi_swap (float | Unset):
        on_prod_cny_b_swap (float | Unset):
        on_prod_cny_ff (float | Unset):
        on_prod_cny_oi_swap (float | Unset):
        on_prod_eur_b_swap (float | Unset):
        on_prod_eur_ff (float | Unset):
        on_prod_eur_oi_swap (float | Unset):
        on_prod_gbp_b_swap (float | Unset):
        on_prod_gbp_ff (float | Unset):
        on_prod_gbp_oi_swap (float | Unset):
        on_prod_jpy_b_swap (float | Unset):
        on_prod_jpy_ff (float | Unset):
        on_prod_jpy_oi_swap (float | Unset):
        on_prod_hkd_b_swap (float | Unset):
        on_prod_hkd_ff (float | Unset):
        on_prod_hkd_oi_swap (float | Unset):
        on_prod_other_curr_b_swap (float | Unset):
        on_prod_other_curr_ff (float | Unset):
        on_prod_other_curr_oi_swap (float | Unset):
        on_prod_0yr_1yr_b_swap (float | Unset):
        on_prod_0yr_1yr_ff (float | Unset):
        on_prod_0yr_1yr_oi_swap (float | Unset):
        on_prod_1yr_2yr_b_swap (float | Unset):
        on_prod_1yr_2yr_ff (float | Unset):
        on_prod_1yr_2yr_oi_swap (float | Unset):
        on_prod_2yr_5yr_b_swap (float | Unset):
        on_prod_2yr_5yr_ff (float | Unset):
        on_prod_2yr_5yr_oi_swap (float | Unset):
        on_prod_5yr_10yr_b_swap (float | Unset):
        on_prod_5yr_10yr_ff (float | Unset):
        on_prod_5yr_10yr_oi_swap (float | Unset):
        on_prod_10yr_15yr_b_swap (float | Unset):
        on_prod_10yr_15yr_ff (float | Unset):
        on_prod_10yr_15yr_oi_swap (float | Unset):
        on_prod_15yr_20yr_b_swap (float | Unset):
        on_prod_15yr_20yr_ff (float | Unset):
        on_prod_15yr_20yr_oi_swap (float | Unset):
        on_prod_20yr_more_b_swap (float | Unset):
        on_prod_20yr_more_ff (float | Unset):
        on_prod_20yr_more_oi_swap (float | Unset):
        not_total_asset_class (float | Unset):
        not_prod_b_swap (float | Unset):
        not_prod_ff (float | Unset):
        not_prod_oi_swap (float | Unset):
        not_prod_intend_clear_b_swap (float | Unset):
        not_prod_intend_clear_ff (float | Unset):
        not_prod_intend_clear_oi_swap (float | Unset):
        not_prod_not_intend_clear_b_swap (float | Unset):
        not_prod_not_intend_clear_ff (float | Unset):
        not_prod_not_intend_clear_oi_swap (float | Unset):
        not_prod_usd_b_swap (float | Unset):
        not_prod_usd_ff (float | Unset):
        not_prod_usd_oi_swap (float | Unset):
        not_prod_cny_b_swap (float | Unset):
        not_prod_cny_ff (float | Unset):
        not_prod_cny_oi_swap (float | Unset):
        not_prod_eur_b_swap (float | Unset):
        not_prod_eur_ff (float | Unset):
        not_prod_eur_oi_swap (float | Unset):
        not_prod_gbp_b_swap (float | Unset):
        not_prod_gbp_ff (float | Unset):
        not_prod_gbp_oi_swap (float | Unset):
        not_prod_jpy_b_swap (float | Unset):
        not_prod_jpy_ff (float | Unset):
        not_prod_jpy_oi_swap (float | Unset):
        not_prod_hkd_b_swap (float | Unset):
        not_prod_hkd_ff (float | Unset):
        not_prod_hkd_oi_swap (float | Unset):
        not_prod_other_curr_b_swap (float | Unset):
        not_prod_other_curr_ff (float | Unset):
        not_prod_other_curr_oi_swap (float | Unset):
        not_prod_0yr_1yr_b_swap (float | Unset):
        not_prod_0yr_1yr_ff (float | Unset):
        not_prod_0yr_1yr_oi_swap (float | Unset):
        not_prod_1yr_2yr_b_swap (float | Unset):
        not_prod_1yr_2yr_ff (float | Unset):
        not_prod_1yr_2yr_oi_swap (float | Unset):
        not_prod_2yr_5yr_b_swap (float | Unset):
        not_prod_2yr_5yr_ff (float | Unset):
        not_prod_2yr_5yr_oi_swap (float | Unset):
        not_prod_5yr_10yr_b_swap (float | Unset):
        not_prod_5yr_10yr_ff (float | Unset):
        not_prod_5yr_10yr_oi_swap (float | Unset):
        not_prod_10yr_15yr_b_swap (float | Unset):
        not_prod_10yr_15yr_ff (float | Unset):
        not_prod_10yr_15yr_oi_swap (float | Unset):
        not_prod_15yr_20yr_b_swap (float | Unset):
        not_prod_15yr_20yr_ff (float | Unset):
        not_prod_15yr_20yr_oi_swap (float | Unset):
        not_prod_20yr_more_b_swap (float | Unset):
        not_prod_20yr_more_ff (float | Unset):
        not_prod_20yr_more_oi_swap (float | Unset):
    """

    end_of_date: datetime.date | Unset = UNSET
    on_total_asset_class: float | Unset = UNSET
    on_prod_b_swap: float | Unset = UNSET
    on_prod_ff: float | Unset = UNSET
    on_prod_oi_swap: float | Unset = UNSET
    on_prod_intend_clear_b_swap: float | Unset = UNSET
    on_prod_intend_clear_ff: float | Unset = UNSET
    on_prod_intend_clear_oi_swap: float | Unset = UNSET
    on_prod_not_intend_clear_b_swap: float | Unset = UNSET
    on_prod_not_intend_clear_ff: float | Unset = UNSET
    on_prod_not_intend_clear_oi_swap: float | Unset = UNSET
    on_prod_usd_b_swap: float | Unset = UNSET
    on_prod_usd_ff: float | Unset = UNSET
    on_prod_usd_oi_swap: float | Unset = UNSET
    on_prod_cny_b_swap: float | Unset = UNSET
    on_prod_cny_ff: float | Unset = UNSET
    on_prod_cny_oi_swap: float | Unset = UNSET
    on_prod_eur_b_swap: float | Unset = UNSET
    on_prod_eur_ff: float | Unset = UNSET
    on_prod_eur_oi_swap: float | Unset = UNSET
    on_prod_gbp_b_swap: float | Unset = UNSET
    on_prod_gbp_ff: float | Unset = UNSET
    on_prod_gbp_oi_swap: float | Unset = UNSET
    on_prod_jpy_b_swap: float | Unset = UNSET
    on_prod_jpy_ff: float | Unset = UNSET
    on_prod_jpy_oi_swap: float | Unset = UNSET
    on_prod_hkd_b_swap: float | Unset = UNSET
    on_prod_hkd_ff: float | Unset = UNSET
    on_prod_hkd_oi_swap: float | Unset = UNSET
    on_prod_other_curr_b_swap: float | Unset = UNSET
    on_prod_other_curr_ff: float | Unset = UNSET
    on_prod_other_curr_oi_swap: float | Unset = UNSET
    on_prod_0yr_1yr_b_swap: float | Unset = UNSET
    on_prod_0yr_1yr_ff: float | Unset = UNSET
    on_prod_0yr_1yr_oi_swap: float | Unset = UNSET
    on_prod_1yr_2yr_b_swap: float | Unset = UNSET
    on_prod_1yr_2yr_ff: float | Unset = UNSET
    on_prod_1yr_2yr_oi_swap: float | Unset = UNSET
    on_prod_2yr_5yr_b_swap: float | Unset = UNSET
    on_prod_2yr_5yr_ff: float | Unset = UNSET
    on_prod_2yr_5yr_oi_swap: float | Unset = UNSET
    on_prod_5yr_10yr_b_swap: float | Unset = UNSET
    on_prod_5yr_10yr_ff: float | Unset = UNSET
    on_prod_5yr_10yr_oi_swap: float | Unset = UNSET
    on_prod_10yr_15yr_b_swap: float | Unset = UNSET
    on_prod_10yr_15yr_ff: float | Unset = UNSET
    on_prod_10yr_15yr_oi_swap: float | Unset = UNSET
    on_prod_15yr_20yr_b_swap: float | Unset = UNSET
    on_prod_15yr_20yr_ff: float | Unset = UNSET
    on_prod_15yr_20yr_oi_swap: float | Unset = UNSET
    on_prod_20yr_more_b_swap: float | Unset = UNSET
    on_prod_20yr_more_ff: float | Unset = UNSET
    on_prod_20yr_more_oi_swap: float | Unset = UNSET
    not_total_asset_class: float | Unset = UNSET
    not_prod_b_swap: float | Unset = UNSET
    not_prod_ff: float | Unset = UNSET
    not_prod_oi_swap: float | Unset = UNSET
    not_prod_intend_clear_b_swap: float | Unset = UNSET
    not_prod_intend_clear_ff: float | Unset = UNSET
    not_prod_intend_clear_oi_swap: float | Unset = UNSET
    not_prod_not_intend_clear_b_swap: float | Unset = UNSET
    not_prod_not_intend_clear_ff: float | Unset = UNSET
    not_prod_not_intend_clear_oi_swap: float | Unset = UNSET
    not_prod_usd_b_swap: float | Unset = UNSET
    not_prod_usd_ff: float | Unset = UNSET
    not_prod_usd_oi_swap: float | Unset = UNSET
    not_prod_cny_b_swap: float | Unset = UNSET
    not_prod_cny_ff: float | Unset = UNSET
    not_prod_cny_oi_swap: float | Unset = UNSET
    not_prod_eur_b_swap: float | Unset = UNSET
    not_prod_eur_ff: float | Unset = UNSET
    not_prod_eur_oi_swap: float | Unset = UNSET
    not_prod_gbp_b_swap: float | Unset = UNSET
    not_prod_gbp_ff: float | Unset = UNSET
    not_prod_gbp_oi_swap: float | Unset = UNSET
    not_prod_jpy_b_swap: float | Unset = UNSET
    not_prod_jpy_ff: float | Unset = UNSET
    not_prod_jpy_oi_swap: float | Unset = UNSET
    not_prod_hkd_b_swap: float | Unset = UNSET
    not_prod_hkd_ff: float | Unset = UNSET
    not_prod_hkd_oi_swap: float | Unset = UNSET
    not_prod_other_curr_b_swap: float | Unset = UNSET
    not_prod_other_curr_ff: float | Unset = UNSET
    not_prod_other_curr_oi_swap: float | Unset = UNSET
    not_prod_0yr_1yr_b_swap: float | Unset = UNSET
    not_prod_0yr_1yr_ff: float | Unset = UNSET
    not_prod_0yr_1yr_oi_swap: float | Unset = UNSET
    not_prod_1yr_2yr_b_swap: float | Unset = UNSET
    not_prod_1yr_2yr_ff: float | Unset = UNSET
    not_prod_1yr_2yr_oi_swap: float | Unset = UNSET
    not_prod_2yr_5yr_b_swap: float | Unset = UNSET
    not_prod_2yr_5yr_ff: float | Unset = UNSET
    not_prod_2yr_5yr_oi_swap: float | Unset = UNSET
    not_prod_5yr_10yr_b_swap: float | Unset = UNSET
    not_prod_5yr_10yr_ff: float | Unset = UNSET
    not_prod_5yr_10yr_oi_swap: float | Unset = UNSET
    not_prod_10yr_15yr_b_swap: float | Unset = UNSET
    not_prod_10yr_15yr_ff: float | Unset = UNSET
    not_prod_10yr_15yr_oi_swap: float | Unset = UNSET
    not_prod_15yr_20yr_b_swap: float | Unset = UNSET
    not_prod_15yr_20yr_ff: float | Unset = UNSET
    not_prod_15yr_20yr_oi_swap: float | Unset = UNSET
    not_prod_20yr_more_b_swap: float | Unset = UNSET
    not_prod_20yr_more_ff: float | Unset = UNSET
    not_prod_20yr_more_oi_swap: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_date: str | Unset = UNSET
        if not isinstance(self.end_of_date, Unset):
            end_of_date = self.end_of_date.isoformat()

        on_total_asset_class = self.on_total_asset_class

        on_prod_b_swap = self.on_prod_b_swap

        on_prod_ff = self.on_prod_ff

        on_prod_oi_swap = self.on_prod_oi_swap

        on_prod_intend_clear_b_swap = self.on_prod_intend_clear_b_swap

        on_prod_intend_clear_ff = self.on_prod_intend_clear_ff

        on_prod_intend_clear_oi_swap = self.on_prod_intend_clear_oi_swap

        on_prod_not_intend_clear_b_swap = self.on_prod_not_intend_clear_b_swap

        on_prod_not_intend_clear_ff = self.on_prod_not_intend_clear_ff

        on_prod_not_intend_clear_oi_swap = self.on_prod_not_intend_clear_oi_swap

        on_prod_usd_b_swap = self.on_prod_usd_b_swap

        on_prod_usd_ff = self.on_prod_usd_ff

        on_prod_usd_oi_swap = self.on_prod_usd_oi_swap

        on_prod_cny_b_swap = self.on_prod_cny_b_swap

        on_prod_cny_ff = self.on_prod_cny_ff

        on_prod_cny_oi_swap = self.on_prod_cny_oi_swap

        on_prod_eur_b_swap = self.on_prod_eur_b_swap

        on_prod_eur_ff = self.on_prod_eur_ff

        on_prod_eur_oi_swap = self.on_prod_eur_oi_swap

        on_prod_gbp_b_swap = self.on_prod_gbp_b_swap

        on_prod_gbp_ff = self.on_prod_gbp_ff

        on_prod_gbp_oi_swap = self.on_prod_gbp_oi_swap

        on_prod_jpy_b_swap = self.on_prod_jpy_b_swap

        on_prod_jpy_ff = self.on_prod_jpy_ff

        on_prod_jpy_oi_swap = self.on_prod_jpy_oi_swap

        on_prod_hkd_b_swap = self.on_prod_hkd_b_swap

        on_prod_hkd_ff = self.on_prod_hkd_ff

        on_prod_hkd_oi_swap = self.on_prod_hkd_oi_swap

        on_prod_other_curr_b_swap = self.on_prod_other_curr_b_swap

        on_prod_other_curr_ff = self.on_prod_other_curr_ff

        on_prod_other_curr_oi_swap = self.on_prod_other_curr_oi_swap

        on_prod_0yr_1yr_b_swap = self.on_prod_0yr_1yr_b_swap

        on_prod_0yr_1yr_ff = self.on_prod_0yr_1yr_ff

        on_prod_0yr_1yr_oi_swap = self.on_prod_0yr_1yr_oi_swap

        on_prod_1yr_2yr_b_swap = self.on_prod_1yr_2yr_b_swap

        on_prod_1yr_2yr_ff = self.on_prod_1yr_2yr_ff

        on_prod_1yr_2yr_oi_swap = self.on_prod_1yr_2yr_oi_swap

        on_prod_2yr_5yr_b_swap = self.on_prod_2yr_5yr_b_swap

        on_prod_2yr_5yr_ff = self.on_prod_2yr_5yr_ff

        on_prod_2yr_5yr_oi_swap = self.on_prod_2yr_5yr_oi_swap

        on_prod_5yr_10yr_b_swap = self.on_prod_5yr_10yr_b_swap

        on_prod_5yr_10yr_ff = self.on_prod_5yr_10yr_ff

        on_prod_5yr_10yr_oi_swap = self.on_prod_5yr_10yr_oi_swap

        on_prod_10yr_15yr_b_swap = self.on_prod_10yr_15yr_b_swap

        on_prod_10yr_15yr_ff = self.on_prod_10yr_15yr_ff

        on_prod_10yr_15yr_oi_swap = self.on_prod_10yr_15yr_oi_swap

        on_prod_15yr_20yr_b_swap = self.on_prod_15yr_20yr_b_swap

        on_prod_15yr_20yr_ff = self.on_prod_15yr_20yr_ff

        on_prod_15yr_20yr_oi_swap = self.on_prod_15yr_20yr_oi_swap

        on_prod_20yr_more_b_swap = self.on_prod_20yr_more_b_swap

        on_prod_20yr_more_ff = self.on_prod_20yr_more_ff

        on_prod_20yr_more_oi_swap = self.on_prod_20yr_more_oi_swap

        not_total_asset_class = self.not_total_asset_class

        not_prod_b_swap = self.not_prod_b_swap

        not_prod_ff = self.not_prod_ff

        not_prod_oi_swap = self.not_prod_oi_swap

        not_prod_intend_clear_b_swap = self.not_prod_intend_clear_b_swap

        not_prod_intend_clear_ff = self.not_prod_intend_clear_ff

        not_prod_intend_clear_oi_swap = self.not_prod_intend_clear_oi_swap

        not_prod_not_intend_clear_b_swap = self.not_prod_not_intend_clear_b_swap

        not_prod_not_intend_clear_ff = self.not_prod_not_intend_clear_ff

        not_prod_not_intend_clear_oi_swap = self.not_prod_not_intend_clear_oi_swap

        not_prod_usd_b_swap = self.not_prod_usd_b_swap

        not_prod_usd_ff = self.not_prod_usd_ff

        not_prod_usd_oi_swap = self.not_prod_usd_oi_swap

        not_prod_cny_b_swap = self.not_prod_cny_b_swap

        not_prod_cny_ff = self.not_prod_cny_ff

        not_prod_cny_oi_swap = self.not_prod_cny_oi_swap

        not_prod_eur_b_swap = self.not_prod_eur_b_swap

        not_prod_eur_ff = self.not_prod_eur_ff

        not_prod_eur_oi_swap = self.not_prod_eur_oi_swap

        not_prod_gbp_b_swap = self.not_prod_gbp_b_swap

        not_prod_gbp_ff = self.not_prod_gbp_ff

        not_prod_gbp_oi_swap = self.not_prod_gbp_oi_swap

        not_prod_jpy_b_swap = self.not_prod_jpy_b_swap

        not_prod_jpy_ff = self.not_prod_jpy_ff

        not_prod_jpy_oi_swap = self.not_prod_jpy_oi_swap

        not_prod_hkd_b_swap = self.not_prod_hkd_b_swap

        not_prod_hkd_ff = self.not_prod_hkd_ff

        not_prod_hkd_oi_swap = self.not_prod_hkd_oi_swap

        not_prod_other_curr_b_swap = self.not_prod_other_curr_b_swap

        not_prod_other_curr_ff = self.not_prod_other_curr_ff

        not_prod_other_curr_oi_swap = self.not_prod_other_curr_oi_swap

        not_prod_0yr_1yr_b_swap = self.not_prod_0yr_1yr_b_swap

        not_prod_0yr_1yr_ff = self.not_prod_0yr_1yr_ff

        not_prod_0yr_1yr_oi_swap = self.not_prod_0yr_1yr_oi_swap

        not_prod_1yr_2yr_b_swap = self.not_prod_1yr_2yr_b_swap

        not_prod_1yr_2yr_ff = self.not_prod_1yr_2yr_ff

        not_prod_1yr_2yr_oi_swap = self.not_prod_1yr_2yr_oi_swap

        not_prod_2yr_5yr_b_swap = self.not_prod_2yr_5yr_b_swap

        not_prod_2yr_5yr_ff = self.not_prod_2yr_5yr_ff

        not_prod_2yr_5yr_oi_swap = self.not_prod_2yr_5yr_oi_swap

        not_prod_5yr_10yr_b_swap = self.not_prod_5yr_10yr_b_swap

        not_prod_5yr_10yr_ff = self.not_prod_5yr_10yr_ff

        not_prod_5yr_10yr_oi_swap = self.not_prod_5yr_10yr_oi_swap

        not_prod_10yr_15yr_b_swap = self.not_prod_10yr_15yr_b_swap

        not_prod_10yr_15yr_ff = self.not_prod_10yr_15yr_ff

        not_prod_10yr_15yr_oi_swap = self.not_prod_10yr_15yr_oi_swap

        not_prod_15yr_20yr_b_swap = self.not_prod_15yr_20yr_b_swap

        not_prod_15yr_20yr_ff = self.not_prod_15yr_20yr_ff

        not_prod_15yr_20yr_oi_swap = self.not_prod_15yr_20yr_oi_swap

        not_prod_20yr_more_b_swap = self.not_prod_20yr_more_b_swap

        not_prod_20yr_more_ff = self.not_prod_20yr_more_ff

        not_prod_20yr_more_oi_swap = self.not_prod_20yr_more_oi_swap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_date is not UNSET:
            field_dict["end_of_date"] = end_of_date
        if on_total_asset_class is not UNSET:
            field_dict["on_total_asset_class"] = on_total_asset_class
        if on_prod_b_swap is not UNSET:
            field_dict["on_prod_b_swap"] = on_prod_b_swap
        if on_prod_ff is not UNSET:
            field_dict["on_prod_ff"] = on_prod_ff
        if on_prod_oi_swap is not UNSET:
            field_dict["on_prod_oi_swap"] = on_prod_oi_swap
        if on_prod_intend_clear_b_swap is not UNSET:
            field_dict["on_prod_intend_clear_b_swap"] = on_prod_intend_clear_b_swap
        if on_prod_intend_clear_ff is not UNSET:
            field_dict["on_prod_intend_clear_ff"] = on_prod_intend_clear_ff
        if on_prod_intend_clear_oi_swap is not UNSET:
            field_dict["on_prod_intend_clear_oi_swap"] = on_prod_intend_clear_oi_swap
        if on_prod_not_intend_clear_b_swap is not UNSET:
            field_dict["on_prod_not_intend_clear_b_swap"] = (
                on_prod_not_intend_clear_b_swap
            )
        if on_prod_not_intend_clear_ff is not UNSET:
            field_dict["on_prod_not_intend_clear_ff"] = on_prod_not_intend_clear_ff
        if on_prod_not_intend_clear_oi_swap is not UNSET:
            field_dict["on_prod_not_intend_clear_oi_swap"] = (
                on_prod_not_intend_clear_oi_swap
            )
        if on_prod_usd_b_swap is not UNSET:
            field_dict["on_prod_usd_b_swap"] = on_prod_usd_b_swap
        if on_prod_usd_ff is not UNSET:
            field_dict["on_prod_usd_ff"] = on_prod_usd_ff
        if on_prod_usd_oi_swap is not UNSET:
            field_dict["on_prod_usd_oi_swap"] = on_prod_usd_oi_swap
        if on_prod_cny_b_swap is not UNSET:
            field_dict["on_prod_cny_b_swap"] = on_prod_cny_b_swap
        if on_prod_cny_ff is not UNSET:
            field_dict["on_prod_cny_ff"] = on_prod_cny_ff
        if on_prod_cny_oi_swap is not UNSET:
            field_dict["on_prod_cny_oi_swap"] = on_prod_cny_oi_swap
        if on_prod_eur_b_swap is not UNSET:
            field_dict["on_prod_eur_b_swap"] = on_prod_eur_b_swap
        if on_prod_eur_ff is not UNSET:
            field_dict["on_prod_eur_ff"] = on_prod_eur_ff
        if on_prod_eur_oi_swap is not UNSET:
            field_dict["on_prod_eur_oi_swap"] = on_prod_eur_oi_swap
        if on_prod_gbp_b_swap is not UNSET:
            field_dict["on_prod_gbp_b_swap"] = on_prod_gbp_b_swap
        if on_prod_gbp_ff is not UNSET:
            field_dict["on_prod_gbp_ff"] = on_prod_gbp_ff
        if on_prod_gbp_oi_swap is not UNSET:
            field_dict["on_prod_gbp_oi_swap"] = on_prod_gbp_oi_swap
        if on_prod_jpy_b_swap is not UNSET:
            field_dict["on_prod_jpy_b_swap"] = on_prod_jpy_b_swap
        if on_prod_jpy_ff is not UNSET:
            field_dict["on_prod_jpy_ff"] = on_prod_jpy_ff
        if on_prod_jpy_oi_swap is not UNSET:
            field_dict["on_prod_jpy_oi_swap"] = on_prod_jpy_oi_swap
        if on_prod_hkd_b_swap is not UNSET:
            field_dict["on_prod_hkd_b_swap"] = on_prod_hkd_b_swap
        if on_prod_hkd_ff is not UNSET:
            field_dict["on_prod_hkd_ff"] = on_prod_hkd_ff
        if on_prod_hkd_oi_swap is not UNSET:
            field_dict["on_prod_hkd_oi_swap"] = on_prod_hkd_oi_swap
        if on_prod_other_curr_b_swap is not UNSET:
            field_dict["on_prod_other_curr_b_swap"] = on_prod_other_curr_b_swap
        if on_prod_other_curr_ff is not UNSET:
            field_dict["on_prod_other_curr_ff"] = on_prod_other_curr_ff
        if on_prod_other_curr_oi_swap is not UNSET:
            field_dict["on_prod_other_curr_oi_swap"] = on_prod_other_curr_oi_swap
        if on_prod_0yr_1yr_b_swap is not UNSET:
            field_dict["on_prod_0yr_1yr_b_swap"] = on_prod_0yr_1yr_b_swap
        if on_prod_0yr_1yr_ff is not UNSET:
            field_dict["on_prod_0yr_1yr_ff"] = on_prod_0yr_1yr_ff
        if on_prod_0yr_1yr_oi_swap is not UNSET:
            field_dict["on_prod_0yr_1yr_oi_swap"] = on_prod_0yr_1yr_oi_swap
        if on_prod_1yr_2yr_b_swap is not UNSET:
            field_dict["on_prod_1yr_2yr_b_swap"] = on_prod_1yr_2yr_b_swap
        if on_prod_1yr_2yr_ff is not UNSET:
            field_dict["on_prod_1yr_2yr_ff"] = on_prod_1yr_2yr_ff
        if on_prod_1yr_2yr_oi_swap is not UNSET:
            field_dict["on_prod_1yr_2yr_oi_swap"] = on_prod_1yr_2yr_oi_swap
        if on_prod_2yr_5yr_b_swap is not UNSET:
            field_dict["on_prod_2yr_5yr_b_swap"] = on_prod_2yr_5yr_b_swap
        if on_prod_2yr_5yr_ff is not UNSET:
            field_dict["on_prod_2yr_5yr_ff"] = on_prod_2yr_5yr_ff
        if on_prod_2yr_5yr_oi_swap is not UNSET:
            field_dict["on_prod_2yr_5yr_oi_swap"] = on_prod_2yr_5yr_oi_swap
        if on_prod_5yr_10yr_b_swap is not UNSET:
            field_dict["on_prod_5yr_10yr_b_swap"] = on_prod_5yr_10yr_b_swap
        if on_prod_5yr_10yr_ff is not UNSET:
            field_dict["on_prod_5yr_10yr_ff"] = on_prod_5yr_10yr_ff
        if on_prod_5yr_10yr_oi_swap is not UNSET:
            field_dict["on_prod_5yr_10yr_oi_swap"] = on_prod_5yr_10yr_oi_swap
        if on_prod_10yr_15yr_b_swap is not UNSET:
            field_dict["on_prod_10yr_15yr_b_swap"] = on_prod_10yr_15yr_b_swap
        if on_prod_10yr_15yr_ff is not UNSET:
            field_dict["on_prod_10yr_15yr_ff"] = on_prod_10yr_15yr_ff
        if on_prod_10yr_15yr_oi_swap is not UNSET:
            field_dict["on_prod_10yr_15yr_oi_swap"] = on_prod_10yr_15yr_oi_swap
        if on_prod_15yr_20yr_b_swap is not UNSET:
            field_dict["on_prod_15yr_20yr_b_swap"] = on_prod_15yr_20yr_b_swap
        if on_prod_15yr_20yr_ff is not UNSET:
            field_dict["on_prod_15yr_20yr_ff"] = on_prod_15yr_20yr_ff
        if on_prod_15yr_20yr_oi_swap is not UNSET:
            field_dict["on_prod_15yr_20yr_oi_swap"] = on_prod_15yr_20yr_oi_swap
        if on_prod_20yr_more_b_swap is not UNSET:
            field_dict["on_prod_20yr_more_b_swap"] = on_prod_20yr_more_b_swap
        if on_prod_20yr_more_ff is not UNSET:
            field_dict["on_prod_20yr_more_ff"] = on_prod_20yr_more_ff
        if on_prod_20yr_more_oi_swap is not UNSET:
            field_dict["on_prod_20yr_more_oi_swap"] = on_prod_20yr_more_oi_swap
        if not_total_asset_class is not UNSET:
            field_dict["not_total_asset_class"] = not_total_asset_class
        if not_prod_b_swap is not UNSET:
            field_dict["not_prod_b_swap"] = not_prod_b_swap
        if not_prod_ff is not UNSET:
            field_dict["not_prod_ff"] = not_prod_ff
        if not_prod_oi_swap is not UNSET:
            field_dict["not_prod_oi_swap"] = not_prod_oi_swap
        if not_prod_intend_clear_b_swap is not UNSET:
            field_dict["not_prod_intend_clear_b_swap"] = not_prod_intend_clear_b_swap
        if not_prod_intend_clear_ff is not UNSET:
            field_dict["not_prod_intend_clear_ff"] = not_prod_intend_clear_ff
        if not_prod_intend_clear_oi_swap is not UNSET:
            field_dict["not_prod_intend_clear_oi_swap"] = not_prod_intend_clear_oi_swap
        if not_prod_not_intend_clear_b_swap is not UNSET:
            field_dict["not_prod_not_intend_clear_b_swap"] = (
                not_prod_not_intend_clear_b_swap
            )
        if not_prod_not_intend_clear_ff is not UNSET:
            field_dict["not_prod_not_intend_clear_ff"] = not_prod_not_intend_clear_ff
        if not_prod_not_intend_clear_oi_swap is not UNSET:
            field_dict["not_prod_not_intend_clear_oi_swap"] = (
                not_prod_not_intend_clear_oi_swap
            )
        if not_prod_usd_b_swap is not UNSET:
            field_dict["not_prod_usd_b_swap"] = not_prod_usd_b_swap
        if not_prod_usd_ff is not UNSET:
            field_dict["not_prod_usd_ff"] = not_prod_usd_ff
        if not_prod_usd_oi_swap is not UNSET:
            field_dict["not_prod_usd_oi_swap"] = not_prod_usd_oi_swap
        if not_prod_cny_b_swap is not UNSET:
            field_dict["not_prod_cny_b_swap"] = not_prod_cny_b_swap
        if not_prod_cny_ff is not UNSET:
            field_dict["not_prod_cny_ff"] = not_prod_cny_ff
        if not_prod_cny_oi_swap is not UNSET:
            field_dict["not_prod_cny_oi_swap"] = not_prod_cny_oi_swap
        if not_prod_eur_b_swap is not UNSET:
            field_dict["not_prod_eur_b_swap"] = not_prod_eur_b_swap
        if not_prod_eur_ff is not UNSET:
            field_dict["not_prod_eur_ff"] = not_prod_eur_ff
        if not_prod_eur_oi_swap is not UNSET:
            field_dict["not_prod_eur_oi_swap"] = not_prod_eur_oi_swap
        if not_prod_gbp_b_swap is not UNSET:
            field_dict["not_prod_gbp_b_swap"] = not_prod_gbp_b_swap
        if not_prod_gbp_ff is not UNSET:
            field_dict["not_prod_gbp_ff"] = not_prod_gbp_ff
        if not_prod_gbp_oi_swap is not UNSET:
            field_dict["not_prod_gbp_oi_swap"] = not_prod_gbp_oi_swap
        if not_prod_jpy_b_swap is not UNSET:
            field_dict["not_prod_jpy_b_swap"] = not_prod_jpy_b_swap
        if not_prod_jpy_ff is not UNSET:
            field_dict["not_prod_jpy_ff"] = not_prod_jpy_ff
        if not_prod_jpy_oi_swap is not UNSET:
            field_dict["not_prod_jpy_oi_swap"] = not_prod_jpy_oi_swap
        if not_prod_hkd_b_swap is not UNSET:
            field_dict["not_prod_hkd_b_swap"] = not_prod_hkd_b_swap
        if not_prod_hkd_ff is not UNSET:
            field_dict["not_prod_hkd_ff"] = not_prod_hkd_ff
        if not_prod_hkd_oi_swap is not UNSET:
            field_dict["not_prod_hkd_oi_swap"] = not_prod_hkd_oi_swap
        if not_prod_other_curr_b_swap is not UNSET:
            field_dict["not_prod_other_curr_b_swap"] = not_prod_other_curr_b_swap
        if not_prod_other_curr_ff is not UNSET:
            field_dict["not_prod_other_curr_ff"] = not_prod_other_curr_ff
        if not_prod_other_curr_oi_swap is not UNSET:
            field_dict["not_prod_other_curr_oi_swap"] = not_prod_other_curr_oi_swap
        if not_prod_0yr_1yr_b_swap is not UNSET:
            field_dict["not_prod_0yr_1yr_b_swap"] = not_prod_0yr_1yr_b_swap
        if not_prod_0yr_1yr_ff is not UNSET:
            field_dict["not_prod_0yr_1yr_ff"] = not_prod_0yr_1yr_ff
        if not_prod_0yr_1yr_oi_swap is not UNSET:
            field_dict["not_prod_0yr_1yr_oi_swap"] = not_prod_0yr_1yr_oi_swap
        if not_prod_1yr_2yr_b_swap is not UNSET:
            field_dict["not_prod_1yr_2yr_b_swap"] = not_prod_1yr_2yr_b_swap
        if not_prod_1yr_2yr_ff is not UNSET:
            field_dict["not_prod_1yr_2yr_ff"] = not_prod_1yr_2yr_ff
        if not_prod_1yr_2yr_oi_swap is not UNSET:
            field_dict["not_prod_1yr_2yr_oi_swap"] = not_prod_1yr_2yr_oi_swap
        if not_prod_2yr_5yr_b_swap is not UNSET:
            field_dict["not_prod_2yr_5yr_b_swap"] = not_prod_2yr_5yr_b_swap
        if not_prod_2yr_5yr_ff is not UNSET:
            field_dict["not_prod_2yr_5yr_ff"] = not_prod_2yr_5yr_ff
        if not_prod_2yr_5yr_oi_swap is not UNSET:
            field_dict["not_prod_2yr_5yr_oi_swap"] = not_prod_2yr_5yr_oi_swap
        if not_prod_5yr_10yr_b_swap is not UNSET:
            field_dict["not_prod_5yr_10yr_b_swap"] = not_prod_5yr_10yr_b_swap
        if not_prod_5yr_10yr_ff is not UNSET:
            field_dict["not_prod_5yr_10yr_ff"] = not_prod_5yr_10yr_ff
        if not_prod_5yr_10yr_oi_swap is not UNSET:
            field_dict["not_prod_5yr_10yr_oi_swap"] = not_prod_5yr_10yr_oi_swap
        if not_prod_10yr_15yr_b_swap is not UNSET:
            field_dict["not_prod_10yr_15yr_b_swap"] = not_prod_10yr_15yr_b_swap
        if not_prod_10yr_15yr_ff is not UNSET:
            field_dict["not_prod_10yr_15yr_ff"] = not_prod_10yr_15yr_ff
        if not_prod_10yr_15yr_oi_swap is not UNSET:
            field_dict["not_prod_10yr_15yr_oi_swap"] = not_prod_10yr_15yr_oi_swap
        if not_prod_15yr_20yr_b_swap is not UNSET:
            field_dict["not_prod_15yr_20yr_b_swap"] = not_prod_15yr_20yr_b_swap
        if not_prod_15yr_20yr_ff is not UNSET:
            field_dict["not_prod_15yr_20yr_ff"] = not_prod_15yr_20yr_ff
        if not_prod_15yr_20yr_oi_swap is not UNSET:
            field_dict["not_prod_15yr_20yr_oi_swap"] = not_prod_15yr_20yr_oi_swap
        if not_prod_20yr_more_b_swap is not UNSET:
            field_dict["not_prod_20yr_more_b_swap"] = not_prod_20yr_more_b_swap
        if not_prod_20yr_more_ff is not UNSET:
            field_dict["not_prod_20yr_more_ff"] = not_prod_20yr_more_ff
        if not_prod_20yr_more_oi_swap is not UNSET:
            field_dict["not_prod_20yr_more_oi_swap"] = not_prod_20yr_more_oi_swap

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_date = d.pop("end_of_date", UNSET)
        end_of_date: datetime.date | Unset
        if isinstance(_end_of_date, Unset):
            end_of_date = UNSET
        else:
            end_of_date = datetime.date.fromisoformat(_end_of_date)

        on_total_asset_class = d.pop("on_total_asset_class", UNSET)

        on_prod_b_swap = d.pop("on_prod_b_swap", UNSET)

        on_prod_ff = d.pop("on_prod_ff", UNSET)

        on_prod_oi_swap = d.pop("on_prod_oi_swap", UNSET)

        on_prod_intend_clear_b_swap = d.pop("on_prod_intend_clear_b_swap", UNSET)

        on_prod_intend_clear_ff = d.pop("on_prod_intend_clear_ff", UNSET)

        on_prod_intend_clear_oi_swap = d.pop("on_prod_intend_clear_oi_swap", UNSET)

        on_prod_not_intend_clear_b_swap = d.pop(
            "on_prod_not_intend_clear_b_swap", UNSET
        )

        on_prod_not_intend_clear_ff = d.pop("on_prod_not_intend_clear_ff", UNSET)

        on_prod_not_intend_clear_oi_swap = d.pop(
            "on_prod_not_intend_clear_oi_swap", UNSET
        )

        on_prod_usd_b_swap = d.pop("on_prod_usd_b_swap", UNSET)

        on_prod_usd_ff = d.pop("on_prod_usd_ff", UNSET)

        on_prod_usd_oi_swap = d.pop("on_prod_usd_oi_swap", UNSET)

        on_prod_cny_b_swap = d.pop("on_prod_cny_b_swap", UNSET)

        on_prod_cny_ff = d.pop("on_prod_cny_ff", UNSET)

        on_prod_cny_oi_swap = d.pop("on_prod_cny_oi_swap", UNSET)

        on_prod_eur_b_swap = d.pop("on_prod_eur_b_swap", UNSET)

        on_prod_eur_ff = d.pop("on_prod_eur_ff", UNSET)

        on_prod_eur_oi_swap = d.pop("on_prod_eur_oi_swap", UNSET)

        on_prod_gbp_b_swap = d.pop("on_prod_gbp_b_swap", UNSET)

        on_prod_gbp_ff = d.pop("on_prod_gbp_ff", UNSET)

        on_prod_gbp_oi_swap = d.pop("on_prod_gbp_oi_swap", UNSET)

        on_prod_jpy_b_swap = d.pop("on_prod_jpy_b_swap", UNSET)

        on_prod_jpy_ff = d.pop("on_prod_jpy_ff", UNSET)

        on_prod_jpy_oi_swap = d.pop("on_prod_jpy_oi_swap", UNSET)

        on_prod_hkd_b_swap = d.pop("on_prod_hkd_b_swap", UNSET)

        on_prod_hkd_ff = d.pop("on_prod_hkd_ff", UNSET)

        on_prod_hkd_oi_swap = d.pop("on_prod_hkd_oi_swap", UNSET)

        on_prod_other_curr_b_swap = d.pop("on_prod_other_curr_b_swap", UNSET)

        on_prod_other_curr_ff = d.pop("on_prod_other_curr_ff", UNSET)

        on_prod_other_curr_oi_swap = d.pop("on_prod_other_curr_oi_swap", UNSET)

        on_prod_0yr_1yr_b_swap = d.pop("on_prod_0yr_1yr_b_swap", UNSET)

        on_prod_0yr_1yr_ff = d.pop("on_prod_0yr_1yr_ff", UNSET)

        on_prod_0yr_1yr_oi_swap = d.pop("on_prod_0yr_1yr_oi_swap", UNSET)

        on_prod_1yr_2yr_b_swap = d.pop("on_prod_1yr_2yr_b_swap", UNSET)

        on_prod_1yr_2yr_ff = d.pop("on_prod_1yr_2yr_ff", UNSET)

        on_prod_1yr_2yr_oi_swap = d.pop("on_prod_1yr_2yr_oi_swap", UNSET)

        on_prod_2yr_5yr_b_swap = d.pop("on_prod_2yr_5yr_b_swap", UNSET)

        on_prod_2yr_5yr_ff = d.pop("on_prod_2yr_5yr_ff", UNSET)

        on_prod_2yr_5yr_oi_swap = d.pop("on_prod_2yr_5yr_oi_swap", UNSET)

        on_prod_5yr_10yr_b_swap = d.pop("on_prod_5yr_10yr_b_swap", UNSET)

        on_prod_5yr_10yr_ff = d.pop("on_prod_5yr_10yr_ff", UNSET)

        on_prod_5yr_10yr_oi_swap = d.pop("on_prod_5yr_10yr_oi_swap", UNSET)

        on_prod_10yr_15yr_b_swap = d.pop("on_prod_10yr_15yr_b_swap", UNSET)

        on_prod_10yr_15yr_ff = d.pop("on_prod_10yr_15yr_ff", UNSET)

        on_prod_10yr_15yr_oi_swap = d.pop("on_prod_10yr_15yr_oi_swap", UNSET)

        on_prod_15yr_20yr_b_swap = d.pop("on_prod_15yr_20yr_b_swap", UNSET)

        on_prod_15yr_20yr_ff = d.pop("on_prod_15yr_20yr_ff", UNSET)

        on_prod_15yr_20yr_oi_swap = d.pop("on_prod_15yr_20yr_oi_swap", UNSET)

        on_prod_20yr_more_b_swap = d.pop("on_prod_20yr_more_b_swap", UNSET)

        on_prod_20yr_more_ff = d.pop("on_prod_20yr_more_ff", UNSET)

        on_prod_20yr_more_oi_swap = d.pop("on_prod_20yr_more_oi_swap", UNSET)

        not_total_asset_class = d.pop("not_total_asset_class", UNSET)

        not_prod_b_swap = d.pop("not_prod_b_swap", UNSET)

        not_prod_ff = d.pop("not_prod_ff", UNSET)

        not_prod_oi_swap = d.pop("not_prod_oi_swap", UNSET)

        not_prod_intend_clear_b_swap = d.pop("not_prod_intend_clear_b_swap", UNSET)

        not_prod_intend_clear_ff = d.pop("not_prod_intend_clear_ff", UNSET)

        not_prod_intend_clear_oi_swap = d.pop("not_prod_intend_clear_oi_swap", UNSET)

        not_prod_not_intend_clear_b_swap = d.pop(
            "not_prod_not_intend_clear_b_swap", UNSET
        )

        not_prod_not_intend_clear_ff = d.pop("not_prod_not_intend_clear_ff", UNSET)

        not_prod_not_intend_clear_oi_swap = d.pop(
            "not_prod_not_intend_clear_oi_swap", UNSET
        )

        not_prod_usd_b_swap = d.pop("not_prod_usd_b_swap", UNSET)

        not_prod_usd_ff = d.pop("not_prod_usd_ff", UNSET)

        not_prod_usd_oi_swap = d.pop("not_prod_usd_oi_swap", UNSET)

        not_prod_cny_b_swap = d.pop("not_prod_cny_b_swap", UNSET)

        not_prod_cny_ff = d.pop("not_prod_cny_ff", UNSET)

        not_prod_cny_oi_swap = d.pop("not_prod_cny_oi_swap", UNSET)

        not_prod_eur_b_swap = d.pop("not_prod_eur_b_swap", UNSET)

        not_prod_eur_ff = d.pop("not_prod_eur_ff", UNSET)

        not_prod_eur_oi_swap = d.pop("not_prod_eur_oi_swap", UNSET)

        not_prod_gbp_b_swap = d.pop("not_prod_gbp_b_swap", UNSET)

        not_prod_gbp_ff = d.pop("not_prod_gbp_ff", UNSET)

        not_prod_gbp_oi_swap = d.pop("not_prod_gbp_oi_swap", UNSET)

        not_prod_jpy_b_swap = d.pop("not_prod_jpy_b_swap", UNSET)

        not_prod_jpy_ff = d.pop("not_prod_jpy_ff", UNSET)

        not_prod_jpy_oi_swap = d.pop("not_prod_jpy_oi_swap", UNSET)

        not_prod_hkd_b_swap = d.pop("not_prod_hkd_b_swap", UNSET)

        not_prod_hkd_ff = d.pop("not_prod_hkd_ff", UNSET)

        not_prod_hkd_oi_swap = d.pop("not_prod_hkd_oi_swap", UNSET)

        not_prod_other_curr_b_swap = d.pop("not_prod_other_curr_b_swap", UNSET)

        not_prod_other_curr_ff = d.pop("not_prod_other_curr_ff", UNSET)

        not_prod_other_curr_oi_swap = d.pop("not_prod_other_curr_oi_swap", UNSET)

        not_prod_0yr_1yr_b_swap = d.pop("not_prod_0yr_1yr_b_swap", UNSET)

        not_prod_0yr_1yr_ff = d.pop("not_prod_0yr_1yr_ff", UNSET)

        not_prod_0yr_1yr_oi_swap = d.pop("not_prod_0yr_1yr_oi_swap", UNSET)

        not_prod_1yr_2yr_b_swap = d.pop("not_prod_1yr_2yr_b_swap", UNSET)

        not_prod_1yr_2yr_ff = d.pop("not_prod_1yr_2yr_ff", UNSET)

        not_prod_1yr_2yr_oi_swap = d.pop("not_prod_1yr_2yr_oi_swap", UNSET)

        not_prod_2yr_5yr_b_swap = d.pop("not_prod_2yr_5yr_b_swap", UNSET)

        not_prod_2yr_5yr_ff = d.pop("not_prod_2yr_5yr_ff", UNSET)

        not_prod_2yr_5yr_oi_swap = d.pop("not_prod_2yr_5yr_oi_swap", UNSET)

        not_prod_5yr_10yr_b_swap = d.pop("not_prod_5yr_10yr_b_swap", UNSET)

        not_prod_5yr_10yr_ff = d.pop("not_prod_5yr_10yr_ff", UNSET)

        not_prod_5yr_10yr_oi_swap = d.pop("not_prod_5yr_10yr_oi_swap", UNSET)

        not_prod_10yr_15yr_b_swap = d.pop("not_prod_10yr_15yr_b_swap", UNSET)

        not_prod_10yr_15yr_ff = d.pop("not_prod_10yr_15yr_ff", UNSET)

        not_prod_10yr_15yr_oi_swap = d.pop("not_prod_10yr_15yr_oi_swap", UNSET)

        not_prod_15yr_20yr_b_swap = d.pop("not_prod_15yr_20yr_b_swap", UNSET)

        not_prod_15yr_20yr_ff = d.pop("not_prod_15yr_20yr_ff", UNSET)

        not_prod_15yr_20yr_oi_swap = d.pop("not_prod_15yr_20yr_oi_swap", UNSET)

        not_prod_20yr_more_b_swap = d.pop("not_prod_20yr_more_b_swap", UNSET)

        not_prod_20yr_more_ff = d.pop("not_prod_20yr_more_ff", UNSET)

        not_prod_20yr_more_oi_swap = d.pop("not_prod_20yr_more_oi_swap", UNSET)

        record = cls(
            end_of_date=end_of_date,
            on_total_asset_class=on_total_asset_class,
            on_prod_b_swap=on_prod_b_swap,
            on_prod_ff=on_prod_ff,
            on_prod_oi_swap=on_prod_oi_swap,
            on_prod_intend_clear_b_swap=on_prod_intend_clear_b_swap,
            on_prod_intend_clear_ff=on_prod_intend_clear_ff,
            on_prod_intend_clear_oi_swap=on_prod_intend_clear_oi_swap,
            on_prod_not_intend_clear_b_swap=on_prod_not_intend_clear_b_swap,
            on_prod_not_intend_clear_ff=on_prod_not_intend_clear_ff,
            on_prod_not_intend_clear_oi_swap=on_prod_not_intend_clear_oi_swap,
            on_prod_usd_b_swap=on_prod_usd_b_swap,
            on_prod_usd_ff=on_prod_usd_ff,
            on_prod_usd_oi_swap=on_prod_usd_oi_swap,
            on_prod_cny_b_swap=on_prod_cny_b_swap,
            on_prod_cny_ff=on_prod_cny_ff,
            on_prod_cny_oi_swap=on_prod_cny_oi_swap,
            on_prod_eur_b_swap=on_prod_eur_b_swap,
            on_prod_eur_ff=on_prod_eur_ff,
            on_prod_eur_oi_swap=on_prod_eur_oi_swap,
            on_prod_gbp_b_swap=on_prod_gbp_b_swap,
            on_prod_gbp_ff=on_prod_gbp_ff,
            on_prod_gbp_oi_swap=on_prod_gbp_oi_swap,
            on_prod_jpy_b_swap=on_prod_jpy_b_swap,
            on_prod_jpy_ff=on_prod_jpy_ff,
            on_prod_jpy_oi_swap=on_prod_jpy_oi_swap,
            on_prod_hkd_b_swap=on_prod_hkd_b_swap,
            on_prod_hkd_ff=on_prod_hkd_ff,
            on_prod_hkd_oi_swap=on_prod_hkd_oi_swap,
            on_prod_other_curr_b_swap=on_prod_other_curr_b_swap,
            on_prod_other_curr_ff=on_prod_other_curr_ff,
            on_prod_other_curr_oi_swap=on_prod_other_curr_oi_swap,
            on_prod_0yr_1yr_b_swap=on_prod_0yr_1yr_b_swap,
            on_prod_0yr_1yr_ff=on_prod_0yr_1yr_ff,
            on_prod_0yr_1yr_oi_swap=on_prod_0yr_1yr_oi_swap,
            on_prod_1yr_2yr_b_swap=on_prod_1yr_2yr_b_swap,
            on_prod_1yr_2yr_ff=on_prod_1yr_2yr_ff,
            on_prod_1yr_2yr_oi_swap=on_prod_1yr_2yr_oi_swap,
            on_prod_2yr_5yr_b_swap=on_prod_2yr_5yr_b_swap,
            on_prod_2yr_5yr_ff=on_prod_2yr_5yr_ff,
            on_prod_2yr_5yr_oi_swap=on_prod_2yr_5yr_oi_swap,
            on_prod_5yr_10yr_b_swap=on_prod_5yr_10yr_b_swap,
            on_prod_5yr_10yr_ff=on_prod_5yr_10yr_ff,
            on_prod_5yr_10yr_oi_swap=on_prod_5yr_10yr_oi_swap,
            on_prod_10yr_15yr_b_swap=on_prod_10yr_15yr_b_swap,
            on_prod_10yr_15yr_ff=on_prod_10yr_15yr_ff,
            on_prod_10yr_15yr_oi_swap=on_prod_10yr_15yr_oi_swap,
            on_prod_15yr_20yr_b_swap=on_prod_15yr_20yr_b_swap,
            on_prod_15yr_20yr_ff=on_prod_15yr_20yr_ff,
            on_prod_15yr_20yr_oi_swap=on_prod_15yr_20yr_oi_swap,
            on_prod_20yr_more_b_swap=on_prod_20yr_more_b_swap,
            on_prod_20yr_more_ff=on_prod_20yr_more_ff,
            on_prod_20yr_more_oi_swap=on_prod_20yr_more_oi_swap,
            not_total_asset_class=not_total_asset_class,
            not_prod_b_swap=not_prod_b_swap,
            not_prod_ff=not_prod_ff,
            not_prod_oi_swap=not_prod_oi_swap,
            not_prod_intend_clear_b_swap=not_prod_intend_clear_b_swap,
            not_prod_intend_clear_ff=not_prod_intend_clear_ff,
            not_prod_intend_clear_oi_swap=not_prod_intend_clear_oi_swap,
            not_prod_not_intend_clear_b_swap=not_prod_not_intend_clear_b_swap,
            not_prod_not_intend_clear_ff=not_prod_not_intend_clear_ff,
            not_prod_not_intend_clear_oi_swap=not_prod_not_intend_clear_oi_swap,
            not_prod_usd_b_swap=not_prod_usd_b_swap,
            not_prod_usd_ff=not_prod_usd_ff,
            not_prod_usd_oi_swap=not_prod_usd_oi_swap,
            not_prod_cny_b_swap=not_prod_cny_b_swap,
            not_prod_cny_ff=not_prod_cny_ff,
            not_prod_cny_oi_swap=not_prod_cny_oi_swap,
            not_prod_eur_b_swap=not_prod_eur_b_swap,
            not_prod_eur_ff=not_prod_eur_ff,
            not_prod_eur_oi_swap=not_prod_eur_oi_swap,
            not_prod_gbp_b_swap=not_prod_gbp_b_swap,
            not_prod_gbp_ff=not_prod_gbp_ff,
            not_prod_gbp_oi_swap=not_prod_gbp_oi_swap,
            not_prod_jpy_b_swap=not_prod_jpy_b_swap,
            not_prod_jpy_ff=not_prod_jpy_ff,
            not_prod_jpy_oi_swap=not_prod_jpy_oi_swap,
            not_prod_hkd_b_swap=not_prod_hkd_b_swap,
            not_prod_hkd_ff=not_prod_hkd_ff,
            not_prod_hkd_oi_swap=not_prod_hkd_oi_swap,
            not_prod_other_curr_b_swap=not_prod_other_curr_b_swap,
            not_prod_other_curr_ff=not_prod_other_curr_ff,
            not_prod_other_curr_oi_swap=not_prod_other_curr_oi_swap,
            not_prod_0yr_1yr_b_swap=not_prod_0yr_1yr_b_swap,
            not_prod_0yr_1yr_ff=not_prod_0yr_1yr_ff,
            not_prod_0yr_1yr_oi_swap=not_prod_0yr_1yr_oi_swap,
            not_prod_1yr_2yr_b_swap=not_prod_1yr_2yr_b_swap,
            not_prod_1yr_2yr_ff=not_prod_1yr_2yr_ff,
            not_prod_1yr_2yr_oi_swap=not_prod_1yr_2yr_oi_swap,
            not_prod_2yr_5yr_b_swap=not_prod_2yr_5yr_b_swap,
            not_prod_2yr_5yr_ff=not_prod_2yr_5yr_ff,
            not_prod_2yr_5yr_oi_swap=not_prod_2yr_5yr_oi_swap,
            not_prod_5yr_10yr_b_swap=not_prod_5yr_10yr_b_swap,
            not_prod_5yr_10yr_ff=not_prod_5yr_10yr_ff,
            not_prod_5yr_10yr_oi_swap=not_prod_5yr_10yr_oi_swap,
            not_prod_10yr_15yr_b_swap=not_prod_10yr_15yr_b_swap,
            not_prod_10yr_15yr_ff=not_prod_10yr_15yr_ff,
            not_prod_10yr_15yr_oi_swap=not_prod_10yr_15yr_oi_swap,
            not_prod_15yr_20yr_b_swap=not_prod_15yr_20yr_b_swap,
            not_prod_15yr_20yr_ff=not_prod_15yr_20yr_ff,
            not_prod_15yr_20yr_oi_swap=not_prod_15yr_20yr_oi_swap,
            not_prod_20yr_more_b_swap=not_prod_20yr_more_b_swap,
            not_prod_20yr_more_ff=not_prod_20yr_more_ff,
            not_prod_20yr_more_oi_swap=not_prod_20yr_more_oi_swap,
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
