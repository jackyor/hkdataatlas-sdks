from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1013Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1013Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        aa_code (None | str | Unset): Publisher field type: esriFieldTypeString
        aa_title (None | str | Unset): Publisher field type: esriFieldTypeString
        same_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        other_area_in_hk (float | None | Unset): Publisher field type: esriFieldTypeDouble
        outside_hk (float | None | Unset): Publisher field type: esriFieldTypeDouble
        no_decision_yet_unknown (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    same_area: float | None | Unset = UNSET
    other_area_in_hk: float | None | Unset = UNSET
    outside_hk: float | None | Unset = UNSET
    no_decision_yet_unknown: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        aa_code: None | str | Unset
        if isinstance(self.aa_code, Unset):
            aa_code = UNSET
        else:
            aa_code = self.aa_code

        aa_title: None | str | Unset
        if isinstance(self.aa_title, Unset):
            aa_title = UNSET
        else:
            aa_title = self.aa_title

        same_area: float | None | Unset
        if isinstance(self.same_area, Unset):
            same_area = UNSET
        else:
            same_area = self.same_area

        other_area_in_hk: float | None | Unset
        if isinstance(self.other_area_in_hk, Unset):
            other_area_in_hk = UNSET
        else:
            other_area_in_hk = self.other_area_in_hk

        outside_hk: float | None | Unset
        if isinstance(self.outside_hk, Unset):
            outside_hk = UNSET
        else:
            outside_hk = self.outside_hk

        no_decision_yet_unknown: float | None | Unset
        if isinstance(self.no_decision_yet_unknown, Unset):
            no_decision_yet_unknown = UNSET
        else:
            no_decision_yet_unknown = self.no_decision_yet_unknown

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if same_area is not UNSET:
            field_dict["Same_area"] = same_area
        if other_area_in_hk is not UNSET:
            field_dict["Other_area_in_HK"] = other_area_in_hk
        if outside_hk is not UNSET:
            field_dict["Outside_HK"] = outside_hk
        if no_decision_yet_unknown is not UNSET:
            field_dict["No_decision_yet_Unknown"] = no_decision_yet_unknown

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_aa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_code = _parse_aa_code(d.pop("AA_Code", UNSET))

        def _parse_aa_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_title = _parse_aa_title(d.pop("AA_Title", UNSET))

        def _parse_same_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        same_area = _parse_same_area(d.pop("Same_area", UNSET))

        def _parse_other_area_in_hk(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        other_area_in_hk = _parse_other_area_in_hk(d.pop("Other_area_in_HK", UNSET))

        def _parse_outside_hk(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        outside_hk = _parse_outside_hk(d.pop("Outside_HK", UNSET))

        def _parse_no_decision_yet_unknown(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_decision_yet_unknown = _parse_no_decision_yet_unknown(
            d.pop("No_decision_yet_Unknown", UNSET)
        )

        arcgis_feature_server_arcgis_layer_1013_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            same_area=same_area,
            other_area_in_hk=other_area_in_hk,
            outside_hk=outside_hk,
            no_decision_yet_unknown=no_decision_yet_unknown,
        )

        arcgis_feature_server_arcgis_layer_1013_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1013_attributes

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
