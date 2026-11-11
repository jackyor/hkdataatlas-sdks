from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsboulderAttributes")


@_attrs_define
class WfsMapServerWfsboulderAttributes:
    """
    Attributes:
        fid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        boulder_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        area_cover (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        bould_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        bould_1m (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        bould_1_2m (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        bould_2_5m (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        bould_5m (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    fid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    boulder_id: None | str | Unset = UNSET
    area_cover: None | str | Unset = UNSET
    bould_type: None | str | Unset = UNSET
    bould_1m: None | str | Unset = UNSET
    bould_1_2m: None | str | Unset = UNSET
    bould_2_5m: None | str | Unset = UNSET
    bould_5m: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fid = self.fid

        shape = self.shape

        boulder_id: None | str | Unset
        if isinstance(self.boulder_id, Unset):
            boulder_id = UNSET
        else:
            boulder_id = self.boulder_id

        area_cover: None | str | Unset
        if isinstance(self.area_cover, Unset):
            area_cover = UNSET
        else:
            area_cover = self.area_cover

        bould_type: None | str | Unset
        if isinstance(self.bould_type, Unset):
            bould_type = UNSET
        else:
            bould_type = self.bould_type

        bould_1m: None | str | Unset
        if isinstance(self.bould_1m, Unset):
            bould_1m = UNSET
        else:
            bould_1m = self.bould_1m

        bould_1_2m: None | str | Unset
        if isinstance(self.bould_1_2m, Unset):
            bould_1_2m = UNSET
        else:
            bould_1_2m = self.bould_1_2m

        bould_2_5m: None | str | Unset
        if isinstance(self.bould_2_5m, Unset):
            bould_2_5m = UNSET
        else:
            bould_2_5m = self.bould_2_5m

        bould_5m: None | str | Unset
        if isinstance(self.bould_5m, Unset):
            bould_5m = UNSET
        else:
            bould_5m = self.bould_5m

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
        if fid is not UNSET:
            field_dict["FID"] = fid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if boulder_id is not UNSET:
            field_dict["BOULDER_ID"] = boulder_id
        if area_cover is not UNSET:
            field_dict["AREA_COVER"] = area_cover
        if bould_type is not UNSET:
            field_dict["BOULD_TYPE"] = bould_type
        if bould_1m is not UNSET:
            field_dict["BOULD_1M"] = bould_1m
        if bould_1_2m is not UNSET:
            field_dict["BOULD_1_2M"] = bould_1_2m
        if bould_2_5m is not UNSET:
            field_dict["BOULD_2_5M"] = bould_2_5m
        if bould_5m is not UNSET:
            field_dict["BOULD_5M"] = bould_5m
        if shape_length is not UNSET:
            field_dict["Shape_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fid = d.pop("FID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_boulder_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        boulder_id = _parse_boulder_id(d.pop("BOULDER_ID", UNSET))

        def _parse_area_cover(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_cover = _parse_area_cover(d.pop("AREA_COVER", UNSET))

        def _parse_bould_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bould_type = _parse_bould_type(d.pop("BOULD_TYPE", UNSET))

        def _parse_bould_1m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bould_1m = _parse_bould_1m(d.pop("BOULD_1M", UNSET))

        def _parse_bould_1_2m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bould_1_2m = _parse_bould_1_2m(d.pop("BOULD_1_2M", UNSET))

        def _parse_bould_2_5m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bould_2_5m = _parse_bould_2_5m(d.pop("BOULD_2_5M", UNSET))

        def _parse_bould_5m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bould_5m = _parse_bould_5m(d.pop("BOULD_5M", UNSET))

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

        wfs_map_server_wfsboulder_attributes = cls(
            fid=fid,
            shape=shape,
            boulder_id=boulder_id,
            area_cover=area_cover,
            bould_type=bould_type,
            bould_1m=bould_1m,
            bould_1_2m=bould_1_2m,
            bould_2_5m=bould_2_5m,
            bould_5m=bould_5m,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfsboulder_attributes.additional_properties = d
        return wfs_map_server_wfsboulder_attributes

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
