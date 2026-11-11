from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfslpgvfsmwredAttributes")


@_attrs_define
class WfsMapServerWfslpgvfsmwredAttributes:
    """
    Attributes:
        company_address_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        company_address_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        company_name_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        company_name_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        fax_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        maintenance_servicing_for_lpg_fuel_injection_system (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        signage_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        telephone_no (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    company_address_chinese: None | str | Unset = UNSET
    company_address_english: None | str | Unset = UNSET
    company_name_chinese: None | str | Unset = UNSET
    company_name_english: None | str | Unset = UNSET
    fax_no: None | str | Unset = UNSET
    maintenance_servicing_for_lpg_fuel_injection_system: None | str | Unset = UNSET
    signage_no: None | str | Unset = UNSET
    telephone_no: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_address_chinese: None | str | Unset
        if isinstance(self.company_address_chinese, Unset):
            company_address_chinese = UNSET
        else:
            company_address_chinese = self.company_address_chinese

        company_address_english: None | str | Unset
        if isinstance(self.company_address_english, Unset):
            company_address_english = UNSET
        else:
            company_address_english = self.company_address_english

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

        fax_no: None | str | Unset
        if isinstance(self.fax_no, Unset):
            fax_no = UNSET
        else:
            fax_no = self.fax_no

        maintenance_servicing_for_lpg_fuel_injection_system: None | str | Unset
        if isinstance(self.maintenance_servicing_for_lpg_fuel_injection_system, Unset):
            maintenance_servicing_for_lpg_fuel_injection_system = UNSET
        else:
            maintenance_servicing_for_lpg_fuel_injection_system = (
                self.maintenance_servicing_for_lpg_fuel_injection_system
            )

        signage_no: None | str | Unset
        if isinstance(self.signage_no, Unset):
            signage_no = UNSET
        else:
            signage_no = self.signage_no

        telephone_no: float | None | Unset
        if isinstance(self.telephone_no, Unset):
            telephone_no = UNSET
        else:
            telephone_no = self.telephone_no

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if company_address_chinese is not UNSET:
            field_dict["Company_Address_Chinese"] = company_address_chinese
        if company_address_english is not UNSET:
            field_dict["Company_Address_English"] = company_address_english
        if company_name_chinese is not UNSET:
            field_dict["Company_Name_Chinese"] = company_name_chinese
        if company_name_english is not UNSET:
            field_dict["Company_Name_English"] = company_name_english
        if fax_no is not UNSET:
            field_dict["Fax_No"] = fax_no
        if maintenance_servicing_for_lpg_fuel_injection_system is not UNSET:
            field_dict["Maintenance_servicing_for_LPG_fuel_injection_system"] = (
                maintenance_servicing_for_lpg_fuel_injection_system
            )
        if signage_no is not UNSET:
            field_dict["Signage_No"] = signage_no
        if telephone_no is not UNSET:
            field_dict["Telephone_No"] = telephone_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_company_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_address_chinese = _parse_company_address_chinese(
            d.pop("Company_Address_Chinese", UNSET)
        )

        def _parse_company_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_address_english = _parse_company_address_english(
            d.pop("Company_Address_English", UNSET)
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

        def _parse_fax_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_no = _parse_fax_no(d.pop("Fax_No", UNSET))

        def _parse_maintenance_servicing_for_lpg_fuel_injection_system(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        maintenance_servicing_for_lpg_fuel_injection_system = (
            _parse_maintenance_servicing_for_lpg_fuel_injection_system(
                d.pop("Maintenance_servicing_for_LPG_fuel_injection_system", UNSET)
            )
        )

        def _parse_signage_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signage_no = _parse_signage_no(d.pop("Signage_No", UNSET))

        def _parse_telephone_no(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        telephone_no = _parse_telephone_no(d.pop("Telephone_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfslpgvfsmwred_attributes = cls(
            company_address_chinese=company_address_chinese,
            company_address_english=company_address_english,
            company_name_chinese=company_name_chinese,
            company_name_english=company_name_english,
            fax_no=fax_no,
            maintenance_servicing_for_lpg_fuel_injection_system=maintenance_servicing_for_lpg_fuel_injection_system,
            signage_no=signage_no,
            telephone_no=telephone_no,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfslpgvfsmwred_attributes.additional_properties = d
        return wfs_map_server_wfslpgvfsmwred_attributes

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
