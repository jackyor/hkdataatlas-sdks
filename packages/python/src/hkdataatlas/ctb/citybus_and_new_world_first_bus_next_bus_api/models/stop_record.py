from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StopRecord")


@_attrs_define
class StopRecord:
    """
    Attributes:
        stop (str | Unset):
        name_en (str | Unset):
        name_tc (str | Unset):
        name_sc (str | Unset):
        lat (float | str | Unset): Publisher dictionary specifies a number; retained current export encodes a string. No
            lexical or range constraint inferred.
        long (float | str | Unset): Publisher dictionary specifies a number; retained current export encodes a string.
            No lexical or range constraint inferred.
        data_timestamp (str | Unset): ISO 8601 date time with time zone per dictionary; no stronger lexical restriction
            inferred.
    """

    stop: str | Unset = UNSET
    name_en: str | Unset = UNSET
    name_tc: str | Unset = UNSET
    name_sc: str | Unset = UNSET
    lat: float | str | Unset = UNSET
    long: float | str | Unset = UNSET
    data_timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stop = self.stop

        name_en = self.name_en

        name_tc = self.name_tc

        name_sc = self.name_sc

        lat: float | str | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        long: float | str | Unset
        if isinstance(self.long, Unset):
            long = UNSET
        else:
            long = self.long

        data_timestamp = self.data_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stop is not UNSET:
            field_dict["stop"] = stop
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc
        if name_sc is not UNSET:
            field_dict["name_sc"] = name_sc
        if lat is not UNSET:
            field_dict["lat"] = lat
        if long is not UNSET:
            field_dict["long"] = long
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stop = d.pop("stop", UNSET)

        name_en = d.pop("name_en", UNSET)

        name_tc = d.pop("name_tc", UNSET)

        name_sc = d.pop("name_sc", UNSET)

        def _parse_lat(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        lat = _parse_lat(d.pop("lat", UNSET))

        def _parse_long(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        long = _parse_long(d.pop("long", UNSET))

        data_timestamp = d.pop("data_timestamp", UNSET)

        stop_record = cls(
            stop=stop,
            name_en=name_en,
            name_tc=name_tc,
            name_sc=name_sc,
            lat=lat,
            long=long,
            data_timestamp=data_timestamp,
        )

        stop_record.additional_properties = d
        return stop_record

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
