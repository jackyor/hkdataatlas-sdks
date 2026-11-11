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
        project_code (None | str | Unset): Publisher field type: esriFieldTypeString
        english_title (None | str | Unset): Publisher field type: esriFieldTypeString
        traditional_chinese_title (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        category_id (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    project_code: None | str | Unset = UNSET
    english_title: None | str | Unset = UNSET
    traditional_chinese_title: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    category_id: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_code: None | str | Unset
        if isinstance(self.project_code, Unset):
            project_code = UNSET
        else:
            project_code = self.project_code

        english_title: None | str | Unset
        if isinstance(self.english_title, Unset):
            english_title = UNSET
        else:
            english_title = self.english_title

        traditional_chinese_title: None | str | Unset
        if isinstance(self.traditional_chinese_title, Unset):
            traditional_chinese_title = UNSET
        else:
            traditional_chinese_title = self.traditional_chinese_title

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_code is not UNSET:
            field_dict["ProjectCode"] = project_code
        if english_title is not UNSET:
            field_dict["English_Title"] = english_title
        if traditional_chinese_title is not UNSET:
            field_dict["Traditional_Chinese_Title"] = traditional_chinese_title
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if category_id is not UNSET:
            field_dict["CategoryID"] = category_id
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_project_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_code = _parse_project_code(d.pop("ProjectCode", UNSET))

        def _parse_english_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_title = _parse_english_title(d.pop("English_Title", UNSET))

        def _parse_traditional_chinese_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        traditional_chinese_title = _parse_traditional_chinese_title(
            d.pop("Traditional_Chinese_Title", UNSET)
        )

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_category_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_id = _parse_category_id(d.pop("CategoryID", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            project_code=project_code,
            english_title=english_title,
            traditional_chinese_title=traditional_chinese_title,
            longitude=longitude,
            latitude=latitude,
            category_id=category_id,
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
