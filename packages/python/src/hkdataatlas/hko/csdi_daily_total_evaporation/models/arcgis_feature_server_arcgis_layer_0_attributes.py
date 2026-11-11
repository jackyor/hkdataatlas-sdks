from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        daily_total_evaporation_all_year_url (None | str | Unset): Publisher field type: esriFieldTypeString
        daily_total_evaporation_current_year_url (None | str | Unset): Publisher field type: esriFieldTypeString
        weather_station_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        weather_station_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        weather_station_name_uc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    daily_total_evaporation_all_year_url: None | str | Unset = UNSET
    daily_total_evaporation_current_year_url: None | str | Unset = UNSET
    weather_station_name_en: None | str | Unset = UNSET
    weather_station_name_sc: None | str | Unset = UNSET
    weather_station_name_uc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_total_evaporation_all_year_url: None | str | Unset
        if isinstance(self.daily_total_evaporation_all_year_url, Unset):
            daily_total_evaporation_all_year_url = UNSET
        else:
            daily_total_evaporation_all_year_url = (
                self.daily_total_evaporation_all_year_url
            )

        daily_total_evaporation_current_year_url: None | str | Unset
        if isinstance(self.daily_total_evaporation_current_year_url, Unset):
            daily_total_evaporation_current_year_url = UNSET
        else:
            daily_total_evaporation_current_year_url = (
                self.daily_total_evaporation_current_year_url
            )

        weather_station_name_en: None | str | Unset
        if isinstance(self.weather_station_name_en, Unset):
            weather_station_name_en = UNSET
        else:
            weather_station_name_en = self.weather_station_name_en

        weather_station_name_sc: None | str | Unset
        if isinstance(self.weather_station_name_sc, Unset):
            weather_station_name_sc = UNSET
        else:
            weather_station_name_sc = self.weather_station_name_sc

        weather_station_name_uc: None | str | Unset
        if isinstance(self.weather_station_name_uc, Unset):
            weather_station_name_uc = UNSET
        else:
            weather_station_name_uc = self.weather_station_name_uc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_total_evaporation_all_year_url is not UNSET:
            field_dict["DailyTotalEvaporation_AllYear_url"] = (
                daily_total_evaporation_all_year_url
            )
        if daily_total_evaporation_current_year_url is not UNSET:
            field_dict["DailyTotalEvaporation_CurrentYear_url"] = (
                daily_total_evaporation_current_year_url
            )
        if weather_station_name_en is not UNSET:
            field_dict["WeatherStationName_en"] = weather_station_name_en
        if weather_station_name_sc is not UNSET:
            field_dict["WeatherStationName_sc"] = weather_station_name_sc
        if weather_station_name_uc is not UNSET:
            field_dict["WeatherStationName_uc"] = weather_station_name_uc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_daily_total_evaporation_all_year_url(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        daily_total_evaporation_all_year_url = (
            _parse_daily_total_evaporation_all_year_url(
                d.pop("DailyTotalEvaporation_AllYear_url", UNSET)
            )
        )

        def _parse_daily_total_evaporation_current_year_url(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        daily_total_evaporation_current_year_url = (
            _parse_daily_total_evaporation_current_year_url(
                d.pop("DailyTotalEvaporation_CurrentYear_url", UNSET)
            )
        )

        def _parse_weather_station_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weather_station_name_en = _parse_weather_station_name_en(
            d.pop("WeatherStationName_en", UNSET)
        )

        def _parse_weather_station_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weather_station_name_sc = _parse_weather_station_name_sc(
            d.pop("WeatherStationName_sc", UNSET)
        )

        def _parse_weather_station_name_uc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        weather_station_name_uc = _parse_weather_station_name_uc(
            d.pop("WeatherStationName_uc", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            daily_total_evaporation_all_year_url=daily_total_evaporation_all_year_url,
            daily_total_evaporation_current_year_url=daily_total_evaporation_current_year_url,
            weather_station_name_en=weather_station_name_en,
            weather_station_name_sc=weather_station_name_sc,
            weather_station_name_uc=weather_station_name_uc,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
