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
        end_of_quarter (datetime.date | Unset):
        coverage_ratio (float | Unset):
        maintenance_ratio (float | Unset):
        netstable_fundratio (float | Unset):
        core_fundratio (float | Unset):
    """

    end_of_quarter: datetime.date | Unset = UNSET
    coverage_ratio: float | Unset = UNSET
    maintenance_ratio: float | Unset = UNSET
    netstable_fundratio: float | Unset = UNSET
    core_fundratio: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_quarter: str | Unset = UNSET
        if not isinstance(self.end_of_quarter, Unset):
            end_of_quarter = self.end_of_quarter.isoformat()

        coverage_ratio = self.coverage_ratio

        maintenance_ratio = self.maintenance_ratio

        netstable_fundratio = self.netstable_fundratio

        core_fundratio = self.core_fundratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_quarter is not UNSET:
            field_dict["end_of_quarter"] = end_of_quarter
        if coverage_ratio is not UNSET:
            field_dict["coverage_ratio"] = coverage_ratio
        if maintenance_ratio is not UNSET:
            field_dict["maintenance_ratio"] = maintenance_ratio
        if netstable_fundratio is not UNSET:
            field_dict["netstable_fundratio"] = netstable_fundratio
        if core_fundratio is not UNSET:
            field_dict["core_fundratio"] = core_fundratio

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_quarter = d.pop("end_of_quarter", UNSET)
        end_of_quarter: datetime.date | Unset
        if isinstance(_end_of_quarter, Unset):
            end_of_quarter = UNSET
        else:
            end_of_quarter = datetime.date.fromisoformat(_end_of_quarter)

        coverage_ratio = d.pop("coverage_ratio", UNSET)

        maintenance_ratio = d.pop("maintenance_ratio", UNSET)

        netstable_fundratio = d.pop("netstable_fundratio", UNSET)

        core_fundratio = d.pop("core_fundratio", UNSET)

        record = cls(
            end_of_quarter=end_of_quarter,
            coverage_ratio=coverage_ratio,
            maintenance_ratio=maintenance_ratio,
            netstable_fundratio=netstable_fundratio,
            core_fundratio=core_fundratio,
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
