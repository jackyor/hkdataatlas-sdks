from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        pt_type (str | Unset): Publisher field type: esriFieldTypeString
        rotation (float | Unset): Publisher field type: esriFieldTypeDouble
        pt_label (str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    pt_type: str | Unset = UNSET
    rotation: float | Unset = UNSET
    pt_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        pt_type = self.pt_type

        rotation = self.rotation

        pt_label = self.pt_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if pt_type is not UNSET:
            field_dict["Pt_Type"] = pt_type
        if rotation is not UNSET:
            field_dict["Rotation"] = rotation
        if pt_label is not UNSET:
            field_dict["Pt_Label"] = pt_label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        pt_type = d.pop("Pt_Type", UNSET)

        rotation = d.pop("Rotation", UNSET)

        pt_label = d.pop("Pt_Label", UNSET)

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            objectid=objectid,
            pt_type=pt_type,
            rotation=rotation,
            pt_label=pt_label,
        )

        arcgis_feature_server_arcgis_layer_1_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1_attributes

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
