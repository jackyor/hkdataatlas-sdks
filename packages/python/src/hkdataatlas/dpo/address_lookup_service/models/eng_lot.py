from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structured_lot import StructuredLot


T = TypeVar("T", bound="EngLot")


@_attrs_define
class EngLot:
    """Lot information in English. The XML dictionary schema describes either structured lot entries or free-text lot
    lines; those XML choice details are not treated as a JSON guarantee.

        Attributes:
            eng_structured_lot (list[StructuredLot] | Unset):
            free_text_lot_lines (list[str] | Unset):
    """

    eng_structured_lot: list[StructuredLot] | Unset = UNSET
    free_text_lot_lines: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        eng_structured_lot: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.eng_structured_lot, Unset):
            eng_structured_lot = []
            for eng_structured_lot_item_data in self.eng_structured_lot:
                eng_structured_lot_item = eng_structured_lot_item_data.to_dict()
                eng_structured_lot.append(eng_structured_lot_item)

        free_text_lot_lines: list[str] | Unset = UNSET
        if not isinstance(self.free_text_lot_lines, Unset):
            free_text_lot_lines = self.free_text_lot_lines

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eng_structured_lot is not UNSET:
            field_dict["EngStructuredLot"] = eng_structured_lot
        if free_text_lot_lines is not UNSET:
            field_dict["FreeTextLotLines"] = free_text_lot_lines

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.structured_lot import StructuredLot

        d = dict(src_dict)
        _eng_structured_lot = d.pop("EngStructuredLot", UNSET)
        eng_structured_lot: list[StructuredLot] | Unset = UNSET
        if _eng_structured_lot is not UNSET:
            eng_structured_lot = []
            for eng_structured_lot_item_data in _eng_structured_lot:
                eng_structured_lot_item = StructuredLot.from_dict(
                    eng_structured_lot_item_data
                )

                eng_structured_lot.append(eng_structured_lot_item)

        free_text_lot_lines = cast(list[str], d.pop("FreeTextLotLines", UNSET))

        eng_lot = cls(
            eng_structured_lot=eng_structured_lot,
            free_text_lot_lines=free_text_lot_lines,
        )

        eng_lot.additional_properties = d
        return eng_lot

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
