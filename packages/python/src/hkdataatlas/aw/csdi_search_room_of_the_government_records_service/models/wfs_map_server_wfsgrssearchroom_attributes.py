from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgrssearchroomAttributes")


@_attrs_define
class WfsMapServerWfsgrssearchroomAttributes:
    """
    Attributes:
        chinese_address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        email_address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        english_address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        facility_name_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        facility_name_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        fax (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        latitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        longitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        opening_hours (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        telephone (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        website (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    chinese_address: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    email_address: None | str | Unset = UNSET
    english_address: None | str | Unset = UNSET
    facility_name_chinese: None | str | Unset = UNSET
    facility_name_english: None | str | Unset = UNSET
    fax: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    opening_hours: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chinese_address: None | str | Unset
        if isinstance(self.chinese_address, Unset):
            chinese_address = UNSET
        else:
            chinese_address = self.chinese_address

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        english_address: None | str | Unset
        if isinstance(self.english_address, Unset):
            english_address = UNSET
        else:
            english_address = self.english_address

        facility_name_chinese: None | str | Unset
        if isinstance(self.facility_name_chinese, Unset):
            facility_name_chinese = UNSET
        else:
            facility_name_chinese = self.facility_name_chinese

        facility_name_english: None | str | Unset
        if isinstance(self.facility_name_english, Unset):
            facility_name_english = UNSET
        else:
            facility_name_english = self.facility_name_english

        fax: None | str | Unset
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

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

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        opening_hours: None | str | Unset
        if isinstance(self.opening_hours, Unset):
            opening_hours = UNSET
        else:
            opening_hours = self.opening_hours

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chinese_address is not UNSET:
            field_dict["Chinese_Address"] = chinese_address
        if district is not UNSET:
            field_dict["District"] = district
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if email_address is not UNSET:
            field_dict["Email_Address"] = email_address
        if english_address is not UNSET:
            field_dict["English_Address"] = english_address
        if facility_name_chinese is not UNSET:
            field_dict["Facility_Name_Chinese"] = facility_name_chinese
        if facility_name_english is not UNSET:
            field_dict["Facility_Name_English"] = facility_name_english
        if fax is not UNSET:
            field_dict["Fax"] = fax
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if opening_hours is not UNSET:
            field_dict["Opening_Hours"] = opening_hours
        if telephone is not UNSET:
            field_dict["Telephone"] = telephone
        if website is not UNSET:
            field_dict["Website"] = website
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_chinese_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_address = _parse_chinese_address(d.pop("Chinese_Address", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("District", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("Email_Address", UNSET))

        def _parse_english_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_address = _parse_english_address(d.pop("English_Address", UNSET))

        def _parse_facility_name_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_chinese = _parse_facility_name_chinese(
            d.pop("Facility_Name_Chinese", UNSET)
        )

        def _parse_facility_name_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_english = _parse_facility_name_english(
            d.pop("Facility_Name_English", UNSET)
        )

        def _parse_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax = _parse_fax(d.pop("Fax", UNSET))

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

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_opening_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours = _parse_opening_hours(d.pop("Opening_Hours", UNSET))

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("Telephone", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("Website", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgrssearchroom_attributes = cls(
            chinese_address=chinese_address,
            district=district,
            easting=easting,
            email_address=email_address,
            english_address=english_address,
            facility_name_chinese=facility_name_chinese,
            facility_name_english=facility_name_english,
            fax=fax,
            latitude=latitude,
            longitude=longitude,
            northing=northing,
            opening_hours=opening_hours,
            telephone=telephone,
            website=website,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgrssearchroom_attributes.additional_properties = d
        return wfs_map_server_wfsgrssearchroom_attributes

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
