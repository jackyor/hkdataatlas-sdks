from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        project_english_name (None | str | Unset): Publisher field type: esriFieldTypeString
        project_chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        district_english_name (None | str | Unset): Publisher field type: esriFieldTypeString
        district_chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        region_english_name (None | str | Unset): Publisher field type: esriFieldTypeString
        region_chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        english_name_of_block (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_name_of_block (None | str | Unset): Publisher field type: esriFieldTypeString
        unit_number (None | str | Unset): Publisher field type: esriFieldTypeString
        floor_number (None | str | Unset): Publisher field type: esriFieldTypeString
        internal_floor_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        avail_of_elevator_services (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    project_english_name: None | str | Unset = UNSET
    project_chinese_name: None | str | Unset = UNSET
    district_english_name: None | str | Unset = UNSET
    district_chinese_name: None | str | Unset = UNSET
    region_english_name: None | str | Unset = UNSET
    region_chinese_name: None | str | Unset = UNSET
    english_name_of_block: None | str | Unset = UNSET
    chinese_name_of_block: None | str | Unset = UNSET
    unit_number: None | str | Unset = UNSET
    floor_number: None | str | Unset = UNSET
    internal_floor_area: float | None | Unset = UNSET
    avail_of_elevator_services: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        project_english_name: None | str | Unset
        if isinstance(self.project_english_name, Unset):
            project_english_name = UNSET
        else:
            project_english_name = self.project_english_name

        project_chinese_name: None | str | Unset
        if isinstance(self.project_chinese_name, Unset):
            project_chinese_name = UNSET
        else:
            project_chinese_name = self.project_chinese_name

        district_english_name: None | str | Unset
        if isinstance(self.district_english_name, Unset):
            district_english_name = UNSET
        else:
            district_english_name = self.district_english_name

        district_chinese_name: None | str | Unset
        if isinstance(self.district_chinese_name, Unset):
            district_chinese_name = UNSET
        else:
            district_chinese_name = self.district_chinese_name

        region_english_name: None | str | Unset
        if isinstance(self.region_english_name, Unset):
            region_english_name = UNSET
        else:
            region_english_name = self.region_english_name

        region_chinese_name: None | str | Unset
        if isinstance(self.region_chinese_name, Unset):
            region_chinese_name = UNSET
        else:
            region_chinese_name = self.region_chinese_name

        english_name_of_block: None | str | Unset
        if isinstance(self.english_name_of_block, Unset):
            english_name_of_block = UNSET
        else:
            english_name_of_block = self.english_name_of_block

        chinese_name_of_block: None | str | Unset
        if isinstance(self.chinese_name_of_block, Unset):
            chinese_name_of_block = UNSET
        else:
            chinese_name_of_block = self.chinese_name_of_block

        unit_number: None | str | Unset
        if isinstance(self.unit_number, Unset):
            unit_number = UNSET
        else:
            unit_number = self.unit_number

        floor_number: None | str | Unset
        if isinstance(self.floor_number, Unset):
            floor_number = UNSET
        else:
            floor_number = self.floor_number

        internal_floor_area: float | None | Unset
        if isinstance(self.internal_floor_area, Unset):
            internal_floor_area = UNSET
        else:
            internal_floor_area = self.internal_floor_area

        avail_of_elevator_services: None | str | Unset
        if isinstance(self.avail_of_elevator_services, Unset):
            avail_of_elevator_services = UNSET
        else:
            avail_of_elevator_services = self.avail_of_elevator_services

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
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
        if internal_floor_area is not UNSET:
            field_dict["internal_floor_area"] = internal_floor_area
        if avail_of_elevator_services is not UNSET:
            field_dict["avail_of_elevator_services"] = avail_of_elevator_services

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_project_english_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_english_name = _parse_project_english_name(
            d.pop("project_english_name", UNSET)
        )

        def _parse_project_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_chinese_name = _parse_project_chinese_name(
            d.pop("project_chinese_name", UNSET)
        )

        def _parse_district_english_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_english_name = _parse_district_english_name(
            d.pop("district_english_name", UNSET)
        )

        def _parse_district_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_chinese_name = _parse_district_chinese_name(
            d.pop("district_chinese_name", UNSET)
        )

        def _parse_region_english_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_english_name = _parse_region_english_name(
            d.pop("region_english_name", UNSET)
        )

        def _parse_region_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_chinese_name = _parse_region_chinese_name(
            d.pop("region_chinese_name", UNSET)
        )

        def _parse_english_name_of_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_name_of_block = _parse_english_name_of_block(
            d.pop("english_name_of_block", UNSET)
        )

        def _parse_chinese_name_of_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name_of_block = _parse_chinese_name_of_block(
            d.pop("chinese_name_of_block", UNSET)
        )

        def _parse_unit_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_number = _parse_unit_number(d.pop("unit_number", UNSET))

        def _parse_floor_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        floor_number = _parse_floor_number(d.pop("floor_number", UNSET))

        def _parse_internal_floor_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        internal_floor_area = _parse_internal_floor_area(
            d.pop("internal_floor_area", UNSET)
        )

        def _parse_avail_of_elevator_services(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avail_of_elevator_services = _parse_avail_of_elevator_services(
            d.pop("avail_of_elevator_services", UNSET)
        )

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
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
            internal_floor_area=internal_floor_area,
            avail_of_elevator_services=avail_of_elevator_services,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
