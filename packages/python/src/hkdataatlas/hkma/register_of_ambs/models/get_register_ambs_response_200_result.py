from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetRegisterAmbsResponse200Result")


@_attrs_define
class GetRegisterAmbsResponse200Result:
    """
    Attributes:
        datasize (int | Unset):
        message (str | Unset):
    """

    datasize: int | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        datasize = self.datasize

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datasize is not UNSET:
            field_dict["datasize"] = datasize
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        datasize = d.pop("datasize", UNSET)

        message = d.pop("message", UNSET)

        get_register_ambs_response_200_result = cls(
            datasize=datasize,
            message=message,
        )

        get_register_ambs_response_200_result.additional_properties = d
        return get_register_ambs_response_200_result

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
