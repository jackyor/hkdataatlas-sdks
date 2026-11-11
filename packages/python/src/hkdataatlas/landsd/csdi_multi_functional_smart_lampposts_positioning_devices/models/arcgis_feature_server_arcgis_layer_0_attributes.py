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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        lp_num (None | str | Unset): Publisher field type: esriFieldTypeString
        lp_north (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lp_east (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lp_gl (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lp_lat (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lp_long (float | None | Unset): Publisher field type: esriFieldTypeDouble
        gm2_hgt (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    lp_num: None | str | Unset = UNSET
    lp_north: float | None | Unset = UNSET
    lp_east: float | None | Unset = UNSET
    lp_gl: float | None | Unset = UNSET
    lp_lat: float | None | Unset = UNSET
    lp_long: float | None | Unset = UNSET
    gm2_hgt: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        lp_num: None | str | Unset
        if isinstance(self.lp_num, Unset):
            lp_num = UNSET
        else:
            lp_num = self.lp_num

        lp_north: float | None | Unset
        if isinstance(self.lp_north, Unset):
            lp_north = UNSET
        else:
            lp_north = self.lp_north

        lp_east: float | None | Unset
        if isinstance(self.lp_east, Unset):
            lp_east = UNSET
        else:
            lp_east = self.lp_east

        lp_gl: float | None | Unset
        if isinstance(self.lp_gl, Unset):
            lp_gl = UNSET
        else:
            lp_gl = self.lp_gl

        lp_lat: float | None | Unset
        if isinstance(self.lp_lat, Unset):
            lp_lat = UNSET
        else:
            lp_lat = self.lp_lat

        lp_long: float | None | Unset
        if isinstance(self.lp_long, Unset):
            lp_long = UNSET
        else:
            lp_long = self.lp_long

        gm2_hgt: float | None | Unset
        if isinstance(self.gm2_hgt, Unset):
            gm2_hgt = UNSET
        else:
            gm2_hgt = self.gm2_hgt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if lp_num is not UNSET:
            field_dict["LP_NUM"] = lp_num
        if lp_north is not UNSET:
            field_dict["LP_NORTH"] = lp_north
        if lp_east is not UNSET:
            field_dict["LP_EAST"] = lp_east
        if lp_gl is not UNSET:
            field_dict["LP_GL"] = lp_gl
        if lp_lat is not UNSET:
            field_dict["LP_LAT"] = lp_lat
        if lp_long is not UNSET:
            field_dict["LP_LONG"] = lp_long
        if gm2_hgt is not UNSET:
            field_dict["GM2_HGT"] = gm2_hgt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_lp_num(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lp_num = _parse_lp_num(d.pop("LP_NUM", UNSET))

        def _parse_lp_north(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lp_north = _parse_lp_north(d.pop("LP_NORTH", UNSET))

        def _parse_lp_east(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lp_east = _parse_lp_east(d.pop("LP_EAST", UNSET))

        def _parse_lp_gl(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lp_gl = _parse_lp_gl(d.pop("LP_GL", UNSET))

        def _parse_lp_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lp_lat = _parse_lp_lat(d.pop("LP_LAT", UNSET))

        def _parse_lp_long(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lp_long = _parse_lp_long(d.pop("LP_LONG", UNSET))

        def _parse_gm2_hgt(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gm2_hgt = _parse_gm2_hgt(d.pop("GM2_HGT", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            lp_num=lp_num,
            lp_north=lp_north,
            lp_east=lp_east,
            lp_gl=lp_gl,
            lp_lat=lp_lat,
            lp_long=lp_long,
            gm2_hgt=gm2_hgt,
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
