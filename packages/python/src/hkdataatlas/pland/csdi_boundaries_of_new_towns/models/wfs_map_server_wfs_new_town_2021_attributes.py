from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsNewTown2021Attributes")


@_attrs_define
class WfsMapServerWfsNewTown2021Attributes:
    """
    Attributes:
        new_town_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        new_town_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        new_town_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
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

    new_town_en: None | str | Unset = UNSET
    new_town_tc: None | str | Unset = UNSET
    new_town_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_town_en: None | str | Unset
        if isinstance(self.new_town_en, Unset):
            new_town_en = UNSET
        else:
            new_town_en = self.new_town_en

        new_town_tc: None | str | Unset
        if isinstance(self.new_town_tc, Unset):
            new_town_tc = UNSET
        else:
            new_town_tc = self.new_town_tc

        new_town_sc: None | str | Unset
        if isinstance(self.new_town_sc, Unset):
            new_town_sc = UNSET
        else:
            new_town_sc = self.new_town_sc

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
        if new_town_en is not UNSET:
            field_dict["NewTown_en"] = new_town_en
        if new_town_tc is not UNSET:
            field_dict["NewTown_Tc"] = new_town_tc
        if new_town_sc is not UNSET:
            field_dict["NewTown_Sc"] = new_town_sc
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

        def _parse_new_town_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_town_en = _parse_new_town_en(d.pop("NewTown_en", UNSET))

        def _parse_new_town_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_town_tc = _parse_new_town_tc(d.pop("NewTown_Tc", UNSET))

        def _parse_new_town_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_town_sc = _parse_new_town_sc(d.pop("NewTown_Sc", UNSET))

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

        wfs_map_server_wfs_new_town_2021_attributes = cls(
            new_town_en=new_town_en,
            new_town_tc=new_town_tc,
            new_town_sc=new_town_sc,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_new_town_2021_attributes.additional_properties = d
        return wfs_map_server_wfs_new_town_2021_attributes

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
