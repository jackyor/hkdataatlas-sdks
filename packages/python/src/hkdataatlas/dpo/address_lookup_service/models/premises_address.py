from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chi_premises_address import ChiPremisesAddress
    from ..models.eng_premises_address import EngPremisesAddress
    from ..models.geospatial_information import GeospatialInformation


T = TypeVar("T", bound="PremisesAddress")


@_attrs_define
class PremisesAddress:
    """Reference to an address which can be occupied by persons or organisations.

    Attributes:
        chi_premises_address (ChiPremisesAddress | Unset): Structured Chinese address referring to a location that can
            be occupied by persons or organisations within Hong Kong.
        eng_premises_address (EngPremisesAddress | Unset): Structured English address referring to a location that can
            be occupied by persons or organisations within Hong Kong.
        geo_address (str | Unset): GeoAddress identifier. The dictionary describes format CHAR(19).
        geospatial_information (GeospatialInformation | Unset): Geospatial information for an address. The companion XML
            schema describes these values as text; its maximum-length restrictions are included.
    """

    chi_premises_address: ChiPremisesAddress | Unset = UNSET
    eng_premises_address: EngPremisesAddress | Unset = UNSET
    geo_address: str | Unset = UNSET
    geospatial_information: GeospatialInformation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chi_premises_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_premises_address, Unset):
            chi_premises_address = self.chi_premises_address.to_dict()

        eng_premises_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_premises_address, Unset):
            eng_premises_address = self.eng_premises_address.to_dict()

        geo_address = self.geo_address

        geospatial_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.geospatial_information, Unset):
            geospatial_information = self.geospatial_information.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chi_premises_address is not UNSET:
            field_dict["ChiPremisesAddress"] = chi_premises_address
        if eng_premises_address is not UNSET:
            field_dict["EngPremisesAddress"] = eng_premises_address
        if geo_address is not UNSET:
            field_dict["GeoAddress"] = geo_address
        if geospatial_information is not UNSET:
            field_dict["GeospatialInformation"] = geospatial_information

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.chi_premises_address import ChiPremisesAddress
        from ..models.eng_premises_address import EngPremisesAddress
        from ..models.geospatial_information import GeospatialInformation

        d = dict(src_dict)
        _chi_premises_address = d.pop("ChiPremisesAddress", UNSET)
        chi_premises_address: ChiPremisesAddress | Unset
        if isinstance(_chi_premises_address, Unset):
            chi_premises_address = UNSET
        else:
            chi_premises_address = ChiPremisesAddress.from_dict(_chi_premises_address)

        _eng_premises_address = d.pop("EngPremisesAddress", UNSET)
        eng_premises_address: EngPremisesAddress | Unset
        if isinstance(_eng_premises_address, Unset):
            eng_premises_address = UNSET
        else:
            eng_premises_address = EngPremisesAddress.from_dict(_eng_premises_address)

        geo_address = d.pop("GeoAddress", UNSET)

        _geospatial_information = d.pop("GeospatialInformation", UNSET)
        geospatial_information: GeospatialInformation | Unset
        if isinstance(_geospatial_information, Unset):
            geospatial_information = UNSET
        else:
            geospatial_information = GeospatialInformation.from_dict(
                _geospatial_information
            )

        premises_address = cls(
            chi_premises_address=chi_premises_address,
            eng_premises_address=eng_premises_address,
            geo_address=geo_address,
            geospatial_information=geospatial_information,
        )

        premises_address.additional_properties = d
        return premises_address

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
