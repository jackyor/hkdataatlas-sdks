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
        planno (None | str | Unset): Publisher field type: esriFieldTypeString
        rcom_ename (None | str | Unset): Publisher field type: esriFieldTypeString
        rcom_cname (None | str | Unset): Publisher field type: esriFieldTypeString
        vil_ename (None | str | Unset): Publisher field type: esriFieldTypeString
        vil_cname (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    planno: None | str | Unset = UNSET
    rcom_ename: None | str | Unset = UNSET
    rcom_cname: None | str | Unset = UNSET
    vil_ename: None | str | Unset = UNSET
    vil_cname: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        planno: None | str | Unset
        if isinstance(self.planno, Unset):
            planno = UNSET
        else:
            planno = self.planno

        rcom_ename: None | str | Unset
        if isinstance(self.rcom_ename, Unset):
            rcom_ename = UNSET
        else:
            rcom_ename = self.rcom_ename

        rcom_cname: None | str | Unset
        if isinstance(self.rcom_cname, Unset):
            rcom_cname = UNSET
        else:
            rcom_cname = self.rcom_cname

        vil_ename: None | str | Unset
        if isinstance(self.vil_ename, Unset):
            vil_ename = UNSET
        else:
            vil_ename = self.vil_ename

        vil_cname: None | str | Unset
        if isinstance(self.vil_cname, Unset):
            vil_cname = UNSET
        else:
            vil_cname = self.vil_cname

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

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
        if planno is not UNSET:
            field_dict["PLANNO"] = planno
        if rcom_ename is not UNSET:
            field_dict["RCOM_ENAME"] = rcom_ename
        if rcom_cname is not UNSET:
            field_dict["RCOM_CNAME"] = rcom_cname
        if vil_ename is not UNSET:
            field_dict["VIL_ENAME"] = vil_ename
        if vil_cname is not UNSET:
            field_dict["VIL_CNAME"] = vil_cname
        if district is not UNSET:
            field_dict["DISTRICT"] = district
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_planno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        planno = _parse_planno(d.pop("PLANNO", UNSET))

        def _parse_rcom_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rcom_ename = _parse_rcom_ename(d.pop("RCOM_ENAME", UNSET))

        def _parse_rcom_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rcom_cname = _parse_rcom_cname(d.pop("RCOM_CNAME", UNSET))

        def _parse_vil_ename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vil_ename = _parse_vil_ename(d.pop("VIL_ENAME", UNSET))

        def _parse_vil_cname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vil_cname = _parse_vil_cname(d.pop("VIL_CNAME", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("DISTRICT", UNSET))

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
            planno=planno,
            rcom_ename=rcom_ename,
            rcom_cname=rcom_cname,
            vil_ename=vil_ename,
            vil_cname=vil_cname,
            district=district,
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
