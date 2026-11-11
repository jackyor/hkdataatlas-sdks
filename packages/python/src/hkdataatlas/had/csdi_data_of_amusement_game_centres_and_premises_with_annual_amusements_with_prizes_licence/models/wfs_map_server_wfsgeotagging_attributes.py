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
        type_ (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        licence_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        centre_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        centre_name_zh_hant (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        centre_name_zh_hans (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_zh_hant (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        address_zh_hans (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        phone (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    type_: None | str | Unset = UNSET
    licence_no: None | str | Unset = UNSET
    centre_name_en: None | str | Unset = UNSET
    centre_name_zh_hant: None | str | Unset = UNSET
    centre_name_zh_hans: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_zh_hant: None | str | Unset = UNSET
    address_zh_hans: None | str | Unset = UNSET
    phone: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        licence_no: None | str | Unset
        if isinstance(self.licence_no, Unset):
            licence_no = UNSET
        else:
            licence_no = self.licence_no

        centre_name_en: None | str | Unset
        if isinstance(self.centre_name_en, Unset):
            centre_name_en = UNSET
        else:
            centre_name_en = self.centre_name_en

        centre_name_zh_hant: None | str | Unset
        if isinstance(self.centre_name_zh_hant, Unset):
            centre_name_zh_hant = UNSET
        else:
            centre_name_zh_hant = self.centre_name_zh_hant

        centre_name_zh_hans: None | str | Unset
        if isinstance(self.centre_name_zh_hans, Unset):
            centre_name_zh_hans = UNSET
        else:
            centre_name_zh_hans = self.centre_name_zh_hans

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_zh_hant: None | str | Unset
        if isinstance(self.address_zh_hant, Unset):
            address_zh_hant = UNSET
        else:
            address_zh_hant = self.address_zh_hant

        address_zh_hans: None | str | Unset
        if isinstance(self.address_zh_hans, Unset):
            address_zh_hans = UNSET
        else:
            address_zh_hans = self.address_zh_hans

        phone: None | str | Unset
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["Type"] = type_
        if licence_no is not UNSET:
            field_dict["Licence_No"] = licence_no
        if centre_name_en is not UNSET:
            field_dict["Centre_Name_EN"] = centre_name_en
        if centre_name_zh_hant is not UNSET:
            field_dict["Centre_Name_ZH_HANT"] = centre_name_zh_hant
        if centre_name_zh_hans is not UNSET:
            field_dict["Centre_Name_ZH_HANS"] = centre_name_zh_hans
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_zh_hant is not UNSET:
            field_dict["Address_ZH_HANT"] = address_zh_hant
        if address_zh_hans is not UNSET:
            field_dict["Address_ZH_HANS"] = address_zh_hans
        if phone is not UNSET:
            field_dict["Phone"] = phone
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("Type", UNSET))

        def _parse_licence_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        licence_no = _parse_licence_no(d.pop("Licence_No", UNSET))

        def _parse_centre_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        centre_name_en = _parse_centre_name_en(d.pop("Centre_Name_EN", UNSET))

        def _parse_centre_name_zh_hant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        centre_name_zh_hant = _parse_centre_name_zh_hant(
            d.pop("Centre_Name_ZH_HANT", UNSET)
        )

        def _parse_centre_name_zh_hans(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        centre_name_zh_hans = _parse_centre_name_zh_hans(
            d.pop("Centre_Name_ZH_HANS", UNSET)
        )

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_zh_hant(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_zh_hant = _parse_address_zh_hant(d.pop("Address_ZH_HANT", UNSET))

        def _parse_address_zh_hans(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_zh_hans = _parse_address_zh_hans(d.pop("Address_ZH_HANS", UNSET))

        def _parse_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone = _parse_phone(d.pop("Phone", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            type_=type_,
            licence_no=licence_no,
            centre_name_en=centre_name_en,
            centre_name_zh_hant=centre_name_zh_hant,
            centre_name_zh_hans=centre_name_zh_hans,
            address_en=address_en,
            address_zh_hant=address_zh_hant,
            address_zh_hans=address_zh_hans,
            phone=phone,
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
