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
        collector_name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        collector_name_chin (None | str | Unset): Publisher field type: esriFieldTypeString
        address_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        address_chin (None | str | Unset): Publisher field type: esriFieldTypeString
        tel_no (None | str | Unset): Publisher field type: esriFieldTypeString
        email (None | str | Unset): Publisher field type: esriFieldTypeString
        company_website (None | str | Unset): Publisher field type: esriFieldTypeString
        waste_type_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        waste_type_chin (None | str | Unset): Publisher field type: esriFieldTypeString
        url (None | str | Unset): Publisher field type: esriFieldTypeString
        lat (None | str | Unset): Publisher field type: esriFieldTypeString
        long (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    collector_name_eng: None | str | Unset = UNSET
    collector_name_chin: None | str | Unset = UNSET
    address_eng: None | str | Unset = UNSET
    address_chin: None | str | Unset = UNSET
    tel_no: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    company_website: None | str | Unset = UNSET
    waste_type_eng: None | str | Unset = UNSET
    waste_type_chin: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    lat: None | str | Unset = UNSET
    long: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collector_name_eng: None | str | Unset
        if isinstance(self.collector_name_eng, Unset):
            collector_name_eng = UNSET
        else:
            collector_name_eng = self.collector_name_eng

        collector_name_chin: None | str | Unset
        if isinstance(self.collector_name_chin, Unset):
            collector_name_chin = UNSET
        else:
            collector_name_chin = self.collector_name_chin

        address_eng: None | str | Unset
        if isinstance(self.address_eng, Unset):
            address_eng = UNSET
        else:
            address_eng = self.address_eng

        address_chin: None | str | Unset
        if isinstance(self.address_chin, Unset):
            address_chin = UNSET
        else:
            address_chin = self.address_chin

        tel_no: None | str | Unset
        if isinstance(self.tel_no, Unset):
            tel_no = UNSET
        else:
            tel_no = self.tel_no

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        company_website: None | str | Unset
        if isinstance(self.company_website, Unset):
            company_website = UNSET
        else:
            company_website = self.company_website

        waste_type_eng: None | str | Unset
        if isinstance(self.waste_type_eng, Unset):
            waste_type_eng = UNSET
        else:
            waste_type_eng = self.waste_type_eng

        waste_type_chin: None | str | Unset
        if isinstance(self.waste_type_chin, Unset):
            waste_type_chin = UNSET
        else:
            waste_type_chin = self.waste_type_chin

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        lat: None | str | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        long: None | str | Unset
        if isinstance(self.long, Unset):
            long = UNSET
        else:
            long = self.long

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collector_name_eng is not UNSET:
            field_dict["Collector_Name_Eng"] = collector_name_eng
        if collector_name_chin is not UNSET:
            field_dict["Collector_Name_Chin"] = collector_name_chin
        if address_eng is not UNSET:
            field_dict["Address_Eng"] = address_eng
        if address_chin is not UNSET:
            field_dict["Address_Chin"] = address_chin
        if tel_no is not UNSET:
            field_dict["Tel_No"] = tel_no
        if email is not UNSET:
            field_dict["Email"] = email
        if company_website is not UNSET:
            field_dict["Company_Website"] = company_website
        if waste_type_eng is not UNSET:
            field_dict["Waste_Type_Eng"] = waste_type_eng
        if waste_type_chin is not UNSET:
            field_dict["Waste_Type_Chin"] = waste_type_chin
        if url is not UNSET:
            field_dict["URL"] = url
        if lat is not UNSET:
            field_dict["Lat"] = lat
        if long is not UNSET:
            field_dict["Long"] = long
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_collector_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collector_name_eng = _parse_collector_name_eng(
            d.pop("Collector_Name_Eng", UNSET)
        )

        def _parse_collector_name_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collector_name_chin = _parse_collector_name_chin(
            d.pop("Collector_Name_Chin", UNSET)
        )

        def _parse_address_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_eng = _parse_address_eng(d.pop("Address_Eng", UNSET))

        def _parse_address_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chin = _parse_address_chin(d.pop("Address_Chin", UNSET))

        def _parse_tel_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel_no = _parse_tel_no(d.pop("Tel_No", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("Email", UNSET))

        def _parse_company_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_website = _parse_company_website(d.pop("Company_Website", UNSET))

        def _parse_waste_type_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        waste_type_eng = _parse_waste_type_eng(d.pop("Waste_Type_Eng", UNSET))

        def _parse_waste_type_chin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        waste_type_chin = _parse_waste_type_chin(d.pop("Waste_Type_Chin", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("URL", UNSET))

        def _parse_lat(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lat = _parse_lat(d.pop("Lat", UNSET))

        def _parse_long(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        long = _parse_long(d.pop("Long", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            collector_name_eng=collector_name_eng,
            collector_name_chin=collector_name_chin,
            address_eng=address_eng,
            address_chin=address_chin,
            tel_no=tel_no,
            email=email,
            company_website=company_website,
            waste_type_eng=waste_type_eng,
            waste_type_chin=waste_type_chin,
            url=url,
            lat=lat,
            long=long,
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
