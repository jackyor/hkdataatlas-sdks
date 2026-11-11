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
        en_name (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_name (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_name (None | str | Unset): Publisher field type: esriFieldTypeString
        en_address (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        en_region (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_region (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_region (None | str | Unset): Publisher field type: esriFieldTypeString
        year_awarded (None | str | Unset): Publisher field type: esriFieldTypeString
        contract_expiry (None | str | Unset): Publisher field type: esriFieldTypeString
        contract_number (None | str | Unset): Publisher field type: esriFieldTypeString
        en_area (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_area (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_area (None | str | Unset): Publisher field type: esriFieldTypeString
        en_name_of_contractor (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_name_of_contractor (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_name_of_contractor (None | str | Unset): Publisher field type: esriFieldTypeString
        contractors_website (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    en_name: None | str | Unset = UNSET
    tc_name: None | str | Unset = UNSET
    sc_name: None | str | Unset = UNSET
    en_address: None | str | Unset = UNSET
    tc_address: None | str | Unset = UNSET
    sc_address: None | str | Unset = UNSET
    en_region: None | str | Unset = UNSET
    tc_region: None | str | Unset = UNSET
    sc_region: None | str | Unset = UNSET
    year_awarded: None | str | Unset = UNSET
    contract_expiry: None | str | Unset = UNSET
    contract_number: None | str | Unset = UNSET
    en_area: None | str | Unset = UNSET
    tc_area: None | str | Unset = UNSET
    sc_area: None | str | Unset = UNSET
    en_name_of_contractor: None | str | Unset = UNSET
    tc_name_of_contractor: None | str | Unset = UNSET
    sc_name_of_contractor: None | str | Unset = UNSET
    contractors_website: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en_name: None | str | Unset
        if isinstance(self.en_name, Unset):
            en_name = UNSET
        else:
            en_name = self.en_name

        tc_name: None | str | Unset
        if isinstance(self.tc_name, Unset):
            tc_name = UNSET
        else:
            tc_name = self.tc_name

        sc_name: None | str | Unset
        if isinstance(self.sc_name, Unset):
            sc_name = UNSET
        else:
            sc_name = self.sc_name

        en_address: None | str | Unset
        if isinstance(self.en_address, Unset):
            en_address = UNSET
        else:
            en_address = self.en_address

        tc_address: None | str | Unset
        if isinstance(self.tc_address, Unset):
            tc_address = UNSET
        else:
            tc_address = self.tc_address

        sc_address: None | str | Unset
        if isinstance(self.sc_address, Unset):
            sc_address = UNSET
        else:
            sc_address = self.sc_address

        en_region: None | str | Unset
        if isinstance(self.en_region, Unset):
            en_region = UNSET
        else:
            en_region = self.en_region

        tc_region: None | str | Unset
        if isinstance(self.tc_region, Unset):
            tc_region = UNSET
        else:
            tc_region = self.tc_region

        sc_region: None | str | Unset
        if isinstance(self.sc_region, Unset):
            sc_region = UNSET
        else:
            sc_region = self.sc_region

        year_awarded: None | str | Unset
        if isinstance(self.year_awarded, Unset):
            year_awarded = UNSET
        else:
            year_awarded = self.year_awarded

        contract_expiry: None | str | Unset
        if isinstance(self.contract_expiry, Unset):
            contract_expiry = UNSET
        else:
            contract_expiry = self.contract_expiry

        contract_number: None | str | Unset
        if isinstance(self.contract_number, Unset):
            contract_number = UNSET
        else:
            contract_number = self.contract_number

        en_area: None | str | Unset
        if isinstance(self.en_area, Unset):
            en_area = UNSET
        else:
            en_area = self.en_area

        tc_area: None | str | Unset
        if isinstance(self.tc_area, Unset):
            tc_area = UNSET
        else:
            tc_area = self.tc_area

        sc_area: None | str | Unset
        if isinstance(self.sc_area, Unset):
            sc_area = UNSET
        else:
            sc_area = self.sc_area

        en_name_of_contractor: None | str | Unset
        if isinstance(self.en_name_of_contractor, Unset):
            en_name_of_contractor = UNSET
        else:
            en_name_of_contractor = self.en_name_of_contractor

        tc_name_of_contractor: None | str | Unset
        if isinstance(self.tc_name_of_contractor, Unset):
            tc_name_of_contractor = UNSET
        else:
            tc_name_of_contractor = self.tc_name_of_contractor

        sc_name_of_contractor: None | str | Unset
        if isinstance(self.sc_name_of_contractor, Unset):
            sc_name_of_contractor = UNSET
        else:
            sc_name_of_contractor = self.sc_name_of_contractor

        contractors_website: None | str | Unset
        if isinstance(self.contractors_website, Unset):
            contractors_website = UNSET
        else:
            contractors_website = self.contractors_website

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en_name is not UNSET:
            field_dict["en_name"] = en_name
        if tc_name is not UNSET:
            field_dict["tc_name"] = tc_name
        if sc_name is not UNSET:
            field_dict["sc_name"] = sc_name
        if en_address is not UNSET:
            field_dict["en_address"] = en_address
        if tc_address is not UNSET:
            field_dict["tc_address"] = tc_address
        if sc_address is not UNSET:
            field_dict["sc_address"] = sc_address
        if en_region is not UNSET:
            field_dict["en_region"] = en_region
        if tc_region is not UNSET:
            field_dict["tc_region"] = tc_region
        if sc_region is not UNSET:
            field_dict["sc_region"] = sc_region
        if year_awarded is not UNSET:
            field_dict["year_awarded"] = year_awarded
        if contract_expiry is not UNSET:
            field_dict["contract_expiry"] = contract_expiry
        if contract_number is not UNSET:
            field_dict["contract_number"] = contract_number
        if en_area is not UNSET:
            field_dict["en_area"] = en_area
        if tc_area is not UNSET:
            field_dict["tc_area"] = tc_area
        if sc_area is not UNSET:
            field_dict["sc_area"] = sc_area
        if en_name_of_contractor is not UNSET:
            field_dict["en_name_of_contractor"] = en_name_of_contractor
        if tc_name_of_contractor is not UNSET:
            field_dict["tc_name_of_contractor"] = tc_name_of_contractor
        if sc_name_of_contractor is not UNSET:
            field_dict["sc_name_of_contractor"] = sc_name_of_contractor
        if contractors_website is not UNSET:
            field_dict["contractors_website"] = contractors_website
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_en_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_name = _parse_en_name(d.pop("en_name", UNSET))

        def _parse_tc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_name = _parse_tc_name(d.pop("tc_name", UNSET))

        def _parse_sc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_name = _parse_sc_name(d.pop("sc_name", UNSET))

        def _parse_en_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_address = _parse_en_address(d.pop("en_address", UNSET))

        def _parse_tc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_address = _parse_tc_address(d.pop("tc_address", UNSET))

        def _parse_sc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_address = _parse_sc_address(d.pop("sc_address", UNSET))

        def _parse_en_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_region = _parse_en_region(d.pop("en_region", UNSET))

        def _parse_tc_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_region = _parse_tc_region(d.pop("tc_region", UNSET))

        def _parse_sc_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_region = _parse_sc_region(d.pop("sc_region", UNSET))

        def _parse_year_awarded(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_awarded = _parse_year_awarded(d.pop("year_awarded", UNSET))

        def _parse_contract_expiry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contract_expiry = _parse_contract_expiry(d.pop("contract_expiry", UNSET))

        def _parse_contract_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contract_number = _parse_contract_number(d.pop("contract_number", UNSET))

        def _parse_en_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_area = _parse_en_area(d.pop("en_area", UNSET))

        def _parse_tc_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_area = _parse_tc_area(d.pop("tc_area", UNSET))

        def _parse_sc_area(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_area = _parse_sc_area(d.pop("sc_area", UNSET))

        def _parse_en_name_of_contractor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_name_of_contractor = _parse_en_name_of_contractor(
            d.pop("en_name_of_contractor", UNSET)
        )

        def _parse_tc_name_of_contractor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_name_of_contractor = _parse_tc_name_of_contractor(
            d.pop("tc_name_of_contractor", UNSET)
        )

        def _parse_sc_name_of_contractor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_name_of_contractor = _parse_sc_name_of_contractor(
            d.pop("sc_name_of_contractor", UNSET)
        )

        def _parse_contractors_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contractors_website = _parse_contractors_website(
            d.pop("contractors_website", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            en_name=en_name,
            tc_name=tc_name,
            sc_name=sc_name,
            en_address=en_address,
            tc_address=tc_address,
            sc_address=sc_address,
            en_region=en_region,
            tc_region=tc_region,
            sc_region=sc_region,
            year_awarded=year_awarded,
            contract_expiry=contract_expiry,
            contract_number=contract_number,
            en_area=en_area,
            tc_area=tc_area,
            sc_area=sc_area,
            en_name_of_contractor=en_name_of_contractor,
            tc_name_of_contractor=tc_name_of_contractor,
            sc_name_of_contractor=sc_name_of_contractor,
            contractors_website=contractors_website,
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
