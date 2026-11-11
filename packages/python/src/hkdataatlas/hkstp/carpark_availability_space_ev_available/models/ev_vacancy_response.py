from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.carpark_vacancy import CarparkVacancy


T = TypeVar("T", bound="EvVacancyResponse")


@_attrs_define
class EvVacancyResponse:
    """Response structure shown in the publisher example; the documentation does not state that this sample is exhaustive.

    Attributes:
        value (list[CarparkVacancy] | Unset): List of objects.
    """

    value: list[CarparkVacancy] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item = value_item_data.to_dict()
                value.append(value_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.carpark_vacancy import CarparkVacancy

        d = dict(src_dict)
        _value = d.pop("value", UNSET)
        value: list[CarparkVacancy] | Unset = UNSET
        if _value is not UNSET:
            value = []
            for value_item_data in _value:
                value_item = CarparkVacancy.from_dict(value_item_data)

                value.append(value_item)

        ev_vacancy_response = cls(
            value=value,
        )

        ev_vacancy_response.additional_properties = d
        return ev_vacancy_response

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
