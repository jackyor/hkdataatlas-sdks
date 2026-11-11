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
        address_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        address_english (None | str | Unset): Publisher field type: esriFieldTypeString
        lift_no (None | str | Unset): Publisher field type: esriFieldTypeString
        location_id (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_lift_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_lift_english (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_chinese: None | str | Unset = UNSET
    address_english: None | str | Unset = UNSET
    lift_no: None | str | Unset = UNSET
    location_id: None | str | Unset = UNSET
    type_of_lift_chinese: None | str | Unset = UNSET
    type_of_lift_english: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_chinese: None | str | Unset
        if isinstance(self.address_chinese, Unset):
            address_chinese = UNSET
        else:
            address_chinese = self.address_chinese

        address_english: None | str | Unset
        if isinstance(self.address_english, Unset):
            address_english = UNSET
        else:
            address_english = self.address_english

        lift_no: None | str | Unset
        if isinstance(self.lift_no, Unset):
            lift_no = UNSET
        else:
            lift_no = self.lift_no

        location_id: None | str | Unset
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        type_of_lift_chinese: None | str | Unset
        if isinstance(self.type_of_lift_chinese, Unset):
            type_of_lift_chinese = UNSET
        else:
            type_of_lift_chinese = self.type_of_lift_chinese

        type_of_lift_english: None | str | Unset
        if isinstance(self.type_of_lift_english, Unset):
            type_of_lift_english = UNSET
        else:
            type_of_lift_english = self.type_of_lift_english

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_chinese is not UNSET:
            field_dict["Address_Chinese"] = address_chinese
        if address_english is not UNSET:
            field_dict["Address_English"] = address_english
        if lift_no is not UNSET:
            field_dict["Lift_No"] = lift_no
        if location_id is not UNSET:
            field_dict["Location_ID"] = location_id
        if type_of_lift_chinese is not UNSET:
            field_dict["Type_of_Lift_Chinese"] = type_of_lift_chinese
        if type_of_lift_english is not UNSET:
            field_dict["Type_of_Lift_English"] = type_of_lift_english
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chinese = _parse_address_chinese(d.pop("Address_Chinese", UNSET))

        def _parse_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_english = _parse_address_english(d.pop("Address_English", UNSET))

        def _parse_lift_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lift_no = _parse_lift_no(d.pop("Lift_No", UNSET))

        def _parse_location_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_id = _parse_location_id(d.pop("Location_ID", UNSET))

        def _parse_type_of_lift_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_lift_chinese = _parse_type_of_lift_chinese(
            d.pop("Type_of_Lift_Chinese", UNSET)
        )

        def _parse_type_of_lift_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_lift_english = _parse_type_of_lift_english(
            d.pop("Type_of_Lift_English", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_chinese=address_chinese,
            address_english=address_english,
            lift_no=lift_no,
            location_id=location_id,
            type_of_lift_chinese=type_of_lift_chinese,
            type_of_lift_english=type_of_lift_english,
            objectid=objectid,
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
