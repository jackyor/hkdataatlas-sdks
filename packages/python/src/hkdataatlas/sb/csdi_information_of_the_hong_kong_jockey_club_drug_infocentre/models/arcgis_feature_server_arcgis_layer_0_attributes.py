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
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        number (float | None | Unset): Publisher field type: esriFieldTypeDouble
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        email (None | str | Unset): Publisher field type: esriFieldTypeString
        fax (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hour_en (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hour_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone (None | str | Unset): Publisher field type: esriFieldTypeString
        venue_en (None | str | Unset): Publisher field type: esriFieldTypeString
        venue_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        website (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    number: float | None | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    fax: None | str | Unset = UNSET
    opening_hour_en: None | str | Unset = UNSET
    opening_hour_tc: None | str | Unset = UNSET
    telephone: None | str | Unset = UNSET
    venue_en: None | str | Unset = UNSET
    venue_tc: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        number: float | None | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

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

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        fax: None | str | Unset
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        opening_hour_en: None | str | Unset
        if isinstance(self.opening_hour_en, Unset):
            opening_hour_en = UNSET
        else:
            opening_hour_en = self.opening_hour_en

        opening_hour_tc: None | str | Unset
        if isinstance(self.opening_hour_tc, Unset):
            opening_hour_tc = UNSET
        else:
            opening_hour_tc = self.opening_hour_tc

        telephone: None | str | Unset
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        venue_en: None | str | Unset
        if isinstance(self.venue_en, Unset):
            venue_en = UNSET
        else:
            venue_en = self.venue_en

        venue_tc: None | str | Unset
        if isinstance(self.venue_tc, Unset):
            venue_tc = UNSET
        else:
            venue_tc = self.venue_tc

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if number is not UNSET:
            field_dict["Number"] = number
        if address_en is not UNSET:
            field_dict["address_en"] = address_en
        if address_tc is not UNSET:
            field_dict["address_tc"] = address_tc
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if opening_hour_en is not UNSET:
            field_dict["opening_hour_en"] = opening_hour_en
        if opening_hour_tc is not UNSET:
            field_dict["opening_hour_tc"] = opening_hour_tc
        if telephone is not UNSET:
            field_dict["telephone"] = telephone
        if venue_en is not UNSET:
            field_dict["venue_en"] = venue_en
        if venue_tc is not UNSET:
            field_dict["venue_tc"] = venue_tc
        if website is not UNSET:
            field_dict["website"] = website
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_number(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        number = _parse_number(d.pop("Number", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("address_en", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("address_tc", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_fax(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax = _parse_fax(d.pop("fax", UNSET))

        def _parse_opening_hour_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hour_en = _parse_opening_hour_en(d.pop("opening_hour_en", UNSET))

        def _parse_opening_hour_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hour_tc = _parse_opening_hour_tc(d.pop("opening_hour_tc", UNSET))

        def _parse_telephone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone = _parse_telephone(d.pop("telephone", UNSET))

        def _parse_venue_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_en = _parse_venue_en(d.pop("venue_en", UNSET))

        def _parse_venue_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_tc = _parse_venue_tc(d.pop("venue_tc", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            latitude=latitude,
            longitude=longitude,
            number=number,
            address_en=address_en,
            address_tc=address_tc,
            email=email,
            fax=fax,
            opening_hour_en=opening_hour_en,
            opening_hour_tc=opening_hour_tc,
            telephone=telephone,
            venue_en=venue_en,
            venue_tc=venue_tc,
            website=website,
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
