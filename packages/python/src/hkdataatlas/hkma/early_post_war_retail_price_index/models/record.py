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
        rpi_qtr (datetime.date | Unset):
        rpi_epwgenrpi_q (float | Unset):
        rpi_epwfood_q (float | Unset):
        rpi_epwrent_q (float | Unset):
        rpi_epwclo_q (float | Unset):
        rpi_epwfuel_q (float | Unset):
        rpi_epwelec_q (float | Unset):
        rpi_epwcln_q (float | Unset):
        rpi_epwedn_q (float | Unset):
        rpi_epwtob_q (float | Unset):
        rpi_epwdm_q (float | Unset):
        rpi_epwfare_q (float | Unset):
        rpi_epwhou_q (float | Unset):
        rpi_epwhair_q (float | Unset):
        rpi_epwnews_q (float | Unset):
        rpi_epwshoer_q (float | Unset):
        rpi_epwrates_q (float | Unset):
    """

    rpi_qtr: datetime.date | Unset = UNSET
    rpi_epwgenrpi_q: float | Unset = UNSET
    rpi_epwfood_q: float | Unset = UNSET
    rpi_epwrent_q: float | Unset = UNSET
    rpi_epwclo_q: float | Unset = UNSET
    rpi_epwfuel_q: float | Unset = UNSET
    rpi_epwelec_q: float | Unset = UNSET
    rpi_epwcln_q: float | Unset = UNSET
    rpi_epwedn_q: float | Unset = UNSET
    rpi_epwtob_q: float | Unset = UNSET
    rpi_epwdm_q: float | Unset = UNSET
    rpi_epwfare_q: float | Unset = UNSET
    rpi_epwhou_q: float | Unset = UNSET
    rpi_epwhair_q: float | Unset = UNSET
    rpi_epwnews_q: float | Unset = UNSET
    rpi_epwshoer_q: float | Unset = UNSET
    rpi_epwrates_q: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rpi_qtr: str | Unset = UNSET
        if not isinstance(self.rpi_qtr, Unset):
            rpi_qtr = self.rpi_qtr.isoformat()

        rpi_epwgenrpi_q = self.rpi_epwgenrpi_q

        rpi_epwfood_q = self.rpi_epwfood_q

        rpi_epwrent_q = self.rpi_epwrent_q

        rpi_epwclo_q = self.rpi_epwclo_q

        rpi_epwfuel_q = self.rpi_epwfuel_q

        rpi_epwelec_q = self.rpi_epwelec_q

        rpi_epwcln_q = self.rpi_epwcln_q

        rpi_epwedn_q = self.rpi_epwedn_q

        rpi_epwtob_q = self.rpi_epwtob_q

        rpi_epwdm_q = self.rpi_epwdm_q

        rpi_epwfare_q = self.rpi_epwfare_q

        rpi_epwhou_q = self.rpi_epwhou_q

        rpi_epwhair_q = self.rpi_epwhair_q

        rpi_epwnews_q = self.rpi_epwnews_q

        rpi_epwshoer_q = self.rpi_epwshoer_q

        rpi_epwrates_q = self.rpi_epwrates_q

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rpi_qtr is not UNSET:
            field_dict["Rpi_qtr"] = rpi_qtr
        if rpi_epwgenrpi_q is not UNSET:
            field_dict["Rpi_epwgenrpi_q"] = rpi_epwgenrpi_q
        if rpi_epwfood_q is not UNSET:
            field_dict["Rpi_epwfood_q"] = rpi_epwfood_q
        if rpi_epwrent_q is not UNSET:
            field_dict["Rpi_epwrent_q"] = rpi_epwrent_q
        if rpi_epwclo_q is not UNSET:
            field_dict["Rpi_epwclo_q"] = rpi_epwclo_q
        if rpi_epwfuel_q is not UNSET:
            field_dict["Rpi_epwfuel_q"] = rpi_epwfuel_q
        if rpi_epwelec_q is not UNSET:
            field_dict["Rpi_epwelec_q"] = rpi_epwelec_q
        if rpi_epwcln_q is not UNSET:
            field_dict["Rpi_epwcln_q"] = rpi_epwcln_q
        if rpi_epwedn_q is not UNSET:
            field_dict["Rpi_epwedn_q"] = rpi_epwedn_q
        if rpi_epwtob_q is not UNSET:
            field_dict["Rpi_epwtob_q"] = rpi_epwtob_q
        if rpi_epwdm_q is not UNSET:
            field_dict["Rpi_epwdm_q"] = rpi_epwdm_q
        if rpi_epwfare_q is not UNSET:
            field_dict["Rpi_epwfare_q"] = rpi_epwfare_q
        if rpi_epwhou_q is not UNSET:
            field_dict["Rpi_epwhou_q"] = rpi_epwhou_q
        if rpi_epwhair_q is not UNSET:
            field_dict["Rpi_epwhair_q"] = rpi_epwhair_q
        if rpi_epwnews_q is not UNSET:
            field_dict["Rpi_epwnews_q"] = rpi_epwnews_q
        if rpi_epwshoer_q is not UNSET:
            field_dict["Rpi_epwshoer_q"] = rpi_epwshoer_q
        if rpi_epwrates_q is not UNSET:
            field_dict["Rpi_epwrates_q"] = rpi_epwrates_q

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _rpi_qtr = d.pop("Rpi_qtr", UNSET)
        rpi_qtr: datetime.date | Unset
        if isinstance(_rpi_qtr, Unset):
            rpi_qtr = UNSET
        else:
            rpi_qtr = datetime.date.fromisoformat(_rpi_qtr)

        rpi_epwgenrpi_q = d.pop("Rpi_epwgenrpi_q", UNSET)

        rpi_epwfood_q = d.pop("Rpi_epwfood_q", UNSET)

        rpi_epwrent_q = d.pop("Rpi_epwrent_q", UNSET)

        rpi_epwclo_q = d.pop("Rpi_epwclo_q", UNSET)

        rpi_epwfuel_q = d.pop("Rpi_epwfuel_q", UNSET)

        rpi_epwelec_q = d.pop("Rpi_epwelec_q", UNSET)

        rpi_epwcln_q = d.pop("Rpi_epwcln_q", UNSET)

        rpi_epwedn_q = d.pop("Rpi_epwedn_q", UNSET)

        rpi_epwtob_q = d.pop("Rpi_epwtob_q", UNSET)

        rpi_epwdm_q = d.pop("Rpi_epwdm_q", UNSET)

        rpi_epwfare_q = d.pop("Rpi_epwfare_q", UNSET)

        rpi_epwhou_q = d.pop("Rpi_epwhou_q", UNSET)

        rpi_epwhair_q = d.pop("Rpi_epwhair_q", UNSET)

        rpi_epwnews_q = d.pop("Rpi_epwnews_q", UNSET)

        rpi_epwshoer_q = d.pop("Rpi_epwshoer_q", UNSET)

        rpi_epwrates_q = d.pop("Rpi_epwrates_q", UNSET)

        record = cls(
            rpi_qtr=rpi_qtr,
            rpi_epwgenrpi_q=rpi_epwgenrpi_q,
            rpi_epwfood_q=rpi_epwfood_q,
            rpi_epwrent_q=rpi_epwrent_q,
            rpi_epwclo_q=rpi_epwclo_q,
            rpi_epwfuel_q=rpi_epwfuel_q,
            rpi_epwelec_q=rpi_epwelec_q,
            rpi_epwcln_q=rpi_epwcln_q,
            rpi_epwedn_q=rpi_epwedn_q,
            rpi_epwtob_q=rpi_epwtob_q,
            rpi_epwdm_q=rpi_epwdm_q,
            rpi_epwfare_q=rpi_epwfare_q,
            rpi_epwhou_q=rpi_epwhou_q,
            rpi_epwhair_q=rpi_epwhair_q,
            rpi_epwnews_q=rpi_epwnews_q,
            rpi_epwshoer_q=rpi_epwshoer_q,
            rpi_epwrates_q=rpi_epwrates_q,
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
