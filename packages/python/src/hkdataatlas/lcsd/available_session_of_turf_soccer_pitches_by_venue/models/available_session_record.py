from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.available_session_record_district_name_en import (
    AvailableSessionRecordDistrictNameEN,
    check_available_session_record_district_name_en,
)
from ..models.available_session_record_district_name_tc import (
    AvailableSessionRecordDistrictNameTC,
    check_available_session_record_district_name_tc,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableSessionRecord")


@_attrs_define
class AvailableSessionRecord:
    """Field dictionary for a record describing an available session of a turf soccer pitch. The source does not establish
    the complete response structure, field requiredness, or whether these fields are all present in every record. The
    catalogue lists the JSON resource at https://data.smartplay.lcsd.gov.hk/rest/cms/api/v1/publ/contents/open-
    data/turf-soccer-pitch/file.

        Attributes:
            available_courts (float | Unset): Count of available courts. The dictionary documents the data type as Number.
            available_date (datetime.date | Unset): Available date, documented as date format yyyy-mm-dd.
            district_name_en (AvailableSessionRecordDistrictNameEN | Unset): District in English.
            district_name_tc (AvailableSessionRecordDistrictNameTC | Unset): District in Traditional Chinese.
            facility_location_name_en (str | Unset): Facility location in English.
            facility_location_name_tc (str | Unset): Facility location in Traditional Chinese.
            facility_type_name_en (str | Unset): Facility type in English.
            facility_type_name_tc (str | Unset): Facility type in Traditional Chinese.
            session_end_time (str | Unset): Available session end time, documented as time format hh:mm.
            session_start_time (str | Unset): Available session start time, documented as time format hh:mm.
            venue_address_en (str | Unset): Venue address in English. The dictionary does not specify a data type.
            venue_address_tc (str | Unset): Venue address in Traditional Chinese. The dictionary does not specify a data
                type.
            venue_latitude (float | Unset): Venue latitude. The dictionary gives the example 22.3193; the example is not
                stated as a constraint.
            venue_longitude (float | Unset): Venue longitude. The dictionary gives the example 114.17403; the example is not
                stated as a constraint.
            venue_name_en (str | Unset): Venue name in English.
            venue_name_tc (str | Unset): Venue name in Traditional Chinese.
            venue_phone_no (str | Unset): Venue telephone number. The dictionary gives the example 3954 5150; it does not
                specify a data type.
    """

    available_courts: float | Unset = UNSET
    available_date: datetime.date | Unset = UNSET
    district_name_en: AvailableSessionRecordDistrictNameEN | Unset = UNSET
    district_name_tc: AvailableSessionRecordDistrictNameTC | Unset = UNSET
    facility_location_name_en: str | Unset = UNSET
    facility_location_name_tc: str | Unset = UNSET
    facility_type_name_en: str | Unset = UNSET
    facility_type_name_tc: str | Unset = UNSET
    session_end_time: str | Unset = UNSET
    session_start_time: str | Unset = UNSET
    venue_address_en: str | Unset = UNSET
    venue_address_tc: str | Unset = UNSET
    venue_latitude: float | Unset = UNSET
    venue_longitude: float | Unset = UNSET
    venue_name_en: str | Unset = UNSET
    venue_name_tc: str | Unset = UNSET
    venue_phone_no: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_courts = self.available_courts

        available_date: str | Unset = UNSET
        if not isinstance(self.available_date, Unset):
            available_date = self.available_date.isoformat()

        district_name_en: str | Unset = UNSET
        if not isinstance(self.district_name_en, Unset):
            district_name_en = self.district_name_en

        district_name_tc: str | Unset = UNSET
        if not isinstance(self.district_name_tc, Unset):
            district_name_tc = self.district_name_tc

        facility_location_name_en = self.facility_location_name_en

        facility_location_name_tc = self.facility_location_name_tc

        facility_type_name_en = self.facility_type_name_en

        facility_type_name_tc = self.facility_type_name_tc

        session_end_time = self.session_end_time

        session_start_time = self.session_start_time

        venue_address_en = self.venue_address_en

        venue_address_tc = self.venue_address_tc

        venue_latitude = self.venue_latitude

        venue_longitude = self.venue_longitude

        venue_name_en = self.venue_name_en

        venue_name_tc = self.venue_name_tc

        venue_phone_no = self.venue_phone_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_courts is not UNSET:
            field_dict["Available_Courts"] = available_courts
        if available_date is not UNSET:
            field_dict["Available_Date"] = available_date
        if district_name_en is not UNSET:
            field_dict["District_Name_EN"] = district_name_en
        if district_name_tc is not UNSET:
            field_dict["District_Name_TC"] = district_name_tc
        if facility_location_name_en is not UNSET:
            field_dict["Facility_Location_Name_EN"] = facility_location_name_en
        if facility_location_name_tc is not UNSET:
            field_dict["Facility_Location_Name_TC"] = facility_location_name_tc
        if facility_type_name_en is not UNSET:
            field_dict["Facility_Type_Name_EN"] = facility_type_name_en
        if facility_type_name_tc is not UNSET:
            field_dict["Facility_Type_Name_TC"] = facility_type_name_tc
        if session_end_time is not UNSET:
            field_dict["Session_End_Time"] = session_end_time
        if session_start_time is not UNSET:
            field_dict["Session_Start_Time"] = session_start_time
        if venue_address_en is not UNSET:
            field_dict["Venue_Address_EN"] = venue_address_en
        if venue_address_tc is not UNSET:
            field_dict["Venue_Address_TC"] = venue_address_tc
        if venue_latitude is not UNSET:
            field_dict["Venue_Latitude"] = venue_latitude
        if venue_longitude is not UNSET:
            field_dict["Venue_Longitude"] = venue_longitude
        if venue_name_en is not UNSET:
            field_dict["Venue_Name_EN"] = venue_name_en
        if venue_name_tc is not UNSET:
            field_dict["Venue_Name_TC"] = venue_name_tc
        if venue_phone_no is not UNSET:
            field_dict["Venue_Phone_No."] = venue_phone_no

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        available_courts = d.pop("Available_Courts", UNSET)

        _available_date = d.pop("Available_Date", UNSET)
        available_date: datetime.date | Unset
        if isinstance(_available_date, Unset):
            available_date = UNSET
        else:
            available_date = datetime.date.fromisoformat(_available_date)

        _district_name_en = d.pop("District_Name_EN", UNSET)
        district_name_en: AvailableSessionRecordDistrictNameEN | Unset
        if isinstance(_district_name_en, Unset):
            district_name_en = UNSET
        else:
            district_name_en = check_available_session_record_district_name_en(
                _district_name_en
            )

        _district_name_tc = d.pop("District_Name_TC", UNSET)
        district_name_tc: AvailableSessionRecordDistrictNameTC | Unset
        if isinstance(_district_name_tc, Unset):
            district_name_tc = UNSET
        else:
            district_name_tc = check_available_session_record_district_name_tc(
                _district_name_tc
            )

        facility_location_name_en = d.pop("Facility_Location_Name_EN", UNSET)

        facility_location_name_tc = d.pop("Facility_Location_Name_TC", UNSET)

        facility_type_name_en = d.pop("Facility_Type_Name_EN", UNSET)

        facility_type_name_tc = d.pop("Facility_Type_Name_TC", UNSET)

        session_end_time = d.pop("Session_End_Time", UNSET)

        session_start_time = d.pop("Session_Start_Time", UNSET)

        venue_address_en = d.pop("Venue_Address_EN", UNSET)

        venue_address_tc = d.pop("Venue_Address_TC", UNSET)

        venue_latitude = d.pop("Venue_Latitude", UNSET)

        venue_longitude = d.pop("Venue_Longitude", UNSET)

        venue_name_en = d.pop("Venue_Name_EN", UNSET)

        venue_name_tc = d.pop("Venue_Name_TC", UNSET)

        venue_phone_no = d.pop("Venue_Phone_No.", UNSET)

        available_session_record = cls(
            available_courts=available_courts,
            available_date=available_date,
            district_name_en=district_name_en,
            district_name_tc=district_name_tc,
            facility_location_name_en=facility_location_name_en,
            facility_location_name_tc=facility_location_name_tc,
            facility_type_name_en=facility_type_name_en,
            facility_type_name_tc=facility_type_name_tc,
            session_end_time=session_end_time,
            session_start_time=session_start_time,
            venue_address_en=venue_address_en,
            venue_address_tc=venue_address_tc,
            venue_latitude=venue_latitude,
            venue_longitude=venue_longitude,
            venue_name_en=venue_name_en,
            venue_name_tc=venue_name_tc,
            venue_phone_no=venue_phone_no,
        )

        available_session_record.additional_properties = d
        return available_session_record

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
