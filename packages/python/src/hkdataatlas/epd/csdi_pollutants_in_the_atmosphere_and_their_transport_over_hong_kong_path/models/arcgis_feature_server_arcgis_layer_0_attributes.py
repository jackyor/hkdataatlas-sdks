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
        year (float | None | Unset): Publisher field type: esriFieldTypeDouble
        annual_fsp (float | None | Unset): Publisher field type: esriFieldTypeDouble
        annual_rsp (float | None | Unset): Publisher field type: esriFieldTypeDouble
        annual_no2 (float | None | Unset): Publisher field type: esriFieldTypeDouble
        link (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    year: float | None | Unset = UNSET
    annual_fsp: float | None | Unset = UNSET
    annual_rsp: float | None | Unset = UNSET
    annual_no2: float | None | Unset = UNSET
    link: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year: float | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        annual_fsp: float | None | Unset
        if isinstance(self.annual_fsp, Unset):
            annual_fsp = UNSET
        else:
            annual_fsp = self.annual_fsp

        annual_rsp: float | None | Unset
        if isinstance(self.annual_rsp, Unset):
            annual_rsp = UNSET
        else:
            annual_rsp = self.annual_rsp

        annual_no2: float | None | Unset
        if isinstance(self.annual_no2, Unset):
            annual_no2 = UNSET
        else:
            annual_no2 = self.annual_no2

        link: None | str | Unset
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

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
        if year is not UNSET:
            field_dict["Year"] = year
        if annual_fsp is not UNSET:
            field_dict["Annual_FSP"] = annual_fsp
        if annual_rsp is not UNSET:
            field_dict["Annual_RSP"] = annual_rsp
        if annual_no2 is not UNSET:
            field_dict["Annual_NO2"] = annual_no2
        if link is not UNSET:
            field_dict["Link"] = link
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

        def _parse_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year = _parse_year(d.pop("Year", UNSET))

        def _parse_annual_fsp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        annual_fsp = _parse_annual_fsp(d.pop("Annual_FSP", UNSET))

        def _parse_annual_rsp(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        annual_rsp = _parse_annual_rsp(d.pop("Annual_RSP", UNSET))

        def _parse_annual_no2(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        annual_no2 = _parse_annual_no2(d.pop("Annual_NO2", UNSET))

        def _parse_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        link = _parse_link(d.pop("Link", UNSET))

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
            year=year,
            annual_fsp=annual_fsp,
            annual_rsp=annual_rsp,
            annual_no2=annual_no2,
            link=link,
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
