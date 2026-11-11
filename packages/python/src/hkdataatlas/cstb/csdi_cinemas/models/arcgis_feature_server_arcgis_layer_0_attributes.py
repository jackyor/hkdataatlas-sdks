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
        contact_information (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_screen (float | None | Unset): Publisher field type: esriFieldTypeDouble
        no_seat (float | None | Unset): Publisher field type: esriFieldTypeDouble
        reference (None | str | Unset): Publisher field type: esriFieldTypeString
        website (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_en: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    contact_information: None | str | Unset = UNSET
    last_update: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    no_screen: float | None | Unset = UNSET
    no_seat: float | None | Unset = UNSET
    reference: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
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

        contact_information: None | str | Unset
        if isinstance(self.contact_information, Unset):
            contact_information = UNSET
        else:
            contact_information = self.contact_information

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        no_screen: float | None | Unset
        if isinstance(self.no_screen, Unset):
            no_screen = UNSET
        else:
            no_screen = self.no_screen

        no_seat: float | None | Unset
        if isinstance(self.no_seat, Unset):
            no_seat = UNSET
        else:
            no_seat = self.no_seat

        reference: None | str | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_sc is not UNSET:
            field_dict["Address_SC"] = address_sc
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if contact_information is not UNSET:
            field_dict["Contact_Information"] = contact_information
        if last_update is not UNSET:
            field_dict["Last_Update"] = last_update
        if name_en is not UNSET:
            field_dict["Name_EN"] = name_en
        if name_sc is not UNSET:
            field_dict["Name_SC"] = name_sc
        if name_tc is not UNSET:
            field_dict["Name_TC"] = name_tc
        if no_screen is not UNSET:
            field_dict["No_Screen"] = no_screen
        if no_seat is not UNSET:
            field_dict["No_Seat"] = no_seat
        if reference is not UNSET:
            field_dict["Reference"] = reference
        if website is not UNSET:
            field_dict["Website"] = website
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

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_SC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_contact_information(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_information = _parse_contact_information(
            d.pop("Contact_Information", UNSET)
        )

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("Last_Update", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("Name_EN", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("Name_SC", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("Name_TC", UNSET))

        def _parse_no_screen(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_screen = _parse_no_screen(d.pop("No_Screen", UNSET))

        def _parse_no_seat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_seat = _parse_no_seat(d.pop("No_Seat", UNSET))

        def _parse_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reference = _parse_reference(d.pop("Reference", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("Website", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            contact_information=contact_information,
            last_update=last_update,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            no_screen=no_screen,
            no_seat=no_seat,
            reference=reference,
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
