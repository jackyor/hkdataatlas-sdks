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
        address_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        address_english (None | str | Unset): Publisher field type: esriFieldTypeString
        building_premises_name_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        building_premises_name_english (None | str | Unset): Publisher field type: esriFieldTypeString
        date_of_expiry (None | str | Unset): Publisher field type: esriFieldTypeString
        date_of_registration (None | str | Unset): Publisher field type: esriFieldTypeString
        district_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        district_english (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_no (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_chinese: None | str | Unset = UNSET
    address_english: None | str | Unset = UNSET
    building_premises_name_chinese: None | str | Unset = UNSET
    building_premises_name_english: None | str | Unset = UNSET
    date_of_expiry: None | str | Unset = UNSET
    date_of_registration: None | str | Unset = UNSET
    district_chinese: None | str | Unset = UNSET
    district_english: None | str | Unset = UNSET
    registration_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_chinese: None | str | Unset
        if isinstance(self.address_chinese, Unset):
            address_chinese = UNSET
        else:
            address_chinese = self.address_chinese

        address_english: None | str | Unset
        if isinstance(self.address_english, Unset):
            address_english = UNSET
        else:
            address_english = self.address_english

        building_premises_name_chinese: None | str | Unset
        if isinstance(self.building_premises_name_chinese, Unset):
            building_premises_name_chinese = UNSET
        else:
            building_premises_name_chinese = self.building_premises_name_chinese

        building_premises_name_english: None | str | Unset
        if isinstance(self.building_premises_name_english, Unset):
            building_premises_name_english = UNSET
        else:
            building_premises_name_english = self.building_premises_name_english

        date_of_expiry: None | str | Unset
        if isinstance(self.date_of_expiry, Unset):
            date_of_expiry = UNSET
        else:
            date_of_expiry = self.date_of_expiry

        date_of_registration: None | str | Unset
        if isinstance(self.date_of_registration, Unset):
            date_of_registration = UNSET
        else:
            date_of_registration = self.date_of_registration

        district_chinese: None | str | Unset
        if isinstance(self.district_chinese, Unset):
            district_chinese = UNSET
        else:
            district_chinese = self.district_chinese

        district_english: None | str | Unset
        if isinstance(self.district_english, Unset):
            district_english = UNSET
        else:
            district_english = self.district_english

        registration_no: None | str | Unset
        if isinstance(self.registration_no, Unset):
            registration_no = UNSET
        else:
            registration_no = self.registration_no

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_chinese is not UNSET:
            field_dict["Address_Chinese"] = address_chinese
        if address_english is not UNSET:
            field_dict["Address_English"] = address_english
        if building_premises_name_chinese is not UNSET:
            field_dict["Building_Premises_Name_Chinese"] = (
                building_premises_name_chinese
            )
        if building_premises_name_english is not UNSET:
            field_dict["Building_Premises_Name_English"] = (
                building_premises_name_english
            )
        if date_of_expiry is not UNSET:
            field_dict["Date_of_Expiry"] = date_of_expiry
        if date_of_registration is not UNSET:
            field_dict["Date_of_Registration"] = date_of_registration
        if district_chinese is not UNSET:
            field_dict["District_Chinese"] = district_chinese
        if district_english is not UNSET:
            field_dict["District_English"] = district_english
        if registration_no is not UNSET:
            field_dict["Registration_No"] = registration_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chinese = _parse_address_chinese(d.pop("Address_Chinese", UNSET))

        def _parse_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_english = _parse_address_english(d.pop("Address_English", UNSET))

        def _parse_building_premises_name_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_premises_name_chinese = _parse_building_premises_name_chinese(
            d.pop("Building_Premises_Name_Chinese", UNSET)
        )

        def _parse_building_premises_name_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_premises_name_english = _parse_building_premises_name_english(
            d.pop("Building_Premises_Name_English", UNSET)
        )

        def _parse_date_of_expiry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_expiry = _parse_date_of_expiry(d.pop("Date_of_Expiry", UNSET))

        def _parse_date_of_registration(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_registration = _parse_date_of_registration(
            d.pop("Date_of_Registration", UNSET)
        )

        def _parse_district_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_chinese = _parse_district_chinese(d.pop("District_Chinese", UNSET))

        def _parse_district_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_english = _parse_district_english(d.pop("District_English", UNSET))

        def _parse_registration_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_no = _parse_registration_no(d.pop("Registration_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_chinese=address_chinese,
            address_english=address_english,
            building_premises_name_chinese=building_premises_name_chinese,
            building_premises_name_english=building_premises_name_english,
            date_of_expiry=date_of_expiry,
            date_of_registration=date_of_registration,
            district_chinese=district_chinese,
            district_english=district_english,
            registration_no=registration_no,
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
