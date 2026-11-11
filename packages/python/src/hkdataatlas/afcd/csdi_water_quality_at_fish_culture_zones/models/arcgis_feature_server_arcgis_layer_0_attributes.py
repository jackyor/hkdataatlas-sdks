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
        objectid (None | str | Unset): Publisher field type: esriFieldTypeString
        site_en (None | str | Unset): Publisher field type: esriFieldTypeString
        site_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        year (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        data (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
    """

    objectid: None | str | Unset = UNSET
    site_en: None | str | Unset = UNSET
    site_tc: None | str | Unset = UNSET
    year: None | str | Unset = UNSET
    remarks: None | str | Unset = UNSET
    data: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    objectid_1: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid: None | str | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        site_en: None | str | Unset
        if isinstance(self.site_en, Unset):
            site_en = UNSET
        else:
            site_en = self.site_en

        site_tc: None | str | Unset
        if isinstance(self.site_tc, Unset):
            site_tc = UNSET
        else:
            site_tc = self.site_tc

        year: None | str | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        remarks: None | str | Unset
        if isinstance(self.remarks, Unset):
            remarks = UNSET
        else:
            remarks = self.remarks

        data: None | str | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        else:
            data = self.data

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        objectid_1 = self.objectid_1

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if site_en is not UNSET:
            field_dict["Site_EN"] = site_en
        if site_tc is not UNSET:
            field_dict["Site_TC"] = site_tc
        if year is not UNSET:
            field_dict["Year"] = year
        if remarks is not UNSET:
            field_dict["Remarks"] = remarks
        if data is not UNSET:
            field_dict["Data"] = data
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_objectid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        def _parse_site_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_en = _parse_site_en(d.pop("Site_EN", UNSET))

        def _parse_site_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_tc = _parse_site_tc(d.pop("Site_TC", UNSET))

        def _parse_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year = _parse_year(d.pop("Year", UNSET))

        def _parse_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks = _parse_remarks(d.pop("Remarks", UNSET))

        def _parse_data(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data = _parse_data(d.pop("Data", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        objectid_1 = d.pop("OBJECTID_1", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            site_en=site_en,
            site_tc=site_tc,
            year=year,
            remarks=remarks,
            data=data,
            latitude=latitude,
            longitude=longitude,
            objectid_1=objectid_1,
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
