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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        pg_uid (None | str | Unset): Publisher field type: esriFieldTypeString
        feat_type (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        sur_type_1 (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        paver_type (None | str | Unset): Publisher field type: esriFieldTypeString
        lvl (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    pg_uid: None | str | Unset = UNSET
    feat_type: int | None | Unset = UNSET
    sur_type_1: int | None | Unset = UNSET
    paver_type: None | str | Unset = UNSET
    lvl: int | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        pg_uid: None | str | Unset
        if isinstance(self.pg_uid, Unset):
            pg_uid = UNSET
        else:
            pg_uid = self.pg_uid

        feat_type: int | None | Unset
        if isinstance(self.feat_type, Unset):
            feat_type = UNSET
        else:
            feat_type = self.feat_type

        sur_type_1: int | None | Unset
        if isinstance(self.sur_type_1, Unset):
            sur_type_1 = UNSET
        else:
            sur_type_1 = self.sur_type_1

        paver_type: None | str | Unset
        if isinstance(self.paver_type, Unset):
            paver_type = UNSET
        else:
            paver_type = self.paver_type

        lvl: int | None | Unset
        if isinstance(self.lvl, Unset):
            lvl = UNSET
        else:
            lvl = self.lvl

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
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if pg_uid is not UNSET:
            field_dict["PG_UID"] = pg_uid
        if feat_type is not UNSET:
            field_dict["FEAT_TYPE"] = feat_type
        if sur_type_1 is not UNSET:
            field_dict["SUR_TYPE_1"] = sur_type_1
        if paver_type is not UNSET:
            field_dict["PAVER_TYPE"] = paver_type
        if lvl is not UNSET:
            field_dict["LVL"] = lvl
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_pg_uid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pg_uid = _parse_pg_uid(d.pop("PG_UID", UNSET))

        def _parse_feat_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feat_type = _parse_feat_type(d.pop("FEAT_TYPE", UNSET))

        def _parse_sur_type_1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sur_type_1 = _parse_sur_type_1(d.pop("SUR_TYPE_1", UNSET))

        def _parse_paver_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        paver_type = _parse_paver_type(d.pop("PAVER_TYPE", UNSET))

        def _parse_lvl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lvl = _parse_lvl(d.pop("LVL", UNSET))

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
            objectid=objectid,
            pg_uid=pg_uid,
            feat_type=feat_type,
            sur_type_1=sur_type_1,
            paver_type=paver_type,
            lvl=lvl,
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
