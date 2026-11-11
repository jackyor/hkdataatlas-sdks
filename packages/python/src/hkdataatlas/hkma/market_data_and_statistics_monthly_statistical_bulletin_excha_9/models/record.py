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
        ep_no_of_cmu_members (float | Unset):
        ep_no_of_dil (float | Unset):
        ep_outstanding_amt_dil_with_hkd (float | Unset):
        ep_outstanding_amt_dil_with_rmb (float | Unset):
        ep_outstanding_amt_dil_with_usd (float | Unset):
        ep_outstanding_amt_dil_with_other_curr (float | Unset):
        ep_outstanding_amt_dil_with_total (float | Unset):
        dp_avg_dt_hkd (float | Unset):
        dp_avg_dt_rmb (float | Unset):
        dp_avg_dt_usd (float | Unset):
        dp_avg_dt_other_curr (float | Unset):
        dp_avg_dt_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    ep_no_of_cmu_members: float | Unset = UNSET
    ep_no_of_dil: float | Unset = UNSET
    ep_outstanding_amt_dil_with_hkd: float | Unset = UNSET
    ep_outstanding_amt_dil_with_rmb: float | Unset = UNSET
    ep_outstanding_amt_dil_with_usd: float | Unset = UNSET
    ep_outstanding_amt_dil_with_other_curr: float | Unset = UNSET
    ep_outstanding_amt_dil_with_total: float | Unset = UNSET
    dp_avg_dt_hkd: float | Unset = UNSET
    dp_avg_dt_rmb: float | Unset = UNSET
    dp_avg_dt_usd: float | Unset = UNSET
    dp_avg_dt_other_curr: float | Unset = UNSET
    dp_avg_dt_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        ep_no_of_cmu_members = self.ep_no_of_cmu_members

        ep_no_of_dil = self.ep_no_of_dil

        ep_outstanding_amt_dil_with_hkd = self.ep_outstanding_amt_dil_with_hkd

        ep_outstanding_amt_dil_with_rmb = self.ep_outstanding_amt_dil_with_rmb

        ep_outstanding_amt_dil_with_usd = self.ep_outstanding_amt_dil_with_usd

        ep_outstanding_amt_dil_with_other_curr = (
            self.ep_outstanding_amt_dil_with_other_curr
        )

        ep_outstanding_amt_dil_with_total = self.ep_outstanding_amt_dil_with_total

        dp_avg_dt_hkd = self.dp_avg_dt_hkd

        dp_avg_dt_rmb = self.dp_avg_dt_rmb

        dp_avg_dt_usd = self.dp_avg_dt_usd

        dp_avg_dt_other_curr = self.dp_avg_dt_other_curr

        dp_avg_dt_total = self.dp_avg_dt_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if ep_no_of_cmu_members is not UNSET:
            field_dict["ep_no_of_cmu_members"] = ep_no_of_cmu_members
        if ep_no_of_dil is not UNSET:
            field_dict["ep_no_of_dil"] = ep_no_of_dil
        if ep_outstanding_amt_dil_with_hkd is not UNSET:
            field_dict["ep_outstanding_amt_dil_with_hkd"] = (
                ep_outstanding_amt_dil_with_hkd
            )
        if ep_outstanding_amt_dil_with_rmb is not UNSET:
            field_dict["ep_outstanding_amt_dil_with_rmb"] = (
                ep_outstanding_amt_dil_with_rmb
            )
        if ep_outstanding_amt_dil_with_usd is not UNSET:
            field_dict["ep_outstanding_amt_dil_with_usd"] = (
                ep_outstanding_amt_dil_with_usd
            )
        if ep_outstanding_amt_dil_with_other_curr is not UNSET:
            field_dict["ep_outstanding_amt_dil_with_other_curr"] = (
                ep_outstanding_amt_dil_with_other_curr
            )
        if ep_outstanding_amt_dil_with_total is not UNSET:
            field_dict["ep_outstanding_amt_dil_with_total"] = (
                ep_outstanding_amt_dil_with_total
            )
        if dp_avg_dt_hkd is not UNSET:
            field_dict["dp_avg_dt_hkd"] = dp_avg_dt_hkd
        if dp_avg_dt_rmb is not UNSET:
            field_dict["dp_avg_dt_rmb"] = dp_avg_dt_rmb
        if dp_avg_dt_usd is not UNSET:
            field_dict["dp_avg_dt_usd"] = dp_avg_dt_usd
        if dp_avg_dt_other_curr is not UNSET:
            field_dict["dp_avg_dt_other_curr"] = dp_avg_dt_other_curr
        if dp_avg_dt_total is not UNSET:
            field_dict["dp_avg_dt_total"] = dp_avg_dt_total

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

        ep_no_of_cmu_members = d.pop("ep_no_of_cmu_members", UNSET)

        ep_no_of_dil = d.pop("ep_no_of_dil", UNSET)

        ep_outstanding_amt_dil_with_hkd = d.pop(
            "ep_outstanding_amt_dil_with_hkd", UNSET
        )

        ep_outstanding_amt_dil_with_rmb = d.pop(
            "ep_outstanding_amt_dil_with_rmb", UNSET
        )

        ep_outstanding_amt_dil_with_usd = d.pop(
            "ep_outstanding_amt_dil_with_usd", UNSET
        )

        ep_outstanding_amt_dil_with_other_curr = d.pop(
            "ep_outstanding_amt_dil_with_other_curr", UNSET
        )

        ep_outstanding_amt_dil_with_total = d.pop(
            "ep_outstanding_amt_dil_with_total", UNSET
        )

        dp_avg_dt_hkd = d.pop("dp_avg_dt_hkd", UNSET)

        dp_avg_dt_rmb = d.pop("dp_avg_dt_rmb", UNSET)

        dp_avg_dt_usd = d.pop("dp_avg_dt_usd", UNSET)

        dp_avg_dt_other_curr = d.pop("dp_avg_dt_other_curr", UNSET)

        dp_avg_dt_total = d.pop("dp_avg_dt_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            ep_no_of_cmu_members=ep_no_of_cmu_members,
            ep_no_of_dil=ep_no_of_dil,
            ep_outstanding_amt_dil_with_hkd=ep_outstanding_amt_dil_with_hkd,
            ep_outstanding_amt_dil_with_rmb=ep_outstanding_amt_dil_with_rmb,
            ep_outstanding_amt_dil_with_usd=ep_outstanding_amt_dil_with_usd,
            ep_outstanding_amt_dil_with_other_curr=ep_outstanding_amt_dil_with_other_curr,
            ep_outstanding_amt_dil_with_total=ep_outstanding_amt_dil_with_total,
            dp_avg_dt_hkd=dp_avg_dt_hkd,
            dp_avg_dt_rmb=dp_avg_dt_rmb,
            dp_avg_dt_usd=dp_avg_dt_usd,
            dp_avg_dt_other_curr=dp_avg_dt_other_curr,
            dp_avg_dt_total=dp_avg_dt_total,
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
