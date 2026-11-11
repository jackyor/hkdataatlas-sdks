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
        grid_name (None | str | Unset): Publisher field type: esriFieldTypeString
        loc_en (None | str | Unset): Publisher field type: esriFieldTypeString
        loc_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        loc_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        min_x (float | None | Unset): Publisher field type: esriFieldTypeDouble
        min_y (float | None | Unset): Publisher field type: esriFieldTypeDouble
        max_x (float | None | Unset): Publisher field type: esriFieldTypeDouble
        max_y (float | None | Unset): Publisher field type: esriFieldTypeDouble
        min_lng (float | None | Unset): Publisher field type: esriFieldTypeDouble
        min_lat (float | None | Unset): Publisher field type: esriFieldTypeDouble
        max_lng (float | None | Unset): Publisher field type: esriFieldTypeDouble
        max_lat (float | None | Unset): Publisher field type: esriFieldTypeDouble
        modi_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        osgb_url (None | str | Unset): Publisher field type: esriFieldTypeString
        obj_url (None | str | Unset): Publisher field type: esriFieldTypeString
        cesium_url (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_leng (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    grid_name: None | str | Unset = UNSET
    loc_en: None | str | Unset = UNSET
    loc_tc: None | str | Unset = UNSET
    loc_sc: None | str | Unset = UNSET
    min_x: float | None | Unset = UNSET
    min_y: float | None | Unset = UNSET
    max_x: float | None | Unset = UNSET
    max_y: float | None | Unset = UNSET
    min_lng: float | None | Unset = UNSET
    min_lat: float | None | Unset = UNSET
    max_lng: float | None | Unset = UNSET
    max_lat: float | None | Unset = UNSET
    modi_date: Any | Unset = UNSET
    osgb_url: None | str | Unset = UNSET
    obj_url: None | str | Unset = UNSET
    cesium_url: None | str | Unset = UNSET
    shape_leng: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grid_name: None | str | Unset
        if isinstance(self.grid_name, Unset):
            grid_name = UNSET
        else:
            grid_name = self.grid_name

        loc_en: None | str | Unset
        if isinstance(self.loc_en, Unset):
            loc_en = UNSET
        else:
            loc_en = self.loc_en

        loc_tc: None | str | Unset
        if isinstance(self.loc_tc, Unset):
            loc_tc = UNSET
        else:
            loc_tc = self.loc_tc

        loc_sc: None | str | Unset
        if isinstance(self.loc_sc, Unset):
            loc_sc = UNSET
        else:
            loc_sc = self.loc_sc

        min_x: float | None | Unset
        if isinstance(self.min_x, Unset):
            min_x = UNSET
        else:
            min_x = self.min_x

        min_y: float | None | Unset
        if isinstance(self.min_y, Unset):
            min_y = UNSET
        else:
            min_y = self.min_y

        max_x: float | None | Unset
        if isinstance(self.max_x, Unset):
            max_x = UNSET
        else:
            max_x = self.max_x

        max_y: float | None | Unset
        if isinstance(self.max_y, Unset):
            max_y = UNSET
        else:
            max_y = self.max_y

        min_lng: float | None | Unset
        if isinstance(self.min_lng, Unset):
            min_lng = UNSET
        else:
            min_lng = self.min_lng

        min_lat: float | None | Unset
        if isinstance(self.min_lat, Unset):
            min_lat = UNSET
        else:
            min_lat = self.min_lat

        max_lng: float | None | Unset
        if isinstance(self.max_lng, Unset):
            max_lng = UNSET
        else:
            max_lng = self.max_lng

        max_lat: float | None | Unset
        if isinstance(self.max_lat, Unset):
            max_lat = UNSET
        else:
            max_lat = self.max_lat

        modi_date = self.modi_date

        osgb_url: None | str | Unset
        if isinstance(self.osgb_url, Unset):
            osgb_url = UNSET
        else:
            osgb_url = self.osgb_url

        obj_url: None | str | Unset
        if isinstance(self.obj_url, Unset):
            obj_url = UNSET
        else:
            obj_url = self.obj_url

        cesium_url: None | str | Unset
        if isinstance(self.cesium_url, Unset):
            cesium_url = UNSET
        else:
            cesium_url = self.cesium_url

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

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grid_name is not UNSET:
            field_dict["GRID_NAME"] = grid_name
        if loc_en is not UNSET:
            field_dict["LOC_EN"] = loc_en
        if loc_tc is not UNSET:
            field_dict["LOC_TC"] = loc_tc
        if loc_sc is not UNSET:
            field_dict["LOC_SC"] = loc_sc
        if min_x is not UNSET:
            field_dict["MIN_X"] = min_x
        if min_y is not UNSET:
            field_dict["MIN_Y"] = min_y
        if max_x is not UNSET:
            field_dict["MAX_X"] = max_x
        if max_y is not UNSET:
            field_dict["MAX_Y"] = max_y
        if min_lng is not UNSET:
            field_dict["MIN_LNG"] = min_lng
        if min_lat is not UNSET:
            field_dict["MIN_LAT"] = min_lat
        if max_lng is not UNSET:
            field_dict["MAX_LNG"] = max_lng
        if max_lat is not UNSET:
            field_dict["MAX_LAT"] = max_lat
        if modi_date is not UNSET:
            field_dict["MODI_DATE"] = modi_date
        if osgb_url is not UNSET:
            field_dict["OSGB_URL"] = osgb_url
        if obj_url is not UNSET:
            field_dict["OBJ_URL"] = obj_url
        if cesium_url is not UNSET:
            field_dict["Cesium_URL"] = cesium_url
        if shape_leng is not UNSET:
            field_dict["Shape_Leng"] = shape_leng
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

        def _parse_grid_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        grid_name = _parse_grid_name(d.pop("GRID_NAME", UNSET))

        def _parse_loc_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loc_en = _parse_loc_en(d.pop("LOC_EN", UNSET))

        def _parse_loc_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loc_tc = _parse_loc_tc(d.pop("LOC_TC", UNSET))

        def _parse_loc_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        loc_sc = _parse_loc_sc(d.pop("LOC_SC", UNSET))

        def _parse_min_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_x = _parse_min_x(d.pop("MIN_X", UNSET))

        def _parse_min_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_y = _parse_min_y(d.pop("MIN_Y", UNSET))

        def _parse_max_x(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_x = _parse_max_x(d.pop("MAX_X", UNSET))

        def _parse_max_y(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_y = _parse_max_y(d.pop("MAX_Y", UNSET))

        def _parse_min_lng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_lng = _parse_min_lng(d.pop("MIN_LNG", UNSET))

        def _parse_min_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_lat = _parse_min_lat(d.pop("MIN_LAT", UNSET))

        def _parse_max_lng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_lng = _parse_max_lng(d.pop("MAX_LNG", UNSET))

        def _parse_max_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_lat = _parse_max_lat(d.pop("MAX_LAT", UNSET))

        modi_date = d.pop("MODI_DATE", UNSET)

        def _parse_osgb_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        osgb_url = _parse_osgb_url(d.pop("OSGB_URL", UNSET))

        def _parse_obj_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        obj_url = _parse_obj_url(d.pop("OBJ_URL", UNSET))

        def _parse_cesium_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cesium_url = _parse_cesium_url(d.pop("Cesium_URL", UNSET))

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

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            grid_name=grid_name,
            loc_en=loc_en,
            loc_tc=loc_tc,
            loc_sc=loc_sc,
            min_x=min_x,
            min_y=min_y,
            max_x=max_x,
            max_y=max_y,
            min_lng=min_lng,
            min_lat=min_lat,
            max_lng=max_lng,
            max_lat=max_lat,
            modi_date=modi_date,
            osgb_url=osgb_url,
            obj_url=obj_url,
            cesium_url=cesium_url,
            shape_leng=shape_leng,
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
