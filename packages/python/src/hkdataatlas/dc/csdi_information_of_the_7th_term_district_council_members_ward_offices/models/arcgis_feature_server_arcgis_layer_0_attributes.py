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
        district_in_english (None | str | Unset): Publisher field type: esriFieldTypeString
        district_in_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_dc_member_in_english (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_dc_member_in_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        office_address_in_english (None | str | Unset): Publisher field type: esriFieldTypeString
        office_address_in_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        office_telephone_no (None | str | Unset): Publisher field type: esriFieldTypeString
        operating_hours_of_ward_office (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    district_in_english: None | str | Unset = UNSET
    district_in_chinese: None | str | Unset = UNSET
    name_of_dc_member_in_english: None | str | Unset = UNSET
    name_of_dc_member_in_chinese: None | str | Unset = UNSET
    office_address_in_english: None | str | Unset = UNSET
    office_address_in_chinese: None | str | Unset = UNSET
    office_telephone_no: None | str | Unset = UNSET
    operating_hours_of_ward_office: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        district_in_english: None | str | Unset
        if isinstance(self.district_in_english, Unset):
            district_in_english = UNSET
        else:
            district_in_english = self.district_in_english

        district_in_chinese: None | str | Unset
        if isinstance(self.district_in_chinese, Unset):
            district_in_chinese = UNSET
        else:
            district_in_chinese = self.district_in_chinese

        name_of_dc_member_in_english: None | str | Unset
        if isinstance(self.name_of_dc_member_in_english, Unset):
            name_of_dc_member_in_english = UNSET
        else:
            name_of_dc_member_in_english = self.name_of_dc_member_in_english

        name_of_dc_member_in_chinese: None | str | Unset
        if isinstance(self.name_of_dc_member_in_chinese, Unset):
            name_of_dc_member_in_chinese = UNSET
        else:
            name_of_dc_member_in_chinese = self.name_of_dc_member_in_chinese

        office_address_in_english: None | str | Unset
        if isinstance(self.office_address_in_english, Unset):
            office_address_in_english = UNSET
        else:
            office_address_in_english = self.office_address_in_english

        office_address_in_chinese: None | str | Unset
        if isinstance(self.office_address_in_chinese, Unset):
            office_address_in_chinese = UNSET
        else:
            office_address_in_chinese = self.office_address_in_chinese

        office_telephone_no: None | str | Unset
        if isinstance(self.office_telephone_no, Unset):
            office_telephone_no = UNSET
        else:
            office_telephone_no = self.office_telephone_no

        operating_hours_of_ward_office: None | str | Unset
        if isinstance(self.operating_hours_of_ward_office, Unset):
            operating_hours_of_ward_office = UNSET
        else:
            operating_hours_of_ward_office = self.operating_hours_of_ward_office

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if district_in_english is not UNSET:
            field_dict["District_in_English"] = district_in_english
        if district_in_chinese is not UNSET:
            field_dict["District_in_Chinese"] = district_in_chinese
        if name_of_dc_member_in_english is not UNSET:
            field_dict["Name_of_DC_Member_in_English"] = name_of_dc_member_in_english
        if name_of_dc_member_in_chinese is not UNSET:
            field_dict["Name_of_DC_Member_in_Chinese"] = name_of_dc_member_in_chinese
        if office_address_in_english is not UNSET:
            field_dict["Office_Address_in_English"] = office_address_in_english
        if office_address_in_chinese is not UNSET:
            field_dict["Office_Address_in_Chinese"] = office_address_in_chinese
        if office_telephone_no is not UNSET:
            field_dict["Office_Telephone_No_"] = office_telephone_no
        if operating_hours_of_ward_office is not UNSET:
            field_dict["Operating_hours_of_ward_office"] = (
                operating_hours_of_ward_office
            )
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_district_in_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_in_english = _parse_district_in_english(
            d.pop("District_in_English", UNSET)
        )

        def _parse_district_in_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_in_chinese = _parse_district_in_chinese(
            d.pop("District_in_Chinese", UNSET)
        )

        def _parse_name_of_dc_member_in_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_dc_member_in_english = _parse_name_of_dc_member_in_english(
            d.pop("Name_of_DC_Member_in_English", UNSET)
        )

        def _parse_name_of_dc_member_in_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_dc_member_in_chinese = _parse_name_of_dc_member_in_chinese(
            d.pop("Name_of_DC_Member_in_Chinese", UNSET)
        )

        def _parse_office_address_in_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_address_in_english = _parse_office_address_in_english(
            d.pop("Office_Address_in_English", UNSET)
        )

        def _parse_office_address_in_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_address_in_chinese = _parse_office_address_in_chinese(
            d.pop("Office_Address_in_Chinese", UNSET)
        )

        def _parse_office_telephone_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_telephone_no = _parse_office_telephone_no(
            d.pop("Office_Telephone_No_", UNSET)
        )

        def _parse_operating_hours_of_ward_office(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operating_hours_of_ward_office = _parse_operating_hours_of_ward_office(
            d.pop("Operating_hours_of_ward_office", UNSET)
        )

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            district_in_english=district_in_english,
            district_in_chinese=district_in_chinese,
            name_of_dc_member_in_english=name_of_dc_member_in_english,
            name_of_dc_member_in_chinese=name_of_dc_member_in_chinese,
            office_address_in_english=office_address_in_english,
            office_address_in_chinese=office_address_in_chinese,
            office_telephone_no=office_telephone_no,
            operating_hours_of_ward_office=operating_hours_of_ward_office,
            latitude=latitude,
            longitude=longitude,
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
