from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EtaRecord")


@_attrs_define
class EtaRecord:
    """
    Attributes:
        co (str | Unset):
        route (str | Unset):
        dir_ (str | Unset):
        stop (str | Unset):
        dest_en (str | Unset):
        dest_tc (str | Unset):
        dest_sc (str | Unset):
        eta (str | Unset):
        rmk_en (str | Unset):
        rmk_tc (str | Unset):
        rmk_sc (str | Unset):
        seq (float | Unset):
        eta_seq (float | Unset):
        data_timestamp (str | Unset): ISO 8601 date time with time zone per dictionary; no stronger lexical restriction
            inferred.
    """

    co: str | Unset = UNSET
    route: str | Unset = UNSET
    dir_: str | Unset = UNSET
    stop: str | Unset = UNSET
    dest_en: str | Unset = UNSET
    dest_tc: str | Unset = UNSET
    dest_sc: str | Unset = UNSET
    eta: str | Unset = UNSET
    rmk_en: str | Unset = UNSET
    rmk_tc: str | Unset = UNSET
    rmk_sc: str | Unset = UNSET
    seq: float | Unset = UNSET
    eta_seq: float | Unset = UNSET
    data_timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co = self.co

        route = self.route

        dir_ = self.dir_

        stop = self.stop

        dest_en = self.dest_en

        dest_tc = self.dest_tc

        dest_sc = self.dest_sc

        eta = self.eta

        rmk_en = self.rmk_en

        rmk_tc = self.rmk_tc

        rmk_sc = self.rmk_sc

        seq = self.seq

        eta_seq = self.eta_seq

        data_timestamp = self.data_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co is not UNSET:
            field_dict["co"] = co
        if route is not UNSET:
            field_dict["route"] = route
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if stop is not UNSET:
            field_dict["stop"] = stop
        if dest_en is not UNSET:
            field_dict["dest_en"] = dest_en
        if dest_tc is not UNSET:
            field_dict["dest_tc"] = dest_tc
        if dest_sc is not UNSET:
            field_dict["dest_sc"] = dest_sc
        if eta is not UNSET:
            field_dict["eta"] = eta
        if rmk_en is not UNSET:
            field_dict["rmk_en"] = rmk_en
        if rmk_tc is not UNSET:
            field_dict["rmk_tc"] = rmk_tc
        if rmk_sc is not UNSET:
            field_dict["rmk_sc"] = rmk_sc
        if seq is not UNSET:
            field_dict["seq"] = seq
        if eta_seq is not UNSET:
            field_dict["eta_seq"] = eta_seq
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        co = d.pop("co", UNSET)

        route = d.pop("route", UNSET)

        dir_ = d.pop("dir", UNSET)

        stop = d.pop("stop", UNSET)

        dest_en = d.pop("dest_en", UNSET)

        dest_tc = d.pop("dest_tc", UNSET)

        dest_sc = d.pop("dest_sc", UNSET)

        eta = d.pop("eta", UNSET)

        rmk_en = d.pop("rmk_en", UNSET)

        rmk_tc = d.pop("rmk_tc", UNSET)

        rmk_sc = d.pop("rmk_sc", UNSET)

        seq = d.pop("seq", UNSET)

        eta_seq = d.pop("eta_seq", UNSET)

        data_timestamp = d.pop("data_timestamp", UNSET)

        eta_record = cls(
            co=co,
            route=route,
            dir_=dir_,
            stop=stop,
            dest_en=dest_en,
            dest_tc=dest_tc,
            dest_sc=dest_sc,
            eta=eta,
            rmk_en=rmk_en,
            rmk_tc=rmk_tc,
            rmk_sc=rmk_sc,
            seq=seq,
            eta_seq=eta_seq,
            data_timestamp=data_timestamp,
        )

        eta_record.additional_properties = d
        return eta_record

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
