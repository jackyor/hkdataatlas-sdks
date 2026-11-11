from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.warning_summary_entry import WarningSummaryEntry


T = TypeVar("T", bound="WeatherWarningSummary")


@_attrs_define
class WeatherWarningSummary:
    """Weather Warning Summary (warnsum). Warning properties may be missing when null or unavailable.

    Attributes:
        wcold (WarningSummaryEntry | Unset):
        wfire (WarningSummaryEntry | Unset):
        wfntsa (WarningSummaryEntry | Unset):
        wfrost (WarningSummaryEntry | Unset):
        whot (WarningSummaryEntry | Unset):
        wl (WarningSummaryEntry | Unset):
        wmsgnl (WarningSummaryEntry | Unset):
        wrain (WarningSummaryEntry | Unset):
        wtcsgnl (WarningSummaryEntry | Unset):
        wtmw (WarningSummaryEntry | Unset):
        wts (WarningSummaryEntry | Unset):
    """

    wcold: WarningSummaryEntry | Unset = UNSET
    wfire: WarningSummaryEntry | Unset = UNSET
    wfntsa: WarningSummaryEntry | Unset = UNSET
    wfrost: WarningSummaryEntry | Unset = UNSET
    whot: WarningSummaryEntry | Unset = UNSET
    wl: WarningSummaryEntry | Unset = UNSET
    wmsgnl: WarningSummaryEntry | Unset = UNSET
    wrain: WarningSummaryEntry | Unset = UNSET
    wtcsgnl: WarningSummaryEntry | Unset = UNSET
    wtmw: WarningSummaryEntry | Unset = UNSET
    wts: WarningSummaryEntry | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wcold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wcold, Unset):
            wcold = self.wcold.to_dict()

        wfire: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wfire, Unset):
            wfire = self.wfire.to_dict()

        wfntsa: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wfntsa, Unset):
            wfntsa = self.wfntsa.to_dict()

        wfrost: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wfrost, Unset):
            wfrost = self.wfrost.to_dict()

        whot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.whot, Unset):
            whot = self.whot.to_dict()

        wl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wl, Unset):
            wl = self.wl.to_dict()

        wmsgnl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wmsgnl, Unset):
            wmsgnl = self.wmsgnl.to_dict()

        wrain: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wrain, Unset):
            wrain = self.wrain.to_dict()

        wtcsgnl: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wtcsgnl, Unset):
            wtcsgnl = self.wtcsgnl.to_dict()

        wtmw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wtmw, Unset):
            wtmw = self.wtmw.to_dict()

        wts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wts, Unset):
            wts = self.wts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wcold is not UNSET:
            field_dict["WCOLD"] = wcold
        if wfire is not UNSET:
            field_dict["WFIRE"] = wfire
        if wfntsa is not UNSET:
            field_dict["WFNTSA"] = wfntsa
        if wfrost is not UNSET:
            field_dict["WFROST"] = wfrost
        if whot is not UNSET:
            field_dict["WHOT"] = whot
        if wl is not UNSET:
            field_dict["WL"] = wl
        if wmsgnl is not UNSET:
            field_dict["WMSGNL"] = wmsgnl
        if wrain is not UNSET:
            field_dict["WRAIN"] = wrain
        if wtcsgnl is not UNSET:
            field_dict["WTCSGNL"] = wtcsgnl
        if wtmw is not UNSET:
            field_dict["WTMW"] = wtmw
        if wts is not UNSET:
            field_dict["WTS"] = wts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.warning_summary_entry import WarningSummaryEntry

        d = dict(src_dict)
        _wcold = d.pop("WCOLD", UNSET)
        wcold: WarningSummaryEntry | Unset
        if isinstance(_wcold, Unset):
            wcold = UNSET
        else:
            wcold = WarningSummaryEntry.from_dict(_wcold)

        _wfire = d.pop("WFIRE", UNSET)
        wfire: WarningSummaryEntry | Unset
        if isinstance(_wfire, Unset):
            wfire = UNSET
        else:
            wfire = WarningSummaryEntry.from_dict(_wfire)

        _wfntsa = d.pop("WFNTSA", UNSET)
        wfntsa: WarningSummaryEntry | Unset
        if isinstance(_wfntsa, Unset):
            wfntsa = UNSET
        else:
            wfntsa = WarningSummaryEntry.from_dict(_wfntsa)

        _wfrost = d.pop("WFROST", UNSET)
        wfrost: WarningSummaryEntry | Unset
        if isinstance(_wfrost, Unset):
            wfrost = UNSET
        else:
            wfrost = WarningSummaryEntry.from_dict(_wfrost)

        _whot = d.pop("WHOT", UNSET)
        whot: WarningSummaryEntry | Unset
        if isinstance(_whot, Unset):
            whot = UNSET
        else:
            whot = WarningSummaryEntry.from_dict(_whot)

        _wl = d.pop("WL", UNSET)
        wl: WarningSummaryEntry | Unset
        if isinstance(_wl, Unset):
            wl = UNSET
        else:
            wl = WarningSummaryEntry.from_dict(_wl)

        _wmsgnl = d.pop("WMSGNL", UNSET)
        wmsgnl: WarningSummaryEntry | Unset
        if isinstance(_wmsgnl, Unset):
            wmsgnl = UNSET
        else:
            wmsgnl = WarningSummaryEntry.from_dict(_wmsgnl)

        _wrain = d.pop("WRAIN", UNSET)
        wrain: WarningSummaryEntry | Unset
        if isinstance(_wrain, Unset):
            wrain = UNSET
        else:
            wrain = WarningSummaryEntry.from_dict(_wrain)

        _wtcsgnl = d.pop("WTCSGNL", UNSET)
        wtcsgnl: WarningSummaryEntry | Unset
        if isinstance(_wtcsgnl, Unset):
            wtcsgnl = UNSET
        else:
            wtcsgnl = WarningSummaryEntry.from_dict(_wtcsgnl)

        _wtmw = d.pop("WTMW", UNSET)
        wtmw: WarningSummaryEntry | Unset
        if isinstance(_wtmw, Unset):
            wtmw = UNSET
        else:
            wtmw = WarningSummaryEntry.from_dict(_wtmw)

        _wts = d.pop("WTS", UNSET)
        wts: WarningSummaryEntry | Unset
        if isinstance(_wts, Unset):
            wts = UNSET
        else:
            wts = WarningSummaryEntry.from_dict(_wts)

        weather_warning_summary = cls(
            wcold=wcold,
            wfire=wfire,
            wfntsa=wfntsa,
            wfrost=wfrost,
            whot=whot,
            wl=wl,
            wmsgnl=wmsgnl,
            wrain=wrain,
            wtcsgnl=wtcsgnl,
            wtmw=wtmw,
            wts=wts,
        )

        weather_warning_summary.additional_properties = d
        return weather_warning_summary

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
