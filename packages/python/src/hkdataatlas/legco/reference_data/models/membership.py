from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Membership")


@_attrs_define
class Membership:
    """Committee membership record fields documented by the reference-data dictionary. Requiredness is not specified.

    Attributes:
        committee_id (float | Unset): Committee identifier. Example: 2567.
        id (float | Unset): Record identifier. Example: 23684.
        member_id (float | Unset): Member identifier. Example: 910.
        membership_id (float | Unset): Membership identifier. Example: 38562.
        post_chi (str | Unset): Post name in Chinese. Example: 委員.
        post_end_date (datetime.datetime | Unset): End date of the post. Documented format: YYYY-MM-DDThh:mm:ss (ISO
            8601).
        post_eng (str | Unset): Post name in English. Example: Member.
        post_start_date (datetime.datetime | Unset): Start date of the post. Documented format: YYYY-MM-DDThh:mm:ss (ISO
            8601). Example: 2016-10-12T10:00:00.
        term_id (float | Unset): Term identifier. Example: 5.
    """

    committee_id: float | Unset = UNSET
    id: float | Unset = UNSET
    member_id: float | Unset = UNSET
    membership_id: float | Unset = UNSET
    post_chi: str | Unset = UNSET
    post_end_date: datetime.datetime | Unset = UNSET
    post_eng: str | Unset = UNSET
    post_start_date: datetime.datetime | Unset = UNSET
    term_id: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        committee_id = self.committee_id

        id = self.id

        member_id = self.member_id

        membership_id = self.membership_id

        post_chi = self.post_chi

        post_end_date: str | Unset = UNSET
        if not isinstance(self.post_end_date, Unset):
            post_end_date = self.post_end_date.isoformat()

        post_eng = self.post_eng

        post_start_date: str | Unset = UNSET
        if not isinstance(self.post_start_date, Unset):
            post_start_date = self.post_start_date.isoformat()

        term_id = self.term_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if committee_id is not UNSET:
            field_dict["committee_id"] = committee_id
        if id is not UNSET:
            field_dict["id"] = id
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if membership_id is not UNSET:
            field_dict["membership_id"] = membership_id
        if post_chi is not UNSET:
            field_dict["post_chi"] = post_chi
        if post_end_date is not UNSET:
            field_dict["post_end_date"] = post_end_date
        if post_eng is not UNSET:
            field_dict["post_eng"] = post_eng
        if post_start_date is not UNSET:
            field_dict["post_start_date"] = post_start_date
        if term_id is not UNSET:
            field_dict["term_id"] = term_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        committee_id = d.pop("committee_id", UNSET)

        id = d.pop("id", UNSET)

        member_id = d.pop("member_id", UNSET)

        membership_id = d.pop("membership_id", UNSET)

        post_chi = d.pop("post_chi", UNSET)

        _post_end_date = d.pop("post_end_date", UNSET)
        post_end_date: datetime.datetime | Unset
        if isinstance(_post_end_date, Unset):
            post_end_date = UNSET
        else:
            post_end_date = datetime.datetime.fromisoformat(_post_end_date)

        post_eng = d.pop("post_eng", UNSET)

        _post_start_date = d.pop("post_start_date", UNSET)
        post_start_date: datetime.datetime | Unset
        if isinstance(_post_start_date, Unset):
            post_start_date = UNSET
        else:
            post_start_date = datetime.datetime.fromisoformat(_post_start_date)

        term_id = d.pop("term_id", UNSET)

        membership = cls(
            committee_id=committee_id,
            id=id,
            member_id=member_id,
            membership_id=membership_id,
            post_chi=post_chi,
            post_end_date=post_end_date,
            post_eng=post_eng,
            post_start_date=post_start_date,
            term_id=term_id,
        )

        membership.additional_properties = d
        return membership

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
