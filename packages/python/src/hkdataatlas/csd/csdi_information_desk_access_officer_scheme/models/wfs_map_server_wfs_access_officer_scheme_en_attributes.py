from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsAccessOfficerSchemeENAttributes")


@_attrs_define
class WfsMapServerWfsAccessOfficerSchemeENAttributes:
    """
    Attributes:
        address (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        contact_email (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        contact_fax_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        contact_telephone_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        district_by_district_council_boundaries (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        post_title_of_access_officer (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        venue_premise_facility (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address: None | str | Unset = UNSET
    contact_email: None | str | Unset = UNSET
    contact_fax_number: None | str | Unset = UNSET
    contact_telephone_number: None | str | Unset = UNSET
    district_by_district_council_boundaries: None | str | Unset = UNSET
    post_title_of_access_officer: None | str | Unset = UNSET
    venue_premise_facility: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        contact_email: None | str | Unset
        if isinstance(self.contact_email, Unset):
            contact_email = UNSET
        else:
            contact_email = self.contact_email

        contact_fax_number: None | str | Unset
        if isinstance(self.contact_fax_number, Unset):
            contact_fax_number = UNSET
        else:
            contact_fax_number = self.contact_fax_number

        contact_telephone_number: None | str | Unset
        if isinstance(self.contact_telephone_number, Unset):
            contact_telephone_number = UNSET
        else:
            contact_telephone_number = self.contact_telephone_number

        district_by_district_council_boundaries: None | str | Unset
        if isinstance(self.district_by_district_council_boundaries, Unset):
            district_by_district_council_boundaries = UNSET
        else:
            district_by_district_council_boundaries = (
                self.district_by_district_council_boundaries
            )

        post_title_of_access_officer: None | str | Unset
        if isinstance(self.post_title_of_access_officer, Unset):
            post_title_of_access_officer = UNSET
        else:
            post_title_of_access_officer = self.post_title_of_access_officer

        venue_premise_facility: None | str | Unset
        if isinstance(self.venue_premise_facility, Unset):
            venue_premise_facility = UNSET
        else:
            venue_premise_facility = self.venue_premise_facility

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if contact_email is not UNSET:
            field_dict["Contact_Email"] = contact_email
        if contact_fax_number is not UNSET:
            field_dict["Contact_Fax_Number"] = contact_fax_number
        if contact_telephone_number is not UNSET:
            field_dict["Contact_Telephone_Number"] = contact_telephone_number
        if district_by_district_council_boundaries is not UNSET:
            field_dict["District_by_District_Council_Boundaries"] = (
                district_by_district_council_boundaries
            )
        if post_title_of_access_officer is not UNSET:
            field_dict["Post_Title_of_Access_Officer"] = post_title_of_access_officer
        if venue_premise_facility is not UNSET:
            field_dict["Venue_Premise_Facility"] = venue_premise_facility
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("Address", UNSET))

        def _parse_contact_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_email = _parse_contact_email(d.pop("Contact_Email", UNSET))

        def _parse_contact_fax_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_fax_number = _parse_contact_fax_number(
            d.pop("Contact_Fax_Number", UNSET)
        )

        def _parse_contact_telephone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_telephone_number = _parse_contact_telephone_number(
            d.pop("Contact_Telephone_Number", UNSET)
        )

        def _parse_district_by_district_council_boundaries(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_by_district_council_boundaries = (
            _parse_district_by_district_council_boundaries(
                d.pop("District_by_District_Council_Boundaries", UNSET)
            )
        )

        def _parse_post_title_of_access_officer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_title_of_access_officer = _parse_post_title_of_access_officer(
            d.pop("Post_Title_of_Access_Officer", UNSET)
        )

        def _parse_venue_premise_facility(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_premise_facility = _parse_venue_premise_facility(
            d.pop("Venue_Premise_Facility", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_access_officer_scheme_en_attributes = cls(
            address=address,
            contact_email=contact_email,
            contact_fax_number=contact_fax_number,
            contact_telephone_number=contact_telephone_number,
            district_by_district_council_boundaries=district_by_district_council_boundaries,
            post_title_of_access_officer=post_title_of_access_officer,
            venue_premise_facility=venue_premise_facility,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_access_officer_scheme_en_attributes.additional_properties = d
        return wfs_map_server_wfs_access_officer_scheme_en_attributes

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
