from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.carpark_info import CarparkInfo
    from ..models.carpark_vacancy import CarparkVacancy


T = TypeVar("T", bound="GetCarparkInfoVacancyResponse200")


@_attrs_define
class GetCarparkInfoVacancyResponse200:
    """
    Attributes:
        results (list[CarparkInfo | CarparkVacancy] | Unset):
    """

    results: list[CarparkInfo | CarparkVacancy] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.carpark_info import CarparkInfo

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item: dict[str, Any]
                if isinstance(results_item_data, CarparkInfo):
                    results_item = results_item_data.to_dict()
                else:
                    results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.carpark_info import CarparkInfo
        from ..models.carpark_vacancy import CarparkVacancy

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: list[CarparkInfo | CarparkVacancy] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:

                def _parse_results_item(data: object) -> CarparkInfo | CarparkVacancy:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        results_item_type_0 = CarparkInfo.from_dict(data)

                        return results_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    results_item_type_1 = CarparkVacancy.from_dict(data)

                    return results_item_type_1

                results_item = _parse_results_item(results_item_data)

                results.append(results_item)

        get_carpark_info_vacancy_response_200 = cls(
            results=results,
        )

        get_carpark_info_vacancy_response_200.additional_properties = d
        return get_carpark_info_vacancy_response_200

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
