from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTappingPointStormwaterAttributes")


@_attrs_define
class WfsMapServerWfsTappingPointStormwaterAttributes:
    """
    Attributes:
        cl (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        feat_num (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        il (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        material (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        ms_angle_deg (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        objectid (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid_1 (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    cl: float | None | Unset = UNSET
    feat_num: None | str | Unset = UNSET
    il: float | None | Unset = UNSET
    material: None | str | Unset = UNSET
    ms_angle_deg: float | None | Unset = UNSET
    objectid: float | None | Unset = UNSET
    objectid_1: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cl: float | None | Unset
        if isinstance(self.cl, Unset):
            cl = UNSET
        else:
            cl = self.cl

        feat_num: None | str | Unset
        if isinstance(self.feat_num, Unset):
            feat_num = UNSET
        else:
            feat_num = self.feat_num

        il: float | None | Unset
        if isinstance(self.il, Unset):
            il = UNSET
        else:
            il = self.il

        material: None | str | Unset
        if isinstance(self.material, Unset):
            material = UNSET
        else:
            material = self.material

        ms_angle_deg: float | None | Unset
        if isinstance(self.ms_angle_deg, Unset):
            ms_angle_deg = UNSET
        else:
            ms_angle_deg = self.ms_angle_deg

        objectid: float | None | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        objectid_1 = self.objectid_1

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cl is not UNSET:
            field_dict["CL"] = cl
        if feat_num is not UNSET:
            field_dict["FEAT_NUM"] = feat_num
        if il is not UNSET:
            field_dict["IL"] = il
        if material is not UNSET:
            field_dict["MATERIAL"] = material
        if ms_angle_deg is not UNSET:
            field_dict["MS_ANGLE_DEG"] = ms_angle_deg
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_cl(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        cl = _parse_cl(d.pop("CL", UNSET))

        def _parse_feat_num(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feat_num = _parse_feat_num(d.pop("FEAT_NUM", UNSET))

        def _parse_il(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        il = _parse_il(d.pop("IL", UNSET))

        def _parse_material(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        material = _parse_material(d.pop("MATERIAL", UNSET))

        def _parse_ms_angle_deg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ms_angle_deg = _parse_ms_angle_deg(d.pop("MS_ANGLE_DEG", UNSET))

        def _parse_objectid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        objectid_1 = d.pop("OBJECTID_1", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_tapping_point_stormwater_attributes = cls(
            cl=cl,
            feat_num=feat_num,
            il=il,
            material=material,
            ms_angle_deg=ms_angle_deg,
            objectid=objectid,
            objectid_1=objectid_1,
            shape=shape,
        )

        wfs_map_server_wfs_tapping_point_stormwater_attributes.additional_properties = d
        return wfs_map_server_wfs_tapping_point_stormwater_attributes

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
