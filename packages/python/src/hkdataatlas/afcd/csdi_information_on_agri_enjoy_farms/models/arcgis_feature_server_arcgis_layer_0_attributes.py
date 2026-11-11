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
        farm_number (None | str | Unset): Publisher field type: esriFieldTypeString
        hk80_grid_north (None | str | Unset): Publisher field type: esriFieldTypeString
        hk80_grid_east (None | str | Unset): Publisher field type: esriFieldTypeString
        area_ft (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    farm_number: None | str | Unset = UNSET
    hk80_grid_north: None | str | Unset = UNSET
    hk80_grid_east: None | str | Unset = UNSET
    area_ft: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        farm_number: None | str | Unset
        if isinstance(self.farm_number, Unset):
            farm_number = UNSET
        else:
            farm_number = self.farm_number

        hk80_grid_north: None | str | Unset
        if isinstance(self.hk80_grid_north, Unset):
            hk80_grid_north = UNSET
        else:
            hk80_grid_north = self.hk80_grid_north

        hk80_grid_east: None | str | Unset
        if isinstance(self.hk80_grid_east, Unset):
            hk80_grid_east = UNSET
        else:
            hk80_grid_east = self.hk80_grid_east

        area_ft: None | str | Unset
        if isinstance(self.area_ft, Unset):
            area_ft = UNSET
        else:
            area_ft = self.area_ft

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if farm_number is not UNSET:
            field_dict["Farm_Number"] = farm_number
        if hk80_grid_north is not UNSET:
            field_dict["HK80Grid_North"] = hk80_grid_north
        if hk80_grid_east is not UNSET:
            field_dict["HK80Grid_East"] = hk80_grid_east
        if area_ft is not UNSET:
            field_dict["Area_ft"] = area_ft
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_farm_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        farm_number = _parse_farm_number(d.pop("Farm_Number", UNSET))

        def _parse_hk80_grid_north(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hk80_grid_north = _parse_hk80_grid_north(d.pop("HK80Grid_North", UNSET))

        def _parse_hk80_grid_east(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hk80_grid_east = _parse_hk80_grid_east(d.pop("HK80Grid_East", UNSET))

        def _parse_area_ft(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_ft = _parse_area_ft(d.pop("Area_ft", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            farm_number=farm_number,
            hk80_grid_north=hk80_grid_north,
            hk80_grid_east=hk80_grid_east,
            area_ft=area_ft,
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
