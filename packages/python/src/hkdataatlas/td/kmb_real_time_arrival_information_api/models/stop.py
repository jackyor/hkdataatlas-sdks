from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Stop")


@_attrs_define
class Stop:
    """The data dictionary declares latitude and longitude as strings; API examples also represent them as JSON numbers.
    Both representations are allowed.

        Attributes:
            data_timestamp (datetime.datetime | Unset): Date-time timestamp with time zone in ISO 8601 format.
            lat (float | str | Unset): Latitude in decimal degrees using WGS84. The data dictionary declares String, while
                examples show both strings and numbers.
            long (float | str | Unset): Longitude in decimal degrees using WGS84. The data dictionary declares String, while
                examples show both strings and numbers.
            name_en (str | Unset): Bus stop name in English.
            name_sc (str | Unset): Bus stop name in Simplified Chinese.
            name_tc (str | Unset): Bus stop name in Traditional Chinese.
            stop (str | Unset): ID of a bus stop. Example: A3ADFCDF8487ADB9.
    """

    data_timestamp: datetime.datetime | Unset = UNSET
    lat: float | str | Unset = UNSET
    long: float | str | Unset = UNSET
    name_en: str | Unset = UNSET
    name_sc: str | Unset = UNSET
    name_tc: str | Unset = UNSET
    stop: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_timestamp: str | Unset = UNSET
        if not isinstance(self.data_timestamp, Unset):
            data_timestamp = self.data_timestamp.isoformat()

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

        name_en = self.name_en

        name_sc = self.name_sc

        name_tc = self.name_tc

        stop = self.stop

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp
        if lat is not UNSET:
            field_dict["lat"] = lat
        if long is not UNSET:
            field_dict["long"] = long
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if name_sc is not UNSET:
            field_dict["name_sc"] = name_sc
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc
        if stop is not UNSET:
            field_dict["stop"] = stop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _data_timestamp = d.pop("data_timestamp", UNSET)
        data_timestamp: datetime.datetime | Unset
        if isinstance(_data_timestamp, Unset):
            data_timestamp = UNSET
        else:
            data_timestamp = datetime.datetime.fromisoformat(_data_timestamp)

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

        name_en = d.pop("name_en", UNSET)

        name_sc = d.pop("name_sc", UNSET)

        name_tc = d.pop("name_tc", UNSET)

        stop = d.pop("stop", UNSET)

        stop = cls(
            data_timestamp=data_timestamp,
            lat=lat,
            long=long,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            stop=stop,
        )

        stop.additional_properties = d
        return stop

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
