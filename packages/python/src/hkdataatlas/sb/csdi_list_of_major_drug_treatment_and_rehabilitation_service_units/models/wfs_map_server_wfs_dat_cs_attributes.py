from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsDATCsAttributes")


@_attrs_define
class WfsMapServerWfsDATCsAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        add_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        add_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        add_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        tel (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        website_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        website_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        website_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    add_en: None | str | Unset = UNSET
    add_tc: None | str | Unset = UNSET
    add_sc: None | str | Unset = UNSET
    tel: None | str | Unset = UNSET
    website_en: None | str | Unset = UNSET
    website_tc: None | str | Unset = UNSET
    website_sc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

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

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        add_en: None | str | Unset
        if isinstance(self.add_en, Unset):
            add_en = UNSET
        else:
            add_en = self.add_en

        add_tc: None | str | Unset
        if isinstance(self.add_tc, Unset):
            add_tc = UNSET
        else:
            add_tc = self.add_tc

        add_sc: None | str | Unset
        if isinstance(self.add_sc, Unset):
            add_sc = UNSET
        else:
            add_sc = self.add_sc

        tel: None | str | Unset
        if isinstance(self.tel, Unset):
            tel = UNSET
        else:
            tel = self.tel

        website_en: None | str | Unset
        if isinstance(self.website_en, Unset):
            website_en = UNSET
        else:
            website_en = self.website_en

        website_tc: None | str | Unset
        if isinstance(self.website_tc, Unset):
            website_tc = UNSET
        else:
            website_tc = self.website_tc

        website_sc: None | str | Unset
        if isinstance(self.website_sc, Unset):
            website_sc = UNSET
        else:
            website_sc = self.website_sc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if name_en is not UNSET:
            field_dict["name_en"] = name_en
        if name_tc is not UNSET:
            field_dict["name_tc"] = name_tc
        if name_sc is not UNSET:
            field_dict["name_sc"] = name_sc
        if add_en is not UNSET:
            field_dict["add_en"] = add_en
        if add_tc is not UNSET:
            field_dict["add_tc"] = add_tc
        if add_sc is not UNSET:
            field_dict["add_sc"] = add_sc
        if tel is not UNSET:
            field_dict["tel"] = tel
        if website_en is not UNSET:
            field_dict["website_en"] = website_en
        if website_tc is not UNSET:
            field_dict["website_tc"] = website_tc
        if website_sc is not UNSET:
            field_dict["website_sc"] = website_sc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("name_en", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("name_tc", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("name_sc", UNSET))

        def _parse_add_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        add_en = _parse_add_en(d.pop("add_en", UNSET))

        def _parse_add_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        add_tc = _parse_add_tc(d.pop("add_tc", UNSET))

        def _parse_add_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        add_sc = _parse_add_sc(d.pop("add_sc", UNSET))

        def _parse_tel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tel = _parse_tel(d.pop("tel", UNSET))

        def _parse_website_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_en = _parse_website_en(d.pop("website_en", UNSET))

        def _parse_website_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_tc = _parse_website_tc(d.pop("website_tc", UNSET))

        def _parse_website_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_sc = _parse_website_sc(d.pop("website_sc", UNSET))

        wfs_map_server_wfs_dat_cs_attributes = cls(
            objectid=objectid,
            shape=shape,
            name_en=name_en,
            name_tc=name_tc,
            name_sc=name_sc,
            add_en=add_en,
            add_tc=add_tc,
            add_sc=add_sc,
            tel=tel,
            website_en=website_en,
            website_tc=website_tc,
            website_sc=website_sc,
        )

        wfs_map_server_wfs_dat_cs_attributes.additional_properties = d
        return wfs_map_server_wfs_dat_cs_attributes

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
