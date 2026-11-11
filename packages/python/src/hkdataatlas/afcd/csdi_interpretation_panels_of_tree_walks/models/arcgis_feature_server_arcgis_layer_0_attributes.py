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
        tree_walk_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        tree_walk (None | str | Unset): Publisher field type: esriFieldTypeString
        panel_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        panel (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    tree_walk_ch: None | str | Unset = UNSET
    tree_walk: None | str | Unset = UNSET
    panel_ch: None | str | Unset = UNSET
    panel: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        tree_walk_ch: None | str | Unset
        if isinstance(self.tree_walk_ch, Unset):
            tree_walk_ch = UNSET
        else:
            tree_walk_ch = self.tree_walk_ch

        tree_walk: None | str | Unset
        if isinstance(self.tree_walk, Unset):
            tree_walk = UNSET
        else:
            tree_walk = self.tree_walk

        panel_ch: None | str | Unset
        if isinstance(self.panel_ch, Unset):
            panel_ch = UNSET
        else:
            panel_ch = self.panel_ch

        panel: None | str | Unset
        if isinstance(self.panel, Unset):
            panel = UNSET
        else:
            panel = self.panel

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if tree_walk_ch is not UNSET:
            field_dict["Tree_Walk_Ch"] = tree_walk_ch
        if tree_walk is not UNSET:
            field_dict["Tree_Walk"] = tree_walk
        if panel_ch is not UNSET:
            field_dict["Panel_Ch"] = panel_ch
        if panel is not UNSET:
            field_dict["Panel"] = panel

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_tree_walk_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_walk_ch = _parse_tree_walk_ch(d.pop("Tree_Walk_Ch", UNSET))

        def _parse_tree_walk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_walk = _parse_tree_walk(d.pop("Tree_Walk", UNSET))

        def _parse_panel_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel_ch = _parse_panel_ch(d.pop("Panel_Ch", UNSET))

        def _parse_panel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        panel = _parse_panel(d.pop("Panel", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            tree_walk_ch=tree_walk_ch,
            tree_walk=tree_walk,
            panel_ch=panel_ch,
            panel=panel,
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
