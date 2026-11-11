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
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        openinghrs_en (None | str | Unset): Publisher field type: esriFieldTypeString
        openinghrs_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        openinghrs_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        services_en (None | str | Unset): Publisher field type: esriFieldTypeString
        services_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        services_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_en: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    openinghrs_en: None | str | Unset = UNSET
    openinghrs_sc: None | str | Unset = UNSET
    openinghrs_tc: None | str | Unset = UNSET
    services_en: None | str | Unset = UNSET
    services_sc: None | str | Unset = UNSET
    services_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        openinghrs_en: None | str | Unset
        if isinstance(self.openinghrs_en, Unset):
            openinghrs_en = UNSET
        else:
            openinghrs_en = self.openinghrs_en

        openinghrs_sc: None | str | Unset
        if isinstance(self.openinghrs_sc, Unset):
            openinghrs_sc = UNSET
        else:
            openinghrs_sc = self.openinghrs_sc

        openinghrs_tc: None | str | Unset
        if isinstance(self.openinghrs_tc, Unset):
            openinghrs_tc = UNSET
        else:
            openinghrs_tc = self.openinghrs_tc

        services_en: None | str | Unset
        if isinstance(self.services_en, Unset):
            services_en = UNSET
        else:
            services_en = self.services_en

        services_sc: None | str | Unset
        if isinstance(self.services_sc, Unset):
            services_sc = UNSET
        else:
            services_sc = self.services_sc

        services_tc: None | str | Unset
        if isinstance(self.services_tc, Unset):
            services_tc = UNSET
        else:
            services_tc = self.services_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["ADDRESS_EN"] = address_en
        if address_sc is not UNSET:
            field_dict["ADDRESS_SC"] = address_sc
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if name_sc is not UNSET:
            field_dict["NAME_SC"] = name_sc
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if openinghrs_en is not UNSET:
            field_dict["OPENINGHRS_EN"] = openinghrs_en
        if openinghrs_sc is not UNSET:
            field_dict["OPENINGHRS_SC"] = openinghrs_sc
        if openinghrs_tc is not UNSET:
            field_dict["OPENINGHRS_TC"] = openinghrs_tc
        if services_en is not UNSET:
            field_dict["SERVICES_EN"] = services_en
        if services_sc is not UNSET:
            field_dict["SERVICES_SC"] = services_sc
        if services_tc is not UNSET:
            field_dict["SERVICES_TC"] = services_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

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

        address_en = _parse_address_en(d.pop("ADDRESS_EN", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("ADDRESS_SC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NAME_EN", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("NAME_SC", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        def _parse_openinghrs_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        openinghrs_en = _parse_openinghrs_en(d.pop("OPENINGHRS_EN", UNSET))

        def _parse_openinghrs_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        openinghrs_sc = _parse_openinghrs_sc(d.pop("OPENINGHRS_SC", UNSET))

        def _parse_openinghrs_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        openinghrs_tc = _parse_openinghrs_tc(d.pop("OPENINGHRS_TC", UNSET))

        def _parse_services_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        services_en = _parse_services_en(d.pop("SERVICES_EN", UNSET))

        def _parse_services_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        services_sc = _parse_services_sc(d.pop("SERVICES_SC", UNSET))

        def _parse_services_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        services_tc = _parse_services_tc(d.pop("SERVICES_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            openinghrs_en=openinghrs_en,
            openinghrs_sc=openinghrs_sc,
            openinghrs_tc=openinghrs_tc,
            services_en=services_en,
            services_sc=services_sc,
            services_tc=services_tc,
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
