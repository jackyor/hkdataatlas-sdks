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
        chq_hkd (float | Unset):
        chq_usd (float | Unset):
        chats_hkd (float | Unset):
        chats_usd (float | Unset):
        chats_euro (float | Unset):
        ecg_hkd (float | Unset):
        ecg_usd (float | Unset):
        total_hkd (float | Unset):
        total_usd (float | Unset):
        total_euro (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    chq_hkd: float | Unset = UNSET
    chq_usd: float | Unset = UNSET
    chats_hkd: float | Unset = UNSET
    chats_usd: float | Unset = UNSET
    chats_euro: float | Unset = UNSET
    ecg_hkd: float | Unset = UNSET
    ecg_usd: float | Unset = UNSET
    total_hkd: float | Unset = UNSET
    total_usd: float | Unset = UNSET
    total_euro: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        chq_hkd = self.chq_hkd

        chq_usd = self.chq_usd

        chats_hkd = self.chats_hkd

        chats_usd = self.chats_usd

        chats_euro = self.chats_euro

        ecg_hkd = self.ecg_hkd

        ecg_usd = self.ecg_usd

        total_hkd = self.total_hkd

        total_usd = self.total_usd

        total_euro = self.total_euro

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if chq_hkd is not UNSET:
            field_dict["chq_hkd"] = chq_hkd
        if chq_usd is not UNSET:
            field_dict["chq_usd"] = chq_usd
        if chats_hkd is not UNSET:
            field_dict["chats_hkd"] = chats_hkd
        if chats_usd is not UNSET:
            field_dict["chats_usd"] = chats_usd
        if chats_euro is not UNSET:
            field_dict["chats_euro"] = chats_euro
        if ecg_hkd is not UNSET:
            field_dict["ecg_hkd"] = ecg_hkd
        if ecg_usd is not UNSET:
            field_dict["ecg_usd"] = ecg_usd
        if total_hkd is not UNSET:
            field_dict["total_hkd"] = total_hkd
        if total_usd is not UNSET:
            field_dict["total_usd"] = total_usd
        if total_euro is not UNSET:
            field_dict["total_euro"] = total_euro

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

        chq_hkd = d.pop("chq_hkd", UNSET)

        chq_usd = d.pop("chq_usd", UNSET)

        chats_hkd = d.pop("chats_hkd", UNSET)

        chats_usd = d.pop("chats_usd", UNSET)

        chats_euro = d.pop("chats_euro", UNSET)

        ecg_hkd = d.pop("ecg_hkd", UNSET)

        ecg_usd = d.pop("ecg_usd", UNSET)

        total_hkd = d.pop("total_hkd", UNSET)

        total_usd = d.pop("total_usd", UNSET)

        total_euro = d.pop("total_euro", UNSET)

        record = cls(
            end_of_month=end_of_month,
            chq_hkd=chq_hkd,
            chq_usd=chq_usd,
            chats_hkd=chats_hkd,
            chats_usd=chats_usd,
            chats_euro=chats_euro,
            ecg_hkd=ecg_hkd,
            ecg_usd=ecg_usd,
            total_hkd=total_hkd,
            total_usd=total_usd,
            total_euro=total_euro,
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
