from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CurrentWeatherReportRainfallPlaceItem")


@_attrs_define
class CurrentWeatherReportRainfallPlaceItem:
    """
    Attributes:
        main (bool | Unset): Maintenance flag (TRUE/FALSE).
        max_ (float | str | Unset): Maximum rainfall record.
        min_ (float | str | Unset): Minimum rainfall record.
        place (str | Unset): Location.
    """

    main: bool | Unset = UNSET
    max_: float | str | Unset = UNSET
    min_: float | str | Unset = UNSET
    place: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main = self.main

        max_: float | str | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        min_: float | str | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        place = self.place

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if main is not UNSET:
            field_dict["Main"] = main
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if place is not UNSET:
            field_dict["place"] = place

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        main = d.pop("Main", UNSET)

        def _parse_max_(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_min_(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        place = d.pop("place", UNSET)

        current_weather_report_rainfall_place_item = cls(
            main=main,
            max_=max_,
            min_=min_,
            place=place,
        )

        current_weather_report_rainfall_place_item.additional_properties = d
        return current_weather_report_rainfall_place_item

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
