from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.press_release import PressRelease


T = TypeVar("T", bound="SearchPressReleasesResponse200")


@_attrs_define
class SearchPressReleasesResponse200:
    """Object/results envelope observed in one source-backed saved response. Additional properties remain allowed; no
    universal envelope requiredness is inferred.

        Attributes:
            results (list[PressRelease] | Unset): Documented record fields in the observed results array. Saved response
                contains four records; observation is not an exhaustive contract.
            returned_count (Any | Unset): Observed envelope key; universal type and requiredness are not specified by the
                publisher dictionary.
            total_count (Any | Unset): Observed envelope key; universal type and requiredness are not specified by the
                publisher dictionary.
    """

    results: list[PressRelease] | Unset = UNSET
    returned_count: Any | Unset = UNSET
    total_count: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        returned_count = self.returned_count

        total_count = self.total_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if returned_count is not UNSET:
            field_dict["returned-count"] = returned_count
        if total_count is not UNSET:
            field_dict["total-count"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.press_release import PressRelease

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[PressRelease] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = PressRelease.from_dict(results_item_data)

                results.append(results_item)

        returned_count = d.pop("returned-count", UNSET)

        total_count = d.pop("total-count", UNSET)

        search_press_releases_response_200 = cls(
            results=results,
            returned_count=returned_count,
            total_count=total_count,
        )

        search_press_releases_response_200.additional_properties = d
        return search_press_releases_response_200

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
