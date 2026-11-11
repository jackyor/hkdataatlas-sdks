from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTileNameAttributes")


@_attrs_define
class WfsMapServerWfsTileNameAttributes:
    """
    Attributes:
        oid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        tile_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        url_1 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        url_2 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    oid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    tile_name: None | str | Unset = UNSET
    url_1: None | str | Unset = UNSET
    url_2: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oid = self.oid

        shape = self.shape

        tile_name: None | str | Unset
        if isinstance(self.tile_name, Unset):
            tile_name = UNSET
        else:
            tile_name = self.tile_name

        url_1: None | str | Unset
        if isinstance(self.url_1, Unset):
            url_1 = UNSET
        else:
            url_1 = self.url_1

        url_2: None | str | Unset
        if isinstance(self.url_2, Unset):
            url_2 = UNSET
        else:
            url_2 = self.url_2

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
        if oid is not UNSET:
            field_dict["OID"] = oid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if tile_name is not UNSET:
            field_dict["TileName"] = tile_name
        if url_1 is not UNSET:
            field_dict["URL_1"] = url_1
        if url_2 is not UNSET:
            field_dict["URL_2"] = url_2
        if shape_length is not UNSET:
            field_dict["Shape_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        oid = d.pop("OID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_tile_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tile_name = _parse_tile_name(d.pop("TileName", UNSET))

        def _parse_url_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_1 = _parse_url_1(d.pop("URL_1", UNSET))

        def _parse_url_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_2 = _parse_url_2(d.pop("URL_2", UNSET))

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

        wfs_map_server_wfs_tile_name_attributes = cls(
            oid=oid,
            shape=shape,
            tile_name=tile_name,
            url_1=url_1,
            url_2=url_2,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_tile_name_attributes.additional_properties = d
        return wfs_map_server_wfs_tile_name_attributes

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
