from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_record import DataRecord
    from ..models.header import Header


T = TypeVar("T", bound="TableResponse")


@_attrs_define
class TableResponse:
    """
    Attributes:
        header (Header):
        data_set (list[DataRecord] | Unset): Array of observation records.
            Present only on a successful request, with the description of the query being "Query Success".
            It may be omitted or empty on failure.
    """

    header: Header
    data_set: list[DataRecord] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header = self.header.to_dict()

        data_set: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data_set, Unset):
            data_set = []
            for data_set_item_data in self.data_set:
                data_set_item = data_set_item_data.to_dict()
                data_set.append(data_set_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "header": header,
            }
        )
        if data_set is not UNSET:
            field_dict["dataSet"] = data_set

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.data_record import DataRecord
        from ..models.header import Header

        d = dict(src_dict)
        header = Header.from_dict(d.pop("header"))

        _data_set = d.pop("dataSet", UNSET)
        data_set: list[DataRecord] | Unset = UNSET
        if _data_set is not UNSET:
            data_set = []
            for data_set_item_data in _data_set:
                data_set_item = DataRecord.from_dict(data_set_item_data)

                data_set.append(data_set_item)

        table_response = cls(
            header=header,
            data_set=data_set,
        )

        table_response.additional_properties = d
        return table_response

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
