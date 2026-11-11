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
        beach (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_grading_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_gradings (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_gradings_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        beach_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        link (None | str | Unset): Publisher field type: esriFieldTypeString
        link_beach (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    beach: None | str | Unset = UNSET
    beach_grading_sc: None | str | Unset = UNSET
    beach_gradings: None | str | Unset = UNSET
    beach_gradings_tc: None | str | Unset = UNSET
    beach_sc: None | str | Unset = UNSET
    beach_tc: None | str | Unset = UNSET
    link: None | str | Unset = UNSET
    link_beach: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beach: None | str | Unset
        if isinstance(self.beach, Unset):
            beach = UNSET
        else:
            beach = self.beach

        beach_grading_sc: None | str | Unset
        if isinstance(self.beach_grading_sc, Unset):
            beach_grading_sc = UNSET
        else:
            beach_grading_sc = self.beach_grading_sc

        beach_gradings: None | str | Unset
        if isinstance(self.beach_gradings, Unset):
            beach_gradings = UNSET
        else:
            beach_gradings = self.beach_gradings

        beach_gradings_tc: None | str | Unset
        if isinstance(self.beach_gradings_tc, Unset):
            beach_gradings_tc = UNSET
        else:
            beach_gradings_tc = self.beach_gradings_tc

        beach_sc: None | str | Unset
        if isinstance(self.beach_sc, Unset):
            beach_sc = UNSET
        else:
            beach_sc = self.beach_sc

        beach_tc: None | str | Unset
        if isinstance(self.beach_tc, Unset):
            beach_tc = UNSET
        else:
            beach_tc = self.beach_tc

        link: None | str | Unset
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        link_beach: None | str | Unset
        if isinstance(self.link_beach, Unset):
            link_beach = UNSET
        else:
            link_beach = self.link_beach

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if beach is not UNSET:
            field_dict["Beach"] = beach
        if beach_grading_sc is not UNSET:
            field_dict["Beach_Grading_SC"] = beach_grading_sc
        if beach_gradings is not UNSET:
            field_dict["Beach_Gradings"] = beach_gradings
        if beach_gradings_tc is not UNSET:
            field_dict["Beach_Gradings_TC"] = beach_gradings_tc
        if beach_sc is not UNSET:
            field_dict["Beach_SC"] = beach_sc
        if beach_tc is not UNSET:
            field_dict["Beach_TC"] = beach_tc
        if link is not UNSET:
            field_dict["link"] = link
        if link_beach is not UNSET:
            field_dict["link_beach"] = link_beach
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_beach(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach = _parse_beach(d.pop("Beach", UNSET))

        def _parse_beach_grading_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_grading_sc = _parse_beach_grading_sc(d.pop("Beach_Grading_SC", UNSET))

        def _parse_beach_gradings(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_gradings = _parse_beach_gradings(d.pop("Beach_Gradings", UNSET))

        def _parse_beach_gradings_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_gradings_tc = _parse_beach_gradings_tc(d.pop("Beach_Gradings_TC", UNSET))

        def _parse_beach_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_sc = _parse_beach_sc(d.pop("Beach_SC", UNSET))

        def _parse_beach_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        beach_tc = _parse_beach_tc(d.pop("Beach_TC", UNSET))

        def _parse_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        link = _parse_link(d.pop("link", UNSET))

        def _parse_link_beach(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        link_beach = _parse_link_beach(d.pop("link_beach", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            beach=beach,
            beach_grading_sc=beach_grading_sc,
            beach_gradings=beach_gradings,
            beach_gradings_tc=beach_gradings_tc,
            beach_sc=beach_sc,
            beach_tc=beach_tc,
            link=link,
            link_beach=link_beach,
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
