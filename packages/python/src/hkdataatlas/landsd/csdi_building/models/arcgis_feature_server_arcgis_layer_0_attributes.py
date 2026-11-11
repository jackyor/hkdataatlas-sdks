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
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
        geo_ref_no (str | Unset): Publisher field type: esriFieldTypeString
        date_create (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        building_block_type (str | Unset): Publisher field type: esriFieldTypeString
        building_csuid (str | Unset): Publisher field type: esriFieldTypeString
        building_id (int | Unset): Publisher field type: esriFieldTypeInteger
        status (str | Unset): Publisher field type: esriFieldTypeString
        building_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        building_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        base_height (float | None | Unset): Publisher field type: esriFieldTypeDouble
        top_height (float | None | Unset): Publisher field type: esriFieldTypeDouble
        storeys (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        storeys_in_basement (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        date_stamp (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
    """

    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    geo_ref_no: str | Unset = UNSET
    date_create: Any | Unset = UNSET
    building_block_type: str | Unset = UNSET
    building_csuid: str | Unset = UNSET
    building_id: int | Unset = UNSET
    status: str | Unset = UNSET
    building_name_en: None | str | Unset = UNSET
    building_name_tc: None | str | Unset = UNSET
    base_height: float | None | Unset = UNSET
    top_height: float | None | Unset = UNSET
    storeys: int | None | Unset = UNSET
    storeys_in_basement: int | None | Unset = UNSET
    date_stamp: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        geo_ref_no = self.geo_ref_no

        date_create = self.date_create

        building_block_type = self.building_block_type

        building_csuid = self.building_csuid

        building_id = self.building_id

        status = self.status

        building_name_en: None | str | Unset
        if isinstance(self.building_name_en, Unset):
            building_name_en = UNSET
        else:
            building_name_en = self.building_name_en

        building_name_tc: None | str | Unset
        if isinstance(self.building_name_tc, Unset):
            building_name_tc = UNSET
        else:
            building_name_tc = self.building_name_tc

        base_height: float | None | Unset
        if isinstance(self.base_height, Unset):
            base_height = UNSET
        else:
            base_height = self.base_height

        top_height: float | None | Unset
        if isinstance(self.top_height, Unset):
            top_height = UNSET
        else:
            top_height = self.top_height

        storeys: int | None | Unset
        if isinstance(self.storeys, Unset):
            storeys = UNSET
        else:
            storeys = self.storeys

        storeys_in_basement: int | None | Unset
        if isinstance(self.storeys_in_basement, Unset):
            storeys_in_basement = UNSET
        else:
            storeys_in_basement = self.storeys_in_basement

        date_stamp = self.date_stamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area
        if geo_ref_no is not UNSET:
            field_dict["GeoRefNo"] = geo_ref_no
        if date_create is not UNSET:
            field_dict["DateCreate"] = date_create
        if building_block_type is not UNSET:
            field_dict["BuildingBlockType"] = building_block_type
        if building_csuid is not UNSET:
            field_dict["BuildingCSUID"] = building_csuid
        if building_id is not UNSET:
            field_dict["BuildingID"] = building_id
        if status is not UNSET:
            field_dict["Status"] = status
        if building_name_en is not UNSET:
            field_dict["BuildingNameEN"] = building_name_en
        if building_name_tc is not UNSET:
            field_dict["BuildingNameTC"] = building_name_tc
        if base_height is not UNSET:
            field_dict["BaseHeight"] = base_height
        if top_height is not UNSET:
            field_dict["TopHeight"] = top_height
        if storeys is not UNSET:
            field_dict["Storeys"] = storeys
        if storeys_in_basement is not UNSET:
            field_dict["StoreysInBasement"] = storeys_in_basement
        if date_stamp is not UNSET:
            field_dict["DateStamp"] = date_stamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
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

        geo_ref_no = d.pop("GeoRefNo", UNSET)

        date_create = d.pop("DateCreate", UNSET)

        building_block_type = d.pop("BuildingBlockType", UNSET)

        building_csuid = d.pop("BuildingCSUID", UNSET)

        building_id = d.pop("BuildingID", UNSET)

        status = d.pop("Status", UNSET)

        def _parse_building_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_name_en = _parse_building_name_en(d.pop("BuildingNameEN", UNSET))

        def _parse_building_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_name_tc = _parse_building_name_tc(d.pop("BuildingNameTC", UNSET))

        def _parse_base_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        base_height = _parse_base_height(d.pop("BaseHeight", UNSET))

        def _parse_top_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        top_height = _parse_top_height(d.pop("TopHeight", UNSET))

        def _parse_storeys(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storeys = _parse_storeys(d.pop("Storeys", UNSET))

        def _parse_storeys_in_basement(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storeys_in_basement = _parse_storeys_in_basement(
            d.pop("StoreysInBasement", UNSET)
        )

        date_stamp = d.pop("DateStamp", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            shape_length=shape_length,
            shape_area=shape_area,
            geo_ref_no=geo_ref_no,
            date_create=date_create,
            building_block_type=building_block_type,
            building_csuid=building_csuid,
            building_id=building_id,
            status=status,
            building_name_en=building_name_en,
            building_name_tc=building_name_tc,
            base_height=base_height,
            top_height=top_height,
            storeys=storeys,
            storeys_in_basement=storeys_in_basement,
            date_stamp=date_stamp,
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
