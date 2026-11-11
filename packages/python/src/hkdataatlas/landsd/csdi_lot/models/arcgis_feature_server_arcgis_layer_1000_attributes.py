from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1000Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1000Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        lot_csuid (str | Unset): Publisher field type: esriFieldTypeString
        lot_code (int | Unset): Publisher field type: esriFieldTypeSmallInteger
        lot_number (int | Unset): Publisher field type: esriFieldTypeInteger
        lot_number_alpha (None | str | Unset): Publisher field type: esriFieldTypeString
        section_code (None | str | Unset): Publisher field type: esriFieldTypeString
        lot_display_name (None | str | Unset): Publisher field type: esriFieldTypeString
        class_ (str | Unset): Publisher field type: esriFieldTypeString
        lbs_info (str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    lot_csuid: str | Unset = UNSET
    lot_code: int | Unset = UNSET
    lot_number: int | Unset = UNSET
    lot_number_alpha: None | str | Unset = UNSET
    section_code: None | str | Unset = UNSET
    lot_display_name: None | str | Unset = UNSET
    class_: str | Unset = UNSET
    lbs_info: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        lot_csuid = self.lot_csuid

        lot_code = self.lot_code

        lot_number = self.lot_number

        lot_number_alpha: None | str | Unset
        if isinstance(self.lot_number_alpha, Unset):
            lot_number_alpha = UNSET
        else:
            lot_number_alpha = self.lot_number_alpha

        section_code: None | str | Unset
        if isinstance(self.section_code, Unset):
            section_code = UNSET
        else:
            section_code = self.section_code

        lot_display_name: None | str | Unset
        if isinstance(self.lot_display_name, Unset):
            lot_display_name = UNSET
        else:
            lot_display_name = self.lot_display_name

        class_ = self.class_

        lbs_info = self.lbs_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if lot_csuid is not UNSET:
            field_dict["LotCSUID"] = lot_csuid
        if lot_code is not UNSET:
            field_dict["LotCode"] = lot_code
        if lot_number is not UNSET:
            field_dict["LotNumber"] = lot_number
        if lot_number_alpha is not UNSET:
            field_dict["LotNumberAlpha"] = lot_number_alpha
        if section_code is not UNSET:
            field_dict["SectionCode"] = section_code
        if lot_display_name is not UNSET:
            field_dict["LotDisplayName"] = lot_display_name
        if class_ is not UNSET:
            field_dict["Class"] = class_
        if lbs_info is not UNSET:
            field_dict["LBSInfo"] = lbs_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        lot_csuid = d.pop("LotCSUID", UNSET)

        lot_code = d.pop("LotCode", UNSET)

        lot_number = d.pop("LotNumber", UNSET)

        def _parse_lot_number_alpha(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_number_alpha = _parse_lot_number_alpha(d.pop("LotNumberAlpha", UNSET))

        def _parse_section_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_code = _parse_section_code(d.pop("SectionCode", UNSET))

        def _parse_lot_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lot_display_name = _parse_lot_display_name(d.pop("LotDisplayName", UNSET))

        class_ = d.pop("Class", UNSET)

        lbs_info = d.pop("LBSInfo", UNSET)

        arcgis_feature_server_arcgis_layer_1000_attributes = cls(
            objectid=objectid,
            lot_csuid=lot_csuid,
            lot_code=lot_code,
            lot_number=lot_number,
            lot_number_alpha=lot_number_alpha,
            section_code=section_code,
            lot_display_name=lot_display_name,
            class_=class_,
            lbs_info=lbs_info,
        )

        arcgis_feature_server_arcgis_layer_1000_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1000_attributes

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
