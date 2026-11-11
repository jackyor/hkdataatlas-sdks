from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_hiking_trails_hiking_trails_ext_gdb_attributes import (
        WfsMapServerWfsHikingTrailsHikingTrailsExtGDBAttributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (WfsMapServerWfsHikingTrailsHikingTrailsExtGDBAttributes | Unset):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: WfsMapServerWfsHikingTrailsHikingTrailsExtGDBAttributes | Unset = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        geometry = self.geometry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if properties is not UNSET:
            field_dict["properties"] = properties
        if geometry is not UNSET:
            field_dict["geometry"] = geometry

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wfs_map_server_wfs_hiking_trails_hiking_trails_ext_gdb_attributes import (
            WfsMapServerWfsHikingTrailsHikingTrailsExtGDBAttributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: WfsMapServerWfsHikingTrailsHikingTrailsExtGDBAttributes | Unset
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = (
                WfsMapServerWfsHikingTrailsHikingTrailsExtGDBAttributes.from_dict(
                    _properties
                )
            )

        geometry = d.pop("geometry", UNSET)

        wfs_map_server_wfs_feature_collection_features_item = cls(
            type_=type_,
            properties=properties,
            geometry=geometry,
        )

        wfs_map_server_wfs_feature_collection_features_item.additional_properties = d
        return wfs_map_server_wfs_feature_collection_features_item

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
