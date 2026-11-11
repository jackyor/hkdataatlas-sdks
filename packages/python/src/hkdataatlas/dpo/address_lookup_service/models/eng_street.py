from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.eng_street_building_no_confirmation_code import (
    EngStreetBuildingNoConfirmationCode,
    check_eng_street_building_no_confirmation_code,
)
from ..models.eng_street_building_no_odd_even_indicator import (
    EngStreetBuildingNoOddEvenIndicator,
    check_eng_street_building_no_odd_even_indicator,
)
from ..models.eng_street_building_no_unofficial_indicator import (
    EngStreetBuildingNoUnofficialIndicator,
    check_eng_street_building_no_unofficial_indicator,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EngStreet")


@_attrs_define
class EngStreet:
    """Street name and building number information in English.

    Attributes:
        building_no_confirmation_code (EngStreetBuildingNoConfirmationCode | Unset): Building-number confirmation: C =
            confirmed; P = provisional; A = not yet allocated but action to be taken; B = use existing old number but action
            to be taken; X = not applicable. When C or P, BuildingNoFrom must not be null.
        building_no_from (str | Unset): Starting or ending building number, including any non-numeric part, as described
            for English street and village addresses. The observed response includes the string `2`; the dictionary
            specifies a constrained text representation.
        building_no_odd_even_indicator (EngStreetBuildingNoOddEvenIndicator | Unset): O = odd numbers, E = even numbers,
            B = both even and odd numbers within the range.
        building_no_to (str | Unset): Starting or ending building number, including any non-numeric part, as described
            for English street and village addresses. The observed response includes the string `2`; the dictionary
            specifies a constrained text representation.
        building_no_unofficial_indicator (EngStreetBuildingNoUnofficialIndicator | Unset): Unofficial-address indicator:
            1 = unofficial building number or no building number; 2 = unofficial building number and building name.
        location_name (str | Unset): Place or location name in English.
        street_name (str | Unset): Street name in English.
    """

    building_no_confirmation_code: EngStreetBuildingNoConfirmationCode | Unset = UNSET
    building_no_from: str | Unset = UNSET
    building_no_odd_even_indicator: EngStreetBuildingNoOddEvenIndicator | Unset = UNSET
    building_no_to: str | Unset = UNSET
    building_no_unofficial_indicator: EngStreetBuildingNoUnofficialIndicator | Unset = (
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
        building_no_confirmation_code: EngStreetBuildingNoConfirmationCode | Unset
        if isinstance(_building_no_confirmation_code, Unset):
            building_no_confirmation_code = UNSET
        else:
            building_no_confirmation_code = (
                check_eng_street_building_no_confirmation_code(
                    _building_no_confirmation_code
                )
            )

        building_no_from = d.pop("BuildingNoFrom", UNSET)

        _building_no_odd_even_indicator = d.pop("BuildingNoOddEvenIndicator", UNSET)
        building_no_odd_even_indicator: EngStreetBuildingNoOddEvenIndicator | Unset
        if isinstance(_building_no_odd_even_indicator, Unset):
            building_no_odd_even_indicator = UNSET
        else:
            building_no_odd_even_indicator = (
                check_eng_street_building_no_odd_even_indicator(
                    _building_no_odd_even_indicator
                )
            )

        building_no_to = d.pop("BuildingNoTo", UNSET)

        _building_no_unofficial_indicator = d.pop(
            "BuildingNoUnofficialIndicator", UNSET
        )
        building_no_unofficial_indicator: EngStreetBuildingNoUnofficialIndicator | Unset
        if isinstance(_building_no_unofficial_indicator, Unset):
            building_no_unofficial_indicator = UNSET
        else:
            building_no_unofficial_indicator = (
                check_eng_street_building_no_unofficial_indicator(
                    _building_no_unofficial_indicator
                )
            )

        location_name = d.pop("LocationName", UNSET)

        street_name = d.pop("StreetName", UNSET)

        eng_street = cls(
            building_no_confirmation_code=building_no_confirmation_code,
            building_no_from=building_no_from,
            building_no_odd_even_indicator=building_no_odd_even_indicator,
            building_no_to=building_no_to,
            building_no_unofficial_indicator=building_no_unofficial_indicator,
            location_name=location_name,
            street_name=street_name,
        )

        eng_street.additional_properties = d
        return eng_street

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
