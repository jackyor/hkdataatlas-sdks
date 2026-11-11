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
        pedestrian_route_id (int | Unset): Publisher field type: esriFieldTypeInteger
        location (int | Unset): Publisher field type: esriFieldTypeInteger
        feature_type (int | Unset): Publisher field type: esriFieldTypeInteger
        alias_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        alias_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        crossing_feature (int | None | Unset): Publisher field type: esriFieldTypeInteger
        weather_proof (int | Unset): Publisher field type: esriFieldTypeInteger
        wheelchair_barrier (int | Unset): Publisher field type: esriFieldTypeInteger
        wheelchair_access (int | Unset): Publisher field type: esriFieldTypeInteger
        obstacles_type (int | None | Unset): Publisher field type: esriFieldTypeInteger
        gradient (float | Unset): Publisher field type: esriFieldTypeDouble
        direction (int | Unset): Publisher field type: esriFieldTypeInteger
        position_certainty (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        enabled (int | Unset): Publisher field type: esriFieldTypeInteger
        data_source (int | Unset): Publisher field type: esriFieldTypeInteger
        level_source (int | Unset): Publisher field type: esriFieldTypeInteger
        street_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        street_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        st_code (int | None | Unset): Publisher field type: esriFieldTypeInteger
        floor_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        building_id_1 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        building_id_2 (int | None | Unset): Publisher field type: esriFieldTypeInteger
        site_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        terminal_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        access_time_id (int | None | Unset): Publisher field type: esriFieldTypeInteger
        creation_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        modified_by (str | Unset): Publisher field type: esriFieldTypeString
        last_amendment_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains
            unknown.
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    pedestrian_route_id: int | Unset = UNSET
    location: int | Unset = UNSET
    feature_type: int | Unset = UNSET
    alias_name_en: None | str | Unset = UNSET
    alias_name_tc: None | str | Unset = UNSET
    crossing_feature: int | None | Unset = UNSET
    weather_proof: int | Unset = UNSET
    wheelchair_barrier: int | Unset = UNSET
    wheelchair_access: int | Unset = UNSET
    obstacles_type: int | None | Unset = UNSET
    gradient: float | Unset = UNSET
    direction: int | Unset = UNSET
    position_certainty: int | None | Unset = UNSET
    enabled: int | Unset = UNSET
    data_source: int | Unset = UNSET
    level_source: int | Unset = UNSET
    street_name_en: None | str | Unset = UNSET
    street_name_tc: None | str | Unset = UNSET
    st_code: int | None | Unset = UNSET
    floor_id: int | None | Unset = UNSET
    building_id_1: int | None | Unset = UNSET
    building_id_2: int | None | Unset = UNSET
    site_id: int | None | Unset = UNSET
    terminal_id: int | None | Unset = UNSET
    access_time_id: int | None | Unset = UNSET
    creation_date: Any | Unset = UNSET
    modified_by: str | Unset = UNSET
    last_amendment_date: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        pedestrian_route_id = self.pedestrian_route_id

        location = self.location

        feature_type = self.feature_type

        alias_name_en: None | str | Unset
        if isinstance(self.alias_name_en, Unset):
            alias_name_en = UNSET
        else:
            alias_name_en = self.alias_name_en

        alias_name_tc: None | str | Unset
        if isinstance(self.alias_name_tc, Unset):
            alias_name_tc = UNSET
        else:
            alias_name_tc = self.alias_name_tc

        crossing_feature: int | None | Unset
        if isinstance(self.crossing_feature, Unset):
            crossing_feature = UNSET
        else:
            crossing_feature = self.crossing_feature

        weather_proof = self.weather_proof

        wheelchair_barrier = self.wheelchair_barrier

        wheelchair_access = self.wheelchair_access

        obstacles_type: int | None | Unset
        if isinstance(self.obstacles_type, Unset):
            obstacles_type = UNSET
        else:
            obstacles_type = self.obstacles_type

        gradient = self.gradient

        direction = self.direction

        position_certainty: int | None | Unset
        if isinstance(self.position_certainty, Unset):
            position_certainty = UNSET
        else:
            position_certainty = self.position_certainty

        enabled = self.enabled

        data_source = self.data_source

        level_source = self.level_source

        street_name_en: None | str | Unset
        if isinstance(self.street_name_en, Unset):
            street_name_en = UNSET
        else:
            street_name_en = self.street_name_en

        street_name_tc: None | str | Unset
        if isinstance(self.street_name_tc, Unset):
            street_name_tc = UNSET
        else:
            street_name_tc = self.street_name_tc

        st_code: int | None | Unset
        if isinstance(self.st_code, Unset):
            st_code = UNSET
        else:
            st_code = self.st_code

        floor_id: int | None | Unset
        if isinstance(self.floor_id, Unset):
            floor_id = UNSET
        else:
            floor_id = self.floor_id

        building_id_1: int | None | Unset
        if isinstance(self.building_id_1, Unset):
            building_id_1 = UNSET
        else:
            building_id_1 = self.building_id_1

        building_id_2: int | None | Unset
        if isinstance(self.building_id_2, Unset):
            building_id_2 = UNSET
        else:
            building_id_2 = self.building_id_2

        site_id: int | None | Unset
        if isinstance(self.site_id, Unset):
            site_id = UNSET
        else:
            site_id = self.site_id

        terminal_id: int | None | Unset
        if isinstance(self.terminal_id, Unset):
            terminal_id = UNSET
        else:
            terminal_id = self.terminal_id

        access_time_id: int | None | Unset
        if isinstance(self.access_time_id, Unset):
            access_time_id = UNSET
        else:
            access_time_id = self.access_time_id

        creation_date = self.creation_date

        modified_by = self.modified_by

        last_amendment_date = self.last_amendment_date

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if pedestrian_route_id is not UNSET:
            field_dict["PedestrianRouteID"] = pedestrian_route_id
        if location is not UNSET:
            field_dict["Location"] = location
        if feature_type is not UNSET:
            field_dict["FeatureType"] = feature_type
        if alias_name_en is not UNSET:
            field_dict["AliasNameEN"] = alias_name_en
        if alias_name_tc is not UNSET:
            field_dict["AliasNameTC"] = alias_name_tc
        if crossing_feature is not UNSET:
            field_dict["CrossingFeature"] = crossing_feature
        if weather_proof is not UNSET:
            field_dict["WeatherProof"] = weather_proof
        if wheelchair_barrier is not UNSET:
            field_dict["WheelchairBarrier"] = wheelchair_barrier
        if wheelchair_access is not UNSET:
            field_dict["WheelchairAccess"] = wheelchair_access
        if obstacles_type is not UNSET:
            field_dict["ObstaclesType"] = obstacles_type
        if gradient is not UNSET:
            field_dict["Gradient"] = gradient
        if direction is not UNSET:
            field_dict["Direction"] = direction
        if position_certainty is not UNSET:
            field_dict["PositionCertainty"] = position_certainty
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if data_source is not UNSET:
            field_dict["DataSource"] = data_source
        if level_source is not UNSET:
            field_dict["LevelSource"] = level_source
        if street_name_en is not UNSET:
            field_dict["StreetNameEN"] = street_name_en
        if street_name_tc is not UNSET:
            field_dict["StreetNameTC"] = street_name_tc
        if st_code is not UNSET:
            field_dict["ST_CODE"] = st_code
        if floor_id is not UNSET:
            field_dict["FloorID"] = floor_id
        if building_id_1 is not UNSET:
            field_dict["BuildingID_1"] = building_id_1
        if building_id_2 is not UNSET:
            field_dict["BuildingID_2"] = building_id_2
        if site_id is not UNSET:
            field_dict["SiteID"] = site_id
        if terminal_id is not UNSET:
            field_dict["TerminalID"] = terminal_id
        if access_time_id is not UNSET:
            field_dict["AccessTimeID"] = access_time_id
        if creation_date is not UNSET:
            field_dict["CreationDate"] = creation_date
        if modified_by is not UNSET:
            field_dict["ModifiedBy"] = modified_by
        if last_amendment_date is not UNSET:
            field_dict["LastAmendmentDate"] = last_amendment_date
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        pedestrian_route_id = d.pop("PedestrianRouteID", UNSET)

        location = d.pop("Location", UNSET)

        feature_type = d.pop("FeatureType", UNSET)

        def _parse_alias_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias_name_en = _parse_alias_name_en(d.pop("AliasNameEN", UNSET))

        def _parse_alias_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alias_name_tc = _parse_alias_name_tc(d.pop("AliasNameTC", UNSET))

        def _parse_crossing_feature(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        crossing_feature = _parse_crossing_feature(d.pop("CrossingFeature", UNSET))

        weather_proof = d.pop("WeatherProof", UNSET)

        wheelchair_barrier = d.pop("WheelchairBarrier", UNSET)

        wheelchair_access = d.pop("WheelchairAccess", UNSET)

        def _parse_obstacles_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        obstacles_type = _parse_obstacles_type(d.pop("ObstaclesType", UNSET))

        gradient = d.pop("Gradient", UNSET)

        direction = d.pop("Direction", UNSET)

        def _parse_position_certainty(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        position_certainty = _parse_position_certainty(
            d.pop("PositionCertainty", UNSET)
        )

        enabled = d.pop("Enabled", UNSET)

        data_source = d.pop("DataSource", UNSET)

        level_source = d.pop("LevelSource", UNSET)

        def _parse_street_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_name_en = _parse_street_name_en(d.pop("StreetNameEN", UNSET))

        def _parse_street_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_name_tc = _parse_street_name_tc(d.pop("StreetNameTC", UNSET))

        def _parse_st_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        st_code = _parse_st_code(d.pop("ST_CODE", UNSET))

        def _parse_floor_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        floor_id = _parse_floor_id(d.pop("FloorID", UNSET))

        def _parse_building_id_1(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        building_id_1 = _parse_building_id_1(d.pop("BuildingID_1", UNSET))

        def _parse_building_id_2(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        building_id_2 = _parse_building_id_2(d.pop("BuildingID_2", UNSET))

        def _parse_site_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        site_id = _parse_site_id(d.pop("SiteID", UNSET))

        def _parse_terminal_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        terminal_id = _parse_terminal_id(d.pop("TerminalID", UNSET))

        def _parse_access_time_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        access_time_id = _parse_access_time_id(d.pop("AccessTimeID", UNSET))

        creation_date = d.pop("CreationDate", UNSET)

        modified_by = d.pop("ModifiedBy", UNSET)

        last_amendment_date = d.pop("LastAmendmentDate", UNSET)

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            pedestrian_route_id=pedestrian_route_id,
            location=location,
            feature_type=feature_type,
            alias_name_en=alias_name_en,
            alias_name_tc=alias_name_tc,
            crossing_feature=crossing_feature,
            weather_proof=weather_proof,
            wheelchair_barrier=wheelchair_barrier,
            wheelchair_access=wheelchair_access,
            obstacles_type=obstacles_type,
            gradient=gradient,
            direction=direction,
            position_certainty=position_certainty,
            enabled=enabled,
            data_source=data_source,
            level_source=level_source,
            street_name_en=street_name_en,
            street_name_tc=street_name_tc,
            st_code=st_code,
            floor_id=floor_id,
            building_id_1=building_id_1,
            building_id_2=building_id_2,
            site_id=site_id,
            terminal_id=terminal_id,
            access_time_id=access_time_id,
            creation_date=creation_date,
            modified_by=modified_by,
            last_amendment_date=last_amendment_date,
            shape_length=shape_length,
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
