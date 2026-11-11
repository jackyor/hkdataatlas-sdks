from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsStructuralsymbolsAttributes")


@_attrs_define
class WfsMapServerWfsStructuralsymbolsAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        stru_type (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        rotation (float | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into all
            JSON queries.
        dip_angle (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    stru_type: str | Unset = UNSET
    rotation: float | Unset = UNSET
    dip_angle: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        stru_type = self.stru_type

        rotation = self.rotation

        dip_angle = self.dip_angle

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
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

        shape = d.pop("Shape", UNSET)

        stru_type = d.pop("Stru_Type", UNSET)

        rotation = d.pop("Rotation", UNSET)

        dip_angle = d.pop("Dip_Angle", UNSET)

        wfs_map_server_wfs_structuralsymbols_attributes = cls(
            objectid=objectid,
            shape=shape,
            stru_type=stru_type,
            rotation=rotation,
            dip_angle=dip_angle,
        )

        wfs_map_server_wfs_structuralsymbols_attributes.additional_properties = d
        return wfs_map_server_wfs_structuralsymbols_attributes

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
