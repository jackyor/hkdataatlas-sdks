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
        min_x (int | None | Unset): Publisher field type: esriFieldTypeInteger
        min_y (int | None | Unset): Publisher field type: esriFieldTypeInteger
        max_x (int | None | Unset): Publisher field type: esriFieldTypeInteger
        max_y (int | None | Unset): Publisher field type: esriFieldTypeInteger
        format_3ds (None | str | Unset): Publisher field type: esriFieldTypeString
        format_fbx (None | str | Unset): Publisher field type: esriFieldTypeString
        format_max (None | str | Unset): Publisher field type: esriFieldTypeString
        format_vrml (None | str | Unset): Publisher field type: esriFieldTypeString
        revisiondate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    sheetno: None | str | Unset = UNSET
    min_x: int | None | Unset = UNSET
    min_y: int | None | Unset = UNSET
    max_x: int | None | Unset = UNSET
    max_y: int | None | Unset = UNSET
    format_3ds: None | str | Unset = UNSET
    format_fbx: None | str | Unset = UNSET
    format_max: None | str | Unset = UNSET
    format_vrml: None | str | Unset = UNSET
    revisiondate: Any | Unset = UNSET
    remarks: None | str | Unset = UNSET
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

        min_x: int | None | Unset
        if isinstance(self.min_x, Unset):
            min_x = UNSET
        else:
            min_x = self.min_x

        min_y: int | None | Unset
        if isinstance(self.min_y, Unset):
            min_y = UNSET
        else:
            min_y = self.min_y

        max_x: int | None | Unset
        if isinstance(self.max_x, Unset):
            max_x = UNSET
        else:
            max_x = self.max_x

        max_y: int | None | Unset
        if isinstance(self.max_y, Unset):
            max_y = UNSET
        else:
            max_y = self.max_y

        format_3ds: None | str | Unset
        if isinstance(self.format_3ds, Unset):
            format_3ds = UNSET
        else:
            format_3ds = self.format_3ds

        format_fbx: None | str | Unset
        if isinstance(self.format_fbx, Unset):
            format_fbx = UNSET
        else:
            format_fbx = self.format_fbx

        format_max: None | str | Unset
        if isinstance(self.format_max, Unset):
            format_max = UNSET
        else:
            format_max = self.format_max

        format_vrml: None | str | Unset
        if isinstance(self.format_vrml, Unset):
            format_vrml = UNSET
        else:
            format_vrml = self.format_vrml

        revisiondate = self.revisiondate

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

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
        if min_x is not UNSET:
            field_dict["Min_x"] = min_x
        if min_y is not UNSET:
            field_dict["Min_y"] = min_y
        if max_x is not UNSET:
            field_dict["Max_x"] = max_x
        if max_y is not UNSET:
            field_dict["Max_y"] = max_y
        if format_3ds is not UNSET:
            field_dict["Format_3DS"] = format_3ds
        if format_fbx is not UNSET:
            field_dict["Format_FBX"] = format_fbx
        if format_max is not UNSET:
            field_dict["Format_MAX"] = format_max
        if format_vrml is not UNSET:
            field_dict["Format_VRML"] = format_vrml
        if revisiondate is not UNSET:
            field_dict["REVISIONDATE"] = revisiondate
        if remarks is not UNSET:
            field_dict["REMARKS"] = remarks
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

        def _parse_min_x(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_x = _parse_min_x(d.pop("Min_x", UNSET))

        def _parse_min_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_y = _parse_min_y(d.pop("Min_y", UNSET))

        def _parse_max_x(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_x = _parse_max_x(d.pop("Max_x", UNSET))

        def _parse_max_y(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_y = _parse_max_y(d.pop("Max_y", UNSET))

        def _parse_format_3ds(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_3ds = _parse_format_3ds(d.pop("Format_3DS", UNSET))

        def _parse_format_fbx(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_fbx = _parse_format_fbx(d.pop("Format_FBX", UNSET))

        def _parse_format_max(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_max = _parse_format_max(d.pop("Format_MAX", UNSET))

        def _parse_format_vrml(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_vrml = _parse_format_vrml(d.pop("Format_VRML", UNSET))

        revisiondate = d.pop("REVISIONDATE", UNSET)

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("REMARKS", UNSET))

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
            min_x=min_x,
            min_y=min_y,
            max_x=max_x,
            max_y=max_y,
            format_3ds=format_3ds,
            format_fbx=format_fbx,
            format_max=format_max,
            format_vrml=format_vrml,
            revisiondate=revisiondate,
            remarks=remarks,
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
