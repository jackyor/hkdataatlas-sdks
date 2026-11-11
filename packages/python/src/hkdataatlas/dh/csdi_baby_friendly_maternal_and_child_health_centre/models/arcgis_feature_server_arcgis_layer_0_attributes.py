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
        address (None | str | Unset): Publisher field type: esriFieldTypeString
        baby_friendly_mchc (None | str | Unset): Publisher field type: esriFieldTypeString
        easting_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        geo_address (None | str | Unset): Publisher field type: esriFieldTypeString
        northing_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        region (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address: None | str | Unset = UNSET
    baby_friendly_mchc: None | str | Unset = UNSET
    easting_m: float | None | Unset = UNSET
    geo_address: None | str | Unset = UNSET
    northing_m: float | None | Unset = UNSET
    region: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        baby_friendly_mchc: None | str | Unset
        if isinstance(self.baby_friendly_mchc, Unset):
            baby_friendly_mchc = UNSET
        else:
            baby_friendly_mchc = self.baby_friendly_mchc

        easting_m: float | None | Unset
        if isinstance(self.easting_m, Unset):
            easting_m = UNSET
        else:
            easting_m = self.easting_m

        geo_address: None | str | Unset
        if isinstance(self.geo_address, Unset):
            geo_address = UNSET
        else:
            geo_address = self.geo_address

        northing_m: float | None | Unset
        if isinstance(self.northing_m, Unset):
            northing_m = UNSET
        else:
            northing_m = self.northing_m

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if baby_friendly_mchc is not UNSET:
            field_dict["Baby_Friendly_MCHC"] = baby_friendly_mchc
        if easting_m is not UNSET:
            field_dict["Easting_m"] = easting_m
        if geo_address is not UNSET:
            field_dict["GeoAddress"] = geo_address
        if northing_m is not UNSET:
            field_dict["Northing_m"] = northing_m
        if region is not UNSET:
            field_dict["Region"] = region
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("Address", UNSET))

        def _parse_baby_friendly_mchc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        baby_friendly_mchc = _parse_baby_friendly_mchc(
            d.pop("Baby_Friendly_MCHC", UNSET)
        )

        def _parse_easting_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting_m = _parse_easting_m(d.pop("Easting_m", UNSET))

        def _parse_geo_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geo_address = _parse_geo_address(d.pop("GeoAddress", UNSET))

        def _parse_northing_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing_m = _parse_northing_m(d.pop("Northing_m", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("Region", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address=address,
            baby_friendly_mchc=baby_friendly_mchc,
            easting_m=easting_m,
            geo_address=geo_address,
            northing_m=northing_m,
            region=region,
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
