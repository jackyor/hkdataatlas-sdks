from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structured_lot import StructuredLot


T = TypeVar("T", bound="ChiLot")


@_attrs_define
class ChiLot:
    """Lot information in Chinese. The XML dictionary schema describes either structured lot entries or free-text lot
    lines; those XML choice details are not treated as a JSON guarantee.

        Attributes:
            chi_structured_lot (list[StructuredLot] | Unset):
            free_text_lot_lines (list[str] | Unset):
    """

    chi_structured_lot: list[StructuredLot] | Unset = UNSET
    free_text_lot_lines: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chi_structured_lot: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.chi_structured_lot, Unset):
            chi_structured_lot = []
            for chi_structured_lot_item_data in self.chi_structured_lot:
                chi_structured_lot_item = chi_structured_lot_item_data.to_dict()
                chi_structured_lot.append(chi_structured_lot_item)

        free_text_lot_lines: list[str] | Unset = UNSET
        if not isinstance(self.free_text_lot_lines, Unset):
            free_text_lot_lines = self.free_text_lot_lines

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chi_structured_lot is not UNSET:
            field_dict["ChiStructuredLot"] = chi_structured_lot
        if free_text_lot_lines is not UNSET:
            field_dict["FreeTextLotLines"] = free_text_lot_lines

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.structured_lot import StructuredLot

        d = dict(src_dict)
        _chi_structured_lot = d.pop("ChiStructuredLot", UNSET)
        chi_structured_lot: list[StructuredLot] | Unset = UNSET
        if _chi_structured_lot is not UNSET:
            chi_structured_lot = []
            for chi_structured_lot_item_data in _chi_structured_lot:
                chi_structured_lot_item = StructuredLot.from_dict(
                    chi_structured_lot_item_data
                )

                chi_structured_lot.append(chi_structured_lot_item)

        free_text_lot_lines = cast(list[str], d.pop("FreeTextLotLines", UNSET))

        chi_lot = cls(
            chi_structured_lot=chi_structured_lot,
            free_text_lot_lines=free_text_lot_lines,
        )

        chi_lot.additional_properties = d
        return chi_lot

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
