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
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        category_en (None | str | Unset): Publisher field type: esriFieldTypeString
        category_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        category_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        country_officially_recognised_body_en (None | str | Unset): Publisher field type: esriFieldTypeString
        country_officially_recognised_body_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        country_officially_recognised_body_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        email_address (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        telephone (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_en: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    category_en: None | str | Unset = UNSET
    category_sc: None | str | Unset = UNSET
    category_tc: None | str | Unset = UNSET
    country_officially_recognised_body_en: None | str | Unset = UNSET
    country_officially_recognised_body_sc: None | str | Unset = UNSET
    country_officially_recognised_body_tc: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    email_address: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    telephone: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        category_en: None | str | Unset
        if isinstance(self.category_en, Unset):
            category_en = UNSET
        else:
            category_en = self.category_en

        category_sc: None | str | Unset
        if isinstance(self.category_sc, Unset):
            category_sc = UNSET
        else:
            category_sc = self.category_sc

        category_tc: None | str | Unset
        if isinstance(self.category_tc, Unset):
            category_tc = UNSET
        else:
            category_tc = self.category_tc

        country_officially_recognised_body_en: None | str | Unset
        if isinstance(self.country_officially_recognised_body_en, Unset):
            country_officially_recognised_body_en = UNSET
        else:
            country_officially_recognised_body_en = (
                self.country_officially_recognised_body_en
            )

        country_officially_recognised_body_sc: None | str | Unset
        if isinstance(self.country_officially_recognised_body_sc, Unset):
            country_officially_recognised_body_sc = UNSET
        else:
            country_officially_recognised_body_sc = (
                self.country_officially_recognised_body_sc
            )

        country_officially_recognised_body_tc: None | str | Unset
        if isinstance(self.country_officially_recognised_body_tc, Unset):
            country_officially_recognised_body_tc = UNSET
        else:
            country_officially_recognised_body_tc = (
                self.country_officially_recognised_body_tc
            )

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        email_address: None | str | Unset
        if isinstance(self.email_address, Unset):
            email_address = UNSET
        else:
            email_address = self.email_address

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

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["Address_en"] = address_en
        if address_sc is not UNSET:
            field_dict["Address_sc"] = address_sc
        if address_tc is not UNSET:
            field_dict["Address_tc"] = address_tc
        if category_en is not UNSET:
            field_dict["Category_en"] = category_en
        if category_sc is not UNSET:
            field_dict["Category_sc"] = category_sc
        if category_tc is not UNSET:
            field_dict["Category_tc"] = category_tc
        if country_officially_recognised_body_en is not UNSET:
            field_dict["Country_Officially_Recognised_Body_en"] = (
                country_officially_recognised_body_en
            )
        if country_officially_recognised_body_sc is not UNSET:
            field_dict["Country_Officially_Recognised_Body_sc"] = (
                country_officially_recognised_body_sc
            )
        if country_officially_recognised_body_tc is not UNSET:
            field_dict["Country_Officially_Recognised_Body_tc"] = (
                country_officially_recognised_body_tc
            )
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if email_address is not UNSET:
            field_dict["Email_Address"] = email_address
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if telephone is not UNSET:
            field_dict["Telephone"] = telephone
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_en", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_sc", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_tc", UNSET))

        def _parse_category_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_en = _parse_category_en(d.pop("Category_en", UNSET))

        def _parse_category_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_sc = _parse_category_sc(d.pop("Category_sc", UNSET))

        def _parse_category_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_tc = _parse_category_tc(d.pop("Category_tc", UNSET))

        def _parse_country_officially_recognised_body_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_officially_recognised_body_en = (
            _parse_country_officially_recognised_body_en(
                d.pop("Country_Officially_Recognised_Body_en", UNSET)
            )
        )

        def _parse_country_officially_recognised_body_sc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_officially_recognised_body_sc = (
            _parse_country_officially_recognised_body_sc(
                d.pop("Country_Officially_Recognised_Body_sc", UNSET)
            )
        )

        def _parse_country_officially_recognised_body_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_officially_recognised_body_tc = (
            _parse_country_officially_recognised_body_tc(
                d.pop("Country_Officially_Recognised_Body_tc", UNSET)
            )
        )

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_email_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address = _parse_email_address(d.pop("Email_Address", UNSET))

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

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("Telephone", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            category_en=category_en,
            category_sc=category_sc,
            category_tc=category_tc,
            country_officially_recognised_body_en=country_officially_recognised_body_en,
            country_officially_recognised_body_sc=country_officially_recognised_body_sc,
            country_officially_recognised_body_tc=country_officially_recognised_body_tc,
            easting=easting,
            email_address=email_address,
            latitude=latitude,
            longitude=longitude,
            northing=northing,
            telephone=telephone,
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
