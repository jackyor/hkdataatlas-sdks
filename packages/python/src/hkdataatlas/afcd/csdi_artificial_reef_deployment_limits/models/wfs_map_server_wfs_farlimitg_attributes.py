from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsFARLIMITGAttributes")


@_attrs_define
class WfsMapServerWfsFARLIMITGAttributes:
    """
    Attributes:
        limit_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        last_updat (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        shape_st_ar (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_st_le (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    limit_name: None | str | Unset = UNSET
    last_updat: None | str | Unset = UNSET
    shape_st_ar: float | None | Unset = UNSET
    shape_st_le: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit_name: None | str | Unset
        if isinstance(self.limit_name, Unset):
            limit_name = UNSET
        else:
            limit_name = self.limit_name

        last_updat: None | str | Unset
        if isinstance(self.last_updat, Unset):
            last_updat = UNSET
        else:
            last_updat = self.last_updat

        shape_st_ar: float | None | Unset
        if isinstance(self.shape_st_ar, Unset):
            shape_st_ar = UNSET
        else:
            shape_st_ar = self.shape_st_ar

        shape_st_le: float | None | Unset
        if isinstance(self.shape_st_le, Unset):
            shape_st_le = UNSET
        else:
            shape_st_le = self.shape_st_le

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
        if limit_name is not UNSET:
            field_dict["LIMIT_NAME"] = limit_name
        if last_updat is not UNSET:
            field_dict["LAST_UPDAT"] = last_updat
        if shape_st_ar is not UNSET:
            field_dict["Shape_STAr"] = shape_st_ar
        if shape_st_le is not UNSET:
            field_dict["Shape_STLe"] = shape_st_le
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

        def _parse_limit_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        limit_name = _parse_limit_name(d.pop("LIMIT_NAME", UNSET))

        def _parse_last_updat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_updat = _parse_last_updat(d.pop("LAST_UPDAT", UNSET))

        def _parse_shape_st_ar(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_st_ar = _parse_shape_st_ar(d.pop("Shape_STAr", UNSET))

        def _parse_shape_st_le(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_st_le = _parse_shape_st_le(d.pop("Shape_STLe", UNSET))

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

        wfs_map_server_wfs_farlimitg_attributes = cls(
            limit_name=limit_name,
            last_updat=last_updat,
            shape_st_ar=shape_st_ar,
            shape_st_le=shape_st_le,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_farlimitg_attributes.additional_properties = d
        return wfs_map_server_wfs_farlimitg_attributes

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
