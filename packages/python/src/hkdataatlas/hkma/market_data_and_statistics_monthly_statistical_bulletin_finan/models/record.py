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
        notes_coins_circulation (float | Unset):
        aggr_balance (float | Unset):
        ef_bills_notes (float | Unset):
        monetary_base_total (float | Unset):
        m1_total (float | Unset):
        m1_hkd (float | Unset):
        m2_total (float | Unset):
        m2_hkd (float | Unset):
        m3_total (float | Unset):
        m3_hkd (float | Unset):
        exrate_hkd_usd (float | Unset):
        nominal_eff_exrate_index (float | Unset):
        hibor_fixing_overnight (float | Unset):
        hibor_fixing_3m (float | Unset):
        deposit_rate_saving (float | Unset):
        deposit_rate_3m (float | Unset):
        yield_efpaper_3m (float | Unset):
        yield_govbond_10y (float | Unset):
        best_lending_rate (float | Unset):
        discount_window_base_rate (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    notes_coins_circulation: float | Unset = UNSET
    aggr_balance: float | Unset = UNSET
    ef_bills_notes: float | Unset = UNSET
    monetary_base_total: float | Unset = UNSET
    m1_total: float | Unset = UNSET
    m1_hkd: float | Unset = UNSET
    m2_total: float | Unset = UNSET
    m2_hkd: float | Unset = UNSET
    m3_total: float | Unset = UNSET
    m3_hkd: float | Unset = UNSET
    exrate_hkd_usd: float | Unset = UNSET
    nominal_eff_exrate_index: float | Unset = UNSET
    hibor_fixing_overnight: float | Unset = UNSET
    hibor_fixing_3m: float | Unset = UNSET
    deposit_rate_saving: float | Unset = UNSET
    deposit_rate_3m: float | Unset = UNSET
    yield_efpaper_3m: float | Unset = UNSET
    yield_govbond_10y: float | Unset = UNSET
    best_lending_rate: float | Unset = UNSET
    discount_window_base_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        notes_coins_circulation = self.notes_coins_circulation

        aggr_balance = self.aggr_balance

        ef_bills_notes = self.ef_bills_notes

        monetary_base_total = self.monetary_base_total

        m1_total = self.m1_total

        m1_hkd = self.m1_hkd

        m2_total = self.m2_total

        m2_hkd = self.m2_hkd

        m3_total = self.m3_total

        m3_hkd = self.m3_hkd

        exrate_hkd_usd = self.exrate_hkd_usd

        nominal_eff_exrate_index = self.nominal_eff_exrate_index

        hibor_fixing_overnight = self.hibor_fixing_overnight

        hibor_fixing_3m = self.hibor_fixing_3m

        deposit_rate_saving = self.deposit_rate_saving

        deposit_rate_3m = self.deposit_rate_3m

        yield_efpaper_3m = self.yield_efpaper_3m

        yield_govbond_10y = self.yield_govbond_10y

        best_lending_rate = self.best_lending_rate

        discount_window_base_rate = self.discount_window_base_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if notes_coins_circulation is not UNSET:
            field_dict["notes_coins_circulation"] = notes_coins_circulation
        if aggr_balance is not UNSET:
            field_dict["aggr_balance"] = aggr_balance
        if ef_bills_notes is not UNSET:
            field_dict["ef_bills_notes"] = ef_bills_notes
        if monetary_base_total is not UNSET:
            field_dict["monetary_base_total"] = monetary_base_total
        if m1_total is not UNSET:
            field_dict["m1_total"] = m1_total
        if m1_hkd is not UNSET:
            field_dict["m1_hkd"] = m1_hkd
        if m2_total is not UNSET:
            field_dict["m2_total"] = m2_total
        if m2_hkd is not UNSET:
            field_dict["m2_hkd"] = m2_hkd
        if m3_total is not UNSET:
            field_dict["m3_total"] = m3_total
        if m3_hkd is not UNSET:
            field_dict["m3_hkd"] = m3_hkd
        if exrate_hkd_usd is not UNSET:
            field_dict["exrate_hkd_usd"] = exrate_hkd_usd
        if nominal_eff_exrate_index is not UNSET:
            field_dict["nominal_eff_exrate_index"] = nominal_eff_exrate_index
        if hibor_fixing_overnight is not UNSET:
            field_dict["hibor_fixing_overnight"] = hibor_fixing_overnight
        if hibor_fixing_3m is not UNSET:
            field_dict["hibor_fixing_3m"] = hibor_fixing_3m
        if deposit_rate_saving is not UNSET:
            field_dict["deposit_rate_saving"] = deposit_rate_saving
        if deposit_rate_3m is not UNSET:
            field_dict["deposit_rate_3m"] = deposit_rate_3m
        if yield_efpaper_3m is not UNSET:
            field_dict["yield_efpaper_3m"] = yield_efpaper_3m
        if yield_govbond_10y is not UNSET:
            field_dict["yield_govbond_10y"] = yield_govbond_10y
        if best_lending_rate is not UNSET:
            field_dict["best_lending_rate"] = best_lending_rate
        if discount_window_base_rate is not UNSET:
            field_dict["discount_window_base_rate"] = discount_window_base_rate

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

        notes_coins_circulation = d.pop("notes_coins_circulation", UNSET)

        aggr_balance = d.pop("aggr_balance", UNSET)

        ef_bills_notes = d.pop("ef_bills_notes", UNSET)

        monetary_base_total = d.pop("monetary_base_total", UNSET)

        m1_total = d.pop("m1_total", UNSET)

        m1_hkd = d.pop("m1_hkd", UNSET)

        m2_total = d.pop("m2_total", UNSET)

        m2_hkd = d.pop("m2_hkd", UNSET)

        m3_total = d.pop("m3_total", UNSET)

        m3_hkd = d.pop("m3_hkd", UNSET)

        exrate_hkd_usd = d.pop("exrate_hkd_usd", UNSET)

        nominal_eff_exrate_index = d.pop("nominal_eff_exrate_index", UNSET)

        hibor_fixing_overnight = d.pop("hibor_fixing_overnight", UNSET)

        hibor_fixing_3m = d.pop("hibor_fixing_3m", UNSET)

        deposit_rate_saving = d.pop("deposit_rate_saving", UNSET)

        deposit_rate_3m = d.pop("deposit_rate_3m", UNSET)

        yield_efpaper_3m = d.pop("yield_efpaper_3m", UNSET)

        yield_govbond_10y = d.pop("yield_govbond_10y", UNSET)

        best_lending_rate = d.pop("best_lending_rate", UNSET)

        discount_window_base_rate = d.pop("discount_window_base_rate", UNSET)

        record = cls(
            end_of_month=end_of_month,
            notes_coins_circulation=notes_coins_circulation,
            aggr_balance=aggr_balance,
            ef_bills_notes=ef_bills_notes,
            monetary_base_total=monetary_base_total,
            m1_total=m1_total,
            m1_hkd=m1_hkd,
            m2_total=m2_total,
            m2_hkd=m2_hkd,
            m3_total=m3_total,
            m3_hkd=m3_hkd,
            exrate_hkd_usd=exrate_hkd_usd,
            nominal_eff_exrate_index=nominal_eff_exrate_index,
            hibor_fixing_overnight=hibor_fixing_overnight,
            hibor_fixing_3m=hibor_fixing_3m,
            deposit_rate_saving=deposit_rate_saving,
            deposit_rate_3m=deposit_rate_3m,
            yield_efpaper_3m=yield_efpaper_3m,
            yield_govbond_10y=yield_govbond_10y,
            best_lending_rate=best_lending_rate,
            discount_window_base_rate=discount_window_base_rate,
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
