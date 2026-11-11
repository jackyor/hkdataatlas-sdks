from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchiveMeeting")


@_attrs_define
class ArchiveMeeting:
    """Field specification for archive meetings (VArchiveMeeting). The data dictionary lists the same fields and examples
    as live meetings; it does not declare which fields are always present.

        Attributes:
            chi_meet_name (str | Unset): Chinese meeting name.
            chi_meet_room_name (str | Unset): Chinese meeting room name.
            meet_date (datetime.datetime | str | Unset): The dictionary explicitly shows local date-time strings without an
                offset. Retain that documented representation alongside the prior RFC3339 branch; no timezone is fabricated.
            meet_name (str | Unset): English meeting name.
            meet_room_name (str | Unset): English meeting room name.
            meet_time (datetime.datetime | str | Unset): The dictionary explicitly shows local date-time strings without an
                offset. Retain that documented representation alongside the prior RFC3339 branch; no timezone is fabricated.
            meeting_id (str | Unset): Meeting identifier.
            link (str | Unset): URL of the meeting in Webcast.
            thumbnail (str | Unset): URL of thumbnail in Webcast.
    """

    chi_meet_name: str | Unset = UNSET
    chi_meet_room_name: str | Unset = UNSET
    meet_date: datetime.datetime | str | Unset = UNSET
    meet_name: str | Unset = UNSET
    meet_room_name: str | Unset = UNSET
    meet_time: datetime.datetime | str | Unset = UNSET
    meeting_id: str | Unset = UNSET
    link: str | Unset = UNSET
    thumbnail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chi_meet_name = self.chi_meet_name

        chi_meet_room_name = self.chi_meet_room_name

        meet_date: str | Unset
        if isinstance(self.meet_date, Unset):
            meet_date = UNSET
        elif isinstance(self.meet_date, datetime.datetime):
            meet_date = self.meet_date.isoformat()
        else:
            meet_date = self.meet_date

        meet_name = self.meet_name

        meet_room_name = self.meet_room_name

        meet_time: str | Unset
        if isinstance(self.meet_time, Unset):
            meet_time = UNSET
        elif isinstance(self.meet_time, datetime.datetime):
            meet_time = self.meet_time.isoformat()
        else:
            meet_time = self.meet_time

        meeting_id = self.meeting_id

        link = self.link

        thumbnail = self.thumbnail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chi_meet_name is not UNSET:
            field_dict["ChiMeetName"] = chi_meet_name
        if chi_meet_room_name is not UNSET:
            field_dict["ChiMeetRoomName"] = chi_meet_room_name
        if meet_date is not UNSET:
            field_dict["MeetDate"] = meet_date
        if meet_name is not UNSET:
            field_dict["MeetName"] = meet_name
        if meet_room_name is not UNSET:
            field_dict["MeetRoomName"] = meet_room_name
        if meet_time is not UNSET:
            field_dict["MeetTime"] = meet_time
        if meeting_id is not UNSET:
            field_dict["MeetingID"] = meeting_id
        if link is not UNSET:
            field_dict["link"] = link
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        chi_meet_name = d.pop("ChiMeetName", UNSET)

        chi_meet_room_name = d.pop("ChiMeetRoomName", UNSET)

        def _parse_meet_date(data: object) -> datetime.datetime | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                meet_date_type_0 = datetime.datetime.fromisoformat(data)

                return meet_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | str | Unset, data)

        meet_date = _parse_meet_date(d.pop("MeetDate", UNSET))

        meet_name = d.pop("MeetName", UNSET)

        meet_room_name = d.pop("MeetRoomName", UNSET)

        def _parse_meet_time(data: object) -> datetime.datetime | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                meet_time_type_0 = datetime.datetime.fromisoformat(data)

                return meet_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | str | Unset, data)

        meet_time = _parse_meet_time(d.pop("MeetTime", UNSET))

        meeting_id = d.pop("MeetingID", UNSET)

        link = d.pop("link", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        archive_meeting = cls(
            chi_meet_name=chi_meet_name,
            chi_meet_room_name=chi_meet_room_name,
            meet_date=meet_date,
            meet_name=meet_name,
            meet_room_name=meet_room_name,
            meet_time=meet_time,
            meeting_id=meeting_id,
            link=link,
            thumbnail=thumbnail,
        )

        archive_meeting.additional_properties = d
        return archive_meeting

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
