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
        overseas_incorp_ais (float | Unset):
        locally_incorp_ais (float | Unset):
        mainland_bank_subs_ais (float | Unset):
        lending_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    overseas_incorp_ais: float | Unset = UNSET
    locally_incorp_ais: float | Unset = UNSET
    mainland_bank_subs_ais: float | Unset = UNSET
    lending_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        overseas_incorp_ais = self.overseas_incorp_ais

        locally_incorp_ais = self.locally_incorp_ais

        mainland_bank_subs_ais = self.mainland_bank_subs_ais

        lending_total = self.lending_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if overseas_incorp_ais is not UNSET:
            field_dict["overseas_incorp_ais"] = overseas_incorp_ais
        if locally_incorp_ais is not UNSET:
            field_dict["locally_incorp_ais"] = locally_incorp_ais
        if mainland_bank_subs_ais is not UNSET:
            field_dict["mainland_bank_subs_ais"] = mainland_bank_subs_ais
        if lending_total is not UNSET:
            field_dict["lending_total"] = lending_total

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

        overseas_incorp_ais = d.pop("overseas_incorp_ais", UNSET)

        locally_incorp_ais = d.pop("locally_incorp_ais", UNSET)

        mainland_bank_subs_ais = d.pop("mainland_bank_subs_ais", UNSET)

        lending_total = d.pop("lending_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            overseas_incorp_ais=overseas_incorp_ais,
            locally_incorp_ais=locally_incorp_ais,
            mainland_bank_subs_ais=mainland_bank_subs_ais,
            lending_total=lending_total,
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
