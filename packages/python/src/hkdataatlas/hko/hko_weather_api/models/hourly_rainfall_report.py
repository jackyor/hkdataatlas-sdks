from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hourly_rainfall_station import HourlyRainfallStation


T = TypeVar("T", bound="HourlyRainfallReport")


@_attrs_define
class HourlyRainfallReport:
    """
    Attributes:
        hourly_rainfall (list[HourlyRainfallStation] | Unset): Rainfall amount during the one-hour period ending at
            observation time.
        obs_time (str | Unset): Timestamp examples use YYYY-MM-DD'T'hh:mm:ssZ notation and include the +08:00 offset.
    """

    hourly_rainfall: list[HourlyRainfallStation] | Unset = UNSET
    obs_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hourly_rainfall: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hourly_rainfall, Unset):
            hourly_rainfall = []
            for hourly_rainfall_item_data in self.hourly_rainfall:
                hourly_rainfall_item = hourly_rainfall_item_data.to_dict()
                hourly_rainfall.append(hourly_rainfall_item)

        obs_time = self.obs_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hourly_rainfall is not UNSET:
            field_dict["hourlyRainfall"] = hourly_rainfall
        if obs_time is not UNSET:
            field_dict["obsTime"] = obs_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hourly_rainfall_station import HourlyRainfallStation

        d = dict(src_dict)
        _hourly_rainfall = d.pop("hourlyRainfall", UNSET)
        hourly_rainfall: list[HourlyRainfallStation] | Unset = UNSET
        if _hourly_rainfall is not UNSET:
            hourly_rainfall = []
            for hourly_rainfall_item_data in _hourly_rainfall:
                hourly_rainfall_item = HourlyRainfallStation.from_dict(
                    hourly_rainfall_item_data
                )

                hourly_rainfall.append(hourly_rainfall_item)

        obs_time = d.pop("obsTime", UNSET)

        hourly_rainfall_report = cls(
            hourly_rainfall=hourly_rainfall,
            obs_time=obs_time,
        )

        hourly_rainfall_report.additional_properties = d
        return hourly_rainfall_report

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
