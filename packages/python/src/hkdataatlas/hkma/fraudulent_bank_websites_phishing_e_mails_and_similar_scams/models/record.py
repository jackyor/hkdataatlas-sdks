from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        issue_date (datetime.date | Unset):
        alleged_name (str | Unset):
        scam_type (str | Unset):
        pr_url (str | Unset):
        fraud_website_address (str | Unset):
    """

    issue_date: datetime.date | Unset = UNSET
    alleged_name: str | Unset = UNSET
    scam_type: str | Unset = UNSET
    pr_url: str | Unset = UNSET
    fraud_website_address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_date: str | Unset = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        alleged_name = self.alleged_name

        scam_type = self.scam_type

        pr_url = self.pr_url

        fraud_website_address = self.fraud_website_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if alleged_name is not UNSET:
            field_dict["alleged_name"] = alleged_name
        if scam_type is not UNSET:
            field_dict["scam_type"] = scam_type
        if pr_url is not UNSET:
            field_dict["pr_url"] = pr_url
        if fraud_website_address is not UNSET:
            field_dict["fraud_website_address"] = fraud_website_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _issue_date = d.pop("issue_date", UNSET)
        issue_date: datetime.date | Unset
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = datetime.date.fromisoformat(_issue_date)

        alleged_name = d.pop("alleged_name", UNSET)

        scam_type = d.pop("scam_type", UNSET)

        pr_url = d.pop("pr_url", UNSET)

        fraud_website_address = d.pop("fraud_website_address", UNSET)

        record = cls(
            issue_date=issue_date,
            alleged_name=alleged_name,
            scam_type=scam_type,
            pr_url=pr_url,
            fraud_website_address=fraud_website_address,
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
