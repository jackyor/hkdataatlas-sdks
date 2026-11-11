from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        event_date_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        event_date_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        event_date_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        event_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        event_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        event_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        venue_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        venue_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        venue_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    event_date_en: None | str | Unset = UNSET
    event_date_tc: None | str | Unset = UNSET
    event_date_sc: None | str | Unset = UNSET
    event_name_en: None | str | Unset = UNSET
    event_name_tc: None | str | Unset = UNSET
    event_name_sc: None | str | Unset = UNSET
    venue_en: None | str | Unset = UNSET
    venue_tc: None | str | Unset = UNSET
    venue_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_date_en: None | str | Unset
        if isinstance(self.event_date_en, Unset):
            event_date_en = UNSET
        else:
            event_date_en = self.event_date_en

        event_date_tc: None | str | Unset
        if isinstance(self.event_date_tc, Unset):
            event_date_tc = UNSET
        else:
            event_date_tc = self.event_date_tc

        event_date_sc: None | str | Unset
        if isinstance(self.event_date_sc, Unset):
            event_date_sc = UNSET
        else:
            event_date_sc = self.event_date_sc

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

        event_name_sc: None | str | Unset
        if isinstance(self.event_name_sc, Unset):
            event_name_sc = UNSET
        else:
            event_name_sc = self.event_name_sc

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

        venue_sc: None | str | Unset
        if isinstance(self.venue_sc, Unset):
            venue_sc = UNSET
        else:
            venue_sc = self.venue_sc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_date_en is not UNSET:
            field_dict["Event_Date_en"] = event_date_en
        if event_date_tc is not UNSET:
            field_dict["Event_Date_tc"] = event_date_tc
        if event_date_sc is not UNSET:
            field_dict["Event_Date_sc"] = event_date_sc
        if event_name_en is not UNSET:
            field_dict["Event_Name_en"] = event_name_en
        if event_name_tc is not UNSET:
            field_dict["Event_Name_tc"] = event_name_tc
        if event_name_sc is not UNSET:
            field_dict["Event_Name_sc"] = event_name_sc
        if venue_en is not UNSET:
            field_dict["Venue_en"] = venue_en
        if venue_tc is not UNSET:
            field_dict["Venue_tc"] = venue_tc
        if venue_sc is not UNSET:
            field_dict["Venue_sc"] = venue_sc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_event_date_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_date_en = _parse_event_date_en(d.pop("Event_Date_en", UNSET))

        def _parse_event_date_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_date_tc = _parse_event_date_tc(d.pop("Event_Date_tc", UNSET))

        def _parse_event_date_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_date_sc = _parse_event_date_sc(d.pop("Event_Date_sc", UNSET))

        def _parse_event_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_name_en = _parse_event_name_en(d.pop("Event_Name_en", UNSET))

        def _parse_event_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_name_tc = _parse_event_name_tc(d.pop("Event_Name_tc", UNSET))

        def _parse_event_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_name_sc = _parse_event_name_sc(d.pop("Event_Name_sc", UNSET))

        def _parse_venue_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_en = _parse_venue_en(d.pop("Venue_en", UNSET))

        def _parse_venue_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_tc = _parse_venue_tc(d.pop("Venue_tc", UNSET))

        def _parse_venue_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        venue_sc = _parse_venue_sc(d.pop("Venue_sc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            event_date_en=event_date_en,
            event_date_tc=event_date_tc,
            event_date_sc=event_date_sc,
            event_name_en=event_name_en,
            event_name_tc=event_name_tc,
            event_name_sc=event_name_sc,
            venue_en=venue_en,
            venue_tc=venue_tc,
            venue_sc=venue_sc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
