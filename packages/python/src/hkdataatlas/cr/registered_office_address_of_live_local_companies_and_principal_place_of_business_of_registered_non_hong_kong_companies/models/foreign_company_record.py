from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ForeignCompanyRecord")


@_attrs_define
class ForeignCompanyRecord:
    """Documented record fields for Principal Place of Business of Registered Non-Hong Kong Companies. The dictionary does
    not establish universal field requiredness or a closed object.

        Attributes:
            approved_name_for_carrying_on_business_in_h_k_corporate (str | Unset): Approved name for carrying on business in
                H.K. (Corporate); alphanumeric and Chinese characters. The documented column name is preserved, including
                punctuation and line wrapping normalized to a single property name.
            approved_name_for_carrying_on_business_in_h_k_other_corporate (None | str | Unset): Approved name for carrying
                on business in H.K. (Other Corporate); alphanumeric and Chinese characters. The documented column name is
                preserved, with line wrapping normalized.
            brn (str | Unset): Business Registration Number; unique business identifier (alphanumeric).
            company_type (str | Unset): Company Type; alphanumeric.
            corporate_name (str | Unset): Corporate Name; alphanumeric and Chinese characters.
            date_of_registration (str | Unset): Date of Registration. Documented display format: DD-MM-YYYY; this may differ
                from the conventional JSON Schema date representation.
            other_corporate_name_s (str | Unset): Other Corporate Name(s); alphanumeric and Chinese characters.
            place_of_incorporation (str | Unset): Place of Incorporation; alphanumeric.
            principal_place_of_business_in_h_k (str | Unset): Principal Place of Business in H.K.; alphanumeric and Chinese
                characters. The documented column name is preserved, with line wrapping normalized.
    """

    approved_name_for_carrying_on_business_in_h_k_corporate: str | Unset = UNSET
    approved_name_for_carrying_on_business_in_h_k_other_corporate: (
        None | str | Unset
    ) = UNSET
    brn: str | Unset = UNSET
    company_type: str | Unset = UNSET
    corporate_name: str | Unset = UNSET
    date_of_registration: str | Unset = UNSET
    other_corporate_name_s: str | Unset = UNSET
    place_of_incorporation: str | Unset = UNSET
    principal_place_of_business_in_h_k: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        approved_name_for_carrying_on_business_in_h_k_corporate = (
            self.approved_name_for_carrying_on_business_in_h_k_corporate
        )

        approved_name_for_carrying_on_business_in_h_k_other_corporate: (
            None | str | Unset
        )
        if isinstance(
            self.approved_name_for_carrying_on_business_in_h_k_other_corporate, Unset
        ):
            approved_name_for_carrying_on_business_in_h_k_other_corporate = UNSET
        else:
            approved_name_for_carrying_on_business_in_h_k_other_corporate = (
                self.approved_name_for_carrying_on_business_in_h_k_other_corporate
            )

        brn = self.brn

        company_type = self.company_type

        corporate_name = self.corporate_name

        date_of_registration = self.date_of_registration

        other_corporate_name_s = self.other_corporate_name_s

        place_of_incorporation = self.place_of_incorporation

        principal_place_of_business_in_h_k = self.principal_place_of_business_in_h_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if approved_name_for_carrying_on_business_in_h_k_corporate is not UNSET:
            field_dict["Approved_name_for_carrying_on_business_in+H.K._Corporate"] = (
                approved_name_for_carrying_on_business_in_h_k_corporate
            )
        if approved_name_for_carrying_on_business_in_h_k_other_corporate is not UNSET:
            field_dict[
                "Approved_name_for_carrying_on_business_in_H.K._Other_Corporate"
            ] = approved_name_for_carrying_on_business_in_h_k_other_corporate
        if brn is not UNSET:
            field_dict["Brn"] = brn
        if company_type is not UNSET:
            field_dict["Company_Type"] = company_type
        if corporate_name is not UNSET:
            field_dict["Corporate_Name"] = corporate_name
        if date_of_registration is not UNSET:
            field_dict["Date_of_Registration"] = date_of_registration
        if other_corporate_name_s is not UNSET:
            field_dict["Other_Corporate_Name_s"] = other_corporate_name_s
        if place_of_incorporation is not UNSET:
            field_dict["Place_of_Incorporation"] = place_of_incorporation
        if principal_place_of_business_in_h_k is not UNSET:
            field_dict["Principal_Place_of_Business_in_H.K."] = (
                principal_place_of_business_in_h_k
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        approved_name_for_carrying_on_business_in_h_k_corporate = d.pop(
            "Approved_name_for_carrying_on_business_in+H.K._Corporate", UNSET
        )

        def _parse_approved_name_for_carrying_on_business_in_h_k_other_corporate(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        approved_name_for_carrying_on_business_in_h_k_other_corporate = (
            _parse_approved_name_for_carrying_on_business_in_h_k_other_corporate(
                d.pop(
                    "Approved_name_for_carrying_on_business_in_H.K._Other_Corporate",
                    UNSET,
                )
            )
        )

        brn = d.pop("Brn", UNSET)

        company_type = d.pop("Company_Type", UNSET)

        corporate_name = d.pop("Corporate_Name", UNSET)

        date_of_registration = d.pop("Date_of_Registration", UNSET)

        other_corporate_name_s = d.pop("Other_Corporate_Name_s", UNSET)

        place_of_incorporation = d.pop("Place_of_Incorporation", UNSET)

        principal_place_of_business_in_h_k = d.pop(
            "Principal_Place_of_Business_in_H.K.", UNSET
        )

        foreign_company_record = cls(
            approved_name_for_carrying_on_business_in_h_k_corporate=approved_name_for_carrying_on_business_in_h_k_corporate,
            approved_name_for_carrying_on_business_in_h_k_other_corporate=approved_name_for_carrying_on_business_in_h_k_other_corporate,
            brn=brn,
            company_type=company_type,
            corporate_name=corporate_name,
            date_of_registration=date_of_registration,
            other_corporate_name_s=other_corporate_name_s,
            place_of_incorporation=place_of_incorporation,
            principal_place_of_business_in_h_k=principal_place_of_business_in_h_k,
        )

        foreign_company_record.additional_properties = d
        return foreign_company_record

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
