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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        installation_id (str | Unset): Publisher field type: esriFieldTypeString
        name (str | Unset): Publisher field type: esriFieldTypeString
        chinese_name (str | Unset): Publisher field type: esriFieldTypeString
        location (str | Unset): Publisher field type: esriFieldTypeString
        location_chinese (str | Unset): Publisher field type: esriFieldTypeString
        system (str | Unset): Publisher field type: esriFieldTypeString
        capacity (float | Unset): Publisher field type: esriFieldTypeDouble
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    installation_id: str | Unset = UNSET
    name: str | Unset = UNSET
    chinese_name: str | Unset = UNSET
    location: str | Unset = UNSET
    location_chinese: str | Unset = UNSET
    system: str | Unset = UNSET
    capacity: float | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        installation_id = self.installation_id

        name = self.name

        chinese_name = self.chinese_name

        location = self.location

        location_chinese = self.location_chinese

        system = self.system

        capacity = self.capacity

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if installation_id is not UNSET:
            field_dict["INSTALLATION_ID"] = installation_id
        if name is not UNSET:
            field_dict["NAME"] = name
        if chinese_name is not UNSET:
            field_dict["CHINESE_NAME"] = chinese_name
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if location_chinese is not UNSET:
            field_dict["LOCATION_CHINESE"] = location_chinese
        if system is not UNSET:
            field_dict["SYSTEM"] = system
        if capacity is not UNSET:
            field_dict["CAPACITY"] = capacity
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        installation_id = d.pop("INSTALLATION_ID", UNSET)

        name = d.pop("NAME", UNSET)

        chinese_name = d.pop("CHINESE_NAME", UNSET)

        location = d.pop("LOCATION", UNSET)

        location_chinese = d.pop("LOCATION_CHINESE", UNSET)

        system = d.pop("SYSTEM", UNSET)

        capacity = d.pop("CAPACITY", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            installation_id=installation_id,
            name=name,
            chinese_name=chinese_name,
            location=location,
            location_chinese=location_chinese,
            system=system,
            capacity=capacity,
            shape_length=shape_length,
            shape_area=shape_area,
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
