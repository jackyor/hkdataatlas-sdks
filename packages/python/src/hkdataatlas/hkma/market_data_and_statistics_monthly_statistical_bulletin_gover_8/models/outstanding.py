from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Outstanding")


@_attrs_define
class Outstanding:
    """
    Attributes:
        end_of_day (datetime.date | Unset):
        ind_pricing_10gb2001 (float | Unset):
        ind_pricing_05gb2002 (float | Unset):
        ind_pricing_05gb2011 (float | Unset):
        ind_pricing_10gb2108 (float | Unset):
        ind_pricing_05gb2205 (float | Unset):
        ind_pricing_10gb2301 (float | Unset):
        ind_pricing_10gb2408 (float | Unset):
        ind_pricing_10gb2601 (float | Unset):
        ind_pricing_10gb2706 (float | Unset):
        ind_pricing_10gb2901 (float | Unset):
        ind_pricing_15gb3007 (float | Unset):
        ind_pricing_15gb3203 (float | Unset):
        ind_pricing_15gb3403 (float | Unset):
        closing_ref_rate_10gb2001 (float | Unset):
        closing_ref_rate_05gb2002 (float | Unset):
        closing_ref_rate_05gb2011 (float | Unset):
        closing_ref_rate_10gb2108 (float | Unset):
        closing_ref_rate_05gb2205 (float | Unset):
        closing_ref_rate_10gb2301 (float | Unset):
        closing_ref_rate_10gb2408 (float | Unset):
        closing_ref_rate_10gb2601 (float | Unset):
        closing_ref_rate_10gb2706 (float | Unset):
        closing_ref_rate_10gb2901 (float | Unset):
        closing_ref_rate_15gb3007 (float | Unset):
        closing_ref_rate_15gb3203 (float | Unset):
        closing_ref_rate_15gb3403 (float | Unset):
    """

    end_of_day: datetime.date | Unset = UNSET
    ind_pricing_10gb2001: float | Unset = UNSET
    ind_pricing_05gb2002: float | Unset = UNSET
    ind_pricing_05gb2011: float | Unset = UNSET
    ind_pricing_10gb2108: float | Unset = UNSET
    ind_pricing_05gb2205: float | Unset = UNSET
    ind_pricing_10gb2301: float | Unset = UNSET
    ind_pricing_10gb2408: float | Unset = UNSET
    ind_pricing_10gb2601: float | Unset = UNSET
    ind_pricing_10gb2706: float | Unset = UNSET
    ind_pricing_10gb2901: float | Unset = UNSET
    ind_pricing_15gb3007: float | Unset = UNSET
    ind_pricing_15gb3203: float | Unset = UNSET
    ind_pricing_15gb3403: float | Unset = UNSET
    closing_ref_rate_10gb2001: float | Unset = UNSET
    closing_ref_rate_05gb2002: float | Unset = UNSET
    closing_ref_rate_05gb2011: float | Unset = UNSET
    closing_ref_rate_10gb2108: float | Unset = UNSET
    closing_ref_rate_05gb2205: float | Unset = UNSET
    closing_ref_rate_10gb2301: float | Unset = UNSET
    closing_ref_rate_10gb2408: float | Unset = UNSET
    closing_ref_rate_10gb2601: float | Unset = UNSET
    closing_ref_rate_10gb2706: float | Unset = UNSET
    closing_ref_rate_10gb2901: float | Unset = UNSET
    closing_ref_rate_15gb3007: float | Unset = UNSET
    closing_ref_rate_15gb3203: float | Unset = UNSET
    closing_ref_rate_15gb3403: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_day: str | Unset = UNSET
        if not isinstance(self.end_of_day, Unset):
            end_of_day = self.end_of_day.isoformat()

        ind_pricing_10gb2001 = self.ind_pricing_10gb2001

        ind_pricing_05gb2002 = self.ind_pricing_05gb2002

        ind_pricing_05gb2011 = self.ind_pricing_05gb2011

        ind_pricing_10gb2108 = self.ind_pricing_10gb2108

        ind_pricing_05gb2205 = self.ind_pricing_05gb2205

        ind_pricing_10gb2301 = self.ind_pricing_10gb2301

        ind_pricing_10gb2408 = self.ind_pricing_10gb2408

        ind_pricing_10gb2601 = self.ind_pricing_10gb2601

        ind_pricing_10gb2706 = self.ind_pricing_10gb2706

        ind_pricing_10gb2901 = self.ind_pricing_10gb2901

        ind_pricing_15gb3007 = self.ind_pricing_15gb3007

        ind_pricing_15gb3203 = self.ind_pricing_15gb3203

        ind_pricing_15gb3403 = self.ind_pricing_15gb3403

        closing_ref_rate_10gb2001 = self.closing_ref_rate_10gb2001

        closing_ref_rate_05gb2002 = self.closing_ref_rate_05gb2002

        closing_ref_rate_05gb2011 = self.closing_ref_rate_05gb2011

        closing_ref_rate_10gb2108 = self.closing_ref_rate_10gb2108

        closing_ref_rate_05gb2205 = self.closing_ref_rate_05gb2205

        closing_ref_rate_10gb2301 = self.closing_ref_rate_10gb2301

        closing_ref_rate_10gb2408 = self.closing_ref_rate_10gb2408

        closing_ref_rate_10gb2601 = self.closing_ref_rate_10gb2601

        closing_ref_rate_10gb2706 = self.closing_ref_rate_10gb2706

        closing_ref_rate_10gb2901 = self.closing_ref_rate_10gb2901

        closing_ref_rate_15gb3007 = self.closing_ref_rate_15gb3007

        closing_ref_rate_15gb3203 = self.closing_ref_rate_15gb3203

        closing_ref_rate_15gb3403 = self.closing_ref_rate_15gb3403

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_day is not UNSET:
            field_dict["end_of_day"] = end_of_day
        if ind_pricing_10gb2001 is not UNSET:
            field_dict["ind_pricing_10gb2001"] = ind_pricing_10gb2001
        if ind_pricing_05gb2002 is not UNSET:
            field_dict["ind_pricing_05gb2002"] = ind_pricing_05gb2002
        if ind_pricing_05gb2011 is not UNSET:
            field_dict["ind_pricing_05gb2011"] = ind_pricing_05gb2011
        if ind_pricing_10gb2108 is not UNSET:
            field_dict["ind_pricing_10gb2108"] = ind_pricing_10gb2108
        if ind_pricing_05gb2205 is not UNSET:
            field_dict["ind_pricing_05gb2205"] = ind_pricing_05gb2205
        if ind_pricing_10gb2301 is not UNSET:
            field_dict["ind_pricing_10gb2301"] = ind_pricing_10gb2301
        if ind_pricing_10gb2408 is not UNSET:
            field_dict["ind_pricing_10gb2408"] = ind_pricing_10gb2408
        if ind_pricing_10gb2601 is not UNSET:
            field_dict["ind_pricing_10gb2601"] = ind_pricing_10gb2601
        if ind_pricing_10gb2706 is not UNSET:
            field_dict["ind_pricing_10gb2706"] = ind_pricing_10gb2706
        if ind_pricing_10gb2901 is not UNSET:
            field_dict["ind_pricing_10gb2901"] = ind_pricing_10gb2901
        if ind_pricing_15gb3007 is not UNSET:
            field_dict["ind_pricing_15gb3007"] = ind_pricing_15gb3007
        if ind_pricing_15gb3203 is not UNSET:
            field_dict["ind_pricing_15gb3203"] = ind_pricing_15gb3203
        if ind_pricing_15gb3403 is not UNSET:
            field_dict["ind_pricing_15gb3403"] = ind_pricing_15gb3403
        if closing_ref_rate_10gb2001 is not UNSET:
            field_dict["closing_ref_rate_10gb2001"] = closing_ref_rate_10gb2001
        if closing_ref_rate_05gb2002 is not UNSET:
            field_dict["closing_ref_rate_05gb2002"] = closing_ref_rate_05gb2002
        if closing_ref_rate_05gb2011 is not UNSET:
            field_dict["closing_ref_rate_05gb2011"] = closing_ref_rate_05gb2011
        if closing_ref_rate_10gb2108 is not UNSET:
            field_dict["closing_ref_rate_10gb2108"] = closing_ref_rate_10gb2108
        if closing_ref_rate_05gb2205 is not UNSET:
            field_dict["closing_ref_rate_05gb2205"] = closing_ref_rate_05gb2205
        if closing_ref_rate_10gb2301 is not UNSET:
            field_dict["closing_ref_rate_10gb2301"] = closing_ref_rate_10gb2301
        if closing_ref_rate_10gb2408 is not UNSET:
            field_dict["closing_ref_rate_10gb2408"] = closing_ref_rate_10gb2408
        if closing_ref_rate_10gb2601 is not UNSET:
            field_dict["closing_ref_rate_10gb2601"] = closing_ref_rate_10gb2601
        if closing_ref_rate_10gb2706 is not UNSET:
            field_dict["closing_ref_rate_10gb2706"] = closing_ref_rate_10gb2706
        if closing_ref_rate_10gb2901 is not UNSET:
            field_dict["closing_ref_rate_10gb2901"] = closing_ref_rate_10gb2901
        if closing_ref_rate_15gb3007 is not UNSET:
            field_dict["closing_ref_rate_15gb3007"] = closing_ref_rate_15gb3007
        if closing_ref_rate_15gb3203 is not UNSET:
            field_dict["closing_ref_rate_15gb3203"] = closing_ref_rate_15gb3203
        if closing_ref_rate_15gb3403 is not UNSET:
            field_dict["closing_ref_rate_15gb3403"] = closing_ref_rate_15gb3403

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_day = d.pop("end_of_day", UNSET)
        end_of_day: datetime.date | Unset
        if isinstance(_end_of_day, Unset):
            end_of_day = UNSET
        else:
            end_of_day = datetime.date.fromisoformat(_end_of_day)

        ind_pricing_10gb2001 = d.pop("ind_pricing_10gb2001", UNSET)

        ind_pricing_05gb2002 = d.pop("ind_pricing_05gb2002", UNSET)

        ind_pricing_05gb2011 = d.pop("ind_pricing_05gb2011", UNSET)

        ind_pricing_10gb2108 = d.pop("ind_pricing_10gb2108", UNSET)

        ind_pricing_05gb2205 = d.pop("ind_pricing_05gb2205", UNSET)

        ind_pricing_10gb2301 = d.pop("ind_pricing_10gb2301", UNSET)

        ind_pricing_10gb2408 = d.pop("ind_pricing_10gb2408", UNSET)

        ind_pricing_10gb2601 = d.pop("ind_pricing_10gb2601", UNSET)

        ind_pricing_10gb2706 = d.pop("ind_pricing_10gb2706", UNSET)

        ind_pricing_10gb2901 = d.pop("ind_pricing_10gb2901", UNSET)

        ind_pricing_15gb3007 = d.pop("ind_pricing_15gb3007", UNSET)

        ind_pricing_15gb3203 = d.pop("ind_pricing_15gb3203", UNSET)

        ind_pricing_15gb3403 = d.pop("ind_pricing_15gb3403", UNSET)

        closing_ref_rate_10gb2001 = d.pop("closing_ref_rate_10gb2001", UNSET)

        closing_ref_rate_05gb2002 = d.pop("closing_ref_rate_05gb2002", UNSET)

        closing_ref_rate_05gb2011 = d.pop("closing_ref_rate_05gb2011", UNSET)

        closing_ref_rate_10gb2108 = d.pop("closing_ref_rate_10gb2108", UNSET)

        closing_ref_rate_05gb2205 = d.pop("closing_ref_rate_05gb2205", UNSET)

        closing_ref_rate_10gb2301 = d.pop("closing_ref_rate_10gb2301", UNSET)

        closing_ref_rate_10gb2408 = d.pop("closing_ref_rate_10gb2408", UNSET)

        closing_ref_rate_10gb2601 = d.pop("closing_ref_rate_10gb2601", UNSET)

        closing_ref_rate_10gb2706 = d.pop("closing_ref_rate_10gb2706", UNSET)

        closing_ref_rate_10gb2901 = d.pop("closing_ref_rate_10gb2901", UNSET)

        closing_ref_rate_15gb3007 = d.pop("closing_ref_rate_15gb3007", UNSET)

        closing_ref_rate_15gb3203 = d.pop("closing_ref_rate_15gb3203", UNSET)

        closing_ref_rate_15gb3403 = d.pop("closing_ref_rate_15gb3403", UNSET)

        outstanding = cls(
            end_of_day=end_of_day,
            ind_pricing_10gb2001=ind_pricing_10gb2001,
            ind_pricing_05gb2002=ind_pricing_05gb2002,
            ind_pricing_05gb2011=ind_pricing_05gb2011,
            ind_pricing_10gb2108=ind_pricing_10gb2108,
            ind_pricing_05gb2205=ind_pricing_05gb2205,
            ind_pricing_10gb2301=ind_pricing_10gb2301,
            ind_pricing_10gb2408=ind_pricing_10gb2408,
            ind_pricing_10gb2601=ind_pricing_10gb2601,
            ind_pricing_10gb2706=ind_pricing_10gb2706,
            ind_pricing_10gb2901=ind_pricing_10gb2901,
            ind_pricing_15gb3007=ind_pricing_15gb3007,
            ind_pricing_15gb3203=ind_pricing_15gb3203,
            ind_pricing_15gb3403=ind_pricing_15gb3403,
            closing_ref_rate_10gb2001=closing_ref_rate_10gb2001,
            closing_ref_rate_05gb2002=closing_ref_rate_05gb2002,
            closing_ref_rate_05gb2011=closing_ref_rate_05gb2011,
            closing_ref_rate_10gb2108=closing_ref_rate_10gb2108,
            closing_ref_rate_05gb2205=closing_ref_rate_05gb2205,
            closing_ref_rate_10gb2301=closing_ref_rate_10gb2301,
            closing_ref_rate_10gb2408=closing_ref_rate_10gb2408,
            closing_ref_rate_10gb2601=closing_ref_rate_10gb2601,
            closing_ref_rate_10gb2706=closing_ref_rate_10gb2706,
            closing_ref_rate_10gb2901=closing_ref_rate_10gb2901,
            closing_ref_rate_15gb3007=closing_ref_rate_15gb3007,
            closing_ref_rate_15gb3203=closing_ref_rate_15gb3203,
            closing_ref_rate_15gb3403=closing_ref_rate_15gb3403,
        )

        outstanding.additional_properties = d
        return outstanding

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
