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
        fc_swap_deposits (float | Unset):
        deposits_hkd (float | Unset):
        deposits_usd (float | Unset):
        deposits_nonusd_fc (float | Unset):
        deposits_all_fc (float | Unset):
        deposits_all (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    fc_swap_deposits: float | Unset = UNSET
    deposits_hkd: float | Unset = UNSET
    deposits_usd: float | Unset = UNSET
    deposits_nonusd_fc: float | Unset = UNSET
    deposits_all_fc: float | Unset = UNSET
    deposits_all: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        fc_swap_deposits = self.fc_swap_deposits

        deposits_hkd = self.deposits_hkd

        deposits_usd = self.deposits_usd

        deposits_nonusd_fc = self.deposits_nonusd_fc

        deposits_all_fc = self.deposits_all_fc

        deposits_all = self.deposits_all

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if fc_swap_deposits is not UNSET:
            field_dict["fc_swap_deposits"] = fc_swap_deposits
        if deposits_hkd is not UNSET:
            field_dict["deposits_hkd"] = deposits_hkd
        if deposits_usd is not UNSET:
            field_dict["deposits_usd"] = deposits_usd
        if deposits_nonusd_fc is not UNSET:
            field_dict["deposits_nonusd_fc"] = deposits_nonusd_fc
        if deposits_all_fc is not UNSET:
            field_dict["deposits_all_fc"] = deposits_all_fc
        if deposits_all is not UNSET:
            field_dict["deposits_all"] = deposits_all

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

        fc_swap_deposits = d.pop("fc_swap_deposits", UNSET)

        deposits_hkd = d.pop("deposits_hkd", UNSET)

        deposits_usd = d.pop("deposits_usd", UNSET)

        deposits_nonusd_fc = d.pop("deposits_nonusd_fc", UNSET)

        deposits_all_fc = d.pop("deposits_all_fc", UNSET)

        deposits_all = d.pop("deposits_all", UNSET)

        record = cls(
            end_of_month=end_of_month,
            fc_swap_deposits=fc_swap_deposits,
            deposits_hkd=deposits_hkd,
            deposits_usd=deposits_usd,
            deposits_nonusd_fc=deposits_nonusd_fc,
            deposits_all_fc=deposits_all_fc,
            deposits_all=deposits_all,
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
