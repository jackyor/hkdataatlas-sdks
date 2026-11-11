from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalCompanyRecord")


@_attrs_define
class LocalCompanyRecord:
    """Documented record fields for Registered Office Address of Live Local Companies. The dictionary does not establish
    universal field requiredness or a closed object.

        Attributes:
            address_of_registered_office (str | Unset): Registered Office address; alphanumeric and Chinese characters.
            brn (str | Unset): Business Registration Number; unique business identifier (alphanumeric).
            chinese_company_name (str | Unset): Local Company Chinese Name; alphanumeric and Chinese characters.
            company_type (str | Unset): Company Type; alphanumeric.
            date_of_incorporation (str | Unset): Date of Incorporation. Documented display format: DD-MM-YYYY; this may
                differ from the conventional JSON Schema date representation.
            english_company_name (str | Unset): Local Company English Name; alphanumeric.
            re_domiciliation_date (None | str | Unset): Re-domiciliation Date. Documented display format: DD-MM-YYYY; this
                may differ from the conventional JSON Schema date representation.
    """

    address_of_registered_office: str | Unset = UNSET
    brn: str | Unset = UNSET
    chinese_company_name: str | Unset = UNSET
    company_type: str | Unset = UNSET
    date_of_incorporation: str | Unset = UNSET
    english_company_name: str | Unset = UNSET
    re_domiciliation_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_of_registered_office = self.address_of_registered_office

        brn = self.brn

        chinese_company_name = self.chinese_company_name

        company_type = self.company_type

        date_of_incorporation = self.date_of_incorporation

        english_company_name = self.english_company_name

        re_domiciliation_date: None | str | Unset
        if isinstance(self.re_domiciliation_date, Unset):
            re_domiciliation_date = UNSET
        else:
            re_domiciliation_date = self.re_domiciliation_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_of_registered_office is not UNSET:
            field_dict["Address_of_Registered_Office"] = address_of_registered_office
        if brn is not UNSET:
            field_dict["Brn"] = brn
        if chinese_company_name is not UNSET:
            field_dict["Chinese_Company_Name"] = chinese_company_name
        if company_type is not UNSET:
            field_dict["Company_Type"] = company_type
        if date_of_incorporation is not UNSET:
            field_dict["Date_of_Incorporation"] = date_of_incorporation
        if english_company_name is not UNSET:
            field_dict["English_Company_Name"] = english_company_name
        if re_domiciliation_date is not UNSET:
            field_dict["Re-domiciliation_Date"] = re_domiciliation_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address_of_registered_office = d.pop("Address_of_Registered_Office", UNSET)

        brn = d.pop("Brn", UNSET)

        chinese_company_name = d.pop("Chinese_Company_Name", UNSET)

        company_type = d.pop("Company_Type", UNSET)

        date_of_incorporation = d.pop("Date_of_Incorporation", UNSET)

        english_company_name = d.pop("English_Company_Name", UNSET)

        def _parse_re_domiciliation_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        re_domiciliation_date = _parse_re_domiciliation_date(
            d.pop("Re-domiciliation_Date", UNSET)
        )

        local_company_record = cls(
            address_of_registered_office=address_of_registered_office,
            brn=brn,
            chinese_company_name=chinese_company_name,
            company_type=company_type,
            date_of_incorporation=date_of_incorporation,
            english_company_name=english_company_name,
            re_domiciliation_date=re_domiciliation_date,
        )

        local_company_record.additional_properties = d
        return local_company_record

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
