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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        stopping_place_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        stopping_place_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        stopping_place_en (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    stopping_place_tc: None | str | Unset = UNSET
    stopping_place_sc: None | str | Unset = UNSET
    stopping_place_en: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        stopping_place_tc: None | str | Unset
        if isinstance(self.stopping_place_tc, Unset):
            stopping_place_tc = UNSET
        else:
            stopping_place_tc = self.stopping_place_tc

        stopping_place_sc: None | str | Unset
        if isinstance(self.stopping_place_sc, Unset):
            stopping_place_sc = UNSET
        else:
            stopping_place_sc = self.stopping_place_sc

        stopping_place_en: None | str | Unset
        if isinstance(self.stopping_place_en, Unset):
            stopping_place_en = UNSET
        else:
            stopping_place_en = self.stopping_place_en

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if stopping_place_tc is not UNSET:
            field_dict["STOPPING_PLACE_TC"] = stopping_place_tc
        if stopping_place_sc is not UNSET:
            field_dict["STOPPING_PLACE_SC"] = stopping_place_sc
        if stopping_place_en is not UNSET:
            field_dict["STOPPING_PLACE_EN"] = stopping_place_en

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_stopping_place_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stopping_place_tc = _parse_stopping_place_tc(d.pop("STOPPING_PLACE_TC", UNSET))

        def _parse_stopping_place_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stopping_place_sc = _parse_stopping_place_sc(d.pop("STOPPING_PLACE_SC", UNSET))

        def _parse_stopping_place_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stopping_place_en = _parse_stopping_place_en(d.pop("STOPPING_PLACE_EN", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            stopping_place_tc=stopping_place_tc,
            stopping_place_sc=stopping_place_sc,
            stopping_place_en=stopping_place_en,
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
