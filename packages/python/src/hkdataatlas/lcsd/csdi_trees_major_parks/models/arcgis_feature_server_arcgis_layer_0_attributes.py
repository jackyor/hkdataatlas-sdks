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
        location_in_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        location_in_english (None | str | Unset): Publisher field type: esriFieldTypeString
        scientific_name (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        x (None | str | Unset): Publisher field type: esriFieldTypeString
        y (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    location_in_chinese: None | str | Unset = UNSET
    location_in_english: None | str | Unset = UNSET
    scientific_name: None | str | Unset = UNSET
    chinese_name: None | str | Unset = UNSET
    x: None | str | Unset = UNSET
    y: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_in_chinese: None | str | Unset
        if isinstance(self.location_in_chinese, Unset):
            location_in_chinese = UNSET
        else:
            location_in_chinese = self.location_in_chinese

        location_in_english: None | str | Unset
        if isinstance(self.location_in_english, Unset):
            location_in_english = UNSET
        else:
            location_in_english = self.location_in_english

        scientific_name: None | str | Unset
        if isinstance(self.scientific_name, Unset):
            scientific_name = UNSET
        else:
            scientific_name = self.scientific_name

        chinese_name: None | str | Unset
        if isinstance(self.chinese_name, Unset):
            chinese_name = UNSET
        else:
            chinese_name = self.chinese_name

        x: None | str | Unset
        if isinstance(self.x, Unset):
            x = UNSET
        else:
            x = self.x

        y: None | str | Unset
        if isinstance(self.y, Unset):
            y = UNSET
        else:
            y = self.y

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_in_chinese is not UNSET:
            field_dict["Location_in_Chinese"] = location_in_chinese
        if location_in_english is not UNSET:
            field_dict["Location_in_English"] = location_in_english
        if scientific_name is not UNSET:
            field_dict["Scientific_Name"] = scientific_name
        if chinese_name is not UNSET:
            field_dict["Chinese_Name"] = chinese_name
        if x is not UNSET:
            field_dict["X"] = x
        if y is not UNSET:
            field_dict["Y"] = y
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_location_in_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_in_chinese = _parse_location_in_chinese(
            d.pop("Location_in_Chinese", UNSET)
        )

        def _parse_location_in_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_in_english = _parse_location_in_english(
            d.pop("Location_in_English", UNSET)
        )

        def _parse_scientific_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scientific_name = _parse_scientific_name(d.pop("Scientific_Name", UNSET))

        def _parse_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name = _parse_chinese_name(d.pop("Chinese_Name", UNSET))

        def _parse_x(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        x = _parse_x(d.pop("X", UNSET))

        def _parse_y(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y = _parse_y(d.pop("Y", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            location_in_chinese=location_in_chinese,
            location_in_english=location_in_english,
            scientific_name=scientific_name,
            chinese_name=chinese_name,
            x=x,
            y=y,
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
