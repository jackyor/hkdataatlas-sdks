from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProgrammeResource")


@_attrs_define
class ProgrammeResource:
    """Permissive representation of programme data described by the publisher's field dictionary. The dictionary does not
    specify a top-level envelope, field requiredness, or whether all listed fields occur in every record. The schema
    therefore permits an object whose properties are documented fields without requiring them.

        Attributes:
            activity_no (str | Unset): Activity number. Format described as XXXYY9999XXX99: district/section code (XXX) is
                1–3 characters; YY is the last two digits of the financial start year; 9999 is a four-digit system-generated
                sequence number; the activity type code (XXX) is 3 characters.
            ballot_end_date (datetime.date | Unset): End date of ballot, formatted YYYY-MM-DD.
            ballot_start_date (datetime.date | Unset): Start date of ballot, formatted YYYY-MM-DD.
            enrol_end_date (datetime.date | Unset): Balloting submission end date for the activity, formatted YYYY-MM-DD.
            enrol_method (str | Unset): Enrollment method. Documented values are BALLOT (Ballot) and FCFS (First-come-first-
                served).
            enrol_start_date (datetime.date | Unset): Balloting submission start date for the activity, formatted YYYY-MM-
                DD.
            en_act_type_name (str | Unset): Activity type in English. Example: Aerobic Dance.
            en_day (str | Unset): Programme days of the week in English.
            en_district (str | Unset): District, section, or game in English. Examples: Eastern, Zoological and
                Horticultural Education Unit, Masters Games.
            en_notes (str | Unset): Customer remarks in English. Examples: Wear non-marking sports shoes; Bring your own
                racket and wear non-marking sports shoes.
            en_pgm_name (str | Unset): Activity name in English. Example: Aerobic Dance Training Course.
            en_target_grp (str | Unset): Target type of persons in English. Examples: General, Persons with Visual
                Impairment.
            en_url (str | Unset): Programme website (English version); publisher describes the value format as a hyperlink.
            en_venue (str | Unset): Venue in English.
            fee (float | Unset): Fee. Publisher data type: decimal number.
            max_age (float | Unset): Maximum age. Publisher data type: numeric.
            min_age (float | Unset): Minimum age. Publisher data type: numeric.
            open_enrol_end_date (datetime.date | Unset): End date of open enrollment for remaining quota, formatted YYYY-MM-
                DD.
            open_enrol_start_date (datetime.date | Unset): Start date of first-come-first-served enrollment, formatted YYYY-
                MM-DD.
            pgm_end_date (datetime.date | Unset): Programme end date, formatted YYYY-MM-DD. Example: 2019-01-15.
            pgm_end_time (str | Unset): Programme end time in 24-hour hh:mm format. Examples: 09:00, 22:00.
            pgm_start_date (datetime.date | Unset): Programme start date, formatted YYYY-MM-DD. Example: 2019-01-15.
            pgm_start_time (str | Unset): Programme start time in 24-hour hh:mm format. Examples: 09:00, 22:00.
            places_left (float | Unset): Places left as at now. Publisher data type: numeric.
            places_left_rel_tmr (float | Unset): Places left to be released tomorrow at 08:30. Publisher data type: numeric.
            quota (float | Unset): Quota. Publisher data type: numeric.
            sc_url (str | Unset): Programme website (Simplified Chinese version); publisher describes the value format as a
                hyperlink.
            tc_act_type_name (str | Unset): Activity type in Traditional Chinese. Example: 健體舞.
            tc_day (str | Unset): Programme days of the week in Traditional Chinese.
            tc_district (str | Unset): District, section, or game in Traditional Chinese. Examples: 東區, 動物及園藝教育組, 先進運動會.
            tc_notes (str | Unset): Customer remarks in Traditional Chinese. Examples: 穿不脫色運動鞋; 自備球拍及穿運動鞋.
            tc_pgm_name (str | Unset): Activity name in Traditional Chinese. Example: 健體舞訓練班.
            tc_target_grp (str | Unset): Target type of persons in Traditional Chinese. Examples: 一般人士, 視障人士.
            tc_url (str | Unset): Programme website (Traditional Chinese version); publisher describes the value format as a
                hyperlink.
            tc_venue (str | Unset): Venue in Traditional Chinese.
            walkin (datetime.date | Unset): Walk-in date, formatted YYYY-MM-DD.
    """

    activity_no: str | Unset = UNSET
    ballot_end_date: datetime.date | Unset = UNSET
    ballot_start_date: datetime.date | Unset = UNSET
    enrol_end_date: datetime.date | Unset = UNSET
    enrol_method: str | Unset = UNSET
    enrol_start_date: datetime.date | Unset = UNSET
    en_act_type_name: str | Unset = UNSET
    en_day: str | Unset = UNSET
    en_district: str | Unset = UNSET
    en_notes: str | Unset = UNSET
    en_pgm_name: str | Unset = UNSET
    en_target_grp: str | Unset = UNSET
    en_url: str | Unset = UNSET
    en_venue: str | Unset = UNSET
    fee: float | Unset = UNSET
    max_age: float | Unset = UNSET
    min_age: float | Unset = UNSET
    open_enrol_end_date: datetime.date | Unset = UNSET
    open_enrol_start_date: datetime.date | Unset = UNSET
    pgm_end_date: datetime.date | Unset = UNSET
    pgm_end_time: str | Unset = UNSET
    pgm_start_date: datetime.date | Unset = UNSET
    pgm_start_time: str | Unset = UNSET
    places_left: float | Unset = UNSET
    places_left_rel_tmr: float | Unset = UNSET
    quota: float | Unset = UNSET
    sc_url: str | Unset = UNSET
    tc_act_type_name: str | Unset = UNSET
    tc_day: str | Unset = UNSET
    tc_district: str | Unset = UNSET
    tc_notes: str | Unset = UNSET
    tc_pgm_name: str | Unset = UNSET
    tc_target_grp: str | Unset = UNSET
    tc_url: str | Unset = UNSET
    tc_venue: str | Unset = UNSET
    walkin: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_no = self.activity_no

        ballot_end_date: str | Unset = UNSET
        if not isinstance(self.ballot_end_date, Unset):
            ballot_end_date = self.ballot_end_date.isoformat()

        ballot_start_date: str | Unset = UNSET
        if not isinstance(self.ballot_start_date, Unset):
            ballot_start_date = self.ballot_start_date.isoformat()

        enrol_end_date: str | Unset = UNSET
        if not isinstance(self.enrol_end_date, Unset):
            enrol_end_date = self.enrol_end_date.isoformat()

        enrol_method = self.enrol_method

        enrol_start_date: str | Unset = UNSET
        if not isinstance(self.enrol_start_date, Unset):
            enrol_start_date = self.enrol_start_date.isoformat()

        en_act_type_name = self.en_act_type_name

        en_day = self.en_day

        en_district = self.en_district

        en_notes = self.en_notes

        en_pgm_name = self.en_pgm_name

        en_target_grp = self.en_target_grp

        en_url = self.en_url

        en_venue = self.en_venue

        fee = self.fee

        max_age = self.max_age

        min_age = self.min_age

        open_enrol_end_date: str | Unset = UNSET
        if not isinstance(self.open_enrol_end_date, Unset):
            open_enrol_end_date = self.open_enrol_end_date.isoformat()

        open_enrol_start_date: str | Unset = UNSET
        if not isinstance(self.open_enrol_start_date, Unset):
            open_enrol_start_date = self.open_enrol_start_date.isoformat()

        pgm_end_date: str | Unset = UNSET
        if not isinstance(self.pgm_end_date, Unset):
            pgm_end_date = self.pgm_end_date.isoformat()

        pgm_end_time = self.pgm_end_time

        pgm_start_date: str | Unset = UNSET
        if not isinstance(self.pgm_start_date, Unset):
            pgm_start_date = self.pgm_start_date.isoformat()

        pgm_start_time = self.pgm_start_time

        places_left = self.places_left

        places_left_rel_tmr = self.places_left_rel_tmr

        quota = self.quota

        sc_url = self.sc_url

        tc_act_type_name = self.tc_act_type_name

        tc_day = self.tc_day

        tc_district = self.tc_district

        tc_notes = self.tc_notes

        tc_pgm_name = self.tc_pgm_name

        tc_target_grp = self.tc_target_grp

        tc_url = self.tc_url

        tc_venue = self.tc_venue

        walkin: str | Unset = UNSET
        if not isinstance(self.walkin, Unset):
            walkin = self.walkin.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_no is not UNSET:
            field_dict["ACTIVITY_NO"] = activity_no
        if ballot_end_date is not UNSET:
            field_dict["BALLOT_END_DATE"] = ballot_end_date
        if ballot_start_date is not UNSET:
            field_dict["BALLOT_START_DATE"] = ballot_start_date
        if enrol_end_date is not UNSET:
            field_dict["ENROL_END_DATE"] = enrol_end_date
        if enrol_method is not UNSET:
            field_dict["ENROL_METHOD"] = enrol_method
        if enrol_start_date is not UNSET:
            field_dict["ENROL_START_DATE"] = enrol_start_date
        if en_act_type_name is not UNSET:
            field_dict["EN_ACT_TYPE_NAME"] = en_act_type_name
        if en_day is not UNSET:
            field_dict["EN_DAY"] = en_day
        if en_district is not UNSET:
            field_dict["EN_DISTRICT"] = en_district
        if en_notes is not UNSET:
            field_dict["EN_NOTES"] = en_notes
        if en_pgm_name is not UNSET:
            field_dict["EN_PGM_NAME"] = en_pgm_name
        if en_target_grp is not UNSET:
            field_dict["EN_TARGET_GRP"] = en_target_grp
        if en_url is not UNSET:
            field_dict["EN_URL"] = en_url
        if en_venue is not UNSET:
            field_dict["EN_VENUE"] = en_venue
        if fee is not UNSET:
            field_dict["FEE"] = fee
        if max_age is not UNSET:
            field_dict["MAX_AGE"] = max_age
        if min_age is not UNSET:
            field_dict["MIN_AGE"] = min_age
        if open_enrol_end_date is not UNSET:
            field_dict["OPEN_ENROL_END_DATE"] = open_enrol_end_date
        if open_enrol_start_date is not UNSET:
            field_dict["OPEN_ENROL_START_DATE"] = open_enrol_start_date
        if pgm_end_date is not UNSET:
            field_dict["PGM_END_DATE"] = pgm_end_date
        if pgm_end_time is not UNSET:
            field_dict["PGM_END_TIME"] = pgm_end_time
        if pgm_start_date is not UNSET:
            field_dict["PGM_START_DATE"] = pgm_start_date
        if pgm_start_time is not UNSET:
            field_dict["PGM_START_TIME"] = pgm_start_time
        if places_left is not UNSET:
            field_dict["PLACES_LEFT"] = places_left
        if places_left_rel_tmr is not UNSET:
            field_dict["PLACES_LEFT_REL_TMR"] = places_left_rel_tmr
        if quota is not UNSET:
            field_dict["QUOTA"] = quota
        if sc_url is not UNSET:
            field_dict["SC_URL"] = sc_url
        if tc_act_type_name is not UNSET:
            field_dict["TC_ACT_TYPE_NAME"] = tc_act_type_name
        if tc_day is not UNSET:
            field_dict["TC_DAY"] = tc_day
        if tc_district is not UNSET:
            field_dict["TC_DISTRICT"] = tc_district
        if tc_notes is not UNSET:
            field_dict["TC_NOTES"] = tc_notes
        if tc_pgm_name is not UNSET:
            field_dict["TC_PGM_NAME"] = tc_pgm_name
        if tc_target_grp is not UNSET:
            field_dict["TC_TARGET_GRP"] = tc_target_grp
        if tc_url is not UNSET:
            field_dict["TC_URL"] = tc_url
        if tc_venue is not UNSET:
            field_dict["TC_VENUE"] = tc_venue
        if walkin is not UNSET:
            field_dict["WALKIN"] = walkin

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        activity_no = d.pop("ACTIVITY_NO", UNSET)

        _ballot_end_date = d.pop("BALLOT_END_DATE", UNSET)
        ballot_end_date: datetime.date | Unset
        if isinstance(_ballot_end_date, Unset):
            ballot_end_date = UNSET
        else:
            ballot_end_date = datetime.date.fromisoformat(_ballot_end_date)

        _ballot_start_date = d.pop("BALLOT_START_DATE", UNSET)
        ballot_start_date: datetime.date | Unset
        if isinstance(_ballot_start_date, Unset):
            ballot_start_date = UNSET
        else:
            ballot_start_date = datetime.date.fromisoformat(_ballot_start_date)

        _enrol_end_date = d.pop("ENROL_END_DATE", UNSET)
        enrol_end_date: datetime.date | Unset
        if isinstance(_enrol_end_date, Unset):
            enrol_end_date = UNSET
        else:
            enrol_end_date = datetime.date.fromisoformat(_enrol_end_date)

        enrol_method = d.pop("ENROL_METHOD", UNSET)

        _enrol_start_date = d.pop("ENROL_START_DATE", UNSET)
        enrol_start_date: datetime.date | Unset
        if isinstance(_enrol_start_date, Unset):
            enrol_start_date = UNSET
        else:
            enrol_start_date = datetime.date.fromisoformat(_enrol_start_date)

        en_act_type_name = d.pop("EN_ACT_TYPE_NAME", UNSET)

        en_day = d.pop("EN_DAY", UNSET)

        en_district = d.pop("EN_DISTRICT", UNSET)

        en_notes = d.pop("EN_NOTES", UNSET)

        en_pgm_name = d.pop("EN_PGM_NAME", UNSET)

        en_target_grp = d.pop("EN_TARGET_GRP", UNSET)

        en_url = d.pop("EN_URL", UNSET)

        en_venue = d.pop("EN_VENUE", UNSET)

        fee = d.pop("FEE", UNSET)

        max_age = d.pop("MAX_AGE", UNSET)

        min_age = d.pop("MIN_AGE", UNSET)

        _open_enrol_end_date = d.pop("OPEN_ENROL_END_DATE", UNSET)
        open_enrol_end_date: datetime.date | Unset
        if isinstance(_open_enrol_end_date, Unset):
            open_enrol_end_date = UNSET
        else:
            open_enrol_end_date = datetime.date.fromisoformat(_open_enrol_end_date)

        _open_enrol_start_date = d.pop("OPEN_ENROL_START_DATE", UNSET)
        open_enrol_start_date: datetime.date | Unset
        if isinstance(_open_enrol_start_date, Unset):
            open_enrol_start_date = UNSET
        else:
            open_enrol_start_date = datetime.date.fromisoformat(_open_enrol_start_date)

        _pgm_end_date = d.pop("PGM_END_DATE", UNSET)
        pgm_end_date: datetime.date | Unset
        if isinstance(_pgm_end_date, Unset):
            pgm_end_date = UNSET
        else:
            pgm_end_date = datetime.date.fromisoformat(_pgm_end_date)

        pgm_end_time = d.pop("PGM_END_TIME", UNSET)

        _pgm_start_date = d.pop("PGM_START_DATE", UNSET)
        pgm_start_date: datetime.date | Unset
        if isinstance(_pgm_start_date, Unset):
            pgm_start_date = UNSET
        else:
            pgm_start_date = datetime.date.fromisoformat(_pgm_start_date)

        pgm_start_time = d.pop("PGM_START_TIME", UNSET)

        places_left = d.pop("PLACES_LEFT", UNSET)

        places_left_rel_tmr = d.pop("PLACES_LEFT_REL_TMR", UNSET)

        quota = d.pop("QUOTA", UNSET)

        sc_url = d.pop("SC_URL", UNSET)

        tc_act_type_name = d.pop("TC_ACT_TYPE_NAME", UNSET)

        tc_day = d.pop("TC_DAY", UNSET)

        tc_district = d.pop("TC_DISTRICT", UNSET)

        tc_notes = d.pop("TC_NOTES", UNSET)

        tc_pgm_name = d.pop("TC_PGM_NAME", UNSET)

        tc_target_grp = d.pop("TC_TARGET_GRP", UNSET)

        tc_url = d.pop("TC_URL", UNSET)

        tc_venue = d.pop("TC_VENUE", UNSET)

        _walkin = d.pop("WALKIN", UNSET)
        walkin: datetime.date | Unset
        if isinstance(_walkin, Unset):
            walkin = UNSET
        else:
            walkin = datetime.date.fromisoformat(_walkin)

        programme_resource = cls(
            activity_no=activity_no,
            ballot_end_date=ballot_end_date,
            ballot_start_date=ballot_start_date,
            enrol_end_date=enrol_end_date,
            enrol_method=enrol_method,
            enrol_start_date=enrol_start_date,
            en_act_type_name=en_act_type_name,
            en_day=en_day,
            en_district=en_district,
            en_notes=en_notes,
            en_pgm_name=en_pgm_name,
            en_target_grp=en_target_grp,
            en_url=en_url,
            en_venue=en_venue,
            fee=fee,
            max_age=max_age,
            min_age=min_age,
            open_enrol_end_date=open_enrol_end_date,
            open_enrol_start_date=open_enrol_start_date,
            pgm_end_date=pgm_end_date,
            pgm_end_time=pgm_end_time,
            pgm_start_date=pgm_start_date,
            pgm_start_time=pgm_start_time,
            places_left=places_left,
            places_left_rel_tmr=places_left_rel_tmr,
            quota=quota,
            sc_url=sc_url,
            tc_act_type_name=tc_act_type_name,
            tc_day=tc_day,
            tc_district=tc_district,
            tc_notes=tc_notes,
            tc_pgm_name=tc_pgm_name,
            tc_target_grp=tc_target_grp,
            tc_url=tc_url,
            tc_venue=tc_venue,
            walkin=walkin,
        )

        programme_resource.additional_properties = d
        return programme_resource

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
