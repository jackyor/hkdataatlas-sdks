from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chi_premises_address_region import (
    ChiPremisesAddressRegion,
    check_chi_premises_address_region,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chi_3d_address import Chi3DAddress
    from ..models.chi_block import ChiBlock
    from ..models.chi_district import ChiDistrict
    from ..models.chi_estate import ChiEstate
    from ..models.chi_lot import ChiLot
    from ..models.chi_street import ChiStreet
    from ..models.chi_village import ChiVillage


T = TypeVar("T", bound="ChiPremisesAddress")


@_attrs_define
class ChiPremisesAddress:
    """Structured Chinese address referring to a location that can be occupied by persons or organisations within Hong
    Kong.

        Attributes:
            building_name (str | Unset): Full building name in Chinese.
            chi_3_d_address (Chi3DAddress | Unset): Optional Chinese floor and unit information; documented as available
                when `3d=1`.
            chi_block (ChiBlock | Unset): Block information in Chinese.
            chi_district (ChiDistrict | Unset): District and/or sub-district information in Chinese.
            chi_estate (ChiEstate | Unset): Estate name and related information in Chinese.
            chi_lot (ChiLot | Unset): Lot information in Chinese. The XML dictionary schema describes either structured lot
                entries or free-text lot lines; those XML choice details are not treated as a JSON guarantee.
            chi_street (ChiStreet | Unset): Street name and building number information in Chinese.
            chi_village (ChiVillage | Unset): Village name and building number information in Chinese.
            region (ChiPremisesAddressRegion | Unset): Region to which the address belongs.
    """

    building_name: str | Unset = UNSET
    chi_3_d_address: Chi3DAddress | Unset = UNSET
    chi_block: ChiBlock | Unset = UNSET
    chi_district: ChiDistrict | Unset = UNSET
    chi_estate: ChiEstate | Unset = UNSET
    chi_lot: ChiLot | Unset = UNSET
    chi_street: ChiStreet | Unset = UNSET
    chi_village: ChiVillage | Unset = UNSET
    region: ChiPremisesAddressRegion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        building_name = self.building_name

        chi_3_d_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_3_d_address, Unset):
            chi_3_d_address = self.chi_3_d_address.to_dict()

        chi_block: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_block, Unset):
            chi_block = self.chi_block.to_dict()

        chi_district: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_district, Unset):
            chi_district = self.chi_district.to_dict()

        chi_estate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_estate, Unset):
            chi_estate = self.chi_estate.to_dict()

        chi_lot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_lot, Unset):
            chi_lot = self.chi_lot.to_dict()

        chi_street: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_street, Unset):
            chi_street = self.chi_street.to_dict()

        chi_village: dict[str, Any] | Unset = UNSET
        if not isinstance(self.chi_village, Unset):
            chi_village = self.chi_village.to_dict()

        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if building_name is not UNSET:
            field_dict["BuildingName"] = building_name
        if chi_3_d_address is not UNSET:
            field_dict["Chi3dAddress"] = chi_3_d_address
        if chi_block is not UNSET:
            field_dict["ChiBlock"] = chi_block
        if chi_district is not UNSET:
            field_dict["ChiDistrict"] = chi_district
        if chi_estate is not UNSET:
            field_dict["ChiEstate"] = chi_estate
        if chi_lot is not UNSET:
            field_dict["ChiLot"] = chi_lot
        if chi_street is not UNSET:
            field_dict["ChiStreet"] = chi_street
        if chi_village is not UNSET:
            field_dict["ChiVillage"] = chi_village
        if region is not UNSET:
            field_dict["Region"] = region

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.chi_3d_address import Chi3DAddress
        from ..models.chi_block import ChiBlock
        from ..models.chi_district import ChiDistrict
        from ..models.chi_estate import ChiEstate
        from ..models.chi_lot import ChiLot
        from ..models.chi_street import ChiStreet
        from ..models.chi_village import ChiVillage

        d = dict(src_dict)
        building_name = d.pop("BuildingName", UNSET)

        _chi_3_d_address = d.pop("Chi3dAddress", UNSET)
        chi_3_d_address: Chi3DAddress | Unset
        if isinstance(_chi_3_d_address, Unset):
            chi_3_d_address = UNSET
        else:
            chi_3_d_address = Chi3DAddress.from_dict(_chi_3_d_address)

        _chi_block = d.pop("ChiBlock", UNSET)
        chi_block: ChiBlock | Unset
        if isinstance(_chi_block, Unset):
            chi_block = UNSET
        else:
            chi_block = ChiBlock.from_dict(_chi_block)

        _chi_district = d.pop("ChiDistrict", UNSET)
        chi_district: ChiDistrict | Unset
        if isinstance(_chi_district, Unset):
            chi_district = UNSET
        else:
            chi_district = ChiDistrict.from_dict(_chi_district)

        _chi_estate = d.pop("ChiEstate", UNSET)
        chi_estate: ChiEstate | Unset
        if isinstance(_chi_estate, Unset):
            chi_estate = UNSET
        else:
            chi_estate = ChiEstate.from_dict(_chi_estate)

        _chi_lot = d.pop("ChiLot", UNSET)
        chi_lot: ChiLot | Unset
        if isinstance(_chi_lot, Unset):
            chi_lot = UNSET
        else:
            chi_lot = ChiLot.from_dict(_chi_lot)

        _chi_street = d.pop("ChiStreet", UNSET)
        chi_street: ChiStreet | Unset
        if isinstance(_chi_street, Unset):
            chi_street = UNSET
        else:
            chi_street = ChiStreet.from_dict(_chi_street)

        _chi_village = d.pop("ChiVillage", UNSET)
        chi_village: ChiVillage | Unset
        if isinstance(_chi_village, Unset):
            chi_village = UNSET
        else:
            chi_village = ChiVillage.from_dict(_chi_village)

        _region = d.pop("Region", UNSET)
        region: ChiPremisesAddressRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = check_chi_premises_address_region(_region)

        chi_premises_address = cls(
            building_name=building_name,
            chi_3_d_address=chi_3_d_address,
            chi_block=chi_block,
            chi_district=chi_district,
            chi_estate=chi_estate,
            chi_lot=chi_lot,
            chi_street=chi_street,
            chi_village=chi_village,
            region=region,
        )

        chi_premises_address.additional_properties = d
        return chi_premises_address

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
