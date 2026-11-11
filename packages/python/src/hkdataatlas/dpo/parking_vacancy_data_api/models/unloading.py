from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.unloading_type import UnloadingType, check_unloading_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usage_threshold import UsageThreshold


T = TypeVar("T", bound="Unloading")


@_attrs_define
class Unloading:
    """
    Attributes:
        price (float): Rate in Hong Kong dollars.
        type_ (UnloadingType):
        remark (str | Unset): Condition to which this rule applies; localized responses provide the remark in the
            specified locale.
        usage_thresholds (list[UsageThreshold] | Unset):
    """

    price: float
    type_: UnloadingType
    remark: str | Unset = UNSET
    usage_thresholds: list[UsageThreshold] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        price = self.price

        type_: str = self.type_

        remark = self.remark

        usage_thresholds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usage_thresholds, Unset):
            usage_thresholds = []
            for usage_thresholds_item_data in self.usage_thresholds:
                usage_thresholds_item = usage_thresholds_item_data.to_dict()
                usage_thresholds.append(usage_thresholds_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "price": price,
                "type": type_,
            }
        )
        if remark is not UNSET:
            field_dict["remark"] = remark
        if usage_thresholds is not UNSET:
            field_dict["usageThresholds"] = usage_thresholds

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_threshold import UsageThreshold

        d = dict(src_dict)
        price = d.pop("price")

        type_ = check_unloading_type(d.pop("type"))

        remark = d.pop("remark", UNSET)

        _usage_thresholds = d.pop("usageThresholds", UNSET)
        usage_thresholds: list[UsageThreshold] | Unset = UNSET
        if _usage_thresholds is not UNSET:
            usage_thresholds = []
            for usage_thresholds_item_data in _usage_thresholds:
                usage_thresholds_item = UsageThreshold.from_dict(
                    usage_thresholds_item_data
                )

                usage_thresholds.append(usage_thresholds_item)

        unloading = cls(
            price=price,
            type_=type_,
            remark=remark,
            usage_thresholds=usage_thresholds,
        )

        unloading.additional_properties = d
        return unloading

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
