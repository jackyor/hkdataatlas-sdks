from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """Address fields in the requested locale. The dictionary uses the spelling dcDestrict; the detailed response sample
    uses dcDistrict.

        Attributes:
            block_descriptor (str | Unset):
            block_no (str | Unset):
            building_name (str | Unset):
            building_no (str | Unset):
            dc_destrict (str | Unset):
            dc_district (str | Unset):
            display_address (str | Unset):
            estate_name (str | Unset):
            floor (str | Unset):
            phase (str | Unset):
            region (str | Unset):
            street_name (str | Unset):
            sub_district (str | Unset):
            unit_descriptor (str | Unset):
            unit_no (str | Unset):
            village_name (str | Unset):
    """

    block_descriptor: str | Unset = UNSET
    block_no: str | Unset = UNSET
    building_name: str | Unset = UNSET
    building_no: str | Unset = UNSET
    dc_destrict: str | Unset = UNSET
    dc_district: str | Unset = UNSET
    display_address: str | Unset = UNSET
    estate_name: str | Unset = UNSET
    floor: str | Unset = UNSET
    phase: str | Unset = UNSET
    region: str | Unset = UNSET
    street_name: str | Unset = UNSET
    sub_district: str | Unset = UNSET
    unit_descriptor: str | Unset = UNSET
    unit_no: str | Unset = UNSET
    village_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_descriptor = self.block_descriptor

        block_no = self.block_no

        building_name = self.building_name

        building_no = self.building_no

        dc_destrict = self.dc_destrict

        dc_district = self.dc_district

        display_address = self.display_address

        estate_name = self.estate_name

        floor = self.floor

        phase = self.phase

        region = self.region

        street_name = self.street_name

        sub_district = self.sub_district

        unit_descriptor = self.unit_descriptor

        unit_no = self.unit_no

        village_name = self.village_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if block_descriptor is not UNSET:
            field_dict["blockDescriptor"] = block_descriptor
        if block_no is not UNSET:
            field_dict["blockNo"] = block_no
        if building_name is not UNSET:
            field_dict["buildingName"] = building_name
        if building_no is not UNSET:
            field_dict["buildingNo"] = building_no
        if dc_destrict is not UNSET:
            field_dict["dcDestrict"] = dc_destrict
        if dc_district is not UNSET:
            field_dict["dcDistrict"] = dc_district
        if display_address is not UNSET:
            field_dict["displayAddress"] = display_address
        if estate_name is not UNSET:
            field_dict["estateName"] = estate_name
        if floor is not UNSET:
            field_dict["floor"] = floor
        if phase is not UNSET:
            field_dict["phase"] = phase
        if region is not UNSET:
            field_dict["region"] = region
        if street_name is not UNSET:
            field_dict["streetName"] = street_name
        if sub_district is not UNSET:
            field_dict["subDistrict"] = sub_district
        if unit_descriptor is not UNSET:
            field_dict["unitDescriptor"] = unit_descriptor
        if unit_no is not UNSET:
            field_dict["unitNo"] = unit_no
        if village_name is not UNSET:
            field_dict["villageName"] = village_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        block_descriptor = d.pop("blockDescriptor", UNSET)

        block_no = d.pop("blockNo", UNSET)

        building_name = d.pop("buildingName", UNSET)

        building_no = d.pop("buildingNo", UNSET)

        dc_destrict = d.pop("dcDestrict", UNSET)

        dc_district = d.pop("dcDistrict", UNSET)

        display_address = d.pop("displayAddress", UNSET)

        estate_name = d.pop("estateName", UNSET)

        floor = d.pop("floor", UNSET)

        phase = d.pop("phase", UNSET)

        region = d.pop("region", UNSET)

        street_name = d.pop("streetName", UNSET)

        sub_district = d.pop("subDistrict", UNSET)

        unit_descriptor = d.pop("unitDescriptor", UNSET)

        unit_no = d.pop("unitNo", UNSET)

        village_name = d.pop("villageName", UNSET)

        address = cls(
            block_descriptor=block_descriptor,
            block_no=block_no,
            building_name=building_name,
            building_no=building_no,
            dc_destrict=dc_destrict,
            dc_district=dc_district,
            display_address=display_address,
            estate_name=estate_name,
            floor=floor,
            phase=phase,
            region=region,
            street_name=street_name,
            sub_district=sub_district,
            unit_descriptor=unit_descriptor,
            unit_no=unit_no,
            village_name=village_name,
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
