from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer8Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer8Attributes:
    """
    Attributes:
        rotation (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dip_angle (None | str | Unset): Publisher field type: esriFieldTypeString
        stru_type (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    rotation: float | None | Unset = UNSET
    dip_angle: None | str | Unset = UNSET
    stru_type: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rotation: float | None | Unset
        if isinstance(self.rotation, Unset):
            rotation = UNSET
        else:
            rotation = self.rotation

        dip_angle: None | str | Unset
        if isinstance(self.dip_angle, Unset):
            dip_angle = UNSET
        else:
            dip_angle = self.dip_angle

        stru_type: None | str | Unset
        if isinstance(self.stru_type, Unset):
            stru_type = UNSET
        else:
            stru_type = self.stru_type

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rotation is not UNSET:
            field_dict["Rotation"] = rotation
        if dip_angle is not UNSET:
            field_dict["Dip_Angle"] = dip_angle
        if stru_type is not UNSET:
            field_dict["Stru_Type"] = stru_type
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_rotation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rotation = _parse_rotation(d.pop("Rotation", UNSET))

        def _parse_dip_angle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dip_angle = _parse_dip_angle(d.pop("Dip_Angle", UNSET))

        def _parse_stru_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stru_type = _parse_stru_type(d.pop("Stru_Type", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_8_attributes = cls(
            rotation=rotation,
            dip_angle=dip_angle,
            stru_type=stru_type,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_8_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_8_attributes

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
