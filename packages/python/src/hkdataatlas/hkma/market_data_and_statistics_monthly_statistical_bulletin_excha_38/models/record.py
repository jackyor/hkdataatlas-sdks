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
        fc_ra_exchange_fund (float | Unset):
        fc_ra_land_fund (float | Unset):
        fc_ra_total (float | Unset):
        fc_ra_per_capita (float | Unset):
        fc_ra_months_retained_imports_goods (float | Unset):
        ratio_fc_ra_to_cic (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    fc_ra_exchange_fund: float | Unset = UNSET
    fc_ra_land_fund: float | Unset = UNSET
    fc_ra_total: float | Unset = UNSET
    fc_ra_per_capita: float | Unset = UNSET
    fc_ra_months_retained_imports_goods: float | Unset = UNSET
    ratio_fc_ra_to_cic: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        fc_ra_exchange_fund = self.fc_ra_exchange_fund

        fc_ra_land_fund = self.fc_ra_land_fund

        fc_ra_total = self.fc_ra_total

        fc_ra_per_capita = self.fc_ra_per_capita

        fc_ra_months_retained_imports_goods = self.fc_ra_months_retained_imports_goods

        ratio_fc_ra_to_cic = self.ratio_fc_ra_to_cic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if fc_ra_exchange_fund is not UNSET:
            field_dict["fc_ra_exchange_fund"] = fc_ra_exchange_fund
        if fc_ra_land_fund is not UNSET:
            field_dict["fc_ra_land_fund"] = fc_ra_land_fund
        if fc_ra_total is not UNSET:
            field_dict["fc_ra_total"] = fc_ra_total
        if fc_ra_per_capita is not UNSET:
            field_dict["fc_ra_per_capita"] = fc_ra_per_capita
        if fc_ra_months_retained_imports_goods is not UNSET:
            field_dict["fc_ra_months_retained_imports_goods"] = (
                fc_ra_months_retained_imports_goods
            )
        if ratio_fc_ra_to_cic is not UNSET:
            field_dict["ratio_fc_ra_to_cic"] = ratio_fc_ra_to_cic

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

        fc_ra_exchange_fund = d.pop("fc_ra_exchange_fund", UNSET)

        fc_ra_land_fund = d.pop("fc_ra_land_fund", UNSET)

        fc_ra_total = d.pop("fc_ra_total", UNSET)

        fc_ra_per_capita = d.pop("fc_ra_per_capita", UNSET)

        fc_ra_months_retained_imports_goods = d.pop(
            "fc_ra_months_retained_imports_goods", UNSET
        )

        ratio_fc_ra_to_cic = d.pop("ratio_fc_ra_to_cic", UNSET)

        record = cls(
            end_of_month=end_of_month,
            fc_ra_exchange_fund=fc_ra_exchange_fund,
            fc_ra_land_fund=fc_ra_land_fund,
            fc_ra_total=fc_ra_total,
            fc_ra_per_capita=fc_ra_per_capita,
            fc_ra_months_retained_imports_goods=fc_ra_months_retained_imports_goods,
            ratio_fc_ra_to_cic=ratio_fc_ra_to_cic,
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
