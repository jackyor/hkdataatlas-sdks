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
        name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        name_chi (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_leng (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    name_eng: None | str | Unset = UNSET
    name_chi: None | str | Unset = UNSET
    shape_leng: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_eng: None | str | Unset
        if isinstance(self.name_eng, Unset):
            name_eng = UNSET
        else:
            name_eng = self.name_eng

        name_chi: None | str | Unset
        if isinstance(self.name_chi, Unset):
            name_chi = UNSET
        else:
            name_chi = self.name_chi

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
        if name_eng is not UNSET:
            field_dict["NAME_ENG"] = name_eng
        if name_chi is not UNSET:
            field_dict["NAME_CHI"] = name_chi
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

        def _parse_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_eng = _parse_name_eng(d.pop("NAME_ENG", UNSET))

        def _parse_name_chi(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_chi = _parse_name_chi(d.pop("NAME_CHI", UNSET))

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

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            name_eng=name_eng,
            name_chi=name_chi,
            shape_leng=shape_leng,
            objectid=objectid,
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
