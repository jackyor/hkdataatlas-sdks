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
        department_tree_id (None | str | Unset): Publisher field type: esriFieldTypeString
        tmcp_tree_id (None | str | Unset): Publisher field type: esriFieldTypeString
        tree_speices (None | str | Unset): Publisher field type: esriFieldTypeString
        location_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        masterzone_ref (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_zone_ref (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dbh_mm (None | str | Unset): Publisher field type: esriFieldTypeString
        height_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        crown_spread_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        triage_color (None | str | Unset): Publisher field type: esriFieldTypeString
        tree_register_no (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    department_tree_id: None | str | Unset = UNSET
    tmcp_tree_id: None | str | Unset = UNSET
    tree_speices: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    masterzone_ref: None | str | Unset = UNSET
    sub_zone_ref: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    dbh_mm: None | str | Unset = UNSET
    height_m: float | None | Unset = UNSET
    crown_spread_m: float | None | Unset = UNSET
    triage_color: None | str | Unset = UNSET
    tree_register_no: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        department_tree_id: None | str | Unset
        if isinstance(self.department_tree_id, Unset):
            department_tree_id = UNSET
        else:
            department_tree_id = self.department_tree_id

        tmcp_tree_id: None | str | Unset
        if isinstance(self.tmcp_tree_id, Unset):
            tmcp_tree_id = UNSET
        else:
            tmcp_tree_id = self.tmcp_tree_id

        tree_speices: None | str | Unset
        if isinstance(self.tree_speices, Unset):
            tree_speices = UNSET
        else:
            tree_speices = self.tree_speices

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        location_tc: None | str | Unset
        if isinstance(self.location_tc, Unset):
            location_tc = UNSET
        else:
            location_tc = self.location_tc

        masterzone_ref: None | str | Unset
        if isinstance(self.masterzone_ref, Unset):
            masterzone_ref = UNSET
        else:
            masterzone_ref = self.masterzone_ref

        sub_zone_ref: None | str | Unset
        if isinstance(self.sub_zone_ref, Unset):
            sub_zone_ref = UNSET
        else:
            sub_zone_ref = self.sub_zone_ref

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

        dbh_mm: None | str | Unset
        if isinstance(self.dbh_mm, Unset):
            dbh_mm = UNSET
        else:
            dbh_mm = self.dbh_mm

        height_m: float | None | Unset
        if isinstance(self.height_m, Unset):
            height_m = UNSET
        else:
            height_m = self.height_m

        crown_spread_m: float | None | Unset
        if isinstance(self.crown_spread_m, Unset):
            crown_spread_m = UNSET
        else:
            crown_spread_m = self.crown_spread_m

        triage_color: None | str | Unset
        if isinstance(self.triage_color, Unset):
            triage_color = UNSET
        else:
            triage_color = self.triage_color

        tree_register_no: None | str | Unset
        if isinstance(self.tree_register_no, Unset):
            tree_register_no = UNSET
        else:
            tree_register_no = self.tree_register_no

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if department_tree_id is not UNSET:
            field_dict["Department_Tree_ID"] = department_tree_id
        if tmcp_tree_id is not UNSET:
            field_dict["TMCP_Tree_ID"] = tmcp_tree_id
        if tree_speices is not UNSET:
            field_dict["Tree_Speices"] = tree_speices
        if location_en is not UNSET:
            field_dict["Location_EN"] = location_en
        if location_tc is not UNSET:
            field_dict["Location_TC"] = location_tc
        if masterzone_ref is not UNSET:
            field_dict["Masterzone_Ref"] = masterzone_ref
        if sub_zone_ref is not UNSET:
            field_dict["SubZone_Ref"] = sub_zone_ref
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if dbh_mm is not UNSET:
            field_dict["DBH_MM"] = dbh_mm
        if height_m is not UNSET:
            field_dict["Height_M"] = height_m
        if crown_spread_m is not UNSET:
            field_dict["Crown_Spread_M"] = crown_spread_m
        if triage_color is not UNSET:
            field_dict["Triage_Color"] = triage_color
        if tree_register_no is not UNSET:
            field_dict["Tree_Register_No"] = tree_register_no
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_department_tree_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department_tree_id = _parse_department_tree_id(
            d.pop("Department_Tree_ID", UNSET)
        )

        def _parse_tmcp_tree_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tmcp_tree_id = _parse_tmcp_tree_id(d.pop("TMCP_Tree_ID", UNSET))

        def _parse_tree_speices(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_speices = _parse_tree_speices(d.pop("Tree_Speices", UNSET))

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("Location_EN", UNSET))

        def _parse_location_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_tc = _parse_location_tc(d.pop("Location_TC", UNSET))

        def _parse_masterzone_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        masterzone_ref = _parse_masterzone_ref(d.pop("Masterzone_Ref", UNSET))

        def _parse_sub_zone_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_zone_ref = _parse_sub_zone_ref(d.pop("SubZone_Ref", UNSET))

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

        def _parse_dbh_mm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dbh_mm = _parse_dbh_mm(d.pop("DBH_MM", UNSET))

        def _parse_height_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height_m = _parse_height_m(d.pop("Height_M", UNSET))

        def _parse_crown_spread_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        crown_spread_m = _parse_crown_spread_m(d.pop("Crown_Spread_M", UNSET))

        def _parse_triage_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        triage_color = _parse_triage_color(d.pop("Triage_Color", UNSET))

        def _parse_tree_register_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_register_no = _parse_tree_register_no(d.pop("Tree_Register_No", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            department_tree_id=department_tree_id,
            tmcp_tree_id=tmcp_tree_id,
            tree_speices=tree_speices,
            location_en=location_en,
            location_tc=location_tc,
            masterzone_ref=masterzone_ref,
            sub_zone_ref=sub_zone_ref,
            latitude=latitude,
            longitude=longitude,
            dbh_mm=dbh_mm,
            height_m=height_m,
            crown_spread_m=crown_spread_m,
            triage_color=triage_color,
            tree_register_no=tree_register_no,
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
