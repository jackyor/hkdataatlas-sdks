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
        x_coordinate (float | None | Unset): Publisher field type: esriFieldTypeDouble
        y_coordinate (float | None | Unset): Publisher field type: esriFieldTypeDouble
        e_tr_ms_id (None | str | Unset): Publisher field type: esriFieldTypeString
        tmcp_id (None | str | Unset): Publisher field type: esriFieldTypeString
        species_en (None | str | Unset): Publisher field type: esriFieldTypeString
        species_ch (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    x_coordinate: float | None | Unset = UNSET
    y_coordinate: float | None | Unset = UNSET
    e_tr_ms_id: None | str | Unset = UNSET
    tmcp_id: None | str | Unset = UNSET
    species_en: None | str | Unset = UNSET
    species_ch: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        x_coordinate: float | None | Unset
        if isinstance(self.x_coordinate, Unset):
            x_coordinate = UNSET
        else:
            x_coordinate = self.x_coordinate

        y_coordinate: float | None | Unset
        if isinstance(self.y_coordinate, Unset):
            y_coordinate = UNSET
        else:
            y_coordinate = self.y_coordinate

        e_tr_ms_id: None | str | Unset
        if isinstance(self.e_tr_ms_id, Unset):
            e_tr_ms_id = UNSET
        else:
            e_tr_ms_id = self.e_tr_ms_id

        tmcp_id: None | str | Unset
        if isinstance(self.tmcp_id, Unset):
            tmcp_id = UNSET
        else:
            tmcp_id = self.tmcp_id

        species_en: None | str | Unset
        if isinstance(self.species_en, Unset):
            species_en = UNSET
        else:
            species_en = self.species_en

        species_ch: None | str | Unset
        if isinstance(self.species_ch, Unset):
            species_ch = UNSET
        else:
            species_ch = self.species_ch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if x_coordinate is not UNSET:
            field_dict["X_coordinate"] = x_coordinate
        if y_coordinate is not UNSET:
            field_dict["Y_coordinate"] = y_coordinate
        if e_tr_ms_id is not UNSET:
            field_dict["ETrMS_ID"] = e_tr_ms_id
        if tmcp_id is not UNSET:
            field_dict["TMCP_ID"] = tmcp_id
        if species_en is not UNSET:
            field_dict["Species_EN"] = species_en
        if species_ch is not UNSET:
            field_dict["Species_CH"] = species_ch

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_x_coordinate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_coordinate = _parse_x_coordinate(d.pop("X_coordinate", UNSET))

        def _parse_y_coordinate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_coordinate = _parse_y_coordinate(d.pop("Y_coordinate", UNSET))

        def _parse_e_tr_ms_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_tr_ms_id = _parse_e_tr_ms_id(d.pop("ETrMS_ID", UNSET))

        def _parse_tmcp_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tmcp_id = _parse_tmcp_id(d.pop("TMCP_ID", UNSET))

        def _parse_species_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        species_en = _parse_species_en(d.pop("Species_EN", UNSET))

        def _parse_species_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        species_ch = _parse_species_ch(d.pop("Species_CH", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
            e_tr_ms_id=e_tr_ms_id,
            tmcp_id=tmcp_id,
            species_en=species_en,
            species_ch=species_ch,
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
