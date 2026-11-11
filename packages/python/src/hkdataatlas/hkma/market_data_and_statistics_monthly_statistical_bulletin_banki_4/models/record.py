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
        demand_savings_deposits (float | Unset):
        time_deposits (float | Unset):
        total_deposits (float | Unset):
        no_of_ais_engaged (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    demand_savings_deposits: float | Unset = UNSET
    time_deposits: float | Unset = UNSET
    total_deposits: float | Unset = UNSET
    no_of_ais_engaged: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        demand_savings_deposits = self.demand_savings_deposits

        time_deposits = self.time_deposits

        total_deposits = self.total_deposits

        no_of_ais_engaged = self.no_of_ais_engaged

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if demand_savings_deposits is not UNSET:
            field_dict["demand_savings_deposits"] = demand_savings_deposits
        if time_deposits is not UNSET:
            field_dict["time_deposits"] = time_deposits
        if total_deposits is not UNSET:
            field_dict["total_deposits"] = total_deposits
        if no_of_ais_engaged is not UNSET:
            field_dict["no_of_ais_engaged"] = no_of_ais_engaged

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

        demand_savings_deposits = d.pop("demand_savings_deposits", UNSET)

        time_deposits = d.pop("time_deposits", UNSET)

        total_deposits = d.pop("total_deposits", UNSET)

        no_of_ais_engaged = d.pop("no_of_ais_engaged", UNSET)

        record = cls(
            end_of_month=end_of_month,
            demand_savings_deposits=demand_savings_deposits,
            time_deposits=time_deposits,
            total_deposits=total_deposits,
            no_of_ais_engaged=no_of_ais_engaged,
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
