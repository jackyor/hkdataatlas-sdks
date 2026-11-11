from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeightLimit")


@_attrs_define
class HeightLimit:
    """
    Attributes:
        height (float | str | Unset): Height limit in meters. The dictionary declares String, while the example uses a
            number.
        remark (str | Unset): Applicable condition, localized when requested.
    """

    height: float | str | Unset = UNSET
    remark: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height: float | str | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        remark = self.remark

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if remark is not UNSET:
            field_dict["remark"] = remark

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_height(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

        remark = d.pop("remark", UNSET)

        height_limit = cls(
            height=height,
            remark=remark,
        )

        height_limit.additional_properties = d
        return height_limit

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
