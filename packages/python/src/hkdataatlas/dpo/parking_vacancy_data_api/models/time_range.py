from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.weekdays_item import WeekdaysItem, check_weekdays_item

T = TypeVar("T", bound="TimeRange")


@_attrs_define
class TimeRange:
    """
    Attributes:
        exclude_public_holiday (bool):
        period_end (str):
        period_start (str):
        weekdays (list[WeekdaysItem]):
    """

    exclude_public_holiday: bool
    period_end: str
    period_start: str
    weekdays: list[WeekdaysItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude_public_holiday = self.exclude_public_holiday

        period_end = self.period_end

        period_start = self.period_start

        weekdays = []
        for componentsschemas_weekdays_item_data in self.weekdays:
            componentsschemas_weekdays_item: str = componentsschemas_weekdays_item_data
            weekdays.append(componentsschemas_weekdays_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "excludePublicHoliday": exclude_public_holiday,
                "periodEnd": period_end,
                "periodStart": period_start,
                "weekdays": weekdays,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        exclude_public_holiday = d.pop("excludePublicHoliday")

        period_end = d.pop("periodEnd")

        period_start = d.pop("periodStart")

        weekdays = []
        _weekdays = d.pop("weekdays")
        for componentsschemas_weekdays_item_data in _weekdays:
            componentsschemas_weekdays_item = check_weekdays_item(
                componentsschemas_weekdays_item_data
            )

            weekdays.append(componentsschemas_weekdays_item)

        time_range = cls(
            exclude_public_holiday=exclude_public_holiday,
            period_end=period_end,
            period_start=period_start,
            weekdays=weekdays,
        )

        time_range.additional_properties = d
        return time_range

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
