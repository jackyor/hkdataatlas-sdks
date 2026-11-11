from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1002Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1002Attributes:
    """
    Attributes:
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
        objectid (int | None | Unset): Publisher field type: esriFieldTypeInteger
        place_of_visit_in_hong_kong_en (None | str | Unset): Publisher field type: esriFieldTypeString
        y2011 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2013_14 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2015 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2017 (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid_1: int | Unset = UNSET
    objectid: int | None | Unset = UNSET
    place_of_visit_in_hong_kong_en: None | str | Unset = UNSET
    y2011: int | None | Unset = UNSET
    y2013_14: int | None | Unset = UNSET
    y2015: int | None | Unset = UNSET
    y2017: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid_1 = self.objectid_1

        objectid: int | None | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        place_of_visit_in_hong_kong_en: None | str | Unset
        if isinstance(self.place_of_visit_in_hong_kong_en, Unset):
            place_of_visit_in_hong_kong_en = UNSET
        else:
            place_of_visit_in_hong_kong_en = self.place_of_visit_in_hong_kong_en

        y2011: int | None | Unset
        if isinstance(self.y2011, Unset):
            y2011 = UNSET
        else:
            y2011 = self.y2011

        y2013_14: int | None | Unset
        if isinstance(self.y2013_14, Unset):
            y2013_14 = UNSET
        else:
            y2013_14 = self.y2013_14

        y2015: int | None | Unset
        if isinstance(self.y2015, Unset):
            y2015 = UNSET
        else:
            y2015 = self.y2015

        y2017: int | None | Unset
        if isinstance(self.y2017, Unset):
            y2017 = UNSET
        else:
            y2017 = self.y2017

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if place_of_visit_in_hong_kong_en is not UNSET:
            field_dict["Place_of_visit_in_Hong_Kong_En"] = (
                place_of_visit_in_hong_kong_en
            )
        if y2011 is not UNSET:
            field_dict["Y2011"] = y2011
        if y2013_14 is not UNSET:
            field_dict["Y2013_14"] = y2013_14
        if y2015 is not UNSET:
            field_dict["Y2015"] = y2015
        if y2017 is not UNSET:
            field_dict["Y2017"] = y2017

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid_1 = d.pop("OBJECTID_1", UNSET)

        def _parse_objectid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        def _parse_place_of_visit_in_hong_kong_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_of_visit_in_hong_kong_en = _parse_place_of_visit_in_hong_kong_en(
            d.pop("Place_of_visit_in_Hong_Kong_En", UNSET)
        )

        def _parse_y2011(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2011 = _parse_y2011(d.pop("Y2011", UNSET))

        def _parse_y2013_14(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2013_14 = _parse_y2013_14(d.pop("Y2013_14", UNSET))

        def _parse_y2015(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2015 = _parse_y2015(d.pop("Y2015", UNSET))

        def _parse_y2017(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2017 = _parse_y2017(d.pop("Y2017", UNSET))

        arcgis_feature_server_arcgis_layer_1002_attributes = cls(
            objectid_1=objectid_1,
            objectid=objectid,
            place_of_visit_in_hong_kong_en=place_of_visit_in_hong_kong_en,
            y2011=y2011,
            y2013_14=y2013_14,
            y2015=y2015,
            y2017=y2017,
        )

        arcgis_feature_server_arcgis_layer_1002_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1002_attributes

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
