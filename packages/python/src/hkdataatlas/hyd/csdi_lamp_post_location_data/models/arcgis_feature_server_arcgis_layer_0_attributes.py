from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        lamp_no (str | Unset): Publisher field type: esriFieldTypeString
        district (str | Unset): Publisher field type: esriFieldTypeString
        primary_st (str | Unset): Publisher field type: esriFieldTypeString
        lat (float | Unset): Publisher field type: esriFieldTypeDouble
        long (float | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    lamp_no: str | Unset = UNSET
    district: str | Unset = UNSET
    primary_st: str | Unset = UNSET
    lat: float | Unset = UNSET
    long: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        lamp_no = self.lamp_no

        district = self.district

        primary_st = self.primary_st

        lat = self.lat

        long = self.long

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if lamp_no is not UNSET:
            field_dict["LAMP_NO"] = lamp_no
        if district is not UNSET:
            field_dict["DISTRICT"] = district
        if primary_st is not UNSET:
            field_dict["PRIMARY_ST"] = primary_st
        if lat is not UNSET:
            field_dict["LAT"] = lat
        if long is not UNSET:
            field_dict["LONG"] = long

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        lamp_no = d.pop("LAMP_NO", UNSET)

        district = d.pop("DISTRICT", UNSET)

        primary_st = d.pop("PRIMARY_ST", UNSET)

        lat = d.pop("LAT", UNSET)

        long = d.pop("LONG", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            lamp_no=lamp_no,
            district=district,
            primary_st=primary_st,
            lat=lat,
            long=long,
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
