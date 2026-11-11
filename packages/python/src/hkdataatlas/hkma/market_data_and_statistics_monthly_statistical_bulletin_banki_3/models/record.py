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
        lb_demand_hkd (float | Unset):
        lb_demand_fc (float | Unset):
        lb_demand_total (float | Unset):
        lb_savings_hkd (float | Unset):
        lb_savings_fc (float | Unset):
        lb_savings_total (float | Unset):
        lb_time_hkd (float | Unset):
        lb_time_fc (float | Unset):
        lb_time_total (float | Unset):
        lb_total_hkd (float | Unset):
        lb_total_fc (float | Unset):
        lb_total (float | Unset):
        rlb_hkd (float | Unset):
        rlb_fc (float | Unset):
        rlb_total (float | Unset):
        dtc_hkd (float | Unset):
        dtc_fc (float | Unset):
        dtc_total (float | Unset):
        rlb_dtc_hkd (float | Unset):
        rlb_dtc_fc (float | Unset):
        rlb_dtc_total (float | Unset):
        all_ais_hkd (float | Unset):
        all_ais_fc (float | Unset):
        all_ais_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    lb_demand_hkd: float | Unset = UNSET
    lb_demand_fc: float | Unset = UNSET
    lb_demand_total: float | Unset = UNSET
    lb_savings_hkd: float | Unset = UNSET
    lb_savings_fc: float | Unset = UNSET
    lb_savings_total: float | Unset = UNSET
    lb_time_hkd: float | Unset = UNSET
    lb_time_fc: float | Unset = UNSET
    lb_time_total: float | Unset = UNSET
    lb_total_hkd: float | Unset = UNSET
    lb_total_fc: float | Unset = UNSET
    lb_total: float | Unset = UNSET
    rlb_hkd: float | Unset = UNSET
    rlb_fc: float | Unset = UNSET
    rlb_total: float | Unset = UNSET
    dtc_hkd: float | Unset = UNSET
    dtc_fc: float | Unset = UNSET
    dtc_total: float | Unset = UNSET
    rlb_dtc_hkd: float | Unset = UNSET
    rlb_dtc_fc: float | Unset = UNSET
    rlb_dtc_total: float | Unset = UNSET
    all_ais_hkd: float | Unset = UNSET
    all_ais_fc: float | Unset = UNSET
    all_ais_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        lb_demand_hkd = self.lb_demand_hkd

        lb_demand_fc = self.lb_demand_fc

        lb_demand_total = self.lb_demand_total

        lb_savings_hkd = self.lb_savings_hkd

        lb_savings_fc = self.lb_savings_fc

        lb_savings_total = self.lb_savings_total

        lb_time_hkd = self.lb_time_hkd

        lb_time_fc = self.lb_time_fc

        lb_time_total = self.lb_time_total

        lb_total_hkd = self.lb_total_hkd

        lb_total_fc = self.lb_total_fc

        lb_total = self.lb_total

        rlb_hkd = self.rlb_hkd

        rlb_fc = self.rlb_fc

        rlb_total = self.rlb_total

        dtc_hkd = self.dtc_hkd

        dtc_fc = self.dtc_fc

        dtc_total = self.dtc_total

        rlb_dtc_hkd = self.rlb_dtc_hkd

        rlb_dtc_fc = self.rlb_dtc_fc

        rlb_dtc_total = self.rlb_dtc_total

        all_ais_hkd = self.all_ais_hkd

        all_ais_fc = self.all_ais_fc

        all_ais_total = self.all_ais_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if lb_demand_hkd is not UNSET:
            field_dict["lb_demand_hkd"] = lb_demand_hkd
        if lb_demand_fc is not UNSET:
            field_dict["lb_demand_fc"] = lb_demand_fc
        if lb_demand_total is not UNSET:
            field_dict["lb_demand_total"] = lb_demand_total
        if lb_savings_hkd is not UNSET:
            field_dict["lb_savings_hkd"] = lb_savings_hkd
        if lb_savings_fc is not UNSET:
            field_dict["lb_savings_fc"] = lb_savings_fc
        if lb_savings_total is not UNSET:
            field_dict["lb_savings_total"] = lb_savings_total
        if lb_time_hkd is not UNSET:
            field_dict["lb_time_hkd"] = lb_time_hkd
        if lb_time_fc is not UNSET:
            field_dict["lb_time_fc"] = lb_time_fc
        if lb_time_total is not UNSET:
            field_dict["lb_time_total"] = lb_time_total
        if lb_total_hkd is not UNSET:
            field_dict["lb_total_hkd"] = lb_total_hkd
        if lb_total_fc is not UNSET:
            field_dict["lb_total_fc"] = lb_total_fc
        if lb_total is not UNSET:
            field_dict["lb_total"] = lb_total
        if rlb_hkd is not UNSET:
            field_dict["rlb_hkd"] = rlb_hkd
        if rlb_fc is not UNSET:
            field_dict["rlb_fc"] = rlb_fc
        if rlb_total is not UNSET:
            field_dict["rlb_total"] = rlb_total
        if dtc_hkd is not UNSET:
            field_dict["dtc_hkd"] = dtc_hkd
        if dtc_fc is not UNSET:
            field_dict["dtc_fc"] = dtc_fc
        if dtc_total is not UNSET:
            field_dict["dtc_total"] = dtc_total
        if rlb_dtc_hkd is not UNSET:
            field_dict["rlb_dtc_hkd"] = rlb_dtc_hkd
        if rlb_dtc_fc is not UNSET:
            field_dict["rlb_dtc_fc"] = rlb_dtc_fc
        if rlb_dtc_total is not UNSET:
            field_dict["rlb_dtc_total"] = rlb_dtc_total
        if all_ais_hkd is not UNSET:
            field_dict["all_ais_hkd"] = all_ais_hkd
        if all_ais_fc is not UNSET:
            field_dict["all_ais_fc"] = all_ais_fc
        if all_ais_total is not UNSET:
            field_dict["all_ais_total"] = all_ais_total

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

        lb_demand_hkd = d.pop("lb_demand_hkd", UNSET)

        lb_demand_fc = d.pop("lb_demand_fc", UNSET)

        lb_demand_total = d.pop("lb_demand_total", UNSET)

        lb_savings_hkd = d.pop("lb_savings_hkd", UNSET)

        lb_savings_fc = d.pop("lb_savings_fc", UNSET)

        lb_savings_total = d.pop("lb_savings_total", UNSET)

        lb_time_hkd = d.pop("lb_time_hkd", UNSET)

        lb_time_fc = d.pop("lb_time_fc", UNSET)

        lb_time_total = d.pop("lb_time_total", UNSET)

        lb_total_hkd = d.pop("lb_total_hkd", UNSET)

        lb_total_fc = d.pop("lb_total_fc", UNSET)

        lb_total = d.pop("lb_total", UNSET)

        rlb_hkd = d.pop("rlb_hkd", UNSET)

        rlb_fc = d.pop("rlb_fc", UNSET)

        rlb_total = d.pop("rlb_total", UNSET)

        dtc_hkd = d.pop("dtc_hkd", UNSET)

        dtc_fc = d.pop("dtc_fc", UNSET)

        dtc_total = d.pop("dtc_total", UNSET)

        rlb_dtc_hkd = d.pop("rlb_dtc_hkd", UNSET)

        rlb_dtc_fc = d.pop("rlb_dtc_fc", UNSET)

        rlb_dtc_total = d.pop("rlb_dtc_total", UNSET)

        all_ais_hkd = d.pop("all_ais_hkd", UNSET)

        all_ais_fc = d.pop("all_ais_fc", UNSET)

        all_ais_total = d.pop("all_ais_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            lb_demand_hkd=lb_demand_hkd,
            lb_demand_fc=lb_demand_fc,
            lb_demand_total=lb_demand_total,
            lb_savings_hkd=lb_savings_hkd,
            lb_savings_fc=lb_savings_fc,
            lb_savings_total=lb_savings_total,
            lb_time_hkd=lb_time_hkd,
            lb_time_fc=lb_time_fc,
            lb_time_total=lb_time_total,
            lb_total_hkd=lb_total_hkd,
            lb_total_fc=lb_total_fc,
            lb_total=lb_total,
            rlb_hkd=rlb_hkd,
            rlb_fc=rlb_fc,
            rlb_total=rlb_total,
            dtc_hkd=dtc_hkd,
            dtc_fc=dtc_fc,
            dtc_total=dtc_total,
            rlb_dtc_hkd=rlb_dtc_hkd,
            rlb_dtc_fc=rlb_dtc_fc,
            rlb_dtc_total=rlb_dtc_total,
            all_ais_hkd=all_ais_hkd,
            all_ais_fc=all_ais_fc,
            all_ais_total=all_ais_total,
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
