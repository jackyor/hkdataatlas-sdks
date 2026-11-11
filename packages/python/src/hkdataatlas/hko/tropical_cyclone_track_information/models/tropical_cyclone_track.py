from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulletin_header import BulletinHeader
    from ..models.weather_report import WeatherReport


T = TypeVar("T", bound="TropicalCycloneTrack")


@_attrs_define
class TropicalCycloneTrack:
    """XML root element TropicalCycloneTrack.

    Attributes:
        bulletin_header (BulletinHeader | Unset):
        weather_report (WeatherReport | Unset):
    """

    bulletin_header: BulletinHeader | Unset = UNSET
    weather_report: WeatherReport | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bulletin_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bulletin_header, Unset):
            bulletin_header = self.bulletin_header.to_dict()

        weather_report: dict[str, Any] | Unset = UNSET
        if not isinstance(self.weather_report, Unset):
            weather_report = self.weather_report.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bulletin_header is not UNSET:
            field_dict["BulletinHeader"] = bulletin_header
        if weather_report is not UNSET:
            field_dict["WeatherReport"] = weather_report

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bulletin_header import BulletinHeader
        from ..models.weather_report import WeatherReport

        d = dict(src_dict)
        _bulletin_header = d.pop("BulletinHeader", UNSET)
        bulletin_header: BulletinHeader | Unset
        if isinstance(_bulletin_header, Unset):
            bulletin_header = UNSET
        else:
            bulletin_header = BulletinHeader.from_dict(_bulletin_header)

        _weather_report = d.pop("WeatherReport", UNSET)
        weather_report: WeatherReport | Unset
        if isinstance(_weather_report, Unset):
            weather_report = UNSET
        else:
            weather_report = WeatherReport.from_dict(_weather_report)

        tropical_cyclone_track = cls(
            bulletin_header=bulletin_header,
            weather_report=weather_report,
        )

        tropical_cyclone_track.additional_properties = d
        return tropical_cyclone_track

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
