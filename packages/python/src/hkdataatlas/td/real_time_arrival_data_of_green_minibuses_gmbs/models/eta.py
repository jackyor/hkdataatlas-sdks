from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Eta")


@_attrs_define
class Eta:
    """
    Attributes:
        diff (int | Unset): Estimated time of arrival in relative minutes.
        eta_seq (int | Unset): Order of ETA entries.
        remarks_en (None | str | Unset): English special message about the ETA.
        remarks_sc (None | str | Unset): Simplified Chinese special message about the ETA.
        remarks_tc (None | str | Unset): Traditional Chinese special message about the ETA.
        timestamp (datetime.datetime | Unset): Estimated time of arrival in absolute time.
    """

    diff: int | Unset = UNSET
    eta_seq: int | Unset = UNSET
    remarks_en: None | str | Unset = UNSET
    remarks_sc: None | str | Unset = UNSET
    remarks_tc: None | str | Unset = UNSET
    timestamp: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        diff = self.diff

        eta_seq = self.eta_seq

        remarks_en: None | str | Unset
        if isinstance(self.remarks_en, Unset):
            remarks_en = UNSET
        else:
            remarks_en = self.remarks_en

        remarks_sc: None | str | Unset
        if isinstance(self.remarks_sc, Unset):
            remarks_sc = UNSET
        else:
            remarks_sc = self.remarks_sc

        remarks_tc: None | str | Unset
        if isinstance(self.remarks_tc, Unset):
            remarks_tc = UNSET
        else:
            remarks_tc = self.remarks_tc

        timestamp: str | Unset = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if diff is not UNSET:
            field_dict["diff"] = diff
        if eta_seq is not UNSET:
            field_dict["eta_seq"] = eta_seq
        if remarks_en is not UNSET:
            field_dict["remarks_en"] = remarks_en
        if remarks_sc is not UNSET:
            field_dict["remarks_sc"] = remarks_sc
        if remarks_tc is not UNSET:
            field_dict["remarks_tc"] = remarks_tc
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        diff = d.pop("diff", UNSET)

        eta_seq = d.pop("eta_seq", UNSET)

        def _parse_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_en = _parse_remarks_en(d.pop("remarks_en", UNSET))

        def _parse_remarks_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_sc = _parse_remarks_sc(d.pop("remarks_sc", UNSET))

        def _parse_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_tc = _parse_remarks_tc(d.pop("remarks_tc", UNSET))

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: datetime.datetime | Unset
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = datetime.datetime.fromisoformat(_timestamp)

        eta = cls(
            diff=diff,
            eta_seq=eta_seq,
            remarks_en=remarks_en,
            remarks_sc=remarks_sc,
            remarks_tc=remarks_tc,
            timestamp=timestamp,
        )

        eta.additional_properties = d
        return eta

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
