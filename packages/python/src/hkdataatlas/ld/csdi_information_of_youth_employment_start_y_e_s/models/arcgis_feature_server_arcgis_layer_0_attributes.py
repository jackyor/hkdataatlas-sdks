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
        facility_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_en (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        enquiry_hotline (None | str | Unset): Publisher field type: esriFieldTypeString
        email_address (None | str | Unset): Publisher field type: esriFieldTypeString
        operator_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        operator_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        operator_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    facility_name_en: None | str | Unset = UNSET
    facility_name_tc: None | str | Unset = UNSET
    facility_name_sc: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    opening_hours_en: None | str | Unset = UNSET
    opening_hours_tc: None | str | Unset = UNSET
    opening_hours_sc: None | str | Unset = UNSET
    enquiry_hotline: None | str | Unset = UNSET
    email_address: None | str | Unset = UNSET
    operator_name_en: None | str | Unset = UNSET
    operator_name_tc: None | str | Unset = UNSET
    operator_name_sc: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facility_name_en: None | str | Unset
        if isinstance(self.facility_name_en, Unset):
            facility_name_en = UNSET
        else:
            facility_name_en = self.facility_name_en

        facility_name_tc: None | str | Unset
        if isinstance(self.facility_name_tc, Unset):
            facility_name_tc = UNSET
        else:
            facility_name_tc = self.facility_name_tc

        facility_name_sc: None | str | Unset
        if isinstance(self.facility_name_sc, Unset):
            facility_name_sc = UNSET
        else:
            facility_name_sc = self.facility_name_sc

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        opening_hours_en: None | str | Unset
        if isinstance(self.opening_hours_en, Unset):
            opening_hours_en = UNSET
        else:
            opening_hours_en = self.opening_hours_en

        opening_hours_tc: None | str | Unset
        if isinstance(self.opening_hours_tc, Unset):
            opening_hours_tc = UNSET
        else:
            opening_hours_tc = self.opening_hours_tc

        opening_hours_sc: None | str | Unset
        if isinstance(self.opening_hours_sc, Unset):
            opening_hours_sc = UNSET
        else:
            opening_hours_sc = self.opening_hours_sc

        enquiry_hotline: None | str | Unset
        if isinstance(self.enquiry_hotline, Unset):
            enquiry_hotline = UNSET
        else:
            enquiry_hotline = self.enquiry_hotline

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

        operator_name_en: None | str | Unset
        if isinstance(self.operator_name_en, Unset):
            operator_name_en = UNSET
        else:
            operator_name_en = self.operator_name_en

        operator_name_tc: None | str | Unset
        if isinstance(self.operator_name_tc, Unset):
            operator_name_tc = UNSET
        else:
            operator_name_tc = self.operator_name_tc

        operator_name_sc: None | str | Unset
        if isinstance(self.operator_name_sc, Unset):
            operator_name_sc = UNSET
        else:
            operator_name_sc = self.operator_name_sc

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
        if facility_name_en is not UNSET:
            field_dict["Facility_Name_EN"] = facility_name_en
        if facility_name_tc is not UNSET:
            field_dict["Facility_Name_TC"] = facility_name_tc
        if facility_name_sc is not UNSET:
            field_dict["Facility_Name_SC"] = facility_name_sc
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if address_sc is not UNSET:
            field_dict["Address_SC"] = address_sc
        if opening_hours_en is not UNSET:
            field_dict["Opening_Hours_EN"] = opening_hours_en
        if opening_hours_tc is not UNSET:
            field_dict["Opening_Hours_TC"] = opening_hours_tc
        if opening_hours_sc is not UNSET:
            field_dict["Opening_Hours_SC"] = opening_hours_sc
        if enquiry_hotline is not UNSET:
            field_dict["Enquiry_Hotline"] = enquiry_hotline
        if email_address is not UNSET:
            field_dict["Email_Address"] = email_address
        if operator_name_en is not UNSET:
            field_dict["Operator_Name_EN"] = operator_name_en
        if operator_name_tc is not UNSET:
            field_dict["Operator_Name_TC"] = operator_name_tc
        if operator_name_sc is not UNSET:
            field_dict["Operator_Name_SC"] = operator_name_sc
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

        def _parse_facility_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_en = _parse_facility_name_en(d.pop("Facility_Name_EN", UNSET))

        def _parse_facility_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_tc = _parse_facility_name_tc(d.pop("Facility_Name_TC", UNSET))

        def _parse_facility_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_sc = _parse_facility_name_sc(d.pop("Facility_Name_SC", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_SC", UNSET))

        def _parse_opening_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_en = _parse_opening_hours_en(d.pop("Opening_Hours_EN", UNSET))

        def _parse_opening_hours_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_tc = _parse_opening_hours_tc(d.pop("Opening_Hours_TC", UNSET))

        def _parse_opening_hours_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_sc = _parse_opening_hours_sc(d.pop("Opening_Hours_SC", UNSET))

        def _parse_enquiry_hotline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        enquiry_hotline = _parse_enquiry_hotline(d.pop("Enquiry_Hotline", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("Email_Address", UNSET))

        def _parse_operator_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operator_name_en = _parse_operator_name_en(d.pop("Operator_Name_EN", UNSET))

        def _parse_operator_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operator_name_tc = _parse_operator_name_tc(d.pop("Operator_Name_TC", UNSET))

        def _parse_operator_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operator_name_sc = _parse_operator_name_sc(d.pop("Operator_Name_SC", UNSET))

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
            facility_name_en=facility_name_en,
            facility_name_tc=facility_name_tc,
            facility_name_sc=facility_name_sc,
            address_en=address_en,
            address_tc=address_tc,
            address_sc=address_sc,
            opening_hours_en=opening_hours_en,
            opening_hours_tc=opening_hours_tc,
            opening_hours_sc=opening_hours_sc,
            enquiry_hotline=enquiry_hotline,
            email_address=email_address,
            operator_name_en=operator_name_en,
            operator_name_tc=operator_name_tc,
            operator_name_sc=operator_name_sc,
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
