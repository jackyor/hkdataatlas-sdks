from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.major_speech import MajorSpeech


T = TypeVar("T", bound="SearchMajorSpeechesResponse200")


@_attrs_define
class SearchMajorSpeechesResponse200:
    """Object/results envelope observed in one source-backed saved live response. Additional fields remain allowed; count
    fields and universal envelope requiredness are not specified by the publisher dictionary.

        Attributes:
            results (list[MajorSpeech] | Unset): Observed results array. Its record definition comes from the documented API
                field column; this captured historical date window returned an empty array, so no nonempty item shape was
                exercised.
            returned_count (Any | Unset): Observed envelope key in one saved dated search response (value 0); the publisher
                dictionary does not specify its universal type or requiredness.
            total_count (Any | Unset): Observed envelope key in one saved dated search response (value 0); the publisher
                dictionary does not specify its universal type or requiredness.
    """

    results: list[MajorSpeech] | Unset = UNSET
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
        from ..models.major_speech import MajorSpeech

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[MajorSpeech] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = MajorSpeech.from_dict(results_item_data)

                results.append(results_item)

        returned_count = d.pop("returned-count", UNSET)

        total_count = d.pop("total-count", UNSET)

        search_major_speeches_response_200 = cls(
            results=results,
            returned_count=returned_count,
            total_count=total_count,
        )

        search_major_speeches_response_200.additional_properties = d
        return search_major_speeches_response_200

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
