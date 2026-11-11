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
        cert_of_indebt (float | Unset):
        gov_notes_coins_circulation (float | Unset):
        aggr_balance_bf_disc_win (float | Unset):
        outstanding_efbn (float | Unset):
        ow_lb_bf_disc_win (float | Unset):
        mb_bf_disc_win_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    cert_of_indebt: float | Unset = UNSET
    gov_notes_coins_circulation: float | Unset = UNSET
    aggr_balance_bf_disc_win: float | Unset = UNSET
    outstanding_efbn: float | Unset = UNSET
    ow_lb_bf_disc_win: float | Unset = UNSET
    mb_bf_disc_win_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        cert_of_indebt = self.cert_of_indebt

        gov_notes_coins_circulation = self.gov_notes_coins_circulation

        aggr_balance_bf_disc_win = self.aggr_balance_bf_disc_win

        outstanding_efbn = self.outstanding_efbn

        ow_lb_bf_disc_win = self.ow_lb_bf_disc_win

        mb_bf_disc_win_total = self.mb_bf_disc_win_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if cert_of_indebt is not UNSET:
            field_dict["cert_of_indebt"] = cert_of_indebt
        if gov_notes_coins_circulation is not UNSET:
            field_dict["gov_notes_coins_circulation"] = gov_notes_coins_circulation
        if aggr_balance_bf_disc_win is not UNSET:
            field_dict["aggr_balance_bf_disc_win"] = aggr_balance_bf_disc_win
        if outstanding_efbn is not UNSET:
            field_dict["outstanding_efbn"] = outstanding_efbn
        if ow_lb_bf_disc_win is not UNSET:
            field_dict["ow_lb_bf_disc_win"] = ow_lb_bf_disc_win
        if mb_bf_disc_win_total is not UNSET:
            field_dict["mb_bf_disc_win_total"] = mb_bf_disc_win_total

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

        cert_of_indebt = d.pop("cert_of_indebt", UNSET)

        gov_notes_coins_circulation = d.pop("gov_notes_coins_circulation", UNSET)

        aggr_balance_bf_disc_win = d.pop("aggr_balance_bf_disc_win", UNSET)

        outstanding_efbn = d.pop("outstanding_efbn", UNSET)

        ow_lb_bf_disc_win = d.pop("ow_lb_bf_disc_win", UNSET)

        mb_bf_disc_win_total = d.pop("mb_bf_disc_win_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            cert_of_indebt=cert_of_indebt,
            gov_notes_coins_circulation=gov_notes_coins_circulation,
            aggr_balance_bf_disc_win=aggr_balance_bf_disc_win,
            outstanding_efbn=outstanding_efbn,
            ow_lb_bf_disc_win=ow_lb_bf_disc_win,
            mb_bf_disc_win_total=mb_bf_disc_win_total,
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
