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
        name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        name_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        region_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        region_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        location_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        location_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        address_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        address_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (None | str | Unset): Publisher field type: esriFieldTypeString
        geometry_longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        geometry_latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    name_eng: None | str | Unset = UNSET
    name_chi: None | str | Unset = UNSET
    region_eng: None | str | Unset = UNSET
    region_chi: None | str | Unset = UNSET
    location_eng: None | str | Unset = UNSET
    location_chi: None | str | Unset = UNSET
    address_eng: None | str | Unset = UNSET
    address_chi: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    geometry_longitude: None | str | Unset = UNSET
    geometry_latitude: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_eng: None | str | Unset
        if isinstance(self.name_eng, Unset):
            name_eng = UNSET
        else:
            name_eng = self.name_eng

        name_chi: None | str | Unset
        if isinstance(self.name_chi, Unset):
            name_chi = UNSET
        else:
            name_chi = self.name_chi

        region_eng: None | str | Unset
        if isinstance(self.region_eng, Unset):
            region_eng = UNSET
        else:
            region_eng = self.region_eng

        region_chi: None | str | Unset
        if isinstance(self.region_chi, Unset):
            region_chi = UNSET
        else:
            region_chi = self.region_chi

        location_eng: None | str | Unset
        if isinstance(self.location_eng, Unset):
            location_eng = UNSET
        else:
            location_eng = self.location_eng

        location_chi: None | str | Unset
        if isinstance(self.location_chi, Unset):
            location_chi = UNSET
        else:
            location_chi = self.location_chi

        address_eng: None | str | Unset
        if isinstance(self.address_eng, Unset):
            address_eng = UNSET
        else:
            address_eng = self.address_eng

        address_chi: None | str | Unset
        if isinstance(self.address_chi, Unset):
            address_chi = UNSET
        else:
            address_chi = self.address_chi

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        easting: None | str | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: None | str | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        geometry_longitude: None | str | Unset
        if isinstance(self.geometry_longitude, Unset):
            geometry_longitude = UNSET
        else:
            geometry_longitude = self.geometry_longitude

        geometry_latitude: None | str | Unset
        if isinstance(self.geometry_latitude, Unset):
            geometry_latitude = UNSET
        else:
            geometry_latitude = self.geometry_latitude

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_eng is not UNSET:
            field_dict["Name_eng"] = name_eng
        if name_chi is not UNSET:
            field_dict["Name_chi"] = name_chi
        if region_eng is not UNSET:
            field_dict["Region_eng"] = region_eng
        if region_chi is not UNSET:
            field_dict["Region_chi"] = region_chi
        if location_eng is not UNSET:
            field_dict["Location_eng"] = location_eng
        if location_chi is not UNSET:
            field_dict["Location_chi"] = location_chi
        if address_eng is not UNSET:
            field_dict["Address_eng"] = address_eng
        if address_chi is not UNSET:
            field_dict["Address_chi"] = address_chi
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if geometry_longitude is not UNSET:
            field_dict["GeometryLongitude"] = geometry_longitude
        if geometry_latitude is not UNSET:
            field_dict["GeometryLatitude"] = geometry_latitude
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_eng = _parse_name_eng(d.pop("Name_eng", UNSET))

        def _parse_name_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_chi = _parse_name_chi(d.pop("Name_chi", UNSET))

        def _parse_region_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_eng = _parse_region_eng(d.pop("Region_eng", UNSET))

        def _parse_region_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_chi = _parse_region_chi(d.pop("Region_chi", UNSET))

        def _parse_location_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_eng = _parse_location_eng(d.pop("Location_eng", UNSET))

        def _parse_location_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_chi = _parse_location_chi(d.pop("Location_chi", UNSET))

        def _parse_address_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_eng = _parse_address_eng(d.pop("Address_eng", UNSET))

        def _parse_address_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chi = _parse_address_chi(d.pop("Address_chi", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_geometry_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geometry_longitude = _parse_geometry_longitude(
            d.pop("GeometryLongitude", UNSET)
        )

        def _parse_geometry_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geometry_latitude = _parse_geometry_latitude(d.pop("GeometryLatitude", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            name_eng=name_eng,
            name_chi=name_chi,
            region_eng=region_eng,
            region_chi=region_chi,
            location_eng=location_eng,
            location_chi=location_chi,
            address_eng=address_eng,
            address_chi=address_chi,
            longitude=longitude,
            latitude=latitude,
            easting=easting,
            northing=northing,
            geometry_longitude=geometry_longitude,
            geometry_latitude=geometry_latitude,
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
