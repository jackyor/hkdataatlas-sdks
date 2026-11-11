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
        site_code (None | str | Unset): Publisher field type: esriFieldTypeString
        location_english (None | str | Unset): Publisher field type: esriFieldTypeString
        location_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        mountpoint_nmea (None | str | Unset): Publisher field type: esriFieldTypeString
        connection_settings (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    site_code: None | str | Unset = UNSET
    location_english: None | str | Unset = UNSET
    location_chinese: None | str | Unset = UNSET
    mountpoint_nmea: None | str | Unset = UNSET
    connection_settings: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        site_code: None | str | Unset
        if isinstance(self.site_code, Unset):
            site_code = UNSET
        else:
            site_code = self.site_code

        location_english: None | str | Unset
        if isinstance(self.location_english, Unset):
            location_english = UNSET
        else:
            location_english = self.location_english

        location_chinese: None | str | Unset
        if isinstance(self.location_chinese, Unset):
            location_chinese = UNSET
        else:
            location_chinese = self.location_chinese

        mountpoint_nmea: None | str | Unset
        if isinstance(self.mountpoint_nmea, Unset):
            mountpoint_nmea = UNSET
        else:
            mountpoint_nmea = self.mountpoint_nmea

        connection_settings: None | str | Unset
        if isinstance(self.connection_settings, Unset):
            connection_settings = UNSET
        else:
            connection_settings = self.connection_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if site_code is not UNSET:
            field_dict["Site_Code"] = site_code
        if location_english is not UNSET:
            field_dict["Location_English"] = location_english
        if location_chinese is not UNSET:
            field_dict["Location_Chinese"] = location_chinese
        if mountpoint_nmea is not UNSET:
            field_dict["Mountpoint_NMEA"] = mountpoint_nmea
        if connection_settings is not UNSET:
            field_dict["Connection_Settings"] = connection_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_site_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_code = _parse_site_code(d.pop("Site_Code", UNSET))

        def _parse_location_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_english = _parse_location_english(d.pop("Location_English", UNSET))

        def _parse_location_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_chinese = _parse_location_chinese(d.pop("Location_Chinese", UNSET))

        def _parse_mountpoint_nmea(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mountpoint_nmea = _parse_mountpoint_nmea(d.pop("Mountpoint_NMEA", UNSET))

        def _parse_connection_settings(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_settings = _parse_connection_settings(
            d.pop("Connection_Settings", UNSET)
        )

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            site_code=site_code,
            location_english=location_english,
            location_chinese=location_chinese,
            mountpoint_nmea=mountpoint_nmea,
            connection_settings=connection_settings,
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
