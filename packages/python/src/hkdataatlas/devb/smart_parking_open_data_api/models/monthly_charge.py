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
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charge_range import ChargeRange


T = TypeVar("T", bound="MonthlyCharge")


@_attrs_define
class MonthlyCharge:
    """
    Attributes:
        covered (MonthlyChargeCovered | Unset):
        price (float | Unset):
        ranges (list[ChargeRange] | Unset):
        remark (str | Unset):
        reserved (MonthlyChargeReserved | Unset):
        type_ (str | Unset): Monthly plan type; documented values include monthly-, bimonthly-, quarterly- and yearly-
            park, with day-park and night-park variants.
    """

    covered: MonthlyChargeCovered | Unset = UNSET
    price: float | Unset = UNSET
    ranges: list[ChargeRange] | Unset = UNSET
    remark: str | Unset = UNSET
    reserved: MonthlyChargeReserved | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        covered: str | Unset = UNSET
        if not isinstance(self.covered, Unset):
            covered = self.covered

        price = self.price

        ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        remark = self.remark

        reserved: str | Unset = UNSET
        if not isinstance(self.reserved, Unset):
            reserved = self.reserved

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if covered is not UNSET:
            field_dict["covered"] = covered
        if price is not UNSET:
            field_dict["price"] = price
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if remark is not UNSET:
            field_dict["remark"] = remark
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.charge_range import ChargeRange

        d = dict(src_dict)
        _covered = d.pop("covered", UNSET)
        covered: MonthlyChargeCovered | Unset
        if isinstance(_covered, Unset):
            covered = UNSET
        else:
            covered = check_monthly_charge_covered(_covered)

        price = d.pop("price", UNSET)

        _ranges = d.pop("ranges", UNSET)
        ranges: list[ChargeRange] | Unset = UNSET
        if _ranges is not UNSET:
            ranges = []
            for ranges_item_data in _ranges:
                ranges_item = ChargeRange.from_dict(ranges_item_data)

                ranges.append(ranges_item)

        remark = d.pop("remark", UNSET)

        _reserved = d.pop("reserved", UNSET)
        reserved: MonthlyChargeReserved | Unset
        if isinstance(_reserved, Unset):
            reserved = UNSET
        else:
            reserved = check_monthly_charge_reserved(_reserved)

        type_ = d.pop("type", UNSET)

        monthly_charge = cls(
            covered=covered,
            price=price,
            ranges=ranges,
            remark=remark,
            reserved=reserved,
            type_=type_,
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
