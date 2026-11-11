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
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_cn (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_cn (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_cn (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_parking_spaces_en (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_parking_spaces_cn (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (None | str | Unset): Publisher field type: esriFieldTypeString
        venue_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        venue_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        venue_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        region_en (None | str | Unset): Publisher field type: esriFieldTypeString
        region_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        region_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        designated_location_en (None | str | Unset): Publisher field type: esriFieldTypeString
        designated_location_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        designated_location_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        area_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        area_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        facilities_en (None | str | Unset): Publisher field type: esriFieldTypeString
        facilities_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        facilities_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_start (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_end (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity (None | str | Unset): Publisher field type: esriFieldTypeString
        enquiry_no (None | str | Unset): Publisher field type: esriFieldTypeString
        dlso_park_application_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dlso_park_application_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        dlso_park_application_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        dlso_park_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dlso_park_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        dlso_park_address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        fax (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    district_en: None | str | Unset = UNSET
    district_cn: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_cn: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_cn: None | str | Unset = UNSET
    no_of_parking_spaces_en: None | str | Unset = UNSET
    no_of_parking_spaces_cn: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    venue_name_en: None | str | Unset = UNSET
    venue_name_tc: None | str | Unset = UNSET
    venue_name_sc: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    region_en: None | str | Unset = UNSET
    region_tc: None | str | Unset = UNSET
    region_sc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    designated_location_en: None | str | Unset = UNSET
    designated_location_tc: None | str | Unset = UNSET
    designated_location_sc: None | str | Unset = UNSET
    area_en: None | str | Unset = UNSET
    area_tc: None | str | Unset = UNSET
    area_sc: None | str | Unset = UNSET
    facilities_en: None | str | Unset = UNSET
    facilities_tc: None | str | Unset = UNSET
    facilities_sc: None | str | Unset = UNSET
    opening_hours_start: None | str | Unset = UNSET
    opening_hours_end: None | str | Unset = UNSET
    capacity: None | str | Unset = UNSET
    enquiry_no: None | str | Unset = UNSET
    dlso_park_application_en: None | str | Unset = UNSET
    dlso_park_application_tc: None | str | Unset = UNSET
    dlso_park_application_sc: None | str | Unset = UNSET
    dlso_park_address_en: None | str | Unset = UNSET
    dlso_park_address_tc: None | str | Unset = UNSET
    dlso_park_address_sc: None | str | Unset = UNSET
    fax: None | str | Unset = UNSET
    remarks_en: None | str | Unset = UNSET
    remarks_tc: None | str | Unset = UNSET
    remarks_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_cn: None | str | Unset
        if isinstance(self.district_cn, Unset):
            district_cn = UNSET
        else:
            district_cn = self.district_cn

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_cn: None | str | Unset
        if isinstance(self.name_cn, Unset):
            name_cn = UNSET
        else:
            name_cn = self.name_cn

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_cn: None | str | Unset
        if isinstance(self.address_cn, Unset):
            address_cn = UNSET
        else:
            address_cn = self.address_cn

        no_of_parking_spaces_en: None | str | Unset
        if isinstance(self.no_of_parking_spaces_en, Unset):
            no_of_parking_spaces_en = UNSET
        else:
            no_of_parking_spaces_en = self.no_of_parking_spaces_en

        no_of_parking_spaces_cn: None | str | Unset
        if isinstance(self.no_of_parking_spaces_cn, Unset):
            no_of_parking_spaces_cn = UNSET
        else:
            no_of_parking_spaces_cn = self.no_of_parking_spaces_cn

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

        venue_name_en: None | str | Unset
        if isinstance(self.venue_name_en, Unset):
            venue_name_en = UNSET
        else:
            venue_name_en = self.venue_name_en

        venue_name_tc: None | str | Unset
        if isinstance(self.venue_name_tc, Unset):
            venue_name_tc = UNSET
        else:
            venue_name_tc = self.venue_name_tc

        venue_name_sc: None | str | Unset
        if isinstance(self.venue_name_sc, Unset):
            venue_name_sc = UNSET
        else:
            venue_name_sc = self.venue_name_sc

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        region_en: None | str | Unset
        if isinstance(self.region_en, Unset):
            region_en = UNSET
        else:
            region_en = self.region_en

        region_tc: None | str | Unset
        if isinstance(self.region_tc, Unset):
            region_tc = UNSET
        else:
            region_tc = self.region_tc

        region_sc: None | str | Unset
        if isinstance(self.region_sc, Unset):
            region_sc = UNSET
        else:
            region_sc = self.region_sc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        designated_location_en: None | str | Unset
        if isinstance(self.designated_location_en, Unset):
            designated_location_en = UNSET
        else:
            designated_location_en = self.designated_location_en

        designated_location_tc: None | str | Unset
        if isinstance(self.designated_location_tc, Unset):
            designated_location_tc = UNSET
        else:
            designated_location_tc = self.designated_location_tc

        designated_location_sc: None | str | Unset
        if isinstance(self.designated_location_sc, Unset):
            designated_location_sc = UNSET
        else:
            designated_location_sc = self.designated_location_sc

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        area_tc: None | str | Unset
        if isinstance(self.area_tc, Unset):
            area_tc = UNSET
        else:
            area_tc = self.area_tc

        area_sc: None | str | Unset
        if isinstance(self.area_sc, Unset):
            area_sc = UNSET
        else:
            area_sc = self.area_sc

        facilities_en: None | str | Unset
        if isinstance(self.facilities_en, Unset):
            facilities_en = UNSET
        else:
            facilities_en = self.facilities_en

        facilities_tc: None | str | Unset
        if isinstance(self.facilities_tc, Unset):
            facilities_tc = UNSET
        else:
            facilities_tc = self.facilities_tc

        facilities_sc: None | str | Unset
        if isinstance(self.facilities_sc, Unset):
            facilities_sc = UNSET
        else:
            facilities_sc = self.facilities_sc

        opening_hours_start: None | str | Unset
        if isinstance(self.opening_hours_start, Unset):
            opening_hours_start = UNSET
        else:
            opening_hours_start = self.opening_hours_start

        opening_hours_end: None | str | Unset
        if isinstance(self.opening_hours_end, Unset):
            opening_hours_end = UNSET
        else:
            opening_hours_end = self.opening_hours_end

        capacity: None | str | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        enquiry_no: None | str | Unset
        if isinstance(self.enquiry_no, Unset):
            enquiry_no = UNSET
        else:
            enquiry_no = self.enquiry_no

        dlso_park_application_en: None | str | Unset
        if isinstance(self.dlso_park_application_en, Unset):
            dlso_park_application_en = UNSET
        else:
            dlso_park_application_en = self.dlso_park_application_en

        dlso_park_application_tc: None | str | Unset
        if isinstance(self.dlso_park_application_tc, Unset):
            dlso_park_application_tc = UNSET
        else:
            dlso_park_application_tc = self.dlso_park_application_tc

        dlso_park_application_sc: None | str | Unset
        if isinstance(self.dlso_park_application_sc, Unset):
            dlso_park_application_sc = UNSET
        else:
            dlso_park_application_sc = self.dlso_park_application_sc

        dlso_park_address_en: None | str | Unset
        if isinstance(self.dlso_park_address_en, Unset):
            dlso_park_address_en = UNSET
        else:
            dlso_park_address_en = self.dlso_park_address_en

        dlso_park_address_tc: None | str | Unset
        if isinstance(self.dlso_park_address_tc, Unset):
            dlso_park_address_tc = UNSET
        else:
            dlso_park_address_tc = self.dlso_park_address_tc

        dlso_park_address_sc: None | str | Unset
        if isinstance(self.dlso_park_address_sc, Unset):
            dlso_park_address_sc = UNSET
        else:
            dlso_park_address_sc = self.dlso_park_address_sc

        fax: None | str | Unset
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        remarks_en: None | str | Unset
        if isinstance(self.remarks_en, Unset):
            remarks_en = UNSET
        else:
            remarks_en = self.remarks_en

        remarks_tc: None | str | Unset
        if isinstance(self.remarks_tc, Unset):
            remarks_tc = UNSET
        else:
            remarks_tc = self.remarks_tc

        remarks_sc: None | str | Unset
        if isinstance(self.remarks_sc, Unset):
            remarks_sc = UNSET
        else:
            remarks_sc = self.remarks_sc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if district_en is not UNSET:
            field_dict["District_en"] = district_en
        if district_cn is not UNSET:
            field_dict["District_cn"] = district_cn
        if name_en is not UNSET:
            field_dict["Name_en"] = name_en
        if name_cn is not UNSET:
            field_dict["Name_cn"] = name_cn
        if address_en is not UNSET:
            field_dict["Address_en"] = address_en
        if address_cn is not UNSET:
            field_dict["Address_cn"] = address_cn
        if no_of_parking_spaces_en is not UNSET:
            field_dict["No_of_parking_spaces_en"] = no_of_parking_spaces_en
        if no_of_parking_spaces_cn is not UNSET:
            field_dict["No_of_parking_spaces_cn"] = no_of_parking_spaces_cn
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if venue_name_en is not UNSET:
            field_dict["Venue_name_en"] = venue_name_en
        if venue_name_tc is not UNSET:
            field_dict["Venue_name_tc"] = venue_name_tc
        if venue_name_sc is not UNSET:
            field_dict["Venue_name_sc"] = venue_name_sc
        if district_tc is not UNSET:
            field_dict["District_tc"] = district_tc
        if district_sc is not UNSET:
            field_dict["District_sc"] = district_sc
        if region_en is not UNSET:
            field_dict["Region_en"] = region_en
        if region_tc is not UNSET:
            field_dict["Region_tc"] = region_tc
        if region_sc is not UNSET:
            field_dict["Region_sc"] = region_sc
        if address_tc is not UNSET:
            field_dict["Address_tc"] = address_tc
        if address_sc is not UNSET:
            field_dict["Address_sc"] = address_sc
        if designated_location_en is not UNSET:
            field_dict["Designated_location_en"] = designated_location_en
        if designated_location_tc is not UNSET:
            field_dict["Designated_location_tc"] = designated_location_tc
        if designated_location_sc is not UNSET:
            field_dict["Designated_location_sc"] = designated_location_sc
        if area_en is not UNSET:
            field_dict["Area_en"] = area_en
        if area_tc is not UNSET:
            field_dict["Area_tc"] = area_tc
        if area_sc is not UNSET:
            field_dict["Area_sc"] = area_sc
        if facilities_en is not UNSET:
            field_dict["Facilities_en"] = facilities_en
        if facilities_tc is not UNSET:
            field_dict["Facilities_tc"] = facilities_tc
        if facilities_sc is not UNSET:
            field_dict["Facilities_sc"] = facilities_sc
        if opening_hours_start is not UNSET:
            field_dict["Opening_hours_start"] = opening_hours_start
        if opening_hours_end is not UNSET:
            field_dict["Opening_hours_end"] = opening_hours_end
        if capacity is not UNSET:
            field_dict["Capacity"] = capacity
        if enquiry_no is not UNSET:
            field_dict["Enquiry_no"] = enquiry_no
        if dlso_park_application_en is not UNSET:
            field_dict["DLSO_Park_Application_en"] = dlso_park_application_en
        if dlso_park_application_tc is not UNSET:
            field_dict["DLSO_Park_Application_tc"] = dlso_park_application_tc
        if dlso_park_application_sc is not UNSET:
            field_dict["DLSO_Park_Application_sc"] = dlso_park_application_sc
        if dlso_park_address_en is not UNSET:
            field_dict["DLSO_Park_address_en"] = dlso_park_address_en
        if dlso_park_address_tc is not UNSET:
            field_dict["DLSO_Park_address_tc"] = dlso_park_address_tc
        if dlso_park_address_sc is not UNSET:
            field_dict["DLSO_Park_address_sc"] = dlso_park_address_sc
        if fax is not UNSET:
            field_dict["Fax"] = fax
        if remarks_en is not UNSET:
            field_dict["Remarks_en"] = remarks_en
        if remarks_tc is not UNSET:
            field_dict["Remarks_tc"] = remarks_tc
        if remarks_sc is not UNSET:
            field_dict["Remarks_sc"] = remarks_sc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_en", UNSET))

        def _parse_district_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_cn = _parse_district_cn(d.pop("District_cn", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("Name_en", UNSET))

        def _parse_name_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_cn = _parse_name_cn(d.pop("Name_cn", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_en", UNSET))

        def _parse_address_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_cn = _parse_address_cn(d.pop("Address_cn", UNSET))

        def _parse_no_of_parking_spaces_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_parking_spaces_en = _parse_no_of_parking_spaces_en(
            d.pop("No_of_parking_spaces_en", UNSET)
        )

        def _parse_no_of_parking_spaces_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_parking_spaces_cn = _parse_no_of_parking_spaces_cn(
            d.pop("No_of_parking_spaces_cn", UNSET)
        )

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

        def _parse_venue_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_name_en = _parse_venue_name_en(d.pop("Venue_name_en", UNSET))

        def _parse_venue_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_name_tc = _parse_venue_name_tc(d.pop("Venue_name_tc", UNSET))

        def _parse_venue_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_name_sc = _parse_venue_name_sc(d.pop("Venue_name_sc", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_tc", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("District_sc", UNSET))

        def _parse_region_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_en = _parse_region_en(d.pop("Region_en", UNSET))

        def _parse_region_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_tc = _parse_region_tc(d.pop("Region_tc", UNSET))

        def _parse_region_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_sc = _parse_region_sc(d.pop("Region_sc", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_tc", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_sc", UNSET))

        def _parse_designated_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        designated_location_en = _parse_designated_location_en(
            d.pop("Designated_location_en", UNSET)
        )

        def _parse_designated_location_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        designated_location_tc = _parse_designated_location_tc(
            d.pop("Designated_location_tc", UNSET)
        )

        def _parse_designated_location_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        designated_location_sc = _parse_designated_location_sc(
            d.pop("Designated_location_sc", UNSET)
        )

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("Area_en", UNSET))

        def _parse_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_tc = _parse_area_tc(d.pop("Area_tc", UNSET))

        def _parse_area_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_sc = _parse_area_sc(d.pop("Area_sc", UNSET))

        def _parse_facilities_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facilities_en = _parse_facilities_en(d.pop("Facilities_en", UNSET))

        def _parse_facilities_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facilities_tc = _parse_facilities_tc(d.pop("Facilities_tc", UNSET))

        def _parse_facilities_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facilities_sc = _parse_facilities_sc(d.pop("Facilities_sc", UNSET))

        def _parse_opening_hours_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_start = _parse_opening_hours_start(
            d.pop("Opening_hours_start", UNSET)
        )

        def _parse_opening_hours_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_end = _parse_opening_hours_end(d.pop("Opening_hours_end", UNSET))

        def _parse_capacity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity = _parse_capacity(d.pop("Capacity", UNSET))

        def _parse_enquiry_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        enquiry_no = _parse_enquiry_no(d.pop("Enquiry_no", UNSET))

        def _parse_dlso_park_application_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dlso_park_application_en = _parse_dlso_park_application_en(
            d.pop("DLSO_Park_Application_en", UNSET)
        )

        def _parse_dlso_park_application_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dlso_park_application_tc = _parse_dlso_park_application_tc(
            d.pop("DLSO_Park_Application_tc", UNSET)
        )

        def _parse_dlso_park_application_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dlso_park_application_sc = _parse_dlso_park_application_sc(
            d.pop("DLSO_Park_Application_sc", UNSET)
        )

        def _parse_dlso_park_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dlso_park_address_en = _parse_dlso_park_address_en(
            d.pop("DLSO_Park_address_en", UNSET)
        )

        def _parse_dlso_park_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dlso_park_address_tc = _parse_dlso_park_address_tc(
            d.pop("DLSO_Park_address_tc", UNSET)
        )

        def _parse_dlso_park_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dlso_park_address_sc = _parse_dlso_park_address_sc(
            d.pop("DLSO_Park_address_sc", UNSET)
        )

        def _parse_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax = _parse_fax(d.pop("Fax", UNSET))

        def _parse_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_en = _parse_remarks_en(d.pop("Remarks_en", UNSET))

        def _parse_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_tc = _parse_remarks_tc(d.pop("Remarks_tc", UNSET))

        def _parse_remarks_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_sc = _parse_remarks_sc(d.pop("Remarks_sc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            district_en=district_en,
            district_cn=district_cn,
            name_en=name_en,
            name_cn=name_cn,
            address_en=address_en,
            address_cn=address_cn,
            no_of_parking_spaces_en=no_of_parking_spaces_en,
            no_of_parking_spaces_cn=no_of_parking_spaces_cn,
            latitude=latitude,
            longitude=longitude,
            northing=northing,
            easting=easting,
            venue_name_en=venue_name_en,
            venue_name_tc=venue_name_tc,
            venue_name_sc=venue_name_sc,
            district_tc=district_tc,
            district_sc=district_sc,
            region_en=region_en,
            region_tc=region_tc,
            region_sc=region_sc,
            address_tc=address_tc,
            address_sc=address_sc,
            designated_location_en=designated_location_en,
            designated_location_tc=designated_location_tc,
            designated_location_sc=designated_location_sc,
            area_en=area_en,
            area_tc=area_tc,
            area_sc=area_sc,
            facilities_en=facilities_en,
            facilities_tc=facilities_tc,
            facilities_sc=facilities_sc,
            opening_hours_start=opening_hours_start,
            opening_hours_end=opening_hours_end,
            capacity=capacity,
            enquiry_no=enquiry_no,
            dlso_park_application_en=dlso_park_application_en,
            dlso_park_application_tc=dlso_park_application_tc,
            dlso_park_application_sc=dlso_park_application_sc,
            dlso_park_address_en=dlso_park_address_en,
            dlso_park_address_tc=dlso_park_address_tc,
            dlso_park_address_sc=dlso_park_address_sc,
            fax=fax,
            remarks_en=remarks_en,
            remarks_tc=remarks_tc,
            remarks_sc=remarks_sc,
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
