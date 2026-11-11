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
        sheetno (None | str | Unset): Publisher field type: esriFieldTypeString
        url_3d_visualisation_map (None | str | Unset): Publisher field type: esriFieldTypeString
        download_api (None | str | Unset): Publisher field type: esriFieldTypeString
        revisiondate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        format_obj (None | str | Unset): Publisher field type: esriFieldTypeString
        format_osgb (None | str | Unset): Publisher field type: esriFieldTypeString
        format_3d_tiles (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    sheetno: None | str | Unset = UNSET
    url_3d_visualisation_map: None | str | Unset = UNSET
    download_api: None | str | Unset = UNSET
    revisiondate: Any | Unset = UNSET
    format_obj: None | str | Unset = UNSET
    format_osgb: None | str | Unset = UNSET
    format_3d_tiles: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sheetno: None | str | Unset
        if isinstance(self.sheetno, Unset):
            sheetno = UNSET
        else:
            sheetno = self.sheetno

        url_3d_visualisation_map: None | str | Unset
        if isinstance(self.url_3d_visualisation_map, Unset):
            url_3d_visualisation_map = UNSET
        else:
            url_3d_visualisation_map = self.url_3d_visualisation_map

        download_api: None | str | Unset
        if isinstance(self.download_api, Unset):
            download_api = UNSET
        else:
            download_api = self.download_api

        revisiondate = self.revisiondate

        format_obj: None | str | Unset
        if isinstance(self.format_obj, Unset):
            format_obj = UNSET
        else:
            format_obj = self.format_obj

        format_osgb: None | str | Unset
        if isinstance(self.format_osgb, Unset):
            format_osgb = UNSET
        else:
            format_osgb = self.format_osgb

        format_3d_tiles: None | str | Unset
        if isinstance(self.format_3d_tiles, Unset):
            format_3d_tiles = UNSET
        else:
            format_3d_tiles = self.format_3d_tiles

        objectid = self.objectid

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
        if sheetno is not UNSET:
            field_dict["SHEETNO"] = sheetno
        if url_3d_visualisation_map is not UNSET:
            field_dict["URL_3D_Visualisation_Map"] = url_3d_visualisation_map
        if download_api is not UNSET:
            field_dict["Download_API"] = download_api
        if revisiondate is not UNSET:
            field_dict["REVISIONDATE"] = revisiondate
        if format_obj is not UNSET:
            field_dict["Format_OBJ"] = format_obj
        if format_osgb is not UNSET:
            field_dict["Format_OSGB"] = format_osgb
        if format_3d_tiles is not UNSET:
            field_dict["Format_3D_Tiles"] = format_3d_tiles
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_sheetno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sheetno = _parse_sheetno(d.pop("SHEETNO", UNSET))

        def _parse_url_3d_visualisation_map(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_3d_visualisation_map = _parse_url_3d_visualisation_map(
            d.pop("URL_3D_Visualisation_Map", UNSET)
        )

        def _parse_download_api(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        download_api = _parse_download_api(d.pop("Download_API", UNSET))

        revisiondate = d.pop("REVISIONDATE", UNSET)

        def _parse_format_obj(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_obj = _parse_format_obj(d.pop("Format_OBJ", UNSET))

        def _parse_format_osgb(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_osgb = _parse_format_osgb(d.pop("Format_OSGB", UNSET))

        def _parse_format_3d_tiles(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_3d_tiles = _parse_format_3d_tiles(d.pop("Format_3D_Tiles", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

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
            sheetno=sheetno,
            url_3d_visualisation_map=url_3d_visualisation_map,
            download_api=download_api,
            revisiondate=revisiondate,
            format_obj=format_obj,
            format_osgb=format_osgb,
            format_3d_tiles=format_3d_tiles,
            objectid=objectid,
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
