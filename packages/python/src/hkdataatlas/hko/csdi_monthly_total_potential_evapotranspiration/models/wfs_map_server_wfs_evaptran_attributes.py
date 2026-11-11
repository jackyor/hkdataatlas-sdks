from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsEVAPTRANAttributes")


@_attrs_define
class WfsMapServerWfsEVAPTRANAttributes:
    """
    Attributes:
        monthly_total_potential_evapotranspiration_all_year_url (None | str | Unset): Native XSD type . Requiredness is
            not projected from XML occurrence into all JSON queries.
        monthly_total_potential_evapotranspiration_current_year_url (None | str | Unset): Native XSD type . Requiredness
            is not projected from XML occurrence into all JSON queries.
        weather_station_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        weather_station_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        weather_station_name_uc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    monthly_total_potential_evapotranspiration_all_year_url: None | str | Unset = UNSET
    monthly_total_potential_evapotranspiration_current_year_url: None | str | Unset = (
        UNSET
    )
    weather_station_name_en: None | str | Unset = UNSET
    weather_station_name_sc: None | str | Unset = UNSET
    weather_station_name_uc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monthly_total_potential_evapotranspiration_all_year_url: None | str | Unset
        if isinstance(
            self.monthly_total_potential_evapotranspiration_all_year_url, Unset
        ):
            monthly_total_potential_evapotranspiration_all_year_url = UNSET
        else:
            monthly_total_potential_evapotranspiration_all_year_url = (
                self.monthly_total_potential_evapotranspiration_all_year_url
            )

        monthly_total_potential_evapotranspiration_current_year_url: None | str | Unset
        if isinstance(
            self.monthly_total_potential_evapotranspiration_current_year_url, Unset
        ):
            monthly_total_potential_evapotranspiration_current_year_url = UNSET
        else:
            monthly_total_potential_evapotranspiration_current_year_url = (
                self.monthly_total_potential_evapotranspiration_current_year_url
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

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monthly_total_potential_evapotranspiration_all_year_url is not UNSET:
            field_dict["MonthlyTotalPotentialEvapotranspiration_AllYear_url"] = (
                monthly_total_potential_evapotranspiration_all_year_url
            )
        if monthly_total_potential_evapotranspiration_current_year_url is not UNSET:
            field_dict["MonthlyTotalPotentialEvapotranspiration_CurrentYear_url"] = (
                monthly_total_potential_evapotranspiration_current_year_url
            )
        if weather_station_name_en is not UNSET:
            field_dict["WeatherStationName_en"] = weather_station_name_en
        if weather_station_name_sc is not UNSET:
            field_dict["WeatherStationName_sc"] = weather_station_name_sc
        if weather_station_name_uc is not UNSET:
            field_dict["WeatherStationName_uc"] = weather_station_name_uc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_monthly_total_potential_evapotranspiration_all_year_url(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        monthly_total_potential_evapotranspiration_all_year_url = (
            _parse_monthly_total_potential_evapotranspiration_all_year_url(
                d.pop("MonthlyTotalPotentialEvapotranspiration_AllYear_url", UNSET)
            )
        )

        def _parse_monthly_total_potential_evapotranspiration_current_year_url(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        monthly_total_potential_evapotranspiration_current_year_url = (
            _parse_monthly_total_potential_evapotranspiration_current_year_url(
                d.pop("MonthlyTotalPotentialEvapotranspiration_CurrentYear_url", UNSET)
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

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_evaptran_attributes = cls(
            monthly_total_potential_evapotranspiration_all_year_url=monthly_total_potential_evapotranspiration_all_year_url,
            monthly_total_potential_evapotranspiration_current_year_url=monthly_total_potential_evapotranspiration_current_year_url,
            weather_station_name_en=weather_station_name_en,
            weather_station_name_sc=weather_station_name_sc,
            weather_station_name_uc=weather_station_name_uc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_evaptran_attributes.additional_properties = d
        return wfs_map_server_wfs_evaptran_attributes

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
