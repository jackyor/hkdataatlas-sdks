from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.structured_lot_lot_extend_portion_code import (
    StructuredLotLotExtendPortionCode,
    check_structured_lot_lot_extend_portion_code,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StructuredLot")


@_attrs_define
class StructuredLot:
    """
    Attributes:
        dd_no (str | Unset):
        dd_type (str | Unset):
        lot_extend_portion_code (StructuredLotLotExtendPortionCode | Unset):
        lot_no (str | Unset):
        lot_section_1 (str | Unset):
        lot_section_2 (str | Unset):
        lot_section_3 (str | Unset):
        lot_section_4 (str | Unset):
        lot_subsection_1 (str | Unset):
        lot_subsection_2 (str | Unset):
        lot_subsection_3 (str | Unset):
        lot_type (str | Unset):
    """

    dd_no: str | Unset = UNSET
    dd_type: str | Unset = UNSET
    lot_extend_portion_code: StructuredLotLotExtendPortionCode | Unset = UNSET
    lot_no: str | Unset = UNSET
    lot_section_1: str | Unset = UNSET
    lot_section_2: str | Unset = UNSET
    lot_section_3: str | Unset = UNSET
    lot_section_4: str | Unset = UNSET
    lot_subsection_1: str | Unset = UNSET
    lot_subsection_2: str | Unset = UNSET
    lot_subsection_3: str | Unset = UNSET
    lot_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dd_no = self.dd_no

        dd_type = self.dd_type

        lot_extend_portion_code: str | Unset = UNSET
        if not isinstance(self.lot_extend_portion_code, Unset):
            lot_extend_portion_code = self.lot_extend_portion_code

        lot_no = self.lot_no

        lot_section_1 = self.lot_section_1

        lot_section_2 = self.lot_section_2

        lot_section_3 = self.lot_section_3

        lot_section_4 = self.lot_section_4

        lot_subsection_1 = self.lot_subsection_1

        lot_subsection_2 = self.lot_subsection_2

        lot_subsection_3 = self.lot_subsection_3

        lot_type = self.lot_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dd_no is not UNSET:
            field_dict["DdNo"] = dd_no
        if dd_type is not UNSET:
            field_dict["DdType"] = dd_type
        if lot_extend_portion_code is not UNSET:
            field_dict["LotExtendPortionCode"] = lot_extend_portion_code
        if lot_no is not UNSET:
            field_dict["LotNo"] = lot_no
        if lot_section_1 is not UNSET:
            field_dict["LotSection1"] = lot_section_1
        if lot_section_2 is not UNSET:
            field_dict["LotSection2"] = lot_section_2
        if lot_section_3 is not UNSET:
            field_dict["LotSection3"] = lot_section_3
        if lot_section_4 is not UNSET:
            field_dict["LotSection4"] = lot_section_4
        if lot_subsection_1 is not UNSET:
            field_dict["LotSubsection1"] = lot_subsection_1
        if lot_subsection_2 is not UNSET:
            field_dict["LotSubsection2"] = lot_subsection_2
        if lot_subsection_3 is not UNSET:
            field_dict["LotSubsection3"] = lot_subsection_3
        if lot_type is not UNSET:
            field_dict["LotType"] = lot_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dd_no = d.pop("DdNo", UNSET)

        dd_type = d.pop("DdType", UNSET)

        _lot_extend_portion_code = d.pop("LotExtendPortionCode", UNSET)
        lot_extend_portion_code: StructuredLotLotExtendPortionCode | Unset
        if isinstance(_lot_extend_portion_code, Unset):
            lot_extend_portion_code = UNSET
        else:
            lot_extend_portion_code = check_structured_lot_lot_extend_portion_code(
                _lot_extend_portion_code
            )

        lot_no = d.pop("LotNo", UNSET)

        lot_section_1 = d.pop("LotSection1", UNSET)

        lot_section_2 = d.pop("LotSection2", UNSET)

        lot_section_3 = d.pop("LotSection3", UNSET)

        lot_section_4 = d.pop("LotSection4", UNSET)

        lot_subsection_1 = d.pop("LotSubsection1", UNSET)

        lot_subsection_2 = d.pop("LotSubsection2", UNSET)

        lot_subsection_3 = d.pop("LotSubsection3", UNSET)

        lot_type = d.pop("LotType", UNSET)

        structured_lot = cls(
            dd_no=dd_no,
            dd_type=dd_type,
            lot_extend_portion_code=lot_extend_portion_code,
            lot_no=lot_no,
            lot_section_1=lot_section_1,
            lot_section_2=lot_section_2,
            lot_section_3=lot_section_3,
            lot_section_4=lot_section_4,
            lot_subsection_1=lot_subsection_1,
            lot_subsection_2=lot_subsection_2,
            lot_subsection_3=lot_subsection_3,
            lot_type=lot_type,
        )

        structured_lot.additional_properties = d
        return structured_lot

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
