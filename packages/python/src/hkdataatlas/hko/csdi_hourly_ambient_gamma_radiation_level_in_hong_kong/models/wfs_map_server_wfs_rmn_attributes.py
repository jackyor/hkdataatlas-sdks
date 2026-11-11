from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsRMNAttributes")


@_attrs_define
class WfsMapServerWfsRMNAttributes:
    """
    Attributes:
        latest_hourly_mean_ambient_gamma_radiation_rate_url (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        station_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        station_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        station_name_uc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    latest_hourly_mean_ambient_gamma_radiation_rate_url: None | str | Unset = UNSET
    station_name_en: None | str | Unset = UNSET
    station_name_sc: None | str | Unset = UNSET
    station_name_uc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latest_hourly_mean_ambient_gamma_radiation_rate_url: None | str | Unset
        if isinstance(self.latest_hourly_mean_ambient_gamma_radiation_rate_url, Unset):
            latest_hourly_mean_ambient_gamma_radiation_rate_url = UNSET
        else:
            latest_hourly_mean_ambient_gamma_radiation_rate_url = (
                self.latest_hourly_mean_ambient_gamma_radiation_rate_url
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

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_hourly_mean_ambient_gamma_radiation_rate_url is not UNSET:
            field_dict["LatestHourlyMeanAmbientGammaRadiationRate_url"] = (
                latest_hourly_mean_ambient_gamma_radiation_rate_url
            )
        if station_name_en is not UNSET:
            field_dict["StationName_en"] = station_name_en
        if station_name_sc is not UNSET:
            field_dict["StationName_sc"] = station_name_sc
        if station_name_uc is not UNSET:
            field_dict["StationName_uc"] = station_name_uc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_latest_hourly_mean_ambient_gamma_radiation_rate_url(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_hourly_mean_ambient_gamma_radiation_rate_url = (
            _parse_latest_hourly_mean_ambient_gamma_radiation_rate_url(
                d.pop("LatestHourlyMeanAmbientGammaRadiationRate_url", UNSET)
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

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_rmn_attributes = cls(
            latest_hourly_mean_ambient_gamma_radiation_rate_url=latest_hourly_mean_ambient_gamma_radiation_rate_url,
            station_name_en=station_name_en,
            station_name_sc=station_name_sc,
            station_name_uc=station_name_uc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_rmn_attributes.additional_properties = d
        return wfs_map_server_wfs_rmn_attributes

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
