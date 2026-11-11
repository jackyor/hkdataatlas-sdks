from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable296Attributes")


@_attrs_define
class WfsMapServerWfsTable296Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        cost (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        cost_occupancy_operational_cost (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        premises (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        premises_suitable_premises_floor_space (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        premises_renew (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        premises_poor_building (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        premises_redevelopment (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        accessibility (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        accessibility_poor_local_transport (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        accessibility_inadequate_parking (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        accessibility_poor_cross_boundary (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        agglomeration_economies (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        agglomeration_economies_head_office (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        agglomeration_economies_far_regular_contacts (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        agglomeration_economies_far_like_business (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        agglomeration_economies_insufficient_supporting (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        environment_and_amenities (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        environment_poor_quality (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        prestige (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        prestige_location_not_prestigious (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        others (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        others_reduce_in_scope (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        others_bought_new_property (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        others_sell_property (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        others_fung_shui (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    cost: int | None | Unset = UNSET
    cost_occupancy_operational_cost: int | None | Unset = UNSET
    premises: int | None | Unset = UNSET
    premises_suitable_premises_floor_space: int | None | Unset = UNSET
    premises_renew: int | None | Unset = UNSET
    premises_poor_building: int | None | Unset = UNSET
    premises_redevelopment: int | None | Unset = UNSET
    accessibility: int | None | Unset = UNSET
    accessibility_poor_local_transport: int | None | Unset = UNSET
    accessibility_inadequate_parking: int | None | Unset = UNSET
    accessibility_poor_cross_boundary: int | None | Unset = UNSET
    agglomeration_economies: int | None | Unset = UNSET
    agglomeration_economies_head_office: int | None | Unset = UNSET
    agglomeration_economies_far_regular_contacts: int | None | Unset = UNSET
    agglomeration_economies_far_like_business: int | None | Unset = UNSET
    agglomeration_economies_insufficient_supporting: None | str | Unset = UNSET
    environment_and_amenities: int | None | Unset = UNSET
    environment_poor_quality: int | None | Unset = UNSET
    prestige: int | None | Unset = UNSET
    prestige_location_not_prestigious: int | None | Unset = UNSET
    others: int | None | Unset = UNSET
    others_reduce_in_scope: int | None | Unset = UNSET
    others_bought_new_property: int | None | Unset = UNSET
    others_sell_property: None | str | Unset = UNSET
    others_fung_shui: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        cost: int | None | Unset
        if isinstance(self.cost, Unset):
            cost = UNSET
        else:
            cost = self.cost

        cost_occupancy_operational_cost: int | None | Unset
        if isinstance(self.cost_occupancy_operational_cost, Unset):
            cost_occupancy_operational_cost = UNSET
        else:
            cost_occupancy_operational_cost = self.cost_occupancy_operational_cost

        premises: int | None | Unset
        if isinstance(self.premises, Unset):
            premises = UNSET
        else:
            premises = self.premises

        premises_suitable_premises_floor_space: int | None | Unset
        if isinstance(self.premises_suitable_premises_floor_space, Unset):
            premises_suitable_premises_floor_space = UNSET
        else:
            premises_suitable_premises_floor_space = (
                self.premises_suitable_premises_floor_space
            )

        premises_renew: int | None | Unset
        if isinstance(self.premises_renew, Unset):
            premises_renew = UNSET
        else:
            premises_renew = self.premises_renew

        premises_poor_building: int | None | Unset
        if isinstance(self.premises_poor_building, Unset):
            premises_poor_building = UNSET
        else:
            premises_poor_building = self.premises_poor_building

        premises_redevelopment: int | None | Unset
        if isinstance(self.premises_redevelopment, Unset):
            premises_redevelopment = UNSET
        else:
            premises_redevelopment = self.premises_redevelopment

        accessibility: int | None | Unset
        if isinstance(self.accessibility, Unset):
            accessibility = UNSET
        else:
            accessibility = self.accessibility

        accessibility_poor_local_transport: int | None | Unset
        if isinstance(self.accessibility_poor_local_transport, Unset):
            accessibility_poor_local_transport = UNSET
        else:
            accessibility_poor_local_transport = self.accessibility_poor_local_transport

        accessibility_inadequate_parking: int | None | Unset
        if isinstance(self.accessibility_inadequate_parking, Unset):
            accessibility_inadequate_parking = UNSET
        else:
            accessibility_inadequate_parking = self.accessibility_inadequate_parking

        accessibility_poor_cross_boundary: int | None | Unset
        if isinstance(self.accessibility_poor_cross_boundary, Unset):
            accessibility_poor_cross_boundary = UNSET
        else:
            accessibility_poor_cross_boundary = self.accessibility_poor_cross_boundary

        agglomeration_economies: int | None | Unset
        if isinstance(self.agglomeration_economies, Unset):
            agglomeration_economies = UNSET
        else:
            agglomeration_economies = self.agglomeration_economies

        agglomeration_economies_head_office: int | None | Unset
        if isinstance(self.agglomeration_economies_head_office, Unset):
            agglomeration_economies_head_office = UNSET
        else:
            agglomeration_economies_head_office = (
                self.agglomeration_economies_head_office
            )

        agglomeration_economies_far_regular_contacts: int | None | Unset
        if isinstance(self.agglomeration_economies_far_regular_contacts, Unset):
            agglomeration_economies_far_regular_contacts = UNSET
        else:
            agglomeration_economies_far_regular_contacts = (
                self.agglomeration_economies_far_regular_contacts
            )

        agglomeration_economies_far_like_business: int | None | Unset
        if isinstance(self.agglomeration_economies_far_like_business, Unset):
            agglomeration_economies_far_like_business = UNSET
        else:
            agglomeration_economies_far_like_business = (
                self.agglomeration_economies_far_like_business
            )

        agglomeration_economies_insufficient_supporting: None | str | Unset
        if isinstance(self.agglomeration_economies_insufficient_supporting, Unset):
            agglomeration_economies_insufficient_supporting = UNSET
        else:
            agglomeration_economies_insufficient_supporting = (
                self.agglomeration_economies_insufficient_supporting
            )

        environment_and_amenities: int | None | Unset
        if isinstance(self.environment_and_amenities, Unset):
            environment_and_amenities = UNSET
        else:
            environment_and_amenities = self.environment_and_amenities

        environment_poor_quality: int | None | Unset
        if isinstance(self.environment_poor_quality, Unset):
            environment_poor_quality = UNSET
        else:
            environment_poor_quality = self.environment_poor_quality

        prestige: int | None | Unset
        if isinstance(self.prestige, Unset):
            prestige = UNSET
        else:
            prestige = self.prestige

        prestige_location_not_prestigious: int | None | Unset
        if isinstance(self.prestige_location_not_prestigious, Unset):
            prestige_location_not_prestigious = UNSET
        else:
            prestige_location_not_prestigious = self.prestige_location_not_prestigious

        others: int | None | Unset
        if isinstance(self.others, Unset):
            others = UNSET
        else:
            others = self.others

        others_reduce_in_scope: int | None | Unset
        if isinstance(self.others_reduce_in_scope, Unset):
            others_reduce_in_scope = UNSET
        else:
            others_reduce_in_scope = self.others_reduce_in_scope

        others_bought_new_property: int | None | Unset
        if isinstance(self.others_bought_new_property, Unset):
            others_bought_new_property = UNSET
        else:
            others_bought_new_property = self.others_bought_new_property

        others_sell_property: None | str | Unset
        if isinstance(self.others_sell_property, Unset):
            others_sell_property = UNSET
        else:
            others_sell_property = self.others_sell_property

        others_fung_shui: None | str | Unset
        if isinstance(self.others_fung_shui, Unset):
            others_fung_shui = UNSET
        else:
            others_fung_shui = self.others_fung_shui

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if cost is not UNSET:
            field_dict["Cost"] = cost
        if cost_occupancy_operational_cost is not UNSET:
            field_dict["Cost_occupancy_operational_cost"] = (
                cost_occupancy_operational_cost
            )
        if premises is not UNSET:
            field_dict["Premises"] = premises
        if premises_suitable_premises_floor_space is not UNSET:
            field_dict["Premises_suitable_premises_floor_space"] = (
                premises_suitable_premises_floor_space
            )
        if premises_renew is not UNSET:
            field_dict["Premises_renew"] = premises_renew
        if premises_poor_building is not UNSET:
            field_dict["Premises_Poor_building"] = premises_poor_building
        if premises_redevelopment is not UNSET:
            field_dict["Premises_Redevelopment"] = premises_redevelopment
        if accessibility is not UNSET:
            field_dict["Accessibility"] = accessibility
        if accessibility_poor_local_transport is not UNSET:
            field_dict["Accessibility_Poor_local_transport"] = (
                accessibility_poor_local_transport
            )
        if accessibility_inadequate_parking is not UNSET:
            field_dict["Accessibility_Inadequate_parking"] = (
                accessibility_inadequate_parking
            )
        if accessibility_poor_cross_boundary is not UNSET:
            field_dict["Accessibility_Poor_cross_boundary"] = (
                accessibility_poor_cross_boundary
            )
        if agglomeration_economies is not UNSET:
            field_dict["Agglomeration_economies"] = agglomeration_economies
        if agglomeration_economies_head_office is not UNSET:
            field_dict["Agglomeration_economies_head_office"] = (
                agglomeration_economies_head_office
            )
        if agglomeration_economies_far_regular_contacts is not UNSET:
            field_dict["Agglomeration_economies_Far_regular_contacts"] = (
                agglomeration_economies_far_regular_contacts
            )
        if agglomeration_economies_far_like_business is not UNSET:
            field_dict["Agglomeration_economies_Far_like_business"] = (
                agglomeration_economies_far_like_business
            )
        if agglomeration_economies_insufficient_supporting is not UNSET:
            field_dict["Agglomeration_economies_Insufficient_supporting"] = (
                agglomeration_economies_insufficient_supporting
            )
        if environment_and_amenities is not UNSET:
            field_dict["Environment_and_amenities"] = environment_and_amenities
        if environment_poor_quality is not UNSET:
            field_dict["Environment_Poor_quality"] = environment_poor_quality
        if prestige is not UNSET:
            field_dict["Prestige"] = prestige
        if prestige_location_not_prestigious is not UNSET:
            field_dict["Prestige_Location_not_prestigious"] = (
                prestige_location_not_prestigious
            )
        if others is not UNSET:
            field_dict["Others"] = others
        if others_reduce_in_scope is not UNSET:
            field_dict["Others_Reduce_in_scope"] = others_reduce_in_scope
        if others_bought_new_property is not UNSET:
            field_dict["Others_Bought_new_property"] = others_bought_new_property
        if others_sell_property is not UNSET:
            field_dict["Others_sell_property"] = others_sell_property
        if others_fung_shui is not UNSET:
            field_dict["Others_Fung_Shui"] = others_fung_shui

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("Area_En", UNSET))

        def _parse_cost(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cost = _parse_cost(d.pop("Cost", UNSET))

        def _parse_cost_occupancy_operational_cost(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cost_occupancy_operational_cost = _parse_cost_occupancy_operational_cost(
            d.pop("Cost_occupancy_operational_cost", UNSET)
        )

        def _parse_premises(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premises = _parse_premises(d.pop("Premises", UNSET))

        def _parse_premises_suitable_premises_floor_space(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premises_suitable_premises_floor_space = (
            _parse_premises_suitable_premises_floor_space(
                d.pop("Premises_suitable_premises_floor_space", UNSET)
            )
        )

        def _parse_premises_renew(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premises_renew = _parse_premises_renew(d.pop("Premises_renew", UNSET))

        def _parse_premises_poor_building(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premises_poor_building = _parse_premises_poor_building(
            d.pop("Premises_Poor_building", UNSET)
        )

        def _parse_premises_redevelopment(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premises_redevelopment = _parse_premises_redevelopment(
            d.pop("Premises_Redevelopment", UNSET)
        )

        def _parse_accessibility(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility = _parse_accessibility(d.pop("Accessibility", UNSET))

        def _parse_accessibility_poor_local_transport(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_poor_local_transport = _parse_accessibility_poor_local_transport(
            d.pop("Accessibility_Poor_local_transport", UNSET)
        )

        def _parse_accessibility_inadequate_parking(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_inadequate_parking = _parse_accessibility_inadequate_parking(
            d.pop("Accessibility_Inadequate_parking", UNSET)
        )

        def _parse_accessibility_poor_cross_boundary(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_poor_cross_boundary = _parse_accessibility_poor_cross_boundary(
            d.pop("Accessibility_Poor_cross_boundary", UNSET)
        )

        def _parse_agglomeration_economies(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agglomeration_economies = _parse_agglomeration_economies(
            d.pop("Agglomeration_economies", UNSET)
        )

        def _parse_agglomeration_economies_head_office(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agglomeration_economies_head_office = (
            _parse_agglomeration_economies_head_office(
                d.pop("Agglomeration_economies_head_office", UNSET)
            )
        )

        def _parse_agglomeration_economies_far_regular_contacts(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agglomeration_economies_far_regular_contacts = (
            _parse_agglomeration_economies_far_regular_contacts(
                d.pop("Agglomeration_economies_Far_regular_contacts", UNSET)
            )
        )

        def _parse_agglomeration_economies_far_like_business(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agglomeration_economies_far_like_business = (
            _parse_agglomeration_economies_far_like_business(
                d.pop("Agglomeration_economies_Far_like_business", UNSET)
            )
        )

        def _parse_agglomeration_economies_insufficient_supporting(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agglomeration_economies_insufficient_supporting = (
            _parse_agglomeration_economies_insufficient_supporting(
                d.pop("Agglomeration_economies_Insufficient_supporting", UNSET)
            )
        )

        def _parse_environment_and_amenities(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        environment_and_amenities = _parse_environment_and_amenities(
            d.pop("Environment_and_amenities", UNSET)
        )

        def _parse_environment_poor_quality(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        environment_poor_quality = _parse_environment_poor_quality(
            d.pop("Environment_Poor_quality", UNSET)
        )

        def _parse_prestige(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prestige = _parse_prestige(d.pop("Prestige", UNSET))

        def _parse_prestige_location_not_prestigious(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prestige_location_not_prestigious = _parse_prestige_location_not_prestigious(
            d.pop("Prestige_Location_not_prestigious", UNSET)
        )

        def _parse_others(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        others = _parse_others(d.pop("Others", UNSET))

        def _parse_others_reduce_in_scope(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        others_reduce_in_scope = _parse_others_reduce_in_scope(
            d.pop("Others_Reduce_in_scope", UNSET)
        )

        def _parse_others_bought_new_property(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        others_bought_new_property = _parse_others_bought_new_property(
            d.pop("Others_Bought_new_property", UNSET)
        )

        def _parse_others_sell_property(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        others_sell_property = _parse_others_sell_property(
            d.pop("Others_sell_property", UNSET)
        )

        def _parse_others_fung_shui(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        others_fung_shui = _parse_others_fung_shui(d.pop("Others_Fung_Shui", UNSET))

        wfs_map_server_wfs_table_296_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            cost=cost,
            cost_occupancy_operational_cost=cost_occupancy_operational_cost,
            premises=premises,
            premises_suitable_premises_floor_space=premises_suitable_premises_floor_space,
            premises_renew=premises_renew,
            premises_poor_building=premises_poor_building,
            premises_redevelopment=premises_redevelopment,
            accessibility=accessibility,
            accessibility_poor_local_transport=accessibility_poor_local_transport,
            accessibility_inadequate_parking=accessibility_inadequate_parking,
            accessibility_poor_cross_boundary=accessibility_poor_cross_boundary,
            agglomeration_economies=agglomeration_economies,
            agglomeration_economies_head_office=agglomeration_economies_head_office,
            agglomeration_economies_far_regular_contacts=agglomeration_economies_far_regular_contacts,
            agglomeration_economies_far_like_business=agglomeration_economies_far_like_business,
            agglomeration_economies_insufficient_supporting=agglomeration_economies_insufficient_supporting,
            environment_and_amenities=environment_and_amenities,
            environment_poor_quality=environment_poor_quality,
            prestige=prestige,
            prestige_location_not_prestigious=prestige_location_not_prestigious,
            others=others,
            others_reduce_in_scope=others_reduce_in_scope,
            others_bought_new_property=others_bought_new_property,
            others_sell_property=others_sell_property,
            others_fung_shui=others_fung_shui,
        )

        wfs_map_server_wfs_table_296_attributes.additional_properties = d
        return wfs_map_server_wfs_table_296_attributes

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
