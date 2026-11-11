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
        date_en (None | str | Unset): Publisher field type: esriFieldTypeString
        date_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        date_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        event_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        event_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        venue_en (None | str | Unset): Publisher field type: esriFieldTypeString
        event_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        venue_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        venue_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        organizer_en (None | str | Unset): Publisher field type: esriFieldTypeString
        organizer_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        organizer_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        enquiry (None | str | Unset): Publisher field type: esriFieldTypeString
        website (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    date_en: None | str | Unset = UNSET
    date_tc: None | str | Unset = UNSET
    date_sc: None | str | Unset = UNSET
    event_name_en: None | str | Unset = UNSET
    event_name_tc: None | str | Unset = UNSET
    venue_en: None | str | Unset = UNSET
    event_name_sc: None | str | Unset = UNSET
    venue_tc: None | str | Unset = UNSET
    venue_sc: None | str | Unset = UNSET
    organizer_en: None | str | Unset = UNSET
    organizer_tc: None | str | Unset = UNSET
    organizer_sc: None | str | Unset = UNSET
    enquiry: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_en: None | str | Unset
        if isinstance(self.date_en, Unset):
            date_en = UNSET
        else:
            date_en = self.date_en

        date_tc: None | str | Unset
        if isinstance(self.date_tc, Unset):
            date_tc = UNSET
        else:
            date_tc = self.date_tc

        date_sc: None | str | Unset
        if isinstance(self.date_sc, Unset):
            date_sc = UNSET
        else:
            date_sc = self.date_sc

        event_name_en: None | str | Unset
        if isinstance(self.event_name_en, Unset):
            event_name_en = UNSET
        else:
            event_name_en = self.event_name_en

        event_name_tc: None | str | Unset
        if isinstance(self.event_name_tc, Unset):
            event_name_tc = UNSET
        else:
            event_name_tc = self.event_name_tc

        venue_en: None | str | Unset
        if isinstance(self.venue_en, Unset):
            venue_en = UNSET
        else:
            venue_en = self.venue_en

        event_name_sc: None | str | Unset
        if isinstance(self.event_name_sc, Unset):
            event_name_sc = UNSET
        else:
            event_name_sc = self.event_name_sc

        venue_tc: None | str | Unset
        if isinstance(self.venue_tc, Unset):
            venue_tc = UNSET
        else:
            venue_tc = self.venue_tc

        venue_sc: None | str | Unset
        if isinstance(self.venue_sc, Unset):
            venue_sc = UNSET
        else:
            venue_sc = self.venue_sc

        organizer_en: None | str | Unset
        if isinstance(self.organizer_en, Unset):
            organizer_en = UNSET
        else:
            organizer_en = self.organizer_en

        organizer_tc: None | str | Unset
        if isinstance(self.organizer_tc, Unset):
            organizer_tc = UNSET
        else:
            organizer_tc = self.organizer_tc

        organizer_sc: None | str | Unset
        if isinstance(self.organizer_sc, Unset):
            organizer_sc = UNSET
        else:
            organizer_sc = self.organizer_sc

        enquiry: None | str | Unset
        if isinstance(self.enquiry, Unset):
            enquiry = UNSET
        else:
            enquiry = self.enquiry

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_en is not UNSET:
            field_dict["date_en"] = date_en
        if date_tc is not UNSET:
            field_dict["date_tc"] = date_tc
        if date_sc is not UNSET:
            field_dict["date_sc"] = date_sc
        if event_name_en is not UNSET:
            field_dict["event_name_en"] = event_name_en
        if event_name_tc is not UNSET:
            field_dict["event_name_tc"] = event_name_tc
        if venue_en is not UNSET:
            field_dict["venue_en"] = venue_en
        if event_name_sc is not UNSET:
            field_dict["event_name_sc"] = event_name_sc
        if venue_tc is not UNSET:
            field_dict["venue_tc"] = venue_tc
        if venue_sc is not UNSET:
            field_dict["venue_sc"] = venue_sc
        if organizer_en is not UNSET:
            field_dict["organizer_en"] = organizer_en
        if organizer_tc is not UNSET:
            field_dict["organizer_tc"] = organizer_tc
        if organizer_sc is not UNSET:
            field_dict["organizer_sc"] = organizer_sc
        if enquiry is not UNSET:
            field_dict["enquiry"] = enquiry
        if website is not UNSET:
            field_dict["website"] = website
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_date_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_en = _parse_date_en(d.pop("date_en", UNSET))

        def _parse_date_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_tc = _parse_date_tc(d.pop("date_tc", UNSET))

        def _parse_date_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_sc = _parse_date_sc(d.pop("date_sc", UNSET))

        def _parse_event_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_name_en = _parse_event_name_en(d.pop("event_name_en", UNSET))

        def _parse_event_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_name_tc = _parse_event_name_tc(d.pop("event_name_tc", UNSET))

        def _parse_venue_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_en = _parse_venue_en(d.pop("venue_en", UNSET))

        def _parse_event_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_name_sc = _parse_event_name_sc(d.pop("event_name_sc", UNSET))

        def _parse_venue_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_tc = _parse_venue_tc(d.pop("venue_tc", UNSET))

        def _parse_venue_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_sc = _parse_venue_sc(d.pop("venue_sc", UNSET))

        def _parse_organizer_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organizer_en = _parse_organizer_en(d.pop("organizer_en", UNSET))

        def _parse_organizer_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organizer_tc = _parse_organizer_tc(d.pop("organizer_tc", UNSET))

        def _parse_organizer_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organizer_sc = _parse_organizer_sc(d.pop("organizer_sc", UNSET))

        def _parse_enquiry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        enquiry = _parse_enquiry(d.pop("enquiry", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            date_en=date_en,
            date_tc=date_tc,
            date_sc=date_sc,
            event_name_en=event_name_en,
            event_name_tc=event_name_tc,
            venue_en=venue_en,
            event_name_sc=event_name_sc,
            venue_tc=venue_tc,
            venue_sc=venue_sc,
            organizer_en=organizer_en,
            organizer_tc=organizer_tc,
            organizer_sc=organizer_sc,
            enquiry=enquiry,
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
