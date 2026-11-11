from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.special_weather_tips_swt_item import SpecialWeatherTipsSwtItem


T = TypeVar("T", bound="SpecialWeatherTips")


@_attrs_define
class SpecialWeatherTips:
    """
    Attributes:
        swt (list[SpecialWeatherTipsSwtItem] | Unset):
    """

    swt: list[SpecialWeatherTipsSwtItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        swt: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.swt, Unset):
            swt = []
            for swt_item_data in self.swt:
                swt_item = swt_item_data.to_dict()
                swt.append(swt_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if swt is not UNSET:
            field_dict["swt"] = swt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.special_weather_tips_swt_item import SpecialWeatherTipsSwtItem

        d = dict(src_dict)
        _swt = d.pop("swt", UNSET)
        swt: list[SpecialWeatherTipsSwtItem] | Unset = UNSET
        if _swt is not UNSET:
            swt = []
            for swt_item_data in _swt:
                swt_item = SpecialWeatherTipsSwtItem.from_dict(swt_item_data)

                swt.append(swt_item)

        special_weather_tips = cls(
            swt=swt,
        )

        special_weather_tips.additional_properties = d
        return special_weather_tips

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
