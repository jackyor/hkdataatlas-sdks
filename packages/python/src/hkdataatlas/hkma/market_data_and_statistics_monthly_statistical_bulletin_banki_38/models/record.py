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
        mobile_personal (float | Unset):
        mobile_corporate (float | Unset):
        mobile_subtotal (float | Unset):
        email_personal (float | Unset):
        email_corporate (float | Unset):
        email_subtotal (float | Unset):
        fpsid_personal (float | Unset):
        fpsid_corporate (float | Unset):
        fpsid_subtotal (float | Unset):
        total_personal (float | Unset):
        total_corporate (float | Unset):
        total_grand_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    mobile_personal: float | Unset = UNSET
    mobile_corporate: float | Unset = UNSET
    mobile_subtotal: float | Unset = UNSET
    email_personal: float | Unset = UNSET
    email_corporate: float | Unset = UNSET
    email_subtotal: float | Unset = UNSET
    fpsid_personal: float | Unset = UNSET
    fpsid_corporate: float | Unset = UNSET
    fpsid_subtotal: float | Unset = UNSET
    total_personal: float | Unset = UNSET
    total_corporate: float | Unset = UNSET
    total_grand_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        mobile_personal = self.mobile_personal

        mobile_corporate = self.mobile_corporate

        mobile_subtotal = self.mobile_subtotal

        email_personal = self.email_personal

        email_corporate = self.email_corporate

        email_subtotal = self.email_subtotal

        fpsid_personal = self.fpsid_personal

        fpsid_corporate = self.fpsid_corporate

        fpsid_subtotal = self.fpsid_subtotal

        total_personal = self.total_personal

        total_corporate = self.total_corporate

        total_grand_total = self.total_grand_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if mobile_personal is not UNSET:
            field_dict["mobile_personal"] = mobile_personal
        if mobile_corporate is not UNSET:
            field_dict["mobile_corporate"] = mobile_corporate
        if mobile_subtotal is not UNSET:
            field_dict["mobile_subtotal"] = mobile_subtotal
        if email_personal is not UNSET:
            field_dict["email_personal"] = email_personal
        if email_corporate is not UNSET:
            field_dict["email_corporate"] = email_corporate
        if email_subtotal is not UNSET:
            field_dict["email_subtotal"] = email_subtotal
        if fpsid_personal is not UNSET:
            field_dict["fpsid_personal"] = fpsid_personal
        if fpsid_corporate is not UNSET:
            field_dict["fpsid_corporate"] = fpsid_corporate
        if fpsid_subtotal is not UNSET:
            field_dict["fpsid_subtotal"] = fpsid_subtotal
        if total_personal is not UNSET:
            field_dict["total_personal"] = total_personal
        if total_corporate is not UNSET:
            field_dict["total_corporate"] = total_corporate
        if total_grand_total is not UNSET:
            field_dict["total_grand_total"] = total_grand_total

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

        mobile_personal = d.pop("mobile_personal", UNSET)

        mobile_corporate = d.pop("mobile_corporate", UNSET)

        mobile_subtotal = d.pop("mobile_subtotal", UNSET)

        email_personal = d.pop("email_personal", UNSET)

        email_corporate = d.pop("email_corporate", UNSET)

        email_subtotal = d.pop("email_subtotal", UNSET)

        fpsid_personal = d.pop("fpsid_personal", UNSET)

        fpsid_corporate = d.pop("fpsid_corporate", UNSET)

        fpsid_subtotal = d.pop("fpsid_subtotal", UNSET)

        total_personal = d.pop("total_personal", UNSET)

        total_corporate = d.pop("total_corporate", UNSET)

        total_grand_total = d.pop("total_grand_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            mobile_personal=mobile_personal,
            mobile_corporate=mobile_corporate,
            mobile_subtotal=mobile_subtotal,
            email_personal=email_personal,
            email_corporate=email_corporate,
            email_subtotal=email_subtotal,
            fpsid_personal=fpsid_personal,
            fpsid_corporate=fpsid_corporate,
            fpsid_subtotal=fpsid_subtotal,
            total_personal=total_personal,
            total_corporate=total_corporate,
            total_grand_total=total_grand_total,
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
