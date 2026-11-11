from __future__ import annotations

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
        end_of_quarter (str | Unset): Reportingperiod for end of quarter. Publisher OpenAPIlabels a full date, but the
            retained officialresponse returns YYYY-MM (for example2026-06). A plain string preserves both monthlyperiods and
            full dates without fabricating a day or adding an undocumented lexicalpattern.
        com_eqt_t1cap_ratio (float | Unset):
        t1cap_ratio (float | Unset):
        total_cap_ratio (float | Unset):
        leverage_ratio (float | Unset):
    """

    end_of_quarter: str | Unset = UNSET
    com_eqt_t1cap_ratio: float | Unset = UNSET
    t1cap_ratio: float | Unset = UNSET
    total_cap_ratio: float | Unset = UNSET
    leverage_ratio: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_quarter = self.end_of_quarter

        com_eqt_t1cap_ratio = self.com_eqt_t1cap_ratio

        t1cap_ratio = self.t1cap_ratio

        total_cap_ratio = self.total_cap_ratio

        leverage_ratio = self.leverage_ratio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_quarter is not UNSET:
            field_dict["end_of_quarter"] = end_of_quarter
        if com_eqt_t1cap_ratio is not UNSET:
            field_dict["com_eqt_t1cap_ratio"] = com_eqt_t1cap_ratio
        if t1cap_ratio is not UNSET:
            field_dict["t1cap_ratio"] = t1cap_ratio
        if total_cap_ratio is not UNSET:
            field_dict["total_cap_ratio"] = total_cap_ratio
        if leverage_ratio is not UNSET:
            field_dict["leverage_ratio"] = leverage_ratio

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        end_of_quarter = d.pop("end_of_quarter", UNSET)

        com_eqt_t1cap_ratio = d.pop("com_eqt_t1cap_ratio", UNSET)

        t1cap_ratio = d.pop("t1cap_ratio", UNSET)

        total_cap_ratio = d.pop("total_cap_ratio", UNSET)

        leverage_ratio = d.pop("leverage_ratio", UNSET)

        record = cls(
            end_of_quarter=end_of_quarter,
            com_eqt_t1cap_ratio=com_eqt_t1cap_ratio,
            t1cap_ratio=t1cap_ratio,
            total_cap_ratio=total_cap_ratio,
            leverage_ratio=leverage_ratio,
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
