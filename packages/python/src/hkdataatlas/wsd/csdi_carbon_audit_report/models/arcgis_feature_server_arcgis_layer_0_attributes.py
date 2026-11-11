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
        location_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        location_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        year (None | str | Unset): Publisher field type: esriFieldTypeString
        scope_1 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        scope_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        scope_3 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        total (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    location_eng: None | str | Unset = UNSET
    location_chi: None | str | Unset = UNSET
    year: None | str | Unset = UNSET
    scope_1: float | None | Unset = UNSET
    scope_2: float | None | Unset = UNSET
    scope_3: float | None | Unset = UNSET
    total: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        location_eng: None | str | Unset
        if isinstance(self.location_eng, Unset):
            location_eng = UNSET
        else:
            location_eng = self.location_eng

        location_chi: None | str | Unset
        if isinstance(self.location_chi, Unset):
            location_chi = UNSET
        else:
            location_chi = self.location_chi

        year: None | str | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        scope_1: float | None | Unset
        if isinstance(self.scope_1, Unset):
            scope_1 = UNSET
        else:
            scope_1 = self.scope_1

        scope_2: float | None | Unset
        if isinstance(self.scope_2, Unset):
            scope_2 = UNSET
        else:
            scope_2 = self.scope_2

        scope_3: float | None | Unset
        if isinstance(self.scope_3, Unset):
            scope_3 = UNSET
        else:
            scope_3 = self.scope_3

        total: float | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if location_eng is not UNSET:
            field_dict["LOCATION_ENG"] = location_eng
        if location_chi is not UNSET:
            field_dict["LOCATION_CHI"] = location_chi
        if year is not UNSET:
            field_dict["YEAR"] = year
        if scope_1 is not UNSET:
            field_dict["SCOPE_1"] = scope_1
        if scope_2 is not UNSET:
            field_dict["SCOPE_2"] = scope_2
        if scope_3 is not UNSET:
            field_dict["SCOPE_3"] = scope_3
        if total is not UNSET:
            field_dict["TOTAL"] = total

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_location_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_eng = _parse_location_eng(d.pop("LOCATION_ENG", UNSET))

        def _parse_location_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_chi = _parse_location_chi(d.pop("LOCATION_CHI", UNSET))

        def _parse_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year = _parse_year(d.pop("YEAR", UNSET))

        def _parse_scope_1(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        scope_1 = _parse_scope_1(d.pop("SCOPE_1", UNSET))

        def _parse_scope_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        scope_2 = _parse_scope_2(d.pop("SCOPE_2", UNSET))

        def _parse_scope_3(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        scope_3 = _parse_scope_3(d.pop("SCOPE_3", UNSET))

        def _parse_total(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total = _parse_total(d.pop("TOTAL", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            location_eng=location_eng,
            location_chi=location_chi,
            year=year,
            scope_1=scope_1,
            scope_2=scope_2,
            scope_3=scope_3,
            total=total,
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
