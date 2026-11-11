from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemarkLegend")


@_attrs_define
class RemarkLegend:
    """Remark legend field dictionary; wire types and requiredness are not specified.

    Attributes:
        legend_english (str | Unset): Remark legend in English.
        legend_s_chinese (str | Unset): Remark legend in Simplified Chinese.
        legend_t_chinese (str | Unset): Remark legend in Traditional Chinese.
        remark_legend (Any | Unset): XML-only one of the remarks in the list.
        remark_name (Any | Unset): Remark identifier.
    """

    legend_english: str | Unset = UNSET
    legend_s_chinese: str | Unset = UNSET
    legend_t_chinese: str | Unset = UNSET
    remark_legend: Any | Unset = UNSET
    remark_name: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legend_english = self.legend_english

        legend_s_chinese = self.legend_s_chinese

        legend_t_chinese = self.legend_t_chinese

        remark_legend = self.remark_legend

        remark_name = self.remark_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if legend_english is not UNSET:
            field_dict["legendEnglish"] = legend_english
        if legend_s_chinese is not UNSET:
            field_dict["legendSChinese"] = legend_s_chinese
        if legend_t_chinese is not UNSET:
            field_dict["legendTChinese"] = legend_t_chinese
        if remark_legend is not UNSET:
            field_dict["remarkLegend"] = remark_legend
        if remark_name is not UNSET:
            field_dict["remarkName"] = remark_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        legend_english = d.pop("legendEnglish", UNSET)

        legend_s_chinese = d.pop("legendSChinese", UNSET)

        legend_t_chinese = d.pop("legendTChinese", UNSET)

        remark_legend = d.pop("remarkLegend", UNSET)

        remark_name = d.pop("remarkName", UNSET)

        remark_legend = cls(
            legend_english=legend_english,
            legend_s_chinese=legend_s_chinese,
            legend_t_chinese=legend_t_chinese,
            remark_legend=remark_legend,
            remark_name=remark_name,
        )

        remark_legend.additional_properties = d
        return remark_legend

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
