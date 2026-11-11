from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsDrivingoffencePointsOfficeAttributes")


@_attrs_define
class WfsMapServerWfsDrivingoffencePointsOfficeAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        gmid (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        facility_name (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        facility_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        opening_hours (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        opening_hours_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        telephone (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        telephone_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        fax_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        fax_number_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        email_address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        email_address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        website (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        website_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        last_update (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    objectid: int | Unset = UNSET
    gmid: None | str | Unset = UNSET
    dataset: None | str | Unset = UNSET
    facility_name: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    facility_name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    opening_hours: None | str | Unset = UNSET
    opening_hours_tc: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    telephone_tc: None | str | Unset = UNSET
    fax_number: None | str | Unset = UNSET
    fax_number_tc: None | str | Unset = UNSET
    email_address: None | str | Unset = UNSET
    email_address_tc: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    website_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    last_update: None | str | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        gmid: None | str | Unset
        if isinstance(self.gmid, Unset):
            gmid = UNSET
        else:
            gmid = self.gmid

        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        else:
            dataset = self.dataset

        facility_name: None | str | Unset
        if isinstance(self.facility_name, Unset):
            facility_name = UNSET
        else:
            facility_name = self.facility_name

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        facility_name_tc: None | str | Unset
        if isinstance(self.facility_name_tc, Unset):
            facility_name_tc = UNSET
        else:
            facility_name_tc = self.facility_name_tc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        opening_hours: None | str | Unset
        if isinstance(self.opening_hours, Unset):
            opening_hours = UNSET
        else:
            opening_hours = self.opening_hours

        opening_hours_tc: None | str | Unset
        if isinstance(self.opening_hours_tc, Unset):
            opening_hours_tc = UNSET
        else:
            opening_hours_tc = self.opening_hours_tc

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        telephone_tc: None | str | Unset
        if isinstance(self.telephone_tc, Unset):
            telephone_tc = UNSET
        else:
            telephone_tc = self.telephone_tc

        fax_number: None | str | Unset
        if isinstance(self.fax_number, Unset):
            fax_number = UNSET
        else:
            fax_number = self.fax_number

        fax_number_tc: None | str | Unset
        if isinstance(self.fax_number_tc, Unset):
            fax_number_tc = UNSET
        else:
            fax_number_tc = self.fax_number_tc

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        email_address_tc: None | str | Unset
        if isinstance(self.email_address_tc, Unset):
            email_address_tc = UNSET
        else:
            email_address_tc = self.email_address_tc

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        website_tc: None | str | Unset
        if isinstance(self.website_tc, Unset):
            website_tc = UNSET
        else:
            website_tc = self.website_tc

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

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

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if gmid is not UNSET:
            field_dict["GMID"] = gmid
        if dataset is not UNSET:
            field_dict["Dataset"] = dataset
        if facility_name is not UNSET:
            field_dict["Facility_Name"] = facility_name
        if address is not UNSET:
            field_dict["Address"] = address
        if dataset_tc is not UNSET:
            field_dict["Dataset_TC"] = dataset_tc
        if facility_name_tc is not UNSET:
            field_dict["Facility_Name_TC"] = facility_name_tc
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if opening_hours is not UNSET:
            field_dict["Opening_Hours"] = opening_hours
        if opening_hours_tc is not UNSET:
            field_dict["Opening_Hours_TC"] = opening_hours_tc
        if telephone is not UNSET:
            field_dict["Telephone"] = telephone
        if telephone_tc is not UNSET:
            field_dict["Telephone_TC"] = telephone_tc
        if fax_number is not UNSET:
            field_dict["Fax_Number"] = fax_number
        if fax_number_tc is not UNSET:
            field_dict["Fax_Number_TC"] = fax_number_tc
        if email_address is not UNSET:
            field_dict["Email_Address"] = email_address
        if email_address_tc is not UNSET:
            field_dict["Email_Address_TC"] = email_address_tc
        if website is not UNSET:
            field_dict["Website"] = website
        if website_tc is not UNSET:
            field_dict["Website_TC"] = website_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if last_update is not UNSET:
            field_dict["Last_Update"] = last_update
        if shape is not UNSET:
            field_dict["Shape"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_gmid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gmid = _parse_gmid(d.pop("GMID", UNSET))

        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("Dataset", UNSET))

        def _parse_facility_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name = _parse_facility_name(d.pop("Facility_Name", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("Address", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("Dataset_TC", UNSET))

        def _parse_facility_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_tc = _parse_facility_name_tc(d.pop("Facility_Name_TC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_opening_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours = _parse_opening_hours(d.pop("Opening_Hours", UNSET))

        def _parse_opening_hours_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_tc = _parse_opening_hours_tc(d.pop("Opening_Hours_TC", UNSET))

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("Telephone", UNSET))

        def _parse_telephone_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_tc = _parse_telephone_tc(d.pop("Telephone_TC", UNSET))

        def _parse_fax_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number = _parse_fax_number(d.pop("Fax_Number", UNSET))

        def _parse_fax_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_tc = _parse_fax_number_tc(d.pop("Fax_Number_TC", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("Email_Address", UNSET))

        def _parse_email_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address_tc = _parse_email_address_tc(d.pop("Email_Address_TC", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("Website", UNSET))

        def _parse_website_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_tc = _parse_website_tc(d.pop("Website_TC", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

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

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("Last_Update", UNSET))

        shape = d.pop("Shape", UNSET)

        wfs_map_server_wfs_drivingoffence_points_office_attributes = cls(
            objectid=objectid,
            gmid=gmid,
            dataset=dataset,
            facility_name=facility_name,
            address=address,
            dataset_tc=dataset_tc,
            facility_name_tc=facility_name_tc,
            address_tc=address_tc,
            opening_hours=opening_hours,
            opening_hours_tc=opening_hours_tc,
            telephone=telephone,
            telephone_tc=telephone_tc,
            fax_number=fax_number,
            fax_number_tc=fax_number_tc,
            email_address=email_address,
            email_address_tc=email_address_tc,
            website=website,
            website_tc=website_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            last_update=last_update,
            shape=shape,
        )

        wfs_map_server_wfs_drivingoffence_points_office_attributes.additional_properties = d
        return wfs_map_server_wfs_drivingoffence_points_office_attributes

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
