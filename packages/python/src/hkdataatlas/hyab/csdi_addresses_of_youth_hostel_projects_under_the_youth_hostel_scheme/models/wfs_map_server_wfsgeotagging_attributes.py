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
        hostel_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        hostel_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        hostel_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        no_of_hostel_places (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        hostel_tel (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        hostel_email (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        hostel_webpage (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        longitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        latitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        easting (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        northing (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    hostel_name_tc: None | str | Unset = UNSET
    hostel_name_sc: None | str | Unset = UNSET
    hostel_name_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    no_of_hostel_places: None | str | Unset = UNSET
    hostel_tel: None | str | Unset = UNSET
    hostel_email: None | str | Unset = UNSET
    hostel_webpage: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hostel_name_tc: None | str | Unset
        if isinstance(self.hostel_name_tc, Unset):
            hostel_name_tc = UNSET
        else:
            hostel_name_tc = self.hostel_name_tc

        hostel_name_sc: None | str | Unset
        if isinstance(self.hostel_name_sc, Unset):
            hostel_name_sc = UNSET
        else:
            hostel_name_sc = self.hostel_name_sc

        hostel_name_en: None | str | Unset
        if isinstance(self.hostel_name_en, Unset):
            hostel_name_en = UNSET
        else:
            hostel_name_en = self.hostel_name_en

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

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

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

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        no_of_hostel_places: None | str | Unset
        if isinstance(self.no_of_hostel_places, Unset):
            no_of_hostel_places = UNSET
        else:
            no_of_hostel_places = self.no_of_hostel_places

        hostel_tel: None | str | Unset
        if isinstance(self.hostel_tel, Unset):
            hostel_tel = UNSET
        else:
            hostel_tel = self.hostel_tel

        hostel_email: None | str | Unset
        if isinstance(self.hostel_email, Unset):
            hostel_email = UNSET
        else:
            hostel_email = self.hostel_email

        hostel_webpage: None | str | Unset
        if isinstance(self.hostel_webpage, Unset):
            hostel_webpage = UNSET
        else:
            hostel_webpage = self.hostel_webpage

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

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostel_name_tc is not UNSET:
            field_dict["HOSTEL_NAME_TC"] = hostel_name_tc
        if hostel_name_sc is not UNSET:
            field_dict["HOSTEL_NAME_SC"] = hostel_name_sc
        if hostel_name_en is not UNSET:
            field_dict["HOSTEL_NAME_EN"] = hostel_name_en
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if address_sc is not UNSET:
            field_dict["ADDRESS_SC"] = address_sc
        if address_en is not UNSET:
            field_dict["ADDRESS_EN"] = address_en
        if district_tc is not UNSET:
            field_dict["DISTRICT_TC"] = district_tc
        if district_sc is not UNSET:
            field_dict["DISTRICT_SC"] = district_sc
        if district_en is not UNSET:
            field_dict["DISTRICT_EN"] = district_en
        if no_of_hostel_places is not UNSET:
            field_dict["NO_OF_HOSTEL_PLACES"] = no_of_hostel_places
        if hostel_tel is not UNSET:
            field_dict["HOSTEL_TEL"] = hostel_tel
        if hostel_email is not UNSET:
            field_dict["HOSTEL_EMAIL"] = hostel_email
        if hostel_webpage is not UNSET:
            field_dict["HOSTEL_WEBPAGE"] = hostel_webpage
        if longitude is not UNSET:
            field_dict["LONGITUDE"] = longitude
        if latitude is not UNSET:
            field_dict["LATITUDE"] = latitude
        if easting is not UNSET:
            field_dict["EASTING"] = easting
        if northing is not UNSET:
            field_dict["NORTHING"] = northing
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_hostel_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostel_name_tc = _parse_hostel_name_tc(d.pop("HOSTEL_NAME_TC", UNSET))

        def _parse_hostel_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostel_name_sc = _parse_hostel_name_sc(d.pop("HOSTEL_NAME_SC", UNSET))

        def _parse_hostel_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostel_name_en = _parse_hostel_name_en(d.pop("HOSTEL_NAME_EN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("ADDRESS_SC", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("ADDRESS_EN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("DISTRICT_TC", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("DISTRICT_SC", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("DISTRICT_EN", UNSET))

        def _parse_no_of_hostel_places(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_hostel_places = _parse_no_of_hostel_places(
            d.pop("NO_OF_HOSTEL_PLACES", UNSET)
        )

        def _parse_hostel_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostel_tel = _parse_hostel_tel(d.pop("HOSTEL_TEL", UNSET))

        def _parse_hostel_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostel_email = _parse_hostel_email(d.pop("HOSTEL_EMAIL", UNSET))

        def _parse_hostel_webpage(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hostel_webpage = _parse_hostel_webpage(d.pop("HOSTEL_WEBPAGE", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("LONGITUDE", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("LATITUDE", UNSET))

        def _parse_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            hostel_name_tc=hostel_name_tc,
            hostel_name_sc=hostel_name_sc,
            hostel_name_en=hostel_name_en,
            address_tc=address_tc,
            address_sc=address_sc,
            address_en=address_en,
            district_tc=district_tc,
            district_sc=district_sc,
            district_en=district_en,
            no_of_hostel_places=no_of_hostel_places,
            hostel_tel=hostel_tel,
            hostel_email=hostel_email,
            hostel_webpage=hostel_webpage,
            longitude=longitude,
            latitude=latitude,
            easting=easting,
            northing=northing,
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
