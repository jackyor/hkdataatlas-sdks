from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1017Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1017Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        aa_code (None | str | Unset): Publisher field type: esriFieldTypeString
        aa_title (None | str | Unset): Publisher field type: esriFieldTypeString
        land_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        no_of_i_bs (float | None | Unset): Publisher field type: esriFieldTypeDouble
        total_gfa (float | None | Unset): Publisher field type: esriFieldTypeDouble
        total_no_of_units (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    land_area: float | None | Unset = UNSET
    no_of_i_bs: float | None | Unset = UNSET
    total_gfa: float | None | Unset = UNSET
    total_no_of_units: float | None | Unset = UNSET
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

        land_area: float | None | Unset
        if isinstance(self.land_area, Unset):
            land_area = UNSET
        else:
            land_area = self.land_area

        no_of_i_bs: float | None | Unset
        if isinstance(self.no_of_i_bs, Unset):
            no_of_i_bs = UNSET
        else:
            no_of_i_bs = self.no_of_i_bs

        total_gfa: float | None | Unset
        if isinstance(self.total_gfa, Unset):
            total_gfa = UNSET
        else:
            total_gfa = self.total_gfa

        total_no_of_units: float | None | Unset
        if isinstance(self.total_no_of_units, Unset):
            total_no_of_units = UNSET
        else:
            total_no_of_units = self.total_no_of_units

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if land_area is not UNSET:
            field_dict["Land_area"] = land_area
        if no_of_i_bs is not UNSET:
            field_dict["No_of_IBs"] = no_of_i_bs
        if total_gfa is not UNSET:
            field_dict["Total_GFA"] = total_gfa
        if total_no_of_units is not UNSET:
            field_dict["Total_no_of_units"] = total_no_of_units

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

        def _parse_land_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        land_area = _parse_land_area(d.pop("Land_area", UNSET))

        def _parse_no_of_i_bs(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_of_i_bs = _parse_no_of_i_bs(d.pop("No_of_IBs", UNSET))

        def _parse_total_gfa(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_gfa = _parse_total_gfa(d.pop("Total_GFA", UNSET))

        def _parse_total_no_of_units(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_no_of_units = _parse_total_no_of_units(d.pop("Total_no_of_units", UNSET))

        arcgis_feature_server_arcgis_layer_1017_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            land_area=land_area,
            no_of_i_bs=no_of_i_bs,
            total_gfa=total_gfa,
            total_no_of_units=total_no_of_units,
        )

        arcgis_feature_server_arcgis_layer_1017_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1017_attributes

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
