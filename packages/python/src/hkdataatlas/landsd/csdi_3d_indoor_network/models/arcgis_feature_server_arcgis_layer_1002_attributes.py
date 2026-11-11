from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1002Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1002Attributes:
    """
    Attributes:
        object_id (int | Unset): Publisher field type: esriFieldTypeOID
        floor_id (int | Unset): Publisher field type: esriFieldTypeInteger
        floor_poly_id (None | str | Unset): Publisher field type: esriFieldTypeString
        building_id (int | Unset): Publisher field type: esriFieldTypeInteger
        english_name (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        data_source (int | Unset): Publisher field type: esriFieldTypeInteger
        level_source (int | Unset): Publisher field type: esriFieldTypeInteger
        creation_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        modified_by (str | Unset): Publisher field type: esriFieldTypeString
        last_amendment_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
    """

    object_id: int | Unset = UNSET
    floor_id: int | Unset = UNSET
    floor_poly_id: None | str | Unset = UNSET
    building_id: int | Unset = UNSET
    english_name: None | str | Unset = UNSET
    chinese_name: None | str | Unset = UNSET
    data_source: int | Unset = UNSET
    level_source: int | Unset = UNSET
    creation_date: Any | Unset = UNSET
    modified_by: str | Unset = UNSET
    last_amendment_date: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        floor_id = self.floor_id

        floor_poly_id: None | str | Unset
        if isinstance(self.floor_poly_id, Unset):
            floor_poly_id = UNSET
        else:
            floor_poly_id = self.floor_poly_id

        building_id = self.building_id

        english_name: None | str | Unset
        if isinstance(self.english_name, Unset):
            english_name = UNSET
        else:
            english_name = self.english_name

        chinese_name: None | str | Unset
        if isinstance(self.chinese_name, Unset):
            chinese_name = UNSET
        else:
            chinese_name = self.chinese_name

        data_source = self.data_source

        level_source = self.level_source

        creation_date = self.creation_date

        modified_by = self.modified_by

        last_amendment_date = self.last_amendment_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_id is not UNSET:
            field_dict["ObjectID"] = object_id
        if floor_id is not UNSET:
            field_dict["FloorID"] = floor_id
        if floor_poly_id is not UNSET:
            field_dict["FloorPolyID"] = floor_poly_id
        if building_id is not UNSET:
            field_dict["BuildingID"] = building_id
        if english_name is not UNSET:
            field_dict["EnglishName"] = english_name
        if chinese_name is not UNSET:
            field_dict["ChineseName"] = chinese_name
        if data_source is not UNSET:
            field_dict["DataSource"] = data_source
        if level_source is not UNSET:
            field_dict["LevelSource"] = level_source
        if creation_date is not UNSET:
            field_dict["CreationDate"] = creation_date
        if modified_by is not UNSET:
            field_dict["ModifiedBy"] = modified_by
        if last_amendment_date is not UNSET:
            field_dict["LastAmendmentDate"] = last_amendment_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        object_id = d.pop("ObjectID", UNSET)

        floor_id = d.pop("FloorID", UNSET)

        def _parse_floor_poly_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        floor_poly_id = _parse_floor_poly_id(d.pop("FloorPolyID", UNSET))

        building_id = d.pop("BuildingID", UNSET)

        def _parse_english_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_name = _parse_english_name(d.pop("EnglishName", UNSET))

        def _parse_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name = _parse_chinese_name(d.pop("ChineseName", UNSET))

        data_source = d.pop("DataSource", UNSET)

        level_source = d.pop("LevelSource", UNSET)

        creation_date = d.pop("CreationDate", UNSET)

        modified_by = d.pop("ModifiedBy", UNSET)

        last_amendment_date = d.pop("LastAmendmentDate", UNSET)

        arcgis_feature_server_arcgis_layer_1002_attributes = cls(
            object_id=object_id,
            floor_id=floor_id,
            floor_poly_id=floor_poly_id,
            building_id=building_id,
            english_name=english_name,
            chinese_name=chinese_name,
            data_source=data_source,
            level_source=level_source,
            creation_date=creation_date,
            modified_by=modified_by,
            last_amendment_date=last_amendment_date,
        )

        arcgis_feature_server_arcgis_layer_1002_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1002_attributes

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
