from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.eng_premises_address_region import (
    EngPremisesAddressRegion,
    check_eng_premises_address_region,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eng_3d_address import Eng3DAddress
    from ..models.eng_block import EngBlock
    from ..models.eng_district import EngDistrict
    from ..models.eng_estate import EngEstate
    from ..models.eng_lot import EngLot
    from ..models.eng_street import EngStreet
    from ..models.eng_village import EngVillage


T = TypeVar("T", bound="EngPremisesAddress")


@_attrs_define
class EngPremisesAddress:
    """Structured English address referring to a location that can be occupied by persons or organisations within Hong
    Kong.

        Attributes:
            building_name (str | Unset): Full building name in English.
            eng_3_d_address (Eng3DAddress | Unset): Optional English floor and unit information; documented as available
                when `3d=1`.
            eng_block (EngBlock | Unset): Block information of the address in English.
            eng_district (EngDistrict | Unset): District and/or sub-district information in English.
            eng_estate (EngEstate | Unset): Estate name and related information in English.
            eng_lot (EngLot | Unset): Lot information in English. The XML dictionary schema describes either structured lot
                entries or free-text lot lines; those XML choice details are not treated as a JSON guarantee.
            eng_street (EngStreet | Unset): Street name and building number information in English.
            eng_village (EngVillage | Unset): Village name and building number information in English.
            region (EngPremisesAddressRegion | Unset): Region: HK = Hong Kong, KLN = Kowloon, NT = New Territories.
    """

    building_name: str | Unset = UNSET
    eng_3_d_address: Eng3DAddress | Unset = UNSET
    eng_block: EngBlock | Unset = UNSET
    eng_district: EngDistrict | Unset = UNSET
    eng_estate: EngEstate | Unset = UNSET
    eng_lot: EngLot | Unset = UNSET
    eng_street: EngStreet | Unset = UNSET
    eng_village: EngVillage | Unset = UNSET
    region: EngPremisesAddressRegion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        building_name = self.building_name

        eng_3_d_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_3_d_address, Unset):
            eng_3_d_address = self.eng_3_d_address.to_dict()

        eng_block: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_block, Unset):
            eng_block = self.eng_block.to_dict()

        eng_district: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_district, Unset):
            eng_district = self.eng_district.to_dict()

        eng_estate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_estate, Unset):
            eng_estate = self.eng_estate.to_dict()

        eng_lot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_lot, Unset):
            eng_lot = self.eng_lot.to_dict()

        eng_street: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_street, Unset):
            eng_street = self.eng_street.to_dict()

        eng_village: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eng_village, Unset):
            eng_village = self.eng_village.to_dict()

        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if building_name is not UNSET:
            field_dict["BuildingName"] = building_name
        if eng_3_d_address is not UNSET:
            field_dict["Eng3dAddress"] = eng_3_d_address
        if eng_block is not UNSET:
            field_dict["EngBlock"] = eng_block
        if eng_district is not UNSET:
            field_dict["EngDistrict"] = eng_district
        if eng_estate is not UNSET:
            field_dict["EngEstate"] = eng_estate
        if eng_lot is not UNSET:
            field_dict["EngLot"] = eng_lot
        if eng_street is not UNSET:
            field_dict["EngStreet"] = eng_street
        if eng_village is not UNSET:
            field_dict["EngVillage"] = eng_village
        if region is not UNSET:
            field_dict["Region"] = region

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eng_3d_address import Eng3DAddress
        from ..models.eng_block import EngBlock
        from ..models.eng_district import EngDistrict
        from ..models.eng_estate import EngEstate
        from ..models.eng_lot import EngLot
        from ..models.eng_street import EngStreet
        from ..models.eng_village import EngVillage

        d = dict(src_dict)
        building_name = d.pop("BuildingName", UNSET)

        _eng_3_d_address = d.pop("Eng3dAddress", UNSET)
        eng_3_d_address: Eng3DAddress | Unset
        if isinstance(_eng_3_d_address, Unset):
            eng_3_d_address = UNSET
        else:
            eng_3_d_address = Eng3DAddress.from_dict(_eng_3_d_address)

        _eng_block = d.pop("EngBlock", UNSET)
        eng_block: EngBlock | Unset
        if isinstance(_eng_block, Unset):
            eng_block = UNSET
        else:
            eng_block = EngBlock.from_dict(_eng_block)

        _eng_district = d.pop("EngDistrict", UNSET)
        eng_district: EngDistrict | Unset
        if isinstance(_eng_district, Unset):
            eng_district = UNSET
        else:
            eng_district = EngDistrict.from_dict(_eng_district)

        _eng_estate = d.pop("EngEstate", UNSET)
        eng_estate: EngEstate | Unset
        if isinstance(_eng_estate, Unset):
            eng_estate = UNSET
        else:
            eng_estate = EngEstate.from_dict(_eng_estate)

        _eng_lot = d.pop("EngLot", UNSET)
        eng_lot: EngLot | Unset
        if isinstance(_eng_lot, Unset):
            eng_lot = UNSET
        else:
            eng_lot = EngLot.from_dict(_eng_lot)

        _eng_street = d.pop("EngStreet", UNSET)
        eng_street: EngStreet | Unset
        if isinstance(_eng_street, Unset):
            eng_street = UNSET
        else:
            eng_street = EngStreet.from_dict(_eng_street)

        _eng_village = d.pop("EngVillage", UNSET)
        eng_village: EngVillage | Unset
        if isinstance(_eng_village, Unset):
            eng_village = UNSET
        else:
            eng_village = EngVillage.from_dict(_eng_village)

        _region = d.pop("Region", UNSET)
        region: EngPremisesAddressRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = check_eng_premises_address_region(_region)

        eng_premises_address = cls(
            building_name=building_name,
            eng_3_d_address=eng_3_d_address,
            eng_block=eng_block,
            eng_district=eng_district,
            eng_estate=eng_estate,
            eng_lot=eng_lot,
            eng_street=eng_street,
            eng_village=eng_village,
            region=region,
        )

        eng_premises_address.additional_properties = d
        return eng_premises_address

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
