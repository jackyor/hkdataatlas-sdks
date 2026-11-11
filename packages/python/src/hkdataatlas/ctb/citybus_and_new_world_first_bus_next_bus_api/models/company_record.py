from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyRecord")


@_attrs_define
class CompanyRecord:
    """
    Attributes:
        co (str | Unset):
        name_en (str | Unset):
        name_tc (str | Unset):
        name_sc (str | Unset):
        url (str | Unset):
        data_timestamp (str | Unset): ISO 8601 date time with time zone per dictionary; no stronger lexical restriction
            inferred.
    """

    co: str | Unset = UNSET
    name_en: str | Unset = UNSET
    name_tc: str | Unset = UNSET
    name_sc: str | Unset = UNSET
    url: str | Unset = UNSET
    data_timestamp: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co = self.co

        name_en = self.name_en

        name_tc = self.name_tc

        name_sc = self.name_sc

        url = self.url

        data_timestamp = self.data_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co is not UNSET:
            field_dict["co"] = co
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc
        if name_sc is not UNSET:
            field_dict["name_sc"] = name_sc
        if url is not UNSET:
            field_dict["url"] = url
        if data_timestamp is not UNSET:
            field_dict["data_timestamp"] = data_timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        co = d.pop("co", UNSET)

        name_en = d.pop("name_en", UNSET)

        name_tc = d.pop("name_tc", UNSET)

        name_sc = d.pop("name_sc", UNSET)

        url = d.pop("url", UNSET)

        data_timestamp = d.pop("data_timestamp", UNSET)

        company_record = cls(
            co=co,
            name_en=name_en,
            name_tc=name_tc,
            name_sc=name_sc,
            url=url,
            data_timestamp=data_timestamp,
        )

        company_record.additional_properties = d
        return company_record

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
