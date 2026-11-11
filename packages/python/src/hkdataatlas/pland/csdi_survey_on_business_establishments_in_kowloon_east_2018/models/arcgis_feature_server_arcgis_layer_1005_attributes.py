from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1005Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1005Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        cost (int | None | Unset): Publisher field type: esriFieldTypeInteger
        cost_low_occupancy_operational_cost (int | None | Unset): Publisher field type: esriFieldTypeInteger
        premises (int | None | Unset): Publisher field type: esriFieldTypeInteger
        premises_suitable_premises (int | None | Unset): Publisher field type: esriFieldTypeInteger
        accessibility (int | None | Unset): Publisher field type: esriFieldTypeInteger
        accessibility_public_transport (int | None | Unset): Publisher field type: esriFieldTypeInteger
        accessibility_parking (int | None | Unset): Publisher field type: esriFieldTypeInteger
        accessibility_cross_boundary (int | None | Unset): Publisher field type: esriFieldTypeInteger
        agglomeration (int | None | Unset): Publisher field type: esriFieldTypeInteger
        agglomeration_like_business (int | None | Unset): Publisher field type: esriFieldTypeInteger
        agglomeration_regular_contacts (int | None | Unset): Publisher field type: esriFieldTypeInteger
        agglomeration_supporting_services (int | None | Unset): Publisher field type: esriFieldTypeInteger
        environment (int | None | Unset): Publisher field type: esriFieldTypeInteger
        environment_environmental_quality (int | None | Unset): Publisher field type: esriFieldTypeInteger
        prestige (int | None | Unset): Publisher field type: esriFieldTypeInteger
        prestige_prestigious_location (int | None | Unset): Publisher field type: esriFieldTypeInteger
        others (int | None | Unset): Publisher field type: esriFieldTypeInteger
        others_parent_company (int | None | Unset): Publisher field type: esriFieldTypeInteger
        others_building_quality_management (int | None | Unset): Publisher field type: esriFieldTypeInteger
        others_development_potential (int | None | Unset): Publisher field type: esriFieldTypeInteger
        others_relocation_head_office (None | str | Unset): Publisher field type: esriFieldTypeString
        others_fung_shui (int | None | Unset): Publisher field type: esriFieldTypeInteger
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    cost: int | None | Unset = UNSET
    cost_low_occupancy_operational_cost: int | None | Unset = UNSET
    premises: int | None | Unset = UNSET
    premises_suitable_premises: int | None | Unset = UNSET
    accessibility: int | None | Unset = UNSET
    accessibility_public_transport: int | None | Unset = UNSET
    accessibility_parking: int | None | Unset = UNSET
    accessibility_cross_boundary: int | None | Unset = UNSET
    agglomeration: int | None | Unset = UNSET
    agglomeration_like_business: int | None | Unset = UNSET
    agglomeration_regular_contacts: int | None | Unset = UNSET
    agglomeration_supporting_services: int | None | Unset = UNSET
    environment: int | None | Unset = UNSET
    environment_environmental_quality: int | None | Unset = UNSET
    prestige: int | None | Unset = UNSET
    prestige_prestigious_location: int | None | Unset = UNSET
    others: int | None | Unset = UNSET
    others_parent_company: int | None | Unset = UNSET
    others_building_quality_management: int | None | Unset = UNSET
    others_development_potential: int | None | Unset = UNSET
    others_relocation_head_office: None | str | Unset = UNSET
    others_fung_shui: int | None | Unset = UNSET
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

        cost_low_occupancy_operational_cost: int | None | Unset
        if isinstance(self.cost_low_occupancy_operational_cost, Unset):
            cost_low_occupancy_operational_cost = UNSET
        else:
            cost_low_occupancy_operational_cost = (
                self.cost_low_occupancy_operational_cost
            )

        premises: int | None | Unset
        if isinstance(self.premises, Unset):
            premises = UNSET
        else:
            premises = self.premises

        premises_suitable_premises: int | None | Unset
        if isinstance(self.premises_suitable_premises, Unset):
            premises_suitable_premises = UNSET
        else:
            premises_suitable_premises = self.premises_suitable_premises

        accessibility: int | None | Unset
        if isinstance(self.accessibility, Unset):
            accessibility = UNSET
        else:
            accessibility = self.accessibility

        accessibility_public_transport: int | None | Unset
        if isinstance(self.accessibility_public_transport, Unset):
            accessibility_public_transport = UNSET
        else:
            accessibility_public_transport = self.accessibility_public_transport

        accessibility_parking: int | None | Unset
        if isinstance(self.accessibility_parking, Unset):
            accessibility_parking = UNSET
        else:
            accessibility_parking = self.accessibility_parking

        accessibility_cross_boundary: int | None | Unset
        if isinstance(self.accessibility_cross_boundary, Unset):
            accessibility_cross_boundary = UNSET
        else:
            accessibility_cross_boundary = self.accessibility_cross_boundary

        agglomeration: int | None | Unset
        if isinstance(self.agglomeration, Unset):
            agglomeration = UNSET
        else:
            agglomeration = self.agglomeration

        agglomeration_like_business: int | None | Unset
        if isinstance(self.agglomeration_like_business, Unset):
            agglomeration_like_business = UNSET
        else:
            agglomeration_like_business = self.agglomeration_like_business

        agglomeration_regular_contacts: int | None | Unset
        if isinstance(self.agglomeration_regular_contacts, Unset):
            agglomeration_regular_contacts = UNSET
        else:
            agglomeration_regular_contacts = self.agglomeration_regular_contacts

        agglomeration_supporting_services: int | None | Unset
        if isinstance(self.agglomeration_supporting_services, Unset):
            agglomeration_supporting_services = UNSET
        else:
            agglomeration_supporting_services = self.agglomeration_supporting_services

        environment: int | None | Unset
        if isinstance(self.environment, Unset):
            environment = UNSET
        else:
            environment = self.environment

        environment_environmental_quality: int | None | Unset
        if isinstance(self.environment_environmental_quality, Unset):
            environment_environmental_quality = UNSET
        else:
            environment_environmental_quality = self.environment_environmental_quality

        prestige: int | None | Unset
        if isinstance(self.prestige, Unset):
            prestige = UNSET
        else:
            prestige = self.prestige

        prestige_prestigious_location: int | None | Unset
        if isinstance(self.prestige_prestigious_location, Unset):
            prestige_prestigious_location = UNSET
        else:
            prestige_prestigious_location = self.prestige_prestigious_location

        others: int | None | Unset
        if isinstance(self.others, Unset):
            others = UNSET
        else:
            others = self.others

        others_parent_company: int | None | Unset
        if isinstance(self.others_parent_company, Unset):
            others_parent_company = UNSET
        else:
            others_parent_company = self.others_parent_company

        others_building_quality_management: int | None | Unset
        if isinstance(self.others_building_quality_management, Unset):
            others_building_quality_management = UNSET
        else:
            others_building_quality_management = self.others_building_quality_management

        others_development_potential: int | None | Unset
        if isinstance(self.others_development_potential, Unset):
            others_development_potential = UNSET
        else:
            others_development_potential = self.others_development_potential

        others_relocation_head_office: None | str | Unset
        if isinstance(self.others_relocation_head_office, Unset):
            others_relocation_head_office = UNSET
        else:
            others_relocation_head_office = self.others_relocation_head_office

        others_fung_shui: int | None | Unset
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
        if cost_low_occupancy_operational_cost is not UNSET:
            field_dict["Cost_Low_occupancy_operational_cost"] = (
                cost_low_occupancy_operational_cost
            )
        if premises is not UNSET:
            field_dict["Premises"] = premises
        if premises_suitable_premises is not UNSET:
            field_dict["Premises_suitable_premises"] = premises_suitable_premises
        if accessibility is not UNSET:
            field_dict["Accessibility"] = accessibility
        if accessibility_public_transport is not UNSET:
            field_dict["Accessibility_public_transport"] = (
                accessibility_public_transport
            )
        if accessibility_parking is not UNSET:
            field_dict["Accessibility_parking"] = accessibility_parking
        if accessibility_cross_boundary is not UNSET:
            field_dict["Accessibility_cross_boundary"] = accessibility_cross_boundary
        if agglomeration is not UNSET:
            field_dict["Agglomeration"] = agglomeration
        if agglomeration_like_business is not UNSET:
            field_dict["Agglomeration_like_business"] = agglomeration_like_business
        if agglomeration_regular_contacts is not UNSET:
            field_dict["Agglomeration_regular_contacts"] = (
                agglomeration_regular_contacts
            )
        if agglomeration_supporting_services is not UNSET:
            field_dict["Agglomeration_supporting_services"] = (
                agglomeration_supporting_services
            )
        if environment is not UNSET:
            field_dict["Environment"] = environment
        if environment_environmental_quality is not UNSET:
            field_dict["Environment_environmental_quality"] = (
                environment_environmental_quality
            )
        if prestige is not UNSET:
            field_dict["Prestige"] = prestige
        if prestige_prestigious_location is not UNSET:
            field_dict["Prestige_Prestigious_location"] = prestige_prestigious_location
        if others is not UNSET:
            field_dict["Others"] = others
        if others_parent_company is not UNSET:
            field_dict["Others_parent_company"] = others_parent_company
        if others_building_quality_management is not UNSET:
            field_dict["Others_building_quality_management"] = (
                others_building_quality_management
            )
        if others_development_potential is not UNSET:
            field_dict["Others_development_potential"] = others_development_potential
        if others_relocation_head_office is not UNSET:
            field_dict["Others_relocation_head_office"] = others_relocation_head_office
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

        def _parse_cost_low_occupancy_operational_cost(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cost_low_occupancy_operational_cost = (
            _parse_cost_low_occupancy_operational_cost(
                d.pop("Cost_Low_occupancy_operational_cost", UNSET)
            )
        )

        def _parse_premises(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premises = _parse_premises(d.pop("Premises", UNSET))

        def _parse_premises_suitable_premises(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premises_suitable_premises = _parse_premises_suitable_premises(
            d.pop("Premises_suitable_premises", UNSET)
        )

        def _parse_accessibility(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility = _parse_accessibility(d.pop("Accessibility", UNSET))

        def _parse_accessibility_public_transport(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_public_transport = _parse_accessibility_public_transport(
            d.pop("Accessibility_public_transport", UNSET)
        )

        def _parse_accessibility_parking(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_parking = _parse_accessibility_parking(
            d.pop("Accessibility_parking", UNSET)
        )

        def _parse_accessibility_cross_boundary(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_cross_boundary = _parse_accessibility_cross_boundary(
            d.pop("Accessibility_cross_boundary", UNSET)
        )

        def _parse_agglomeration(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agglomeration = _parse_agglomeration(d.pop("Agglomeration", UNSET))

        def _parse_agglomeration_like_business(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agglomeration_like_business = _parse_agglomeration_like_business(
            d.pop("Agglomeration_like_business", UNSET)
        )

        def _parse_agglomeration_regular_contacts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agglomeration_regular_contacts = _parse_agglomeration_regular_contacts(
            d.pop("Agglomeration_regular_contacts", UNSET)
        )

        def _parse_agglomeration_supporting_services(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        agglomeration_supporting_services = _parse_agglomeration_supporting_services(
            d.pop("Agglomeration_supporting_services", UNSET)
        )

        def _parse_environment(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        environment = _parse_environment(d.pop("Environment", UNSET))

        def _parse_environment_environmental_quality(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        environment_environmental_quality = _parse_environment_environmental_quality(
            d.pop("Environment_environmental_quality", UNSET)
        )

        def _parse_prestige(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prestige = _parse_prestige(d.pop("Prestige", UNSET))

        def _parse_prestige_prestigious_location(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prestige_prestigious_location = _parse_prestige_prestigious_location(
            d.pop("Prestige_Prestigious_location", UNSET)
        )

        def _parse_others(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        others = _parse_others(d.pop("Others", UNSET))

        def _parse_others_parent_company(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        others_parent_company = _parse_others_parent_company(
            d.pop("Others_parent_company", UNSET)
        )

        def _parse_others_building_quality_management(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        others_building_quality_management = _parse_others_building_quality_management(
            d.pop("Others_building_quality_management", UNSET)
        )

        def _parse_others_development_potential(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        others_development_potential = _parse_others_development_potential(
            d.pop("Others_development_potential", UNSET)
        )

        def _parse_others_relocation_head_office(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        others_relocation_head_office = _parse_others_relocation_head_office(
            d.pop("Others_relocation_head_office", UNSET)
        )

        def _parse_others_fung_shui(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        others_fung_shui = _parse_others_fung_shui(d.pop("Others_Fung_Shui", UNSET))

        arcgis_feature_server_arcgis_layer_1005_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            cost=cost,
            cost_low_occupancy_operational_cost=cost_low_occupancy_operational_cost,
            premises=premises,
            premises_suitable_premises=premises_suitable_premises,
            accessibility=accessibility,
            accessibility_public_transport=accessibility_public_transport,
            accessibility_parking=accessibility_parking,
            accessibility_cross_boundary=accessibility_cross_boundary,
            agglomeration=agglomeration,
            agglomeration_like_business=agglomeration_like_business,
            agglomeration_regular_contacts=agglomeration_regular_contacts,
            agglomeration_supporting_services=agglomeration_supporting_services,
            environment=environment,
            environment_environmental_quality=environment_environmental_quality,
            prestige=prestige,
            prestige_prestigious_location=prestige_prestigious_location,
            others=others,
            others_parent_company=others_parent_company,
            others_building_quality_management=others_building_quality_management,
            others_development_potential=others_development_potential,
            others_relocation_head_office=others_relocation_head_office,
            others_fung_shui=others_fung_shui,
        )

        arcgis_feature_server_arcgis_layer_1005_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1005_attributes

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
