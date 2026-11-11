from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer2Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer2Attributes:
    """
    Attributes:
        f_type (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    f_type: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        f_type: None | str | Unset
        if isinstance(self.f_type, Unset):
            f_type = UNSET
        else:
            f_type = self.f_type

        objectid = self.objectid

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if f_type is not UNSET:
            field_dict["F_Type"] = f_type
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_f_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        f_type = _parse_f_type(d.pop("F_Type", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_2_attributes = cls(
            f_type=f_type,
            objectid=objectid,
            shape_length=shape_length,
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
