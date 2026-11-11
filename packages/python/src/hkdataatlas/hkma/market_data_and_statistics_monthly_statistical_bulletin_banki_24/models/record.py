from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        end_of_month (datetime.date | Unset):
        spot_assets (float | Unset):
        forward_purchases (float | Unset):
        spot_liabilities (float | Unset):
        forward_sales (float | Unset):
        net_spot_position (float | Unset):
        net_forward_position (float | Unset):
        open_position (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    spot_assets: float | Unset = UNSET
    forward_purchases: float | Unset = UNSET
    spot_liabilities: float | Unset = UNSET
    forward_sales: float | Unset = UNSET
    net_spot_position: float | Unset = UNSET
    net_forward_position: float | Unset = UNSET
    open_position: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        spot_assets = self.spot_assets

        forward_purchases = self.forward_purchases

        spot_liabilities = self.spot_liabilities

        forward_sales = self.forward_sales

        net_spot_position = self.net_spot_position

        net_forward_position = self.net_forward_position

        open_position = self.open_position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if spot_assets is not UNSET:
            field_dict["spot_assets"] = spot_assets
        if forward_purchases is not UNSET:
            field_dict["forward_purchases"] = forward_purchases
        if spot_liabilities is not UNSET:
            field_dict["spot_liabilities"] = spot_liabilities
        if forward_sales is not UNSET:
            field_dict["forward_sales"] = forward_sales
        if net_spot_position is not UNSET:
            field_dict["net_spot_position"] = net_spot_position
        if net_forward_position is not UNSET:
            field_dict["net_forward_position"] = net_forward_position
        if open_position is not UNSET:
            field_dict["open_position"] = open_position

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_month = d.pop("end_of_month", UNSET)
        end_of_month: datetime.date | Unset
        if isinstance(_end_of_month, Unset):
            end_of_month = UNSET
        else:
            end_of_month = datetime.date.fromisoformat(_end_of_month)

        spot_assets = d.pop("spot_assets", UNSET)

        forward_purchases = d.pop("forward_purchases", UNSET)

        spot_liabilities = d.pop("spot_liabilities", UNSET)

        forward_sales = d.pop("forward_sales", UNSET)

        net_spot_position = d.pop("net_spot_position", UNSET)

        net_forward_position = d.pop("net_forward_position", UNSET)

        open_position = d.pop("open_position", UNSET)

        record = cls(
            end_of_month=end_of_month,
            spot_assets=spot_assets,
            forward_purchases=forward_purchases,
            spot_liabilities=spot_liabilities,
            forward_sales=forward_sales,
            net_spot_position=net_spot_position,
            net_forward_position=net_forward_position,
            open_position=open_position,
        )

        record.additional_properties = d
        return record

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
