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
        a_station (None | str | Unset): Publisher field type: esriFieldTypeString
        b_station_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        b_station_c (None | str | Unset): Publisher field type: esriFieldTypeString
        b_station_cs (None | str | Unset): Publisher field type: esriFieldTypeString
        c_water_control_zone_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        c_water_control_zone_c (None | str | Unset): Publisher field type: esriFieldTypeString
        c_water_control_zone_cs (None | str | Unset): Publisher field type: esriFieldTypeString
        d_link_historical_marine_water_quality_data_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        d_link_historical_marine_water_quality_data_c (None | str | Unset): Publisher field type: esriFieldTypeString
        d_link_historical_marine_water_quality_data_cs (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    a_station: None | str | Unset = UNSET
    b_station_eng: None | str | Unset = UNSET
    b_station_c: None | str | Unset = UNSET
    b_station_cs: None | str | Unset = UNSET
    c_water_control_zone_eng: None | str | Unset = UNSET
    c_water_control_zone_c: None | str | Unset = UNSET
    c_water_control_zone_cs: None | str | Unset = UNSET
    d_link_historical_marine_water_quality_data_eng: None | str | Unset = UNSET
    d_link_historical_marine_water_quality_data_c: None | str | Unset = UNSET
    d_link_historical_marine_water_quality_data_cs: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a_station: None | str | Unset
        if isinstance(self.a_station, Unset):
            a_station = UNSET
        else:
            a_station = self.a_station

        b_station_eng: None | str | Unset
        if isinstance(self.b_station_eng, Unset):
            b_station_eng = UNSET
        else:
            b_station_eng = self.b_station_eng

        b_station_c: None | str | Unset
        if isinstance(self.b_station_c, Unset):
            b_station_c = UNSET
        else:
            b_station_c = self.b_station_c

        b_station_cs: None | str | Unset
        if isinstance(self.b_station_cs, Unset):
            b_station_cs = UNSET
        else:
            b_station_cs = self.b_station_cs

        c_water_control_zone_eng: None | str | Unset
        if isinstance(self.c_water_control_zone_eng, Unset):
            c_water_control_zone_eng = UNSET
        else:
            c_water_control_zone_eng = self.c_water_control_zone_eng

        c_water_control_zone_c: None | str | Unset
        if isinstance(self.c_water_control_zone_c, Unset):
            c_water_control_zone_c = UNSET
        else:
            c_water_control_zone_c = self.c_water_control_zone_c

        c_water_control_zone_cs: None | str | Unset
        if isinstance(self.c_water_control_zone_cs, Unset):
            c_water_control_zone_cs = UNSET
        else:
            c_water_control_zone_cs = self.c_water_control_zone_cs

        d_link_historical_marine_water_quality_data_eng: None | str | Unset
        if isinstance(self.d_link_historical_marine_water_quality_data_eng, Unset):
            d_link_historical_marine_water_quality_data_eng = UNSET
        else:
            d_link_historical_marine_water_quality_data_eng = (
                self.d_link_historical_marine_water_quality_data_eng
            )

        d_link_historical_marine_water_quality_data_c: None | str | Unset
        if isinstance(self.d_link_historical_marine_water_quality_data_c, Unset):
            d_link_historical_marine_water_quality_data_c = UNSET
        else:
            d_link_historical_marine_water_quality_data_c = (
                self.d_link_historical_marine_water_quality_data_c
            )

        d_link_historical_marine_water_quality_data_cs: None | str | Unset
        if isinstance(self.d_link_historical_marine_water_quality_data_cs, Unset):
            d_link_historical_marine_water_quality_data_cs = UNSET
        else:
            d_link_historical_marine_water_quality_data_cs = (
                self.d_link_historical_marine_water_quality_data_cs
            )

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a_station is not UNSET:
            field_dict["A_Station"] = a_station
        if b_station_eng is not UNSET:
            field_dict["B_Station_Eng"] = b_station_eng
        if b_station_c is not UNSET:
            field_dict["B_Station_C"] = b_station_c
        if b_station_cs is not UNSET:
            field_dict["B_Station_Cs"] = b_station_cs
        if c_water_control_zone_eng is not UNSET:
            field_dict["C_Water_Control_Zone_Eng"] = c_water_control_zone_eng
        if c_water_control_zone_c is not UNSET:
            field_dict["C_Water_Control_Zone_C"] = c_water_control_zone_c
        if c_water_control_zone_cs is not UNSET:
            field_dict["C_Water_Control_Zone_Cs"] = c_water_control_zone_cs
        if d_link_historical_marine_water_quality_data_eng is not UNSET:
            field_dict["D_Link_Historical_Marine_Water_Quality_Data_Eng"] = (
                d_link_historical_marine_water_quality_data_eng
            )
        if d_link_historical_marine_water_quality_data_c is not UNSET:
            field_dict["D_Link_Historical_Marine_Water_Quality_Data_C"] = (
                d_link_historical_marine_water_quality_data_c
            )
        if d_link_historical_marine_water_quality_data_cs is not UNSET:
            field_dict["D_Link_Historical_Marine_Water_Quality_Data_Cs"] = (
                d_link_historical_marine_water_quality_data_cs
            )
        if latitude is not UNSET:
            field_dict["LATITUDE"] = latitude
        if longitude is not UNSET:
            field_dict["LONGITUDE"] = longitude
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_a_station(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        a_station = _parse_a_station(d.pop("A_Station", UNSET))

        def _parse_b_station_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        b_station_eng = _parse_b_station_eng(d.pop("B_Station_Eng", UNSET))

        def _parse_b_station_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        b_station_c = _parse_b_station_c(d.pop("B_Station_C", UNSET))

        def _parse_b_station_cs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        b_station_cs = _parse_b_station_cs(d.pop("B_Station_Cs", UNSET))

        def _parse_c_water_control_zone_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c_water_control_zone_eng = _parse_c_water_control_zone_eng(
            d.pop("C_Water_Control_Zone_Eng", UNSET)
        )

        def _parse_c_water_control_zone_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c_water_control_zone_c = _parse_c_water_control_zone_c(
            d.pop("C_Water_Control_Zone_C", UNSET)
        )

        def _parse_c_water_control_zone_cs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c_water_control_zone_cs = _parse_c_water_control_zone_cs(
            d.pop("C_Water_Control_Zone_Cs", UNSET)
        )

        def _parse_d_link_historical_marine_water_quality_data_eng(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_link_historical_marine_water_quality_data_eng = (
            _parse_d_link_historical_marine_water_quality_data_eng(
                d.pop("D_Link_Historical_Marine_Water_Quality_Data_Eng", UNSET)
            )
        )

        def _parse_d_link_historical_marine_water_quality_data_c(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_link_historical_marine_water_quality_data_c = (
            _parse_d_link_historical_marine_water_quality_data_c(
                d.pop("D_Link_Historical_Marine_Water_Quality_Data_C", UNSET)
            )
        )

        def _parse_d_link_historical_marine_water_quality_data_cs(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_link_historical_marine_water_quality_data_cs = (
            _parse_d_link_historical_marine_water_quality_data_cs(
                d.pop("D_Link_Historical_Marine_Water_Quality_Data_Cs", UNSET)
            )
        )

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("LATITUDE", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("LONGITUDE", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            a_station=a_station,
            b_station_eng=b_station_eng,
            b_station_c=b_station_c,
            b_station_cs=b_station_cs,
            c_water_control_zone_eng=c_water_control_zone_eng,
            c_water_control_zone_c=c_water_control_zone_c,
            c_water_control_zone_cs=c_water_control_zone_cs,
            d_link_historical_marine_water_quality_data_eng=d_link_historical_marine_water_quality_data_eng,
            d_link_historical_marine_water_quality_data_c=d_link_historical_marine_water_quality_data_c,
            d_link_historical_marine_water_quality_data_cs=d_link_historical_marine_water_quality_data_cs,
            latitude=latitude,
            longitude=longitude,
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
