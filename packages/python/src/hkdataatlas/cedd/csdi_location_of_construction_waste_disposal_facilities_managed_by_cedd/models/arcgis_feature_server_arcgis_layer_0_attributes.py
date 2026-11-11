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
        english (None | str | Unset): Publisher field type: esriFieldTypeString
        traditional_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    english: None | str | Unset = UNSET
    traditional_chinese: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        english: None | str | Unset
        if isinstance(self.english, Unset):
            english = UNSET
        else:
            english = self.english

        traditional_chinese: None | str | Unset
        if isinstance(self.traditional_chinese, Unset):
            traditional_chinese = UNSET
        else:
            traditional_chinese = self.traditional_chinese

        easting: None | str | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: None | str | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if english is not UNSET:
            field_dict["English"] = english
        if traditional_chinese is not UNSET:
            field_dict["Traditional_Chinese"] = traditional_chinese
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english = _parse_english(d.pop("English", UNSET))

        def _parse_traditional_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        traditional_chinese = _parse_traditional_chinese(
            d.pop("Traditional_Chinese", UNSET)
        )

        def _parse_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            english=english,
            traditional_chinese=traditional_chinese,
            easting=easting,
            northing=northing,
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
