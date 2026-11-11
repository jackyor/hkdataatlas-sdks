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
        cp_en (None | str | Unset): Publisher field type: esriFieldTypeString
        cp_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        cp_sc (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    cp_en: None | str | Unset = UNSET
    cp_tc: None | str | Unset = UNSET
    cp_sc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        cp_en: None | str | Unset
        if isinstance(self.cp_en, Unset):
            cp_en = UNSET
        else:
            cp_en = self.cp_en

        cp_tc: None | str | Unset
        if isinstance(self.cp_tc, Unset):
            cp_tc = UNSET
        else:
            cp_tc = self.cp_tc

        cp_sc: None | str | Unset
        if isinstance(self.cp_sc, Unset):
            cp_sc = UNSET
        else:
            cp_sc = self.cp_sc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if cp_en is not UNSET:
            field_dict["CP_En"] = cp_en
        if cp_tc is not UNSET:
            field_dict["CP_Tc"] = cp_tc
        if cp_sc is not UNSET:
            field_dict["CP_Sc"] = cp_sc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_cp_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cp_en = _parse_cp_en(d.pop("CP_En", UNSET))

        def _parse_cp_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cp_tc = _parse_cp_tc(d.pop("CP_Tc", UNSET))

        def _parse_cp_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cp_sc = _parse_cp_sc(d.pop("CP_Sc", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            cp_en=cp_en,
            cp_tc=cp_tc,
            cp_sc=cp_sc,
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
