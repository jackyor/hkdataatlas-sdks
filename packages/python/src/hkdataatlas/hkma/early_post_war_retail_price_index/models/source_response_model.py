from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.header import Header
    from ..models.result import Result


T = TypeVar("T", bound="SourceResponseModel")


@_attrs_define
class SourceResponseModel:
    """
    Attributes:
        header (Header | Unset):
        result (Result | Unset):
    """

    header: Header | Unset = UNSET
    result: Result | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.header import Header
        from ..models.result import Result

        d = dict(src_dict)
        _header = d.pop("header", UNSET)
        header: Header | Unset
        if isinstance(_header, Unset):
            header = UNSET
        else:
            header = Header.from_dict(_header)

        _result = d.pop("result", UNSET)
        result: Result | Unset
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = Result.from_dict(_result)

        source_response_model = cls(
            header=header,
            result=result,
        )

        source_response_model.additional_properties = d
        return source_response_model

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
