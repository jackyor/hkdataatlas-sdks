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
        ppu (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        spu (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        tpu (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        sb_vc (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    ppu: int | None | Unset = UNSET
    spu: int | None | Unset = UNSET
    tpu: int | None | Unset = UNSET
    sb_vc: int | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ppu: int | None | Unset
        if isinstance(self.ppu, Unset):
            ppu = UNSET
        else:
            ppu = self.ppu

        spu: int | None | Unset
        if isinstance(self.spu, Unset):
            spu = UNSET
        else:
            spu = self.spu

        tpu: int | None | Unset
        if isinstance(self.tpu, Unset):
            tpu = UNSET
        else:
            tpu = self.tpu

        sb_vc: int | None | Unset
        if isinstance(self.sb_vc, Unset):
            sb_vc = UNSET
        else:
            sb_vc = self.sb_vc

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
        if ppu is not UNSET:
            field_dict["PPU"] = ppu
        if spu is not UNSET:
            field_dict["SPU"] = spu
        if tpu is not UNSET:
            field_dict["TPU"] = tpu
        if sb_vc is not UNSET:
            field_dict["SB_VC"] = sb_vc
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

        def _parse_ppu(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ppu = _parse_ppu(d.pop("PPU", UNSET))

        def _parse_spu(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        spu = _parse_spu(d.pop("SPU", UNSET))

        def _parse_tpu(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tpu = _parse_tpu(d.pop("TPU", UNSET))

        def _parse_sb_vc(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sb_vc = _parse_sb_vc(d.pop("SB_VC", UNSET))

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
            ppu=ppu,
            spu=spu,
            tpu=tpu,
            sb_vc=sb_vc,
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
