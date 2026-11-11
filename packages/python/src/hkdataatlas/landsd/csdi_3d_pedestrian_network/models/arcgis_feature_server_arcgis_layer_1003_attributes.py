from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1003Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1003Attributes:
    """
    Attributes:
        object_id (int | Unset): Publisher field type: esriFieldTypeOID
        building_id (int | Unset): Publisher field type: esriFieldTypeInteger
        chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        english_name (None | str | Unset): Publisher field type: esriFieldTypeString
        creation_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        modified_by (str | Unset): Publisher field type: esriFieldTypeString
        last_amendment_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
    """

    object_id: int | Unset = UNSET
    building_id: int | Unset = UNSET
    chinese_name: None | str | Unset = UNSET
    english_name: None | str | Unset = UNSET
    creation_date: Any | Unset = UNSET
    modified_by: str | Unset = UNSET
    last_amendment_date: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        building_id = self.building_id

        chinese_name: None | str | Unset
        if isinstance(self.chinese_name, Unset):
            chinese_name = UNSET
        else:
            chinese_name = self.chinese_name

        english_name: None | str | Unset
        if isinstance(self.english_name, Unset):
            english_name = UNSET
        else:
            english_name = self.english_name

        creation_date = self.creation_date

        modified_by = self.modified_by

        last_amendment_date = self.last_amendment_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_id is not UNSET:
            field_dict["ObjectID"] = object_id
        if building_id is not UNSET:
            field_dict["BuildingID"] = building_id
        if chinese_name is not UNSET:
            field_dict["ChineseName"] = chinese_name
        if english_name is not UNSET:
            field_dict["EnglishName"] = english_name
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

        building_id = d.pop("BuildingID", UNSET)

        def _parse_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name = _parse_chinese_name(d.pop("ChineseName", UNSET))

        def _parse_english_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_name = _parse_english_name(d.pop("EnglishName", UNSET))

        creation_date = d.pop("CreationDate", UNSET)

        modified_by = d.pop("ModifiedBy", UNSET)

        last_amendment_date = d.pop("LastAmendmentDate", UNSET)

        arcgis_feature_server_arcgis_layer_1003_attributes = cls(
            object_id=object_id,
            building_id=building_id,
            chinese_name=chinese_name,
            english_name=english_name,
            creation_date=creation_date,
            modified_by=modified_by,
            last_amendment_date=last_amendment_date,
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
