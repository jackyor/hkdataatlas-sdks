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
        dcs_id (None | str | Unset): Publisher field type: esriFieldTypeString
        dcs_name_english (None | str | Unset): Publisher field type: esriFieldTypeString
        dcs_name_simplified_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        dcs_name_traditional_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    dcs_id: None | str | Unset = UNSET
    dcs_name_english: None | str | Unset = UNSET
    dcs_name_simplified_chinese: None | str | Unset = UNSET
    dcs_name_traditional_chinese: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dcs_id: None | str | Unset
        if isinstance(self.dcs_id, Unset):
            dcs_id = UNSET
        else:
            dcs_id = self.dcs_id

        dcs_name_english: None | str | Unset
        if isinstance(self.dcs_name_english, Unset):
            dcs_name_english = UNSET
        else:
            dcs_name_english = self.dcs_name_english

        dcs_name_simplified_chinese: None | str | Unset
        if isinstance(self.dcs_name_simplified_chinese, Unset):
            dcs_name_simplified_chinese = UNSET
        else:
            dcs_name_simplified_chinese = self.dcs_name_simplified_chinese

        dcs_name_traditional_chinese: None | str | Unset
        if isinstance(self.dcs_name_traditional_chinese, Unset):
            dcs_name_traditional_chinese = UNSET
        else:
            dcs_name_traditional_chinese = self.dcs_name_traditional_chinese

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dcs_id is not UNSET:
            field_dict["DCS_ID"] = dcs_id
        if dcs_name_english is not UNSET:
            field_dict["DCS_Name_English"] = dcs_name_english
        if dcs_name_simplified_chinese is not UNSET:
            field_dict["DCS_Name_Simplified_Chinese"] = dcs_name_simplified_chinese
        if dcs_name_traditional_chinese is not UNSET:
            field_dict["DCS_Name_Traditional_Chinese"] = dcs_name_traditional_chinese
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_dcs_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dcs_id = _parse_dcs_id(d.pop("DCS_ID", UNSET))

        def _parse_dcs_name_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dcs_name_english = _parse_dcs_name_english(d.pop("DCS_Name_English", UNSET))

        def _parse_dcs_name_simplified_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dcs_name_simplified_chinese = _parse_dcs_name_simplified_chinese(
            d.pop("DCS_Name_Simplified_Chinese", UNSET)
        )

        def _parse_dcs_name_traditional_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dcs_name_traditional_chinese = _parse_dcs_name_traditional_chinese(
            d.pop("DCS_Name_Traditional_Chinese", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            dcs_id=dcs_id,
            dcs_name_english=dcs_name_english,
            dcs_name_simplified_chinese=dcs_name_simplified_chinese,
            dcs_name_traditional_chinese=dcs_name_traditional_chinese,
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
