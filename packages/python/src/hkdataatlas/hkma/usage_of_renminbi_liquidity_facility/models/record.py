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
        end_of_date (datetime.date | Unset):
        intraday_repo_at_0900 (float | Unset):
        overnight_repo_at_0900 (float | Unset):
        plp_fac_at_0900 (float | Unset):
        intraday_repo_at_1100 (float | Unset):
        overnight_repo_at_1100 (float | Unset):
        plp_fac_at_1100 (float | Unset):
        intraday_repo_at_1400 (float | Unset):
        overnight_repo_at_1400 (float | Unset):
        plp_fac_at_1400 (float | Unset):
        intraday_repo_at_1600 (float | Unset):
        overnight_repo_at_1600 (float | Unset):
        plp_fac_at_1600 (float | Unset):
    """

    end_of_date: datetime.date | Unset = UNSET
    intraday_repo_at_0900: float | Unset = UNSET
    overnight_repo_at_0900: float | Unset = UNSET
    plp_fac_at_0900: float | Unset = UNSET
    intraday_repo_at_1100: float | Unset = UNSET
    overnight_repo_at_1100: float | Unset = UNSET
    plp_fac_at_1100: float | Unset = UNSET
    intraday_repo_at_1400: float | Unset = UNSET
    overnight_repo_at_1400: float | Unset = UNSET
    plp_fac_at_1400: float | Unset = UNSET
    intraday_repo_at_1600: float | Unset = UNSET
    overnight_repo_at_1600: float | Unset = UNSET
    plp_fac_at_1600: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_date: str | Unset = UNSET
        if not isinstance(self.end_of_date, Unset):
            end_of_date = self.end_of_date.isoformat()

        intraday_repo_at_0900 = self.intraday_repo_at_0900

        overnight_repo_at_0900 = self.overnight_repo_at_0900

        plp_fac_at_0900 = self.plp_fac_at_0900

        intraday_repo_at_1100 = self.intraday_repo_at_1100

        overnight_repo_at_1100 = self.overnight_repo_at_1100

        plp_fac_at_1100 = self.plp_fac_at_1100

        intraday_repo_at_1400 = self.intraday_repo_at_1400

        overnight_repo_at_1400 = self.overnight_repo_at_1400

        plp_fac_at_1400 = self.plp_fac_at_1400

        intraday_repo_at_1600 = self.intraday_repo_at_1600

        overnight_repo_at_1600 = self.overnight_repo_at_1600

        plp_fac_at_1600 = self.plp_fac_at_1600

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_date is not UNSET:
            field_dict["end_of_date"] = end_of_date
        if intraday_repo_at_0900 is not UNSET:
            field_dict["intraday_repo_at_0900"] = intraday_repo_at_0900
        if overnight_repo_at_0900 is not UNSET:
            field_dict["overnight_repo_at_0900"] = overnight_repo_at_0900
        if plp_fac_at_0900 is not UNSET:
            field_dict["plp_fac_at_0900"] = plp_fac_at_0900
        if intraday_repo_at_1100 is not UNSET:
            field_dict["intraday_repo_at_1100"] = intraday_repo_at_1100
        if overnight_repo_at_1100 is not UNSET:
            field_dict["overnight_repo_at_1100"] = overnight_repo_at_1100
        if plp_fac_at_1100 is not UNSET:
            field_dict["plp_fac_at_1100"] = plp_fac_at_1100
        if intraday_repo_at_1400 is not UNSET:
            field_dict["intraday_repo_at_1400"] = intraday_repo_at_1400
        if overnight_repo_at_1400 is not UNSET:
            field_dict["overnight_repo_at_1400"] = overnight_repo_at_1400
        if plp_fac_at_1400 is not UNSET:
            field_dict["plp_fac_at_1400"] = plp_fac_at_1400
        if intraday_repo_at_1600 is not UNSET:
            field_dict["intraday_repo_at_1600"] = intraday_repo_at_1600
        if overnight_repo_at_1600 is not UNSET:
            field_dict["overnight_repo_at_1600"] = overnight_repo_at_1600
        if plp_fac_at_1600 is not UNSET:
            field_dict["plp_fac_at_1600"] = plp_fac_at_1600

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_date = d.pop("end_of_date", UNSET)
        end_of_date: datetime.date | Unset
        if isinstance(_end_of_date, Unset):
            end_of_date = UNSET
        else:
            end_of_date = datetime.date.fromisoformat(_end_of_date)

        intraday_repo_at_0900 = d.pop("intraday_repo_at_0900", UNSET)

        overnight_repo_at_0900 = d.pop("overnight_repo_at_0900", UNSET)

        plp_fac_at_0900 = d.pop("plp_fac_at_0900", UNSET)

        intraday_repo_at_1100 = d.pop("intraday_repo_at_1100", UNSET)

        overnight_repo_at_1100 = d.pop("overnight_repo_at_1100", UNSET)

        plp_fac_at_1100 = d.pop("plp_fac_at_1100", UNSET)

        intraday_repo_at_1400 = d.pop("intraday_repo_at_1400", UNSET)

        overnight_repo_at_1400 = d.pop("overnight_repo_at_1400", UNSET)

        plp_fac_at_1400 = d.pop("plp_fac_at_1400", UNSET)

        intraday_repo_at_1600 = d.pop("intraday_repo_at_1600", UNSET)

        overnight_repo_at_1600 = d.pop("overnight_repo_at_1600", UNSET)

        plp_fac_at_1600 = d.pop("plp_fac_at_1600", UNSET)

        record = cls(
            end_of_date=end_of_date,
            intraday_repo_at_0900=intraday_repo_at_0900,
            overnight_repo_at_0900=overnight_repo_at_0900,
            plp_fac_at_0900=plp_fac_at_0900,
            intraday_repo_at_1100=intraday_repo_at_1100,
            overnight_repo_at_1100=overnight_repo_at_1100,
            plp_fac_at_1100=plp_fac_at_1100,
            intraday_repo_at_1400=intraday_repo_at_1400,
            overnight_repo_at_1400=overnight_repo_at_1400,
            plp_fac_at_1400=plp_fac_at_1400,
            intraday_repo_at_1600=intraday_repo_at_1600,
            overnight_repo_at_1600=overnight_repo_at_1600,
            plp_fac_at_1600=plp_fac_at_1600,
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
