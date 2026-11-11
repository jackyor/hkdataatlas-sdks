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
        department_tree_id (None | str | Unset): Publisher field type: esriFieldTypeString
        tmcp_tree_id (None | str | Unset): Publisher field type: esriFieldTypeString
        tree_register_no (None | str | Unset): Publisher field type: esriFieldTypeString
        ovt_ref_no (None | str | Unset): Publisher field type: esriFieldTypeString
        department (None | str | Unset): Publisher field type: esriFieldTypeString
        tree_species (None | str | Unset): Publisher field type: esriFieldTypeString
        x_coordinate (float | None | Unset): Publisher field type: esriFieldTypeDouble
        y_coordinate (float | None | Unset): Publisher field type: esriFieldTypeDouble
        location_english (None | str | Unset): Publisher field type: esriFieldTypeString
        location_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        masterzone_ref (None | str | Unset): Publisher field type: esriFieldTypeString
        sub_zone_ref (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        height_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        dbh_mm (float | None | Unset): Publisher field type: esriFieldTypeDouble
        crown_spread_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        triage_color (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    department_tree_id: None | str | Unset = UNSET
    tmcp_tree_id: None | str | Unset = UNSET
    tree_register_no: None | str | Unset = UNSET
    ovt_ref_no: None | str | Unset = UNSET
    department: None | str | Unset = UNSET
    tree_species: None | str | Unset = UNSET
    x_coordinate: float | None | Unset = UNSET
    y_coordinate: float | None | Unset = UNSET
    location_english: None | str | Unset = UNSET
    location_chinese: None | str | Unset = UNSET
    masterzone_ref: None | str | Unset = UNSET
    sub_zone_ref: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    height_m: float | None | Unset = UNSET
    dbh_mm: float | None | Unset = UNSET
    crown_spread_m: float | None | Unset = UNSET
    triage_color: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

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

        tree_register_no: None | str | Unset
        if isinstance(self.tree_register_no, Unset):
            tree_register_no = UNSET
        else:
            tree_register_no = self.tree_register_no

        ovt_ref_no: None | str | Unset
        if isinstance(self.ovt_ref_no, Unset):
            ovt_ref_no = UNSET
        else:
            ovt_ref_no = self.ovt_ref_no

        department: None | str | Unset
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        tree_species: None | str | Unset
        if isinstance(self.tree_species, Unset):
            tree_species = UNSET
        else:
            tree_species = self.tree_species

        x_coordinate: float | None | Unset
        if isinstance(self.x_coordinate, Unset):
            x_coordinate = UNSET
        else:
            x_coordinate = self.x_coordinate

        y_coordinate: float | None | Unset
        if isinstance(self.y_coordinate, Unset):
            y_coordinate = UNSET
        else:
            y_coordinate = self.y_coordinate

        location_english: None | str | Unset
        if isinstance(self.location_english, Unset):
            location_english = UNSET
        else:
            location_english = self.location_english

        location_chinese: None | str | Unset
        if isinstance(self.location_chinese, Unset):
            location_chinese = UNSET
        else:
            location_chinese = self.location_chinese

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

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        height_m: float | None | Unset
        if isinstance(self.height_m, Unset):
            height_m = UNSET
        else:
            height_m = self.height_m

        dbh_mm: float | None | Unset
        if isinstance(self.dbh_mm, Unset):
            dbh_mm = UNSET
        else:
            dbh_mm = self.dbh_mm

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if department_tree_id is not UNSET:
            field_dict["Department_Tree_ID"] = department_tree_id
        if tmcp_tree_id is not UNSET:
            field_dict["TMCP_Tree_ID"] = tmcp_tree_id
        if tree_register_no is not UNSET:
            field_dict["Tree_Register_No"] = tree_register_no
        if ovt_ref_no is not UNSET:
            field_dict["OVT_Ref_No"] = ovt_ref_no
        if department is not UNSET:
            field_dict["Department"] = department
        if tree_species is not UNSET:
            field_dict["Tree_Species"] = tree_species
        if x_coordinate is not UNSET:
            field_dict["X_Coordinate"] = x_coordinate
        if y_coordinate is not UNSET:
            field_dict["Y_Coordinate"] = y_coordinate
        if location_english is not UNSET:
            field_dict["Location_English"] = location_english
        if location_chinese is not UNSET:
            field_dict["Location_Chinese"] = location_chinese
        if masterzone_ref is not UNSET:
            field_dict["Masterzone_Ref"] = masterzone_ref
        if sub_zone_ref is not UNSET:
            field_dict["SubZone_Ref"] = sub_zone_ref
        if district is not UNSET:
            field_dict["District"] = district
        if height_m is not UNSET:
            field_dict["Height_m"] = height_m
        if dbh_mm is not UNSET:
            field_dict["DBH_mm"] = dbh_mm
        if crown_spread_m is not UNSET:
            field_dict["Crown_Spread_m"] = crown_spread_m
        if triage_color is not UNSET:
            field_dict["Triage_Color"] = triage_color

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

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

        def _parse_tree_register_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_register_no = _parse_tree_register_no(d.pop("Tree_Register_No", UNSET))

        def _parse_ovt_ref_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ovt_ref_no = _parse_ovt_ref_no(d.pop("OVT_Ref_No", UNSET))

        def _parse_department(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department = _parse_department(d.pop("Department", UNSET))

        def _parse_tree_species(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tree_species = _parse_tree_species(d.pop("Tree_Species", UNSET))

        def _parse_x_coordinate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        x_coordinate = _parse_x_coordinate(d.pop("X_Coordinate", UNSET))

        def _parse_y_coordinate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        y_coordinate = _parse_y_coordinate(d.pop("Y_Coordinate", UNSET))

        def _parse_location_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_english = _parse_location_english(d.pop("Location_English", UNSET))

        def _parse_location_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_chinese = _parse_location_chinese(d.pop("Location_Chinese", UNSET))

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

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("District", UNSET))

        def _parse_height_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        height_m = _parse_height_m(d.pop("Height_m", UNSET))

        def _parse_dbh_mm(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        dbh_mm = _parse_dbh_mm(d.pop("DBH_mm", UNSET))

        def _parse_crown_spread_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        crown_spread_m = _parse_crown_spread_m(d.pop("Crown_Spread_m", UNSET))

        def _parse_triage_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        triage_color = _parse_triage_color(d.pop("Triage_Color", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            department_tree_id=department_tree_id,
            tmcp_tree_id=tmcp_tree_id,
            tree_register_no=tree_register_no,
            ovt_ref_no=ovt_ref_no,
            department=department,
            tree_species=tree_species,
            x_coordinate=x_coordinate,
            y_coordinate=y_coordinate,
            location_english=location_english,
            location_chinese=location_chinese,
            masterzone_ref=masterzone_ref,
            sub_zone_ref=sub_zone_ref,
            district=district,
            height_m=height_m,
            dbh_mm=dbh_mm,
            crown_spread_m=crown_spread_m,
            triage_color=triage_color,
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
