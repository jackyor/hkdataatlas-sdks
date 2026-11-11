from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer15Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer15Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        eia_no (None | str | Unset): Publisher field type: esriFieldTypeString
        project (None | str | Unset): Publisher field type: esriFieldTypeString
        fig_no (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        layertype (None | str | Unset): Publisher field type: esriFieldTypeString
        layercateg (None | str | Unset): Publisher field type: esriFieldTypeString
        layername (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_leng (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    eia_no: None | str | Unset = UNSET
    project: None | str | Unset = UNSET
    fig_no: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    layertype: None | str | Unset = UNSET
    layercateg: None | str | Unset = UNSET
    layername: None | str | Unset = UNSET
    shape_leng: float | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        eia_no: None | str | Unset
        if isinstance(self.eia_no, Unset):
            eia_no = UNSET
        else:
            eia_no = self.eia_no

        project: None | str | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        else:
            project = self.project

        fig_no: None | str | Unset
        if isinstance(self.fig_no, Unset):
            fig_no = UNSET
        else:
            fig_no = self.fig_no

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        layertype: None | str | Unset
        if isinstance(self.layertype, Unset):
            layertype = UNSET
        else:
            layertype = self.layertype

        layercateg: None | str | Unset
        if isinstance(self.layercateg, Unset):
            layercateg = UNSET
        else:
            layercateg = self.layercateg

        layername: None | str | Unset
        if isinstance(self.layername, Unset):
            layername = UNSET
        else:
            layername = self.layername

        shape_leng: float | None | Unset
        if isinstance(self.shape_leng, Unset):
            shape_leng = UNSET
        else:
            shape_leng = self.shape_leng

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
        if eia_no is not UNSET:
            field_dict["EIA_No"] = eia_no
        if project is not UNSET:
            field_dict["Project"] = project
        if fig_no is not UNSET:
            field_dict["FigNo"] = fig_no
        if district is not UNSET:
            field_dict["district"] = district
        if layertype is not UNSET:
            field_dict["layertype"] = layertype
        if layercateg is not UNSET:
            field_dict["layercateg"] = layercateg
        if layername is not UNSET:
            field_dict["layername"] = layername
        if shape_leng is not UNSET:
            field_dict["Shape_Leng"] = shape_leng
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_eia_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        eia_no = _parse_eia_no(d.pop("EIA_No", UNSET))

        def _parse_project(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project = _parse_project(d.pop("Project", UNSET))

        def _parse_fig_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fig_no = _parse_fig_no(d.pop("FigNo", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("district", UNSET))

        def _parse_layertype(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        layertype = _parse_layertype(d.pop("layertype", UNSET))

        def _parse_layercateg(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        layercateg = _parse_layercateg(d.pop("layercateg", UNSET))

        def _parse_layername(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        layername = _parse_layername(d.pop("layername", UNSET))

        def _parse_shape_leng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_leng = _parse_shape_leng(d.pop("Shape_Leng", UNSET))

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

        arcgis_feature_server_arcgis_layer_15_attributes = cls(
            objectid=objectid,
            eia_no=eia_no,
            project=project,
            fig_no=fig_no,
            district=district,
            layertype=layertype,
            layercateg=layercateg,
            layername=layername,
            shape_leng=shape_leng,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        arcgis_feature_server_arcgis_layer_15_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_15_attributes

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
