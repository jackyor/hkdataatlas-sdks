from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsBFFCHCCAttributes")


@_attrs_define
class WfsMapServerWfsBFFCHCCAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        accessible_entrance_exit_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        accessible_entrance_exit_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        accessible_lift_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        accessible_lift_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        accessible_toilet_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        accessible_toilet_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        accessible_carpark_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        accessible_carpark_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        accessible_public_info_counter_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        accessible_public_info_counter_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        visual_fire_alarm_system_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        visual_fire_alarm_system_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        accessibility_sign_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        accessibility_sign_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        tactile_guide_path_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        tactile_guide_path_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        brailleand_tactile_floor_plan_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        brailleand_tactile_floor_plan_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        assistive_listening_system_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        assistive_listening_system_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        bfa_common_area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        bfa_common_area_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        accessible_route_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        accessible_route_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        visual_display_board_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        visual_display_board_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        stg_movable_lifting_platform_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        stg_movable_lifting_platform_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        stg_fixed_lift_pl_tn_stair_lift_en (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        stg_fixed_lift_pl_tn_stair_lift_tc (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        stg_ramp_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        stg_ramp_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        last_update (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    accessible_entrance_exit_en: None | str | Unset = UNSET
    accessible_entrance_exit_tc: None | str | Unset = UNSET
    accessible_lift_en: None | str | Unset = UNSET
    accessible_lift_tc: None | str | Unset = UNSET
    accessible_toilet_en: None | str | Unset = UNSET
    accessible_toilet_tc: None | str | Unset = UNSET
    accessible_carpark_en: None | str | Unset = UNSET
    accessible_carpark_tc: None | str | Unset = UNSET
    accessible_public_info_counter_en: None | str | Unset = UNSET
    accessible_public_info_counter_tc: None | str | Unset = UNSET
    visual_fire_alarm_system_en: None | str | Unset = UNSET
    visual_fire_alarm_system_tc: None | str | Unset = UNSET
    accessibility_sign_en: None | str | Unset = UNSET
    accessibility_sign_tc: None | str | Unset = UNSET
    tactile_guide_path_en: None | str | Unset = UNSET
    tactile_guide_path_tc: None | str | Unset = UNSET
    brailleand_tactile_floor_plan_en: None | str | Unset = UNSET
    brailleand_tactile_floor_plan_tc: None | str | Unset = UNSET
    assistive_listening_system_en: None | str | Unset = UNSET
    assistive_listening_system_tc: None | str | Unset = UNSET
    bfa_common_area_en: None | str | Unset = UNSET
    bfa_common_area_tc: None | str | Unset = UNSET
    accessible_route_en: None | str | Unset = UNSET
    accessible_route_tc: None | str | Unset = UNSET
    visual_display_board_en: None | str | Unset = UNSET
    visual_display_board_tc: None | str | Unset = UNSET
    stg_movable_lifting_platform_en: None | str | Unset = UNSET
    stg_movable_lifting_platform_tc: None | str | Unset = UNSET
    stg_fixed_lift_pl_tn_stair_lift_en: None | str | Unset = UNSET
    stg_fixed_lift_pl_tn_stair_lift_tc: None | str | Unset = UNSET
    stg_ramp_en: None | str | Unset = UNSET
    stg_ramp_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    last_update: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        dataset_en: None | str | Unset
        if isinstance(self.dataset_en, Unset):
            dataset_en = UNSET
        else:
            dataset_en = self.dataset_en

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        accessible_entrance_exit_en: None | str | Unset
        if isinstance(self.accessible_entrance_exit_en, Unset):
            accessible_entrance_exit_en = UNSET
        else:
            accessible_entrance_exit_en = self.accessible_entrance_exit_en

        accessible_entrance_exit_tc: None | str | Unset
        if isinstance(self.accessible_entrance_exit_tc, Unset):
            accessible_entrance_exit_tc = UNSET
        else:
            accessible_entrance_exit_tc = self.accessible_entrance_exit_tc

        accessible_lift_en: None | str | Unset
        if isinstance(self.accessible_lift_en, Unset):
            accessible_lift_en = UNSET
        else:
            accessible_lift_en = self.accessible_lift_en

        accessible_lift_tc: None | str | Unset
        if isinstance(self.accessible_lift_tc, Unset):
            accessible_lift_tc = UNSET
        else:
            accessible_lift_tc = self.accessible_lift_tc

        accessible_toilet_en: None | str | Unset
        if isinstance(self.accessible_toilet_en, Unset):
            accessible_toilet_en = UNSET
        else:
            accessible_toilet_en = self.accessible_toilet_en

        accessible_toilet_tc: None | str | Unset
        if isinstance(self.accessible_toilet_tc, Unset):
            accessible_toilet_tc = UNSET
        else:
            accessible_toilet_tc = self.accessible_toilet_tc

        accessible_carpark_en: None | str | Unset
        if isinstance(self.accessible_carpark_en, Unset):
            accessible_carpark_en = UNSET
        else:
            accessible_carpark_en = self.accessible_carpark_en

        accessible_carpark_tc: None | str | Unset
        if isinstance(self.accessible_carpark_tc, Unset):
            accessible_carpark_tc = UNSET
        else:
            accessible_carpark_tc = self.accessible_carpark_tc

        accessible_public_info_counter_en: None | str | Unset
        if isinstance(self.accessible_public_info_counter_en, Unset):
            accessible_public_info_counter_en = UNSET
        else:
            accessible_public_info_counter_en = self.accessible_public_info_counter_en

        accessible_public_info_counter_tc: None | str | Unset
        if isinstance(self.accessible_public_info_counter_tc, Unset):
            accessible_public_info_counter_tc = UNSET
        else:
            accessible_public_info_counter_tc = self.accessible_public_info_counter_tc

        visual_fire_alarm_system_en: None | str | Unset
        if isinstance(self.visual_fire_alarm_system_en, Unset):
            visual_fire_alarm_system_en = UNSET
        else:
            visual_fire_alarm_system_en = self.visual_fire_alarm_system_en

        visual_fire_alarm_system_tc: None | str | Unset
        if isinstance(self.visual_fire_alarm_system_tc, Unset):
            visual_fire_alarm_system_tc = UNSET
        else:
            visual_fire_alarm_system_tc = self.visual_fire_alarm_system_tc

        accessibility_sign_en: None | str | Unset
        if isinstance(self.accessibility_sign_en, Unset):
            accessibility_sign_en = UNSET
        else:
            accessibility_sign_en = self.accessibility_sign_en

        accessibility_sign_tc: None | str | Unset
        if isinstance(self.accessibility_sign_tc, Unset):
            accessibility_sign_tc = UNSET
        else:
            accessibility_sign_tc = self.accessibility_sign_tc

        tactile_guide_path_en: None | str | Unset
        if isinstance(self.tactile_guide_path_en, Unset):
            tactile_guide_path_en = UNSET
        else:
            tactile_guide_path_en = self.tactile_guide_path_en

        tactile_guide_path_tc: None | str | Unset
        if isinstance(self.tactile_guide_path_tc, Unset):
            tactile_guide_path_tc = UNSET
        else:
            tactile_guide_path_tc = self.tactile_guide_path_tc

        brailleand_tactile_floor_plan_en: None | str | Unset
        if isinstance(self.brailleand_tactile_floor_plan_en, Unset):
            brailleand_tactile_floor_plan_en = UNSET
        else:
            brailleand_tactile_floor_plan_en = self.brailleand_tactile_floor_plan_en

        brailleand_tactile_floor_plan_tc: None | str | Unset
        if isinstance(self.brailleand_tactile_floor_plan_tc, Unset):
            brailleand_tactile_floor_plan_tc = UNSET
        else:
            brailleand_tactile_floor_plan_tc = self.brailleand_tactile_floor_plan_tc

        assistive_listening_system_en: None | str | Unset
        if isinstance(self.assistive_listening_system_en, Unset):
            assistive_listening_system_en = UNSET
        else:
            assistive_listening_system_en = self.assistive_listening_system_en

        assistive_listening_system_tc: None | str | Unset
        if isinstance(self.assistive_listening_system_tc, Unset):
            assistive_listening_system_tc = UNSET
        else:
            assistive_listening_system_tc = self.assistive_listening_system_tc

        bfa_common_area_en: None | str | Unset
        if isinstance(self.bfa_common_area_en, Unset):
            bfa_common_area_en = UNSET
        else:
            bfa_common_area_en = self.bfa_common_area_en

        bfa_common_area_tc: None | str | Unset
        if isinstance(self.bfa_common_area_tc, Unset):
            bfa_common_area_tc = UNSET
        else:
            bfa_common_area_tc = self.bfa_common_area_tc

        accessible_route_en: None | str | Unset
        if isinstance(self.accessible_route_en, Unset):
            accessible_route_en = UNSET
        else:
            accessible_route_en = self.accessible_route_en

        accessible_route_tc: None | str | Unset
        if isinstance(self.accessible_route_tc, Unset):
            accessible_route_tc = UNSET
        else:
            accessible_route_tc = self.accessible_route_tc

        visual_display_board_en: None | str | Unset
        if isinstance(self.visual_display_board_en, Unset):
            visual_display_board_en = UNSET
        else:
            visual_display_board_en = self.visual_display_board_en

        visual_display_board_tc: None | str | Unset
        if isinstance(self.visual_display_board_tc, Unset):
            visual_display_board_tc = UNSET
        else:
            visual_display_board_tc = self.visual_display_board_tc

        stg_movable_lifting_platform_en: None | str | Unset
        if isinstance(self.stg_movable_lifting_platform_en, Unset):
            stg_movable_lifting_platform_en = UNSET
        else:
            stg_movable_lifting_platform_en = self.stg_movable_lifting_platform_en

        stg_movable_lifting_platform_tc: None | str | Unset
        if isinstance(self.stg_movable_lifting_platform_tc, Unset):
            stg_movable_lifting_platform_tc = UNSET
        else:
            stg_movable_lifting_platform_tc = self.stg_movable_lifting_platform_tc

        stg_fixed_lift_pl_tn_stair_lift_en: None | str | Unset
        if isinstance(self.stg_fixed_lift_pl_tn_stair_lift_en, Unset):
            stg_fixed_lift_pl_tn_stair_lift_en = UNSET
        else:
            stg_fixed_lift_pl_tn_stair_lift_en = self.stg_fixed_lift_pl_tn_stair_lift_en

        stg_fixed_lift_pl_tn_stair_lift_tc: None | str | Unset
        if isinstance(self.stg_fixed_lift_pl_tn_stair_lift_tc, Unset):
            stg_fixed_lift_pl_tn_stair_lift_tc = UNSET
        else:
            stg_fixed_lift_pl_tn_stair_lift_tc = self.stg_fixed_lift_pl_tn_stair_lift_tc

        stg_ramp_en: None | str | Unset
        if isinstance(self.stg_ramp_en, Unset):
            stg_ramp_en = UNSET
        else:
            stg_ramp_en = self.stg_ramp_en

        stg_ramp_tc: None | str | Unset
        if isinstance(self.stg_ramp_tc, Unset):
            stg_ramp_tc = UNSET
        else:
            stg_ramp_tc = self.stg_ramp_tc

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

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

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["shape"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if dataset_en is not UNSET:
            field_dict["DatasetEN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["DatasetTC"] = dataset_tc
        if name_en is not UNSET:
            field_dict["NameEN"] = name_en
        if address_en is not UNSET:
            field_dict["AddressEN"] = address_en
        if name_tc is not UNSET:
            field_dict["NameTC"] = name_tc
        if address_tc is not UNSET:
            field_dict["AddressTC"] = address_tc
        if accessible_entrance_exit_en is not UNSET:
            field_dict["AccessibleEntranceExitEN"] = accessible_entrance_exit_en
        if accessible_entrance_exit_tc is not UNSET:
            field_dict["AccessibleEntranceExitTC"] = accessible_entrance_exit_tc
        if accessible_lift_en is not UNSET:
            field_dict["AccessibleLiftEN"] = accessible_lift_en
        if accessible_lift_tc is not UNSET:
            field_dict["AccessibleLiftTC"] = accessible_lift_tc
        if accessible_toilet_en is not UNSET:
            field_dict["AccessibleToiletEN"] = accessible_toilet_en
        if accessible_toilet_tc is not UNSET:
            field_dict["AccessibleToiletTC"] = accessible_toilet_tc
        if accessible_carpark_en is not UNSET:
            field_dict["AccessibleCarparkEN"] = accessible_carpark_en
        if accessible_carpark_tc is not UNSET:
            field_dict["AccessibleCarparkTC"] = accessible_carpark_tc
        if accessible_public_info_counter_en is not UNSET:
            field_dict["AccessiblePublicInfoCounterEN"] = (
                accessible_public_info_counter_en
            )
        if accessible_public_info_counter_tc is not UNSET:
            field_dict["AccessiblePublicInfoCounterTC"] = (
                accessible_public_info_counter_tc
            )
        if visual_fire_alarm_system_en is not UNSET:
            field_dict["VisualFireAlarmSystemEN"] = visual_fire_alarm_system_en
        if visual_fire_alarm_system_tc is not UNSET:
            field_dict["VisualFireAlarmSystemTC"] = visual_fire_alarm_system_tc
        if accessibility_sign_en is not UNSET:
            field_dict["AccessibilitySignEN"] = accessibility_sign_en
        if accessibility_sign_tc is not UNSET:
            field_dict["AccessibilitySignTC"] = accessibility_sign_tc
        if tactile_guide_path_en is not UNSET:
            field_dict["TactileGuidePathEN"] = tactile_guide_path_en
        if tactile_guide_path_tc is not UNSET:
            field_dict["TactileGuidePathTC"] = tactile_guide_path_tc
        if brailleand_tactile_floor_plan_en is not UNSET:
            field_dict["BrailleandTactileFloorPlanEN"] = (
                brailleand_tactile_floor_plan_en
            )
        if brailleand_tactile_floor_plan_tc is not UNSET:
            field_dict["BrailleandTactileFloorPlanTC"] = (
                brailleand_tactile_floor_plan_tc
            )
        if assistive_listening_system_en is not UNSET:
            field_dict["AssistiveListeningSystemEN"] = assistive_listening_system_en
        if assistive_listening_system_tc is not UNSET:
            field_dict["AssistiveListeningSystemTC"] = assistive_listening_system_tc
        if bfa_common_area_en is not UNSET:
            field_dict["BFACommonAreaEN"] = bfa_common_area_en
        if bfa_common_area_tc is not UNSET:
            field_dict["BFACommonAreaTC"] = bfa_common_area_tc
        if accessible_route_en is not UNSET:
            field_dict["AccessibleRouteEN"] = accessible_route_en
        if accessible_route_tc is not UNSET:
            field_dict["AccessibleRouteTC"] = accessible_route_tc
        if visual_display_board_en is not UNSET:
            field_dict["VisualDisplayBoardEN"] = visual_display_board_en
        if visual_display_board_tc is not UNSET:
            field_dict["VisualDisplayBoardTC"] = visual_display_board_tc
        if stg_movable_lifting_platform_en is not UNSET:
            field_dict["StgMovableLiftingPlatformEN"] = stg_movable_lifting_platform_en
        if stg_movable_lifting_platform_tc is not UNSET:
            field_dict["StgMovableLiftingPlatformTC"] = stg_movable_lifting_platform_tc
        if stg_fixed_lift_pl_tn_stair_lift_en is not UNSET:
            field_dict["StgFixedLiftPLTnStairLiftEN"] = (
                stg_fixed_lift_pl_tn_stair_lift_en
            )
        if stg_fixed_lift_pl_tn_stair_lift_tc is not UNSET:
            field_dict["StgFixedLiftPLTnStairLiftTC"] = (
                stg_fixed_lift_pl_tn_stair_lift_tc
            )
        if stg_ramp_en is not UNSET:
            field_dict["StgRampEN"] = stg_ramp_en
        if stg_ramp_tc is not UNSET:
            field_dict["StgRampTC"] = stg_ramp_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("shape", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("DatasetEN", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DatasetTC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NameEN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("AddressEN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NameTC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("AddressTC", UNSET))

        def _parse_accessible_entrance_exit_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_entrance_exit_en = _parse_accessible_entrance_exit_en(
            d.pop("AccessibleEntranceExitEN", UNSET)
        )

        def _parse_accessible_entrance_exit_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_entrance_exit_tc = _parse_accessible_entrance_exit_tc(
            d.pop("AccessibleEntranceExitTC", UNSET)
        )

        def _parse_accessible_lift_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_lift_en = _parse_accessible_lift_en(d.pop("AccessibleLiftEN", UNSET))

        def _parse_accessible_lift_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_lift_tc = _parse_accessible_lift_tc(d.pop("AccessibleLiftTC", UNSET))

        def _parse_accessible_toilet_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_toilet_en = _parse_accessible_toilet_en(
            d.pop("AccessibleToiletEN", UNSET)
        )

        def _parse_accessible_toilet_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_toilet_tc = _parse_accessible_toilet_tc(
            d.pop("AccessibleToiletTC", UNSET)
        )

        def _parse_accessible_carpark_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_carpark_en = _parse_accessible_carpark_en(
            d.pop("AccessibleCarparkEN", UNSET)
        )

        def _parse_accessible_carpark_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_carpark_tc = _parse_accessible_carpark_tc(
            d.pop("AccessibleCarparkTC", UNSET)
        )

        def _parse_accessible_public_info_counter_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_public_info_counter_en = _parse_accessible_public_info_counter_en(
            d.pop("AccessiblePublicInfoCounterEN", UNSET)
        )

        def _parse_accessible_public_info_counter_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_public_info_counter_tc = _parse_accessible_public_info_counter_tc(
            d.pop("AccessiblePublicInfoCounterTC", UNSET)
        )

        def _parse_visual_fire_alarm_system_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visual_fire_alarm_system_en = _parse_visual_fire_alarm_system_en(
            d.pop("VisualFireAlarmSystemEN", UNSET)
        )

        def _parse_visual_fire_alarm_system_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visual_fire_alarm_system_tc = _parse_visual_fire_alarm_system_tc(
            d.pop("VisualFireAlarmSystemTC", UNSET)
        )

        def _parse_accessibility_sign_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessibility_sign_en = _parse_accessibility_sign_en(
            d.pop("AccessibilitySignEN", UNSET)
        )

        def _parse_accessibility_sign_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessibility_sign_tc = _parse_accessibility_sign_tc(
            d.pop("AccessibilitySignTC", UNSET)
        )

        def _parse_tactile_guide_path_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tactile_guide_path_en = _parse_tactile_guide_path_en(
            d.pop("TactileGuidePathEN", UNSET)
        )

        def _parse_tactile_guide_path_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tactile_guide_path_tc = _parse_tactile_guide_path_tc(
            d.pop("TactileGuidePathTC", UNSET)
        )

        def _parse_brailleand_tactile_floor_plan_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brailleand_tactile_floor_plan_en = _parse_brailleand_tactile_floor_plan_en(
            d.pop("BrailleandTactileFloorPlanEN", UNSET)
        )

        def _parse_brailleand_tactile_floor_plan_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        brailleand_tactile_floor_plan_tc = _parse_brailleand_tactile_floor_plan_tc(
            d.pop("BrailleandTactileFloorPlanTC", UNSET)
        )

        def _parse_assistive_listening_system_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assistive_listening_system_en = _parse_assistive_listening_system_en(
            d.pop("AssistiveListeningSystemEN", UNSET)
        )

        def _parse_assistive_listening_system_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        assistive_listening_system_tc = _parse_assistive_listening_system_tc(
            d.pop("AssistiveListeningSystemTC", UNSET)
        )

        def _parse_bfa_common_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bfa_common_area_en = _parse_bfa_common_area_en(d.pop("BFACommonAreaEN", UNSET))

        def _parse_bfa_common_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bfa_common_area_tc = _parse_bfa_common_area_tc(d.pop("BFACommonAreaTC", UNSET))

        def _parse_accessible_route_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_route_en = _parse_accessible_route_en(
            d.pop("AccessibleRouteEN", UNSET)
        )

        def _parse_accessible_route_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessible_route_tc = _parse_accessible_route_tc(
            d.pop("AccessibleRouteTC", UNSET)
        )

        def _parse_visual_display_board_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visual_display_board_en = _parse_visual_display_board_en(
            d.pop("VisualDisplayBoardEN", UNSET)
        )

        def _parse_visual_display_board_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        visual_display_board_tc = _parse_visual_display_board_tc(
            d.pop("VisualDisplayBoardTC", UNSET)
        )

        def _parse_stg_movable_lifting_platform_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stg_movable_lifting_platform_en = _parse_stg_movable_lifting_platform_en(
            d.pop("StgMovableLiftingPlatformEN", UNSET)
        )

        def _parse_stg_movable_lifting_platform_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stg_movable_lifting_platform_tc = _parse_stg_movable_lifting_platform_tc(
            d.pop("StgMovableLiftingPlatformTC", UNSET)
        )

        def _parse_stg_fixed_lift_pl_tn_stair_lift_en(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stg_fixed_lift_pl_tn_stair_lift_en = _parse_stg_fixed_lift_pl_tn_stair_lift_en(
            d.pop("StgFixedLiftPLTnStairLiftEN", UNSET)
        )

        def _parse_stg_fixed_lift_pl_tn_stair_lift_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stg_fixed_lift_pl_tn_stair_lift_tc = _parse_stg_fixed_lift_pl_tn_stair_lift_tc(
            d.pop("StgFixedLiftPLTnStairLiftTC", UNSET)
        )

        def _parse_stg_ramp_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stg_ramp_en = _parse_stg_ramp_en(d.pop("StgRampEN", UNSET))

        def _parse_stg_ramp_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stg_ramp_tc = _parse_stg_ramp_tc(d.pop("StgRampTC", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

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

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("LastUpdate", UNSET))

        wfs_map_server_wfs_bffchcc_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            accessible_entrance_exit_en=accessible_entrance_exit_en,
            accessible_entrance_exit_tc=accessible_entrance_exit_tc,
            accessible_lift_en=accessible_lift_en,
            accessible_lift_tc=accessible_lift_tc,
            accessible_toilet_en=accessible_toilet_en,
            accessible_toilet_tc=accessible_toilet_tc,
            accessible_carpark_en=accessible_carpark_en,
            accessible_carpark_tc=accessible_carpark_tc,
            accessible_public_info_counter_en=accessible_public_info_counter_en,
            accessible_public_info_counter_tc=accessible_public_info_counter_tc,
            visual_fire_alarm_system_en=visual_fire_alarm_system_en,
            visual_fire_alarm_system_tc=visual_fire_alarm_system_tc,
            accessibility_sign_en=accessibility_sign_en,
            accessibility_sign_tc=accessibility_sign_tc,
            tactile_guide_path_en=tactile_guide_path_en,
            tactile_guide_path_tc=tactile_guide_path_tc,
            brailleand_tactile_floor_plan_en=brailleand_tactile_floor_plan_en,
            brailleand_tactile_floor_plan_tc=brailleand_tactile_floor_plan_tc,
            assistive_listening_system_en=assistive_listening_system_en,
            assistive_listening_system_tc=assistive_listening_system_tc,
            bfa_common_area_en=bfa_common_area_en,
            bfa_common_area_tc=bfa_common_area_tc,
            accessible_route_en=accessible_route_en,
            accessible_route_tc=accessible_route_tc,
            visual_display_board_en=visual_display_board_en,
            visual_display_board_tc=visual_display_board_tc,
            stg_movable_lifting_platform_en=stg_movable_lifting_platform_en,
            stg_movable_lifting_platform_tc=stg_movable_lifting_platform_tc,
            stg_fixed_lift_pl_tn_stair_lift_en=stg_fixed_lift_pl_tn_stair_lift_en,
            stg_fixed_lift_pl_tn_stair_lift_tc=stg_fixed_lift_pl_tn_stair_lift_tc,
            stg_ramp_en=stg_ramp_en,
            stg_ramp_tc=stg_ramp_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            last_update=last_update,
        )

        wfs_map_server_wfs_bffchcc_attributes.additional_properties = d
        return wfs_map_server_wfs_bffchcc_attributes

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
