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
        accredit_no (None | str | Unset): Publisher field type: esriFieldTypeString
        area_dc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        hk80_grid_e (float | None | Unset): Publisher field type: esriFieldTypeDouble
        hk80_grid_n (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    accredit_no: None | str | Unset = UNSET
    area_dc: float | None | Unset = UNSET
    hk80_grid_e: float | None | Unset = UNSET
    hk80_grid_n: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accredit_no: None | str | Unset
        if isinstance(self.accredit_no, Unset):
            accredit_no = UNSET
        else:
            accredit_no = self.accredit_no

        area_dc: float | None | Unset
        if isinstance(self.area_dc, Unset):
            area_dc = UNSET
        else:
            area_dc = self.area_dc

        hk80_grid_e: float | None | Unset
        if isinstance(self.hk80_grid_e, Unset):
            hk80_grid_e = UNSET
        else:
            hk80_grid_e = self.hk80_grid_e

        hk80_grid_n: float | None | Unset
        if isinstance(self.hk80_grid_n, Unset):
            hk80_grid_n = UNSET
        else:
            hk80_grid_n = self.hk80_grid_n

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accredit_no is not UNSET:
            field_dict["Accredit_no"] = accredit_no
        if area_dc is not UNSET:
            field_dict["Area_dc"] = area_dc
        if hk80_grid_e is not UNSET:
            field_dict["HK80Grid_E"] = hk80_grid_e
        if hk80_grid_n is not UNSET:
            field_dict["HK80Grid_N"] = hk80_grid_n
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_accredit_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accredit_no = _parse_accredit_no(d.pop("Accredit_no", UNSET))

        def _parse_area_dc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        area_dc = _parse_area_dc(d.pop("Area_dc", UNSET))

        def _parse_hk80_grid_e(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hk80_grid_e = _parse_hk80_grid_e(d.pop("HK80Grid_E", UNSET))

        def _parse_hk80_grid_n(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        hk80_grid_n = _parse_hk80_grid_n(d.pop("HK80Grid_N", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            accredit_no=accredit_no,
            area_dc=area_dc,
            hk80_grid_e=hk80_grid_e,
            hk80_grid_n=hk80_grid_n,
            objectid=objectid,
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
