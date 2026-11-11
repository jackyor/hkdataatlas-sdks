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
        fac_id (None | str | Unset): Publisher field type: esriFieldTypeString
        x_ground (None | str | Unset): Publisher field type: esriFieldTypeString
        y_ground (None | str | Unset): Publisher field type: esriFieldTypeString
        utm_grid (None | str | Unset): Publisher field type: esriFieldTypeString
        trail_id (None | str | Unset): Publisher field type: esriFieldTypeString
        country_park_en (None | str | Unset): Publisher field type: esriFieldTypeString
        country_park_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        utm_zone (None | str | Unset): Publisher field type: esriFieldTypeString
        trail_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        trail_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    fac_id: None | str | Unset = UNSET
    x_ground: None | str | Unset = UNSET
    y_ground: None | str | Unset = UNSET
    utm_grid: None | str | Unset = UNSET
    trail_id: None | str | Unset = UNSET
    country_park_en: None | str | Unset = UNSET
    country_park_tc: None | str | Unset = UNSET
    utm_zone: None | str | Unset = UNSET
    trail_name_en: None | str | Unset = UNSET
    trail_name_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fac_id: None | str | Unset
        if isinstance(self.fac_id, Unset):
            fac_id = UNSET
        else:
            fac_id = self.fac_id

        x_ground: None | str | Unset
        if isinstance(self.x_ground, Unset):
            x_ground = UNSET
        else:
            x_ground = self.x_ground

        y_ground: None | str | Unset
        if isinstance(self.y_ground, Unset):
            y_ground = UNSET
        else:
            y_ground = self.y_ground

        utm_grid: None | str | Unset
        if isinstance(self.utm_grid, Unset):
            utm_grid = UNSET
        else:
            utm_grid = self.utm_grid

        trail_id: None | str | Unset
        if isinstance(self.trail_id, Unset):
            trail_id = UNSET
        else:
            trail_id = self.trail_id

        country_park_en: None | str | Unset
        if isinstance(self.country_park_en, Unset):
            country_park_en = UNSET
        else:
            country_park_en = self.country_park_en

        country_park_tc: None | str | Unset
        if isinstance(self.country_park_tc, Unset):
            country_park_tc = UNSET
        else:
            country_park_tc = self.country_park_tc

        utm_zone: None | str | Unset
        if isinstance(self.utm_zone, Unset):
            utm_zone = UNSET
        else:
            utm_zone = self.utm_zone

        trail_name_en: None | str | Unset
        if isinstance(self.trail_name_en, Unset):
            trail_name_en = UNSET
        else:
            trail_name_en = self.trail_name_en

        trail_name_tc: None | str | Unset
        if isinstance(self.trail_name_tc, Unset):
            trail_name_tc = UNSET
        else:
            trail_name_tc = self.trail_name_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fac_id is not UNSET:
            field_dict["FAC_ID"] = fac_id
        if x_ground is not UNSET:
            field_dict["X_GROUND"] = x_ground
        if y_ground is not UNSET:
            field_dict["Y_GROUND"] = y_ground
        if utm_grid is not UNSET:
            field_dict["UTM_GRID"] = utm_grid
        if trail_id is not UNSET:
            field_dict["TRAIL_ID"] = trail_id
        if country_park_en is not UNSET:
            field_dict["COUNTRY_PARK_EN"] = country_park_en
        if country_park_tc is not UNSET:
            field_dict["COUNTRY_PARK_TC"] = country_park_tc
        if utm_zone is not UNSET:
            field_dict["UTM_ZONE"] = utm_zone
        if trail_name_en is not UNSET:
            field_dict["TRAIL_NAME_EN"] = trail_name_en
        if trail_name_tc is not UNSET:
            field_dict["TRAIL_NAME_TC"] = trail_name_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_fac_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_id = _parse_fac_id(d.pop("FAC_ID", UNSET))

        def _parse_x_ground(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        x_ground = _parse_x_ground(d.pop("X_GROUND", UNSET))

        def _parse_y_ground(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        y_ground = _parse_y_ground(d.pop("Y_GROUND", UNSET))

        def _parse_utm_grid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_grid = _parse_utm_grid(d.pop("UTM_GRID", UNSET))

        def _parse_trail_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_id = _parse_trail_id(d.pop("TRAIL_ID", UNSET))

        def _parse_country_park_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_park_en = _parse_country_park_en(d.pop("COUNTRY_PARK_EN", UNSET))

        def _parse_country_park_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_park_tc = _parse_country_park_tc(d.pop("COUNTRY_PARK_TC", UNSET))

        def _parse_utm_zone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_zone = _parse_utm_zone(d.pop("UTM_ZONE", UNSET))

        def _parse_trail_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_name_en = _parse_trail_name_en(d.pop("TRAIL_NAME_EN", UNSET))

        def _parse_trail_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trail_name_tc = _parse_trail_name_tc(d.pop("TRAIL_NAME_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            fac_id=fac_id,
            x_ground=x_ground,
            y_ground=y_ground,
            utm_grid=utm_grid,
            trail_id=trail_id,
            country_park_en=country_park_en,
            country_park_tc=country_park_tc,
            utm_zone=utm_zone,
            trail_name_en=trail_name_en,
            trail_name_tc=trail_name_tc,
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
