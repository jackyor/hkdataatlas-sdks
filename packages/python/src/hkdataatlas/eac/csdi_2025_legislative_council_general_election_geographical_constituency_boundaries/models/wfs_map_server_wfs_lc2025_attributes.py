from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLC2025Attributes")


@_attrs_define
class WfsMapServerWfsLC2025Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        lc_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        lc_chi (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        lc_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    lc_code: None | str | Unset = UNSET
    lc_chi: None | str | Unset = UNSET
    lc_eng: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        lc_code: None | str | Unset
        if isinstance(self.lc_code, Unset):
            lc_code = UNSET
        else:
            lc_code = self.lc_code

        lc_chi: None | str | Unset
        if isinstance(self.lc_chi, Unset):
            lc_chi = UNSET
        else:
            lc_chi = self.lc_chi

        lc_eng: None | str | Unset
        if isinstance(self.lc_eng, Unset):
            lc_eng = UNSET
        else:
            lc_eng = self.lc_eng

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
        if lc_code is not UNSET:
            field_dict["LC_Code"] = lc_code
        if lc_chi is not UNSET:
            field_dict["LC_CHI"] = lc_chi
        if lc_eng is not UNSET:
            field_dict["LC_ENG"] = lc_eng
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

        def _parse_lc_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lc_code = _parse_lc_code(d.pop("LC_Code", UNSET))

        def _parse_lc_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lc_chi = _parse_lc_chi(d.pop("LC_CHI", UNSET))

        def _parse_lc_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lc_eng = _parse_lc_eng(d.pop("LC_ENG", UNSET))

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

        wfs_map_server_wfs_lc2025_attributes = cls(
            objectid=objectid,
            shape=shape,
            lc_code=lc_code,
            lc_chi=lc_chi,
            lc_eng=lc_eng,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_lc2025_attributes.additional_properties = d
        return wfs_map_server_wfs_lc2025_attributes

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
