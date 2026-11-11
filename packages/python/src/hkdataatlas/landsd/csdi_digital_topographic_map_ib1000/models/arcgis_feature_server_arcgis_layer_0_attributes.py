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
        sheetno (str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        revisiondate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        fgdb (None | str | Unset): Publisher field type: esriFieldTypeString
        gml (None | str | Unset): Publisher field type: esriFieldTypeString
        dgn (None | str | Unset): Publisher field type: esriFieldTypeString
        dwg (None | str | Unset): Publisher field type: esriFieldTypeString
        tiff (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    sheetno: str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    revisiondate: Any | Unset = UNSET
    fgdb: None | str | Unset = UNSET
    gml: None | str | Unset = UNSET
    dgn: None | str | Unset = UNSET
    dwg: None | str | Unset = UNSET
    tiff: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        sheetno = self.sheetno

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

        revisiondate = self.revisiondate

        fgdb: None | str | Unset
        if isinstance(self.fgdb, Unset):
            fgdb = UNSET
        else:
            fgdb = self.fgdb

        gml: None | str | Unset
        if isinstance(self.gml, Unset):
            gml = UNSET
        else:
            gml = self.gml

        dgn: None | str | Unset
        if isinstance(self.dgn, Unset):
            dgn = UNSET
        else:
            dgn = self.dgn

        dwg: None | str | Unset
        if isinstance(self.dwg, Unset):
            dwg = UNSET
        else:
            dwg = self.dwg

        tiff: None | str | Unset
        if isinstance(self.tiff, Unset):
            tiff = UNSET
        else:
            tiff = self.tiff

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if sheetno is not UNSET:
            field_dict["SHEETNO"] = sheetno
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if revisiondate is not UNSET:
            field_dict["REVISIONDATE"] = revisiondate
        if fgdb is not UNSET:
            field_dict["FGDB"] = fgdb
        if gml is not UNSET:
            field_dict["GML"] = gml
        if dgn is not UNSET:
            field_dict["DGN"] = dgn
        if dwg is not UNSET:
            field_dict["DWG"] = dwg
        if tiff is not UNSET:
            field_dict["TIFF"] = tiff

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        sheetno = d.pop("SHEETNO", UNSET)

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

        revisiondate = d.pop("REVISIONDATE", UNSET)

        def _parse_fgdb(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fgdb = _parse_fgdb(d.pop("FGDB", UNSET))

        def _parse_gml(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gml = _parse_gml(d.pop("GML", UNSET))

        def _parse_dgn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dgn = _parse_dgn(d.pop("DGN", UNSET))

        def _parse_dwg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dwg = _parse_dwg(d.pop("DWG", UNSET))

        def _parse_tiff(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tiff = _parse_tiff(d.pop("TIFF", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            sheetno=sheetno,
            shape_length=shape_length,
            shape_area=shape_area,
            revisiondate=revisiondate,
            fgdb=fgdb,
            gml=gml,
            dgn=dgn,
            dwg=dwg,
            tiff=tiff,
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
