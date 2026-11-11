from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1010Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1010Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        aa_code (None | str | Unset): Publisher field type: esriFieldTypeString
        aa_title (None | str | Unset): Publisher field type: esriFieldTypeString
        year_5 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        year_5_7 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        year_7 (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    year_5: float | None | Unset = UNSET
    year_5_7: float | None | Unset = UNSET
    year_7: float | None | Unset = UNSET
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

        year_5: float | None | Unset
        if isinstance(self.year_5, Unset):
            year_5 = UNSET
        else:
            year_5 = self.year_5

        year_5_7: float | None | Unset
        if isinstance(self.year_5_7, Unset):
            year_5_7 = UNSET
        else:
            year_5_7 = self.year_5_7

        year_7: float | None | Unset
        if isinstance(self.year_7, Unset):
            year_7 = UNSET
        else:
            year_7 = self.year_7

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if year_5 is not UNSET:
            field_dict["Year_5"] = year_5
        if year_5_7 is not UNSET:
            field_dict["Year_5_7"] = year_5_7
        if year_7 is not UNSET:
            field_dict["Year_7"] = year_7

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

        def _parse_year_5(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year_5 = _parse_year_5(d.pop("Year_5", UNSET))

        def _parse_year_5_7(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year_5_7 = _parse_year_5_7(d.pop("Year_5_7", UNSET))

        def _parse_year_7(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year_7 = _parse_year_7(d.pop("Year_7", UNSET))

        arcgis_feature_server_arcgis_layer_1010_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            year_5=year_5,
            year_5_7=year_5_7,
            year_7=year_7,
        )

        arcgis_feature_server_arcgis_layer_1010_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1010_attributes

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
