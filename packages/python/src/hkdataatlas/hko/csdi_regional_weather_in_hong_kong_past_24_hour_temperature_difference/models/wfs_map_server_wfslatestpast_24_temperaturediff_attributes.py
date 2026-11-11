from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfslatestpast24TemperaturediffAttributes")


@_attrs_define
class WfsMapServerWfslatestpast24TemperaturediffAttributes:
    """
    Attributes:
        automatic_weather_station_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        automatic_weather_station_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        automatic_weather_station_uc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        data_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    automatic_weather_station_en: None | str | Unset = UNSET
    automatic_weather_station_sc: None | str | Unset = UNSET
    automatic_weather_station_uc: None | str | Unset = UNSET
    data_url: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automatic_weather_station_en: None | str | Unset
        if isinstance(self.automatic_weather_station_en, Unset):
            automatic_weather_station_en = UNSET
        else:
            automatic_weather_station_en = self.automatic_weather_station_en

        automatic_weather_station_sc: None | str | Unset
        if isinstance(self.automatic_weather_station_sc, Unset):
            automatic_weather_station_sc = UNSET
        else:
            automatic_weather_station_sc = self.automatic_weather_station_sc

        automatic_weather_station_uc: None | str | Unset
        if isinstance(self.automatic_weather_station_uc, Unset):
            automatic_weather_station_uc = UNSET
        else:
            automatic_weather_station_uc = self.automatic_weather_station_uc

        data_url: None | str | Unset
        if isinstance(self.data_url, Unset):
            data_url = UNSET
        else:
            data_url = self.data_url

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if automatic_weather_station_en is not UNSET:
            field_dict["AutomaticWeatherStation_en"] = automatic_weather_station_en
        if automatic_weather_station_sc is not UNSET:
            field_dict["AutomaticWeatherStation_sc"] = automatic_weather_station_sc
        if automatic_weather_station_uc is not UNSET:
            field_dict["AutomaticWeatherStation_uc"] = automatic_weather_station_uc
        if data_url is not UNSET:
            field_dict["Data_url"] = data_url
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_automatic_weather_station_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        automatic_weather_station_en = _parse_automatic_weather_station_en(
            d.pop("AutomaticWeatherStation_en", UNSET)
        )

        def _parse_automatic_weather_station_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        automatic_weather_station_sc = _parse_automatic_weather_station_sc(
            d.pop("AutomaticWeatherStation_sc", UNSET)
        )

        def _parse_automatic_weather_station_uc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        automatic_weather_station_uc = _parse_automatic_weather_station_uc(
            d.pop("AutomaticWeatherStation_uc", UNSET)
        )

        def _parse_data_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_url = _parse_data_url(d.pop("Data_url", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfslatestpast_24_temperaturediff_attributes = cls(
            automatic_weather_station_en=automatic_weather_station_en,
            automatic_weather_station_sc=automatic_weather_station_sc,
            automatic_weather_station_uc=automatic_weather_station_uc,
            data_url=data_url,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfslatestpast_24_temperaturediff_attributes.additional_properties = d
        return wfs_map_server_wfslatestpast_24_temperaturediff_attributes

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
