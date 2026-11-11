from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LightPublicHousingRecord")


@_attrs_define
class LightPublicHousingRecord:
    """Dictionary fields; current export number-or-string alternatives retained without coercion.

    Attributes:
        project_english_name (str | Unset):
        project_chinese_name (str | Unset):
        district_english_name (str | Unset):
        district_chinese_name (str | Unset):
        region_english_name (str | Unset):
        region_chinese_name (str | Unset):
        english_name_of_block (str | Unset):
        chinese_name_of_block (str | Unset):
        unit_number (str | Unset):
        floor_number (str | Unset):
        avail_of_elevator_services (str | Unset):
        internal_floor_area (float | str | Unset): Publisher dictionary specifies a number; retained current export
            encodes a string. No lexical or range constraint inferred.
        project_map_latitude (float | str | Unset): Publisher dictionary specifies a number; retained current export
            encodes a string. No lexical or range constraint inferred.
        project_map_longitude (float | str | Unset): Publisher dictionary specifies a number; retained current export
            encodes a string. No lexical or range constraint inferred.
    """

    project_english_name: str | Unset = UNSET
    project_chinese_name: str | Unset = UNSET
    district_english_name: str | Unset = UNSET
    district_chinese_name: str | Unset = UNSET
    region_english_name: str | Unset = UNSET
    region_chinese_name: str | Unset = UNSET
    english_name_of_block: str | Unset = UNSET
    chinese_name_of_block: str | Unset = UNSET
    unit_number: str | Unset = UNSET
    floor_number: str | Unset = UNSET
    avail_of_elevator_services: str | Unset = UNSET
    internal_floor_area: float | str | Unset = UNSET
    project_map_latitude: float | str | Unset = UNSET
    project_map_longitude: float | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_english_name = self.project_english_name

        project_chinese_name = self.project_chinese_name

        district_english_name = self.district_english_name

        district_chinese_name = self.district_chinese_name

        region_english_name = self.region_english_name

        region_chinese_name = self.region_chinese_name

        english_name_of_block = self.english_name_of_block

        chinese_name_of_block = self.chinese_name_of_block

        unit_number = self.unit_number

        floor_number = self.floor_number

        avail_of_elevator_services = self.avail_of_elevator_services

        internal_floor_area: float | str | Unset
        if isinstance(self.internal_floor_area, Unset):
            internal_floor_area = UNSET
        else:
            internal_floor_area = self.internal_floor_area

        project_map_latitude: float | str | Unset
        if isinstance(self.project_map_latitude, Unset):
            project_map_latitude = UNSET
        else:
            project_map_latitude = self.project_map_latitude

        project_map_longitude: float | str | Unset
        if isinstance(self.project_map_longitude, Unset):
            project_map_longitude = UNSET
        else:
            project_map_longitude = self.project_map_longitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_english_name is not UNSET:
            field_dict["project_english_name"] = project_english_name
        if project_chinese_name is not UNSET:
            field_dict["project_chinese_name"] = project_chinese_name
        if district_english_name is not UNSET:
            field_dict["district_english_name"] = district_english_name
        if district_chinese_name is not UNSET:
            field_dict["district_chinese_name"] = district_chinese_name
        if region_english_name is not UNSET:
            field_dict["region_english_name"] = region_english_name
        if region_chinese_name is not UNSET:
            field_dict["region_chinese_name"] = region_chinese_name
        if english_name_of_block is not UNSET:
            field_dict["english_name_of_block"] = english_name_of_block
        if chinese_name_of_block is not UNSET:
            field_dict["chinese_name_of_block"] = chinese_name_of_block
        if unit_number is not UNSET:
            field_dict["unit_number"] = unit_number
        if floor_number is not UNSET:
            field_dict["floor_number"] = floor_number
        if avail_of_elevator_services is not UNSET:
            field_dict["avail_of_elevator_services"] = avail_of_elevator_services
        if internal_floor_area is not UNSET:
            field_dict["internal_floor_area"] = internal_floor_area
        if project_map_latitude is not UNSET:
            field_dict["project_map_latitude"] = project_map_latitude
        if project_map_longitude is not UNSET:
            field_dict["project_map_longitude"] = project_map_longitude

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        project_english_name = d.pop("project_english_name", UNSET)

        project_chinese_name = d.pop("project_chinese_name", UNSET)

        district_english_name = d.pop("district_english_name", UNSET)

        district_chinese_name = d.pop("district_chinese_name", UNSET)

        region_english_name = d.pop("region_english_name", UNSET)

        region_chinese_name = d.pop("region_chinese_name", UNSET)

        english_name_of_block = d.pop("english_name_of_block", UNSET)

        chinese_name_of_block = d.pop("chinese_name_of_block", UNSET)

        unit_number = d.pop("unit_number", UNSET)

        floor_number = d.pop("floor_number", UNSET)

        avail_of_elevator_services = d.pop("avail_of_elevator_services", UNSET)

        def _parse_internal_floor_area(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        internal_floor_area = _parse_internal_floor_area(
            d.pop("internal_floor_area", UNSET)
        )

        def _parse_project_map_latitude(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        project_map_latitude = _parse_project_map_latitude(
            d.pop("project_map_latitude", UNSET)
        )

        def _parse_project_map_longitude(data: object) -> float | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset, data)

        project_map_longitude = _parse_project_map_longitude(
            d.pop("project_map_longitude", UNSET)
        )

        light_public_housing_record = cls(
            project_english_name=project_english_name,
            project_chinese_name=project_chinese_name,
            district_english_name=district_english_name,
            district_chinese_name=district_chinese_name,
            region_english_name=region_english_name,
            region_chinese_name=region_chinese_name,
            english_name_of_block=english_name_of_block,
            chinese_name_of_block=chinese_name_of_block,
            unit_number=unit_number,
            floor_number=floor_number,
            avail_of_elevator_services=avail_of_elevator_services,
            internal_floor_area=internal_floor_area,
            project_map_latitude=project_map_latitude,
            project_map_longitude=project_map_longitude,
        )

        light_public_housing_record.additional_properties = d
        return light_public_housing_record

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
