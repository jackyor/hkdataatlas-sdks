from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsMiscsymbolsAttributes")


@_attrs_define
class WfsMapServerWfsMiscsymbolsAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        pt_type (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        rotation (float | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into all
            JSON queries.
        pt_label (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    pt_type: str | Unset = UNSET
    rotation: float | Unset = UNSET
    pt_label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        pt_type = self.pt_type

        rotation = self.rotation

        pt_label = self.pt_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
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

        shape = d.pop("Shape", UNSET)

        pt_type = d.pop("Pt_Type", UNSET)

        rotation = d.pop("Rotation", UNSET)

        pt_label = d.pop("Pt_Label", UNSET)

        wfs_map_server_wfs_miscsymbols_attributes = cls(
            objectid=objectid,
            shape=shape,
            pt_type=pt_type,
            rotation=rotation,
            pt_label=pt_label,
        )

        wfs_map_server_wfs_miscsymbols_attributes.additional_properties = d
        return wfs_map_server_wfs_miscsymbols_attributes

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
