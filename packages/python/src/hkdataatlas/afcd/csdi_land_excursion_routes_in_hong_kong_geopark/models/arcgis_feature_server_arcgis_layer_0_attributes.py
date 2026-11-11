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
        route_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        route_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dist_ch (None | str | Unset): Publisher field type: esriFieldTypeString
        dist_en (None | str | Unset): Publisher field type: esriFieldTypeString
        visit_t_c (None | str | Unset): Publisher field type: esriFieldTypeString
        visit_t_e (None | str | Unset): Publisher field type: esriFieldTypeString
        diff_c (None | str | Unset): Publisher field type: esriFieldTypeString
        diff_e (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    route_ch: None | str | Unset = UNSET
    route_en: None | str | Unset = UNSET
    dist_ch: None | str | Unset = UNSET
    dist_en: None | str | Unset = UNSET
    visit_t_c: None | str | Unset = UNSET
    visit_t_e: None | str | Unset = UNSET
    diff_c: None | str | Unset = UNSET
    diff_e: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        route_ch: None | str | Unset
        if isinstance(self.route_ch, Unset):
            route_ch = UNSET
        else:
            route_ch = self.route_ch

        route_en: None | str | Unset
        if isinstance(self.route_en, Unset):
            route_en = UNSET
        else:
            route_en = self.route_en

        dist_ch: None | str | Unset
        if isinstance(self.dist_ch, Unset):
            dist_ch = UNSET
        else:
            dist_ch = self.dist_ch

        dist_en: None | str | Unset
        if isinstance(self.dist_en, Unset):
            dist_en = UNSET
        else:
            dist_en = self.dist_en

        visit_t_c: None | str | Unset
        if isinstance(self.visit_t_c, Unset):
            visit_t_c = UNSET
        else:
            visit_t_c = self.visit_t_c

        visit_t_e: None | str | Unset
        if isinstance(self.visit_t_e, Unset):
            visit_t_e = UNSET
        else:
            visit_t_e = self.visit_t_e

        diff_c: None | str | Unset
        if isinstance(self.diff_c, Unset):
            diff_c = UNSET
        else:
            diff_c = self.diff_c

        diff_e: None | str | Unset
        if isinstance(self.diff_e, Unset):
            diff_e = UNSET
        else:
            diff_e = self.diff_e

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if route_ch is not UNSET:
            field_dict["Route_ch"] = route_ch
        if route_en is not UNSET:
            field_dict["Route_en"] = route_en
        if dist_ch is not UNSET:
            field_dict["Dist_ch"] = dist_ch
        if dist_en is not UNSET:
            field_dict["Dist_en"] = dist_en
        if visit_t_c is not UNSET:
            field_dict["Visit_T_c"] = visit_t_c
        if visit_t_e is not UNSET:
            field_dict["Visit_T_e"] = visit_t_e
        if diff_c is not UNSET:
            field_dict["Diff_c"] = diff_c
        if diff_e is not UNSET:
            field_dict["Diff_e"] = diff_e
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_route_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_ch = _parse_route_ch(d.pop("Route_ch", UNSET))

        def _parse_route_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        route_en = _parse_route_en(d.pop("Route_en", UNSET))

        def _parse_dist_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dist_ch = _parse_dist_ch(d.pop("Dist_ch", UNSET))

        def _parse_dist_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dist_en = _parse_dist_en(d.pop("Dist_en", UNSET))

        def _parse_visit_t_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visit_t_c = _parse_visit_t_c(d.pop("Visit_T_c", UNSET))

        def _parse_visit_t_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visit_t_e = _parse_visit_t_e(d.pop("Visit_T_e", UNSET))

        def _parse_diff_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        diff_c = _parse_diff_c(d.pop("Diff_c", UNSET))

        def _parse_diff_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        diff_e = _parse_diff_e(d.pop("Diff_e", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            route_ch=route_ch,
            route_en=route_en,
            dist_ch=dist_ch,
            dist_en=dist_en,
            visit_t_c=visit_t_c,
            visit_t_e=visit_t_e,
            diff_c=diff_c,
            diff_e=diff_e,
            shape_length=shape_length,
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
