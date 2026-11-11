from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chi_street_building_no_confirmation_code import (
    ChiStreetBuildingNoConfirmationCode,
    check_chi_street_building_no_confirmation_code,
)
from ..models.chi_street_building_no_odd_even_indicator import (
    ChiStreetBuildingNoOddEvenIndicator,
    check_chi_street_building_no_odd_even_indicator,
)
from ..models.chi_street_building_no_unofficial_indicator import (
    ChiStreetBuildingNoUnofficialIndicator,
    check_chi_street_building_no_unofficial_indicator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChiStreet")


@_attrs_define
class ChiStreet:
    """Street name and building number information in Chinese.

    Attributes:
        building_no_confirmation_code (ChiStreetBuildingNoConfirmationCode | Unset): Building-number confirmation; when
            C or P, BuildingNoFrom must not be null.
        building_no_from (str | Unset): Starting or ending building number, including any non-numeric part.
        building_no_odd_even_indicator (ChiStreetBuildingNoOddEvenIndicator | Unset): O = odd numbers, E = even numbers,
            B = both even and odd numbers within the range.
        building_no_to (str | Unset): Starting or ending building number, including any non-numeric part.
        building_no_unofficial_indicator (ChiStreetBuildingNoUnofficialIndicator | Unset): Unofficial-address indicator:
            1 = unofficial building number or no building number; 2 = unofficial building number and building name.
        location_name (str | Unset): Place name in Chinese.
        street_name (str | Unset): Street name in Chinese.
    """

    building_no_confirmation_code: ChiStreetBuildingNoConfirmationCode | Unset = UNSET
    building_no_from: str | Unset = UNSET
    building_no_odd_even_indicator: ChiStreetBuildingNoOddEvenIndicator | Unset = UNSET
    building_no_to: str | Unset = UNSET
    building_no_unofficial_indicator: ChiStreetBuildingNoUnofficialIndicator | Unset = (
        UNSET
    )
    location_name: str | Unset = UNSET
    street_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        building_no_confirmation_code: str | Unset = UNSET
        if not isinstance(self.building_no_confirmation_code, Unset):
            building_no_confirmation_code = self.building_no_confirmation_code

        building_no_from = self.building_no_from

        building_no_odd_even_indicator: str | Unset = UNSET
        if not isinstance(self.building_no_odd_even_indicator, Unset):
            building_no_odd_even_indicator = self.building_no_odd_even_indicator

        building_no_to = self.building_no_to

        building_no_unofficial_indicator: str | Unset = UNSET
        if not isinstance(self.building_no_unofficial_indicator, Unset):
            building_no_unofficial_indicator = self.building_no_unofficial_indicator

        location_name = self.location_name

        street_name = self.street_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if building_no_confirmation_code is not UNSET:
            field_dict["BuildingNoConfirmationCode"] = building_no_confirmation_code
        if building_no_from is not UNSET:
            field_dict["BuildingNoFrom"] = building_no_from
        if building_no_odd_even_indicator is not UNSET:
            field_dict["BuildingNoOddEvenIndicator"] = building_no_odd_even_indicator
        if building_no_to is not UNSET:
            field_dict["BuildingNoTo"] = building_no_to
        if building_no_unofficial_indicator is not UNSET:
            field_dict["BuildingNoUnofficialIndicator"] = (
                building_no_unofficial_indicator
            )
        if location_name is not UNSET:
            field_dict["LocationName"] = location_name
        if street_name is not UNSET:
            field_dict["StreetName"] = street_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _building_no_confirmation_code = d.pop("BuildingNoConfirmationCode", UNSET)
        building_no_confirmation_code: ChiStreetBuildingNoConfirmationCode | Unset
        if isinstance(_building_no_confirmation_code, Unset):
            building_no_confirmation_code = UNSET
        else:
            building_no_confirmation_code = (
                check_chi_street_building_no_confirmation_code(
                    _building_no_confirmation_code
                )
            )

        building_no_from = d.pop("BuildingNoFrom", UNSET)

        _building_no_odd_even_indicator = d.pop("BuildingNoOddEvenIndicator", UNSET)
        building_no_odd_even_indicator: ChiStreetBuildingNoOddEvenIndicator | Unset
        if isinstance(_building_no_odd_even_indicator, Unset):
            building_no_odd_even_indicator = UNSET
        else:
            building_no_odd_even_indicator = (
                check_chi_street_building_no_odd_even_indicator(
                    _building_no_odd_even_indicator
                )
            )

        building_no_to = d.pop("BuildingNoTo", UNSET)

        _building_no_unofficial_indicator = d.pop(
            "BuildingNoUnofficialIndicator", UNSET
        )
        building_no_unofficial_indicator: ChiStreetBuildingNoUnofficialIndicator | Unset
        if isinstance(_building_no_unofficial_indicator, Unset):
            building_no_unofficial_indicator = UNSET
        else:
            building_no_unofficial_indicator = (
                check_chi_street_building_no_unofficial_indicator(
                    _building_no_unofficial_indicator
                )
            )

        location_name = d.pop("LocationName", UNSET)

        street_name = d.pop("StreetName", UNSET)

        chi_street = cls(
            building_no_confirmation_code=building_no_confirmation_code,
            building_no_from=building_no_from,
            building_no_odd_even_indicator=building_no_odd_even_indicator,
            building_no_to=building_no_to,
            building_no_unofficial_indicator=building_no_unofficial_indicator,
            location_name=location_name,
            street_name=street_name,
        )

        chi_street.additional_properties = d
        return chi_street

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
