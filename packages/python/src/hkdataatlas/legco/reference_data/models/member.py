from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Member")


@_attrs_define
class Member:
    """Member fields documented by the reference-data dictionary. Requiredness is not specified.

    Attributes:
        english_name (str | Unset): English name of the Member. Example: Abraham.
        firstname_chi (str | Unset): First name of the Member in Chinese. Example: 禮謙.
        firstname_eng (str | Unset): First name of the Member in English. Example: Lai-him.
        honourable_chi (str | Unset): Honorific of the Member in Chinese. Example: GBS, JP.
        honourable_eng (str | Unset): Honorific of the Member in English. Example: GBS, JP.
        latest_term_id (float | Unset): The latest term that the Member belongs to. Example: 5.
        member_id (float | Unset): Member identifier. Example: 187.
        seq_num (float | Unset): Sequence number. Example: 4.
        surname_chi (str | Unset): Surname of the Member in Chinese. Example: 石.
        surname_eng (str | Unset): Surname of the Member in English. Example: SHEK.
        title_chi (str | Unset): Title of the Member in Chinese. Example: 議員.
        title_eng (str | Unset): Title of the Member in English. Example: Hon.
    """

    english_name: str | Unset = UNSET
    firstname_chi: str | Unset = UNSET
    firstname_eng: str | Unset = UNSET
    honourable_chi: str | Unset = UNSET
    honourable_eng: str | Unset = UNSET
    latest_term_id: float | Unset = UNSET
    member_id: float | Unset = UNSET
    seq_num: float | Unset = UNSET
    surname_chi: str | Unset = UNSET
    surname_eng: str | Unset = UNSET
    title_chi: str | Unset = UNSET
    title_eng: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        english_name = self.english_name

        firstname_chi = self.firstname_chi

        firstname_eng = self.firstname_eng

        honourable_chi = self.honourable_chi

        honourable_eng = self.honourable_eng

        latest_term_id = self.latest_term_id

        member_id = self.member_id

        seq_num = self.seq_num

        surname_chi = self.surname_chi

        surname_eng = self.surname_eng

        title_chi = self.title_chi

        title_eng = self.title_eng

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if english_name is not UNSET:
            field_dict["english_name"] = english_name
        if firstname_chi is not UNSET:
            field_dict["firstname_chi"] = firstname_chi
        if firstname_eng is not UNSET:
            field_dict["firstname_eng"] = firstname_eng
        if honourable_chi is not UNSET:
            field_dict["honourable_chi"] = honourable_chi
        if honourable_eng is not UNSET:
            field_dict["honourable_eng"] = honourable_eng
        if latest_term_id is not UNSET:
            field_dict["latest_term_id"] = latest_term_id
        if member_id is not UNSET:
            field_dict["member_id"] = member_id
        if seq_num is not UNSET:
            field_dict["seq_num"] = seq_num
        if surname_chi is not UNSET:
            field_dict["surname_chi"] = surname_chi
        if surname_eng is not UNSET:
            field_dict["surname_eng"] = surname_eng
        if title_chi is not UNSET:
            field_dict["title_chi"] = title_chi
        if title_eng is not UNSET:
            field_dict["title_eng"] = title_eng

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        english_name = d.pop("english_name", UNSET)

        firstname_chi = d.pop("firstname_chi", UNSET)

        firstname_eng = d.pop("firstname_eng", UNSET)

        honourable_chi = d.pop("honourable_chi", UNSET)

        honourable_eng = d.pop("honourable_eng", UNSET)

        latest_term_id = d.pop("latest_term_id", UNSET)

        member_id = d.pop("member_id", UNSET)

        seq_num = d.pop("seq_num", UNSET)

        surname_chi = d.pop("surname_chi", UNSET)

        surname_eng = d.pop("surname_eng", UNSET)

        title_chi = d.pop("title_chi", UNSET)

        title_eng = d.pop("title_eng", UNSET)

        member = cls(
            english_name=english_name,
            firstname_chi=firstname_chi,
            firstname_eng=firstname_eng,
            honourable_chi=honourable_chi,
            honourable_eng=honourable_eng,
            latest_term_id=latest_term_id,
            member_id=member_id,
            seq_num=seq_num,
            surname_chi=surname_chi,
            surname_eng=surname_eng,
            title_chi=title_chi,
            title_eng=title_eng,
        )

        member.additional_properties = d
        return member

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
