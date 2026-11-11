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
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        email_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        email_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number_en (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        opening_hours_en (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        premises_based_y_n (None | str | Unset): Publisher field type: esriFieldTypeString
        site_area_sq_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        telephone_en (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        website_en (None | str | Unset): Publisher field type: esriFieldTypeString
        website_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    email_address_en: None | str | Unset = UNSET
    email_address_tc: None | str | Unset = UNSET
    facility_name_en: None | str | Unset = UNSET
    facility_name_tc: None | str | Unset = UNSET
    fax_number_en: None | str | Unset = UNSET
    fax_number_tc: None | str | Unset = UNSET
    last_update: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    opening_hours_en: None | str | Unset = UNSET
    opening_hours_tc: None | str | Unset = UNSET
    premises_based_y_n: None | str | Unset = UNSET
    site_area_sq_m: float | None | Unset = UNSET
    telephone_en: None | str | Unset = UNSET
    telephone_tc: None | str | Unset = UNSET
    website_en: None | str | Unset = UNSET
    website_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        dataset_en: None | str | Unset
        if isinstance(self.dataset_en, Unset):
            dataset_en = UNSET
        else:
            dataset_en = self.dataset_en

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        email_address_en: None | str | Unset
        if isinstance(self.email_address_en, Unset):
            email_address_en = UNSET
        else:
            email_address_en = self.email_address_en

        email_address_tc: None | str | Unset
        if isinstance(self.email_address_tc, Unset):
            email_address_tc = UNSET
        else:
            email_address_tc = self.email_address_tc

        facility_name_en: None | str | Unset
        if isinstance(self.facility_name_en, Unset):
            facility_name_en = UNSET
        else:
            facility_name_en = self.facility_name_en

        facility_name_tc: None | str | Unset
        if isinstance(self.facility_name_tc, Unset):
            facility_name_tc = UNSET
        else:
            facility_name_tc = self.facility_name_tc

        fax_number_en: None | str | Unset
        if isinstance(self.fax_number_en, Unset):
            fax_number_en = UNSET
        else:
            fax_number_en = self.fax_number_en

        fax_number_tc: None | str | Unset
        if isinstance(self.fax_number_tc, Unset):
            fax_number_tc = UNSET
        else:
            fax_number_tc = self.fax_number_tc

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        opening_hours_en: None | str | Unset
        if isinstance(self.opening_hours_en, Unset):
            opening_hours_en = UNSET
        else:
            opening_hours_en = self.opening_hours_en

        opening_hours_tc: None | str | Unset
        if isinstance(self.opening_hours_tc, Unset):
            opening_hours_tc = UNSET
        else:
            opening_hours_tc = self.opening_hours_tc

        premises_based_y_n: None | str | Unset
        if isinstance(self.premises_based_y_n, Unset):
            premises_based_y_n = UNSET
        else:
            premises_based_y_n = self.premises_based_y_n

        site_area_sq_m: float | None | Unset
        if isinstance(self.site_area_sq_m, Unset):
            site_area_sq_m = UNSET
        else:
            site_area_sq_m = self.site_area_sq_m

        telephone_en: None | str | Unset
        if isinstance(self.telephone_en, Unset):
            telephone_en = UNSET
        else:
            telephone_en = self.telephone_en

        telephone_tc: None | str | Unset
        if isinstance(self.telephone_tc, Unset):
            telephone_tc = UNSET
        else:
            telephone_tc = self.telephone_tc

        website_en: None | str | Unset
        if isinstance(self.website_en, Unset):
            website_en = UNSET
        else:
            website_en = self.website_en

        website_tc: None | str | Unset
        if isinstance(self.website_tc, Unset):
            website_tc = UNSET
        else:
            website_tc = self.website_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if dataset_en is not UNSET:
            field_dict["Dataset_EN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["Dataset_TC"] = dataset_tc
        if district_en is not UNSET:
            field_dict["District_EN"] = district_en
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if email_address_en is not UNSET:
            field_dict["Email_Address_EN"] = email_address_en
        if email_address_tc is not UNSET:
            field_dict["Email_Address_TC"] = email_address_tc
        if facility_name_en is not UNSET:
            field_dict["Facility_Name_EN"] = facility_name_en
        if facility_name_tc is not UNSET:
            field_dict["Facility_Name_TC"] = facility_name_tc
        if fax_number_en is not UNSET:
            field_dict["Fax_Number_EN"] = fax_number_en
        if fax_number_tc is not UNSET:
            field_dict["Fax_Number_TC"] = fax_number_tc
        if last_update is not UNSET:
            field_dict["Last_Update"] = last_update
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if opening_hours_en is not UNSET:
            field_dict["Opening_Hours_EN"] = opening_hours_en
        if opening_hours_tc is not UNSET:
            field_dict["Opening_Hours_TC"] = opening_hours_tc
        if premises_based_y_n is not UNSET:
            field_dict["Premises_based_Y_N"] = premises_based_y_n
        if site_area_sq_m is not UNSET:
            field_dict["Site_area_sq_m"] = site_area_sq_m
        if telephone_en is not UNSET:
            field_dict["Telephone_EN"] = telephone_en
        if telephone_tc is not UNSET:
            field_dict["Telephone_TC"] = telephone_tc
        if website_en is not UNSET:
            field_dict["Website_EN"] = website_en
        if website_tc is not UNSET:
            field_dict["Website_TC"] = website_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("Dataset_EN", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("Dataset_TC", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_EN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_email_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address_en = _parse_email_address_en(d.pop("Email_Address_EN", UNSET))

        def _parse_email_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address_tc = _parse_email_address_tc(d.pop("Email_Address_TC", UNSET))

        def _parse_facility_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_en = _parse_facility_name_en(d.pop("Facility_Name_EN", UNSET))

        def _parse_facility_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_tc = _parse_facility_name_tc(d.pop("Facility_Name_TC", UNSET))

        def _parse_fax_number_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_en = _parse_fax_number_en(d.pop("Fax_Number_EN", UNSET))

        def _parse_fax_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_tc = _parse_fax_number_tc(d.pop("Fax_Number_TC", UNSET))

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("Last_Update", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_opening_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_en = _parse_opening_hours_en(d.pop("Opening_Hours_EN", UNSET))

        def _parse_opening_hours_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_tc = _parse_opening_hours_tc(d.pop("Opening_Hours_TC", UNSET))

        def _parse_premises_based_y_n(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        premises_based_y_n = _parse_premises_based_y_n(
            d.pop("Premises_based_Y_N", UNSET)
        )

        def _parse_site_area_sq_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        site_area_sq_m = _parse_site_area_sq_m(d.pop("Site_area_sq_m", UNSET))

        def _parse_telephone_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_en = _parse_telephone_en(d.pop("Telephone_EN", UNSET))

        def _parse_telephone_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_tc = _parse_telephone_tc(d.pop("Telephone_TC", UNSET))

        def _parse_website_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_en = _parse_website_en(d.pop("Website_EN", UNSET))

        def _parse_website_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_tc = _parse_website_tc(d.pop("Website_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_en=address_en,
            address_tc=address_tc,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            district_en=district_en,
            district_tc=district_tc,
            easting=easting,
            email_address_en=email_address_en,
            email_address_tc=email_address_tc,
            facility_name_en=facility_name_en,
            facility_name_tc=facility_name_tc,
            fax_number_en=fax_number_en,
            fax_number_tc=fax_number_tc,
            last_update=last_update,
            latitude=latitude,
            longitude=longitude,
            northing=northing,
            opening_hours_en=opening_hours_en,
            opening_hours_tc=opening_hours_tc,
            premises_based_y_n=premises_based_y_n,
            site_area_sq_m=site_area_sq_m,
            telephone_en=telephone_en,
            telephone_tc=telephone_tc,
            website_en=website_en,
            website_tc=website_tc,
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
