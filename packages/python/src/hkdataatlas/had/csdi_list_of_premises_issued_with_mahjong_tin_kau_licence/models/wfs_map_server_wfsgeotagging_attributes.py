from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        shop_signs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_english (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        address_chinese_tradional (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        address_chinese_simplified (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        northing (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        easting (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    number: None | str | Unset = UNSET
    shop_signs: None | str | Unset = UNSET
    address_english: None | str | Unset = UNSET
    address_chinese_tradional: None | str | Unset = UNSET
    address_chinese_simplified: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number: None | str | Unset
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        shop_signs: None | str | Unset
        if isinstance(self.shop_signs, Unset):
            shop_signs = UNSET
        else:
            shop_signs = self.shop_signs

        address_english: None | str | Unset
        if isinstance(self.address_english, Unset):
            address_english = UNSET
        else:
            address_english = self.address_english

        address_chinese_tradional: None | str | Unset
        if isinstance(self.address_chinese_tradional, Unset):
            address_chinese_tradional = UNSET
        else:
            address_chinese_tradional = self.address_chinese_tradional

        address_chinese_simplified: None | str | Unset
        if isinstance(self.address_chinese_simplified, Unset):
            address_chinese_simplified = UNSET
        else:
            address_chinese_simplified = self.address_chinese_simplified

        northing: None | str | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: None | str | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["Number"] = number
        if shop_signs is not UNSET:
            field_dict["Shop_Signs"] = shop_signs
        if address_english is not UNSET:
            field_dict["Address_English"] = address_english
        if address_chinese_tradional is not UNSET:
            field_dict["Address_Chinese_Tradional"] = address_chinese_tradional
        if address_chinese_simplified is not UNSET:
            field_dict["Address_Chinese_Simplified"] = address_chinese_simplified
        if northing is not UNSET:
            field_dict["northing"] = northing
        if easting is not UNSET:
            field_dict["easting"] = easting
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number = _parse_number(d.pop("Number", UNSET))

        def _parse_shop_signs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shop_signs = _parse_shop_signs(d.pop("Shop_Signs", UNSET))

        def _parse_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_english = _parse_address_english(d.pop("Address_English", UNSET))

        def _parse_address_chinese_tradional(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chinese_tradional = _parse_address_chinese_tradional(
            d.pop("Address_Chinese_Tradional", UNSET)
        )

        def _parse_address_chinese_simplified(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_chinese_simplified = _parse_address_chinese_simplified(
            d.pop("Address_Chinese_Simplified", UNSET)
        )

        def _parse_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        northing = _parse_northing(d.pop("northing", UNSET))

        def _parse_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        easting = _parse_easting(d.pop("easting", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            number=number,
            shop_signs=shop_signs,
            address_english=address_english,
            address_chinese_tradional=address_chinese_tradional,
            address_chinese_simplified=address_chinese_simplified,
            northing=northing,
            easting=easting,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
