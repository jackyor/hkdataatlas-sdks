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
        location_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        url_en (None | str | Unset): Publisher field type: esriFieldTypeString
        url_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        url_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    location_name_en: None | str | Unset = UNSET
    location_name_sc: None | str | Unset = UNSET
    location_name_tc: None | str | Unset = UNSET
    url_en: None | str | Unset = UNSET
    url_sc: None | str | Unset = UNSET
    url_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_name_en: None | str | Unset
        if isinstance(self.location_name_en, Unset):
            location_name_en = UNSET
        else:
            location_name_en = self.location_name_en

        location_name_sc: None | str | Unset
        if isinstance(self.location_name_sc, Unset):
            location_name_sc = UNSET
        else:
            location_name_sc = self.location_name_sc

        location_name_tc: None | str | Unset
        if isinstance(self.location_name_tc, Unset):
            location_name_tc = UNSET
        else:
            location_name_tc = self.location_name_tc

        url_en: None | str | Unset
        if isinstance(self.url_en, Unset):
            url_en = UNSET
        else:
            url_en = self.url_en

        url_sc: None | str | Unset
        if isinstance(self.url_sc, Unset):
            url_sc = UNSET
        else:
            url_sc = self.url_sc

        url_tc: None | str | Unset
        if isinstance(self.url_tc, Unset):
            url_tc = UNSET
        else:
            url_tc = self.url_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_name_en is not UNSET:
            field_dict["location_name_en"] = location_name_en
        if location_name_sc is not UNSET:
            field_dict["location_name_sc"] = location_name_sc
        if location_name_tc is not UNSET:
            field_dict["location_name_tc"] = location_name_tc
        if url_en is not UNSET:
            field_dict["url_en"] = url_en
        if url_sc is not UNSET:
            field_dict["url_sc"] = url_sc
        if url_tc is not UNSET:
            field_dict["url_tc"] = url_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_location_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_name_en = _parse_location_name_en(d.pop("location_name_en", UNSET))

        def _parse_location_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_name_sc = _parse_location_name_sc(d.pop("location_name_sc", UNSET))

        def _parse_location_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_name_tc = _parse_location_name_tc(d.pop("location_name_tc", UNSET))

        def _parse_url_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_en = _parse_url_en(d.pop("url_en", UNSET))

        def _parse_url_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_sc = _parse_url_sc(d.pop("url_sc", UNSET))

        def _parse_url_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_tc = _parse_url_tc(d.pop("url_tc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            location_name_en=location_name_en,
            location_name_sc=location_name_sc,
            location_name_tc=location_name_tc,
            url_en=url_en,
            url_sc=url_sc,
            url_tc=url_tc,
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
