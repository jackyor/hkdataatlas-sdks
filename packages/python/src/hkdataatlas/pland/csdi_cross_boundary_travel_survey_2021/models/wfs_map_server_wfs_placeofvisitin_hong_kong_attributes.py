from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsPlaceofvisitinHongKongAttributes")


@_attrs_define
class WfsMapServerWfsPlaceofvisitinHongKongAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        place_of_visit_in_hong_kong_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        place_of_visit_in_hong_kong_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        place_of_visit_in_hong_kong_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    place_of_visit_in_hong_kong_en: None | str | Unset = UNSET
    place_of_visit_in_hong_kong_tc: None | str | Unset = UNSET
    place_of_visit_in_hong_kong_sc: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        place_of_visit_in_hong_kong_en: None | str | Unset
        if isinstance(self.place_of_visit_in_hong_kong_en, Unset):
            place_of_visit_in_hong_kong_en = UNSET
        else:
            place_of_visit_in_hong_kong_en = self.place_of_visit_in_hong_kong_en

        place_of_visit_in_hong_kong_tc: None | str | Unset
        if isinstance(self.place_of_visit_in_hong_kong_tc, Unset):
            place_of_visit_in_hong_kong_tc = UNSET
        else:
            place_of_visit_in_hong_kong_tc = self.place_of_visit_in_hong_kong_tc

        place_of_visit_in_hong_kong_sc: None | str | Unset
        if isinstance(self.place_of_visit_in_hong_kong_sc, Unset):
            place_of_visit_in_hong_kong_sc = UNSET
        else:
            place_of_visit_in_hong_kong_sc = self.place_of_visit_in_hong_kong_sc

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
        if place_of_visit_in_hong_kong_en is not UNSET:
            field_dict["Place_of_visit_in_Hong_Kong_En"] = (
                place_of_visit_in_hong_kong_en
            )
        if place_of_visit_in_hong_kong_tc is not UNSET:
            field_dict["Place_of_visit_in_Hong_Kong_Tc"] = (
                place_of_visit_in_hong_kong_tc
            )
        if place_of_visit_in_hong_kong_sc is not UNSET:
            field_dict["Place_of_visit_in_Hong_Kong_Sc"] = (
                place_of_visit_in_hong_kong_sc
            )
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

        def _parse_place_of_visit_in_hong_kong_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_of_visit_in_hong_kong_en = _parse_place_of_visit_in_hong_kong_en(
            d.pop("Place_of_visit_in_Hong_Kong_En", UNSET)
        )

        def _parse_place_of_visit_in_hong_kong_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_of_visit_in_hong_kong_tc = _parse_place_of_visit_in_hong_kong_tc(
            d.pop("Place_of_visit_in_Hong_Kong_Tc", UNSET)
        )

        def _parse_place_of_visit_in_hong_kong_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_of_visit_in_hong_kong_sc = _parse_place_of_visit_in_hong_kong_sc(
            d.pop("Place_of_visit_in_Hong_Kong_Sc", UNSET)
        )

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

        wfs_map_server_wfs_placeofvisitin_hong_kong_attributes = cls(
            objectid=objectid,
            shape=shape,
            place_of_visit_in_hong_kong_en=place_of_visit_in_hong_kong_en,
            place_of_visit_in_hong_kong_tc=place_of_visit_in_hong_kong_tc,
            place_of_visit_in_hong_kong_sc=place_of_visit_in_hong_kong_sc,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_placeofvisitin_hong_kong_attributes.additional_properties = d
        return wfs_map_server_wfs_placeofvisitin_hong_kong_attributes

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
