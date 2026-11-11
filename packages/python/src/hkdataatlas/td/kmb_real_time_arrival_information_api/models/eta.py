from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.eta_dir import EtaDir, check_eta_dir
from ..types import UNSET, Unset

T = TypeVar("T", bound="Eta")


@_attrs_define
class Eta:
    """
    Attributes:
        co (str | Unset): Bus company; documented value is KMB. Example: KMB.
        data_timestamp (datetime.datetime | Unset): Date-time timestamp with time zone in ISO 8601 format.
        dest_en (str | Unset): Route destination in English.
        dest_sc (str | Unset): Route destination in Simplified Chinese.
        dest_tc (str | Unset): Route destination in Traditional Chinese.
        dir_ (EtaDir | Unset): Route direction: I is inbound and O is outbound. Example: O.
        eta (datetime.datetime | None | Unset): Next ETA timestamp, or null when no ETA is available, as shown for a
            route with limited operating days.
        eta_seq (int | Unset): Sequence number of ETA. Example: 1.
        rmk_en (str | Unset): ETA remark in English.
        rmk_sc (str | Unset): ETA remark in Simplified Chinese.
        rmk_tc (str | Unset): ETA remark in Traditional Chinese.
        route (str | Unset): Bus route number. Example: 40.
        seq (int | Unset): Stop sequence number of a bus route. Example: 7.
        service_type (int | str | Unset): Service type. The data dictionary declares String, whereas ETA API examples
            use both string and integer representations.
        stop (str | Unset): ID of a bus stop. Example: A60AE774B09A5E44.
    """

    co: str | Unset = UNSET
    data_timestamp: datetime.datetime | Unset = UNSET
    dest_en: str | Unset = UNSET
    dest_sc: str | Unset = UNSET
    dest_tc: str | Unset = UNSET
    dir_: EtaDir | Unset = UNSET
    eta: datetime.datetime | None | Unset = UNSET
    eta_seq: int | Unset = UNSET
    rmk_en: str | Unset = UNSET
    rmk_sc: str | Unset = UNSET
    rmk_tc: str | Unset = UNSET
    route: str | Unset = UNSET
    seq: int | Unset = UNSET
    service_type: int | str | Unset = UNSET
    stop: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co = self.co

        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

        dest_en = self.dest_en

        dest_sc = self.dest_sc

        dest_tc = self.dest_tc

        dir_: str | Unset = UNSET
        if not isinstance(self.dir_, Unset):
            dir_ = self.dir_

        eta: None | str | Unset
        if isinstance(self.eta, Unset):
            eta = UNSET
        elif isinstance(self.eta, datetime.datetime):
            eta = self.eta.isoformat()
        else:
            eta = self.eta

        eta_seq = self.eta_seq

        rmk_en = self.rmk_en

        rmk_sc = self.rmk_sc

        rmk_tc = self.rmk_tc

        route = self.route

        seq = self.seq

        service_type: int | str | Unset
        if isinstance(self.service_type, Unset):
            service_type = UNSET
        else:
            service_type = self.service_type

        stop = self.stop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co is not UNSET:
            field_dict["co"] = co
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if dest_en is not UNSET:
            field_dict["dest_en"] = dest_en
        if dest_sc is not UNSET:
            field_dict["dest_sc"] = dest_sc
        if dest_tc is not UNSET:
            field_dict["dest_tc"] = dest_tc
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if eta is not UNSET:
            field_dict["eta"] = eta
        if eta_seq is not UNSET:
            field_dict["eta_seq"] = eta_seq
        if rmk_en is not UNSET:
            field_dict["rmk_en"] = rmk_en
        if rmk_sc is not UNSET:
            field_dict["rmk_sc"] = rmk_sc
        if rmk_tc is not UNSET:
            field_dict["rmk_tc"] = rmk_tc
        if route is not UNSET:
            field_dict["route"] = route
        if seq is not UNSET:
            field_dict["seq"] = seq
        if service_type is not UNSET:
            field_dict["service_type"] = service_type
        if stop is not UNSET:
            field_dict["stop"] = stop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        co = d.pop("co", UNSET)

        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

        dest_en = d.pop("dest_en", UNSET)

        dest_sc = d.pop("dest_sc", UNSET)

        dest_tc = d.pop("dest_tc", UNSET)

        _dir_ = d.pop("dir", UNSET)
        dir_: EtaDir | Unset
        if isinstance(_dir_, Unset):
            dir_ = UNSET
        else:
            dir_ = check_eta_dir(_dir_)

        def _parse_eta(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                eta_type_0 = datetime.datetime.fromisoformat(data)

                return eta_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        eta = _parse_eta(d.pop("eta", UNSET))

        eta_seq = d.pop("eta_seq", UNSET)

        rmk_en = d.pop("rmk_en", UNSET)

        rmk_sc = d.pop("rmk_sc", UNSET)

        rmk_tc = d.pop("rmk_tc", UNSET)

        route = d.pop("route", UNSET)

        seq = d.pop("seq", UNSET)

        def _parse_service_type(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        service_type = _parse_service_type(d.pop("service_type", UNSET))

        stop = d.pop("stop", UNSET)

        eta = cls(
            co=co,
            data_timestamp=data_timestamp,
            dest_en=dest_en,
            dest_sc=dest_sc,
            dest_tc=dest_tc,
            dir_=dir_,
            eta=eta,
            eta_seq=eta_seq,
            rmk_en=rmk_en,
            rmk_sc=rmk_sc,
            rmk_tc=rmk_tc,
            route=route,
            seq=seq,
            service_type=service_type,
            stop=stop,
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
