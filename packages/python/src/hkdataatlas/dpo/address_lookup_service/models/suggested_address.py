from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.validation_information_type_0 import ValidationInformationType0


T = TypeVar("T", bound="SuggestedAddress")


@_attrs_define
class SuggestedAddress:
    """A suggested address from the address database.

    Attributes:
        address (Address | Unset): A premises address or other address type, if applicable. The retained XML schema
            describes a PremisesAddress choice; it is not assumed to define the JSON response.
        validation_information (None | Unset | ValidationInformationType0): Preserves documented validation-information
            object and retained official null for geo-address results without validation information; no score/value
            coercion.
    """

    address: Address | Unset = UNSET
    validation_information: None | Unset | ValidationInformationType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.validation_information_type_0 import ValidationInformationType0

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        validation_information: dict[str, Any] | None | Unset
        if isinstance(self.validation_information, Unset):
            validation_information = UNSET
        elif isinstance(self.validation_information, ValidationInformationType0):
            validation_information = self.validation_information.to_dict()
        else:
            validation_information = self.validation_information

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["Address"] = address
        if validation_information is not UNSET:
            field_dict["ValidationInformation"] = validation_information

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.address import Address
        from ..models.validation_information_type_0 import ValidationInformationType0

        d = dict(src_dict)
        _address = d.pop("Address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        def _parse_validation_information(
            data: object,
        ) -> None | Unset | ValidationInformationType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_validation_information_type_0 = (
                    ValidationInformationType0.from_dict(data)
                )

                return componentsschemas_validation_information_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | ValidationInformationType0, data)

        validation_information = _parse_validation_information(
            d.pop("ValidationInformation", UNSET)
        )

        suggested_address = cls(
            address=address,
            validation_information=validation_information,
        )

        suggested_address.additional_properties = d
        return suggested_address

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
