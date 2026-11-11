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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        park_id (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        display_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        display_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        display_address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        contact_no (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_status (None | str | Unset): Publisher field type: esriFieldTypeString
        height (int | None | Unset): Publisher field type: esriFieldTypeInteger
        remark_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        website_en (None | str | Unset): Publisher field type: esriFieldTypeString
        website_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        website_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        carpark_photo (None | str | Unset): Publisher field type: esriFieldTypeString
        vacancy_url (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    park_id: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    display_address_en: None | str | Unset = UNSET
    display_address_tc: None | str | Unset = UNSET
    display_address_sc: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    contact_no: None | str | Unset = UNSET
    opening_status: None | str | Unset = UNSET
    height: int | None | Unset = UNSET
    remark_en: None | str | Unset = UNSET
    remark_tc: None | str | Unset = UNSET
    remark_sc: None | str | Unset = UNSET
    website_en: None | str | Unset = UNSET
    website_tc: None | str | Unset = UNSET
    website_sc: None | str | Unset = UNSET
    carpark_photo: None | str | Unset = UNSET
    vacancy_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        park_id: None | str | Unset
        if isinstance(self.park_id, Unset):
            park_id = UNSET
        else:
            park_id = self.park_id

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        display_address_en: None | str | Unset
        if isinstance(self.display_address_en, Unset):
            display_address_en = UNSET
        else:
            display_address_en = self.display_address_en

        display_address_tc: None | str | Unset
        if isinstance(self.display_address_tc, Unset):
            display_address_tc = UNSET
        else:
            display_address_tc = self.display_address_tc

        display_address_sc: None | str | Unset
        if isinstance(self.display_address_sc, Unset):
            display_address_sc = UNSET
        else:
            display_address_sc = self.display_address_sc

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

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        contact_no: None | str | Unset
        if isinstance(self.contact_no, Unset):
            contact_no = UNSET
        else:
            contact_no = self.contact_no

        opening_status: None | str | Unset
        if isinstance(self.opening_status, Unset):
            opening_status = UNSET
        else:
            opening_status = self.opening_status

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        remark_en: None | str | Unset
        if isinstance(self.remark_en, Unset):
            remark_en = UNSET
        else:
            remark_en = self.remark_en

        remark_tc: None | str | Unset
        if isinstance(self.remark_tc, Unset):
            remark_tc = UNSET
        else:
            remark_tc = self.remark_tc

        remark_sc: None | str | Unset
        if isinstance(self.remark_sc, Unset):
            remark_sc = UNSET
        else:
            remark_sc = self.remark_sc

        website_en: None | str | Unset
        if isinstance(self.website_en, Unset):
            website_en = UNSET
        else:
            website_en = self.website_en

        website_tc: None | str | Unset
        if isinstance(self.website_tc, Unset):
            website_tc = UNSET
        else:
            website_tc = self.website_tc

        website_sc: None | str | Unset
        if isinstance(self.website_sc, Unset):
            website_sc = UNSET
        else:
            website_sc = self.website_sc

        carpark_photo: None | str | Unset
        if isinstance(self.carpark_photo, Unset):
            carpark_photo = UNSET
        else:
            carpark_photo = self.carpark_photo

        vacancy_url: None | str | Unset
        if isinstance(self.vacancy_url, Unset):
            vacancy_url = UNSET
        else:
            vacancy_url = self.vacancy_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if park_id is not UNSET:
            field_dict["park_id"] = park_id
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc
        if name_sc is not UNSET:
            field_dict["name_sc"] = name_sc
        if display_address_en is not UNSET:
            field_dict["displayAddress_en"] = display_address_en
        if display_address_tc is not UNSET:
            field_dict["displayAddress_tc"] = display_address_tc
        if display_address_sc is not UNSET:
            field_dict["displayAddress_sc"] = display_address_sc
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if district_en is not UNSET:
            field_dict["district_en"] = district_en
        if district_tc is not UNSET:
            field_dict["district_tc"] = district_tc
        if district_sc is not UNSET:
            field_dict["district_sc"] = district_sc
        if contact_no is not UNSET:
            field_dict["contactNo"] = contact_no
        if opening_status is not UNSET:
            field_dict["opening_status"] = opening_status
        if height is not UNSET:
            field_dict["height"] = height
        if remark_en is not UNSET:
            field_dict["remark_en"] = remark_en
        if remark_tc is not UNSET:
            field_dict["remark_tc"] = remark_tc
        if remark_sc is not UNSET:
            field_dict["remark_sc"] = remark_sc
        if website_en is not UNSET:
            field_dict["website_en"] = website_en
        if website_tc is not UNSET:
            field_dict["website_tc"] = website_tc
        if website_sc is not UNSET:
            field_dict["website_sc"] = website_sc
        if carpark_photo is not UNSET:
            field_dict["carpark_photo"] = carpark_photo
        if vacancy_url is not UNSET:
            field_dict["vacancy_url"] = vacancy_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_park_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        park_id = _parse_park_id(d.pop("park_id", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("name_en", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("name_tc", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("name_sc", UNSET))

        def _parse_display_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_address_en = _parse_display_address_en(
            d.pop("displayAddress_en", UNSET)
        )

        def _parse_display_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_address_tc = _parse_display_address_tc(
            d.pop("displayAddress_tc", UNSET)
        )

        def _parse_display_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_address_sc = _parse_display_address_sc(
            d.pop("displayAddress_sc", UNSET)
        )

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("district_en", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("district_tc", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("district_sc", UNSET))

        def _parse_contact_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_no = _parse_contact_no(d.pop("contactNo", UNSET))

        def _parse_opening_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_status = _parse_opening_status(d.pop("opening_status", UNSET))

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_remark_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_en = _parse_remark_en(d.pop("remark_en", UNSET))

        def _parse_remark_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_tc = _parse_remark_tc(d.pop("remark_tc", UNSET))

        def _parse_remark_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_sc = _parse_remark_sc(d.pop("remark_sc", UNSET))

        def _parse_website_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_en = _parse_website_en(d.pop("website_en", UNSET))

        def _parse_website_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_tc = _parse_website_tc(d.pop("website_tc", UNSET))

        def _parse_website_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_sc = _parse_website_sc(d.pop("website_sc", UNSET))

        def _parse_carpark_photo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carpark_photo = _parse_carpark_photo(d.pop("carpark_photo", UNSET))

        def _parse_vacancy_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vacancy_url = _parse_vacancy_url(d.pop("vacancy_url", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            park_id=park_id,
            name_en=name_en,
            name_tc=name_tc,
            name_sc=name_sc,
            display_address_en=display_address_en,
            display_address_tc=display_address_tc,
            display_address_sc=display_address_sc,
            latitude=latitude,
            longitude=longitude,
            district_en=district_en,
            district_tc=district_tc,
            district_sc=district_sc,
            contact_no=contact_no,
            opening_status=opening_status,
            height=height,
            remark_en=remark_en,
            remark_tc=remark_tc,
            remark_sc=remark_sc,
            website_en=website_en,
            website_tc=website_tc,
            website_sc=website_sc,
            carpark_photo=carpark_photo,
            vacancy_url=vacancy_url,
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
