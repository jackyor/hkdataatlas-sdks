from __future__ import annotations

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
        retailbank_name (str | Unset):
        hotline_1 (str | Unset):
        remark_1 (str | Unset):
        hotline_2 (str | Unset):
        remark_2 (str | Unset):
        hotline_3 (str | Unset):
        remark_3 (str | Unset):
    """

    retailbank_name: str | Unset = UNSET
    hotline_1: str | Unset = UNSET
    remark_1: str | Unset = UNSET
    hotline_2: str | Unset = UNSET
    remark_2: str | Unset = UNSET
    hotline_3: str | Unset = UNSET
    remark_3: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retailbank_name = self.retailbank_name

        hotline_1 = self.hotline_1

        remark_1 = self.remark_1

        hotline_2 = self.hotline_2

        remark_2 = self.remark_2

        hotline_3 = self.hotline_3

        remark_3 = self.remark_3

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retailbank_name is not UNSET:
            field_dict["retailbank_name"] = retailbank_name
        if hotline_1 is not UNSET:
            field_dict["hotline_1"] = hotline_1
        if remark_1 is not UNSET:
            field_dict["remark_1"] = remark_1
        if hotline_2 is not UNSET:
            field_dict["hotline_2"] = hotline_2
        if remark_2 is not UNSET:
            field_dict["remark_2"] = remark_2
        if hotline_3 is not UNSET:
            field_dict["hotline_3"] = hotline_3
        if remark_3 is not UNSET:
            field_dict["remark_3"] = remark_3

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        retailbank_name = d.pop("retailbank_name", UNSET)

        hotline_1 = d.pop("hotline_1", UNSET)

        remark_1 = d.pop("remark_1", UNSET)

        hotline_2 = d.pop("hotline_2", UNSET)

        remark_2 = d.pop("remark_2", UNSET)

        hotline_3 = d.pop("hotline_3", UNSET)

        remark_3 = d.pop("remark_3", UNSET)

        record = cls(
            retailbank_name=retailbank_name,
            hotline_1=hotline_1,
            remark_1=remark_1,
            hotline_2=hotline_2,
            remark_2=remark_2,
            hotline_3=hotline_3,
            remark_3=remark_3,
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
