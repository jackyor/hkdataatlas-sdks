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
        comp_name (None | str | Unset): Publisher field type: esriFieldTypeString
        comp_name_chn (None | str | Unset): Publisher field type: esriFieldTypeString
        comp_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        open_addr1_chn (None | str | Unset): Publisher field type: esriFieldTypeString
        open_addr1_en (None | str | Unset): Publisher field type: esriFieldTypeString
        open_addr1_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        open_addr2_en (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    comp_name: None | str | Unset = UNSET
    comp_name_chn: None | str | Unset = UNSET
    comp_name_sc: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    open_addr1_chn: None | str | Unset = UNSET
    open_addr1_en: None | str | Unset = UNSET
    open_addr1_sc: None | str | Unset = UNSET
    open_addr2_en: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        comp_name: None | str | Unset
        if isinstance(self.comp_name, Unset):
            comp_name = UNSET
        else:
            comp_name = self.comp_name

        comp_name_chn: None | str | Unset
        if isinstance(self.comp_name_chn, Unset):
            comp_name_chn = UNSET
        else:
            comp_name_chn = self.comp_name_chn

        comp_name_sc: None | str | Unset
        if isinstance(self.comp_name_sc, Unset):
            comp_name_sc = UNSET
        else:
            comp_name_sc = self.comp_name_sc

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        open_addr1_chn: None | str | Unset
        if isinstance(self.open_addr1_chn, Unset):
            open_addr1_chn = UNSET
        else:
            open_addr1_chn = self.open_addr1_chn

        open_addr1_en: None | str | Unset
        if isinstance(self.open_addr1_en, Unset):
            open_addr1_en = UNSET
        else:
            open_addr1_en = self.open_addr1_en

        open_addr1_sc: None | str | Unset
        if isinstance(self.open_addr1_sc, Unset):
            open_addr1_sc = UNSET
        else:
            open_addr1_sc = self.open_addr1_sc

        open_addr2_en: None | str | Unset
        if isinstance(self.open_addr2_en, Unset):
            open_addr2_en = UNSET
        else:
            open_addr2_en = self.open_addr2_en

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comp_name is not UNSET:
            field_dict["comp_name"] = comp_name
        if comp_name_chn is not UNSET:
            field_dict["comp_name_chn"] = comp_name_chn
        if comp_name_sc is not UNSET:
            field_dict["comp_name_sc"] = comp_name_sc
        if easting is not UNSET:
            field_dict["easting"] = easting
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if northing is not UNSET:
            field_dict["northing"] = northing
        if open_addr1_chn is not UNSET:
            field_dict["open_addr1_chn"] = open_addr1_chn
        if open_addr1_en is not UNSET:
            field_dict["open_addr1_en"] = open_addr1_en
        if open_addr1_sc is not UNSET:
            field_dict["open_addr1_sc"] = open_addr1_sc
        if open_addr2_en is not UNSET:
            field_dict["open_addr2_en"] = open_addr2_en
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_comp_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp_name = _parse_comp_name(d.pop("comp_name", UNSET))

        def _parse_comp_name_chn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp_name_chn = _parse_comp_name_chn(d.pop("comp_name_chn", UNSET))

        def _parse_comp_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp_name_sc = _parse_comp_name_sc(d.pop("comp_name_sc", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("easting", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("northing", UNSET))

        def _parse_open_addr1_chn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_addr1_chn = _parse_open_addr1_chn(d.pop("open_addr1_chn", UNSET))

        def _parse_open_addr1_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_addr1_en = _parse_open_addr1_en(d.pop("open_addr1_en", UNSET))

        def _parse_open_addr1_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_addr1_sc = _parse_open_addr1_sc(d.pop("open_addr1_sc", UNSET))

        def _parse_open_addr2_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_addr2_en = _parse_open_addr2_en(d.pop("open_addr2_en", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            comp_name=comp_name,
            comp_name_chn=comp_name_chn,
            comp_name_sc=comp_name_sc,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            northing=northing,
            open_addr1_chn=open_addr1_chn,
            open_addr1_en=open_addr1_en,
            open_addr1_sc=open_addr1_sc,
            open_addr2_en=open_addr2_en,
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
