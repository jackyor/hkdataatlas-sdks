from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        geo_name_id (str | Unset): Publisher field type: esriFieldTypeString
        place_class (str | Unset): Publisher field type: esriFieldTypeString
        place_type (str | Unset): Publisher field type: esriFieldTypeString
        district (str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    geo_name_id: str | Unset = UNSET
    place_class: str | Unset = UNSET
    place_type: str | Unset = UNSET
    district: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        geo_name_id = self.geo_name_id

        place_class = self.place_class

        place_type = self.place_type

        district = self.district

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if geo_name_id is not UNSET:
            field_dict["GEO_NAME_ID"] = geo_name_id
        if place_class is not UNSET:
            field_dict["PLACE_CLASS"] = place_class
        if place_type is not UNSET:
            field_dict["PLACE_TYPE"] = place_type
        if district is not UNSET:
            field_dict["DISTRICT"] = district

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        geo_name_id = d.pop("GEO_NAME_ID", UNSET)

        place_class = d.pop("PLACE_CLASS", UNSET)

        place_type = d.pop("PLACE_TYPE", UNSET)

        district = d.pop("DISTRICT", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            geo_name_id=geo_name_id,
            place_class=place_class,
            place_type=place_type,
            district=district,
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
