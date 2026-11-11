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
        bec_edition (None | str | Unset): Publisher field type: esriFieldTypeString
        building_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        building_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        building_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        building_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        declaration_date (None | str | Unset): Publisher field type: esriFieldTypeString
        lot_no (None | str | Unset): Publisher field type: esriFieldTypeString
        ref_no (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    bec_edition: None | str | Unset = UNSET
    building_address_en: None | str | Unset = UNSET
    building_address_tc: None | str | Unset = UNSET
    building_name_en: None | str | Unset = UNSET
    building_name_tc: None | str | Unset = UNSET
    declaration_date: None | str | Unset = UNSET
    lot_no: None | str | Unset = UNSET
    ref_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bec_edition: None | str | Unset
        if isinstance(self.bec_edition, Unset):
            bec_edition = UNSET
        else:
            bec_edition = self.bec_edition

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

        declaration_date: None | str | Unset
        if isinstance(self.declaration_date, Unset):
            declaration_date = UNSET
        else:
            declaration_date = self.declaration_date

        lot_no: None | str | Unset
        if isinstance(self.lot_no, Unset):
            lot_no = UNSET
        else:
            lot_no = self.lot_no

        ref_no: None | str | Unset
        if isinstance(self.ref_no, Unset):
            ref_no = UNSET
        else:
            ref_no = self.ref_no

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bec_edition is not UNSET:
            field_dict["BEC_Edition"] = bec_edition
        if building_address_en is not UNSET:
            field_dict["Building_Address_EN"] = building_address_en
        if building_address_tc is not UNSET:
            field_dict["Building_Address_TC"] = building_address_tc
        if building_name_en is not UNSET:
            field_dict["Building_Name_EN"] = building_name_en
        if building_name_tc is not UNSET:
            field_dict["Building_Name_TC"] = building_name_tc
        if declaration_date is not UNSET:
            field_dict["Declaration_Date"] = declaration_date
        if lot_no is not UNSET:
            field_dict["Lot_No"] = lot_no
        if ref_no is not UNSET:
            field_dict["Ref_No"] = ref_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_bec_edition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bec_edition = _parse_bec_edition(d.pop("BEC_Edition", UNSET))

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

        def _parse_declaration_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        declaration_date = _parse_declaration_date(d.pop("Declaration_Date", UNSET))

        def _parse_lot_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_no = _parse_lot_no(d.pop("Lot_No", UNSET))

        def _parse_ref_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ref_no = _parse_ref_no(d.pop("Ref_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            bec_edition=bec_edition,
            building_address_en=building_address_en,
            building_address_tc=building_address_tc,
            building_name_en=building_name_en,
            building_name_tc=building_name_tc,
            declaration_date=declaration_date,
            lot_no=lot_no,
            ref_no=ref_no,
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
