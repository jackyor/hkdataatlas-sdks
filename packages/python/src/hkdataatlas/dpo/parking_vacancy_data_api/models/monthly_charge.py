from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.monthly_charge_covered import (
    MonthlyChargeCovered,
    check_monthly_charge_covered,
)
from ..models.monthly_charge_reserved import (
    MonthlyChargeReserved,
    check_monthly_charge_reserved,
)
from ..models.monthly_charge_type import MonthlyChargeType, check_monthly_charge_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_range import TimeRange


T = TypeVar("T", bound="MonthlyCharge")


@_attrs_define
class MonthlyCharge:
    """
    Attributes:
        covered (MonthlyChargeCovered):
        price (float): Rate in Hong Kong dollars.
        reserved (MonthlyChargeReserved):
        type_ (MonthlyChargeType):
        ranges (list[TimeRange] | Unset): Time periods in which the monthly charge rule particularly applies to
            day/night parking.
        remark (str | Unset): Condition to which this rule applies; localized responses provide the remark in the
            specified locale.
    """

    covered: MonthlyChargeCovered
    price: float
    reserved: MonthlyChargeReserved
    type_: MonthlyChargeType
    ranges: list[TimeRange] | Unset = UNSET
    remark: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        covered: str = self.covered

        price = self.price

        reserved: str = self.reserved

        type_: str = self.type_

        ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        remark = self.remark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "covered": covered,
                "price": price,
                "reserved": reserved,
                "type": type_,
            }
        )
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if remark is not UNSET:
            field_dict["remark"] = remark

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.time_range import TimeRange

        d = dict(src_dict)
        covered = check_monthly_charge_covered(d.pop("covered"))

        price = d.pop("price")

        reserved = check_monthly_charge_reserved(d.pop("reserved"))

        type_ = check_monthly_charge_type(d.pop("type"))

        _ranges = d.pop("ranges", UNSET)
        ranges: list[TimeRange] | Unset = UNSET
        if _ranges is not UNSET:
            ranges = []
            for ranges_item_data in _ranges:
                ranges_item = TimeRange.from_dict(ranges_item_data)

                ranges.append(ranges_item)

        remark = d.pop("remark", UNSET)

        monthly_charge = cls(
            covered=covered,
            price=price,
            reserved=reserved,
            type_=type_,
            ranges=ranges,
            remark=remark,
        )

        monthly_charge.additional_properties = d
        return monthly_charge

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
