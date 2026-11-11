from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeodatastoreAttributes")


@_attrs_define
class WfsMapServerWfsgeodatastoreAttributes:
    """
    Attributes:
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        effective_date_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        effective_date_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        licence_number_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        licence_number_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        type_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        type_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    effective_date_en: None | str | Unset = UNSET
    effective_date_tc: None | str | Unset = UNSET
    licence_number_en: None | str | Unset = UNSET
    licence_number_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    type_en: None | str | Unset = UNSET
    type_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        effective_date_en: None | str | Unset
        if isinstance(self.effective_date_en, Unset):
            effective_date_en = UNSET
        else:
            effective_date_en = self.effective_date_en

        effective_date_tc: None | str | Unset
        if isinstance(self.effective_date_tc, Unset):
            effective_date_tc = UNSET
        else:
            effective_date_tc = self.effective_date_tc

        licence_number_en: None | str | Unset
        if isinstance(self.licence_number_en, Unset):
            licence_number_en = UNSET
        else:
            licence_number_en = self.licence_number_en

        licence_number_tc: None | str | Unset
        if isinstance(self.licence_number_tc, Unset):
            licence_number_tc = UNSET
        else:
            licence_number_tc = self.licence_number_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        type_en: None | str | Unset
        if isinstance(self.type_en, Unset):
            type_en = UNSET
        else:
            type_en = self.type_en

        type_tc: None | str | Unset
        if isinstance(self.type_tc, Unset):
            type_tc = UNSET
        else:
            type_tc = self.type_tc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if effective_date_en is not UNSET:
            field_dict["EffectiveDate_EN"] = effective_date_en
        if effective_date_tc is not UNSET:
            field_dict["EffectiveDate_TC"] = effective_date_tc
        if licence_number_en is not UNSET:
            field_dict["LicenceNumber_EN"] = licence_number_en
        if licence_number_tc is not UNSET:
            field_dict["LicenceNumber_TC"] = licence_number_tc
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if type_en is not UNSET:
            field_dict["TYPE_EN"] = type_en
        if type_tc is not UNSET:
            field_dict["TYPE_TC"] = type_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_effective_date_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        effective_date_en = _parse_effective_date_en(d.pop("EffectiveDate_EN", UNSET))

        def _parse_effective_date_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        effective_date_tc = _parse_effective_date_tc(d.pop("EffectiveDate_TC", UNSET))

        def _parse_licence_number_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        licence_number_en = _parse_licence_number_en(d.pop("LicenceNumber_EN", UNSET))

        def _parse_licence_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        licence_number_tc = _parse_licence_number_tc(d.pop("LicenceNumber_TC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NAME_EN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        def _parse_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_en = _parse_type_en(d.pop("TYPE_EN", UNSET))

        def _parse_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_tc = _parse_type_tc(d.pop("TYPE_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeodatastore_attributes = cls(
            address_en=address_en,
            address_tc=address_tc,
            effective_date_en=effective_date_en,
            effective_date_tc=effective_date_tc,
            licence_number_en=licence_number_en,
            licence_number_tc=licence_number_tc,
            name_en=name_en,
            name_tc=name_tc,
            type_en=type_en,
            type_tc=type_tc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeodatastore_attributes.additional_properties = d
        return wfs_map_server_wfsgeodatastore_attributes

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
