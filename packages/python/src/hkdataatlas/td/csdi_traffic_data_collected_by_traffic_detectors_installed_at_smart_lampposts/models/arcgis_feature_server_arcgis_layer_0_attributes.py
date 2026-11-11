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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        aid_id_number (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        road_en (None | str | Unset): Publisher field type: esriFieldTypeString
        road_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        road_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        direction (None | str | Unset): Publisher field type: esriFieldTypeString
        rotation (int | None | Unset): Publisher field type: esriFieldTypeInteger
        raw_speed_vol_url (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    aid_id_number: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    road_en: None | str | Unset = UNSET
    road_tc: None | str | Unset = UNSET
    road_sc: None | str | Unset = UNSET
    direction: None | str | Unset = UNSET
    rotation: int | None | Unset = UNSET
    raw_speed_vol_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        aid_id_number: None | str | Unset
        if isinstance(self.aid_id_number, Unset):
            aid_id_number = UNSET
        else:
            aid_id_number = self.aid_id_number

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        road_en: None | str | Unset
        if isinstance(self.road_en, Unset):
            road_en = UNSET
        else:
            road_en = self.road_en

        road_tc: None | str | Unset
        if isinstance(self.road_tc, Unset):
            road_tc = UNSET
        else:
            road_tc = self.road_tc

        road_sc: None | str | Unset
        if isinstance(self.road_sc, Unset):
            road_sc = UNSET
        else:
            road_sc = self.road_sc

        direction: None | str | Unset
        if isinstance(self.direction, Unset):
            direction = UNSET
        else:
            direction = self.direction

        rotation: int | None | Unset
        if isinstance(self.rotation, Unset):
            rotation = UNSET
        else:
            rotation = self.rotation

        raw_speed_vol_url: None | str | Unset
        if isinstance(self.raw_speed_vol_url, Unset):
            raw_speed_vol_url = UNSET
        else:
            raw_speed_vol_url = self.raw_speed_vol_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aid_id_number is not UNSET:
            field_dict["AID_ID_Number"] = aid_id_number
        if district is not UNSET:
            field_dict["District"] = district
        if road_en is not UNSET:
            field_dict["Road_EN"] = road_en
        if road_tc is not UNSET:
            field_dict["Road_TC"] = road_tc
        if road_sc is not UNSET:
            field_dict["Road_SC"] = road_sc
        if direction is not UNSET:
            field_dict["Direction"] = direction
        if rotation is not UNSET:
            field_dict["Rotation"] = rotation
        if raw_speed_vol_url is not UNSET:
            field_dict["RawSpeedVolUrl"] = raw_speed_vol_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_aid_id_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aid_id_number = _parse_aid_id_number(d.pop("AID_ID_Number", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("District", UNSET))

        def _parse_road_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        road_en = _parse_road_en(d.pop("Road_EN", UNSET))

        def _parse_road_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        road_tc = _parse_road_tc(d.pop("Road_TC", UNSET))

        def _parse_road_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        road_sc = _parse_road_sc(d.pop("Road_SC", UNSET))

        def _parse_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        direction = _parse_direction(d.pop("Direction", UNSET))

        def _parse_rotation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rotation = _parse_rotation(d.pop("Rotation", UNSET))

        def _parse_raw_speed_vol_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        raw_speed_vol_url = _parse_raw_speed_vol_url(d.pop("RawSpeedVolUrl", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            aid_id_number=aid_id_number,
            district=district,
            road_en=road_en,
            road_tc=road_tc,
            road_sc=road_sc,
            direction=direction,
            rotation=rotation,
            raw_speed_vol_url=raw_speed_vol_url,
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
