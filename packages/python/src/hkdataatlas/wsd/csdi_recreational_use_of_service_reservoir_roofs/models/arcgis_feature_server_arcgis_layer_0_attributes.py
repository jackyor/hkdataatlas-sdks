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
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        region (None | str | Unset): Publisher field type: esriFieldTypeString
        installation_id (None | str | Unset): Publisher field type: esriFieldTypeString
        name (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        location (None | str | Unset): Publisher field type: esriFieldTypeString
        location_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        status (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    district: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    installation_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    chinese_name: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    location_chinese: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        installation_id: None | str | Unset
        if isinstance(self.installation_id, Unset):
            installation_id = UNSET
        else:
            installation_id = self.installation_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        chinese_name: None | str | Unset
        if isinstance(self.chinese_name, Unset):
            chinese_name = UNSET
        else:
            chinese_name = self.chinese_name

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        location_chinese: None | str | Unset
        if isinstance(self.location_chinese, Unset):
            location_chinese = UNSET
        else:
            location_chinese = self.location_chinese

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if district is not UNSET:
            field_dict["DISTRICT"] = district
        if region is not UNSET:
            field_dict["REGION"] = region
        if installation_id is not UNSET:
            field_dict["INSTALLATION_ID"] = installation_id
        if name is not UNSET:
            field_dict["NAME"] = name
        if chinese_name is not UNSET:
            field_dict["CHINESE_NAME"] = chinese_name
        if location is not UNSET:
            field_dict["LOCATION"] = location
        if location_chinese is not UNSET:
            field_dict["LOCATION_CHINESE"] = location_chinese
        if status is not UNSET:
            field_dict["STATUS"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("DISTRICT", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("REGION", UNSET))

        def _parse_installation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installation_id = _parse_installation_id(d.pop("INSTALLATION_ID", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("NAME", UNSET))

        def _parse_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name = _parse_chinese_name(d.pop("CHINESE_NAME", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("LOCATION", UNSET))

        def _parse_location_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_chinese = _parse_location_chinese(d.pop("LOCATION_CHINESE", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("STATUS", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            district=district,
            region=region,
            installation_id=installation_id,
            name=name,
            chinese_name=chinese_name,
            location=location,
            location_chinese=location_chinese,
            status=status,
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
