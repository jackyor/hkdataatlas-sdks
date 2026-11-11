from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        bank_name (str | Unset):
        review_arrangement_hotline (str | Unset):
        review_arrangement_email (None | str | Unset):
    """

    bank_name: str | Unset = UNSET
    review_arrangement_hotline: str | Unset = UNSET
    review_arrangement_email: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bank_name = self.bank_name

        review_arrangement_hotline = self.review_arrangement_hotline

        review_arrangement_email: None | str | Unset
        if isinstance(self.review_arrangement_email, Unset):
            review_arrangement_email = UNSET
        else:
            review_arrangement_email = self.review_arrangement_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if review_arrangement_hotline is not UNSET:
            field_dict["review_arrangement_hotline"] = review_arrangement_hotline
        if review_arrangement_email is not UNSET:
            field_dict["review_arrangement_email"] = review_arrangement_email

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        bank_name = d.pop("bank_name", UNSET)

        review_arrangement_hotline = d.pop("review_arrangement_hotline", UNSET)

        def _parse_review_arrangement_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_arrangement_email = _parse_review_arrangement_email(
            d.pop("review_arrangement_email", UNSET)
        )

        record = cls(
            bank_name=bank_name,
            review_arrangement_hotline=review_arrangement_hotline,
            review_arrangement_email=review_arrangement_email,
        )

        record.additional_properties = d
        return record

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
