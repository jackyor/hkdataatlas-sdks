from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        en_property_name (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_property_name (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_property_name (None | str | Unset): Publisher field type: esriFieldTypeString
        en_property_address (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_property_address (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_property_address (None | str | Unset): Publisher field type: esriFieldTypeString
        en_district (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        tender_quotation_reference_number (None | str | Unset): Publisher field type: esriFieldTypeString
        en_name_of_tenant (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_name_of_tenant (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_name_of_tenant (None | str | Unset): Publisher field type: esriFieldTypeString
        en_tenancy_term (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_tenancy_term (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_tenancy_term (None | str | Unset): Publisher field type: esriFieldTypeString
        en_amount (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_amount (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_amount (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    en_property_name: None | str | Unset = UNSET
    tc_property_name: None | str | Unset = UNSET
    sc_property_name: None | str | Unset = UNSET
    en_property_address: None | str | Unset = UNSET
    tc_property_address: None | str | Unset = UNSET
    sc_property_address: None | str | Unset = UNSET
    en_district: None | str | Unset = UNSET
    tc_district: None | str | Unset = UNSET
    sc_district: None | str | Unset = UNSET
    tender_quotation_reference_number: None | str | Unset = UNSET
    en_name_of_tenant: None | str | Unset = UNSET
    tc_name_of_tenant: None | str | Unset = UNSET
    sc_name_of_tenant: None | str | Unset = UNSET
    en_tenancy_term: None | str | Unset = UNSET
    tc_tenancy_term: None | str | Unset = UNSET
    sc_tenancy_term: None | str | Unset = UNSET
    en_amount: None | str | Unset = UNSET
    tc_amount: None | str | Unset = UNSET
    sc_amount: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en_property_name: None | str | Unset
        if isinstance(self.en_property_name, Unset):
            en_property_name = UNSET
        else:
            en_property_name = self.en_property_name

        tc_property_name: None | str | Unset
        if isinstance(self.tc_property_name, Unset):
            tc_property_name = UNSET
        else:
            tc_property_name = self.tc_property_name

        sc_property_name: None | str | Unset
        if isinstance(self.sc_property_name, Unset):
            sc_property_name = UNSET
        else:
            sc_property_name = self.sc_property_name

        en_property_address: None | str | Unset
        if isinstance(self.en_property_address, Unset):
            en_property_address = UNSET
        else:
            en_property_address = self.en_property_address

        tc_property_address: None | str | Unset
        if isinstance(self.tc_property_address, Unset):
            tc_property_address = UNSET
        else:
            tc_property_address = self.tc_property_address

        sc_property_address: None | str | Unset
        if isinstance(self.sc_property_address, Unset):
            sc_property_address = UNSET
        else:
            sc_property_address = self.sc_property_address

        en_district: None | str | Unset
        if isinstance(self.en_district, Unset):
            en_district = UNSET
        else:
            en_district = self.en_district

        tc_district: None | str | Unset
        if isinstance(self.tc_district, Unset):
            tc_district = UNSET
        else:
            tc_district = self.tc_district

        sc_district: None | str | Unset
        if isinstance(self.sc_district, Unset):
            sc_district = UNSET
        else:
            sc_district = self.sc_district

        tender_quotation_reference_number: None | str | Unset
        if isinstance(self.tender_quotation_reference_number, Unset):
            tender_quotation_reference_number = UNSET
        else:
            tender_quotation_reference_number = self.tender_quotation_reference_number

        en_name_of_tenant: None | str | Unset
        if isinstance(self.en_name_of_tenant, Unset):
            en_name_of_tenant = UNSET
        else:
            en_name_of_tenant = self.en_name_of_tenant

        tc_name_of_tenant: None | str | Unset
        if isinstance(self.tc_name_of_tenant, Unset):
            tc_name_of_tenant = UNSET
        else:
            tc_name_of_tenant = self.tc_name_of_tenant

        sc_name_of_tenant: None | str | Unset
        if isinstance(self.sc_name_of_tenant, Unset):
            sc_name_of_tenant = UNSET
        else:
            sc_name_of_tenant = self.sc_name_of_tenant

        en_tenancy_term: None | str | Unset
        if isinstance(self.en_tenancy_term, Unset):
            en_tenancy_term = UNSET
        else:
            en_tenancy_term = self.en_tenancy_term

        tc_tenancy_term: None | str | Unset
        if isinstance(self.tc_tenancy_term, Unset):
            tc_tenancy_term = UNSET
        else:
            tc_tenancy_term = self.tc_tenancy_term

        sc_tenancy_term: None | str | Unset
        if isinstance(self.sc_tenancy_term, Unset):
            sc_tenancy_term = UNSET
        else:
            sc_tenancy_term = self.sc_tenancy_term

        en_amount: None | str | Unset
        if isinstance(self.en_amount, Unset):
            en_amount = UNSET
        else:
            en_amount = self.en_amount

        tc_amount: None | str | Unset
        if isinstance(self.tc_amount, Unset):
            tc_amount = UNSET
        else:
            tc_amount = self.tc_amount

        sc_amount: None | str | Unset
        if isinstance(self.sc_amount, Unset):
            sc_amount = UNSET
        else:
            sc_amount = self.sc_amount

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en_property_name is not UNSET:
            field_dict["en_property_name"] = en_property_name
        if tc_property_name is not UNSET:
            field_dict["tc_property_name"] = tc_property_name
        if sc_property_name is not UNSET:
            field_dict["sc_property_name"] = sc_property_name
        if en_property_address is not UNSET:
            field_dict["en_property_address"] = en_property_address
        if tc_property_address is not UNSET:
            field_dict["tc_property_address"] = tc_property_address
        if sc_property_address is not UNSET:
            field_dict["sc_property_address"] = sc_property_address
        if en_district is not UNSET:
            field_dict["en_district"] = en_district
        if tc_district is not UNSET:
            field_dict["tc_district"] = tc_district
        if sc_district is not UNSET:
            field_dict["sc_district"] = sc_district
        if tender_quotation_reference_number is not UNSET:
            field_dict["tender_quotation_reference_number"] = (
                tender_quotation_reference_number
            )
        if en_name_of_tenant is not UNSET:
            field_dict["en_name_of_tenant"] = en_name_of_tenant
        if tc_name_of_tenant is not UNSET:
            field_dict["tc_name_of_tenant"] = tc_name_of_tenant
        if sc_name_of_tenant is not UNSET:
            field_dict["sc_name_of_tenant"] = sc_name_of_tenant
        if en_tenancy_term is not UNSET:
            field_dict["en_tenancy_term"] = en_tenancy_term
        if tc_tenancy_term is not UNSET:
            field_dict["tc_tenancy_term"] = tc_tenancy_term
        if sc_tenancy_term is not UNSET:
            field_dict["sc_tenancy_term"] = sc_tenancy_term
        if en_amount is not UNSET:
            field_dict["en_amount"] = en_amount
        if tc_amount is not UNSET:
            field_dict["tc_amount"] = tc_amount
        if sc_amount is not UNSET:
            field_dict["sc_amount"] = sc_amount
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_en_property_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_property_name = _parse_en_property_name(d.pop("en_property_name", UNSET))

        def _parse_tc_property_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_property_name = _parse_tc_property_name(d.pop("tc_property_name", UNSET))

        def _parse_sc_property_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_property_name = _parse_sc_property_name(d.pop("sc_property_name", UNSET))

        def _parse_en_property_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_property_address = _parse_en_property_address(
            d.pop("en_property_address", UNSET)
        )

        def _parse_tc_property_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_property_address = _parse_tc_property_address(
            d.pop("tc_property_address", UNSET)
        )

        def _parse_sc_property_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_property_address = _parse_sc_property_address(
            d.pop("sc_property_address", UNSET)
        )

        def _parse_en_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_district = _parse_en_district(d.pop("en_district", UNSET))

        def _parse_tc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_district = _parse_tc_district(d.pop("tc_district", UNSET))

        def _parse_sc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_district = _parse_sc_district(d.pop("sc_district", UNSET))

        def _parse_tender_quotation_reference_number(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tender_quotation_reference_number = _parse_tender_quotation_reference_number(
            d.pop("tender_quotation_reference_number", UNSET)
        )

        def _parse_en_name_of_tenant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_name_of_tenant = _parse_en_name_of_tenant(d.pop("en_name_of_tenant", UNSET))

        def _parse_tc_name_of_tenant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_name_of_tenant = _parse_tc_name_of_tenant(d.pop("tc_name_of_tenant", UNSET))

        def _parse_sc_name_of_tenant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_name_of_tenant = _parse_sc_name_of_tenant(d.pop("sc_name_of_tenant", UNSET))

        def _parse_en_tenancy_term(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_tenancy_term = _parse_en_tenancy_term(d.pop("en_tenancy_term", UNSET))

        def _parse_tc_tenancy_term(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_tenancy_term = _parse_tc_tenancy_term(d.pop("tc_tenancy_term", UNSET))

        def _parse_sc_tenancy_term(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_tenancy_term = _parse_sc_tenancy_term(d.pop("sc_tenancy_term", UNSET))

        def _parse_en_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_amount = _parse_en_amount(d.pop("en_amount", UNSET))

        def _parse_tc_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_amount = _parse_tc_amount(d.pop("tc_amount", UNSET))

        def _parse_sc_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_amount = _parse_sc_amount(d.pop("sc_amount", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            en_property_name=en_property_name,
            tc_property_name=tc_property_name,
            sc_property_name=sc_property_name,
            en_property_address=en_property_address,
            tc_property_address=tc_property_address,
            sc_property_address=sc_property_address,
            en_district=en_district,
            tc_district=tc_district,
            sc_district=sc_district,
            tender_quotation_reference_number=tender_quotation_reference_number,
            en_name_of_tenant=en_name_of_tenant,
            tc_name_of_tenant=tc_name_of_tenant,
            sc_name_of_tenant=sc_name_of_tenant,
            en_tenancy_term=en_tenancy_term,
            tc_tenancy_term=tc_tenancy_term,
            sc_tenancy_term=sc_tenancy_term,
            en_amount=en_amount,
            tc_amount=tc_amount,
            sc_amount=sc_amount,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
