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
        location_id (None | str | Unset): Publisher field type: esriFieldTypeString
        lt_esc_no (None | str | Unset): Publisher field type: esriFieldTypeString
        statutory_orders_or_notices (None | str | Unset): Publisher field type: esriFieldTypeString
        type_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        type_english (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_chinese: None | str | Unset = UNSET
    address_english: None | str | Unset = UNSET
    location_id: None | str | Unset = UNSET
    lt_esc_no: None | str | Unset = UNSET
    statutory_orders_or_notices: None | str | Unset = UNSET
    type_chinese: None | str | Unset = UNSET
    type_english: None | str | Unset = UNSET
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

        location_id: None | str | Unset
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        lt_esc_no: None | str | Unset
        if isinstance(self.lt_esc_no, Unset):
            lt_esc_no = UNSET
        else:
            lt_esc_no = self.lt_esc_no

        statutory_orders_or_notices: None | str | Unset
        if isinstance(self.statutory_orders_or_notices, Unset):
            statutory_orders_or_notices = UNSET
        else:
            statutory_orders_or_notices = self.statutory_orders_or_notices

        type_chinese: None | str | Unset
        if isinstance(self.type_chinese, Unset):
            type_chinese = UNSET
        else:
            type_chinese = self.type_chinese

        type_english: None | str | Unset
        if isinstance(self.type_english, Unset):
            type_english = UNSET
        else:
            type_english = self.type_english

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_chinese is not UNSET:
            field_dict["Address_Chinese"] = address_chinese
        if address_english is not UNSET:
            field_dict["Address_English"] = address_english
        if location_id is not UNSET:
            field_dict["Location_ID"] = location_id
        if lt_esc_no is not UNSET:
            field_dict["Lt_Esc_No"] = lt_esc_no
        if statutory_orders_or_notices is not UNSET:
            field_dict["Statutory_Orders_or_Notices"] = statutory_orders_or_notices
        if type_chinese is not UNSET:
            field_dict["Type_Chinese"] = type_chinese
        if type_english is not UNSET:
            field_dict["Type_English"] = type_english
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

        def _parse_location_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_id = _parse_location_id(d.pop("Location_ID", UNSET))

        def _parse_lt_esc_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lt_esc_no = _parse_lt_esc_no(d.pop("Lt_Esc_No", UNSET))

        def _parse_statutory_orders_or_notices(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        statutory_orders_or_notices = _parse_statutory_orders_or_notices(
            d.pop("Statutory_Orders_or_Notices", UNSET)
        )

        def _parse_type_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_chinese = _parse_type_chinese(d.pop("Type_Chinese", UNSET))

        def _parse_type_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_english = _parse_type_english(d.pop("Type_English", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_chinese=address_chinese,
            address_english=address_english,
            location_id=location_id,
            lt_esc_no=lt_esc_no,
            statutory_orders_or_notices=statutory_orders_or_notices,
            type_chinese=type_chinese,
            type_english=type_english,
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
