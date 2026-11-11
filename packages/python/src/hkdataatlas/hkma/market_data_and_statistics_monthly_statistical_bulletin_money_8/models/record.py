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
        transinhk_plcmt_brwg (float | Unset):
        transinhk_swap (float | Unset):
        transinhk_total (float | Unset):
        transouthk_plcmt_brwg (float | Unset):
        transouthk_swap (float | Unset):
        transouthk_total (float | Unset):
        alltrans_plcmt_brwg (float | Unset):
        alltrans_swap (float | Unset):
        alltrans_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    transinhk_plcmt_brwg: float | Unset = UNSET
    transinhk_swap: float | Unset = UNSET
    transinhk_total: float | Unset = UNSET
    transouthk_plcmt_brwg: float | Unset = UNSET
    transouthk_swap: float | Unset = UNSET
    transouthk_total: float | Unset = UNSET
    alltrans_plcmt_brwg: float | Unset = UNSET
    alltrans_swap: float | Unset = UNSET
    alltrans_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        transinhk_plcmt_brwg = self.transinhk_plcmt_brwg

        transinhk_swap = self.transinhk_swap

        transinhk_total = self.transinhk_total

        transouthk_plcmt_brwg = self.transouthk_plcmt_brwg

        transouthk_swap = self.transouthk_swap

        transouthk_total = self.transouthk_total

        alltrans_plcmt_brwg = self.alltrans_plcmt_brwg

        alltrans_swap = self.alltrans_swap

        alltrans_total = self.alltrans_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if transinhk_plcmt_brwg is not UNSET:
            field_dict["transinhk_plcmt_brwg"] = transinhk_plcmt_brwg
        if transinhk_swap is not UNSET:
            field_dict["transinhk_swap"] = transinhk_swap
        if transinhk_total is not UNSET:
            field_dict["transinhk_total"] = transinhk_total
        if transouthk_plcmt_brwg is not UNSET:
            field_dict["transouthk_plcmt_brwg"] = transouthk_plcmt_brwg
        if transouthk_swap is not UNSET:
            field_dict["transouthk_swap"] = transouthk_swap
        if transouthk_total is not UNSET:
            field_dict["transouthk_total"] = transouthk_total
        if alltrans_plcmt_brwg is not UNSET:
            field_dict["alltrans_plcmt_brwg"] = alltrans_plcmt_brwg
        if alltrans_swap is not UNSET:
            field_dict["alltrans_swap"] = alltrans_swap
        if alltrans_total is not UNSET:
            field_dict["alltrans_total"] = alltrans_total

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

        transinhk_plcmt_brwg = d.pop("transinhk_plcmt_brwg", UNSET)

        transinhk_swap = d.pop("transinhk_swap", UNSET)

        transinhk_total = d.pop("transinhk_total", UNSET)

        transouthk_plcmt_brwg = d.pop("transouthk_plcmt_brwg", UNSET)

        transouthk_swap = d.pop("transouthk_swap", UNSET)

        transouthk_total = d.pop("transouthk_total", UNSET)

        alltrans_plcmt_brwg = d.pop("alltrans_plcmt_brwg", UNSET)

        alltrans_swap = d.pop("alltrans_swap", UNSET)

        alltrans_total = d.pop("alltrans_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            transinhk_plcmt_brwg=transinhk_plcmt_brwg,
            transinhk_swap=transinhk_swap,
            transinhk_total=transinhk_total,
            transouthk_plcmt_brwg=transouthk_plcmt_brwg,
            transouthk_swap=transouthk_swap,
            transouthk_total=transouthk_total,
            alltrans_plcmt_brwg=alltrans_plcmt_brwg,
            alltrans_swap=alltrans_swap,
            alltrans_total=alltrans_total,
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
