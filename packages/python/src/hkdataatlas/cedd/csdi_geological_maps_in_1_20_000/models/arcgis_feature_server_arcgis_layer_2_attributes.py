from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer2Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer2Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        stru_type (str | Unset): Publisher field type: esriFieldTypeString
        rotation (float | Unset): Publisher field type: esriFieldTypeDouble
        dip_angle (str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    stru_type: str | Unset = UNSET
    rotation: float | Unset = UNSET
    dip_angle: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        stru_type = self.stru_type

        rotation = self.rotation

        dip_angle = self.dip_angle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if stru_type is not UNSET:
            field_dict["Stru_Type"] = stru_type
        if rotation is not UNSET:
            field_dict["Rotation"] = rotation
        if dip_angle is not UNSET:
            field_dict["Dip_Angle"] = dip_angle

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        stru_type = d.pop("Stru_Type", UNSET)

        rotation = d.pop("Rotation", UNSET)

        dip_angle = d.pop("Dip_Angle", UNSET)

        arcgis_feature_server_arcgis_layer_2_attributes = cls(
            objectid=objectid,
            stru_type=stru_type,
            rotation=rotation,
            dip_angle=dip_angle,
        )

        arcgis_feature_server_arcgis_layer_2_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_2_attributes

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
