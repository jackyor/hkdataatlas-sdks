from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RecPubDisActByHkma")


@_attrs_define
class RecPubDisActByHkma:
    """
    Attributes:
        action_date (str | Unset):
        action_taken (str | Unset):
        pr_en (str | Unset):
        pr_tc (str | Unset):
    """

    action_date: str | Unset = UNSET
    action_taken: str | Unset = UNSET
    pr_en: str | Unset = UNSET
    pr_tc: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_date = self.action_date

        action_taken = self.action_taken

        pr_en = self.pr_en

        pr_tc = self.pr_tc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_date is not UNSET:
            field_dict["action_date"] = action_date
        if action_taken is not UNSET:
            field_dict["action_taken"] = action_taken
        if pr_en is not UNSET:
            field_dict["pr_en"] = pr_en
        if pr_tc is not UNSET:
            field_dict["pr_tc"] = pr_tc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        action_date = d.pop("action_date", UNSET)

        action_taken = d.pop("action_taken", UNSET)

        pr_en = d.pop("pr_en", UNSET)

        pr_tc = d.pop("pr_tc", UNSET)

        rec_pub_dis_act_by_hkma = cls(
            action_date=action_date,
            action_taken=action_taken,
            pr_en=pr_en,
            pr_tc=pr_tc,
        )

        rec_pub_dis_act_by_hkma.additional_properties = d
        return rec_pub_dis_act_by_hkma

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
