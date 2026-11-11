from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        install_type (None | str | Unset): Publisher field type: esriFieldTypeString
        name (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        location (None | str | Unset): Publisher field type: esriFieldTypeString
        location_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        area (None | str | Unset): Publisher field type: esriFieldTypeString
        area_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        system (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity (float | None | Unset): Publisher field type: esriFieldTypeDouble
        capacity_unit (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    install_type: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    chinese_name: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    location_chinese: None | str | Unset = UNSET
    area: None | str | Unset = UNSET
    area_chinese: None | str | Unset = UNSET
    system: None | str | Unset = UNSET
    capacity: float | None | Unset = UNSET
    capacity_unit: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        install_type: None | str | Unset
        if isinstance(self.install_type, Unset):
            install_type = UNSET
        else:
            install_type = self.install_type

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        chinese_name: None | str | Unset
        if isinstance(self.chinese_name, Unset):
            chinese_name = UNSET
        else:
            chinese_name = self.chinese_name

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        location_chinese: None | str | Unset
        if isinstance(self.location_chinese, Unset):
            location_chinese = UNSET
        else:
            location_chinese = self.location_chinese

        area: None | str | Unset
        if isinstance(self.area, Unset):
            area = UNSET
        else:
            area = self.area

        area_chinese: None | str | Unset
        if isinstance(self.area_chinese, Unset):
            area_chinese = UNSET
        else:
            area_chinese = self.area_chinese

        system: None | str | Unset
        if isinstance(self.system, Unset):
            system = UNSET
        else:
            system = self.system

        capacity: float | None | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        capacity_unit: None | str | Unset
        if isinstance(self.capacity_unit, Unset):
            capacity_unit = UNSET
        else:
            capacity_unit = self.capacity_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if install_type is not UNSET:
            field_dict["INSTALL_TYPE"] = install_type
        if name is not UNSET:
            field_dict["NAME"] = name
        if chinese_name is not UNSET:
            field_dict["CHINESE_NAME"] = chinese_name
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if location_chinese is not UNSET:
            field_dict["LOCATION_CHINESE"] = location_chinese
        if area is not UNSET:
            field_dict["AREA"] = area
        if area_chinese is not UNSET:
            field_dict["AREA_CHINESE"] = area_chinese
        if system is not UNSET:
            field_dict["SYSTEM"] = system
        if capacity is not UNSET:
            field_dict["CAPACITY"] = capacity
        if capacity_unit is not UNSET:
            field_dict["CAPACITY_UNIT"] = capacity_unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_install_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        install_type = _parse_install_type(d.pop("INSTALL_TYPE", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("NAME", UNSET))

        def _parse_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name = _parse_chinese_name(d.pop("CHINESE_NAME", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("LOCATION", UNSET))

        def _parse_location_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_chinese = _parse_location_chinese(d.pop("LOCATION_CHINESE", UNSET))

        def _parse_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area = _parse_area(d.pop("AREA", UNSET))

        def _parse_area_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_chinese = _parse_area_chinese(d.pop("AREA_CHINESE", UNSET))

        def _parse_system(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system = _parse_system(d.pop("SYSTEM", UNSET))

        def _parse_capacity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        capacity = _parse_capacity(d.pop("CAPACITY", UNSET))

        def _parse_capacity_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity_unit = _parse_capacity_unit(d.pop("CAPACITY_UNIT", UNSET))

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            objectid=objectid,
            install_type=install_type,
            name=name,
            chinese_name=chinese_name,
            location=location,
            location_chinese=location_chinese,
            area=area,
            area_chinese=area_chinese,
            system=system,
            capacity=capacity,
            capacity_unit=capacity_unit,
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
