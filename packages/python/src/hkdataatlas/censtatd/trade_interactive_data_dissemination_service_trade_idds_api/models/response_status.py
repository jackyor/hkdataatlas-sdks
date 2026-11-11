from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.response_status_code import ResponseStatusCode, check_response_status_code
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseStatus")


@_attrs_define
class ResponseStatus:
    """Response status values documented by the publisher.

    Attributes:
        api_help (str | Unset): API help link shown in the response example.
        code (ResponseStatusCode | Unset): Documented status code: 0 query success, 1 validation error, 2 usage limit
            reached, 3 server busy, and 4 access denied.
        description (str | Unset): Status description.
        name (str | Unset): Status name.
    """

    api_help: str | Unset = UNSET
    code: ResponseStatusCode | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_help = self.api_help

        code: int | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code

        description = self.description

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_help is not UNSET:
            field_dict["apiHelp"] = api_help
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        api_help = d.pop("apiHelp", UNSET)

        _code = d.pop("code", UNSET)
        code: ResponseStatusCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = check_response_status_code(_code)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        response_status = cls(
            api_help=api_help,
            code=code,
            description=description,
            name=name,
        )

        response_status.additional_properties = d
        return response_status

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
