from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer3Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer3Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        reportname (None | str | Unset): Publisher field type: esriFieldTypeString
        project (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        figno (None | str | Unset): Publisher field type: esriFieldTypeString
        layertype (None | str | Unset): Publisher field type: esriFieldTypeString
        layercateg (None | str | Unset): Publisher field type: esriFieldTypeString
        layername (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_len (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_are (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    reportname: None | str | Unset = UNSET
    project: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    figno: None | str | Unset = UNSET
    layertype: None | str | Unset = UNSET
    layercateg: None | str | Unset = UNSET
    layername: None | str | Unset = UNSET
    shape_len: float | None | Unset = UNSET
    shape_are: float | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        reportname: None | str | Unset
        if isinstance(self.reportname, Unset):
            reportname = UNSET
        else:
            reportname = self.reportname

        project: None | str | Unset
        if isinstance(self.project, Unset):
            project = UNSET
        else:
            project = self.project

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        figno: None | str | Unset
        if isinstance(self.figno, Unset):
            figno = UNSET
        else:
            figno = self.figno

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

        shape_len: float | None | Unset
        if isinstance(self.shape_len, Unset):
            shape_len = UNSET
        else:
            shape_len = self.shape_len

        shape_are: float | None | Unset
        if isinstance(self.shape_are, Unset):
            shape_are = UNSET
        else:
            shape_are = self.shape_are

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
        if reportname is not UNSET:
            field_dict["reportname"] = reportname
        if project is not UNSET:
            field_dict["Project"] = project
        if district is not UNSET:
            field_dict["district"] = district
        if figno is not UNSET:
            field_dict["figno"] = figno
        if layertype is not UNSET:
            field_dict["layertype"] = layertype
        if layercateg is not UNSET:
            field_dict["layercateg"] = layercateg
        if layername is not UNSET:
            field_dict["layername"] = layername
        if shape_len is not UNSET:
            field_dict["SHAPE__Len"] = shape_len
        if shape_are is not UNSET:
            field_dict["SHAPE__Are"] = shape_are
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_reportname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reportname = _parse_reportname(d.pop("reportname", UNSET))

        def _parse_project(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project = _parse_project(d.pop("Project", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("district", UNSET))

        def _parse_figno(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        figno = _parse_figno(d.pop("figno", UNSET))

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

        def _parse_shape_len(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_len = _parse_shape_len(d.pop("SHAPE__Len", UNSET))

        def _parse_shape_are(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_are = _parse_shape_are(d.pop("SHAPE__Are", UNSET))

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

        arcgis_feature_server_arcgis_layer_3_attributes = cls(
            objectid=objectid,
            reportname=reportname,
            project=project,
            district=district,
            figno=figno,
            layertype=layertype,
            layercateg=layercateg,
            layername=layername,
            shape_len=shape_len,
            shape_are=shape_are,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        arcgis_feature_server_arcgis_layer_3_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_3_attributes

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
