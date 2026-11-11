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
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        point_grid_reference (None | str | Unset): Publisher field type: esriFieldTypeString
        point_en (None | str | Unset): Publisher field type: esriFieldTypeString
        point_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_1_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remark_1_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        task_en (None | str | Unset): Publisher field type: esriFieldTypeString
        task_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    point_grid_reference: None | str | Unset = UNSET
    point_en: None | str | Unset = UNSET
    point_tc: None | str | Unset = UNSET
    remark_1_en: None | str | Unset = UNSET
    remark_1_tc: None | str | Unset = UNSET
    task_en: None | str | Unset = UNSET
    task_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        point_grid_reference: None | str | Unset
        if isinstance(self.point_grid_reference, Unset):
            point_grid_reference = UNSET
        else:
            point_grid_reference = self.point_grid_reference

        point_en: None | str | Unset
        if isinstance(self.point_en, Unset):
            point_en = UNSET
        else:
            point_en = self.point_en

        point_tc: None | str | Unset
        if isinstance(self.point_tc, Unset):
            point_tc = UNSET
        else:
            point_tc = self.point_tc

        remark_1_en: None | str | Unset
        if isinstance(self.remark_1_en, Unset):
            remark_1_en = UNSET
        else:
            remark_1_en = self.remark_1_en

        remark_1_tc: None | str | Unset
        if isinstance(self.remark_1_tc, Unset):
            remark_1_tc = UNSET
        else:
            remark_1_tc = self.remark_1_tc

        task_en: None | str | Unset
        if isinstance(self.task_en, Unset):
            task_en = UNSET
        else:
            task_en = self.task_en

        task_tc: None | str | Unset
        if isinstance(self.task_tc, Unset):
            task_tc = UNSET
        else:
            task_tc = self.task_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if point_grid_reference is not UNSET:
            field_dict["Point_Grid_Reference"] = point_grid_reference
        if point_en is not UNSET:
            field_dict["Point_en"] = point_en
        if point_tc is not UNSET:
            field_dict["Point_tc"] = point_tc
        if remark_1_en is not UNSET:
            field_dict["Remark1_en"] = remark_1_en
        if remark_1_tc is not UNSET:
            field_dict["Remark1_tc"] = remark_1_tc
        if task_en is not UNSET:
            field_dict["Task_en"] = task_en
        if task_tc is not UNSET:
            field_dict["Task_tc"] = task_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_point_grid_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        point_grid_reference = _parse_point_grid_reference(
            d.pop("Point_Grid_Reference", UNSET)
        )

        def _parse_point_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        point_en = _parse_point_en(d.pop("Point_en", UNSET))

        def _parse_point_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        point_tc = _parse_point_tc(d.pop("Point_tc", UNSET))

        def _parse_remark_1_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_1_en = _parse_remark_1_en(d.pop("Remark1_en", UNSET))

        def _parse_remark_1_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remark_1_tc = _parse_remark_1_tc(d.pop("Remark1_tc", UNSET))

        def _parse_task_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_en = _parse_task_en(d.pop("Task_en", UNSET))

        def _parse_task_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        task_tc = _parse_task_tc(d.pop("Task_tc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            latitude=latitude,
            longitude=longitude,
            point_grid_reference=point_grid_reference,
            point_en=point_en,
            point_tc=point_tc,
            remark_1_en=remark_1_en,
            remark_1_tc=remark_1_tc,
            task_en=task_en,
            task_tc=task_tc,
            objectid=objectid,
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
