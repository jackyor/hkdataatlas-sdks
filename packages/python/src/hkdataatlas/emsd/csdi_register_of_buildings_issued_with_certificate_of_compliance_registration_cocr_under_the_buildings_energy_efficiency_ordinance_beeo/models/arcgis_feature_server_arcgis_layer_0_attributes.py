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
        cocr_no (None | str | Unset): Publisher field type: esriFieldTypeString
        remark (None | str | Unset): Publisher field type: esriFieldTypeString
        validity_p_expiry (None | str | Unset): Publisher field type: esriFieldTypeString
        validity_p_first (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    bec_edition: None | str | Unset = UNSET
    building_address_en: None | str | Unset = UNSET
    building_address_tc: None | str | Unset = UNSET
    building_name_en: None | str | Unset = UNSET
    building_name_tc: None | str | Unset = UNSET
    cocr_no: None | str | Unset = UNSET
    remark: None | str | Unset = UNSET
    validity_p_expiry: None | str | Unset = UNSET
    validity_p_first: None | str | Unset = UNSET
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

        cocr_no: None | str | Unset
        if isinstance(self.cocr_no, Unset):
            cocr_no = UNSET
        else:
            cocr_no = self.cocr_no

        remark: None | str | Unset
        if isinstance(self.remark, Unset):
            remark = UNSET
        else:
            remark = self.remark

        validity_p_expiry: None | str | Unset
        if isinstance(self.validity_p_expiry, Unset):
            validity_p_expiry = UNSET
        else:
            validity_p_expiry = self.validity_p_expiry

        validity_p_first: None | str | Unset
        if isinstance(self.validity_p_first, Unset):
            validity_p_first = UNSET
        else:
            validity_p_first = self.validity_p_first

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
        if cocr_no is not UNSET:
            field_dict["COCR_No"] = cocr_no
        if remark is not UNSET:
            field_dict["Remark"] = remark
        if validity_p_expiry is not UNSET:
            field_dict["Validity_P_Expiry"] = validity_p_expiry
        if validity_p_first is not UNSET:
            field_dict["Validity_P_First"] = validity_p_first
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

        def _parse_cocr_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cocr_no = _parse_cocr_no(d.pop("COCR_No", UNSET))

        def _parse_remark(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark = _parse_remark(d.pop("Remark", UNSET))

        def _parse_validity_p_expiry(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        validity_p_expiry = _parse_validity_p_expiry(d.pop("Validity_P_Expiry", UNSET))

        def _parse_validity_p_first(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        validity_p_first = _parse_validity_p_first(d.pop("Validity_P_First", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            bec_edition=bec_edition,
            building_address_en=building_address_en,
            building_address_tc=building_address_tc,
            building_name_en=building_name_en,
            building_name_tc=building_name_tc,
            cocr_no=cocr_no,
            remark=remark,
            validity_p_expiry=validity_p_expiry,
            validity_p_first=validity_p_first,
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
