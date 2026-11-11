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
        facility_category (None | str | Unset): Publisher field type: esriFieldTypeString
        eng_service_provider (None | str | Unset): Publisher field type: esriFieldTypeString
        chi_service_provider (None | str | Unset): Publisher field type: esriFieldTypeString
        eng_address (None | str | Unset): Publisher field type: esriFieldTypeString
        chi_address (None | str | Unset): Publisher field type: esriFieldTypeString
        eng_district (None | str | Unset): Publisher field type: esriFieldTypeString
        chi_district (None | str | Unset): Publisher field type: esriFieldTypeString
        eng_frequency_band_s_in_use (None | str | Unset): Publisher field type: esriFieldTypeString
        chi_frequency_band_s_in_use (None | str | Unset): Publisher field type: esriFieldTypeString
        access_point_identification (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    facility_category: None | str | Unset = UNSET
    eng_service_provider: None | str | Unset = UNSET
    chi_service_provider: None | str | Unset = UNSET
    eng_address: None | str | Unset = UNSET
    chi_address: None | str | Unset = UNSET
    eng_district: None | str | Unset = UNSET
    chi_district: None | str | Unset = UNSET
    eng_frequency_band_s_in_use: None | str | Unset = UNSET
    chi_frequency_band_s_in_use: None | str | Unset = UNSET
    access_point_identification: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facility_category: None | str | Unset
        if isinstance(self.facility_category, Unset):
            facility_category = UNSET
        else:
            facility_category = self.facility_category

        eng_service_provider: None | str | Unset
        if isinstance(self.eng_service_provider, Unset):
            eng_service_provider = UNSET
        else:
            eng_service_provider = self.eng_service_provider

        chi_service_provider: None | str | Unset
        if isinstance(self.chi_service_provider, Unset):
            chi_service_provider = UNSET
        else:
            chi_service_provider = self.chi_service_provider

        eng_address: None | str | Unset
        if isinstance(self.eng_address, Unset):
            eng_address = UNSET
        else:
            eng_address = self.eng_address

        chi_address: None | str | Unset
        if isinstance(self.chi_address, Unset):
            chi_address = UNSET
        else:
            chi_address = self.chi_address

        eng_district: None | str | Unset
        if isinstance(self.eng_district, Unset):
            eng_district = UNSET
        else:
            eng_district = self.eng_district

        chi_district: None | str | Unset
        if isinstance(self.chi_district, Unset):
            chi_district = UNSET
        else:
            chi_district = self.chi_district

        eng_frequency_band_s_in_use: None | str | Unset
        if isinstance(self.eng_frequency_band_s_in_use, Unset):
            eng_frequency_band_s_in_use = UNSET
        else:
            eng_frequency_band_s_in_use = self.eng_frequency_band_s_in_use

        chi_frequency_band_s_in_use: None | str | Unset
        if isinstance(self.chi_frequency_band_s_in_use, Unset):
            chi_frequency_band_s_in_use = UNSET
        else:
            chi_frequency_band_s_in_use = self.chi_frequency_band_s_in_use

        access_point_identification: None | str | Unset
        if isinstance(self.access_point_identification, Unset):
            access_point_identification = UNSET
        else:
            access_point_identification = self.access_point_identification

        northing: None | str | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: None | str | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

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

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if facility_category is not UNSET:
            field_dict["Facility_Category"] = facility_category
        if eng_service_provider is not UNSET:
            field_dict["Eng__Service_Provider"] = eng_service_provider
        if chi_service_provider is not UNSET:
            field_dict["Chi__Service_Provider"] = chi_service_provider
        if eng_address is not UNSET:
            field_dict["Eng__Address"] = eng_address
        if chi_address is not UNSET:
            field_dict["Chi__Address"] = chi_address
        if eng_district is not UNSET:
            field_dict["Eng__District"] = eng_district
        if chi_district is not UNSET:
            field_dict["Chi__District"] = chi_district
        if eng_frequency_band_s_in_use is not UNSET:
            field_dict["Eng__Frequency_Band_s__In_Use"] = eng_frequency_band_s_in_use
        if chi_frequency_band_s_in_use is not UNSET:
            field_dict["Chi__Frequency_Band_s__In_Use"] = chi_frequency_band_s_in_use
        if access_point_identification is not UNSET:
            field_dict["Access_Point_Identification"] = access_point_identification
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_facility_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_category = _parse_facility_category(d.pop("Facility_Category", UNSET))

        def _parse_eng_service_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eng_service_provider = _parse_eng_service_provider(
            d.pop("Eng__Service_Provider", UNSET)
        )

        def _parse_chi_service_provider(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chi_service_provider = _parse_chi_service_provider(
            d.pop("Chi__Service_Provider", UNSET)
        )

        def _parse_eng_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eng_address = _parse_eng_address(d.pop("Eng__Address", UNSET))

        def _parse_chi_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chi_address = _parse_chi_address(d.pop("Chi__Address", UNSET))

        def _parse_eng_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eng_district = _parse_eng_district(d.pop("Eng__District", UNSET))

        def _parse_chi_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chi_district = _parse_chi_district(d.pop("Chi__District", UNSET))

        def _parse_eng_frequency_band_s_in_use(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eng_frequency_band_s_in_use = _parse_eng_frequency_band_s_in_use(
            d.pop("Eng__Frequency_Band_s__In_Use", UNSET)
        )

        def _parse_chi_frequency_band_s_in_use(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chi_frequency_band_s_in_use = _parse_chi_frequency_band_s_in_use(
            d.pop("Chi__Frequency_Band_s__In_Use", UNSET)
        )

        def _parse_access_point_identification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        access_point_identification = _parse_access_point_identification(
            d.pop("Access_Point_Identification", UNSET)
        )

        def _parse_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

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

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            facility_category=facility_category,
            eng_service_provider=eng_service_provider,
            chi_service_provider=chi_service_provider,
            eng_address=eng_address,
            chi_address=chi_address,
            eng_district=eng_district,
            chi_district=chi_district,
            eng_frequency_band_s_in_use=eng_frequency_band_s_in_use,
            chi_frequency_band_s_in_use=chi_frequency_band_s_in_use,
            access_point_identification=access_point_identification,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
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
