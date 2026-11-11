from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        end_of_month (str | Unset): Reportingperiod is returned asYYYY-MM; preserve plainstrings including full dates
            without inventing aday or pattern.
        hkd_drmkt_outstand_efbn (float | Unset):
        hkd_drmkt_outstand_odrinst (float | None | Unset): Retained officialresponses use null when this statistical
            value is unavailable.
        hkd_drmkt_outstand_total (float | None | Unset): Retained officialresponses use null when this statistical value
            is unavailable.
        hkd_drmkt_new_non_efbn (float | None | Unset): Retained officialresponses use null when this statistical value
            is unavailable.
        eq_mkt_hs_index (float | Unset):
        eq_mkt_ttl_stock_cap (float | Unset):
        eq_mkt_fund_raised (float | Unset):
    """

    end_of_month: str | Unset = UNSET
    hkd_drmkt_outstand_efbn: float | Unset = UNSET
    hkd_drmkt_outstand_odrinst: float | None | Unset = UNSET
    hkd_drmkt_outstand_total: float | None | Unset = UNSET
    hkd_drmkt_new_non_efbn: float | None | Unset = UNSET
    eq_mkt_hs_index: float | Unset = UNSET
    eq_mkt_ttl_stock_cap: float | Unset = UNSET
    eq_mkt_fund_raised: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month = self.end_of_month

        hkd_drmkt_outstand_efbn = self.hkd_drmkt_outstand_efbn

        hkd_drmkt_outstand_odrinst: float | None | Unset
        if isinstance(self.hkd_drmkt_outstand_odrinst, Unset):
            hkd_drmkt_outstand_odrinst = UNSET
        else:
            hkd_drmkt_outstand_odrinst = self.hkd_drmkt_outstand_odrinst

        hkd_drmkt_outstand_total: float | None | Unset
        if isinstance(self.hkd_drmkt_outstand_total, Unset):
            hkd_drmkt_outstand_total = UNSET
        else:
            hkd_drmkt_outstand_total = self.hkd_drmkt_outstand_total

        hkd_drmkt_new_non_efbn: float | None | Unset
        if isinstance(self.hkd_drmkt_new_non_efbn, Unset):
            hkd_drmkt_new_non_efbn = UNSET
        else:
            hkd_drmkt_new_non_efbn = self.hkd_drmkt_new_non_efbn

        eq_mkt_hs_index = self.eq_mkt_hs_index

        eq_mkt_ttl_stock_cap = self.eq_mkt_ttl_stock_cap

        eq_mkt_fund_raised = self.eq_mkt_fund_raised

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if hkd_drmkt_outstand_efbn is not UNSET:
            field_dict["hkd_drmkt_outstand_efbn"] = hkd_drmkt_outstand_efbn
        if hkd_drmkt_outstand_odrinst is not UNSET:
            field_dict["hkd_drmkt_outstand_odrinst"] = hkd_drmkt_outstand_odrinst
        if hkd_drmkt_outstand_total is not UNSET:
            field_dict["hkd_drmkt_outstand_total"] = hkd_drmkt_outstand_total
        if hkd_drmkt_new_non_efbn is not UNSET:
            field_dict["hkd_drmkt_new_non_efbn"] = hkd_drmkt_new_non_efbn
        if eq_mkt_hs_index is not UNSET:
            field_dict["eq_mkt_hs_index"] = eq_mkt_hs_index
        if eq_mkt_ttl_stock_cap is not UNSET:
            field_dict["eq_mkt_ttl_stock_cap"] = eq_mkt_ttl_stock_cap
        if eq_mkt_fund_raised is not UNSET:
            field_dict["eq_mkt_fund_raised"] = eq_mkt_fund_raised

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        end_of_month = d.pop("end_of_month", UNSET)

        hkd_drmkt_outstand_efbn = d.pop("hkd_drmkt_outstand_efbn", UNSET)

        def _parse_hkd_drmkt_outstand_odrinst(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hkd_drmkt_outstand_odrinst = _parse_hkd_drmkt_outstand_odrinst(
            d.pop("hkd_drmkt_outstand_odrinst", UNSET)
        )

        def _parse_hkd_drmkt_outstand_total(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hkd_drmkt_outstand_total = _parse_hkd_drmkt_outstand_total(
            d.pop("hkd_drmkt_outstand_total", UNSET)
        )

        def _parse_hkd_drmkt_new_non_efbn(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hkd_drmkt_new_non_efbn = _parse_hkd_drmkt_new_non_efbn(
            d.pop("hkd_drmkt_new_non_efbn", UNSET)
        )

        eq_mkt_hs_index = d.pop("eq_mkt_hs_index", UNSET)

        eq_mkt_ttl_stock_cap = d.pop("eq_mkt_ttl_stock_cap", UNSET)

        eq_mkt_fund_raised = d.pop("eq_mkt_fund_raised", UNSET)

        record = cls(
            end_of_month=end_of_month,
            hkd_drmkt_outstand_efbn=hkd_drmkt_outstand_efbn,
            hkd_drmkt_outstand_odrinst=hkd_drmkt_outstand_odrinst,
            hkd_drmkt_outstand_total=hkd_drmkt_outstand_total,
            hkd_drmkt_new_non_efbn=hkd_drmkt_new_non_efbn,
            eq_mkt_hs_index=eq_mkt_hs_index,
            eq_mkt_ttl_stock_cap=eq_mkt_ttl_stock_cap,
            eq_mkt_fund_raised=eq_mkt_fund_raised,
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
