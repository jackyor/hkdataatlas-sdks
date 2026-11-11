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
        name (None | str | Unset): Publisher field type: esriFieldTypeString
        chinese_name (None | str | Unset): Publisher field type: esriFieldTypeString
        address (None | str | Unset): Publisher field type: esriFieldTypeString
        address_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        visit_time (None | str | Unset): Publisher field type: esriFieldTypeString
        visit_time_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        participant_age (None | str | Unset): Publisher field type: esriFieldTypeString
        participant_no (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    name: None | str | Unset = UNSET
    chinese_name: None | str | Unset = UNSET
    address: None | str | Unset = UNSET
    address_chinese: None | str | Unset = UNSET
    visit_time: None | str | Unset = UNSET
    visit_time_chinese: None | str | Unset = UNSET
    participant_age: None | str | Unset = UNSET
    participant_no: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        chinese_name: None | str | Unset
        if isinstance(self.chinese_name, Unset):
            chinese_name = UNSET
        else:
            chinese_name = self.chinese_name

        address: None | str | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        address_chinese: None | str | Unset
        if isinstance(self.address_chinese, Unset):
            address_chinese = UNSET
        else:
            address_chinese = self.address_chinese

        visit_time: None | str | Unset
        if isinstance(self.visit_time, Unset):
            visit_time = UNSET
        else:
            visit_time = self.visit_time

        visit_time_chinese: None | str | Unset
        if isinstance(self.visit_time_chinese, Unset):
            visit_time_chinese = UNSET
        else:
            visit_time_chinese = self.visit_time_chinese

        participant_age: None | str | Unset
        if isinstance(self.participant_age, Unset):
            participant_age = UNSET
        else:
            participant_age = self.participant_age

        participant_no: None | str | Unset
        if isinstance(self.participant_no, Unset):
            participant_no = UNSET
        else:
            participant_no = self.participant_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if name is not UNSET:
            field_dict["NAME"] = name
        if chinese_name is not UNSET:
            field_dict["CHINESE_NAME"] = chinese_name
        if address is not UNSET:
            field_dict["ADDRESS"] = address
        if address_chinese is not UNSET:
            field_dict["ADDRESS_CHINESE"] = address_chinese
        if visit_time is not UNSET:
            field_dict["VISIT_TIME"] = visit_time
        if visit_time_chinese is not UNSET:
            field_dict["VISIT_TIME_CHINESE"] = visit_time_chinese
        if participant_age is not UNSET:
            field_dict["PARTICIPANT_AGE"] = participant_age
        if participant_no is not UNSET:
            field_dict["PARTICIPANT_NO"] = participant_no

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("NAME", UNSET))

        def _parse_chinese_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_name = _parse_chinese_name(d.pop("CHINESE_NAME", UNSET))

        def _parse_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address = _parse_address(d.pop("ADDRESS", UNSET))

        def _parse_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chinese = _parse_address_chinese(d.pop("ADDRESS_CHINESE", UNSET))

        def _parse_visit_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visit_time = _parse_visit_time(d.pop("VISIT_TIME", UNSET))

        def _parse_visit_time_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visit_time_chinese = _parse_visit_time_chinese(
            d.pop("VISIT_TIME_CHINESE", UNSET)
        )

        def _parse_participant_age(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        participant_age = _parse_participant_age(d.pop("PARTICIPANT_AGE", UNSET))

        def _parse_participant_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        participant_no = _parse_participant_no(d.pop("PARTICIPANT_NO", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            name=name,
            chinese_name=chinese_name,
            address=address,
            address_chinese=address_chinese,
            visit_time=visit_time,
            visit_time_chinese=visit_time_chinese,
            participant_age=participant_age,
            participant_no=participant_no,
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
