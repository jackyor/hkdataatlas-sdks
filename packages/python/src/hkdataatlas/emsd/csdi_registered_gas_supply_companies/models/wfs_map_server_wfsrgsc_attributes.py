from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsrgscAttributes")


@_attrs_define
class WfsMapServerWfsrgscAttributes:
    """
    Attributes:
        address_of_every_premises_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        address_of_every_premises_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        company_name_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        company_name_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        date_of_registration (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        other_particulars_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        other_particulars_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        postal_address_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        postal_address_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        registration_no (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_of_every_premises_chinese: None | str | Unset = UNSET
    address_of_every_premises_english: None | str | Unset = UNSET
    company_name_chinese: None | str | Unset = UNSET
    company_name_english: None | str | Unset = UNSET
    date_of_registration: None | str | Unset = UNSET
    other_particulars_chinese: None | str | Unset = UNSET
    other_particulars_english: None | str | Unset = UNSET
    postal_address_chinese: None | str | Unset = UNSET
    postal_address_english: None | str | Unset = UNSET
    registration_no: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_of_every_premises_chinese: None | str | Unset
        if isinstance(self.address_of_every_premises_chinese, Unset):
            address_of_every_premises_chinese = UNSET
        else:
            address_of_every_premises_chinese = self.address_of_every_premises_chinese

        address_of_every_premises_english: None | str | Unset
        if isinstance(self.address_of_every_premises_english, Unset):
            address_of_every_premises_english = UNSET
        else:
            address_of_every_premises_english = self.address_of_every_premises_english

        company_name_chinese: None | str | Unset
        if isinstance(self.company_name_chinese, Unset):
            company_name_chinese = UNSET
        else:
            company_name_chinese = self.company_name_chinese

        company_name_english: None | str | Unset
        if isinstance(self.company_name_english, Unset):
            company_name_english = UNSET
        else:
            company_name_english = self.company_name_english

        date_of_registration: None | str | Unset
        if isinstance(self.date_of_registration, Unset):
            date_of_registration = UNSET
        else:
            date_of_registration = self.date_of_registration

        other_particulars_chinese: None | str | Unset
        if isinstance(self.other_particulars_chinese, Unset):
            other_particulars_chinese = UNSET
        else:
            other_particulars_chinese = self.other_particulars_chinese

        other_particulars_english: None | str | Unset
        if isinstance(self.other_particulars_english, Unset):
            other_particulars_english = UNSET
        else:
            other_particulars_english = self.other_particulars_english

        postal_address_chinese: None | str | Unset
        if isinstance(self.postal_address_chinese, Unset):
            postal_address_chinese = UNSET
        else:
            postal_address_chinese = self.postal_address_chinese

        postal_address_english: None | str | Unset
        if isinstance(self.postal_address_english, Unset):
            postal_address_english = UNSET
        else:
            postal_address_english = self.postal_address_english

        registration_no: float | None | Unset
        if isinstance(self.registration_no, Unset):
            registration_no = UNSET
        else:
            registration_no = self.registration_no

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_of_every_premises_chinese is not UNSET:
            field_dict["Address_of_Every_Premises_Chinese"] = (
                address_of_every_premises_chinese
            )
        if address_of_every_premises_english is not UNSET:
            field_dict["Address_of_Every_Premises_English"] = (
                address_of_every_premises_english
            )
        if company_name_chinese is not UNSET:
            field_dict["Company_Name_Chinese"] = company_name_chinese
        if company_name_english is not UNSET:
            field_dict["Company_Name_English"] = company_name_english
        if date_of_registration is not UNSET:
            field_dict["Date_of_Registration"] = date_of_registration
        if other_particulars_chinese is not UNSET:
            field_dict["Other_Particulars_Chinese"] = other_particulars_chinese
        if other_particulars_english is not UNSET:
            field_dict["Other_Particulars_English"] = other_particulars_english
        if postal_address_chinese is not UNSET:
            field_dict["Postal_Address_Chinese"] = postal_address_chinese
        if postal_address_english is not UNSET:
            field_dict["Postal_Address_English"] = postal_address_english
        if registration_no is not UNSET:
            field_dict["Registration_No"] = registration_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_of_every_premises_chinese(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_every_premises_chinese = _parse_address_of_every_premises_chinese(
            d.pop("Address_of_Every_Premises_Chinese", UNSET)
        )

        def _parse_address_of_every_premises_english(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_every_premises_english = _parse_address_of_every_premises_english(
            d.pop("Address_of_Every_Premises_English", UNSET)
        )

        def _parse_company_name_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_chinese = _parse_company_name_chinese(
            d.pop("Company_Name_Chinese", UNSET)
        )

        def _parse_company_name_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name_english = _parse_company_name_english(
            d.pop("Company_Name_English", UNSET)
        )

        def _parse_date_of_registration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_registration = _parse_date_of_registration(
            d.pop("Date_of_Registration", UNSET)
        )

        def _parse_other_particulars_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_particulars_chinese = _parse_other_particulars_chinese(
            d.pop("Other_Particulars_Chinese", UNSET)
        )

        def _parse_other_particulars_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_particulars_english = _parse_other_particulars_english(
            d.pop("Other_Particulars_English", UNSET)
        )

        def _parse_postal_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_address_chinese = _parse_postal_address_chinese(
            d.pop("Postal_Address_Chinese", UNSET)
        )

        def _parse_postal_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        postal_address_english = _parse_postal_address_english(
            d.pop("Postal_Address_English", UNSET)
        )

        def _parse_registration_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        registration_no = _parse_registration_no(d.pop("Registration_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsrgsc_attributes = cls(
            address_of_every_premises_chinese=address_of_every_premises_chinese,
            address_of_every_premises_english=address_of_every_premises_english,
            company_name_chinese=company_name_chinese,
            company_name_english=company_name_english,
            date_of_registration=date_of_registration,
            other_particulars_chinese=other_particulars_chinese,
            other_particulars_english=other_particulars_english,
            postal_address_chinese=postal_address_chinese,
            postal_address_english=postal_address_english,
            registration_no=registration_no,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsrgsc_attributes.additional_properties = d
        return wfs_map_server_wfsrgsc_attributes

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
