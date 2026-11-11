from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_code import StatusCode, check_status_code
from ..models.status_name import StatusName, check_status_name
from ..types import UNSET, Unset

T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    """
    Attributes:
        name (StatusName):
        code (StatusCode): 0 = Query success
            1 = Validation error
        description (str):
        message (list[str] | None | str | Unset): Error detail(s) when `code = 1`.
            Null, omitted, or empty on success.
        api_help (str | Unset): Link to the API helper page on the corresponding Web Table webpage.
    """

    name: StatusName
    code: StatusCode
    description: str
    message: list[str] | None | str | Unset = UNSET
    api_help: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: str = self.name

        code: int = self.code

        description = self.description

        message: list[str] | None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        elif isinstance(self.message, list):
            message = self.message

        else:
            message = self.message

        api_help = self.api_help

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "code": code,
                "description": description,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if api_help is not UNSET:
            field_dict["apiHelp"] = api_help

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = check_status_name(d.pop("name"))

        code = check_status_code(d.pop("code"))

        description = d.pop("description")

        def _parse_message(data: object) -> list[str] | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                message_type_1_type_0 = cast(list[str], data)

                return message_type_1_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        api_help = d.pop("apiHelp", UNSET)

        status = cls(
            name=name,
            code=code,
            description=description,
            message=message,
            api_help=api_help,
        )

        status.additional_properties = d
        return status

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
