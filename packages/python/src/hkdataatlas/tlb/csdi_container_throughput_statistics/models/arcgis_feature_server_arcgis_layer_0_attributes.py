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
        container_throughput_en (None | str | Unset): Publisher field type: esriFieldTypeString
        container_throughput_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        container_throughput_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    container_throughput_en: None | str | Unset = UNSET
    container_throughput_sc: None | str | Unset = UNSET
    container_throughput_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_throughput_en: None | str | Unset
        if isinstance(self.container_throughput_en, Unset):
            container_throughput_en = UNSET
        else:
            container_throughput_en = self.container_throughput_en

        container_throughput_sc: None | str | Unset
        if isinstance(self.container_throughput_sc, Unset):
            container_throughput_sc = UNSET
        else:
            container_throughput_sc = self.container_throughput_sc

        container_throughput_tc: None | str | Unset
        if isinstance(self.container_throughput_tc, Unset):
            container_throughput_tc = UNSET
        else:
            container_throughput_tc = self.container_throughput_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container_throughput_en is not UNSET:
            field_dict["Container_Throughput_EN"] = container_throughput_en
        if container_throughput_sc is not UNSET:
            field_dict["Container_Throughput_SC"] = container_throughput_sc
        if container_throughput_tc is not UNSET:
            field_dict["Container_Throughput_TC"] = container_throughput_tc
        if name_en is not UNSET:
            field_dict["Name_EN"] = name_en
        if name_sc is not UNSET:
            field_dict["Name_SC"] = name_sc
        if name_tc is not UNSET:
            field_dict["Name_TC"] = name_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_container_throughput_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container_throughput_en = _parse_container_throughput_en(
            d.pop("Container_Throughput_EN", UNSET)
        )

        def _parse_container_throughput_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container_throughput_sc = _parse_container_throughput_sc(
            d.pop("Container_Throughput_SC", UNSET)
        )

        def _parse_container_throughput_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container_throughput_tc = _parse_container_throughput_tc(
            d.pop("Container_Throughput_TC", UNSET)
        )

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("Name_EN", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("Name_SC", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("Name_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            container_throughput_en=container_throughput_en,
            container_throughput_sc=container_throughput_sc,
            container_throughput_tc=container_throughput_tc,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
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
