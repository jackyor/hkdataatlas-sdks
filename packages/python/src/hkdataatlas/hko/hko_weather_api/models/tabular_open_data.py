from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TabularOpenData")


@_attrs_define
class TabularOpenData:
    """Generic documented JSON table shape for several climate and weather datasets; fields and values vary by dataset.

    Attributes:
        data (list[list[float | None | str]] | Unset): Rows of tabular data; cell types are not specified.
        fields (list[str] | Unset): Field names.
        legend (list[str] | Unset): Legend values where supplied.
        type_ (list[str] | Unset): Dataset type labels, documented for temperature datasets.
    """

    data: list[list[float | None | str]] | Unset = UNSET
    fields: list[str] | Unset = UNSET
    legend: list[str] | Unset = UNSET
    type_: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[list[float | None | str]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = []
                for data_item_item_data in data_item_data:
                    data_item_item: float | None | str
                    data_item_item = data_item_item_data
                    data_item.append(data_item_item)

                data.append(data_item)

        fields: list[str] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        legend: list[str] | Unset = UNSET
        if not isinstance(self.legend, Unset):
            legend = self.legend

        type_: list[str] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if fields is not UNSET:
            field_dict["fields"] = fields
        if legend is not UNSET:
            field_dict["legend"] = legend
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[list[float | None | str]] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = []
                _data_item = data_item_data
                for data_item_item_data in _data_item:

                    def _parse_data_item_item(data: object) -> float | None | str:
                        if data is None:
                            return data
                        return cast(float | None | str, data)

                    data_item_item = _parse_data_item_item(data_item_item_data)

                    data_item.append(data_item_item)

                data.append(data_item)

        fields = cast(list[str], d.pop("fields", UNSET))

        legend = cast(list[str], d.pop("legend", UNSET))

        type_ = cast(list[str], d.pop("type", UNSET))

        tabular_open_data = cls(
            data=data,
            fields=fields,
            legend=legend,
            type_=type_,
        )

        tabular_open_data.additional_properties = d
        return tabular_open_data

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
