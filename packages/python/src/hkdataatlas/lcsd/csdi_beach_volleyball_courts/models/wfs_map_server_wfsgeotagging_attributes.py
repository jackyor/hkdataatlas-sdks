from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_cn (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_cn (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_cn (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        gihs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        court_no_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        court_no_cn (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        ancillary_facilities_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        ancillary_facilities_cn (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        opening_hours_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        opening_hours_cn (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        phone (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        longitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        latitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        longitude_dec (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        latitude_dec (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    district_en: None | str | Unset = UNSET
    district_cn: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_cn: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_cn: None | str | Unset = UNSET
    gihs: None | str | Unset = UNSET
    court_no_en: None | str | Unset = UNSET
    court_no_cn: None | str | Unset = UNSET
    ancillary_facilities_en: None | str | Unset = UNSET
    ancillary_facilities_cn: None | str | Unset = UNSET
    opening_hours_en: None | str | Unset = UNSET
    opening_hours_cn: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude_dec: None | str | Unset = UNSET
    latitude_dec: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
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

        gihs: None | str | Unset
        if isinstance(self.gihs, Unset):
            gihs = UNSET
        else:
            gihs = self.gihs

        court_no_en: None | str | Unset
        if isinstance(self.court_no_en, Unset):
            court_no_en = UNSET
        else:
            court_no_en = self.court_no_en

        court_no_cn: None | str | Unset
        if isinstance(self.court_no_cn, Unset):
            court_no_cn = UNSET
        else:
            court_no_cn = self.court_no_cn

        ancillary_facilities_en: None | str | Unset
        if isinstance(self.ancillary_facilities_en, Unset):
            ancillary_facilities_en = UNSET
        else:
            ancillary_facilities_en = self.ancillary_facilities_en

        ancillary_facilities_cn: None | str | Unset
        if isinstance(self.ancillary_facilities_cn, Unset):
            ancillary_facilities_cn = UNSET
        else:
            ancillary_facilities_cn = self.ancillary_facilities_cn

        opening_hours_en: None | str | Unset
        if isinstance(self.opening_hours_en, Unset):
            opening_hours_en = UNSET
        else:
            opening_hours_en = self.opening_hours_en

        opening_hours_cn: None | str | Unset
        if isinstance(self.opening_hours_cn, Unset):
            opening_hours_cn = UNSET
        else:
            opening_hours_cn = self.opening_hours_cn

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

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

        longitude_dec: None | str | Unset
        if isinstance(self.longitude_dec, Unset):
            longitude_dec = UNSET
        else:
            longitude_dec = self.longitude_dec

        latitude_dec: None | str | Unset
        if isinstance(self.latitude_dec, Unset):
            latitude_dec = UNSET
        else:
            latitude_dec = self.latitude_dec

        objectid = self.objectid

        shape = self.shape

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
        if gihs is not UNSET:
            field_dict["GIHS"] = gihs
        if court_no_en is not UNSET:
            field_dict["Court_no_en"] = court_no_en
        if court_no_cn is not UNSET:
            field_dict["Court_no_cn"] = court_no_cn
        if ancillary_facilities_en is not UNSET:
            field_dict["Ancillary_facilities_en"] = ancillary_facilities_en
        if ancillary_facilities_cn is not UNSET:
            field_dict["Ancillary_facilities_cn"] = ancillary_facilities_cn
        if opening_hours_en is not UNSET:
            field_dict["Opening_hours_en"] = opening_hours_en
        if opening_hours_cn is not UNSET:
            field_dict["Opening_hours_cn"] = opening_hours_cn
        if phone is not UNSET:
            field_dict["Phone"] = phone
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude_dec is not UNSET:
            field_dict["Longitude_dec"] = longitude_dec
        if latitude_dec is not UNSET:
            field_dict["Latitude_dec"] = latitude_dec
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

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

        def _parse_gihs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gihs = _parse_gihs(d.pop("GIHS", UNSET))

        def _parse_court_no_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        court_no_en = _parse_court_no_en(d.pop("Court_no_en", UNSET))

        def _parse_court_no_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        court_no_cn = _parse_court_no_cn(d.pop("Court_no_cn", UNSET))

        def _parse_ancillary_facilities_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ancillary_facilities_en = _parse_ancillary_facilities_en(
            d.pop("Ancillary_facilities_en", UNSET)
        )

        def _parse_ancillary_facilities_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ancillary_facilities_cn = _parse_ancillary_facilities_cn(
            d.pop("Ancillary_facilities_cn", UNSET)
        )

        def _parse_opening_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_en = _parse_opening_hours_en(d.pop("Opening_hours_en", UNSET))

        def _parse_opening_hours_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_cn = _parse_opening_hours_cn(d.pop("Opening_hours_cn", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("Phone", UNSET))

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

        def _parse_longitude_dec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude_dec = _parse_longitude_dec(d.pop("Longitude_dec", UNSET))

        def _parse_latitude_dec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude_dec = _parse_latitude_dec(d.pop("Latitude_dec", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            district_en=district_en,
            district_cn=district_cn,
            name_en=name_en,
            name_cn=name_cn,
            address_en=address_en,
            address_cn=address_cn,
            gihs=gihs,
            court_no_en=court_no_en,
            court_no_cn=court_no_cn,
            ancillary_facilities_en=ancillary_facilities_en,
            ancillary_facilities_cn=ancillary_facilities_cn,
            opening_hours_en=opening_hours_en,
            opening_hours_cn=opening_hours_cn,
            phone=phone,
            longitude=longitude,
            latitude=latitude,
            longitude_dec=longitude_dec,
            latitude_dec=latitude_dec,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
