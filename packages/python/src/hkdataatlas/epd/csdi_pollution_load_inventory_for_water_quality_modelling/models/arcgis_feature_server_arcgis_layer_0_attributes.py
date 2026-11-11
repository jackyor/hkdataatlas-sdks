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
        gmid (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        load (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pollution_load_type (None | str | Unset): Publisher field type: esriFieldTypeString
        wqp (None | str | Unset): Publisher field type: esriFieldTypeString
        wqpv_2021 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        wqpv_2041 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    gmid: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    load: None | str | Unset = UNSET
    longitude: float | None | Unset = UNSET
    pollution_load_type: None | str | Unset = UNSET
    wqp: None | str | Unset = UNSET
    wqpv_2021: float | None | Unset = UNSET
    wqpv_2041: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gmid: float | None | Unset
        if isinstance(self.gmid, Unset):
            gmid = UNSET
        else:
            gmid = self.gmid

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        load: None | str | Unset
        if isinstance(self.load, Unset):
            load = UNSET
        else:
            load = self.load

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        pollution_load_type: None | str | Unset
        if isinstance(self.pollution_load_type, Unset):
            pollution_load_type = UNSET
        else:
            pollution_load_type = self.pollution_load_type

        wqp: None | str | Unset
        if isinstance(self.wqp, Unset):
            wqp = UNSET
        else:
            wqp = self.wqp

        wqpv_2021: float | None | Unset
        if isinstance(self.wqpv_2021, Unset):
            wqpv_2021 = UNSET
        else:
            wqpv_2021 = self.wqpv_2021

        wqpv_2041: float | None | Unset
        if isinstance(self.wqpv_2041, Unset):
            wqpv_2041 = UNSET
        else:
            wqpv_2041 = self.wqpv_2041

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gmid is not UNSET:
            field_dict["GMID"] = gmid
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if load is not UNSET:
            field_dict["load"] = load
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if pollution_load_type is not UNSET:
            field_dict["pollution_load_type"] = pollution_load_type
        if wqp is not UNSET:
            field_dict["wqp"] = wqp
        if wqpv_2021 is not UNSET:
            field_dict["wqpv_2021"] = wqpv_2021
        if wqpv_2041 is not UNSET:
            field_dict["wqpv_2041"] = wqpv_2041
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_gmid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gmid = _parse_gmid(d.pop("GMID", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_load(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        load = _parse_load(d.pop("load", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_pollution_load_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pollution_load_type = _parse_pollution_load_type(
            d.pop("pollution_load_type", UNSET)
        )

        def _parse_wqp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wqp = _parse_wqp(d.pop("wqp", UNSET))

        def _parse_wqpv_2021(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wqpv_2021 = _parse_wqpv_2021(d.pop("wqpv_2021", UNSET))

        def _parse_wqpv_2041(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        wqpv_2041 = _parse_wqpv_2041(d.pop("wqpv_2041", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            gmid=gmid,
            latitude=latitude,
            load=load,
            longitude=longitude,
            pollution_load_type=pollution_load_type,
            wqp=wqp,
            wqpv_2021=wqpv_2021,
            wqpv_2041=wqpv_2041,
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
