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
        dc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dc_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        dc_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        la (float | None | Unset): Publisher field type: esriFieldTypeDouble
        mypopn_land (float | None | Unset): Publisher field type: esriFieldTypeDouble
        period (float | None | Unset): Publisher field type: esriFieldTypeDouble
        popn_d (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    dc: float | None | Unset = UNSET
    dc_chi: None | str | Unset = UNSET
    dc_eng: None | str | Unset = UNSET
    la: float | None | Unset = UNSET
    mypopn_land: float | None | Unset = UNSET
    period: float | None | Unset = UNSET
    popn_d: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dc: float | None | Unset
        if isinstance(self.dc, Unset):
            dc = UNSET
        else:
            dc = self.dc

        dc_chi: None | str | Unset
        if isinstance(self.dc_chi, Unset):
            dc_chi = UNSET
        else:
            dc_chi = self.dc_chi

        dc_eng: None | str | Unset
        if isinstance(self.dc_eng, Unset):
            dc_eng = UNSET
        else:
            dc_eng = self.dc_eng

        la: float | None | Unset
        if isinstance(self.la, Unset):
            la = UNSET
        else:
            la = self.la

        mypopn_land: float | None | Unset
        if isinstance(self.mypopn_land, Unset):
            mypopn_land = UNSET
        else:
            mypopn_land = self.mypopn_land

        period: float | None | Unset
        if isinstance(self.period, Unset):
            period = UNSET
        else:
            period = self.period

        popn_d: float | None | Unset
        if isinstance(self.popn_d, Unset):
            popn_d = UNSET
        else:
            popn_d = self.popn_d

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
        if dc is not UNSET:
            field_dict["DC"] = dc
        if dc_chi is not UNSET:
            field_dict["DC_CHI"] = dc_chi
        if dc_eng is not UNSET:
            field_dict["DC_ENG"] = dc_eng
        if la is not UNSET:
            field_dict["LA"] = la
        if mypopn_land is not UNSET:
            field_dict["MYPOPN_LAND"] = mypopn_land
        if period is not UNSET:
            field_dict["PERIOD"] = period
        if popn_d is not UNSET:
            field_dict["POPN_D"] = popn_d
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

        def _parse_dc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dc = _parse_dc(d.pop("DC", UNSET))

        def _parse_dc_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_chi = _parse_dc_chi(d.pop("DC_CHI", UNSET))

        def _parse_dc_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dc_eng = _parse_dc_eng(d.pop("DC_ENG", UNSET))

        def _parse_la(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        la = _parse_la(d.pop("LA", UNSET))

        def _parse_mypopn_land(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mypopn_land = _parse_mypopn_land(d.pop("MYPOPN_LAND", UNSET))

        def _parse_period(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        period = _parse_period(d.pop("PERIOD", UNSET))

        def _parse_popn_d(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        popn_d = _parse_popn_d(d.pop("POPN_D", UNSET))

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
            dc=dc,
            dc_chi=dc_chi,
            dc_eng=dc_eng,
            la=la,
            mypopn_land=mypopn_land,
            period=period,
            popn_d=popn_d,
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
