from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.premises_address import PremisesAddress


T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """A premises address or other address type, if applicable. The retained XML schema describes a PremisesAddress choice;
    it is not assumed to define the JSON response.

        Attributes:
            premises_address (PremisesAddress | Unset): Reference to an address which can be occupied by persons or
                organisations.
    """

    premises_address: PremisesAddress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        premises_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.premises_address, Unset):
            premises_address = self.premises_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if premises_address is not UNSET:
            field_dict["PremisesAddress"] = premises_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.premises_address import PremisesAddress

        d = dict(src_dict)
        _premises_address = d.pop("PremisesAddress", UNSET)
        premises_address: PremisesAddress | Unset
        if isinstance(_premises_address, Unset):
            premises_address = UNSET
        else:
            premises_address = PremisesAddress.from_dict(_premises_address)

        address = cls(
            premises_address=premises_address,
        )

        address.additional_properties = d
        return address

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
