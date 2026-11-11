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
        name_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        y2021_popu (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2021_empl (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2026_popu (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2026_empl (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2031_popu (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2031_empl (int | None | Unset): Publisher field type: esriFieldTypeInteger
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    name_eng: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    y2021_popu: int | None | Unset = UNSET
    y2021_empl: int | None | Unset = UNSET
    y2026_popu: int | None | Unset = UNSET
    y2026_empl: int | None | Unset = UNSET
    y2031_popu: int | None | Unset = UNSET
    y2031_empl: int | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        name_eng: None | str | Unset
        if isinstance(self.name_eng, Unset):
            name_eng = UNSET
        else:
            name_eng = self.name_eng

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        y2021_popu: int | None | Unset
        if isinstance(self.y2021_popu, Unset):
            y2021_popu = UNSET
        else:
            y2021_popu = self.y2021_popu

        y2021_empl: int | None | Unset
        if isinstance(self.y2021_empl, Unset):
            y2021_empl = UNSET
        else:
            y2021_empl = self.y2021_empl

        y2026_popu: int | None | Unset
        if isinstance(self.y2026_popu, Unset):
            y2026_popu = UNSET
        else:
            y2026_popu = self.y2026_popu

        y2026_empl: int | None | Unset
        if isinstance(self.y2026_empl, Unset):
            y2026_empl = UNSET
        else:
            y2026_empl = self.y2026_empl

        y2031_popu: int | None | Unset
        if isinstance(self.y2031_popu, Unset):
            y2031_popu = UNSET
        else:
            y2031_popu = self.y2031_popu

        y2031_empl: int | None | Unset
        if isinstance(self.y2031_empl, Unset):
            y2031_empl = UNSET
        else:
            y2031_empl = self.y2031_empl

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
        if name_eng is not UNSET:
            field_dict["Name_Eng"] = name_eng
        if name_tc is not UNSET:
            field_dict["Name_TC"] = name_tc
        if name_sc is not UNSET:
            field_dict["Name_SC"] = name_sc
        if y2021_popu is not UNSET:
            field_dict["Y2021_Popu"] = y2021_popu
        if y2021_empl is not UNSET:
            field_dict["Y2021_Empl"] = y2021_empl
        if y2026_popu is not UNSET:
            field_dict["Y2026_Popu"] = y2026_popu
        if y2026_empl is not UNSET:
            field_dict["Y2026_Empl"] = y2026_empl
        if y2031_popu is not UNSET:
            field_dict["Y2031_Popu"] = y2031_popu
        if y2031_empl is not UNSET:
            field_dict["Y2031_Empl"] = y2031_empl
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_name_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_eng = _parse_name_eng(d.pop("Name_Eng", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("Name_TC", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("Name_SC", UNSET))

        def _parse_y2021_popu(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2021_popu = _parse_y2021_popu(d.pop("Y2021_Popu", UNSET))

        def _parse_y2021_empl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2021_empl = _parse_y2021_empl(d.pop("Y2021_Empl", UNSET))

        def _parse_y2026_popu(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2026_popu = _parse_y2026_popu(d.pop("Y2026_Popu", UNSET))

        def _parse_y2026_empl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2026_empl = _parse_y2026_empl(d.pop("Y2026_Empl", UNSET))

        def _parse_y2031_popu(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2031_popu = _parse_y2031_popu(d.pop("Y2031_Popu", UNSET))

        def _parse_y2031_empl(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2031_empl = _parse_y2031_empl(d.pop("Y2031_Empl", UNSET))

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
            name_eng=name_eng,
            name_tc=name_tc,
            name_sc=name_sc,
            y2021_popu=y2021_popu,
            y2021_empl=y2021_empl,
            y2026_popu=y2026_popu,
            y2026_empl=y2026_empl,
            y2031_popu=y2031_popu,
            y2031_empl=y2031_empl,
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
