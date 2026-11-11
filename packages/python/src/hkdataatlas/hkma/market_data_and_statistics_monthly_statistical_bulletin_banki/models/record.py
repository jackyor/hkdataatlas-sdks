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
        lb_incorp_hk (float | Unset):
        lb_incorp_outside_hk (float | Unset):
        rlb_incorp_hk (float | Unset):
        rlb_incorp_outside_hk (float | Unset):
        dtc_incorp_hk (float | Unset):
        dtc_incorp_outside_hk (float | Unset):
        all_ais (float | Unset):
        lros (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    lb_incorp_hk: float | Unset = UNSET
    lb_incorp_outside_hk: float | Unset = UNSET
    rlb_incorp_hk: float | Unset = UNSET
    rlb_incorp_outside_hk: float | Unset = UNSET
    dtc_incorp_hk: float | Unset = UNSET
    dtc_incorp_outside_hk: float | Unset = UNSET
    all_ais: float | Unset = UNSET
    lros: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        lb_incorp_hk = self.lb_incorp_hk

        lb_incorp_outside_hk = self.lb_incorp_outside_hk

        rlb_incorp_hk = self.rlb_incorp_hk

        rlb_incorp_outside_hk = self.rlb_incorp_outside_hk

        dtc_incorp_hk = self.dtc_incorp_hk

        dtc_incorp_outside_hk = self.dtc_incorp_outside_hk

        all_ais = self.all_ais

        lros = self.lros

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if lb_incorp_hk is not UNSET:
            field_dict["lb_incorp_hk"] = lb_incorp_hk
        if lb_incorp_outside_hk is not UNSET:
            field_dict["lb_incorp_outside_hk"] = lb_incorp_outside_hk
        if rlb_incorp_hk is not UNSET:
            field_dict["rlb_incorp_hk"] = rlb_incorp_hk
        if rlb_incorp_outside_hk is not UNSET:
            field_dict["rlb_incorp_outside_hk"] = rlb_incorp_outside_hk
        if dtc_incorp_hk is not UNSET:
            field_dict["dtc_incorp_hk"] = dtc_incorp_hk
        if dtc_incorp_outside_hk is not UNSET:
            field_dict["dtc_incorp_outside_hk"] = dtc_incorp_outside_hk
        if all_ais is not UNSET:
            field_dict["all_ais"] = all_ais
        if lros is not UNSET:
            field_dict["lros"] = lros

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

        lb_incorp_hk = d.pop("lb_incorp_hk", UNSET)

        lb_incorp_outside_hk = d.pop("lb_incorp_outside_hk", UNSET)

        rlb_incorp_hk = d.pop("rlb_incorp_hk", UNSET)

        rlb_incorp_outside_hk = d.pop("rlb_incorp_outside_hk", UNSET)

        dtc_incorp_hk = d.pop("dtc_incorp_hk", UNSET)

        dtc_incorp_outside_hk = d.pop("dtc_incorp_outside_hk", UNSET)

        all_ais = d.pop("all_ais", UNSET)

        lros = d.pop("lros", UNSET)

        record = cls(
            end_of_month=end_of_month,
            lb_incorp_hk=lb_incorp_hk,
            lb_incorp_outside_hk=lb_incorp_outside_hk,
            rlb_incorp_hk=rlb_incorp_hk,
            rlb_incorp_outside_hk=rlb_incorp_outside_hk,
            dtc_incorp_hk=dtc_incorp_hk,
            dtc_incorp_outside_hk=dtc_incorp_outside_hk,
            all_ais=all_ais,
            lros=lros,
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
