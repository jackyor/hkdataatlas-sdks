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
        on_prod_non_deliver_fw (float | Unset):
        on_prod_intend_clear_non_deliver_fw (float | Unset):
        on_prod_not_intend_clear_non_deliver_fw (float | Unset):
        on_prod_usd_cny_non_deliver_fw (float | Unset):
        on_prod_usd_idr_non_deliver_fw (float | Unset):
        on_prod_usd_inr_non_deliver_fw (float | Unset):
        on_prod_usd_krw_non_deliver_fw (float | Unset):
        on_prod_usd_myr_non_deliver_fw (float | Unset):
        on_prod_usd_php_non_deliver_fw (float | Unset):
        on_prod_usd_twd_non_deliver_fw (float | Unset):
        on_prod_other_curr_non_deliver_fw (float | Unset):
        on_prod_0m_3m_non_deliver_fw (float | Unset):
        on_prod_3m_6m_non_deliver_fw (float | Unset):
        on_prod_6m_9m_non_deliver_fw (float | Unset):
        on_prod_9m_12m_non_deliver_fw (float | Unset):
        on_prod_1y_2y_non_deliver_fw (float | Unset):
        on_prod_2y_5y_non_deliver_fw (float | Unset):
        on_prod_5y_more_non_deliver_fw (float | Unset):
        not_total_asset_class (float | Unset):
        not_prod_non_deliver_fw (float | Unset):
        not_prod_intent_clear_non_deliver_fw (float | Unset):
        not_prod_not_intent_clear_non_deliver_fw (float | Unset):
        not_prod_usd_cny_non_deliver_fw (float | Unset):
        not_prod_usd_idr_non_deliver_fw (float | Unset):
        not_prod_usd_inr_non_deliver_fw (float | Unset):
        not_prod_usd_krw_non_deliver_fw (float | Unset):
        not_prod_usd_myr_non_deliver_fw (float | Unset):
        not_prod_usd_php_non_deliver_fw (float | Unset):
        not_prod_usd_twd_non_deliver_fw (float | Unset):
        not_prod_other_curr_non_deliver_fw (float | Unset):
        not_prod_0m_3m_non_deliver_fw (float | Unset):
        not_prod_3m_6m_non_deliver_fw (float | Unset):
        not_prod_6m_9m_non_deliver_fw (float | Unset):
        not_prod_9m_12m_non_deliver_fw (float | Unset):
        not_prod_1y_2y_non_deliver_fw (float | Unset):
        not_prod_2y_5y_non_deliver_fw (float | Unset):
        not_prod_5y_more_non_deliver_fw (float | Unset):
    """

    end_of_date: datetime.date | Unset = UNSET
    on_total_asset_class: float | Unset = UNSET
    on_prod_non_deliver_fw: float | Unset = UNSET
    on_prod_intend_clear_non_deliver_fw: float | Unset = UNSET
    on_prod_not_intend_clear_non_deliver_fw: float | Unset = UNSET
    on_prod_usd_cny_non_deliver_fw: float | Unset = UNSET
    on_prod_usd_idr_non_deliver_fw: float | Unset = UNSET
    on_prod_usd_inr_non_deliver_fw: float | Unset = UNSET
    on_prod_usd_krw_non_deliver_fw: float | Unset = UNSET
    on_prod_usd_myr_non_deliver_fw: float | Unset = UNSET
    on_prod_usd_php_non_deliver_fw: float | Unset = UNSET
    on_prod_usd_twd_non_deliver_fw: float | Unset = UNSET
    on_prod_other_curr_non_deliver_fw: float | Unset = UNSET
    on_prod_0m_3m_non_deliver_fw: float | Unset = UNSET
    on_prod_3m_6m_non_deliver_fw: float | Unset = UNSET
    on_prod_6m_9m_non_deliver_fw: float | Unset = UNSET
    on_prod_9m_12m_non_deliver_fw: float | Unset = UNSET
    on_prod_1y_2y_non_deliver_fw: float | Unset = UNSET
    on_prod_2y_5y_non_deliver_fw: float | Unset = UNSET
    on_prod_5y_more_non_deliver_fw: float | Unset = UNSET
    not_total_asset_class: float | Unset = UNSET
    not_prod_non_deliver_fw: float | Unset = UNSET
    not_prod_intent_clear_non_deliver_fw: float | Unset = UNSET
    not_prod_not_intent_clear_non_deliver_fw: float | Unset = UNSET
    not_prod_usd_cny_non_deliver_fw: float | Unset = UNSET
    not_prod_usd_idr_non_deliver_fw: float | Unset = UNSET
    not_prod_usd_inr_non_deliver_fw: float | Unset = UNSET
    not_prod_usd_krw_non_deliver_fw: float | Unset = UNSET
    not_prod_usd_myr_non_deliver_fw: float | Unset = UNSET
    not_prod_usd_php_non_deliver_fw: float | Unset = UNSET
    not_prod_usd_twd_non_deliver_fw: float | Unset = UNSET
    not_prod_other_curr_non_deliver_fw: float | Unset = UNSET
    not_prod_0m_3m_non_deliver_fw: float | Unset = UNSET
    not_prod_3m_6m_non_deliver_fw: float | Unset = UNSET
    not_prod_6m_9m_non_deliver_fw: float | Unset = UNSET
    not_prod_9m_12m_non_deliver_fw: float | Unset = UNSET
    not_prod_1y_2y_non_deliver_fw: float | Unset = UNSET
    not_prod_2y_5y_non_deliver_fw: float | Unset = UNSET
    not_prod_5y_more_non_deliver_fw: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_date: str | Unset = UNSET
        if not isinstance(self.end_of_date, Unset):
            end_of_date = self.end_of_date.isoformat()

        on_total_asset_class = self.on_total_asset_class

        on_prod_non_deliver_fw = self.on_prod_non_deliver_fw

        on_prod_intend_clear_non_deliver_fw = self.on_prod_intend_clear_non_deliver_fw

        on_prod_not_intend_clear_non_deliver_fw = (
            self.on_prod_not_intend_clear_non_deliver_fw
        )

        on_prod_usd_cny_non_deliver_fw = self.on_prod_usd_cny_non_deliver_fw

        on_prod_usd_idr_non_deliver_fw = self.on_prod_usd_idr_non_deliver_fw

        on_prod_usd_inr_non_deliver_fw = self.on_prod_usd_inr_non_deliver_fw

        on_prod_usd_krw_non_deliver_fw = self.on_prod_usd_krw_non_deliver_fw

        on_prod_usd_myr_non_deliver_fw = self.on_prod_usd_myr_non_deliver_fw

        on_prod_usd_php_non_deliver_fw = self.on_prod_usd_php_non_deliver_fw

        on_prod_usd_twd_non_deliver_fw = self.on_prod_usd_twd_non_deliver_fw

        on_prod_other_curr_non_deliver_fw = self.on_prod_other_curr_non_deliver_fw

        on_prod_0m_3m_non_deliver_fw = self.on_prod_0m_3m_non_deliver_fw

        on_prod_3m_6m_non_deliver_fw = self.on_prod_3m_6m_non_deliver_fw

        on_prod_6m_9m_non_deliver_fw = self.on_prod_6m_9m_non_deliver_fw

        on_prod_9m_12m_non_deliver_fw = self.on_prod_9m_12m_non_deliver_fw

        on_prod_1y_2y_non_deliver_fw = self.on_prod_1y_2y_non_deliver_fw

        on_prod_2y_5y_non_deliver_fw = self.on_prod_2y_5y_non_deliver_fw

        on_prod_5y_more_non_deliver_fw = self.on_prod_5y_more_non_deliver_fw

        not_total_asset_class = self.not_total_asset_class

        not_prod_non_deliver_fw = self.not_prod_non_deliver_fw

        not_prod_intent_clear_non_deliver_fw = self.not_prod_intent_clear_non_deliver_fw

        not_prod_not_intent_clear_non_deliver_fw = (
            self.not_prod_not_intent_clear_non_deliver_fw
        )

        not_prod_usd_cny_non_deliver_fw = self.not_prod_usd_cny_non_deliver_fw

        not_prod_usd_idr_non_deliver_fw = self.not_prod_usd_idr_non_deliver_fw

        not_prod_usd_inr_non_deliver_fw = self.not_prod_usd_inr_non_deliver_fw

        not_prod_usd_krw_non_deliver_fw = self.not_prod_usd_krw_non_deliver_fw

        not_prod_usd_myr_non_deliver_fw = self.not_prod_usd_myr_non_deliver_fw

        not_prod_usd_php_non_deliver_fw = self.not_prod_usd_php_non_deliver_fw

        not_prod_usd_twd_non_deliver_fw = self.not_prod_usd_twd_non_deliver_fw

        not_prod_other_curr_non_deliver_fw = self.not_prod_other_curr_non_deliver_fw

        not_prod_0m_3m_non_deliver_fw = self.not_prod_0m_3m_non_deliver_fw

        not_prod_3m_6m_non_deliver_fw = self.not_prod_3m_6m_non_deliver_fw

        not_prod_6m_9m_non_deliver_fw = self.not_prod_6m_9m_non_deliver_fw

        not_prod_9m_12m_non_deliver_fw = self.not_prod_9m_12m_non_deliver_fw

        not_prod_1y_2y_non_deliver_fw = self.not_prod_1y_2y_non_deliver_fw

        not_prod_2y_5y_non_deliver_fw = self.not_prod_2y_5y_non_deliver_fw

        not_prod_5y_more_non_deliver_fw = self.not_prod_5y_more_non_deliver_fw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_date is not UNSET:
            field_dict["end_of_date"] = end_of_date
        if on_total_asset_class is not UNSET:
            field_dict["on_total_asset_class"] = on_total_asset_class
        if on_prod_non_deliver_fw is not UNSET:
            field_dict["on_prod_non_deliver_fw"] = on_prod_non_deliver_fw
        if on_prod_intend_clear_non_deliver_fw is not UNSET:
            field_dict["on_prod_intend_clear_non_deliver_fw"] = (
                on_prod_intend_clear_non_deliver_fw
            )
        if on_prod_not_intend_clear_non_deliver_fw is not UNSET:
            field_dict["on_prod_not_intend_clear_non_deliver_fw"] = (
                on_prod_not_intend_clear_non_deliver_fw
            )
        if on_prod_usd_cny_non_deliver_fw is not UNSET:
            field_dict["on_prod_usd_cny_non_deliver_fw"] = (
                on_prod_usd_cny_non_deliver_fw
            )
        if on_prod_usd_idr_non_deliver_fw is not UNSET:
            field_dict["on_prod_usd_idr_non_deliver_fw"] = (
                on_prod_usd_idr_non_deliver_fw
            )
        if on_prod_usd_inr_non_deliver_fw is not UNSET:
            field_dict["on_prod_usd_inr_non_deliver_fw"] = (
                on_prod_usd_inr_non_deliver_fw
            )
        if on_prod_usd_krw_non_deliver_fw is not UNSET:
            field_dict["on_prod_usd_krw_non_deliver_fw"] = (
                on_prod_usd_krw_non_deliver_fw
            )
        if on_prod_usd_myr_non_deliver_fw is not UNSET:
            field_dict["on_prod_usd_myr_non_deliver_fw"] = (
                on_prod_usd_myr_non_deliver_fw
            )
        if on_prod_usd_php_non_deliver_fw is not UNSET:
            field_dict["on_prod_usd_php_non_deliver_fw"] = (
                on_prod_usd_php_non_deliver_fw
            )
        if on_prod_usd_twd_non_deliver_fw is not UNSET:
            field_dict["on_prod_usd_twd_non_deliver_fw"] = (
                on_prod_usd_twd_non_deliver_fw
            )
        if on_prod_other_curr_non_deliver_fw is not UNSET:
            field_dict["on_prod_other_curr_non_deliver_fw"] = (
                on_prod_other_curr_non_deliver_fw
            )
        if on_prod_0m_3m_non_deliver_fw is not UNSET:
            field_dict["on_prod_0m_3m_non_deliver_fw"] = on_prod_0m_3m_non_deliver_fw
        if on_prod_3m_6m_non_deliver_fw is not UNSET:
            field_dict["on_prod_3m_6m_non_deliver_fw"] = on_prod_3m_6m_non_deliver_fw
        if on_prod_6m_9m_non_deliver_fw is not UNSET:
            field_dict["on_prod_6m_9m_non_deliver_fw"] = on_prod_6m_9m_non_deliver_fw
        if on_prod_9m_12m_non_deliver_fw is not UNSET:
            field_dict["on_prod_9m_12m_non_deliver_fw"] = on_prod_9m_12m_non_deliver_fw
        if on_prod_1y_2y_non_deliver_fw is not UNSET:
            field_dict["on_prod_1y_2y_non_deliver_fw"] = on_prod_1y_2y_non_deliver_fw
        if on_prod_2y_5y_non_deliver_fw is not UNSET:
            field_dict["on_prod_2y_5y_non_deliver_fw"] = on_prod_2y_5y_non_deliver_fw
        if on_prod_5y_more_non_deliver_fw is not UNSET:
            field_dict["on_prod_5y_more_non_deliver_fw"] = (
                on_prod_5y_more_non_deliver_fw
            )
        if not_total_asset_class is not UNSET:
            field_dict["not_total_asset_class"] = not_total_asset_class
        if not_prod_non_deliver_fw is not UNSET:
            field_dict["not_prod_non_deliver_fw"] = not_prod_non_deliver_fw
        if not_prod_intent_clear_non_deliver_fw is not UNSET:
            field_dict["not_prod_intent_clear_non_deliver_fw"] = (
                not_prod_intent_clear_non_deliver_fw
            )
        if not_prod_not_intent_clear_non_deliver_fw is not UNSET:
            field_dict["not_prod_not_intent_clear_non_deliver_fw"] = (
                not_prod_not_intent_clear_non_deliver_fw
            )
        if not_prod_usd_cny_non_deliver_fw is not UNSET:
            field_dict["not_prod_usd_cny_non_deliver_fw"] = (
                not_prod_usd_cny_non_deliver_fw
            )
        if not_prod_usd_idr_non_deliver_fw is not UNSET:
            field_dict["not_prod_usd_idr_non_deliver_fw"] = (
                not_prod_usd_idr_non_deliver_fw
            )
        if not_prod_usd_inr_non_deliver_fw is not UNSET:
            field_dict["not_prod_usd_inr_non_deliver_fw"] = (
                not_prod_usd_inr_non_deliver_fw
            )
        if not_prod_usd_krw_non_deliver_fw is not UNSET:
            field_dict["not_prod_usd_krw_non_deliver_fw"] = (
                not_prod_usd_krw_non_deliver_fw
            )
        if not_prod_usd_myr_non_deliver_fw is not UNSET:
            field_dict["not_prod_usd_myr_non_deliver_fw"] = (
                not_prod_usd_myr_non_deliver_fw
            )
        if not_prod_usd_php_non_deliver_fw is not UNSET:
            field_dict["not_prod_usd_php_non_deliver_fw"] = (
                not_prod_usd_php_non_deliver_fw
            )
        if not_prod_usd_twd_non_deliver_fw is not UNSET:
            field_dict["not_prod_usd_twd_non_deliver_fw"] = (
                not_prod_usd_twd_non_deliver_fw
            )
        if not_prod_other_curr_non_deliver_fw is not UNSET:
            field_dict["not_prod_other_curr_non_deliver_fw"] = (
                not_prod_other_curr_non_deliver_fw
            )
        if not_prod_0m_3m_non_deliver_fw is not UNSET:
            field_dict["not_prod_0m_3m_non_deliver_fw"] = not_prod_0m_3m_non_deliver_fw
        if not_prod_3m_6m_non_deliver_fw is not UNSET:
            field_dict["not_prod_3m_6m_non_deliver_fw"] = not_prod_3m_6m_non_deliver_fw
        if not_prod_6m_9m_non_deliver_fw is not UNSET:
            field_dict["not_prod_6m_9m_non_deliver_fw"] = not_prod_6m_9m_non_deliver_fw
        if not_prod_9m_12m_non_deliver_fw is not UNSET:
            field_dict["not_prod_9m_12m_non_deliver_fw"] = (
                not_prod_9m_12m_non_deliver_fw
            )
        if not_prod_1y_2y_non_deliver_fw is not UNSET:
            field_dict["not_prod_1y_2y_non_deliver_fw"] = not_prod_1y_2y_non_deliver_fw
        if not_prod_2y_5y_non_deliver_fw is not UNSET:
            field_dict["not_prod_2y_5y_non_deliver_fw"] = not_prod_2y_5y_non_deliver_fw
        if not_prod_5y_more_non_deliver_fw is not UNSET:
            field_dict["not_prod_5y_more_non_deliver_fw"] = (
                not_prod_5y_more_non_deliver_fw
            )

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

        on_prod_non_deliver_fw = d.pop("on_prod_non_deliver_fw", UNSET)

        on_prod_intend_clear_non_deliver_fw = d.pop(
            "on_prod_intend_clear_non_deliver_fw", UNSET
        )

        on_prod_not_intend_clear_non_deliver_fw = d.pop(
            "on_prod_not_intend_clear_non_deliver_fw", UNSET
        )

        on_prod_usd_cny_non_deliver_fw = d.pop("on_prod_usd_cny_non_deliver_fw", UNSET)

        on_prod_usd_idr_non_deliver_fw = d.pop("on_prod_usd_idr_non_deliver_fw", UNSET)

        on_prod_usd_inr_non_deliver_fw = d.pop("on_prod_usd_inr_non_deliver_fw", UNSET)

        on_prod_usd_krw_non_deliver_fw = d.pop("on_prod_usd_krw_non_deliver_fw", UNSET)

        on_prod_usd_myr_non_deliver_fw = d.pop("on_prod_usd_myr_non_deliver_fw", UNSET)

        on_prod_usd_php_non_deliver_fw = d.pop("on_prod_usd_php_non_deliver_fw", UNSET)

        on_prod_usd_twd_non_deliver_fw = d.pop("on_prod_usd_twd_non_deliver_fw", UNSET)

        on_prod_other_curr_non_deliver_fw = d.pop(
            "on_prod_other_curr_non_deliver_fw", UNSET
        )

        on_prod_0m_3m_non_deliver_fw = d.pop("on_prod_0m_3m_non_deliver_fw", UNSET)

        on_prod_3m_6m_non_deliver_fw = d.pop("on_prod_3m_6m_non_deliver_fw", UNSET)

        on_prod_6m_9m_non_deliver_fw = d.pop("on_prod_6m_9m_non_deliver_fw", UNSET)

        on_prod_9m_12m_non_deliver_fw = d.pop("on_prod_9m_12m_non_deliver_fw", UNSET)

        on_prod_1y_2y_non_deliver_fw = d.pop("on_prod_1y_2y_non_deliver_fw", UNSET)

        on_prod_2y_5y_non_deliver_fw = d.pop("on_prod_2y_5y_non_deliver_fw", UNSET)

        on_prod_5y_more_non_deliver_fw = d.pop("on_prod_5y_more_non_deliver_fw", UNSET)

        not_total_asset_class = d.pop("not_total_asset_class", UNSET)

        not_prod_non_deliver_fw = d.pop("not_prod_non_deliver_fw", UNSET)

        not_prod_intent_clear_non_deliver_fw = d.pop(
            "not_prod_intent_clear_non_deliver_fw", UNSET
        )

        not_prod_not_intent_clear_non_deliver_fw = d.pop(
            "not_prod_not_intent_clear_non_deliver_fw", UNSET
        )

        not_prod_usd_cny_non_deliver_fw = d.pop(
            "not_prod_usd_cny_non_deliver_fw", UNSET
        )

        not_prod_usd_idr_non_deliver_fw = d.pop(
            "not_prod_usd_idr_non_deliver_fw", UNSET
        )

        not_prod_usd_inr_non_deliver_fw = d.pop(
            "not_prod_usd_inr_non_deliver_fw", UNSET
        )

        not_prod_usd_krw_non_deliver_fw = d.pop(
            "not_prod_usd_krw_non_deliver_fw", UNSET
        )

        not_prod_usd_myr_non_deliver_fw = d.pop(
            "not_prod_usd_myr_non_deliver_fw", UNSET
        )

        not_prod_usd_php_non_deliver_fw = d.pop(
            "not_prod_usd_php_non_deliver_fw", UNSET
        )

        not_prod_usd_twd_non_deliver_fw = d.pop(
            "not_prod_usd_twd_non_deliver_fw", UNSET
        )

        not_prod_other_curr_non_deliver_fw = d.pop(
            "not_prod_other_curr_non_deliver_fw", UNSET
        )

        not_prod_0m_3m_non_deliver_fw = d.pop("not_prod_0m_3m_non_deliver_fw", UNSET)

        not_prod_3m_6m_non_deliver_fw = d.pop("not_prod_3m_6m_non_deliver_fw", UNSET)

        not_prod_6m_9m_non_deliver_fw = d.pop("not_prod_6m_9m_non_deliver_fw", UNSET)

        not_prod_9m_12m_non_deliver_fw = d.pop("not_prod_9m_12m_non_deliver_fw", UNSET)

        not_prod_1y_2y_non_deliver_fw = d.pop("not_prod_1y_2y_non_deliver_fw", UNSET)

        not_prod_2y_5y_non_deliver_fw = d.pop("not_prod_2y_5y_non_deliver_fw", UNSET)

        not_prod_5y_more_non_deliver_fw = d.pop(
            "not_prod_5y_more_non_deliver_fw", UNSET
        )

        record = cls(
            end_of_date=end_of_date,
            on_total_asset_class=on_total_asset_class,
            on_prod_non_deliver_fw=on_prod_non_deliver_fw,
            on_prod_intend_clear_non_deliver_fw=on_prod_intend_clear_non_deliver_fw,
            on_prod_not_intend_clear_non_deliver_fw=on_prod_not_intend_clear_non_deliver_fw,
            on_prod_usd_cny_non_deliver_fw=on_prod_usd_cny_non_deliver_fw,
            on_prod_usd_idr_non_deliver_fw=on_prod_usd_idr_non_deliver_fw,
            on_prod_usd_inr_non_deliver_fw=on_prod_usd_inr_non_deliver_fw,
            on_prod_usd_krw_non_deliver_fw=on_prod_usd_krw_non_deliver_fw,
            on_prod_usd_myr_non_deliver_fw=on_prod_usd_myr_non_deliver_fw,
            on_prod_usd_php_non_deliver_fw=on_prod_usd_php_non_deliver_fw,
            on_prod_usd_twd_non_deliver_fw=on_prod_usd_twd_non_deliver_fw,
            on_prod_other_curr_non_deliver_fw=on_prod_other_curr_non_deliver_fw,
            on_prod_0m_3m_non_deliver_fw=on_prod_0m_3m_non_deliver_fw,
            on_prod_3m_6m_non_deliver_fw=on_prod_3m_6m_non_deliver_fw,
            on_prod_6m_9m_non_deliver_fw=on_prod_6m_9m_non_deliver_fw,
            on_prod_9m_12m_non_deliver_fw=on_prod_9m_12m_non_deliver_fw,
            on_prod_1y_2y_non_deliver_fw=on_prod_1y_2y_non_deliver_fw,
            on_prod_2y_5y_non_deliver_fw=on_prod_2y_5y_non_deliver_fw,
            on_prod_5y_more_non_deliver_fw=on_prod_5y_more_non_deliver_fw,
            not_total_asset_class=not_total_asset_class,
            not_prod_non_deliver_fw=not_prod_non_deliver_fw,
            not_prod_intent_clear_non_deliver_fw=not_prod_intent_clear_non_deliver_fw,
            not_prod_not_intent_clear_non_deliver_fw=not_prod_not_intent_clear_non_deliver_fw,
            not_prod_usd_cny_non_deliver_fw=not_prod_usd_cny_non_deliver_fw,
            not_prod_usd_idr_non_deliver_fw=not_prod_usd_idr_non_deliver_fw,
            not_prod_usd_inr_non_deliver_fw=not_prod_usd_inr_non_deliver_fw,
            not_prod_usd_krw_non_deliver_fw=not_prod_usd_krw_non_deliver_fw,
            not_prod_usd_myr_non_deliver_fw=not_prod_usd_myr_non_deliver_fw,
            not_prod_usd_php_non_deliver_fw=not_prod_usd_php_non_deliver_fw,
            not_prod_usd_twd_non_deliver_fw=not_prod_usd_twd_non_deliver_fw,
            not_prod_other_curr_non_deliver_fw=not_prod_other_curr_non_deliver_fw,
            not_prod_0m_3m_non_deliver_fw=not_prod_0m_3m_non_deliver_fw,
            not_prod_3m_6m_non_deliver_fw=not_prod_3m_6m_non_deliver_fw,
            not_prod_6m_9m_non_deliver_fw=not_prod_6m_9m_non_deliver_fw,
            not_prod_9m_12m_non_deliver_fw=not_prod_9m_12m_non_deliver_fw,
            not_prod_1y_2y_non_deliver_fw=not_prod_1y_2y_non_deliver_fw,
            not_prod_2y_5y_non_deliver_fw=not_prod_2y_5y_non_deliver_fw,
            not_prod_5y_more_non_deliver_fw=not_prod_5y_more_non_deliver_fw,
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
