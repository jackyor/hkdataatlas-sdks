from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsHTPolyline20250121161219Attributes")


@_attrs_define
class WfsMapServerWfsHTPolyline20250121161219Attributes:
    """
    Attributes:
        trail_id (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        trail (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        trail_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiCurvePropertyType; JSON geometry is not inferred from its
            XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    trail_id: int | None | Unset = UNSET
    trail: None | str | Unset = UNSET
    trail_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trail_id: int | None | Unset
        if isinstance(self.trail_id, Unset):
            trail_id = UNSET
        else:
            trail_id = self.trail_id

        trail: None | str | Unset
        if isinstance(self.trail, Unset):
            trail = UNSET
        else:
            trail = self.trail

        trail_tc: None | str | Unset
        if isinstance(self.trail_tc, Unset):
            trail_tc = UNSET
        else:
            trail_tc = self.trail_tc

        objectid = self.objectid

        shape = self.shape

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trail_id is not UNSET:
            field_dict["TRAIL_ID"] = trail_id
        if trail is not UNSET:
            field_dict["TRAIL"] = trail
        if trail_tc is not UNSET:
            field_dict["TRAIL_TC"] = trail_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_trail_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        trail_id = _parse_trail_id(d.pop("TRAIL_ID", UNSET))

        def _parse_trail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail = _parse_trail(d.pop("TRAIL", UNSET))

        def _parse_trail_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_tc = _parse_trail_tc(d.pop("TRAIL_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        wfs_map_server_wfs_ht_polyline_20250121161219_attributes = cls(
            trail_id=trail_id,
            trail=trail,
            trail_tc=trail_tc,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
        )

        wfs_map_server_wfs_ht_polyline_20250121161219_attributes.additional_properties = d
        return wfs_map_server_wfs_ht_polyline_20250121161219_attributes

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
