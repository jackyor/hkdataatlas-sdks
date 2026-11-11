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
        office_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        office_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        office_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        office_tel_no (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_en (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_en: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    office_name_en: None | str | Unset = UNSET
    office_name_sc: None | str | Unset = UNSET
    office_name_tc: None | str | Unset = UNSET
    office_tel_no: None | str | Unset = UNSET
    opening_hours_en: None | str | Unset = UNSET
    opening_hours_sc: None | str | Unset = UNSET
    opening_hours_tc: None | str | Unset = UNSET
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

        office_name_en: None | str | Unset
        if isinstance(self.office_name_en, Unset):
            office_name_en = UNSET
        else:
            office_name_en = self.office_name_en

        office_name_sc: None | str | Unset
        if isinstance(self.office_name_sc, Unset):
            office_name_sc = UNSET
        else:
            office_name_sc = self.office_name_sc

        office_name_tc: None | str | Unset
        if isinstance(self.office_name_tc, Unset):
            office_name_tc = UNSET
        else:
            office_name_tc = self.office_name_tc

        office_tel_no: None | str | Unset
        if isinstance(self.office_tel_no, Unset):
            office_tel_no = UNSET
        else:
            office_tel_no = self.office_tel_no

        opening_hours_en: None | str | Unset
        if isinstance(self.opening_hours_en, Unset):
            opening_hours_en = UNSET
        else:
            opening_hours_en = self.opening_hours_en

        opening_hours_sc: None | str | Unset
        if isinstance(self.opening_hours_sc, Unset):
            opening_hours_sc = UNSET
        else:
            opening_hours_sc = self.opening_hours_sc

        opening_hours_tc: None | str | Unset
        if isinstance(self.opening_hours_tc, Unset):
            opening_hours_tc = UNSET
        else:
            opening_hours_tc = self.opening_hours_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_sc is not UNSET:
            field_dict["Address_SC"] = address_sc
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if office_name_en is not UNSET:
            field_dict["Office_Name_EN"] = office_name_en
        if office_name_sc is not UNSET:
            field_dict["Office_Name_SC"] = office_name_sc
        if office_name_tc is not UNSET:
            field_dict["Office_Name_TC"] = office_name_tc
        if office_tel_no is not UNSET:
            field_dict["Office_Tel_No"] = office_tel_no
        if opening_hours_en is not UNSET:
            field_dict["Opening_Hours_EN"] = opening_hours_en
        if opening_hours_sc is not UNSET:
            field_dict["Opening_Hours_SC"] = opening_hours_sc
        if opening_hours_tc is not UNSET:
            field_dict["Opening_Hours_TC"] = opening_hours_tc
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

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_SC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_office_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_name_en = _parse_office_name_en(d.pop("Office_Name_EN", UNSET))

        def _parse_office_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_name_sc = _parse_office_name_sc(d.pop("Office_Name_SC", UNSET))

        def _parse_office_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_name_tc = _parse_office_name_tc(d.pop("Office_Name_TC", UNSET))

        def _parse_office_tel_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_tel_no = _parse_office_tel_no(d.pop("Office_Tel_No", UNSET))

        def _parse_opening_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_en = _parse_opening_hours_en(d.pop("Opening_Hours_EN", UNSET))

        def _parse_opening_hours_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_sc = _parse_opening_hours_sc(d.pop("Opening_Hours_SC", UNSET))

        def _parse_opening_hours_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_tc = _parse_opening_hours_tc(d.pop("Opening_Hours_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            office_name_en=office_name_en,
            office_name_sc=office_name_sc,
            office_name_tc=office_name_tc,
            office_tel_no=office_tel_no,
            opening_hours_en=opening_hours_en,
            opening_hours_sc=opening_hours_sc,
            opening_hours_tc=opening_hours_tc,
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
