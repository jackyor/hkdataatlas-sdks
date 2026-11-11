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
        sheetno (None | str | Unset): Publisher field type: esriFieldTypeString
        edition_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        edition (int | None | Unset): Publisher field type: esriFieldTypeInteger
        geo_tiff (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    sheetno: None | str | Unset = UNSET
    edition_date: Any | Unset = UNSET
    edition: int | None | Unset = UNSET
    geo_tiff: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        sheetno: None | str | Unset
        if isinstance(self.sheetno, Unset):
            sheetno = UNSET
        else:
            sheetno = self.sheetno

        edition_date = self.edition_date

        edition: int | None | Unset
        if isinstance(self.edition, Unset):
            edition = UNSET
        else:
            edition = self.edition

        geo_tiff: None | str | Unset
        if isinstance(self.geo_tiff, Unset):
            geo_tiff = UNSET
        else:
            geo_tiff = self.geo_tiff

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if sheetno is not UNSET:
            field_dict["SHEETNO"] = sheetno
        if edition_date is not UNSET:
            field_dict["EDITION_DATE"] = edition_date
        if edition is not UNSET:
            field_dict["EDITION"] = edition
        if geo_tiff is not UNSET:
            field_dict["GeoTiff"] = geo_tiff
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_sheetno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sheetno = _parse_sheetno(d.pop("SHEETNO", UNSET))

        edition_date = d.pop("EDITION_DATE", UNSET)

        def _parse_edition(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edition = _parse_edition(d.pop("EDITION", UNSET))

        def _parse_geo_tiff(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geo_tiff = _parse_geo_tiff(d.pop("GeoTiff", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            sheetno=sheetno,
            edition_date=edition_date,
            edition=edition,
            geo_tiff=geo_tiff,
            shape_length=shape_length,
            shape_area=shape_area,
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
