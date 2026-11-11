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
        daily_mean_sea_temp_all_year_url (None | str | Unset): Publisher field type: esriFieldTypeString
        daily_mean_sea_temp_current_year_url (None | str | Unset): Publisher field type: esriFieldTypeString
        station_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        station_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        station_name_uc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    daily_mean_sea_temp_all_year_url: None | str | Unset = UNSET
    daily_mean_sea_temp_current_year_url: None | str | Unset = UNSET
    station_name_en: None | str | Unset = UNSET
    station_name_sc: None | str | Unset = UNSET
    station_name_uc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_mean_sea_temp_all_year_url: None | str | Unset
        if isinstance(self.daily_mean_sea_temp_all_year_url, Unset):
            daily_mean_sea_temp_all_year_url = UNSET
        else:
            daily_mean_sea_temp_all_year_url = self.daily_mean_sea_temp_all_year_url

        daily_mean_sea_temp_current_year_url: None | str | Unset
        if isinstance(self.daily_mean_sea_temp_current_year_url, Unset):
            daily_mean_sea_temp_current_year_url = UNSET
        else:
            daily_mean_sea_temp_current_year_url = (
                self.daily_mean_sea_temp_current_year_url
            )

        station_name_en: None | str | Unset
        if isinstance(self.station_name_en, Unset):
            station_name_en = UNSET
        else:
            station_name_en = self.station_name_en

        station_name_sc: None | str | Unset
        if isinstance(self.station_name_sc, Unset):
            station_name_sc = UNSET
        else:
            station_name_sc = self.station_name_sc

        station_name_uc: None | str | Unset
        if isinstance(self.station_name_uc, Unset):
            station_name_uc = UNSET
        else:
            station_name_uc = self.station_name_uc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_mean_sea_temp_all_year_url is not UNSET:
            field_dict["DailyMeanSeaTemp_AllYear_url"] = (
                daily_mean_sea_temp_all_year_url
            )
        if daily_mean_sea_temp_current_year_url is not UNSET:
            field_dict["DailyMeanSeaTemp_CurrentYear_url"] = (
                daily_mean_sea_temp_current_year_url
            )
        if station_name_en is not UNSET:
            field_dict["StationName_en"] = station_name_en
        if station_name_sc is not UNSET:
            field_dict["StationName_sc"] = station_name_sc
        if station_name_uc is not UNSET:
            field_dict["StationName_uc"] = station_name_uc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_daily_mean_sea_temp_all_year_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        daily_mean_sea_temp_all_year_url = _parse_daily_mean_sea_temp_all_year_url(
            d.pop("DailyMeanSeaTemp_AllYear_url", UNSET)
        )

        def _parse_daily_mean_sea_temp_current_year_url(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        daily_mean_sea_temp_current_year_url = (
            _parse_daily_mean_sea_temp_current_year_url(
                d.pop("DailyMeanSeaTemp_CurrentYear_url", UNSET)
            )
        )

        def _parse_station_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        station_name_en = _parse_station_name_en(d.pop("StationName_en", UNSET))

        def _parse_station_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        station_name_sc = _parse_station_name_sc(d.pop("StationName_sc", UNSET))

        def _parse_station_name_uc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        station_name_uc = _parse_station_name_uc(d.pop("StationName_uc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            daily_mean_sea_temp_all_year_url=daily_mean_sea_temp_all_year_url,
            daily_mean_sea_temp_current_year_url=daily_mean_sea_temp_current_year_url,
            station_name_en=station_name_en,
            station_name_sc=station_name_sc,
            station_name_uc=station_name_uc,
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
