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
        site_code (None | str | Unset): Publisher field type: esriFieldTypeString
        pbg_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        pbg_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        fid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    site_code: None | str | Unset = UNSET
    pbg_name_tc: None | str | Unset = UNSET
    pbg_name_en: None | str | Unset = UNSET
    last_update_date: Any | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_code: None | str | Unset
        if isinstance(self.site_code, Unset):
            site_code = UNSET
        else:
            site_code = self.site_code

        pbg_name_tc: None | str | Unset
        if isinstance(self.pbg_name_tc, Unset):
            pbg_name_tc = UNSET
        else:
            pbg_name_tc = self.pbg_name_tc

        pbg_name_en: None | str | Unset
        if isinstance(self.pbg_name_en, Unset):
            pbg_name_en = UNSET
        else:
            pbg_name_en = self.pbg_name_en

        last_update_date = self.last_update_date

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        objectid = self.objectid

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_code is not UNSET:
            field_dict["site_code"] = site_code
        if pbg_name_tc is not UNSET:
            field_dict["pbg_name_tc"] = pbg_name_tc
        if pbg_name_en is not UNSET:
            field_dict["pbg_name_en"] = pbg_name_en
        if last_update_date is not UNSET:
            field_dict["last_update_date"] = last_update_date
        if fid is not UNSET:
            field_dict["fid"] = fid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_site_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_code = _parse_site_code(d.pop("site_code", UNSET))

        def _parse_pbg_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pbg_name_tc = _parse_pbg_name_tc(d.pop("pbg_name_tc", UNSET))

        def _parse_pbg_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pbg_name_en = _parse_pbg_name_en(d.pop("pbg_name_en", UNSET))

        last_update_date = d.pop("last_update_date", UNSET)

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            site_code=site_code,
            pbg_name_tc=pbg_name_tc,
            pbg_name_en=pbg_name_en,
            last_update_date=last_update_date,
            fid=fid,
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
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
