from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer6Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer6Attributes:
    """
    Attributes:
        name_ec (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        length_ec (None | str | Unset): Publisher field type: esriFieldTypeString
        length_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_details_ec (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_details_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    name_ec: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    length_ec: None | str | Unset = UNSET
    length_tc: None | str | Unset = UNSET
    opening_details_ec: None | str | Unset = UNSET
    opening_details_tc: None | str | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_ec: None | str | Unset
        if isinstance(self.name_ec, Unset):
            name_ec = UNSET
        else:
            name_ec = self.name_ec

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        length_ec: None | str | Unset
        if isinstance(self.length_ec, Unset):
            length_ec = UNSET
        else:
            length_ec = self.length_ec

        length_tc: None | str | Unset
        if isinstance(self.length_tc, Unset):
            length_tc = UNSET
        else:
            length_tc = self.length_tc

        opening_details_ec: None | str | Unset
        if isinstance(self.opening_details_ec, Unset):
            opening_details_ec = UNSET
        else:
            opening_details_ec = self.opening_details_ec

        opening_details_tc: None | str | Unset
        if isinstance(self.opening_details_tc, Unset):
            opening_details_tc = UNSET
        else:
            opening_details_tc = self.opening_details_tc

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

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
        if name_ec is not UNSET:
            field_dict["Name_EC"] = name_ec
        if name_tc is not UNSET:
            field_dict["Name_TC"] = name_tc
        if length_ec is not UNSET:
            field_dict["Length_EC"] = length_ec
        if length_tc is not UNSET:
            field_dict["Length_TC"] = length_tc
        if opening_details_ec is not UNSET:
            field_dict["Opening_Details_EC"] = opening_details_ec
        if opening_details_tc is not UNSET:
            field_dict["Opening_Details_TC"] = opening_details_tc
        if fid is not UNSET:
            field_dict["fid"] = fid
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

        def _parse_name_ec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_ec = _parse_name_ec(d.pop("Name_EC", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("Name_TC", UNSET))

        def _parse_length_ec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        length_ec = _parse_length_ec(d.pop("Length_EC", UNSET))

        def _parse_length_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        length_tc = _parse_length_tc(d.pop("Length_TC", UNSET))

        def _parse_opening_details_ec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_details_ec = _parse_opening_details_ec(
            d.pop("Opening_Details_EC", UNSET)
        )

        def _parse_opening_details_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_details_tc = _parse_opening_details_tc(
            d.pop("Opening_Details_TC", UNSET)
        )

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

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

        arcgis_feature_server_arcgis_layer_6_attributes = cls(
            name_ec=name_ec,
            name_tc=name_tc,
            length_ec=length_ec,
            length_tc=length_tc,
            opening_details_ec=opening_details_ec,
            opening_details_tc=opening_details_tc,
            fid=fid,
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        arcgis_feature_server_arcgis_layer_6_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_6_attributes

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
