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
        local_address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        local_address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        principle_address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        principle_address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        secstaff_reg_url_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        secstaff_reg_url_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        type_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        type_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    local_address_en: None | str | Unset = UNSET
    local_address_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    principle_address_en: None | str | Unset = UNSET
    principle_address_tc: None | str | Unset = UNSET
    secstaff_reg_url_en: None | str | Unset = UNSET
    secstaff_reg_url_tc: None | str | Unset = UNSET
    type_en: None | str | Unset = UNSET
    type_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_address_en: None | str | Unset
        if isinstance(self.local_address_en, Unset):
            local_address_en = UNSET
        else:
            local_address_en = self.local_address_en

        local_address_tc: None | str | Unset
        if isinstance(self.local_address_tc, Unset):
            local_address_tc = UNSET
        else:
            local_address_tc = self.local_address_tc

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

        principle_address_en: None | str | Unset
        if isinstance(self.principle_address_en, Unset):
            principle_address_en = UNSET
        else:
            principle_address_en = self.principle_address_en

        principle_address_tc: None | str | Unset
        if isinstance(self.principle_address_tc, Unset):
            principle_address_tc = UNSET
        else:
            principle_address_tc = self.principle_address_tc

        secstaff_reg_url_en: None | str | Unset
        if isinstance(self.secstaff_reg_url_en, Unset):
            secstaff_reg_url_en = UNSET
        else:
            secstaff_reg_url_en = self.secstaff_reg_url_en

        secstaff_reg_url_tc: None | str | Unset
        if isinstance(self.secstaff_reg_url_tc, Unset):
            secstaff_reg_url_tc = UNSET
        else:
            secstaff_reg_url_tc = self.secstaff_reg_url_tc

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
        if local_address_en is not UNSET:
            field_dict["LocalAddress_EN"] = local_address_en
        if local_address_tc is not UNSET:
            field_dict["LocalAddress_TC"] = local_address_tc
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if principle_address_en is not UNSET:
            field_dict["PrincipleAddress_EN"] = principle_address_en
        if principle_address_tc is not UNSET:
            field_dict["PrincipleAddress_TC"] = principle_address_tc
        if secstaff_reg_url_en is not UNSET:
            field_dict["SecstaffRegURL_EN"] = secstaff_reg_url_en
        if secstaff_reg_url_tc is not UNSET:
            field_dict["SecstaffRegURL_TC"] = secstaff_reg_url_tc
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

        def _parse_local_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_address_en = _parse_local_address_en(d.pop("LocalAddress_EN", UNSET))

        def _parse_local_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_address_tc = _parse_local_address_tc(d.pop("LocalAddress_TC", UNSET))

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

        def _parse_principle_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principle_address_en = _parse_principle_address_en(
            d.pop("PrincipleAddress_EN", UNSET)
        )

        def _parse_principle_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        principle_address_tc = _parse_principle_address_tc(
            d.pop("PrincipleAddress_TC", UNSET)
        )

        def _parse_secstaff_reg_url_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secstaff_reg_url_en = _parse_secstaff_reg_url_en(
            d.pop("SecstaffRegURL_EN", UNSET)
        )

        def _parse_secstaff_reg_url_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secstaff_reg_url_tc = _parse_secstaff_reg_url_tc(
            d.pop("SecstaffRegURL_TC", UNSET)
        )

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
            local_address_en=local_address_en,
            local_address_tc=local_address_tc,
            name_en=name_en,
            name_tc=name_tc,
            principle_address_en=principle_address_en,
            principle_address_tc=principle_address_tc,
            secstaff_reg_url_en=secstaff_reg_url_en,
            secstaff_reg_url_tc=secstaff_reg_url_tc,
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
