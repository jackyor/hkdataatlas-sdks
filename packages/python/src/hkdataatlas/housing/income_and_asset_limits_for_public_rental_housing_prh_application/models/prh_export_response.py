from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.prh_export_record import PrhExportRecord


T = TypeVar("T", bound="PrhExportResponse")


@_attrs_define
class PrhExportResponse:
    """Current export uses data wrapper, established by retained response. Publisher PDF example uses records wrapper and
    is not substituted for current export.

        Attributes:
            data (list[PrhExportRecord] | Unset):
    """

    data: list[PrhExportRecord] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.prh_export_record import PrhExportRecord

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[PrhExportRecord] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = PrhExportRecord.from_dict(data_item_data)

                data.append(data_item)

        prh_export_response = cls(
            data=data,
        )

        prh_export_response.additional_properties = d
        return prh_export_response

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
