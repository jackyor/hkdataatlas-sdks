from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_register_ambs_response_200_records_item import (
        GetRegisterAmbsResponse200RecordsItem,
    )
    from ..models.get_register_ambs_response_200_result import (
        GetRegisterAmbsResponse200Result,
    )


T = TypeVar("T", bound="GetRegisterAmbsResponse200")


@_attrs_define
class GetRegisterAmbsResponse200:
    """
    Attributes:
        result (GetRegisterAmbsResponse200Result | Unset):
        records (list[GetRegisterAmbsResponse200RecordsItem] | Unset):
    """

    result: GetRegisterAmbsResponse200Result | Unset = UNSET
    records: list[GetRegisterAmbsResponse200RecordsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.get_register_ambs_response_200_records_item import (
            GetRegisterAmbsResponse200RecordsItem,
        )
        from ..models.get_register_ambs_response_200_result import (
            GetRegisterAmbsResponse200Result,
        )

        d = dict(src_dict)
        _result = d.pop("result", UNSET)
        result: GetRegisterAmbsResponse200Result | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = GetRegisterAmbsResponse200Result.from_dict(_result)

        _records = d.pop("records", UNSET)
        records: list[GetRegisterAmbsResponse200RecordsItem] | Unset = UNSET
        if _records is not UNSET:
            records = []
            for records_item_data in _records:
                records_item = GetRegisterAmbsResponse200RecordsItem.from_dict(
                    records_item_data
                )

                records.append(records_item)

        get_register_ambs_response_200 = cls(
            result=result,
            records=records,
        )

        get_register_ambs_response_200.additional_properties = d
        return get_register_ambs_response_200

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
