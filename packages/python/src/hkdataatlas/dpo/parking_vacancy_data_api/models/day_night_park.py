from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.day_night_park_covered import (
    DayNightParkCovered,
    check_day_night_park_covered,
)
from ..models.day_night_park_type import DayNightParkType, check_day_night_park_type
from ..models.day_night_park_valid_until import (
    DayNightParkValidUntil,
    check_day_night_park_valid_until,
)
from ..models.weekdays_item import WeekdaysItem, check_weekdays_item
from ..types import UNSET, Unset

T = TypeVar("T", bound="DayNightPark")


@_attrs_define
class DayNightPark:
    """
    Attributes:
        covered (DayNightParkCovered):
        exclude_public_holiday (bool):
        period_end (str):
        period_start (str):
        price (float): Rate in Hong Kong dollars.
        type_ (DayNightParkType):
        valid_until (DayNightParkValidUntil):
        weekdays (list[WeekdaysItem]):
        remark (None | str | Unset): Condition to which this rule applies; localized responses provide the remark in the
            specified locale. The documented example uses null.
        valid_until_end (str | Unset): End time until which parking of the specified number of hours is valid. Example:
            24:00.
    """

    covered: DayNightParkCovered
    exclude_public_holiday: bool
    period_end: str
    period_start: str
    price: float
    type_: DayNightParkType
    valid_until: DayNightParkValidUntil
    weekdays: list[WeekdaysItem]
    remark: None | str | Unset = UNSET
    valid_until_end: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        covered: str = self.covered

        exclude_public_holiday = self.exclude_public_holiday

        period_end = self.period_end

        period_start = self.period_start

        price = self.price

        type_: str = self.type_

        valid_until: str = self.valid_until

        weekdays = []
        for componentsschemas_weekdays_item_data in self.weekdays:
            componentsschemas_weekdays_item: str = componentsschemas_weekdays_item_data
            weekdays.append(componentsschemas_weekdays_item)

        remark: None | str | Unset
        if isinstance(self.remark, Unset):
            remark = UNSET
        else:
            remark = self.remark

        valid_until_end = self.valid_until_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "covered": covered,
                "excludePublicHoliday": exclude_public_holiday,
                "periodEnd": period_end,
                "periodStart": period_start,
                "price": price,
                "type": type_,
                "validUntil": valid_until,
                "weekdays": weekdays,
            }
        )
        if remark is not UNSET:
            field_dict["remark"] = remark
        if valid_until_end is not UNSET:
            field_dict["validUntilEnd"] = valid_until_end

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        covered = check_day_night_park_covered(d.pop("covered"))

        exclude_public_holiday = d.pop("excludePublicHoliday")

        period_end = d.pop("periodEnd")

        period_start = d.pop("periodStart")

        price = d.pop("price")

        type_ = check_day_night_park_type(d.pop("type"))

        valid_until = check_day_night_park_valid_until(d.pop("validUntil"))

        weekdays = []
        _weekdays = d.pop("weekdays")
        for componentsschemas_weekdays_item_data in _weekdays:
            componentsschemas_weekdays_item = check_weekdays_item(
                componentsschemas_weekdays_item_data
            )

            weekdays.append(componentsschemas_weekdays_item)

        def _parse_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark = _parse_remark(d.pop("remark", UNSET))

        valid_until_end = d.pop("validUntilEnd", UNSET)

        day_night_park = cls(
            covered=covered,
            exclude_public_holiday=exclude_public_holiday,
            period_end=period_end,
            period_start=period_start,
            price=price,
            type_=type_,
            valid_until=valid_until,
            weekdays=weekdays,
            remark=remark,
            valid_until_end=valid_until_end,
        )

        day_night_park.additional_properties = d
        return day_night_park

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
