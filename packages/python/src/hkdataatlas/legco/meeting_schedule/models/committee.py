from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Committee")


@_attrs_define
class Committee:
    """Fields documented for Tcommittee. No universal requiredness is specified.

    Attributes:
        committee_code (str | Unset): Code of the committee. Example: PL/HOU.
        committee_id (int | Unset): Committee identifier. Example: 2608.
        home_url_chi (str | Unset): URL of the Chinese committee home page. Example shown by the dictionary:
            http://www.legco.gov.hk/general/chinese/panels/yr16-20/hg.htm.
        home_url_eng (str | Unset): URL of the English committee home page. Example shown by the dictionary:
            http://www.legco.gov.hk/general/english/panels/yr16-20/hg.htm.
        name_chi (str | Unset): Committee name in Chinese. Example: 房屋事務委員會.
        name_eng (str | Unset): Committee name in English. Example: Panel on Housing.
        term_id (int | Unset): Term identifier. Example: 5.
    """

    committee_code: str | Unset = UNSET
    committee_id: int | Unset = UNSET
    home_url_chi: str | Unset = UNSET
    home_url_eng: str | Unset = UNSET
    name_chi: str | Unset = UNSET
    name_eng: str | Unset = UNSET
    term_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        committee_code = self.committee_code

        committee_id = self.committee_id

        home_url_chi = self.home_url_chi

        home_url_eng = self.home_url_eng

        name_chi = self.name_chi

        name_eng = self.name_eng

        term_id = self.term_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if committee_code is not UNSET:
            field_dict["committee_code"] = committee_code
        if committee_id is not UNSET:
            field_dict["committee_id"] = committee_id
        if home_url_chi is not UNSET:
            field_dict["home_url_chi"] = home_url_chi
        if home_url_eng is not UNSET:
            field_dict["home_url_eng"] = home_url_eng
        if name_chi is not UNSET:
            field_dict["name_chi"] = name_chi
        if name_eng is not UNSET:
            field_dict["name_eng"] = name_eng
        if term_id is not UNSET:
            field_dict["term_id"] = term_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        committee_code = d.pop("committee_code", UNSET)

        committee_id = d.pop("committee_id", UNSET)

        home_url_chi = d.pop("home_url_chi", UNSET)

        home_url_eng = d.pop("home_url_eng", UNSET)

        name_chi = d.pop("name_chi", UNSET)

        name_eng = d.pop("name_eng", UNSET)

        term_id = d.pop("term_id", UNSET)

        committee = cls(
            committee_code=committee_code,
            committee_id=committee_id,
            home_url_chi=home_url_chi,
            home_url_eng=home_url_eng,
            name_chi=name_chi,
            name_eng=name_eng,
            term_id=term_id,
        )

        committee.additional_properties = d
        return committee

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
