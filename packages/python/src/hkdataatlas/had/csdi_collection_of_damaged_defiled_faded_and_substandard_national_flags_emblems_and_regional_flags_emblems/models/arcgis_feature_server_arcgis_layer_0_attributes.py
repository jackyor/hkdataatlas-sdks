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
        search01_en (None | str | Unset): Publisher field type: esriFieldTypeString
        search01_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        search01_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch01_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch01_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch01_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch02_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch02_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch02_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    search01_en: None | str | Unset = UNSET
    search01_tc: None | str | Unset = UNSET
    search01_sc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    nsearch01_en: None | str | Unset = UNSET
    nsearch01_tc: None | str | Unset = UNSET
    nsearch01_sc: None | str | Unset = UNSET
    nsearch02_en: None | str | Unset = UNSET
    nsearch02_tc: None | str | Unset = UNSET
    nsearch02_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search01_en: None | str | Unset
        if isinstance(self.search01_en, Unset):
            search01_en = UNSET
        else:
            search01_en = self.search01_en

        search01_tc: None | str | Unset
        if isinstance(self.search01_tc, Unset):
            search01_tc = UNSET
        else:
            search01_tc = self.search01_tc

        search01_sc: None | str | Unset
        if isinstance(self.search01_sc, Unset):
            search01_sc = UNSET
        else:
            search01_sc = self.search01_sc

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

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        nsearch01_en: None | str | Unset
        if isinstance(self.nsearch01_en, Unset):
            nsearch01_en = UNSET
        else:
            nsearch01_en = self.nsearch01_en

        nsearch01_tc: None | str | Unset
        if isinstance(self.nsearch01_tc, Unset):
            nsearch01_tc = UNSET
        else:
            nsearch01_tc = self.nsearch01_tc

        nsearch01_sc: None | str | Unset
        if isinstance(self.nsearch01_sc, Unset):
            nsearch01_sc = UNSET
        else:
            nsearch01_sc = self.nsearch01_sc

        nsearch02_en: None | str | Unset
        if isinstance(self.nsearch02_en, Unset):
            nsearch02_en = UNSET
        else:
            nsearch02_en = self.nsearch02_en

        nsearch02_tc: None | str | Unset
        if isinstance(self.nsearch02_tc, Unset):
            nsearch02_tc = UNSET
        else:
            nsearch02_tc = self.nsearch02_tc

        nsearch02_sc: None | str | Unset
        if isinstance(self.nsearch02_sc, Unset):
            nsearch02_sc = UNSET
        else:
            nsearch02_sc = self.nsearch02_sc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search01_en is not UNSET:
            field_dict["SEARCH01_EN"] = search01_en
        if search01_tc is not UNSET:
            field_dict["SEARCH01_TC"] = search01_tc
        if search01_sc is not UNSET:
            field_dict["SEARCH01_SC"] = search01_sc
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if name_sc is not UNSET:
            field_dict["NAME_SC"] = name_sc
        if address_en is not UNSET:
            field_dict["ADDRESS_EN"] = address_en
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if address_sc is not UNSET:
            field_dict["ADDRESS_SC"] = address_sc
        if nsearch01_en is not UNSET:
            field_dict["NSEARCH01_EN"] = nsearch01_en
        if nsearch01_tc is not UNSET:
            field_dict["NSEARCH01_TC"] = nsearch01_tc
        if nsearch01_sc is not UNSET:
            field_dict["NSEARCH01_SC"] = nsearch01_sc
        if nsearch02_en is not UNSET:
            field_dict["NSEARCH02_EN"] = nsearch02_en
        if nsearch02_tc is not UNSET:
            field_dict["NSEARCH02_TC"] = nsearch02_tc
        if nsearch02_sc is not UNSET:
            field_dict["NSEARCH02_SC"] = nsearch02_sc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_search01_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search01_en = _parse_search01_en(d.pop("SEARCH01_EN", UNSET))

        def _parse_search01_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search01_tc = _parse_search01_tc(d.pop("SEARCH01_TC", UNSET))

        def _parse_search01_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search01_sc = _parse_search01_sc(d.pop("SEARCH01_SC", UNSET))

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

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("NAME_SC", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("ADDRESS_EN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("ADDRESS_SC", UNSET))

        def _parse_nsearch01_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch01_en = _parse_nsearch01_en(d.pop("NSEARCH01_EN", UNSET))

        def _parse_nsearch01_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch01_tc = _parse_nsearch01_tc(d.pop("NSEARCH01_TC", UNSET))

        def _parse_nsearch01_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch01_sc = _parse_nsearch01_sc(d.pop("NSEARCH01_SC", UNSET))

        def _parse_nsearch02_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch02_en = _parse_nsearch02_en(d.pop("NSEARCH02_EN", UNSET))

        def _parse_nsearch02_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch02_tc = _parse_nsearch02_tc(d.pop("NSEARCH02_TC", UNSET))

        def _parse_nsearch02_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch02_sc = _parse_nsearch02_sc(d.pop("NSEARCH02_SC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            search01_en=search01_en,
            search01_tc=search01_tc,
            search01_sc=search01_sc,
            name_en=name_en,
            name_tc=name_tc,
            name_sc=name_sc,
            address_en=address_en,
            address_tc=address_tc,
            address_sc=address_sc,
            nsearch01_en=nsearch01_en,
            nsearch01_tc=nsearch01_tc,
            nsearch01_sc=nsearch01_sc,
            nsearch02_en=nsearch02_en,
            nsearch02_tc=nsearch02_tc,
            nsearch02_sc=nsearch02_sc,
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
