from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer2Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer2Attributes:
    """
    Attributes:
        address (None | str | Unset): Publisher field type: esriFieldTypeString
        capacity (None | str | Unset): Publisher field type: esriFieldTypeString
        enquiries (None | str | Unset): Publisher field type: esriFieldTypeString
        establishment (None | str | Unset): Publisher field type: esriFieldTypeString
        how_to_get_there (None | str | Unset): Publisher field type: esriFieldTypeString
        institution (None | str | Unset): Publisher field type: esriFieldTypeString
        other_services (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_persons_in_custody (None | str | Unset): Publisher field type: esriFieldTypeString
        types_of_facilities_age (None | str | Unset): Publisher field type: esriFieldTypeString
        types_of_facilities_gender (None | str | Unset): Publisher field type: esriFieldTypeString
        types_of_facilities_others (None | str | Unset): Publisher field type: esriFieldTypeString
        types_of_facilities_security_level (None | str | Unset): Publisher field type: esriFieldTypeString
        visiting_hour_official_visit (None | str | Unset): Publisher field type: esriFieldTypeString
        visiting_hours_general_visit (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address: None | str | Unset = UNSET
    capacity: None | str | Unset = UNSET
    enquiries: None | str | Unset = UNSET
    establishment: None | str | Unset = UNSET
    how_to_get_there: None | str | Unset = UNSET
    institution: None | str | Unset = UNSET
    other_services: None | str | Unset = UNSET
    type_of_persons_in_custody: None | str | Unset = UNSET
    types_of_facilities_age: None | str | Unset = UNSET
    types_of_facilities_gender: None | str | Unset = UNSET
    types_of_facilities_others: None | str | Unset = UNSET
    types_of_facilities_security_level: None | str | Unset = UNSET
    visiting_hour_official_visit: None | str | Unset = UNSET
    visiting_hours_general_visit: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        capacity: None | str | Unset
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        enquiries: None | str | Unset
        if isinstance(self.enquiries, Unset):
            enquiries = UNSET
        else:
            enquiries = self.enquiries

        establishment: None | str | Unset
        if isinstance(self.establishment, Unset):
            establishment = UNSET
        else:
            establishment = self.establishment

        how_to_get_there: None | str | Unset
        if isinstance(self.how_to_get_there, Unset):
            how_to_get_there = UNSET
        else:
            how_to_get_there = self.how_to_get_there

        institution: None | str | Unset
        if isinstance(self.institution, Unset):
            institution = UNSET
        else:
            institution = self.institution

        other_services: None | str | Unset
        if isinstance(self.other_services, Unset):
            other_services = UNSET
        else:
            other_services = self.other_services

        type_of_persons_in_custody: None | str | Unset
        if isinstance(self.type_of_persons_in_custody, Unset):
            type_of_persons_in_custody = UNSET
        else:
            type_of_persons_in_custody = self.type_of_persons_in_custody

        types_of_facilities_age: None | str | Unset
        if isinstance(self.types_of_facilities_age, Unset):
            types_of_facilities_age = UNSET
        else:
            types_of_facilities_age = self.types_of_facilities_age

        types_of_facilities_gender: None | str | Unset
        if isinstance(self.types_of_facilities_gender, Unset):
            types_of_facilities_gender = UNSET
        else:
            types_of_facilities_gender = self.types_of_facilities_gender

        types_of_facilities_others: None | str | Unset
        if isinstance(self.types_of_facilities_others, Unset):
            types_of_facilities_others = UNSET
        else:
            types_of_facilities_others = self.types_of_facilities_others

        types_of_facilities_security_level: None | str | Unset
        if isinstance(self.types_of_facilities_security_level, Unset):
            types_of_facilities_security_level = UNSET
        else:
            types_of_facilities_security_level = self.types_of_facilities_security_level

        visiting_hour_official_visit: None | str | Unset
        if isinstance(self.visiting_hour_official_visit, Unset):
            visiting_hour_official_visit = UNSET
        else:
            visiting_hour_official_visit = self.visiting_hour_official_visit

        visiting_hours_general_visit: None | str | Unset
        if isinstance(self.visiting_hours_general_visit, Unset):
            visiting_hours_general_visit = UNSET
        else:
            visiting_hours_general_visit = self.visiting_hours_general_visit

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if capacity is not UNSET:
            field_dict["Capacity"] = capacity
        if enquiries is not UNSET:
            field_dict["Enquiries"] = enquiries
        if establishment is not UNSET:
            field_dict["Establishment"] = establishment
        if how_to_get_there is not UNSET:
            field_dict["How_to_get_there"] = how_to_get_there
        if institution is not UNSET:
            field_dict["Institution"] = institution
        if other_services is not UNSET:
            field_dict["Other_Services"] = other_services
        if type_of_persons_in_custody is not UNSET:
            field_dict["Type_of_Persons_in_Custody"] = type_of_persons_in_custody
        if types_of_facilities_age is not UNSET:
            field_dict["Types_of_Facilities__Age"] = types_of_facilities_age
        if types_of_facilities_gender is not UNSET:
            field_dict["Types_of_Facilities__Gender"] = types_of_facilities_gender
        if types_of_facilities_others is not UNSET:
            field_dict["Types_of_Facilities__Others"] = types_of_facilities_others
        if types_of_facilities_security_level is not UNSET:
            field_dict["Types_of_Facilities__Security_Level"] = (
                types_of_facilities_security_level
            )
        if visiting_hour_official_visit is not UNSET:
            field_dict["Visiting_Hour__Official_Visit"] = visiting_hour_official_visit
        if visiting_hours_general_visit is not UNSET:
            field_dict["Visiting_Hours__General_Visit"] = visiting_hours_general_visit
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

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

        def _parse_capacity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        capacity = _parse_capacity(d.pop("Capacity", UNSET))

        def _parse_enquiries(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        enquiries = _parse_enquiries(d.pop("Enquiries", UNSET))

        def _parse_establishment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        establishment = _parse_establishment(d.pop("Establishment", UNSET))

        def _parse_how_to_get_there(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        how_to_get_there = _parse_how_to_get_there(d.pop("How_to_get_there", UNSET))

        def _parse_institution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        institution = _parse_institution(d.pop("Institution", UNSET))

        def _parse_other_services(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_services = _parse_other_services(d.pop("Other_Services", UNSET))

        def _parse_type_of_persons_in_custody(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_persons_in_custody = _parse_type_of_persons_in_custody(
            d.pop("Type_of_Persons_in_Custody", UNSET)
        )

        def _parse_types_of_facilities_age(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_facilities_age = _parse_types_of_facilities_age(
            d.pop("Types_of_Facilities__Age", UNSET)
        )

        def _parse_types_of_facilities_gender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_facilities_gender = _parse_types_of_facilities_gender(
            d.pop("Types_of_Facilities__Gender", UNSET)
        )

        def _parse_types_of_facilities_others(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_facilities_others = _parse_types_of_facilities_others(
            d.pop("Types_of_Facilities__Others", UNSET)
        )

        def _parse_types_of_facilities_security_level(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_facilities_security_level = _parse_types_of_facilities_security_level(
            d.pop("Types_of_Facilities__Security_Level", UNSET)
        )

        def _parse_visiting_hour_official_visit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visiting_hour_official_visit = _parse_visiting_hour_official_visit(
            d.pop("Visiting_Hour__Official_Visit", UNSET)
        )

        def _parse_visiting_hours_general_visit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visiting_hours_general_visit = _parse_visiting_hours_general_visit(
            d.pop("Visiting_Hours__General_Visit", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_2_attributes = cls(
            address=address,
            capacity=capacity,
            enquiries=enquiries,
            establishment=establishment,
            how_to_get_there=how_to_get_there,
            institution=institution,
            other_services=other_services,
            type_of_persons_in_custody=type_of_persons_in_custody,
            types_of_facilities_age=types_of_facilities_age,
            types_of_facilities_gender=types_of_facilities_gender,
            types_of_facilities_others=types_of_facilities_others,
            types_of_facilities_security_level=types_of_facilities_security_level,
            visiting_hour_official_visit=visiting_hour_official_visit,
            visiting_hours_general_visit=visiting_hours_general_visit,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_2_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_2_attributes

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
