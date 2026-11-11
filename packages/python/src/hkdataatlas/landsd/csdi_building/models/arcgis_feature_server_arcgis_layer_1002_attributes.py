from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1002Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1002Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        building_csuid (str | Unset): Publisher field type: esriFieldTypeString
        building_structure_id (int | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    building_csuid: str | Unset = UNSET
    building_structure_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        building_csuid = self.building_csuid

        building_structure_id = self.building_structure_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if building_csuid is not UNSET:
            field_dict["BuildingCSUID"] = building_csuid
        if building_structure_id is not UNSET:
            field_dict["BuildingStructureID"] = building_structure_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        building_csuid = d.pop("BuildingCSUID", UNSET)

        building_structure_id = d.pop("BuildingStructureID", UNSET)

        arcgis_feature_server_arcgis_layer_1002_attributes = cls(
            objectid=objectid,
            building_csuid=building_csuid,
            building_structure_id=building_structure_id,
        )

        arcgis_feature_server_arcgis_layer_1002_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1002_attributes

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
