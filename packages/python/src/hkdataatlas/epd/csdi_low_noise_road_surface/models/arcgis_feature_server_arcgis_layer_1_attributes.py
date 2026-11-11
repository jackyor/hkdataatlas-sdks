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
        rd_name (None | str | Unset): Publisher field type: esriFieldTypeString
        elevation (int | None | Unset): Publisher field type: esriFieldTypeInteger
        am_flow (int | None | Unset): Publisher field type: esriFieldTypeInteger
        am_hv (float | None | Unset): Publisher field type: esriFieldTypeDouble
        pm_flow (int | None | Unset): Publisher field type: esriFieldTypeInteger
        pm_hv (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_leng (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    rd_name: None | str | Unset = UNSET
    elevation: int | None | Unset = UNSET
    am_flow: int | None | Unset = UNSET
    am_hv: float | None | Unset = UNSET
    pm_flow: int | None | Unset = UNSET
    pm_hv: float | None | Unset = UNSET
    shape_leng: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rd_name: None | str | Unset
        if isinstance(self.rd_name, Unset):
            rd_name = UNSET
        else:
            rd_name = self.rd_name

        elevation: int | None | Unset
        if isinstance(self.elevation, Unset):
            elevation = UNSET
        else:
            elevation = self.elevation

        am_flow: int | None | Unset
        if isinstance(self.am_flow, Unset):
            am_flow = UNSET
        else:
            am_flow = self.am_flow

        am_hv: float | None | Unset
        if isinstance(self.am_hv, Unset):
            am_hv = UNSET
        else:
            am_hv = self.am_hv

        pm_flow: int | None | Unset
        if isinstance(self.pm_flow, Unset):
            pm_flow = UNSET
        else:
            pm_flow = self.pm_flow

        pm_hv: float | None | Unset
        if isinstance(self.pm_hv, Unset):
            pm_hv = UNSET
        else:
            pm_hv = self.pm_hv

        shape_leng: float | None | Unset
        if isinstance(self.shape_leng, Unset):
            shape_leng = UNSET
        else:
            shape_leng = self.shape_leng

        objectid = self.objectid

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rd_name is not UNSET:
            field_dict["rd_name"] = rd_name
        if elevation is not UNSET:
            field_dict["elevation"] = elevation
        if am_flow is not UNSET:
            field_dict["AMFlow"] = am_flow
        if am_hv is not UNSET:
            field_dict["AM_HV_"] = am_hv
        if pm_flow is not UNSET:
            field_dict["PMFlow"] = pm_flow
        if pm_hv is not UNSET:
            field_dict["PM_HV_"] = pm_hv
        if shape_leng is not UNSET:
            field_dict["Shape_Leng"] = shape_leng
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_rd_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rd_name = _parse_rd_name(d.pop("rd_name", UNSET))

        def _parse_elevation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        elevation = _parse_elevation(d.pop("elevation", UNSET))

        def _parse_am_flow(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        am_flow = _parse_am_flow(d.pop("AMFlow", UNSET))

        def _parse_am_hv(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        am_hv = _parse_am_hv(d.pop("AM_HV_", UNSET))

        def _parse_pm_flow(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pm_flow = _parse_pm_flow(d.pop("PMFlow", UNSET))

        def _parse_pm_hv(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pm_hv = _parse_pm_hv(d.pop("PM_HV_", UNSET))

        def _parse_shape_leng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_leng = _parse_shape_leng(d.pop("Shape_Leng", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            rd_name=rd_name,
            elevation=elevation,
            am_flow=am_flow,
            am_hv=am_hv,
            pm_flow=pm_flow,
            pm_hv=pm_hv,
            shape_leng=shape_leng,
            objectid=objectid,
            shape_length=shape_length,
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
