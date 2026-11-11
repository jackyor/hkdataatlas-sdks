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
        specific_data (str | Unset):
        liquid_adj_facility_bid_rate (float | Unset):
        disc_window_base_rate (float | Unset):
        overnight_hibor (float | Unset):
        field_1m_hibor_fixing (float | Unset):
        liquid_adj_window_offer_rate (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    specific_data: str | Unset = UNSET
    liquid_adj_facility_bid_rate: float | Unset = UNSET
    disc_window_base_rate: float | Unset = UNSET
    overnight_hibor: float | Unset = UNSET
    field_1m_hibor_fixing: float | Unset = UNSET
    liquid_adj_window_offer_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        specific_data = self.specific_data

        liquid_adj_facility_bid_rate = self.liquid_adj_facility_bid_rate

        disc_window_base_rate = self.disc_window_base_rate

        overnight_hibor = self.overnight_hibor

        field_1m_hibor_fixing = self.field_1m_hibor_fixing

        liquid_adj_window_offer_rate = self.liquid_adj_window_offer_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if specific_data is not UNSET:
            field_dict["specific_data"] = specific_data
        if liquid_adj_facility_bid_rate is not UNSET:
            field_dict["liquid_adj_facility_bid_rate"] = liquid_adj_facility_bid_rate
        if disc_window_base_rate is not UNSET:
            field_dict["disc_window_base_rate"] = disc_window_base_rate
        if overnight_hibor is not UNSET:
            field_dict["overnight_hibor"] = overnight_hibor
        if field_1m_hibor_fixing is not UNSET:
            field_dict["1m_hibor_fixing"] = field_1m_hibor_fixing
        if liquid_adj_window_offer_rate is not UNSET:
            field_dict["liquid_adj_window_offer_rate"] = liquid_adj_window_offer_rate

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

        specific_data = d.pop("specific_data", UNSET)

        liquid_adj_facility_bid_rate = d.pop("liquid_adj_facility_bid_rate", UNSET)

        disc_window_base_rate = d.pop("disc_window_base_rate", UNSET)

        overnight_hibor = d.pop("overnight_hibor", UNSET)

        field_1m_hibor_fixing = d.pop("1m_hibor_fixing", UNSET)

        liquid_adj_window_offer_rate = d.pop("liquid_adj_window_offer_rate", UNSET)

        record = cls(
            end_of_month=end_of_month,
            specific_data=specific_data,
            liquid_adj_facility_bid_rate=liquid_adj_facility_bid_rate,
            disc_window_base_rate=disc_window_base_rate,
            overnight_hibor=overnight_hibor,
            field_1m_hibor_fixing=field_1m_hibor_fixing,
            liquid_adj_window_offer_rate=liquid_adj_window_offer_rate,
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
