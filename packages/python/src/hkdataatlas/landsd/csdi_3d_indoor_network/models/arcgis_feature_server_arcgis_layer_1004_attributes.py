from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1004Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1004Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        pedestrian_route_id (int | Unset): Publisher field type: esriFieldTypeInteger
        distance_post_1 (str | Unset): Publisher field type: esriFieldTypeString
        distance_post_2 (str | Unset): Publisher field type: esriFieldTypeString
        alias_name_tc (str | Unset): Publisher field type: esriFieldTypeString
        alias_name_en (str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    pedestrian_route_id: int | Unset = UNSET
    distance_post_1: str | Unset = UNSET
    distance_post_2: str | Unset = UNSET
    alias_name_tc: str | Unset = UNSET
    alias_name_en: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        pedestrian_route_id = self.pedestrian_route_id

        distance_post_1 = self.distance_post_1

        distance_post_2 = self.distance_post_2

        alias_name_tc = self.alias_name_tc

        alias_name_en = self.alias_name_en

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if pedestrian_route_id is not UNSET:
            field_dict["PedestrianRouteID"] = pedestrian_route_id
        if distance_post_1 is not UNSET:
            field_dict["DistancePost1"] = distance_post_1
        if distance_post_2 is not UNSET:
            field_dict["DistancePost2"] = distance_post_2
        if alias_name_tc is not UNSET:
            field_dict["AliasNameTC"] = alias_name_tc
        if alias_name_en is not UNSET:
            field_dict["AliasNameEN"] = alias_name_en

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        pedestrian_route_id = d.pop("PedestrianRouteID", UNSET)

        distance_post_1 = d.pop("DistancePost1", UNSET)

        distance_post_2 = d.pop("DistancePost2", UNSET)

        alias_name_tc = d.pop("AliasNameTC", UNSET)

        alias_name_en = d.pop("AliasNameEN", UNSET)

        arcgis_feature_server_arcgis_layer_1004_attributes = cls(
            objectid=objectid,
            pedestrian_route_id=pedestrian_route_id,
            distance_post_1=distance_post_1,
            distance_post_2=distance_post_2,
            alias_name_tc=alias_name_tc,
            alias_name_en=alias_name_en,
        )

        arcgis_feature_server_arcgis_layer_1004_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1004_attributes

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
