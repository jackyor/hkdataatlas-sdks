from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsOldSurveySheetOLD600MapIndexAttributes")


@_attrs_define
class WfsMapServerWfsOldSurveySheetOLD600MapIndexAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        sheetno (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        edition_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        edition (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        geo_tiff (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    sheetno: None | str | Unset = UNSET
    edition_date: None | str | Unset = UNSET
    edition: int | None | Unset = UNSET
    geo_tiff: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        sheetno: None | str | Unset
        if isinstance(self.sheetno, Unset):
            sheetno = UNSET
        else:
            sheetno = self.sheetno

        edition_date: None | str | Unset
        if isinstance(self.edition_date, Unset):
            edition_date = UNSET
        else:
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
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if sheetno is not UNSET:
            field_dict["SHEETNO"] = sheetno
        if edition_date is not UNSET:
            field_dict["EDITION_DATE"] = edition_date
        if edition is not UNSET:
            field_dict["EDITION"] = edition
        if geo_tiff is not UNSET:
            field_dict["GeoTiff"] = geo_tiff
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

        def _parse_sheetno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sheetno = _parse_sheetno(d.pop("SHEETNO", UNSET))

        def _parse_edition_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edition_date = _parse_edition_date(d.pop("EDITION_DATE", UNSET))

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

        shape_length = _parse_shape_length(d.pop("Shape_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape_Area", UNSET))

        wfs_map_server_wfs_old_survey_sheet_old600_map_index_attributes = cls(
            objectid=objectid,
            shape=shape,
            sheetno=sheetno,
            edition_date=edition_date,
            edition=edition,
            geo_tiff=geo_tiff,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_old_survey_sheet_old600_map_index_attributes.additional_properties = d
        return wfs_map_server_wfs_old_survey_sheet_old600_map_index_attributes

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
