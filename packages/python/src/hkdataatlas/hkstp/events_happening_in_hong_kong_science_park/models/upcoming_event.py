from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpcomingEvent")


@_attrs_define
class UpcomingEvent:
    """
    Attributes:
        event_date (str | Unset): Start and/or End Date of the event.
        event_link_en (str | Unset): URL to the event page in EN.
        event_link_sc (None | str | Unset): URL to the event page in CHS.
        event_link_tc (None | str | Unset): URL to the event page in CHT.
        event_title_en (str | Unset): Title of the event in EN.
        event_title_sc (str | Unset): Title of the event in CHS.
        event_title_tc (str | Unset): Title of the event in CHT.
    """

    event_date: str | Unset = UNSET
    event_link_en: str | Unset = UNSET
    event_link_sc: None | str | Unset = UNSET
    event_link_tc: None | str | Unset = UNSET
    event_title_en: str | Unset = UNSET
    event_title_sc: str | Unset = UNSET
    event_title_tc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_date = self.event_date

        event_link_en = self.event_link_en

        event_link_sc: None | str | Unset
        if isinstance(self.event_link_sc, Unset):
            event_link_sc = UNSET
        else:
            event_link_sc = self.event_link_sc

        event_link_tc: None | str | Unset
        if isinstance(self.event_link_tc, Unset):
            event_link_tc = UNSET
        else:
            event_link_tc = self.event_link_tc

        event_title_en = self.event_title_en

        event_title_sc = self.event_title_sc

        event_title_tc = self.event_title_tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_date is not UNSET:
            field_dict["event_date"] = event_date
        if event_link_en is not UNSET:
            field_dict["event_link_EN"] = event_link_en
        if event_link_sc is not UNSET:
            field_dict["event_link_SC"] = event_link_sc
        if event_link_tc is not UNSET:
            field_dict["event_link_TC"] = event_link_tc
        if event_title_en is not UNSET:
            field_dict["event_title_EN"] = event_title_en
        if event_title_sc is not UNSET:
            field_dict["event_title_SC"] = event_title_sc
        if event_title_tc is not UNSET:
            field_dict["event_title_TC"] = event_title_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        event_date = d.pop("event_date", UNSET)

        event_link_en = d.pop("event_link_EN", UNSET)

        def _parse_event_link_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_link_sc = _parse_event_link_sc(d.pop("event_link_SC", UNSET))

        def _parse_event_link_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        event_link_tc = _parse_event_link_tc(d.pop("event_link_TC", UNSET))

        event_title_en = d.pop("event_title_EN", UNSET)

        event_title_sc = d.pop("event_title_SC", UNSET)

        event_title_tc = d.pop("event_title_TC", UNSET)

        upcoming_event = cls(
            event_date=event_date,
            event_link_en=event_link_en,
            event_link_sc=event_link_sc,
            event_link_tc=event_link_tc,
            event_title_en=event_title_en,
            event_title_sc=event_title_sc,
            event_title_tc=event_title_tc,
        )

        upcoming_event.additional_properties = d
        return upcoming_event

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
