from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        fac_id (None | str | Unset): Publisher field type: esriFieldTypeString
        x_ground (float | None | Unset): Publisher field type: esriFieldTypeDouble
        y_ground (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    fac_id: None | str | Unset = UNSET
    x_ground: float | None | Unset = UNSET
    y_ground: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fac_id: None | str | Unset
        if isinstance(self.fac_id, Unset):
            fac_id = UNSET
        else:
            fac_id = self.fac_id

        x_ground: float | None | Unset
        if isinstance(self.x_ground, Unset):
            x_ground = UNSET
        else:
            x_ground = self.x_ground

        y_ground: float | None | Unset
        if isinstance(self.y_ground, Unset):
            y_ground = UNSET
        else:
            y_ground = self.y_ground

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fac_id is not UNSET:
            field_dict["FAC_ID"] = fac_id
        if x_ground is not UNSET:
            field_dict["X_GROUND"] = x_ground
        if y_ground is not UNSET:
            field_dict["Y_GROUND"] = y_ground
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_fac_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_id = _parse_fac_id(d.pop("FAC_ID", UNSET))

        def _parse_x_ground(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_ground = _parse_x_ground(d.pop("X_GROUND", UNSET))

        def _parse_y_ground(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_ground = _parse_y_ground(d.pop("Y_GROUND", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            fac_id=fac_id,
            x_ground=x_ground,
            y_ground=y_ground,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
