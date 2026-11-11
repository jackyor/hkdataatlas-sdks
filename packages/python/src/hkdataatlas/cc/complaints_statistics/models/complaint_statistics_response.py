from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.complaint_year import ComplaintYear


T = TypeVar("T", bound="ComplaintStatisticsResponse")


@_attrs_define
class ComplaintStatisticsResponse:
    """Response object containing complaint statistics. The example demonstrates the `complaints` property; the source does
    not specify requiredness or a closed set of properties.

        Attributes:
            complaints (list[ComplaintYear] | Unset): Complaint statistics grouped by year.
    """

    complaints: list[ComplaintYear] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        complaints: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.complaints, Unset):
            complaints = []
            for complaints_item_data in self.complaints:
                complaints_item = complaints_item_data.to_dict()
                complaints.append(complaints_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if complaints is not UNSET:
            field_dict["complaints"] = complaints

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.complaint_year import ComplaintYear

        d = dict(src_dict)
        _complaints = d.pop("complaints", UNSET)
        complaints: list[ComplaintYear] | Unset = UNSET
        if _complaints is not UNSET:
            complaints = []
            for complaints_item_data in _complaints:
                complaints_item = ComplaintYear.from_dict(complaints_item_data)

                complaints.append(complaints_item)

        complaint_statistics_response = cls(
            complaints=complaints,
        )

        complaint_statistics_response.additional_properties = d
        return complaint_statistics_response

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
