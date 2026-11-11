from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.weekdays_item import WeekdaysItem, check_weekdays_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChargeRange")


@_attrs_define
class ChargeRange:
    """
    Attributes:
        exclude_public_holiday (bool | Unset):
        period_end (str | Unset):
        period_start (str | Unset):
        weekday_ranges (str | Unset):
        weekdays (list[WeekdaysItem] | Unset):
    """

    exclude_public_holiday: bool | Unset = UNSET
    period_end: str | Unset = UNSET
    period_start: str | Unset = UNSET
    weekday_ranges: str | Unset = UNSET
    weekdays: list[WeekdaysItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude_public_holiday = self.exclude_public_holiday

        period_end = self.period_end

        period_start = self.period_start

        weekday_ranges = self.weekday_ranges

        weekdays: list[str] | Unset = UNSET
        if not isinstance(self.weekdays, Unset):
            weekdays = []
            for componentsschemas_weekdays_item_data in self.weekdays:
                componentsschemas_weekdays_item: str = (
                    componentsschemas_weekdays_item_data
                )
                weekdays.append(componentsschemas_weekdays_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude_public_holiday is not UNSET:
            field_dict["excludePublicHoliday"] = exclude_public_holiday
        if period_end is not UNSET:
            field_dict["periodEnd"] = period_end
        if period_start is not UNSET:
            field_dict["periodStart"] = period_start
        if weekday_ranges is not UNSET:
            field_dict["weekdayRanges"] = weekday_ranges
        if weekdays is not UNSET:
            field_dict["weekdays"] = weekdays

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        exclude_public_holiday = d.pop("excludePublicHoliday", UNSET)

        period_end = d.pop("periodEnd", UNSET)

        period_start = d.pop("periodStart", UNSET)

        weekday_ranges = d.pop("weekdayRanges", UNSET)

        _weekdays = d.pop("weekdays", UNSET)
        weekdays: list[WeekdaysItem] | Unset = UNSET
        if _weekdays is not UNSET:
            weekdays = []
            for componentsschemas_weekdays_item_data in _weekdays:
                componentsschemas_weekdays_item = check_weekdays_item(
                    componentsschemas_weekdays_item_data
                )

                weekdays.append(componentsschemas_weekdays_item)

        charge_range = cls(
            exclude_public_holiday=exclude_public_holiday,
            period_end=period_end,
            period_start=period_start,
            weekday_ranges=weekday_ranges,
            weekdays=weekdays,
        )

        charge_range.additional_properties = d
        return charge_range

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
