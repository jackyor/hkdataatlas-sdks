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
        bec_eac_edition (None | str | Unset): Publisher field type: esriFieldTypeString
        building_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        building_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        building_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        building_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        date_in (None | str | Unset): Publisher field type: esriFieldTypeString
        types_bsi (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    bec_eac_edition: None | str | Unset = UNSET
    building_address_en: None | str | Unset = UNSET
    building_address_tc: None | str | Unset = UNSET
    building_name_en: None | str | Unset = UNSET
    building_name_tc: None | str | Unset = UNSET
    date_in: None | str | Unset = UNSET
    types_bsi: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bec_eac_edition: None | str | Unset
        if isinstance(self.bec_eac_edition, Unset):
            bec_eac_edition = UNSET
        else:
            bec_eac_edition = self.bec_eac_edition

        building_address_en: None | str | Unset
        if isinstance(self.building_address_en, Unset):
            building_address_en = UNSET
        else:
            building_address_en = self.building_address_en

        building_address_tc: None | str | Unset
        if isinstance(self.building_address_tc, Unset):
            building_address_tc = UNSET
        else:
            building_address_tc = self.building_address_tc

        building_name_en: None | str | Unset
        if isinstance(self.building_name_en, Unset):
            building_name_en = UNSET
        else:
            building_name_en = self.building_name_en

        building_name_tc: None | str | Unset
        if isinstance(self.building_name_tc, Unset):
            building_name_tc = UNSET
        else:
            building_name_tc = self.building_name_tc

        date_in: None | str | Unset
        if isinstance(self.date_in, Unset):
            date_in = UNSET
        else:
            date_in = self.date_in

        types_bsi: None | str | Unset
        if isinstance(self.types_bsi, Unset):
            types_bsi = UNSET
        else:
            types_bsi = self.types_bsi

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bec_eac_edition is not UNSET:
            field_dict["BEC_EAC_Edition"] = bec_eac_edition
        if building_address_en is not UNSET:
            field_dict["Building_Address_EN"] = building_address_en
        if building_address_tc is not UNSET:
            field_dict["Building_Address_TC"] = building_address_tc
        if building_name_en is not UNSET:
            field_dict["Building_Name_EN"] = building_name_en
        if building_name_tc is not UNSET:
            field_dict["Building_Name_TC"] = building_name_tc
        if date_in is not UNSET:
            field_dict["Date_IN"] = date_in
        if types_bsi is not UNSET:
            field_dict["Types_BSI"] = types_bsi
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_bec_eac_edition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bec_eac_edition = _parse_bec_eac_edition(d.pop("BEC_EAC_Edition", UNSET))

        def _parse_building_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_address_en = _parse_building_address_en(
            d.pop("Building_Address_EN", UNSET)
        )

        def _parse_building_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_address_tc = _parse_building_address_tc(
            d.pop("Building_Address_TC", UNSET)
        )

        def _parse_building_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_name_en = _parse_building_name_en(d.pop("Building_Name_EN", UNSET))

        def _parse_building_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_name_tc = _parse_building_name_tc(d.pop("Building_Name_TC", UNSET))

        def _parse_date_in(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_in = _parse_date_in(d.pop("Date_IN", UNSET))

        def _parse_types_bsi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_bsi = _parse_types_bsi(d.pop("Types_BSI", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            bec_eac_edition=bec_eac_edition,
            building_address_en=building_address_en,
            building_address_tc=building_address_tc,
            building_name_en=building_name_en,
            building_name_tc=building_name_tc,
            date_in=date_in,
            types_bsi=types_bsi,
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
