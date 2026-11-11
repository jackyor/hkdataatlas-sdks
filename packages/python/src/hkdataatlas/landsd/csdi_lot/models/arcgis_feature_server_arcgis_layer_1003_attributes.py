from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1003Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1003Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        prn (str | Unset): Publisher field type: esriFieldTypeString
        memorial_no (str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    prn: str | Unset = UNSET
    memorial_no: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        prn = self.prn

        memorial_no = self.memorial_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if prn is not UNSET:
            field_dict["PRN"] = prn
        if memorial_no is not UNSET:
            field_dict["MemorialNo"] = memorial_no

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        prn = d.pop("PRN", UNSET)

        memorial_no = d.pop("MemorialNo", UNSET)

        arcgis_feature_server_arcgis_layer_1003_attributes = cls(
            objectid=objectid,
            prn=prn,
            memorial_no=memorial_no,
        )

        arcgis_feature_server_arcgis_layer_1003_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1003_attributes

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
