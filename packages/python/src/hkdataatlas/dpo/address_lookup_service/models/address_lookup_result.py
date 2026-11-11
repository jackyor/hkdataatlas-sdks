from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_address import RequestAddress
    from ..models.suggested_address import SuggestedAddress


T = TypeVar("T", bound="AddressLookupResult")


@_attrs_define
class AddressLookupResult:
    """Conceptual lookup result containing the request address and suggested addresses in decreasing order of similarity.
    The observed JSON has RequestAddress and SuggestedAddress at the top level; the XML schema is XML-only and is not
    treated as a JSON schema.

        Attributes:
            request_address (RequestAddress | Unset): The address to be looked up.
            suggested_address (list[SuggestedAddress] | Unset): Suggested addresses in decreasing similarity order; the
                dictionary notes a maximum of 200 results.
    """

    request_address: RequestAddress | Unset = UNSET
    suggested_address: list[SuggestedAddress] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request_address, Unset):
            request_address = self.request_address.to_dict()

        suggested_address: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suggested_address, Unset):
            suggested_address = []
            for suggested_address_item_data in self.suggested_address:
                suggested_address_item = suggested_address_item_data.to_dict()
                suggested_address.append(suggested_address_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_address is not UNSET:
            field_dict["RequestAddress"] = request_address
        if suggested_address is not UNSET:
            field_dict["SuggestedAddress"] = suggested_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.request_address import RequestAddress
        from ..models.suggested_address import SuggestedAddress

        d = dict(src_dict)
        _request_address = d.pop("RequestAddress", UNSET)
        request_address: RequestAddress | Unset
        if isinstance(_request_address, Unset):
            request_address = UNSET
        else:
            request_address = RequestAddress.from_dict(_request_address)

        _suggested_address = d.pop("SuggestedAddress", UNSET)
        suggested_address: list[SuggestedAddress] | Unset = UNSET
        if _suggested_address is not UNSET:
            suggested_address = []
            for suggested_address_item_data in _suggested_address:
                suggested_address_item = SuggestedAddress.from_dict(
                    suggested_address_item_data
                )

                suggested_address.append(suggested_address_item)

        address_lookup_result = cls(
            request_address=request_address,
            suggested_address=suggested_address,
        )

        address_lookup_result.additional_properties = d
        return address_lookup_result

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
