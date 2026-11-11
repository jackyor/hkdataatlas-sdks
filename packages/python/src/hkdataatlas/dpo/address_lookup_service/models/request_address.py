from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestAddress")


@_attrs_define
class RequestAddress:
    """The address to be looked up.

    Attributes:
        address_line (list[str] | str | Unset): Free-text address captured from the input parameter. The observed JSON
            encodes this as an array of lines; this is an observation, not a declaration of all permitted representations.
    """

    address_line: list[str] | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_line: list[str] | str | Unset
        if isinstance(self.address_line, Unset):
            address_line = UNSET
        elif isinstance(self.address_line, list):
            address_line = self.address_line

        else:
            address_line = self.address_line

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_line is not UNSET:
            field_dict["AddressLine"] = address_line

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_line(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                address_line_type_1 = cast(list[str], data)

                return address_line_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        address_line = _parse_address_line(d.pop("AddressLine", UNSET))

        request_address = cls(
            address_line=address_line,
        )

        request_address.additional_properties = d
        return request_address

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
