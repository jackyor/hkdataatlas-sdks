from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1Attributes:
    """
    Attributes:
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        desc_en (None | str | Unset): Publisher field type: esriFieldTypeString
        desc_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        desc_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        record_id (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        remark_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    easting: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    desc_en: None | str | Unset = UNSET
    desc_sc: None | str | Unset = UNSET
    desc_tc: None | str | Unset = UNSET
    record_id: int | None | Unset = UNSET
    remark_en: None | str | Unset = UNSET
    remark_sc: None | str | Unset = UNSET
    remark_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        desc_en: None | str | Unset
        if isinstance(self.desc_en, Unset):
            desc_en = UNSET
        else:
            desc_en = self.desc_en

        desc_sc: None | str | Unset
        if isinstance(self.desc_sc, Unset):
            desc_sc = UNSET
        else:
            desc_sc = self.desc_sc

        desc_tc: None | str | Unset
        if isinstance(self.desc_tc, Unset):
            desc_tc = UNSET
        else:
            desc_tc = self.desc_tc

        record_id: int | None | Unset
        if isinstance(self.record_id, Unset):
            record_id = UNSET
        else:
            record_id = self.record_id

        remark_en: None | str | Unset
        if isinstance(self.remark_en, Unset):
            remark_en = UNSET
        else:
            remark_en = self.remark_en

        remark_sc: None | str | Unset
        if isinstance(self.remark_sc, Unset):
            remark_sc = UNSET
        else:
            remark_sc = self.remark_sc

        remark_tc: None | str | Unset
        if isinstance(self.remark_tc, Unset):
            remark_tc = UNSET
        else:
            remark_tc = self.remark_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if easting is not UNSET:
            field_dict["EASTING"] = easting
        if northing is not UNSET:
            field_dict["NORTHING"] = northing
        if desc_en is not UNSET:
            field_dict["DESC_EN"] = desc_en
        if desc_sc is not UNSET:
            field_dict["DESC_SC"] = desc_sc
        if desc_tc is not UNSET:
            field_dict["DESC_TC"] = desc_tc
        if record_id is not UNSET:
            field_dict["RECORD_ID"] = record_id
        if remark_en is not UNSET:
            field_dict["REMARK_EN"] = remark_en
        if remark_sc is not UNSET:
            field_dict["REMARK_SC"] = remark_sc
        if remark_tc is not UNSET:
            field_dict["REMARK_TC"] = remark_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

        def _parse_desc_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        desc_en = _parse_desc_en(d.pop("DESC_EN", UNSET))

        def _parse_desc_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        desc_sc = _parse_desc_sc(d.pop("DESC_SC", UNSET))

        def _parse_desc_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        desc_tc = _parse_desc_tc(d.pop("DESC_TC", UNSET))

        def _parse_record_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        record_id = _parse_record_id(d.pop("RECORD_ID", UNSET))

        def _parse_remark_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_en = _parse_remark_en(d.pop("REMARK_EN", UNSET))

        def _parse_remark_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_sc = _parse_remark_sc(d.pop("REMARK_SC", UNSET))

        def _parse_remark_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_tc = _parse_remark_tc(d.pop("REMARK_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            easting=easting,
            northing=northing,
            desc_en=desc_en,
            desc_sc=desc_sc,
            desc_tc=desc_tc,
            record_id=record_id,
            remark_en=remark_en,
            remark_sc=remark_sc,
            remark_tc=remark_tc,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_1_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1_attributes

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
