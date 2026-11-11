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
        evanumber (None | str | Unset): Publisher field type: esriFieldTypeString
        englishlocationname (None | str | Unset): Publisher field type: esriFieldTypeString
        chineselocationname (None | str | Unset): Publisher field type: esriFieldTypeString
        dlooffice (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    evanumber: None | str | Unset = UNSET
    englishlocationname: None | str | Unset = UNSET
    chineselocationname: None | str | Unset = UNSET
    dlooffice: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        evanumber: None | str | Unset
        if isinstance(self.evanumber, Unset):
            evanumber = UNSET
        else:
            evanumber = self.evanumber

        englishlocationname: None | str | Unset
        if isinstance(self.englishlocationname, Unset):
            englishlocationname = UNSET
        else:
            englishlocationname = self.englishlocationname

        chineselocationname: None | str | Unset
        if isinstance(self.chineselocationname, Unset):
            chineselocationname = UNSET
        else:
            chineselocationname = self.chineselocationname

        dlooffice: None | str | Unset
        if isinstance(self.dlooffice, Unset):
            dlooffice = UNSET
        else:
            dlooffice = self.dlooffice

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
        if evanumber is not UNSET:
            field_dict["EVANUMBER"] = evanumber
        if englishlocationname is not UNSET:
            field_dict["ENGLISHLOCATIONNAME"] = englishlocationname
        if chineselocationname is not UNSET:
            field_dict["CHINESELOCATIONNAME"] = chineselocationname
        if dlooffice is not UNSET:
            field_dict["DLOOFFICE"] = dlooffice
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_evanumber(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evanumber = _parse_evanumber(d.pop("EVANUMBER", UNSET))

        def _parse_englishlocationname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        englishlocationname = _parse_englishlocationname(
            d.pop("ENGLISHLOCATIONNAME", UNSET)
        )

        def _parse_chineselocationname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chineselocationname = _parse_chineselocationname(
            d.pop("CHINESELOCATIONNAME", UNSET)
        )

        def _parse_dlooffice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dlooffice = _parse_dlooffice(d.pop("DLOOFFICE", UNSET))

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
            evanumber=evanumber,
            englishlocationname=englishlocationname,
            chineselocationname=chineselocationname,
            dlooffice=dlooffice,
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
