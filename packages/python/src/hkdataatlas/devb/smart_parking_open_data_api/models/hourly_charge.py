from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.charge_base_covered import ChargeBaseCovered, check_charge_base_covered
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
        covered (ChargeBaseCovered | Unset):
        exclude_public_holiday (bool | Unset):
        period_end (str | Unset):
        period_start (str | Unset):
        price (float | Unset): Rate in Hong Kong dollars.
        remark (None | str | Unset): Applicable condition; sample includes null.
        type_ (HourlyChargeType | Unset):
        usage_thresholds (list[UsageThreshold] | Unset):
        weekdays (list[WeekdaysItem] | Unset):
    """

    covered: ChargeBaseCovered | Unset = UNSET
    exclude_public_holiday: bool | Unset = UNSET
    period_end: str | Unset = UNSET
    period_start: str | Unset = UNSET
    price: float | Unset = UNSET
    remark: None | str | Unset = UNSET
    type_: HourlyChargeType | Unset = UNSET
    usage_thresholds: list[UsageThreshold] | Unset = UNSET
    weekdays: list[WeekdaysItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        covered: str | Unset = UNSET
        if not isinstance(self.covered, Unset):
            covered = self.covered

        exclude_public_holiday = self.exclude_public_holiday

        period_end = self.period_end

        period_start = self.period_start

        price = self.price

        remark: None | str | Unset
        if isinstance(self.remark, Unset):
            remark = UNSET
        else:
            remark = self.remark

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        usage_thresholds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage_thresholds, Unset):
            usage_thresholds = []
            for usage_thresholds_item_data in self.usage_thresholds:
                usage_thresholds_item = usage_thresholds_item_data.to_dict()
                usage_thresholds.append(usage_thresholds_item)

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
        if covered is not UNSET:
            field_dict["covered"] = covered
        if exclude_public_holiday is not UNSET:
            field_dict["excludePublicHoliday"] = exclude_public_holiday
        if period_end is not UNSET:
            field_dict["periodEnd"] = period_end
        if period_start is not UNSET:
            field_dict["periodStart"] = period_start
        if price is not UNSET:
            field_dict["price"] = price
        if remark is not UNSET:
            field_dict["remark"] = remark
        if type_ is not UNSET:
            field_dict["type"] = type_
        if usage_thresholds is not UNSET:
            field_dict["usageThresholds"] = usage_thresholds
        if weekdays is not UNSET:
            field_dict["weekdays"] = weekdays

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_threshold import UsageThreshold

        d = dict(src_dict)
        _covered = d.pop("covered", UNSET)
        covered: ChargeBaseCovered | Unset
        if isinstance(_covered, Unset):
            covered = UNSET
        else:
            covered = check_charge_base_covered(_covered)

        exclude_public_holiday = d.pop("excludePublicHoliday", UNSET)

        period_end = d.pop("periodEnd", UNSET)

        period_start = d.pop("periodStart", UNSET)

        price = d.pop("price", UNSET)

        def _parse_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark = _parse_remark(d.pop("remark", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: HourlyChargeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_hourly_charge_type(_type_)

        _usage_thresholds = d.pop("usageThresholds", UNSET)
        usage_thresholds: list[UsageThreshold] | Unset = UNSET
        if _usage_thresholds is not UNSET:
            usage_thresholds = []
            for usage_thresholds_item_data in _usage_thresholds:
                usage_thresholds_item = UsageThreshold.from_dict(
                    usage_thresholds_item_data
                )

                usage_thresholds.append(usage_thresholds_item)

        _weekdays = d.pop("weekdays", UNSET)
        weekdays: list[WeekdaysItem] | Unset = UNSET
        if _weekdays is not UNSET:
            weekdays = []
            for componentsschemas_weekdays_item_data in _weekdays:
                componentsschemas_weekdays_item = check_weekdays_item(
                    componentsschemas_weekdays_item_data
                )

                weekdays.append(componentsschemas_weekdays_item)

        hourly_charge = cls(
            covered=covered,
            exclude_public_holiday=exclude_public_holiday,
            period_end=period_end,
            period_start=period_start,
            price=price,
            remark=remark,
            type_=type_,
            usage_thresholds=usage_thresholds,
            weekdays=weekdays,
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
