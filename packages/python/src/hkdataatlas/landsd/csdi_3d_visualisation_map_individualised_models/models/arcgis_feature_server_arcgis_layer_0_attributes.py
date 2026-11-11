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
        url_3d_visualisation_map (None | str | Unset): Publisher field type: esriFieldTypeString
        download_api (None | str | Unset): Publisher field type: esriFieldTypeString
        revisiondate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        format_fbx (None | str | Unset): Publisher field type: esriFieldTypeString
        format_gl_tf (None | str | Unset): Publisher field type: esriFieldTypeString
        format_max (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    sheetno: None | str | Unset = UNSET
    url_3d_visualisation_map: None | str | Unset = UNSET
    download_api: None | str | Unset = UNSET
    revisiondate: Any | Unset = UNSET
    format_fbx: None | str | Unset = UNSET
    format_gl_tf: None | str | Unset = UNSET
    format_max: None | str | Unset = UNSET
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

        format_fbx: None | str | Unset
        if isinstance(self.format_fbx, Unset):
            format_fbx = UNSET
        else:
            format_fbx = self.format_fbx

        format_gl_tf: None | str | Unset
        if isinstance(self.format_gl_tf, Unset):
            format_gl_tf = UNSET
        else:
            format_gl_tf = self.format_gl_tf

        format_max: None | str | Unset
        if isinstance(self.format_max, Unset):
            format_max = UNSET
        else:
            format_max = self.format_max

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
        if url_3d_visualisation_map is not UNSET:
            field_dict["URL_3D_Visualisation_Map"] = url_3d_visualisation_map
        if download_api is not UNSET:
            field_dict["Download_API"] = download_api
        if revisiondate is not UNSET:
            field_dict["REVISIONDATE"] = revisiondate
        if format_fbx is not UNSET:
            field_dict["Format_FBX"] = format_fbx
        if format_gl_tf is not UNSET:
            field_dict["Format_glTF"] = format_gl_tf
        if format_max is not UNSET:
            field_dict["Format_MAX"] = format_max
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

        def _parse_format_fbx(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_fbx = _parse_format_fbx(d.pop("Format_FBX", UNSET))

        def _parse_format_gl_tf(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_gl_tf = _parse_format_gl_tf(d.pop("Format_glTF", UNSET))

        def _parse_format_max(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_max = _parse_format_max(d.pop("Format_MAX", UNSET))

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
            url_3d_visualisation_map=url_3d_visualisation_map,
            download_api=download_api,
            revisiondate=revisiondate,
            format_fbx=format_fbx,
            format_gl_tf=format_gl_tf,
            format_max=format_max,
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
