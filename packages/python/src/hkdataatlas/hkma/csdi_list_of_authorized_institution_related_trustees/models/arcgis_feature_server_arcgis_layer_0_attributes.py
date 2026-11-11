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
        segment (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        prinvipal_place_en (None | str | Unset): Publisher field type: esriFieldTypeString
        official_web_en (None | str | Unset): Publisher field type: esriFieldTypeString
        associated_ai_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        prinvipal_place_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        official_web_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        associated_ai_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    segment: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    prinvipal_place_en: None | str | Unset = UNSET
    official_web_en: None | str | Unset = UNSET
    associated_ai_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    prinvipal_place_tc: None | str | Unset = UNSET
    official_web_tc: None | str | Unset = UNSET
    associated_ai_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segment: None | str | Unset
        if isinstance(self.segment, Unset):
            segment = UNSET
        else:
            segment = self.segment

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        prinvipal_place_en: None | str | Unset
        if isinstance(self.prinvipal_place_en, Unset):
            prinvipal_place_en = UNSET
        else:
            prinvipal_place_en = self.prinvipal_place_en

        official_web_en: None | str | Unset
        if isinstance(self.official_web_en, Unset):
            official_web_en = UNSET
        else:
            official_web_en = self.official_web_en

        associated_ai_en: None | str | Unset
        if isinstance(self.associated_ai_en, Unset):
            associated_ai_en = UNSET
        else:
            associated_ai_en = self.associated_ai_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        prinvipal_place_tc: None | str | Unset
        if isinstance(self.prinvipal_place_tc, Unset):
            prinvipal_place_tc = UNSET
        else:
            prinvipal_place_tc = self.prinvipal_place_tc

        official_web_tc: None | str | Unset
        if isinstance(self.official_web_tc, Unset):
            official_web_tc = UNSET
        else:
            official_web_tc = self.official_web_tc

        associated_ai_tc: None | str | Unset
        if isinstance(self.associated_ai_tc, Unset):
            associated_ai_tc = UNSET
        else:
            associated_ai_tc = self.associated_ai_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if segment is not UNSET:
            field_dict["segment"] = segment
        if name_en is not UNSET:
            field_dict["name_EN"] = name_en
        if prinvipal_place_en is not UNSET:
            field_dict["prinvipal_place_EN"] = prinvipal_place_en
        if official_web_en is not UNSET:
            field_dict["official_web_EN"] = official_web_en
        if associated_ai_en is not UNSET:
            field_dict["associated_ai_EN"] = associated_ai_en
        if name_tc is not UNSET:
            field_dict["name_TC"] = name_tc
        if prinvipal_place_tc is not UNSET:
            field_dict["prinvipal_place_TC"] = prinvipal_place_tc
        if official_web_tc is not UNSET:
            field_dict["official_web_TC"] = official_web_tc
        if associated_ai_tc is not UNSET:
            field_dict["associated_ai_TC"] = associated_ai_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_segment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        segment = _parse_segment(d.pop("segment", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("name_EN", UNSET))

        def _parse_prinvipal_place_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prinvipal_place_en = _parse_prinvipal_place_en(
            d.pop("prinvipal_place_EN", UNSET)
        )

        def _parse_official_web_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        official_web_en = _parse_official_web_en(d.pop("official_web_EN", UNSET))

        def _parse_associated_ai_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        associated_ai_en = _parse_associated_ai_en(d.pop("associated_ai_EN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("name_TC", UNSET))

        def _parse_prinvipal_place_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prinvipal_place_tc = _parse_prinvipal_place_tc(
            d.pop("prinvipal_place_TC", UNSET)
        )

        def _parse_official_web_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        official_web_tc = _parse_official_web_tc(d.pop("official_web_TC", UNSET))

        def _parse_associated_ai_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        associated_ai_tc = _parse_associated_ai_tc(d.pop("associated_ai_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            segment=segment,
            name_en=name_en,
            prinvipal_place_en=prinvipal_place_en,
            official_web_en=official_web_en,
            associated_ai_en=associated_ai_en,
            name_tc=name_tc,
            prinvipal_place_tc=prinvipal_place_tc,
            official_web_tc=official_web_tc,
            associated_ai_tc=associated_ai_tc,
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
