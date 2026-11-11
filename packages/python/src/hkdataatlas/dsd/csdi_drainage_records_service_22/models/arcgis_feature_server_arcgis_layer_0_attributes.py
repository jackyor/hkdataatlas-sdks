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
        feat_num (None | str | Unset): Publisher field type: esriFieldTypeString
        material (None | str | Unset): Publisher field type: esriFieldTypeString
        cl (float | None | Unset): Publisher field type: esriFieldTypeDouble
        il (float | None | Unset): Publisher field type: esriFieldTypeDouble
        ms_angle_deg (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    feat_num: None | str | Unset = UNSET
    material: None | str | Unset = UNSET
    cl: float | None | Unset = UNSET
    il: float | None | Unset = UNSET
    ms_angle_deg: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        feat_num: None | str | Unset
        if isinstance(self.feat_num, Unset):
            feat_num = UNSET
        else:
            feat_num = self.feat_num

        material: None | str | Unset
        if isinstance(self.material, Unset):
            material = UNSET
        else:
            material = self.material

        cl: float | None | Unset
        if isinstance(self.cl, Unset):
            cl = UNSET
        else:
            cl = self.cl

        il: float | None | Unset
        if isinstance(self.il, Unset):
            il = UNSET
        else:
            il = self.il

        ms_angle_deg: float | None | Unset
        if isinstance(self.ms_angle_deg, Unset):
            ms_angle_deg = UNSET
        else:
            ms_angle_deg = self.ms_angle_deg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if feat_num is not UNSET:
            field_dict["FEAT_NUM"] = feat_num
        if material is not UNSET:
            field_dict["MATERIAL"] = material
        if cl is not UNSET:
            field_dict["CL"] = cl
        if il is not UNSET:
            field_dict["IL"] = il
        if ms_angle_deg is not UNSET:
            field_dict["MS_ANGLE_DEG"] = ms_angle_deg

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_feat_num(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feat_num = _parse_feat_num(d.pop("FEAT_NUM", UNSET))

        def _parse_material(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        material = _parse_material(d.pop("MATERIAL", UNSET))

        def _parse_cl(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cl = _parse_cl(d.pop("CL", UNSET))

        def _parse_il(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        il = _parse_il(d.pop("IL", UNSET))

        def _parse_ms_angle_deg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_angle_deg = _parse_ms_angle_deg(d.pop("MS_ANGLE_DEG", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            feat_num=feat_num,
            material=material,
            cl=cl,
            il=il,
            ms_angle_deg=ms_angle_deg,
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
