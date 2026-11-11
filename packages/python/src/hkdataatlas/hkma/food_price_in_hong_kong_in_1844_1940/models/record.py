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
        fd_yr (datetime.date | Unset):
        fd_bread_a (float | Unset):
        fd_tobac_a (float | Unset):
        fd_coffee_a (float | Unset):
        fd_milk_a (float | Unset):
        fd_beef_a (float | Unset):
        fd_pork_a (float | Unset):
        fd_rice_a (float | Unset):
        fd_tea_a (float | Unset):
        fd_sugar_a (float | Unset):
        fd_salt_a (float | Unset):
        fd_beer_a (float | Unset):
    """

    fd_yr: datetime.date | Unset = UNSET
    fd_bread_a: float | Unset = UNSET
    fd_tobac_a: float | Unset = UNSET
    fd_coffee_a: float | Unset = UNSET
    fd_milk_a: float | Unset = UNSET
    fd_beef_a: float | Unset = UNSET
    fd_pork_a: float | Unset = UNSET
    fd_rice_a: float | Unset = UNSET
    fd_tea_a: float | Unset = UNSET
    fd_sugar_a: float | Unset = UNSET
    fd_salt_a: float | Unset = UNSET
    fd_beer_a: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fd_yr: str | Unset = UNSET
        if not isinstance(self.fd_yr, Unset):
            fd_yr = self.fd_yr.isoformat()

        fd_bread_a = self.fd_bread_a

        fd_tobac_a = self.fd_tobac_a

        fd_coffee_a = self.fd_coffee_a

        fd_milk_a = self.fd_milk_a

        fd_beef_a = self.fd_beef_a

        fd_pork_a = self.fd_pork_a

        fd_rice_a = self.fd_rice_a

        fd_tea_a = self.fd_tea_a

        fd_sugar_a = self.fd_sugar_a

        fd_salt_a = self.fd_salt_a

        fd_beer_a = self.fd_beer_a

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fd_yr is not UNSET:
            field_dict["Fd_yr"] = fd_yr
        if fd_bread_a is not UNSET:
            field_dict["Fd_bread_a"] = fd_bread_a
        if fd_tobac_a is not UNSET:
            field_dict["Fd_tobac_a"] = fd_tobac_a
        if fd_coffee_a is not UNSET:
            field_dict["Fd_coffee_a"] = fd_coffee_a
        if fd_milk_a is not UNSET:
            field_dict["Fd_milk_a"] = fd_milk_a
        if fd_beef_a is not UNSET:
            field_dict["Fd_beef_a"] = fd_beef_a
        if fd_pork_a is not UNSET:
            field_dict["Fd_pork_a"] = fd_pork_a
        if fd_rice_a is not UNSET:
            field_dict["Fd_rice_a"] = fd_rice_a
        if fd_tea_a is not UNSET:
            field_dict["Fd_tea_a"] = fd_tea_a
        if fd_sugar_a is not UNSET:
            field_dict["Fd_sugar_a"] = fd_sugar_a
        if fd_salt_a is not UNSET:
            field_dict["Fd_salt_a"] = fd_salt_a
        if fd_beer_a is not UNSET:
            field_dict["Fd_beer_a"] = fd_beer_a

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _fd_yr = d.pop("Fd_yr", UNSET)
        fd_yr: datetime.date | Unset
        if isinstance(_fd_yr, Unset):
            fd_yr = UNSET
        else:
            fd_yr = datetime.date.fromisoformat(_fd_yr)

        fd_bread_a = d.pop("Fd_bread_a", UNSET)

        fd_tobac_a = d.pop("Fd_tobac_a", UNSET)

        fd_coffee_a = d.pop("Fd_coffee_a", UNSET)

        fd_milk_a = d.pop("Fd_milk_a", UNSET)

        fd_beef_a = d.pop("Fd_beef_a", UNSET)

        fd_pork_a = d.pop("Fd_pork_a", UNSET)

        fd_rice_a = d.pop("Fd_rice_a", UNSET)

        fd_tea_a = d.pop("Fd_tea_a", UNSET)

        fd_sugar_a = d.pop("Fd_sugar_a", UNSET)

        fd_salt_a = d.pop("Fd_salt_a", UNSET)

        fd_beer_a = d.pop("Fd_beer_a", UNSET)

        record = cls(
            fd_yr=fd_yr,
            fd_bread_a=fd_bread_a,
            fd_tobac_a=fd_tobac_a,
            fd_coffee_a=fd_coffee_a,
            fd_milk_a=fd_milk_a,
            fd_beef_a=fd_beef_a,
            fd_pork_a=fd_pork_a,
            fd_rice_a=fd_rice_a,
            fd_tea_a=fd_tea_a,
            fd_sugar_a=fd_sugar_a,
            fd_salt_a=fd_salt_a,
            fd_beer_a=fd_beer_a,
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
