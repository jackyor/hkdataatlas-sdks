from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTPUAttributes")


@_attrs_define
class WfsMapServerWfsTPUAttributes:
    """
    Attributes:
        objectid_1 (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        tpu (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        y2021 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        y2022 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        y2023 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        y2024 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        y2025 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        y2026 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        y2027 (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid_1: int | Unset = UNSET
    shape: Any | Unset = UNSET
    area_en: None | str | Unset = UNSET
    area_tc: None | str | Unset = UNSET
    area_sc: None | str | Unset = UNSET
    tpu: None | str | Unset = UNSET
    y2021: int | None | Unset = UNSET
    y2022: int | None | Unset = UNSET
    y2023: int | None | Unset = UNSET
    y2024: int | None | Unset = UNSET
    y2025: int | None | Unset = UNSET
    y2026: int | None | Unset = UNSET
    y2027: int | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid_1 = self.objectid_1

        shape = self.shape

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        area_tc: None | str | Unset
        if isinstance(self.area_tc, Unset):
            area_tc = UNSET
        else:
            area_tc = self.area_tc

        area_sc: None | str | Unset
        if isinstance(self.area_sc, Unset):
            area_sc = UNSET
        else:
            area_sc = self.area_sc

        tpu: None | str | Unset
        if isinstance(self.tpu, Unset):
            tpu = UNSET
        else:
            tpu = self.tpu

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
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if area_en is not UNSET:
            field_dict["area_en"] = area_en
        if area_tc is not UNSET:
            field_dict["area_tc"] = area_tc
        if area_sc is not UNSET:
            field_dict["area_sc"] = area_sc
        if tpu is not UNSET:
            field_dict["TPU"] = tpu
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
        if shape_length is not UNSET:
            field_dict["Shape_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid_1 = d.pop("OBJECTID_1", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("area_en", UNSET))

        def _parse_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_tc = _parse_area_tc(d.pop("area_tc", UNSET))

        def _parse_area_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_sc = _parse_area_sc(d.pop("area_sc", UNSET))

        def _parse_tpu(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tpu = _parse_tpu(d.pop("TPU", UNSET))

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

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape_Area", UNSET))

        wfs_map_server_wfs_tpu_attributes = cls(
            objectid_1=objectid_1,
            shape=shape,
            area_en=area_en,
            area_tc=area_tc,
            area_sc=area_sc,
            tpu=tpu,
            y2021=y2021,
            y2022=y2022,
            y2023=y2023,
            y2024=y2024,
            y2025=y2025,
            y2026=y2026,
            y2027=y2027,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_tpu_attributes.additional_properties = d
        return wfs_map_server_wfs_tpu_attributes

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
