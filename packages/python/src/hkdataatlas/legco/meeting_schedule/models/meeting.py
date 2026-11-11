from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting_committee import MeetingCommittee


T = TypeVar("T", bound="Meeting")


@_attrs_define
class Meeting:
    """Dictionary fields for a meeting record. No universal requiredness is specified.

    Attributes:
        tmeeting_committee (list[MeetingCommittee] | Unset): Associated meeting-committee records, where present. The
            dictionary documents the related table and fields but does not specify the exact serialized relationship shape.
        agenda_url_chi (str | Unset): URL of the Chinese meeting agenda. The dictionary example is a relative agenda
            path and shows a corresponding legco.gov.hk agenda URL.
        agenda_url_eng (str | Unset): URL of the English meeting agenda. The dictionary example is a relative agenda
            path and shows a corresponding legco.gov.hk agenda URL.
        meet_id (int | Unset): Meeting identifier. Dictionary example: 120514.
        meeting_type_chi (str | Unset): Meeting type in Chinese. Documented values: 閉門會議, 午宴∕晚宴∕其他, and 公開會議.
        meeting_type_eng (str | Unset): Meeting type in English. The dictionary specifies text but no values.
        start_date_time (datetime.datetime | Unset): Meeting start date and time. Dictionary format is YYYY-MM-
            DDThh:mm:ss (ISO 8601); example: 2016-10-18T16:30:00.
        subject_chi (str | Unset): Meeting subject in Chinese. Example: 房屋事務委員會會議.
        subject_eng (str | Unset): Meeting subject in English. Example: Meeting of Panel on Housing.
        term_id (int | Unset): Term identifier.
        venue_code (str | Unset): Code of the venue. Documented values: 1 (Chamber), 2 (Rm 1), 3 (Rm 2), 4 (Rm 2A), 5
            (Rm 2B), and 6 (Rm 3).
        venue_name_chi (str | Unset): Venue name in Chinese. Documented values: 會議廳, 會議室 1, 會議室 2, 會議室 2A, 會議室 2B, and
            會議室 3.
        venue_name_eng (str | Unset): Venue name in English. Documented values: Chamber, Conference Room 1, Conference
            Room 2, Conference Room 2A, Conference Room 2B, and Conference Room 3.
    """

    tmeeting_committee: list[MeetingCommittee] | Unset = UNSET
    agenda_url_chi: str | Unset = UNSET
    agenda_url_eng: str | Unset = UNSET
    meet_id: int | Unset = UNSET
    meeting_type_chi: str | Unset = UNSET
    meeting_type_eng: str | Unset = UNSET
    start_date_time: datetime.datetime | Unset = UNSET
    subject_chi: str | Unset = UNSET
    subject_eng: str | Unset = UNSET
    term_id: int | Unset = UNSET
    venue_code: str | Unset = UNSET
    venue_name_chi: str | Unset = UNSET
    venue_name_eng: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tmeeting_committee: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tmeeting_committee, Unset):
            tmeeting_committee = []
            for tmeeting_committee_item_data in self.tmeeting_committee:
                tmeeting_committee_item = tmeeting_committee_item_data.to_dict()
                tmeeting_committee.append(tmeeting_committee_item)

        agenda_url_chi = self.agenda_url_chi

        agenda_url_eng = self.agenda_url_eng

        meet_id = self.meet_id

        meeting_type_chi = self.meeting_type_chi

        meeting_type_eng = self.meeting_type_eng

        start_date_time: str | Unset = UNSET
        if not isinstance(self.start_date_time, Unset):
            start_date_time = self.start_date_time.isoformat()

        subject_chi = self.subject_chi

        subject_eng = self.subject_eng

        term_id = self.term_id

        venue_code = self.venue_code

        venue_name_chi = self.venue_name_chi

        venue_name_eng = self.venue_name_eng

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tmeeting_committee is not UNSET:
            field_dict["Tmeeting_committee"] = tmeeting_committee
        if agenda_url_chi is not UNSET:
            field_dict["agenda_url_chi"] = agenda_url_chi
        if agenda_url_eng is not UNSET:
            field_dict["agenda_url_eng"] = agenda_url_eng
        if meet_id is not UNSET:
            field_dict["meet_id"] = meet_id
        if meeting_type_chi is not UNSET:
            field_dict["meeting_type_chi"] = meeting_type_chi
        if meeting_type_eng is not UNSET:
            field_dict["meeting_type_eng"] = meeting_type_eng
        if start_date_time is not UNSET:
            field_dict["start_date_time"] = start_date_time
        if subject_chi is not UNSET:
            field_dict["subject_chi"] = subject_chi
        if subject_eng is not UNSET:
            field_dict["subject_eng"] = subject_eng
        if term_id is not UNSET:
            field_dict["term_id"] = term_id
        if venue_code is not UNSET:
            field_dict["venue_code"] = venue_code
        if venue_name_chi is not UNSET:
            field_dict["venue_name_chi"] = venue_name_chi
        if venue_name_eng is not UNSET:
            field_dict["venue_name_eng"] = venue_name_eng

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.meeting_committee import MeetingCommittee

        d = dict(src_dict)
        _tmeeting_committee = d.pop("Tmeeting_committee", UNSET)
        tmeeting_committee: list[MeetingCommittee] | Unset = UNSET
        if _tmeeting_committee is not UNSET:
            tmeeting_committee = []
            for tmeeting_committee_item_data in _tmeeting_committee:
                tmeeting_committee_item = MeetingCommittee.from_dict(
                    tmeeting_committee_item_data
                )

                tmeeting_committee.append(tmeeting_committee_item)

        agenda_url_chi = d.pop("agenda_url_chi", UNSET)

        agenda_url_eng = d.pop("agenda_url_eng", UNSET)

        meet_id = d.pop("meet_id", UNSET)

        meeting_type_chi = d.pop("meeting_type_chi", UNSET)

        meeting_type_eng = d.pop("meeting_type_eng", UNSET)

        _start_date_time = d.pop("start_date_time", UNSET)
        start_date_time: datetime.datetime | Unset
        if isinstance(_start_date_time, Unset):
            start_date_time = UNSET
        else:
            start_date_time = datetime.datetime.fromisoformat(_start_date_time)

        subject_chi = d.pop("subject_chi", UNSET)

        subject_eng = d.pop("subject_eng", UNSET)

        term_id = d.pop("term_id", UNSET)

        venue_code = d.pop("venue_code", UNSET)

        venue_name_chi = d.pop("venue_name_chi", UNSET)

        venue_name_eng = d.pop("venue_name_eng", UNSET)

        meeting = cls(
            tmeeting_committee=tmeeting_committee,
            agenda_url_chi=agenda_url_chi,
            agenda_url_eng=agenda_url_eng,
            meet_id=meet_id,
            meeting_type_chi=meeting_type_chi,
            meeting_type_eng=meeting_type_eng,
            start_date_time=start_date_time,
            subject_chi=subject_chi,
            subject_eng=subject_eng,
            term_id=term_id,
            venue_code=venue_code,
            venue_name_chi=venue_name_chi,
            venue_name_eng=venue_name_eng,
        )

        meeting.additional_properties = d
        return meeting

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
