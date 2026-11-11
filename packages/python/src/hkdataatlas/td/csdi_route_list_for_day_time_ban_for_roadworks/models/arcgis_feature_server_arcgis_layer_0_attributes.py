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
        road_route_id (int | Unset): Publisher field type: esriFieldTypeInteger
        c_route_id (int | Unset): Publisher field type: esriFieldTypeInteger
        c_route_type (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        last_upd_date_g (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    road_route_id: int | Unset = UNSET
    c_route_id: int | Unset = UNSET
    c_route_type: int | None | Unset = UNSET
    last_upd_date_g: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        road_route_id = self.road_route_id

        c_route_id = self.c_route_id

        c_route_type: int | None | Unset
        if isinstance(self.c_route_type, Unset):
            c_route_type = UNSET
        else:
            c_route_type = self.c_route_type

        last_upd_date_g = self.last_upd_date_g

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if road_route_id is not UNSET:
            field_dict["ROAD_ROUTE_ID"] = road_route_id
        if c_route_id is not UNSET:
            field_dict["C_ROUTE_ID"] = c_route_id
        if c_route_type is not UNSET:
            field_dict["C_ROUTE_TYPE"] = c_route_type
        if last_upd_date_g is not UNSET:
            field_dict["LAST_UPD_DATE_G"] = last_upd_date_g
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        road_route_id = d.pop("ROAD_ROUTE_ID", UNSET)

        c_route_id = d.pop("C_ROUTE_ID", UNSET)

        def _parse_c_route_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        c_route_type = _parse_c_route_type(d.pop("C_ROUTE_TYPE", UNSET))

        last_upd_date_g = d.pop("LAST_UPD_DATE_G", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            road_route_id=road_route_id,
            c_route_id=c_route_id,
            c_route_type=c_route_type,
            last_upd_date_g=last_upd_date_g,
            shape_length=shape_length,
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
