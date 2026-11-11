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
        company_name_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        company_name_chin (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        address_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_chin (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        contact_person_eng (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        contact_person_chin (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        tel_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        fax_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        website_email_address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        types_of_recycling_facilities_provided_eng (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        types_of_recycling_facilities_provided_chin (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        address_longitude_lands (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        address_latitude_lands (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        address_easting_lands (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        address_northing_lands (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    company_name_eng: None | str | Unset = UNSET
    company_name_chin: None | str | Unset = UNSET
    address_eng: None | str | Unset = UNSET
    address_chin: None | str | Unset = UNSET
    contact_person_eng: None | str | Unset = UNSET
    contact_person_chin: None | str | Unset = UNSET
    tel_no: None | str | Unset = UNSET
    fax_no: None | str | Unset = UNSET
    website_email_address: None | str | Unset = UNSET
    types_of_recycling_facilities_provided_eng: None | str | Unset = UNSET
    types_of_recycling_facilities_provided_chin: None | str | Unset = UNSET
    address_longitude_lands: None | str | Unset = UNSET
    address_latitude_lands: None | str | Unset = UNSET
    address_easting_lands: None | str | Unset = UNSET
    address_northing_lands: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name_eng: None | str | Unset
        if isinstance(self.company_name_eng, Unset):
            company_name_eng = UNSET
        else:
            company_name_eng = self.company_name_eng

        company_name_chin: None | str | Unset
        if isinstance(self.company_name_chin, Unset):
            company_name_chin = UNSET
        else:
            company_name_chin = self.company_name_chin

        address_eng: None | str | Unset
        if isinstance(self.address_eng, Unset):
            address_eng = UNSET
        else:
            address_eng = self.address_eng

        address_chin: None | str | Unset
        if isinstance(self.address_chin, Unset):
            address_chin = UNSET
        else:
            address_chin = self.address_chin

        contact_person_eng: None | str | Unset
        if isinstance(self.contact_person_eng, Unset):
            contact_person_eng = UNSET
        else:
            contact_person_eng = self.contact_person_eng

        contact_person_chin: None | str | Unset
        if isinstance(self.contact_person_chin, Unset):
            contact_person_chin = UNSET
        else:
            contact_person_chin = self.contact_person_chin

        tel_no: None | str | Unset
        if isinstance(self.tel_no, Unset):
            tel_no = UNSET
        else:
            tel_no = self.tel_no

        fax_no: None | str | Unset
        if isinstance(self.fax_no, Unset):
            fax_no = UNSET
        else:
            fax_no = self.fax_no

        website_email_address: None | str | Unset
        if isinstance(self.website_email_address, Unset):
            website_email_address = UNSET
        else:
            website_email_address = self.website_email_address

        types_of_recycling_facilities_provided_eng: None | str | Unset
        if isinstance(self.types_of_recycling_facilities_provided_eng, Unset):
            types_of_recycling_facilities_provided_eng = UNSET
        else:
            types_of_recycling_facilities_provided_eng = (
                self.types_of_recycling_facilities_provided_eng
            )

        types_of_recycling_facilities_provided_chin: None | str | Unset
        if isinstance(self.types_of_recycling_facilities_provided_chin, Unset):
            types_of_recycling_facilities_provided_chin = UNSET
        else:
            types_of_recycling_facilities_provided_chin = (
                self.types_of_recycling_facilities_provided_chin
            )

        address_longitude_lands: None | str | Unset
        if isinstance(self.address_longitude_lands, Unset):
            address_longitude_lands = UNSET
        else:
            address_longitude_lands = self.address_longitude_lands

        address_latitude_lands: None | str | Unset
        if isinstance(self.address_latitude_lands, Unset):
            address_latitude_lands = UNSET
        else:
            address_latitude_lands = self.address_latitude_lands

        address_easting_lands: None | str | Unset
        if isinstance(self.address_easting_lands, Unset):
            address_easting_lands = UNSET
        else:
            address_easting_lands = self.address_easting_lands

        address_northing_lands: None | str | Unset
        if isinstance(self.address_northing_lands, Unset):
            address_northing_lands = UNSET
        else:
            address_northing_lands = self.address_northing_lands

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_name_eng is not UNSET:
            field_dict["Company_Name_Eng"] = company_name_eng
        if company_name_chin is not UNSET:
            field_dict["Company_Name_Chin"] = company_name_chin
        if address_eng is not UNSET:
            field_dict["Address_Eng"] = address_eng
        if address_chin is not UNSET:
            field_dict["Address_Chin"] = address_chin
        if contact_person_eng is not UNSET:
            field_dict["Contact_Person_Eng"] = contact_person_eng
        if contact_person_chin is not UNSET:
            field_dict["Contact_Person_Chin"] = contact_person_chin
        if tel_no is not UNSET:
            field_dict["Tel_No"] = tel_no
        if fax_no is not UNSET:
            field_dict["Fax_No"] = fax_no
        if website_email_address is not UNSET:
            field_dict["Website_Email_address"] = website_email_address
        if types_of_recycling_facilities_provided_eng is not UNSET:
            field_dict["Types_of_recycling_facilities_provided_Eng"] = (
                types_of_recycling_facilities_provided_eng
            )
        if types_of_recycling_facilities_provided_chin is not UNSET:
            field_dict["Types_of_recycling_facilities_provided_Chin"] = (
                types_of_recycling_facilities_provided_chin
            )
        if address_longitude_lands is not UNSET:
            field_dict["Address_longitude_lands"] = address_longitude_lands
        if address_latitude_lands is not UNSET:
            field_dict["Address_latitude_lands"] = address_latitude_lands
        if address_easting_lands is not UNSET:
            field_dict["Address_easting_lands"] = address_easting_lands
        if address_northing_lands is not UNSET:
            field_dict["Address_northing_lands"] = address_northing_lands
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_company_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_eng = _parse_company_name_eng(d.pop("Company_Name_Eng", UNSET))

        def _parse_company_name_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_chin = _parse_company_name_chin(d.pop("Company_Name_Chin", UNSET))

        def _parse_address_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_eng = _parse_address_eng(d.pop("Address_Eng", UNSET))

        def _parse_address_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chin = _parse_address_chin(d.pop("Address_Chin", UNSET))

        def _parse_contact_person_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_person_eng = _parse_contact_person_eng(
            d.pop("Contact_Person_Eng", UNSET)
        )

        def _parse_contact_person_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_person_chin = _parse_contact_person_chin(
            d.pop("Contact_Person_Chin", UNSET)
        )

        def _parse_tel_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel_no = _parse_tel_no(d.pop("Tel_No", UNSET))

        def _parse_fax_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_no = _parse_fax_no(d.pop("Fax_No", UNSET))

        def _parse_website_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_email_address = _parse_website_email_address(
            d.pop("Website_Email_address", UNSET)
        )

        def _parse_types_of_recycling_facilities_provided_eng(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_recycling_facilities_provided_eng = (
            _parse_types_of_recycling_facilities_provided_eng(
                d.pop("Types_of_recycling_facilities_provided_Eng", UNSET)
            )
        )

        def _parse_types_of_recycling_facilities_provided_chin(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_recycling_facilities_provided_chin = (
            _parse_types_of_recycling_facilities_provided_chin(
                d.pop("Types_of_recycling_facilities_provided_Chin", UNSET)
            )
        )

        def _parse_address_longitude_lands(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_longitude_lands = _parse_address_longitude_lands(
            d.pop("Address_longitude_lands", UNSET)
        )

        def _parse_address_latitude_lands(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_latitude_lands = _parse_address_latitude_lands(
            d.pop("Address_latitude_lands", UNSET)
        )

        def _parse_address_easting_lands(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_easting_lands = _parse_address_easting_lands(
            d.pop("Address_easting_lands", UNSET)
        )

        def _parse_address_northing_lands(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_northing_lands = _parse_address_northing_lands(
            d.pop("Address_northing_lands", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            company_name_eng=company_name_eng,
            company_name_chin=company_name_chin,
            address_eng=address_eng,
            address_chin=address_chin,
            contact_person_eng=contact_person_eng,
            contact_person_chin=contact_person_chin,
            tel_no=tel_no,
            fax_no=fax_no,
            website_email_address=website_email_address,
            types_of_recycling_facilities_provided_eng=types_of_recycling_facilities_provided_eng,
            types_of_recycling_facilities_provided_chin=types_of_recycling_facilities_provided_chin,
            address_longitude_lands=address_longitude_lands,
            address_latitude_lands=address_latitude_lands,
            address_easting_lands=address_easting_lands,
            address_northing_lands=address_northing_lands,
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
