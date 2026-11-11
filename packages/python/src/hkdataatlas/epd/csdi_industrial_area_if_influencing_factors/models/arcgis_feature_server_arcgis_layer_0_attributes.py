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
        plan_no (None | str | Unset): Publisher field type: esriFieldTypeString
        zone_label (None | str | Unset): Publisher field type: esriFieldTypeString
        desc_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        desc_cht (None | str | Unset): Publisher field type: esriFieldTypeString
        spuse_eng (None | str | Unset): Publisher field type: esriFieldTypeString
        spuse_cht (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_len (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_are (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    plan_no: None | str | Unset = UNSET
    zone_label: None | str | Unset = UNSET
    desc_eng: None | str | Unset = UNSET
    desc_cht: None | str | Unset = UNSET
    spuse_eng: None | str | Unset = UNSET
    spuse_cht: None | str | Unset = UNSET
    shape_len: float | None | Unset = UNSET
    shape_are: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plan_no: None | str | Unset
        if isinstance(self.plan_no, Unset):
            plan_no = UNSET
        else:
            plan_no = self.plan_no

        zone_label: None | str | Unset
        if isinstance(self.zone_label, Unset):
            zone_label = UNSET
        else:
            zone_label = self.zone_label

        desc_eng: None | str | Unset
        if isinstance(self.desc_eng, Unset):
            desc_eng = UNSET
        else:
            desc_eng = self.desc_eng

        desc_cht: None | str | Unset
        if isinstance(self.desc_cht, Unset):
            desc_cht = UNSET
        else:
            desc_cht = self.desc_cht

        spuse_eng: None | str | Unset
        if isinstance(self.spuse_eng, Unset):
            spuse_eng = UNSET
        else:
            spuse_eng = self.spuse_eng

        spuse_cht: None | str | Unset
        if isinstance(self.spuse_cht, Unset):
            spuse_cht = UNSET
        else:
            spuse_cht = self.spuse_cht

        shape_len: float | None | Unset
        if isinstance(self.shape_len, Unset):
            shape_len = UNSET
        else:
            shape_len = self.shape_len

        shape_are: float | None | Unset
        if isinstance(self.shape_are, Unset):
            shape_are = UNSET
        else:
            shape_are = self.shape_are

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
        if plan_no is not UNSET:
            field_dict["plan_no"] = plan_no
        if zone_label is not UNSET:
            field_dict["zone_label"] = zone_label
        if desc_eng is not UNSET:
            field_dict["desc_eng"] = desc_eng
        if desc_cht is not UNSET:
            field_dict["desc_cht"] = desc_cht
        if spuse_eng is not UNSET:
            field_dict["spuse_eng"] = spuse_eng
        if spuse_cht is not UNSET:
            field_dict["spuse_cht"] = spuse_cht
        if shape_len is not UNSET:
            field_dict["shape__len"] = shape_len
        if shape_are is not UNSET:
            field_dict["shape__are"] = shape_are
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

        def _parse_plan_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        plan_no = _parse_plan_no(d.pop("plan_no", UNSET))

        def _parse_zone_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        zone_label = _parse_zone_label(d.pop("zone_label", UNSET))

        def _parse_desc_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        desc_eng = _parse_desc_eng(d.pop("desc_eng", UNSET))

        def _parse_desc_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        desc_cht = _parse_desc_cht(d.pop("desc_cht", UNSET))

        def _parse_spuse_eng(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spuse_eng = _parse_spuse_eng(d.pop("spuse_eng", UNSET))

        def _parse_spuse_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spuse_cht = _parse_spuse_cht(d.pop("spuse_cht", UNSET))

        def _parse_shape_len(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_len = _parse_shape_len(d.pop("shape__len", UNSET))

        def _parse_shape_are(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_are = _parse_shape_are(d.pop("shape__are", UNSET))

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
            plan_no=plan_no,
            zone_label=zone_label,
            desc_eng=desc_eng,
            desc_cht=desc_cht,
            spuse_eng=spuse_eng,
            spuse_cht=spuse_cht,
            shape_len=shape_len,
            shape_are=shape_are,
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
