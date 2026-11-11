from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfskiddieridesAttributes")


@_attrs_define
class WfsMapServerWfskiddieridesAttributes:
    """
    Attributes:
        address_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        address_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        category (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        location_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        name_chinese (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_chinese: None | str | Unset = UNSET
    address_english: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    location_number: None | str | Unset = UNSET
    name_chinese: None | str | Unset = UNSET
    name_english: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
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

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        location_number: None | str | Unset
        if isinstance(self.location_number, Unset):
            location_number = UNSET
        else:
            location_number = self.location_number

        name_chinese: None | str | Unset
        if isinstance(self.name_chinese, Unset):
            name_chinese = UNSET
        else:
            name_chinese = self.name_chinese

        name_english: None | str | Unset
        if isinstance(self.name_english, Unset):
            name_english = UNSET
        else:
            name_english = self.name_english

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_chinese is not UNSET:
            field_dict["Address_Chinese"] = address_chinese
        if address_english is not UNSET:
            field_dict["Address_English"] = address_english
        if category is not UNSET:
            field_dict["Category"] = category
        if location_number is not UNSET:
            field_dict["Location_Number"] = location_number
        if name_chinese is not UNSET:
            field_dict["Name_Chinese"] = name_chinese
        if name_english is not UNSET:
            field_dict["Name_English"] = name_english
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

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

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("Category", UNSET))

        def _parse_location_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_number = _parse_location_number(d.pop("Location_Number", UNSET))

        def _parse_name_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_chinese = _parse_name_chinese(d.pop("Name_Chinese", UNSET))

        def _parse_name_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_english = _parse_name_english(d.pop("Name_English", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfskiddierides_attributes = cls(
            address_chinese=address_chinese,
            address_english=address_english,
            category=category,
            location_number=location_number,
            name_chinese=name_chinese,
            name_english=name_english,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfskiddierides_attributes.additional_properties = d
        return wfs_map_server_wfskiddierides_attributes

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
