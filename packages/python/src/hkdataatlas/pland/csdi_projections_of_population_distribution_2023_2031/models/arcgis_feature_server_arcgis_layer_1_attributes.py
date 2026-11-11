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
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
        new_town_en (None | str | Unset): Publisher field type: esriFieldTypeString
        new_town_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        new_town_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        y2021 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2022 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2023 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2024 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2025 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2026 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2027 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2028 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2029 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2030 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        y2031 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid_1: int | Unset = UNSET
    new_town_en: None | str | Unset = UNSET
    new_town_tc: None | str | Unset = UNSET
    new_town_sc: None | str | Unset = UNSET
    y2021: int | None | Unset = UNSET
    y2022: int | None | Unset = UNSET
    y2023: int | None | Unset = UNSET
    y2024: int | None | Unset = UNSET
    y2025: int | None | Unset = UNSET
    y2026: int | None | Unset = UNSET
    y2027: int | None | Unset = UNSET
    y2028: int | None | Unset = UNSET
    y2029: int | None | Unset = UNSET
    y2030: int | None | Unset = UNSET
    y2031: int | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid_1 = self.objectid_1

        new_town_en: None | str | Unset
        if isinstance(self.new_town_en, Unset):
            new_town_en = UNSET
        else:
            new_town_en = self.new_town_en

        new_town_tc: None | str | Unset
        if isinstance(self.new_town_tc, Unset):
            new_town_tc = UNSET
        else:
            new_town_tc = self.new_town_tc

        new_town_sc: None | str | Unset
        if isinstance(self.new_town_sc, Unset):
            new_town_sc = UNSET
        else:
            new_town_sc = self.new_town_sc

        y2021: int | None | Unset
        if isinstance(self.y2021, Unset):
            y2021 = UNSET
        else:
            y2021 = self.y2021

        y2022: int | None | Unset
        if isinstance(self.y2022, Unset):
            y2022 = UNSET
        else:
            y2022 = self.y2022

        y2023: int | None | Unset
        if isinstance(self.y2023, Unset):
            y2023 = UNSET
        else:
            y2023 = self.y2023

        y2024: int | None | Unset
        if isinstance(self.y2024, Unset):
            y2024 = UNSET
        else:
            y2024 = self.y2024

        y2025: int | None | Unset
        if isinstance(self.y2025, Unset):
            y2025 = UNSET
        else:
            y2025 = self.y2025

        y2026: int | None | Unset
        if isinstance(self.y2026, Unset):
            y2026 = UNSET
        else:
            y2026 = self.y2026

        y2027: int | None | Unset
        if isinstance(self.y2027, Unset):
            y2027 = UNSET
        else:
            y2027 = self.y2027

        y2028: int | None | Unset
        if isinstance(self.y2028, Unset):
            y2028 = UNSET
        else:
            y2028 = self.y2028

        y2029: int | None | Unset
        if isinstance(self.y2029, Unset):
            y2029 = UNSET
        else:
            y2029 = self.y2029

        y2030: int | None | Unset
        if isinstance(self.y2030, Unset):
            y2030 = UNSET
        else:
            y2030 = self.y2030

        y2031: int | None | Unset
        if isinstance(self.y2031, Unset):
            y2031 = UNSET
        else:
            y2031 = self.y2031

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
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
        if new_town_en is not UNSET:
            field_dict["NewTown_en"] = new_town_en
        if new_town_tc is not UNSET:
            field_dict["NewTown_Tc"] = new_town_tc
        if new_town_sc is not UNSET:
            field_dict["NewTown_Sc"] = new_town_sc
        if y2021 is not UNSET:
            field_dict["Y2021"] = y2021
        if y2022 is not UNSET:
            field_dict["Y2022"] = y2022
        if y2023 is not UNSET:
            field_dict["Y2023"] = y2023
        if y2024 is not UNSET:
            field_dict["Y2024"] = y2024
        if y2025 is not UNSET:
            field_dict["Y2025"] = y2025
        if y2026 is not UNSET:
            field_dict["Y2026"] = y2026
        if y2027 is not UNSET:
            field_dict["Y2027"] = y2027
        if y2028 is not UNSET:
            field_dict["Y2028"] = y2028
        if y2029 is not UNSET:
            field_dict["Y2029"] = y2029
        if y2030 is not UNSET:
            field_dict["Y2030"] = y2030
        if y2031 is not UNSET:
            field_dict["Y2031"] = y2031
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid_1 = d.pop("OBJECTID_1", UNSET)

        def _parse_new_town_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_town_en = _parse_new_town_en(d.pop("NewTown_en", UNSET))

        def _parse_new_town_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_town_tc = _parse_new_town_tc(d.pop("NewTown_Tc", UNSET))

        def _parse_new_town_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_town_sc = _parse_new_town_sc(d.pop("NewTown_Sc", UNSET))

        def _parse_y2021(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2021 = _parse_y2021(d.pop("Y2021", UNSET))

        def _parse_y2022(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2022 = _parse_y2022(d.pop("Y2022", UNSET))

        def _parse_y2023(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2023 = _parse_y2023(d.pop("Y2023", UNSET))

        def _parse_y2024(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2024 = _parse_y2024(d.pop("Y2024", UNSET))

        def _parse_y2025(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2025 = _parse_y2025(d.pop("Y2025", UNSET))

        def _parse_y2026(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2026 = _parse_y2026(d.pop("Y2026", UNSET))

        def _parse_y2027(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2027 = _parse_y2027(d.pop("Y2027", UNSET))

        def _parse_y2028(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2028 = _parse_y2028(d.pop("Y2028", UNSET))

        def _parse_y2029(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2029 = _parse_y2029(d.pop("Y2029", UNSET))

        def _parse_y2030(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2030 = _parse_y2030(d.pop("Y2030", UNSET))

        def _parse_y2031(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        y2031 = _parse_y2031(d.pop("Y2031", UNSET))

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

        arcgis_feature_server_arcgis_layer_1_attributes = cls(
            objectid_1=objectid_1,
            new_town_en=new_town_en,
            new_town_tc=new_town_tc,
            new_town_sc=new_town_sc,
            y2021=y2021,
            y2022=y2022,
            y2023=y2023,
            y2024=y2024,
            y2025=y2025,
            y2026=y2026,
            y2027=y2027,
            y2028=y2028,
            y2029=y2029,
            y2030=y2030,
            y2031=y2031,
            shape_length=shape_length,
            shape_area=shape_area,
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
