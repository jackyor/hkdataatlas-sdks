from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.complaint_category import ComplaintCategory


T = TypeVar("T", bound="ComplaintYear")


@_attrs_define
class ComplaintYear:
    """Statistics for a complaint year. The source data dictionary describes the year and month values as text.

    Attributes:
        categories (list[ComplaintCategory] | Unset): Contains all categories and the complaint amount for each
            category.
        complaints_month (str | Unset): The period of month in the year of the complaint statistic.
        complaints_year (str | Unset): The year of the complaint statistic.
    """

    categories: list[ComplaintCategory] | Unset = UNSET
    complaints_month: str | Unset = UNSET
    complaints_year: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        complaints_month = self.complaints_month

        complaints_year = self.complaints_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if complaints_month is not UNSET:
            field_dict["complaints_month"] = complaints_month
        if complaints_year is not UNSET:
            field_dict["complaints_year"] = complaints_year

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.complaint_category import ComplaintCategory

        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: list[ComplaintCategory] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = ComplaintCategory.from_dict(categories_item_data)

                categories.append(categories_item)

        complaints_month = d.pop("complaints_month", UNSET)

        complaints_year = d.pop("complaints_year", UNSET)

        complaint_year = cls(
            categories=categories,
            complaints_month=complaints_month,
            complaints_year=complaints_year,
        )

        complaint_year.additional_properties = d
        return complaint_year

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
