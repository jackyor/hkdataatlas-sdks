from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsSSAAttributes")


@_attrs_define
class WfsMapServerWfsSSAAttributes:
    """
    Attributes:
        name_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_cn (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_cn (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        opening_hours_zh (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        opening_hours_cn (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        opening_hours_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        enquiry_hotline (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    name_zh: None | str | Unset = UNSET
    name_cn: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_zh: None | str | Unset = UNSET
    address_cn: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    opening_hours_zh: None | str | Unset = UNSET
    opening_hours_cn: None | str | Unset = UNSET
    opening_hours_en: None | str | Unset = UNSET
    enquiry_hotline: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_zh: None | str | Unset
        if isinstance(self.name_zh, Unset):
            name_zh = UNSET
        else:
            name_zh = self.name_zh

        name_cn: None | str | Unset
        if isinstance(self.name_cn, Unset):
            name_cn = UNSET
        else:
            name_cn = self.name_cn

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        address_zh: None | str | Unset
        if isinstance(self.address_zh, Unset):
            address_zh = UNSET
        else:
            address_zh = self.address_zh

        address_cn: None | str | Unset
        if isinstance(self.address_cn, Unset):
            address_cn = UNSET
        else:
            address_cn = self.address_cn

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        opening_hours_zh: None | str | Unset
        if isinstance(self.opening_hours_zh, Unset):
            opening_hours_zh = UNSET
        else:
            opening_hours_zh = self.opening_hours_zh

        opening_hours_cn: None | str | Unset
        if isinstance(self.opening_hours_cn, Unset):
            opening_hours_cn = UNSET
        else:
            opening_hours_cn = self.opening_hours_cn

        opening_hours_en: None | str | Unset
        if isinstance(self.opening_hours_en, Unset):
            opening_hours_en = UNSET
        else:
            opening_hours_en = self.opening_hours_en

        enquiry_hotline: None | str | Unset
        if isinstance(self.enquiry_hotline, Unset):
            enquiry_hotline = UNSET
        else:
            enquiry_hotline = self.enquiry_hotline

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_zh is not UNSET:
            field_dict["Name_ZH"] = name_zh
        if name_cn is not UNSET:
            field_dict["Name_CN"] = name_cn
        if name_en is not UNSET:
            field_dict["Name_EN"] = name_en
        if address_zh is not UNSET:
            field_dict["Address_ZH"] = address_zh
        if address_cn is not UNSET:
            field_dict["Address_CN"] = address_cn
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if opening_hours_zh is not UNSET:
            field_dict["Opening_Hours_ZH"] = opening_hours_zh
        if opening_hours_cn is not UNSET:
            field_dict["Opening_Hours_CN"] = opening_hours_cn
        if opening_hours_en is not UNSET:
            field_dict["Opening_Hours_EN"] = opening_hours_en
        if enquiry_hotline is not UNSET:
            field_dict["Enquiry_Hotline"] = enquiry_hotline
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_name_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_zh = _parse_name_zh(d.pop("Name_ZH", UNSET))

        def _parse_name_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_cn = _parse_name_cn(d.pop("Name_CN", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("Name_EN", UNSET))

        def _parse_address_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_zh = _parse_address_zh(d.pop("Address_ZH", UNSET))

        def _parse_address_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_cn = _parse_address_cn(d.pop("Address_CN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_opening_hours_zh(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_zh = _parse_opening_hours_zh(d.pop("Opening_Hours_ZH", UNSET))

        def _parse_opening_hours_cn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_cn = _parse_opening_hours_cn(d.pop("Opening_Hours_CN", UNSET))

        def _parse_opening_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_en = _parse_opening_hours_en(d.pop("Opening_Hours_EN", UNSET))

        def _parse_enquiry_hotline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        enquiry_hotline = _parse_enquiry_hotline(d.pop("Enquiry_Hotline", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_ssa_attributes = cls(
            name_zh=name_zh,
            name_cn=name_cn,
            name_en=name_en,
            address_zh=address_zh,
            address_cn=address_cn,
            address_en=address_en,
            opening_hours_zh=opening_hours_zh,
            opening_hours_cn=opening_hours_cn,
            opening_hours_en=opening_hours_en,
            enquiry_hotline=enquiry_hotline,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_ssa_attributes.additional_properties = d
        return wfs_map_server_wfs_ssa_attributes

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
