from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1005Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1005Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        child_lot_prn (str | Unset): Publisher field type: esriFieldTypeString
        amalgamating_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        parent_lot_prn (str | Unset): Publisher field type: esriFieldTypeString
        memorial_no (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    child_lot_prn: str | Unset = UNSET
    amalgamating_date: Any | Unset = UNSET
    parent_lot_prn: str | Unset = UNSET
    memorial_no: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        child_lot_prn = self.child_lot_prn

        amalgamating_date = self.amalgamating_date

        parent_lot_prn = self.parent_lot_prn

        memorial_no: None | str | Unset
        if isinstance(self.memorial_no, Unset):
            memorial_no = UNSET
        else:
            memorial_no = self.memorial_no

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if child_lot_prn is not UNSET:
            field_dict["ChildLotPRN"] = child_lot_prn
        if amalgamating_date is not UNSET:
            field_dict["AmalgamatingDate"] = amalgamating_date
        if parent_lot_prn is not UNSET:
            field_dict["ParentLotPRN"] = parent_lot_prn
        if memorial_no is not UNSET:
            field_dict["MemorialNo"] = memorial_no

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        child_lot_prn = d.pop("ChildLotPRN", UNSET)

        amalgamating_date = d.pop("AmalgamatingDate", UNSET)

        parent_lot_prn = d.pop("ParentLotPRN", UNSET)

        def _parse_memorial_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        memorial_no = _parse_memorial_no(d.pop("MemorialNo", UNSET))

        arcgis_feature_server_arcgis_layer_1005_attributes = cls(
            objectid=objectid,
            child_lot_prn=child_lot_prn,
            amalgamating_date=amalgamating_date,
            parent_lot_prn=parent_lot_prn,
            memorial_no=memorial_no,
        )

        arcgis_feature_server_arcgis_layer_1005_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1005_attributes

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
