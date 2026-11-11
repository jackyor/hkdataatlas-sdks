from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1Attributes:
    """
    Attributes:
        weather_station_en (None | str | Unset): Publisher field type: esriFieldTypeString
        weather_station_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        weather_station_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        url (None | str | Unset): Publisher field type: esriFieldTypeString
        fid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    weather_station_en: None | str | Unset = UNSET
    weather_station_tc: None | str | Unset = UNSET
    weather_station_sc: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weather_station_en: None | str | Unset
        if isinstance(self.weather_station_en, Unset):
            weather_station_en = UNSET
        else:
            weather_station_en = self.weather_station_en

        weather_station_tc: None | str | Unset
        if isinstance(self.weather_station_tc, Unset):
            weather_station_tc = UNSET
        else:
            weather_station_tc = self.weather_station_tc

        weather_station_sc: None | str | Unset
        if isinstance(self.weather_station_sc, Unset):
            weather_station_sc = UNSET
        else:
            weather_station_sc = self.weather_station_sc

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weather_station_en is not UNSET:
            field_dict["weather_station_en"] = weather_station_en
        if weather_station_tc is not UNSET:
            field_dict["weather_station_tc"] = weather_station_tc
        if weather_station_sc is not UNSET:
            field_dict["weather_station_sc"] = weather_station_sc
        if url is not UNSET:
            field_dict["url"] = url
        if fid is not UNSET:
            field_dict["fid"] = fid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_weather_station_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weather_station_en = _parse_weather_station_en(
            d.pop("weather_station_en", UNSET)
        )

        def _parse_weather_station_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weather_station_tc = _parse_weather_station_tc(
            d.pop("weather_station_tc", UNSET)
        )

        def _parse_weather_station_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weather_station_sc = _parse_weather_station_sc(
            d.pop("weather_station_sc", UNSET)
        )

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            weather_station_en=weather_station_en,
            weather_station_tc=weather_station_tc,
            weather_station_sc=weather_station_sc,
            url=url,
            fid=fid,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_1_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1_attributes

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
