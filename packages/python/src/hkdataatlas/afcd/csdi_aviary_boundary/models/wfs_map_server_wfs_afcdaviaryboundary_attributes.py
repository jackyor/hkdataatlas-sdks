from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsAFCDAVIARYBOUNDARYAttributes")


@_attrs_define
class WfsMapServerWfsAFCDAVIARYBOUNDARYAttributes:
    """
    Attributes:
        location (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ogr_fid (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        shape_star (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        shape_stle (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        x (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into all
            JSON queries.
        y (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    location: None | str | Unset = UNSET
    ogr_fid: float | None | Unset = UNSET
    shape_star: float | None | Unset = UNSET
    shape_stle: float | None | Unset = UNSET
    x: float | None | Unset = UNSET
    y: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        ogr_fid: float | None | Unset
        if isinstance(self.ogr_fid, Unset):
            ogr_fid = UNSET
        else:
            ogr_fid = self.ogr_fid

        shape_star: float | None | Unset
        if isinstance(self.shape_star, Unset):
            shape_star = UNSET
        else:
            shape_star = self.shape_star

        shape_stle: float | None | Unset
        if isinstance(self.shape_stle, Unset):
            shape_stle = UNSET
        else:
            shape_stle = self.shape_stle

        x: float | None | Unset
        if isinstance(self.x, Unset):
            x = UNSET
        else:
            x = self.x

        y: float | None | Unset
        if isinstance(self.y, Unset):
            y = UNSET
        else:
            y = self.y

        objectid = self.objectid

        shape = self.shape

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
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if ogr_fid is not UNSET:
            field_dict["OGR_FID"] = ogr_fid
        if shape_star is not UNSET:
            field_dict["SHAPE_STAR"] = shape_star
        if shape_stle is not UNSET:
            field_dict["SHAPE_STLE"] = shape_stle
        if x is not UNSET:
            field_dict["X"] = x
        if y is not UNSET:
            field_dict["Y"] = y
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("LOCATION", UNSET))

        def _parse_ogr_fid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ogr_fid = _parse_ogr_fid(d.pop("OGR_FID", UNSET))

        def _parse_shape_star(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_star = _parse_shape_star(d.pop("SHAPE_STAR", UNSET))

        def _parse_shape_stle(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_stle = _parse_shape_stle(d.pop("SHAPE_STLE", UNSET))

        def _parse_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x = _parse_x(d.pop("X", UNSET))

        def _parse_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y = _parse_y(d.pop("Y", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("SHAPE_Area", UNSET))

        wfs_map_server_wfs_afcdaviaryboundary_attributes = cls(
            location=location,
            ogr_fid=ogr_fid,
            shape_star=shape_star,
            shape_stle=shape_stle,
            x=x,
            y=y,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_afcdaviaryboundary_attributes.additional_properties = d
        return wfs_map_server_wfs_afcdaviaryboundary_attributes

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
