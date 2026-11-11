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
        a_station_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        a_station_c (None | str | Unset): Publisher field type: esriFieldTypeString
        a_station_cs (None | str | Unset): Publisher field type: esriFieldTypeString
        b_sampling_date (None | str | Unset): Publisher field type: esriFieldTypeString
        c_dissolved_oxygen_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        c_dissolved_oxygen_c (None | str | Unset): Publisher field type: esriFieldTypeString
        c_dissolved_oxygen_cs (None | str | Unset): Publisher field type: esriFieldTypeString
        c_bod5_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        c_bod5_c (None | str | Unset): Publisher field type: esriFieldTypeString
        c_bod5_cs (None | str | Unset): Publisher field type: esriFieldTypeString
        d_link_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        d_link_c (None | str | Unset): Publisher field type: esriFieldTypeString
        d_link_cs (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    a_station: None | str | Unset = UNSET
    a_station_eng: None | str | Unset = UNSET
    a_station_c: None | str | Unset = UNSET
    a_station_cs: None | str | Unset = UNSET
    b_sampling_date: None | str | Unset = UNSET
    c_dissolved_oxygen_eng: None | str | Unset = UNSET
    c_dissolved_oxygen_c: None | str | Unset = UNSET
    c_dissolved_oxygen_cs: None | str | Unset = UNSET
    c_bod5_eng: None | str | Unset = UNSET
    c_bod5_c: None | str | Unset = UNSET
    c_bod5_cs: None | str | Unset = UNSET
    d_link_eng: None | str | Unset = UNSET
    d_link_c: None | str | Unset = UNSET
    d_link_cs: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        a_station: None | str | Unset
        if isinstance(self.a_station, Unset):
            a_station = UNSET
        else:
            a_station = self.a_station

        a_station_eng: None | str | Unset
        if isinstance(self.a_station_eng, Unset):
            a_station_eng = UNSET
        else:
            a_station_eng = self.a_station_eng

        a_station_c: None | str | Unset
        if isinstance(self.a_station_c, Unset):
            a_station_c = UNSET
        else:
            a_station_c = self.a_station_c

        a_station_cs: None | str | Unset
        if isinstance(self.a_station_cs, Unset):
            a_station_cs = UNSET
        else:
            a_station_cs = self.a_station_cs

        b_sampling_date: None | str | Unset
        if isinstance(self.b_sampling_date, Unset):
            b_sampling_date = UNSET
        else:
            b_sampling_date = self.b_sampling_date

        c_dissolved_oxygen_eng: None | str | Unset
        if isinstance(self.c_dissolved_oxygen_eng, Unset):
            c_dissolved_oxygen_eng = UNSET
        else:
            c_dissolved_oxygen_eng = self.c_dissolved_oxygen_eng

        c_dissolved_oxygen_c: None | str | Unset
        if isinstance(self.c_dissolved_oxygen_c, Unset):
            c_dissolved_oxygen_c = UNSET
        else:
            c_dissolved_oxygen_c = self.c_dissolved_oxygen_c

        c_dissolved_oxygen_cs: None | str | Unset
        if isinstance(self.c_dissolved_oxygen_cs, Unset):
            c_dissolved_oxygen_cs = UNSET
        else:
            c_dissolved_oxygen_cs = self.c_dissolved_oxygen_cs

        c_bod5_eng: None | str | Unset
        if isinstance(self.c_bod5_eng, Unset):
            c_bod5_eng = UNSET
        else:
            c_bod5_eng = self.c_bod5_eng

        c_bod5_c: None | str | Unset
        if isinstance(self.c_bod5_c, Unset):
            c_bod5_c = UNSET
        else:
            c_bod5_c = self.c_bod5_c

        c_bod5_cs: None | str | Unset
        if isinstance(self.c_bod5_cs, Unset):
            c_bod5_cs = UNSET
        else:
            c_bod5_cs = self.c_bod5_cs

        d_link_eng: None | str | Unset
        if isinstance(self.d_link_eng, Unset):
            d_link_eng = UNSET
        else:
            d_link_eng = self.d_link_eng

        d_link_c: None | str | Unset
        if isinstance(self.d_link_c, Unset):
            d_link_c = UNSET
        else:
            d_link_c = self.d_link_c

        d_link_cs: None | str | Unset
        if isinstance(self.d_link_cs, Unset):
            d_link_cs = UNSET
        else:
            d_link_cs = self.d_link_cs

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if a_station is not UNSET:
            field_dict["A_Station"] = a_station
        if a_station_eng is not UNSET:
            field_dict["A_Station_Eng"] = a_station_eng
        if a_station_c is not UNSET:
            field_dict["A_Station_C"] = a_station_c
        if a_station_cs is not UNSET:
            field_dict["A_Station_Cs"] = a_station_cs
        if b_sampling_date is not UNSET:
            field_dict["B_Sampling_Date"] = b_sampling_date
        if c_dissolved_oxygen_eng is not UNSET:
            field_dict["C_Dissolved_Oxygen_Eng"] = c_dissolved_oxygen_eng
        if c_dissolved_oxygen_c is not UNSET:
            field_dict["C_Dissolved_Oxygen_C"] = c_dissolved_oxygen_c
        if c_dissolved_oxygen_cs is not UNSET:
            field_dict["C_Dissolved_Oxygen_Cs"] = c_dissolved_oxygen_cs
        if c_bod5_eng is not UNSET:
            field_dict["C_BOD5_Eng"] = c_bod5_eng
        if c_bod5_c is not UNSET:
            field_dict["C_BOD5_C"] = c_bod5_c
        if c_bod5_cs is not UNSET:
            field_dict["C_BOD5_Cs"] = c_bod5_cs
        if d_link_eng is not UNSET:
            field_dict["D_Link_Eng"] = d_link_eng
        if d_link_c is not UNSET:
            field_dict["D_Link_C"] = d_link_c
        if d_link_cs is not UNSET:
            field_dict["D_Link_Cs"] = d_link_cs
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
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

        def _parse_a_station_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        a_station_eng = _parse_a_station_eng(d.pop("A_Station_Eng", UNSET))

        def _parse_a_station_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        a_station_c = _parse_a_station_c(d.pop("A_Station_C", UNSET))

        def _parse_a_station_cs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        a_station_cs = _parse_a_station_cs(d.pop("A_Station_Cs", UNSET))

        def _parse_b_sampling_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        b_sampling_date = _parse_b_sampling_date(d.pop("B_Sampling_Date", UNSET))

        def _parse_c_dissolved_oxygen_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c_dissolved_oxygen_eng = _parse_c_dissolved_oxygen_eng(
            d.pop("C_Dissolved_Oxygen_Eng", UNSET)
        )

        def _parse_c_dissolved_oxygen_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c_dissolved_oxygen_c = _parse_c_dissolved_oxygen_c(
            d.pop("C_Dissolved_Oxygen_C", UNSET)
        )

        def _parse_c_dissolved_oxygen_cs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c_dissolved_oxygen_cs = _parse_c_dissolved_oxygen_cs(
            d.pop("C_Dissolved_Oxygen_Cs", UNSET)
        )

        def _parse_c_bod5_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c_bod5_eng = _parse_c_bod5_eng(d.pop("C_BOD5_Eng", UNSET))

        def _parse_c_bod5_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c_bod5_c = _parse_c_bod5_c(d.pop("C_BOD5_C", UNSET))

        def _parse_c_bod5_cs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        c_bod5_cs = _parse_c_bod5_cs(d.pop("C_BOD5_Cs", UNSET))

        def _parse_d_link_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_link_eng = _parse_d_link_eng(d.pop("D_Link_Eng", UNSET))

        def _parse_d_link_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_link_c = _parse_d_link_c(d.pop("D_Link_C", UNSET))

        def _parse_d_link_cs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_link_cs = _parse_d_link_cs(d.pop("D_Link_Cs", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            a_station=a_station,
            a_station_eng=a_station_eng,
            a_station_c=a_station_c,
            a_station_cs=a_station_cs,
            b_sampling_date=b_sampling_date,
            c_dissolved_oxygen_eng=c_dissolved_oxygen_eng,
            c_dissolved_oxygen_c=c_dissolved_oxygen_c,
            c_dissolved_oxygen_cs=c_dissolved_oxygen_cs,
            c_bod5_eng=c_bod5_eng,
            c_bod5_c=c_bod5_c,
            c_bod5_cs=c_bod5_cs,
            d_link_eng=d_link_eng,
            d_link_c=d_link_c,
            d_link_cs=d_link_cs,
            longitude=longitude,
            latitude=latitude,
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
