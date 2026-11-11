from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1007Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1007Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        code (str | Unset): Publisher field type: esriFieldTypeString
        description (str | Unset): Publisher field type: esriFieldTypeString
        lr_area (str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    code: str | Unset = UNSET
    description: str | Unset = UNSET
    lr_area: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        code = self.code

        description = self.description

        lr_area = self.lr_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if code is not UNSET:
            field_dict["Code"] = code
        if description is not UNSET:
            field_dict["Description"] = description
        if lr_area is not UNSET:
            field_dict["LRArea"] = lr_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        code = d.pop("Code", UNSET)

        description = d.pop("Description", UNSET)

        lr_area = d.pop("LRArea", UNSET)

        arcgis_feature_server_arcgis_layer_1007_attributes = cls(
            objectid=objectid,
            code=code,
            description=description,
            lr_area=lr_area,
        )

        arcgis_feature_server_arcgis_layer_1007_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1007_attributes

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
