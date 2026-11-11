from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Schedule")


@_attrs_define
class Schedule:
    """Activity schedule. A timeFrom and timeTo value of 00:00 indicates a whole-day event.

    Attributes:
        date_from (str | Unset): Activity begin date, in dd-mm-yyyy format. Compatibility derivative also accepts
            retained publisher YYYY-MM-DD strings; the source still documents dd-mm-yyyy.
        date_to (str | Unset): Activity end date, in dd-mm-yyyy format. Compatibility derivative also accepts retained
            publisher YYYY-MM-DD strings; the source still documents dd-mm-yyyy.
        district_name_english (str | Unset): District in English where the activity will be held. Listed values are
            Territory-Wide, HK Island, Kowloon, New Territories, and Islands.
        district_name_s_chinese (str | Unset): District in Simplified Chinese where the activity will be held.
        district_name_t_chinese (str | Unset): District in Traditional Chinese where the activity will be held.
        location_name_english (str | Unset): Location in English where the activity will be held.
        location_name_s_chinese (str | Unset): Location in Simplified Chinese where the activity will be held.
        location_name_t_chinese (str | Unset): Location in Traditional Chinese where the activity will be held.
        time_from (str | Unset): Activity begin time, in HH:mm format. Retained publisher responses also include seconds
            (HH:mm:ss).
        time_to (str | Unset): Activity end time, in HH:mm format. Retained publisher responses also include seconds
            (HH:mm:ss).
    """

    date_from: str | Unset = UNSET
    date_to: str | Unset = UNSET
    district_name_english: str | Unset = UNSET
    district_name_s_chinese: str | Unset = UNSET
    district_name_t_chinese: str | Unset = UNSET
    location_name_english: str | Unset = UNSET
    location_name_s_chinese: str | Unset = UNSET
    location_name_t_chinese: str | Unset = UNSET
    time_from: str | Unset = UNSET
    time_to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_from = self.date_from

        date_to = self.date_to

        district_name_english = self.district_name_english

        district_name_s_chinese = self.district_name_s_chinese

        district_name_t_chinese = self.district_name_t_chinese

        location_name_english = self.location_name_english

        location_name_s_chinese = self.location_name_s_chinese

        location_name_t_chinese = self.location_name_t_chinese

        time_from = self.time_from

        time_to = self.time_to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_from is not UNSET:
            field_dict["dateFrom"] = date_from
        if date_to is not UNSET:
            field_dict["dateTo"] = date_to
        if district_name_english is not UNSET:
            field_dict["districtNameEnglish"] = district_name_english
        if district_name_s_chinese is not UNSET:
            field_dict["districtNameSChinese"] = district_name_s_chinese
        if district_name_t_chinese is not UNSET:
            field_dict["districtNameTChinese"] = district_name_t_chinese
        if location_name_english is not UNSET:
            field_dict["locationNameEnglish"] = location_name_english
        if location_name_s_chinese is not UNSET:
            field_dict["locationNameSChinese"] = location_name_s_chinese
        if location_name_t_chinese is not UNSET:
            field_dict["locationNameTChinese"] = location_name_t_chinese
        if time_from is not UNSET:
            field_dict["timeFrom"] = time_from
        if time_to is not UNSET:
            field_dict["timeTo"] = time_to

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date_from = d.pop("dateFrom", UNSET)

        date_to = d.pop("dateTo", UNSET)

        district_name_english = d.pop("districtNameEnglish", UNSET)

        district_name_s_chinese = d.pop("districtNameSChinese", UNSET)

        district_name_t_chinese = d.pop("districtNameTChinese", UNSET)

        location_name_english = d.pop("locationNameEnglish", UNSET)

        location_name_s_chinese = d.pop("locationNameSChinese", UNSET)

        location_name_t_chinese = d.pop("locationNameTChinese", UNSET)

        time_from = d.pop("timeFrom", UNSET)

        time_to = d.pop("timeTo", UNSET)

        schedule = cls(
            date_from=date_from,
            date_to=date_to,
            district_name_english=district_name_english,
            district_name_s_chinese=district_name_s_chinese,
            district_name_t_chinese=district_name_t_chinese,
            location_name_english=location_name_english,
            location_name_s_chinese=location_name_s_chinese,
            location_name_t_chinese=location_name_t_chinese,
            time_from=time_from,
            time_to=time_to,
        )

        schedule.additional_properties = d
        return schedule

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
