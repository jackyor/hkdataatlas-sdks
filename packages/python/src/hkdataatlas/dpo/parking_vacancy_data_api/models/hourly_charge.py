from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.hourly_charge_covered import (
    HourlyChargeCovered,
    check_hourly_charge_covered,
)
from ..models.hourly_charge_type import HourlyChargeType, check_hourly_charge_type
from ..models.weekdays_item import WeekdaysItem, check_weekdays_item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_threshold import UsageThreshold


T = TypeVar("T", bound="HourlyCharge")


@_attrs_define
class HourlyCharge:
    """
    Attributes:
        covered (HourlyChargeCovered):
        exclude_public_holiday (bool):
        period_end (str):
        period_start (str):
        price (float): Rate in Hong Kong dollars.
        type_ (HourlyChargeType):
        weekdays (list[WeekdaysItem]):
        remark (str | Unset): Condition to which this rule applies; localized responses provide the remark in the
            specified locale.
        usage_thresholds (list[UsageThreshold] | Unset): Usage thresholds charged on a usage basis.
    """

    covered: HourlyChargeCovered
    exclude_public_holiday: bool
    period_end: str
    period_start: str
    price: float
    type_: HourlyChargeType
    weekdays: list[WeekdaysItem]
    remark: str | Unset = UNSET
    usage_thresholds: list[UsageThreshold] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        covered: str = self.covered

        exclude_public_holiday = self.exclude_public_holiday

        period_end = self.period_end

        period_start = self.period_start

        price = self.price

        type_: str = self.type_

        weekdays = []
        for componentsschemas_weekdays_item_data in self.weekdays:
            componentsschemas_weekdays_item: str = componentsschemas_weekdays_item_data
            weekdays.append(componentsschemas_weekdays_item)

        remark = self.remark

        usage_thresholds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage_thresholds, Unset):
            usage_thresholds = []
            for usage_thresholds_item_data in self.usage_thresholds:
                usage_thresholds_item = usage_thresholds_item_data.to_dict()
                usage_thresholds.append(usage_thresholds_item)

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
                "weekdays": weekdays,
            }
        )
        if remark is not UNSET:
            field_dict["remark"] = remark
        if usage_thresholds is not UNSET:
            field_dict["usageThresholds"] = usage_thresholds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_threshold import UsageThreshold

        d = dict(src_dict)
        covered = check_hourly_charge_covered(d.pop("covered"))

        exclude_public_holiday = d.pop("excludePublicHoliday")

        period_end = d.pop("periodEnd")

        period_start = d.pop("periodStart")

        price = d.pop("price")

        type_ = check_hourly_charge_type(d.pop("type"))

        weekdays = []
        _weekdays = d.pop("weekdays")
        for componentsschemas_weekdays_item_data in _weekdays:
            componentsschemas_weekdays_item = check_weekdays_item(
                componentsschemas_weekdays_item_data
            )

            weekdays.append(componentsschemas_weekdays_item)

        remark = d.pop("remark", UNSET)

        _usage_thresholds = d.pop("usageThresholds", UNSET)
        usage_thresholds: list[UsageThreshold] | Unset = UNSET
        if _usage_thresholds is not UNSET:
            usage_thresholds = []
            for usage_thresholds_item_data in _usage_thresholds:
                usage_thresholds_item = UsageThreshold.from_dict(
                    usage_thresholds_item_data
                )

                usage_thresholds.append(usage_thresholds_item)

        hourly_charge = cls(
            covered=covered,
            exclude_public_holiday=exclude_public_holiday,
            period_end=period_end,
            period_start=period_start,
            price=price,
            type_=type_,
            weekdays=weekdays,
            remark=remark,
            usage_thresholds=usage_thresholds,
        )

        hourly_charge.additional_properties = d
        return hourly_charge

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
