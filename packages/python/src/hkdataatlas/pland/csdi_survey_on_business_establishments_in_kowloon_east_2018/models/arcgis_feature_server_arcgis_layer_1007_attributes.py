from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1007Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1007Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        year_s_2 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        year_2_5 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        year_5_10 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        year_l_10 (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    year_s_2: int | None | Unset = UNSET
    year_2_5: int | None | Unset = UNSET
    year_5_10: int | None | Unset = UNSET
    year_l_10: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        year_s_2: int | None | Unset
        if isinstance(self.year_s_2, Unset):
            year_s_2 = UNSET
        else:
            year_s_2 = self.year_s_2

        year_2_5: int | None | Unset
        if isinstance(self.year_2_5, Unset):
            year_2_5 = UNSET
        else:
            year_2_5 = self.year_2_5

        year_5_10: int | None | Unset
        if isinstance(self.year_5_10, Unset):
            year_5_10 = UNSET
        else:
            year_5_10 = self.year_5_10

        year_l_10: int | None | Unset
        if isinstance(self.year_l_10, Unset):
            year_l_10 = UNSET
        else:
            year_l_10 = self.year_l_10

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if year_s_2 is not UNSET:
            field_dict["Year_s_2"] = year_s_2
        if year_2_5 is not UNSET:
            field_dict["Year_2_5"] = year_2_5
        if year_5_10 is not UNSET:
            field_dict["Year_5_10"] = year_5_10
        if year_l_10 is not UNSET:
            field_dict["Year_l_10"] = year_l_10

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("Area_En", UNSET))

        def _parse_year_s_2(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year_s_2 = _parse_year_s_2(d.pop("Year_s_2", UNSET))

        def _parse_year_2_5(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year_2_5 = _parse_year_2_5(d.pop("Year_2_5", UNSET))

        def _parse_year_5_10(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year_5_10 = _parse_year_5_10(d.pop("Year_5_10", UNSET))

        def _parse_year_l_10(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year_l_10 = _parse_year_l_10(d.pop("Year_l_10", UNSET))

        arcgis_feature_server_arcgis_layer_1007_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            year_s_2=year_s_2,
            year_2_5=year_2_5,
            year_5_10=year_5_10,
            year_l_10=year_l_10,
        )

        arcgis_feature_server_arcgis_layer_1007_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1007_attributes

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
