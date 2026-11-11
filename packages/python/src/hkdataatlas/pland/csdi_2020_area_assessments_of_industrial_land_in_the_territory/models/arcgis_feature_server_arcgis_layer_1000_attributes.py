from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1000Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1000Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        aa_code (None | str | Unset): Publisher field type: esriFieldTypeString
        aa_title (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_i_bs_single_ownership (float | None | Unset): Publisher field type: esriFieldTypeDouble
        gfa_in_i_bs_single_ownership (float | None | Unset): Publisher field type: esriFieldTypeDouble
        no_of_i_bs_multiple_ownership (float | None | Unset): Publisher field type: esriFieldTypeDouble
        gfa_in_i_bs_multiple_ownership (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    no_of_i_bs_single_ownership: float | None | Unset = UNSET
    gfa_in_i_bs_single_ownership: float | None | Unset = UNSET
    no_of_i_bs_multiple_ownership: float | None | Unset = UNSET
    gfa_in_i_bs_multiple_ownership: float | None | Unset = UNSET
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

        no_of_i_bs_single_ownership: float | None | Unset
        if isinstance(self.no_of_i_bs_single_ownership, Unset):
            no_of_i_bs_single_ownership = UNSET
        else:
            no_of_i_bs_single_ownership = self.no_of_i_bs_single_ownership

        gfa_in_i_bs_single_ownership: float | None | Unset
        if isinstance(self.gfa_in_i_bs_single_ownership, Unset):
            gfa_in_i_bs_single_ownership = UNSET
        else:
            gfa_in_i_bs_single_ownership = self.gfa_in_i_bs_single_ownership

        no_of_i_bs_multiple_ownership: float | None | Unset
        if isinstance(self.no_of_i_bs_multiple_ownership, Unset):
            no_of_i_bs_multiple_ownership = UNSET
        else:
            no_of_i_bs_multiple_ownership = self.no_of_i_bs_multiple_ownership

        gfa_in_i_bs_multiple_ownership: float | None | Unset
        if isinstance(self.gfa_in_i_bs_multiple_ownership, Unset):
            gfa_in_i_bs_multiple_ownership = UNSET
        else:
            gfa_in_i_bs_multiple_ownership = self.gfa_in_i_bs_multiple_ownership

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if no_of_i_bs_single_ownership is not UNSET:
            field_dict["No_of_IBs_single_ownership"] = no_of_i_bs_single_ownership
        if gfa_in_i_bs_single_ownership is not UNSET:
            field_dict["GFA_in_IBs_single_ownership"] = gfa_in_i_bs_single_ownership
        if no_of_i_bs_multiple_ownership is not UNSET:
            field_dict["No_of_IBs_multiple_ownership"] = no_of_i_bs_multiple_ownership
        if gfa_in_i_bs_multiple_ownership is not UNSET:
            field_dict["GFA_in_IBs_multiple_ownership"] = gfa_in_i_bs_multiple_ownership

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

        def _parse_no_of_i_bs_single_ownership(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_of_i_bs_single_ownership = _parse_no_of_i_bs_single_ownership(
            d.pop("No_of_IBs_single_ownership", UNSET)
        )

        def _parse_gfa_in_i_bs_single_ownership(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gfa_in_i_bs_single_ownership = _parse_gfa_in_i_bs_single_ownership(
            d.pop("GFA_in_IBs_single_ownership", UNSET)
        )

        def _parse_no_of_i_bs_multiple_ownership(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_of_i_bs_multiple_ownership = _parse_no_of_i_bs_multiple_ownership(
            d.pop("No_of_IBs_multiple_ownership", UNSET)
        )

        def _parse_gfa_in_i_bs_multiple_ownership(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gfa_in_i_bs_multiple_ownership = _parse_gfa_in_i_bs_multiple_ownership(
            d.pop("GFA_in_IBs_multiple_ownership", UNSET)
        )

        arcgis_feature_server_arcgis_layer_1000_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            no_of_i_bs_single_ownership=no_of_i_bs_single_ownership,
            gfa_in_i_bs_single_ownership=gfa_in_i_bs_single_ownership,
            no_of_i_bs_multiple_ownership=no_of_i_bs_multiple_ownership,
            gfa_in_i_bs_multiple_ownership=gfa_in_i_bs_multiple_ownership,
        )

        arcgis_feature_server_arcgis_layer_1000_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1000_attributes

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
