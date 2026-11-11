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
        fcz (None | str | Unset): Publisher field type: esriFieldTypeString
        name_c (None | str | Unset): Publisher field type: esriFieldTypeString
        name_e (None | str | Unset): Publisher field type: esriFieldTypeString
        scheme_c (None | str | Unset): Publisher field type: esriFieldTypeString
        scheme_e (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    fcz: None | str | Unset = UNSET
    name_c: None | str | Unset = UNSET
    name_e: None | str | Unset = UNSET
    scheme_c: None | str | Unset = UNSET
    scheme_e: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fcz: None | str | Unset
        if isinstance(self.fcz, Unset):
            fcz = UNSET
        else:
            fcz = self.fcz

        name_c: None | str | Unset
        if isinstance(self.name_c, Unset):
            name_c = UNSET
        else:
            name_c = self.name_c

        name_e: None | str | Unset
        if isinstance(self.name_e, Unset):
            name_e = UNSET
        else:
            name_e = self.name_e

        scheme_c: None | str | Unset
        if isinstance(self.scheme_c, Unset):
            scheme_c = UNSET
        else:
            scheme_c = self.scheme_c

        scheme_e: None | str | Unset
        if isinstance(self.scheme_e, Unset):
            scheme_e = UNSET
        else:
            scheme_e = self.scheme_e

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
        if fcz is not UNSET:
            field_dict["FCZ"] = fcz
        if name_c is not UNSET:
            field_dict["NAME_C"] = name_c
        if name_e is not UNSET:
            field_dict["NAME_E"] = name_e
        if scheme_c is not UNSET:
            field_dict["SCHEME_C"] = scheme_c
        if scheme_e is not UNSET:
            field_dict["SCHEME_E"] = scheme_e
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

        def _parse_fcz(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fcz = _parse_fcz(d.pop("FCZ", UNSET))

        def _parse_name_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_c = _parse_name_c(d.pop("NAME_C", UNSET))

        def _parse_name_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_e = _parse_name_e(d.pop("NAME_E", UNSET))

        def _parse_scheme_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme_c = _parse_scheme_c(d.pop("SCHEME_C", UNSET))

        def _parse_scheme_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheme_e = _parse_scheme_e(d.pop("SCHEME_E", UNSET))

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
            fcz=fcz,
            name_c=name_c,
            name_e=name_e,
            scheme_c=scheme_c,
            scheme_e=scheme_e,
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
