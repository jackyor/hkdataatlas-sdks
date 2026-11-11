from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity import Activity


T = TypeVar("T", bound="FundraisingResponse")


@_attrs_define
class FundraisingResponse:
    """JSON response field dictionary. The source does not establish complete JSON nesting, property requiredness, or wire
    types for these fields.

        Attributes:
            activities (list[Activity] | Unset): List of activities matching the search parameters.
            current_page (int | str | Unset): The source does not establish wire types; retain the prior integer
                interpretation and exact observed decimal-digit strings without coercion.
            generator (str | Unset): Generator identifier of this JSON/XML.
            total_records_in_current_page (int | str | Unset): The source does not establish wire types; retain the prior
                integer interpretation and exact observed decimal-digit strings without coercion.
            total_records_searched (int | str | Unset): The source does not establish wire types; retain the prior integer
                interpretation and exact observed decimal-digit strings without coercion.
    """

    activities: list[Activity] | Unset = UNSET
    current_page: int | str | Unset = UNSET
    generator: str | Unset = UNSET
    total_records_in_current_page: int | str | Unset = UNSET
    total_records_searched: int | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.activities, Unset):
            activities = []
            for activities_item_data in self.activities:
                activities_item = activities_item_data.to_dict()
                activities.append(activities_item)

        current_page: int | str | Unset
        if isinstance(self.current_page, Unset):
            current_page = UNSET
        else:
            current_page = self.current_page

        generator = self.generator

        total_records_in_current_page: int | str | Unset
        if isinstance(self.total_records_in_current_page, Unset):
            total_records_in_current_page = UNSET
        else:
            total_records_in_current_page = self.total_records_in_current_page

        total_records_searched: int | str | Unset
        if isinstance(self.total_records_searched, Unset):
            total_records_searched = UNSET
        else:
            total_records_searched = self.total_records_searched

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activities is not UNSET:
            field_dict["activities"] = activities
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if generator is not UNSET:
            field_dict["generator"] = generator
        if total_records_in_current_page is not UNSET:
            field_dict["totalRecordsInCurrentPage"] = total_records_in_current_page
        if total_records_searched is not UNSET:
            field_dict["totalRecordsSearched"] = total_records_searched

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.activity import Activity

        d = dict(src_dict)
        _activities = d.pop("activities", UNSET)
        activities: list[Activity] | Unset = UNSET
        if _activities is not UNSET:
            activities = []
            for activities_item_data in _activities:
                activities_item = Activity.from_dict(activities_item_data)

                activities.append(activities_item)

        def _parse_current_page(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        current_page = _parse_current_page(d.pop("currentPage", UNSET))

        generator = d.pop("generator", UNSET)

        def _parse_total_records_in_current_page(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        total_records_in_current_page = _parse_total_records_in_current_page(
            d.pop("totalRecordsInCurrentPage", UNSET)
        )

        def _parse_total_records_searched(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        total_records_searched = _parse_total_records_searched(
            d.pop("totalRecordsSearched", UNSET)
        )

        fundraising_response = cls(
            activities=activities,
            current_page=current_page,
            generator=generator,
            total_records_in_current_page=total_records_in_current_page,
            total_records_searched=total_records_searched,
        )

        fundraising_response.additional_properties = d
        return fundraising_response

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
