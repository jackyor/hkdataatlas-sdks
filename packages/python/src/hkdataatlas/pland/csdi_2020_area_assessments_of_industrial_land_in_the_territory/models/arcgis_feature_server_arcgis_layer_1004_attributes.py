from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1004Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1004Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        aa_code (None | str | Unset): Publisher field type: esriFieldTypeString
        aa_title (None | str | Unset): Publisher field type: esriFieldTypeString
        office_solely_used (float | None | Unset): Publisher field type: esriFieldTypeDouble
        office_other_predominant_use (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    office_solely_used: float | None | Unset = UNSET
    office_other_predominant_use: float | None | Unset = UNSET
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

        office_solely_used: float | None | Unset
        if isinstance(self.office_solely_used, Unset):
            office_solely_used = UNSET
        else:
            office_solely_used = self.office_solely_used

        office_other_predominant_use: float | None | Unset
        if isinstance(self.office_other_predominant_use, Unset):
            office_other_predominant_use = UNSET
        else:
            office_other_predominant_use = self.office_other_predominant_use

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if office_solely_used is not UNSET:
            field_dict["Office_solely_used"] = office_solely_used
        if office_other_predominant_use is not UNSET:
            field_dict["Office_other_predominant_use"] = office_other_predominant_use

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

        def _parse_office_solely_used(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        office_solely_used = _parse_office_solely_used(
            d.pop("Office_solely_used", UNSET)
        )

        def _parse_office_other_predominant_use(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        office_other_predominant_use = _parse_office_other_predominant_use(
            d.pop("Office_other_predominant_use", UNSET)
        )

        arcgis_feature_server_arcgis_layer_1004_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            office_solely_used=office_solely_used,
            office_other_predominant_use=office_other_predominant_use,
        )

        arcgis_feature_server_arcgis_layer_1004_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1004_attributes

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
