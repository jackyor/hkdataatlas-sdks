from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTileIndexAttributes")


@_attrs_define
class WfsMapServerWfsTileIndexAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        sheetno (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        revisiondate (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        fgdb (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        gml (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dgn (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dwg (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        tiff (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    sheetno: str | Unset = UNSET
    revisiondate: None | str | Unset = UNSET
    fgdb: None | str | Unset = UNSET
    gml: None | str | Unset = UNSET
    dgn: None | str | Unset = UNSET
    dwg: None | str | Unset = UNSET
    tiff: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        sheetno = self.sheetno

        revisiondate: None | str | Unset
        if isinstance(self.revisiondate, Unset):
            revisiondate = UNSET
        else:
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
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if sheetno is not UNSET:
            field_dict["SHEETNO"] = sheetno
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
        if shape_length is not UNSET:
            field_dict["Shape_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        sheetno = d.pop("SHEETNO", UNSET)

        def _parse_revisiondate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revisiondate = _parse_revisiondate(d.pop("REVISIONDATE", UNSET))

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

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape_Area", UNSET))

        wfs_map_server_wfs_tile_index_attributes = cls(
            objectid=objectid,
            shape=shape,
            sheetno=sheetno,
            revisiondate=revisiondate,
            fgdb=fgdb,
            gml=gml,
            dgn=dgn,
            dwg=dwg,
            tiff=tiff,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_tile_index_attributes.additional_properties = d
        return wfs_map_server_wfs_tile_index_attributes

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
