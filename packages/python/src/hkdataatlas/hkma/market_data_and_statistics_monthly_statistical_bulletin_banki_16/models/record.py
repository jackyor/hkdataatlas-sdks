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
        end_of_quarter (datetime.date | Unset):
        endperiod_noofaccts (float | Unset):
        endperiod_delinquent_amt (float | Unset):
        during_chargeoff_amt (float | Unset):
        during_rollover_amt (float | Unset):
        during_avg_total_receivables (float | Unset):
    """

    end_of_quarter: datetime.date | Unset = UNSET
    endperiod_noofaccts: float | Unset = UNSET
    endperiod_delinquent_amt: float | Unset = UNSET
    during_chargeoff_amt: float | Unset = UNSET
    during_rollover_amt: float | Unset = UNSET
    during_avg_total_receivables: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_quarter: str | Unset = UNSET
        if not isinstance(self.end_of_quarter, Unset):
            end_of_quarter = self.end_of_quarter.isoformat()

        endperiod_noofaccts = self.endperiod_noofaccts

        endperiod_delinquent_amt = self.endperiod_delinquent_amt

        during_chargeoff_amt = self.during_chargeoff_amt

        during_rollover_amt = self.during_rollover_amt

        during_avg_total_receivables = self.during_avg_total_receivables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_quarter is not UNSET:
            field_dict["end_of_quarter"] = end_of_quarter
        if endperiod_noofaccts is not UNSET:
            field_dict["endperiod_noofaccts"] = endperiod_noofaccts
        if endperiod_delinquent_amt is not UNSET:
            field_dict["endperiod_delinquent_amt"] = endperiod_delinquent_amt
        if during_chargeoff_amt is not UNSET:
            field_dict["during_chargeoff_amt"] = during_chargeoff_amt
        if during_rollover_amt is not UNSET:
            field_dict["during_rollover_amt"] = during_rollover_amt
        if during_avg_total_receivables is not UNSET:
            field_dict["during_avg_total_receivables"] = during_avg_total_receivables

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_quarter = d.pop("end_of_quarter", UNSET)
        end_of_quarter: datetime.date | Unset
        if isinstance(_end_of_quarter, Unset):
            end_of_quarter = UNSET
        else:
            end_of_quarter = datetime.date.fromisoformat(_end_of_quarter)

        endperiod_noofaccts = d.pop("endperiod_noofaccts", UNSET)

        endperiod_delinquent_amt = d.pop("endperiod_delinquent_amt", UNSET)

        during_chargeoff_amt = d.pop("during_chargeoff_amt", UNSET)

        during_rollover_amt = d.pop("during_rollover_amt", UNSET)

        during_avg_total_receivables = d.pop("during_avg_total_receivables", UNSET)

        record = cls(
            end_of_quarter=end_of_quarter,
            endperiod_noofaccts=endperiod_noofaccts,
            endperiod_delinquent_amt=endperiod_delinquent_amt,
            during_chargeoff_amt=during_chargeoff_amt,
            during_rollover_amt=during_rollover_amt,
            during_avg_total_receivables=during_avg_total_receivables,
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
