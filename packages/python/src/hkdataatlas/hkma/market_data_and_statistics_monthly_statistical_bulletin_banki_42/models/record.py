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
        rtctp_pp_payee_proxy_id (float | Unset):
        rtctp_pp_payee_acc_no (float | Unset):
        rtctp_other_payment (float | Unset):
        rtctp (float | Unset):
        rtddp (float | Unset):
        rt_payment (float | Unset):
        bat_payment (float | Unset):
        total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    rtctp_pp_payee_proxy_id: float | Unset = UNSET
    rtctp_pp_payee_acc_no: float | Unset = UNSET
    rtctp_other_payment: float | Unset = UNSET
    rtctp: float | Unset = UNSET
    rtddp: float | Unset = UNSET
    rt_payment: float | Unset = UNSET
    bat_payment: float | Unset = UNSET
    total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        rtctp_pp_payee_proxy_id = self.rtctp_pp_payee_proxy_id

        rtctp_pp_payee_acc_no = self.rtctp_pp_payee_acc_no

        rtctp_other_payment = self.rtctp_other_payment

        rtctp = self.rtctp

        rtddp = self.rtddp

        rt_payment = self.rt_payment

        bat_payment = self.bat_payment

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if rtctp_pp_payee_proxy_id is not UNSET:
            field_dict["rtctp_pp_payee_proxy_id"] = rtctp_pp_payee_proxy_id
        if rtctp_pp_payee_acc_no is not UNSET:
            field_dict["rtctp_pp_payee_acc_no"] = rtctp_pp_payee_acc_no
        if rtctp_other_payment is not UNSET:
            field_dict["rtctp_other_payment"] = rtctp_other_payment
        if rtctp is not UNSET:
            field_dict["rtctp"] = rtctp
        if rtddp is not UNSET:
            field_dict["rtddp"] = rtddp
        if rt_payment is not UNSET:
            field_dict["rt_payment"] = rt_payment
        if bat_payment is not UNSET:
            field_dict["bat_payment"] = bat_payment
        if total is not UNSET:
            field_dict["total"] = total

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

        rtctp_pp_payee_proxy_id = d.pop("rtctp_pp_payee_proxy_id", UNSET)

        rtctp_pp_payee_acc_no = d.pop("rtctp_pp_payee_acc_no", UNSET)

        rtctp_other_payment = d.pop("rtctp_other_payment", UNSET)

        rtctp = d.pop("rtctp", UNSET)

        rtddp = d.pop("rtddp", UNSET)

        rt_payment = d.pop("rt_payment", UNSET)

        bat_payment = d.pop("bat_payment", UNSET)

        total = d.pop("total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            rtctp_pp_payee_proxy_id=rtctp_pp_payee_proxy_id,
            rtctp_pp_payee_acc_no=rtctp_pp_payee_acc_no,
            rtctp_other_payment=rtctp_other_payment,
            rtctp=rtctp,
            rtddp=rtddp,
            rt_payment=rt_payment,
            bat_payment=bat_payment,
            total=total,
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
