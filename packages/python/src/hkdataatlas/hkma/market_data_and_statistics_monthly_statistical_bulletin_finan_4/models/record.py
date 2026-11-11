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
        nominal_gdp (float | Unset):
        real_gdp (float | Unset):
        gov_consol_bal (float | Unset):
        composite_cpi (float | Unset):
        unemploy_rate (float | Unset):
        curr_acc_bal (float | Unset):
        fc_reserve (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    nominal_gdp: float | Unset = UNSET
    real_gdp: float | Unset = UNSET
    gov_consol_bal: float | Unset = UNSET
    composite_cpi: float | Unset = UNSET
    unemploy_rate: float | Unset = UNSET
    curr_acc_bal: float | Unset = UNSET
    fc_reserve: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        nominal_gdp = self.nominal_gdp

        real_gdp = self.real_gdp

        gov_consol_bal = self.gov_consol_bal

        composite_cpi = self.composite_cpi

        unemploy_rate = self.unemploy_rate

        curr_acc_bal = self.curr_acc_bal

        fc_reserve = self.fc_reserve

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if nominal_gdp is not UNSET:
            field_dict["nominal_gdp"] = nominal_gdp
        if real_gdp is not UNSET:
            field_dict["real_gdp"] = real_gdp
        if gov_consol_bal is not UNSET:
            field_dict["gov_consol_bal"] = gov_consol_bal
        if composite_cpi is not UNSET:
            field_dict["composite_cpi"] = composite_cpi
        if unemploy_rate is not UNSET:
            field_dict["unemploy_rate"] = unemploy_rate
        if curr_acc_bal is not UNSET:
            field_dict["curr_acc_bal"] = curr_acc_bal
        if fc_reserve is not UNSET:
            field_dict["fc_reserve"] = fc_reserve

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

        nominal_gdp = d.pop("nominal_gdp", UNSET)

        real_gdp = d.pop("real_gdp", UNSET)

        gov_consol_bal = d.pop("gov_consol_bal", UNSET)

        composite_cpi = d.pop("composite_cpi", UNSET)

        unemploy_rate = d.pop("unemploy_rate", UNSET)

        curr_acc_bal = d.pop("curr_acc_bal", UNSET)

        fc_reserve = d.pop("fc_reserve", UNSET)

        record = cls(
            end_of_month=end_of_month,
            nominal_gdp=nominal_gdp,
            real_gdp=real_gdp,
            gov_consol_bal=gov_consol_bal,
            composite_cpi=composite_cpi,
            unemploy_rate=unemploy_rate,
            curr_acc_bal=curr_acc_bal,
            fc_reserve=fc_reserve,
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
