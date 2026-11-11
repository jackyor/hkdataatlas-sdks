from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1009Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1009Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        aa_code (None | str | Unset): Publisher field type: esriFieldTypeString
        aa_title (None | str | Unset): Publisher field type: esriFieldTypeString
        year_2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        year_2_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        year_5_10 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        year_10_20 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        year_20 (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    year_2: float | None | Unset = UNSET
    year_2_5: float | None | Unset = UNSET
    year_5_10: float | None | Unset = UNSET
    year_10_20: float | None | Unset = UNSET
    year_20: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        aa_code: None | str | Unset
        if isinstance(self.aa_code, Unset):
            aa_code = UNSET
        else:
            aa_code = self.aa_code

        aa_title: None | str | Unset
        if isinstance(self.aa_title, Unset):
            aa_title = UNSET
        else:
            aa_title = self.aa_title

        year_2: float | None | Unset
        if isinstance(self.year_2, Unset):
            year_2 = UNSET
        else:
            year_2 = self.year_2

        year_2_5: float | None | Unset
        if isinstance(self.year_2_5, Unset):
            year_2_5 = UNSET
        else:
            year_2_5 = self.year_2_5

        year_5_10: float | None | Unset
        if isinstance(self.year_5_10, Unset):
            year_5_10 = UNSET
        else:
            year_5_10 = self.year_5_10

        year_10_20: float | None | Unset
        if isinstance(self.year_10_20, Unset):
            year_10_20 = UNSET
        else:
            year_10_20 = self.year_10_20

        year_20: float | None | Unset
        if isinstance(self.year_20, Unset):
            year_20 = UNSET
        else:
            year_20 = self.year_20

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if year_2 is not UNSET:
            field_dict["Year_2"] = year_2
        if year_2_5 is not UNSET:
            field_dict["Year_2_5"] = year_2_5
        if year_5_10 is not UNSET:
            field_dict["Year_5_10"] = year_5_10
        if year_10_20 is not UNSET:
            field_dict["Year_10_20"] = year_10_20
        if year_20 is not UNSET:
            field_dict["Year_20"] = year_20

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_aa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_code = _parse_aa_code(d.pop("AA_Code", UNSET))

        def _parse_aa_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_title = _parse_aa_title(d.pop("AA_Title", UNSET))

        def _parse_year_2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year_2 = _parse_year_2(d.pop("Year_2", UNSET))

        def _parse_year_2_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year_2_5 = _parse_year_2_5(d.pop("Year_2_5", UNSET))

        def _parse_year_5_10(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year_5_10 = _parse_year_5_10(d.pop("Year_5_10", UNSET))

        def _parse_year_10_20(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year_10_20 = _parse_year_10_20(d.pop("Year_10_20", UNSET))

        def _parse_year_20(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year_20 = _parse_year_20(d.pop("Year_20", UNSET))

        arcgis_feature_server_arcgis_layer_1009_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            year_2=year_2,
            year_2_5=year_2_5,
            year_5_10=year_5_10,
            year_10_20=year_10_20,
            year_20=year_20,
        )

        arcgis_feature_server_arcgis_layer_1009_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1009_attributes

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
