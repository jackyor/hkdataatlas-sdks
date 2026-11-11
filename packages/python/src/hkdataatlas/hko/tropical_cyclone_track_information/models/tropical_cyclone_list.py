from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tropical_cyclone_list_entry import TropicalCycloneListEntry


T = TypeVar("T", bound="TropicalCycloneList")


@_attrs_define
class TropicalCycloneList:
    """XML root element TropicalCycloneList. It contains TropicalCyclone items when HKO currently issues forecast tracks;
    the item is absent when there are none.

        Attributes:
            tropical_cyclone (list[TropicalCycloneListEntry] | TropicalCycloneListEntry | Unset): Cyclone entry or entries.
                Absent when no tropical cyclone forecast track is currently issued.
    """

    tropical_cyclone: (
        list[TropicalCycloneListEntry] | TropicalCycloneListEntry | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tropical_cyclone_list_entry import TropicalCycloneListEntry

        tropical_cyclone: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.tropical_cyclone, Unset):
            tropical_cyclone = UNSET
        elif isinstance(self.tropical_cyclone, TropicalCycloneListEntry):
            tropical_cyclone = self.tropical_cyclone.to_dict()
        else:
            tropical_cyclone = []
            for tropical_cyclone_type_1_item_data in self.tropical_cyclone:
                tropical_cyclone_type_1_item = (
                    tropical_cyclone_type_1_item_data.to_dict()
                )
                tropical_cyclone.append(tropical_cyclone_type_1_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tropical_cyclone is not UNSET:
            field_dict["TropicalCyclone"] = tropical_cyclone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.tropical_cyclone_list_entry import TropicalCycloneListEntry

        d = dict(src_dict)

        def _parse_tropical_cyclone(
            data: object,
        ) -> list[TropicalCycloneListEntry] | TropicalCycloneListEntry | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tropical_cyclone_type_0 = TropicalCycloneListEntry.from_dict(data)

                return tropical_cyclone_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            tropical_cyclone_type_1 = []
            _tropical_cyclone_type_1 = data
            for tropical_cyclone_type_1_item_data in _tropical_cyclone_type_1:
                tropical_cyclone_type_1_item = TropicalCycloneListEntry.from_dict(
                    tropical_cyclone_type_1_item_data
                )

                tropical_cyclone_type_1.append(tropical_cyclone_type_1_item)

            return tropical_cyclone_type_1

        tropical_cyclone = _parse_tropical_cyclone(d.pop("TropicalCyclone", UNSET))

        tropical_cyclone_list = cls(
            tropical_cyclone=tropical_cyclone,
        )

        tropical_cyclone_list.additional_properties = d
        return tropical_cyclone_list

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
