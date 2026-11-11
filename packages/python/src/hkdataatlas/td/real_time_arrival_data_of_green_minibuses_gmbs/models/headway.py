from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Headway")


@_attrs_define
class Headway:
    """
    Attributes:
        end_time (None | str | Unset): End time for the headway; null for a single-trip headway. Retained official
            headways use local clock strings such as06:30:00 without a timezone offset. No fullRFC3339time, inferred
            timezone or extra pattern is asserted.
        frequency (int | None | Unset): Headway frequency; null for a single-trip headway.
        frequency_upper (int | None | Unset): Upper bound of headway frequency, if applicable.
        headway_seq (int | Unset): Presentation sequence for the headway.
        public_holiday (bool | Unset): Whether this headway applies on public holidays.
        start_time (str | Unset): Start time for the headway. Retained official headways use local clock strings such
            as06:30:00 without a timezone offset. No fullRFC3339time, inferred timezone or extra pattern is asserted.
        weekdays (list[bool] | Unset): Boolean flags for weekdays when this headway applies, starting from Monday.
    """

    end_time: None | str | Unset = UNSET
    frequency: int | None | Unset = UNSET
    frequency_upper: int | None | Unset = UNSET
    headway_seq: int | Unset = UNSET
    public_holiday: bool | Unset = UNSET
    start_time: str | Unset = UNSET
    weekdays: list[bool] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_time: None | str | Unset
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        frequency: int | None | Unset
        if isinstance(self.frequency, Unset):
            frequency = UNSET
        else:
            frequency = self.frequency

        frequency_upper: int | None | Unset
        if isinstance(self.frequency_upper, Unset):
            frequency_upper = UNSET
        else:
            frequency_upper = self.frequency_upper

        headway_seq = self.headway_seq

        public_holiday = self.public_holiday

        start_time = self.start_time

        weekdays: list[bool] | Unset = UNSET
        if not isinstance(self.weekdays, Unset):
            weekdays = self.weekdays

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if frequency_upper is not UNSET:
            field_dict["frequency_upper"] = frequency_upper
        if headway_seq is not UNSET:
            field_dict["headway_seq"] = headway_seq
        if public_holiday is not UNSET:
            field_dict["public_holiday"] = public_holiday
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if weekdays is not UNSET:
            field_dict["weekdays"] = weekdays

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_end_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        def _parse_frequency(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        frequency = _parse_frequency(d.pop("frequency", UNSET))

        def _parse_frequency_upper(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        frequency_upper = _parse_frequency_upper(d.pop("frequency_upper", UNSET))

        headway_seq = d.pop("headway_seq", UNSET)

        public_holiday = d.pop("public_holiday", UNSET)

        start_time = d.pop("start_time", UNSET)

        weekdays = cast(list[bool], d.pop("weekdays", UNSET))

        headway = cls(
            end_time=end_time,
            frequency=frequency,
            frequency_upper=frequency_upper,
            headway_seq=headway_seq,
            public_holiday=public_holiday,
            start_time=start_time,
            weekdays=weekdays,
        )

        headway.additional_properties = d
        return headway

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
