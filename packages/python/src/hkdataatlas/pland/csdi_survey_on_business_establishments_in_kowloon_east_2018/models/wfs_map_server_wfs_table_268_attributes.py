from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable268Attributes")


@_attrs_define
class WfsMapServerWfsTable268Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        occupancy_cost_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        occupancy_cost_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        occupancy_cost_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        occupancy_cost_no_comment (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        operational_cost_general_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        operational_cost_general_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        operational_cost_general_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        operational_cost_general_no_comment (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        choices_suitable_premises_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        choices_suitable_premises_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        choices_suitable_premises_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        choices_suitable_premises_no_comment (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        accessibility_cross_boundary_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        accessibility_cross_boundary_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        accessibility_cross_boundary_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        accessibility_cross_boundary_no_comment (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        accessibility_local_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        accessibility_local_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        accessibility_local_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        accessibility_local_no_comment (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        accessibility_ke_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        accessibility_ke_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        accessibility_ke_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        accessibility_ke_no_comment (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        proximity_clients_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        proximity_clients_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        proximity_clients_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        proximity_clients_no_comment (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        proximity_government_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        proximity_government_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        proximity_government_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        proximity_government_no_comment (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        presence_like_businesses_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        presence_like_businesses_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        presence_like_businesses_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not
            projected from XML occurrence into all JSON queries.
        presence_like_businesses_no_comment (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        proximity_supporting_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        proximity_supporting_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        proximity_supporting_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        proximity_supporting_no_comment (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        choices_retail_eating_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        choices_retail_eating_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        choices_retail_eating_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        choices_retail_eating_no_comment (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        environmental_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        environmental_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        environmental_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        vibrant_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        vibrant_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        vibrant_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        prestigious_location_satisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        prestigious_location_neutral (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        prestigious_location_dissatisfied (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        prestigious_location_no_comment (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    occupancy_cost_satisfied: int | None | Unset = UNSET
    occupancy_cost_neutral: int | None | Unset = UNSET
    occupancy_cost_dissatisfied: int | None | Unset = UNSET
    occupancy_cost_no_comment: None | str | Unset = UNSET
    operational_cost_general_satisfied: int | None | Unset = UNSET
    operational_cost_general_neutral: int | None | Unset = UNSET
    operational_cost_general_dissatisfied: int | None | Unset = UNSET
    operational_cost_general_no_comment: None | str | Unset = UNSET
    choices_suitable_premises_satisfied: int | None | Unset = UNSET
    choices_suitable_premises_neutral: int | None | Unset = UNSET
    choices_suitable_premises_dissatisfied: int | None | Unset = UNSET
    choices_suitable_premises_no_comment: int | None | Unset = UNSET
    accessibility_cross_boundary_satisfied: int | None | Unset = UNSET
    accessibility_cross_boundary_neutral: int | None | Unset = UNSET
    accessibility_cross_boundary_dissatisfied: int | None | Unset = UNSET
    accessibility_cross_boundary_no_comment: int | None | Unset = UNSET
    accessibility_local_satisfied: int | None | Unset = UNSET
    accessibility_local_neutral: int | None | Unset = UNSET
    accessibility_local_dissatisfied: int | None | Unset = UNSET
    accessibility_local_no_comment: None | str | Unset = UNSET
    accessibility_ke_satisfied: int | None | Unset = UNSET
    accessibility_ke_neutral: int | None | Unset = UNSET
    accessibility_ke_dissatisfied: int | None | Unset = UNSET
    accessibility_ke_no_comment: int | None | Unset = UNSET
    proximity_clients_satisfied: int | None | Unset = UNSET
    proximity_clients_neutral: int | None | Unset = UNSET
    proximity_clients_dissatisfied: int | None | Unset = UNSET
    proximity_clients_no_comment: None | str | Unset = UNSET
    proximity_government_satisfied: int | None | Unset = UNSET
    proximity_government_neutral: int | None | Unset = UNSET
    proximity_government_dissatisfied: int | None | Unset = UNSET
    proximity_government_no_comment: None | str | Unset = UNSET
    presence_like_businesses_satisfied: int | None | Unset = UNSET
    presence_like_businesses_neutral: int | None | Unset = UNSET
    presence_like_businesses_dissatisfied: int | None | Unset = UNSET
    presence_like_businesses_no_comment: int | None | Unset = UNSET
    proximity_supporting_satisfied: int | None | Unset = UNSET
    proximity_supporting_neutral: int | None | Unset = UNSET
    proximity_supporting_dissatisfied: int | None | Unset = UNSET
    proximity_supporting_no_comment: None | str | Unset = UNSET
    choices_retail_eating_satisfied: int | None | Unset = UNSET
    choices_retail_eating_neutral: int | None | Unset = UNSET
    choices_retail_eating_dissatisfied: int | None | Unset = UNSET
    choices_retail_eating_no_comment: int | None | Unset = UNSET
    environmental_satisfied: int | None | Unset = UNSET
    environmental_neutral: int | None | Unset = UNSET
    environmental_dissatisfied: int | None | Unset = UNSET
    vibrant_satisfied: int | None | Unset = UNSET
    vibrant_neutral: int | None | Unset = UNSET
    vibrant_dissatisfied: int | None | Unset = UNSET
    prestigious_location_satisfied: int | None | Unset = UNSET
    prestigious_location_neutral: int | None | Unset = UNSET
    prestigious_location_dissatisfied: int | None | Unset = UNSET
    prestigious_location_no_comment: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        occupancy_cost_satisfied: int | None | Unset
        if isinstance(self.occupancy_cost_satisfied, Unset):
            occupancy_cost_satisfied = UNSET
        else:
            occupancy_cost_satisfied = self.occupancy_cost_satisfied

        occupancy_cost_neutral: int | None | Unset
        if isinstance(self.occupancy_cost_neutral, Unset):
            occupancy_cost_neutral = UNSET
        else:
            occupancy_cost_neutral = self.occupancy_cost_neutral

        occupancy_cost_dissatisfied: int | None | Unset
        if isinstance(self.occupancy_cost_dissatisfied, Unset):
            occupancy_cost_dissatisfied = UNSET
        else:
            occupancy_cost_dissatisfied = self.occupancy_cost_dissatisfied

        occupancy_cost_no_comment: None | str | Unset
        if isinstance(self.occupancy_cost_no_comment, Unset):
            occupancy_cost_no_comment = UNSET
        else:
            occupancy_cost_no_comment = self.occupancy_cost_no_comment

        operational_cost_general_satisfied: int | None | Unset
        if isinstance(self.operational_cost_general_satisfied, Unset):
            operational_cost_general_satisfied = UNSET
        else:
            operational_cost_general_satisfied = self.operational_cost_general_satisfied

        operational_cost_general_neutral: int | None | Unset
        if isinstance(self.operational_cost_general_neutral, Unset):
            operational_cost_general_neutral = UNSET
        else:
            operational_cost_general_neutral = self.operational_cost_general_neutral

        operational_cost_general_dissatisfied: int | None | Unset
        if isinstance(self.operational_cost_general_dissatisfied, Unset):
            operational_cost_general_dissatisfied = UNSET
        else:
            operational_cost_general_dissatisfied = (
                self.operational_cost_general_dissatisfied
            )

        operational_cost_general_no_comment: None | str | Unset
        if isinstance(self.operational_cost_general_no_comment, Unset):
            operational_cost_general_no_comment = UNSET
        else:
            operational_cost_general_no_comment = (
                self.operational_cost_general_no_comment
            )

        choices_suitable_premises_satisfied: int | None | Unset
        if isinstance(self.choices_suitable_premises_satisfied, Unset):
            choices_suitable_premises_satisfied = UNSET
        else:
            choices_suitable_premises_satisfied = (
                self.choices_suitable_premises_satisfied
            )

        choices_suitable_premises_neutral: int | None | Unset
        if isinstance(self.choices_suitable_premises_neutral, Unset):
            choices_suitable_premises_neutral = UNSET
        else:
            choices_suitable_premises_neutral = self.choices_suitable_premises_neutral

        choices_suitable_premises_dissatisfied: int | None | Unset
        if isinstance(self.choices_suitable_premises_dissatisfied, Unset):
            choices_suitable_premises_dissatisfied = UNSET
        else:
            choices_suitable_premises_dissatisfied = (
                self.choices_suitable_premises_dissatisfied
            )

        choices_suitable_premises_no_comment: int | None | Unset
        if isinstance(self.choices_suitable_premises_no_comment, Unset):
            choices_suitable_premises_no_comment = UNSET
        else:
            choices_suitable_premises_no_comment = (
                self.choices_suitable_premises_no_comment
            )

        accessibility_cross_boundary_satisfied: int | None | Unset
        if isinstance(self.accessibility_cross_boundary_satisfied, Unset):
            accessibility_cross_boundary_satisfied = UNSET
        else:
            accessibility_cross_boundary_satisfied = (
                self.accessibility_cross_boundary_satisfied
            )

        accessibility_cross_boundary_neutral: int | None | Unset
        if isinstance(self.accessibility_cross_boundary_neutral, Unset):
            accessibility_cross_boundary_neutral = UNSET
        else:
            accessibility_cross_boundary_neutral = (
                self.accessibility_cross_boundary_neutral
            )

        accessibility_cross_boundary_dissatisfied: int | None | Unset
        if isinstance(self.accessibility_cross_boundary_dissatisfied, Unset):
            accessibility_cross_boundary_dissatisfied = UNSET
        else:
            accessibility_cross_boundary_dissatisfied = (
                self.accessibility_cross_boundary_dissatisfied
            )

        accessibility_cross_boundary_no_comment: int | None | Unset
        if isinstance(self.accessibility_cross_boundary_no_comment, Unset):
            accessibility_cross_boundary_no_comment = UNSET
        else:
            accessibility_cross_boundary_no_comment = (
                self.accessibility_cross_boundary_no_comment
            )

        accessibility_local_satisfied: int | None | Unset
        if isinstance(self.accessibility_local_satisfied, Unset):
            accessibility_local_satisfied = UNSET
        else:
            accessibility_local_satisfied = self.accessibility_local_satisfied

        accessibility_local_neutral: int | None | Unset
        if isinstance(self.accessibility_local_neutral, Unset):
            accessibility_local_neutral = UNSET
        else:
            accessibility_local_neutral = self.accessibility_local_neutral

        accessibility_local_dissatisfied: int | None | Unset
        if isinstance(self.accessibility_local_dissatisfied, Unset):
            accessibility_local_dissatisfied = UNSET
        else:
            accessibility_local_dissatisfied = self.accessibility_local_dissatisfied

        accessibility_local_no_comment: None | str | Unset
        if isinstance(self.accessibility_local_no_comment, Unset):
            accessibility_local_no_comment = UNSET
        else:
            accessibility_local_no_comment = self.accessibility_local_no_comment

        accessibility_ke_satisfied: int | None | Unset
        if isinstance(self.accessibility_ke_satisfied, Unset):
            accessibility_ke_satisfied = UNSET
        else:
            accessibility_ke_satisfied = self.accessibility_ke_satisfied

        accessibility_ke_neutral: int | None | Unset
        if isinstance(self.accessibility_ke_neutral, Unset):
            accessibility_ke_neutral = UNSET
        else:
            accessibility_ke_neutral = self.accessibility_ke_neutral

        accessibility_ke_dissatisfied: int | None | Unset
        if isinstance(self.accessibility_ke_dissatisfied, Unset):
            accessibility_ke_dissatisfied = UNSET
        else:
            accessibility_ke_dissatisfied = self.accessibility_ke_dissatisfied

        accessibility_ke_no_comment: int | None | Unset
        if isinstance(self.accessibility_ke_no_comment, Unset):
            accessibility_ke_no_comment = UNSET
        else:
            accessibility_ke_no_comment = self.accessibility_ke_no_comment

        proximity_clients_satisfied: int | None | Unset
        if isinstance(self.proximity_clients_satisfied, Unset):
            proximity_clients_satisfied = UNSET
        else:
            proximity_clients_satisfied = self.proximity_clients_satisfied

        proximity_clients_neutral: int | None | Unset
        if isinstance(self.proximity_clients_neutral, Unset):
            proximity_clients_neutral = UNSET
        else:
            proximity_clients_neutral = self.proximity_clients_neutral

        proximity_clients_dissatisfied: int | None | Unset
        if isinstance(self.proximity_clients_dissatisfied, Unset):
            proximity_clients_dissatisfied = UNSET
        else:
            proximity_clients_dissatisfied = self.proximity_clients_dissatisfied

        proximity_clients_no_comment: None | str | Unset
        if isinstance(self.proximity_clients_no_comment, Unset):
            proximity_clients_no_comment = UNSET
        else:
            proximity_clients_no_comment = self.proximity_clients_no_comment

        proximity_government_satisfied: int | None | Unset
        if isinstance(self.proximity_government_satisfied, Unset):
            proximity_government_satisfied = UNSET
        else:
            proximity_government_satisfied = self.proximity_government_satisfied

        proximity_government_neutral: int | None | Unset
        if isinstance(self.proximity_government_neutral, Unset):
            proximity_government_neutral = UNSET
        else:
            proximity_government_neutral = self.proximity_government_neutral

        proximity_government_dissatisfied: int | None | Unset
        if isinstance(self.proximity_government_dissatisfied, Unset):
            proximity_government_dissatisfied = UNSET
        else:
            proximity_government_dissatisfied = self.proximity_government_dissatisfied

        proximity_government_no_comment: None | str | Unset
        if isinstance(self.proximity_government_no_comment, Unset):
            proximity_government_no_comment = UNSET
        else:
            proximity_government_no_comment = self.proximity_government_no_comment

        presence_like_businesses_satisfied: int | None | Unset
        if isinstance(self.presence_like_businesses_satisfied, Unset):
            presence_like_businesses_satisfied = UNSET
        else:
            presence_like_businesses_satisfied = self.presence_like_businesses_satisfied

        presence_like_businesses_neutral: int | None | Unset
        if isinstance(self.presence_like_businesses_neutral, Unset):
            presence_like_businesses_neutral = UNSET
        else:
            presence_like_businesses_neutral = self.presence_like_businesses_neutral

        presence_like_businesses_dissatisfied: int | None | Unset
        if isinstance(self.presence_like_businesses_dissatisfied, Unset):
            presence_like_businesses_dissatisfied = UNSET
        else:
            presence_like_businesses_dissatisfied = (
                self.presence_like_businesses_dissatisfied
            )

        presence_like_businesses_no_comment: int | None | Unset
        if isinstance(self.presence_like_businesses_no_comment, Unset):
            presence_like_businesses_no_comment = UNSET
        else:
            presence_like_businesses_no_comment = (
                self.presence_like_businesses_no_comment
            )

        proximity_supporting_satisfied: int | None | Unset
        if isinstance(self.proximity_supporting_satisfied, Unset):
            proximity_supporting_satisfied = UNSET
        else:
            proximity_supporting_satisfied = self.proximity_supporting_satisfied

        proximity_supporting_neutral: int | None | Unset
        if isinstance(self.proximity_supporting_neutral, Unset):
            proximity_supporting_neutral = UNSET
        else:
            proximity_supporting_neutral = self.proximity_supporting_neutral

        proximity_supporting_dissatisfied: int | None | Unset
        if isinstance(self.proximity_supporting_dissatisfied, Unset):
            proximity_supporting_dissatisfied = UNSET
        else:
            proximity_supporting_dissatisfied = self.proximity_supporting_dissatisfied

        proximity_supporting_no_comment: None | str | Unset
        if isinstance(self.proximity_supporting_no_comment, Unset):
            proximity_supporting_no_comment = UNSET
        else:
            proximity_supporting_no_comment = self.proximity_supporting_no_comment

        choices_retail_eating_satisfied: int | None | Unset
        if isinstance(self.choices_retail_eating_satisfied, Unset):
            choices_retail_eating_satisfied = UNSET
        else:
            choices_retail_eating_satisfied = self.choices_retail_eating_satisfied

        choices_retail_eating_neutral: int | None | Unset
        if isinstance(self.choices_retail_eating_neutral, Unset):
            choices_retail_eating_neutral = UNSET
        else:
            choices_retail_eating_neutral = self.choices_retail_eating_neutral

        choices_retail_eating_dissatisfied: int | None | Unset
        if isinstance(self.choices_retail_eating_dissatisfied, Unset):
            choices_retail_eating_dissatisfied = UNSET
        else:
            choices_retail_eating_dissatisfied = self.choices_retail_eating_dissatisfied

        choices_retail_eating_no_comment: int | None | Unset
        if isinstance(self.choices_retail_eating_no_comment, Unset):
            choices_retail_eating_no_comment = UNSET
        else:
            choices_retail_eating_no_comment = self.choices_retail_eating_no_comment

        environmental_satisfied: int | None | Unset
        if isinstance(self.environmental_satisfied, Unset):
            environmental_satisfied = UNSET
        else:
            environmental_satisfied = self.environmental_satisfied

        environmental_neutral: int | None | Unset
        if isinstance(self.environmental_neutral, Unset):
            environmental_neutral = UNSET
        else:
            environmental_neutral = self.environmental_neutral

        environmental_dissatisfied: int | None | Unset
        if isinstance(self.environmental_dissatisfied, Unset):
            environmental_dissatisfied = UNSET
        else:
            environmental_dissatisfied = self.environmental_dissatisfied

        vibrant_satisfied: int | None | Unset
        if isinstance(self.vibrant_satisfied, Unset):
            vibrant_satisfied = UNSET
        else:
            vibrant_satisfied = self.vibrant_satisfied

        vibrant_neutral: int | None | Unset
        if isinstance(self.vibrant_neutral, Unset):
            vibrant_neutral = UNSET
        else:
            vibrant_neutral = self.vibrant_neutral

        vibrant_dissatisfied: int | None | Unset
        if isinstance(self.vibrant_dissatisfied, Unset):
            vibrant_dissatisfied = UNSET
        else:
            vibrant_dissatisfied = self.vibrant_dissatisfied

        prestigious_location_satisfied: int | None | Unset
        if isinstance(self.prestigious_location_satisfied, Unset):
            prestigious_location_satisfied = UNSET
        else:
            prestigious_location_satisfied = self.prestigious_location_satisfied

        prestigious_location_neutral: int | None | Unset
        if isinstance(self.prestigious_location_neutral, Unset):
            prestigious_location_neutral = UNSET
        else:
            prestigious_location_neutral = self.prestigious_location_neutral

        prestigious_location_dissatisfied: int | None | Unset
        if isinstance(self.prestigious_location_dissatisfied, Unset):
            prestigious_location_dissatisfied = UNSET
        else:
            prestigious_location_dissatisfied = self.prestigious_location_dissatisfied

        prestigious_location_no_comment: None | str | Unset
        if isinstance(self.prestigious_location_no_comment, Unset):
            prestigious_location_no_comment = UNSET
        else:
            prestigious_location_no_comment = self.prestigious_location_no_comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if occupancy_cost_satisfied is not UNSET:
            field_dict["Occupancy_cost_satisfied"] = occupancy_cost_satisfied
        if occupancy_cost_neutral is not UNSET:
            field_dict["Occupancy_cost_Neutral"] = occupancy_cost_neutral
        if occupancy_cost_dissatisfied is not UNSET:
            field_dict["Occupancy_cost_dissatisfied"] = occupancy_cost_dissatisfied
        if occupancy_cost_no_comment is not UNSET:
            field_dict["Occupancy_cost_No_comment"] = occupancy_cost_no_comment
        if operational_cost_general_satisfied is not UNSET:
            field_dict["Operational_cost_general_satisfied"] = (
                operational_cost_general_satisfied
            )
        if operational_cost_general_neutral is not UNSET:
            field_dict["Operational_cost_general_Neutral"] = (
                operational_cost_general_neutral
            )
        if operational_cost_general_dissatisfied is not UNSET:
            field_dict["Operational_cost_general_dissatisfied"] = (
                operational_cost_general_dissatisfied
            )
        if operational_cost_general_no_comment is not UNSET:
            field_dict["Operational_cost_general_No_comment"] = (
                operational_cost_general_no_comment
            )
        if choices_suitable_premises_satisfied is not UNSET:
            field_dict["Choices_suitable_premises_satisfied"] = (
                choices_suitable_premises_satisfied
            )
        if choices_suitable_premises_neutral is not UNSET:
            field_dict["Choices_suitable_premises_Neutral"] = (
                choices_suitable_premises_neutral
            )
        if choices_suitable_premises_dissatisfied is not UNSET:
            field_dict["Choices_suitable_premises_dissatisfied"] = (
                choices_suitable_premises_dissatisfied
            )
        if choices_suitable_premises_no_comment is not UNSET:
            field_dict["Choices_suitable_premises_No_comment"] = (
                choices_suitable_premises_no_comment
            )
        if accessibility_cross_boundary_satisfied is not UNSET:
            field_dict["Accessibility_cross_boundary_satisfied"] = (
                accessibility_cross_boundary_satisfied
            )
        if accessibility_cross_boundary_neutral is not UNSET:
            field_dict["Accessibility_cross_boundary_Neutral"] = (
                accessibility_cross_boundary_neutral
            )
        if accessibility_cross_boundary_dissatisfied is not UNSET:
            field_dict["Accessibility_cross_boundary_dissatisfied"] = (
                accessibility_cross_boundary_dissatisfied
            )
        if accessibility_cross_boundary_no_comment is not UNSET:
            field_dict["Accessibility_cross_boundary_No_comment"] = (
                accessibility_cross_boundary_no_comment
            )
        if accessibility_local_satisfied is not UNSET:
            field_dict["Accessibility_local_satisfied"] = accessibility_local_satisfied
        if accessibility_local_neutral is not UNSET:
            field_dict["Accessibility_local_Neutral"] = accessibility_local_neutral
        if accessibility_local_dissatisfied is not UNSET:
            field_dict["Accessibility_local_dissatisfied"] = (
                accessibility_local_dissatisfied
            )
        if accessibility_local_no_comment is not UNSET:
            field_dict["Accessibility_local_No_comment"] = (
                accessibility_local_no_comment
            )
        if accessibility_ke_satisfied is not UNSET:
            field_dict["Accessibility_KE_satisfied"] = accessibility_ke_satisfied
        if accessibility_ke_neutral is not UNSET:
            field_dict["Accessibility_KE_Neutral"] = accessibility_ke_neutral
        if accessibility_ke_dissatisfied is not UNSET:
            field_dict["Accessibility_KE_dissatisfied"] = accessibility_ke_dissatisfied
        if accessibility_ke_no_comment is not UNSET:
            field_dict["Accessibility_KENo_comment"] = accessibility_ke_no_comment
        if proximity_clients_satisfied is not UNSET:
            field_dict["Proximity_clients_satisfied"] = proximity_clients_satisfied
        if proximity_clients_neutral is not UNSET:
            field_dict["Proximity_clients_Neutral"] = proximity_clients_neutral
        if proximity_clients_dissatisfied is not UNSET:
            field_dict["Proximity_clients_dissatisfied"] = (
                proximity_clients_dissatisfied
            )
        if proximity_clients_no_comment is not UNSET:
            field_dict["Proximity_clients_No_comment"] = proximity_clients_no_comment
        if proximity_government_satisfied is not UNSET:
            field_dict["Proximity_government_satisfied"] = (
                proximity_government_satisfied
            )
        if proximity_government_neutral is not UNSET:
            field_dict["Proximity_government_Neutral"] = proximity_government_neutral
        if proximity_government_dissatisfied is not UNSET:
            field_dict["Proximity_government_dissatisfied"] = (
                proximity_government_dissatisfied
            )
        if proximity_government_no_comment is not UNSET:
            field_dict["Proximity_government_No_comment"] = (
                proximity_government_no_comment
            )
        if presence_like_businesses_satisfied is not UNSET:
            field_dict["Presence_like_businesses_satisfied"] = (
                presence_like_businesses_satisfied
            )
        if presence_like_businesses_neutral is not UNSET:
            field_dict["Presence_like_businesses_Neutral"] = (
                presence_like_businesses_neutral
            )
        if presence_like_businesses_dissatisfied is not UNSET:
            field_dict["Presence_like_businesses_dissatisfied"] = (
                presence_like_businesses_dissatisfied
            )
        if presence_like_businesses_no_comment is not UNSET:
            field_dict["Presence_like_businesses_No_comment"] = (
                presence_like_businesses_no_comment
            )
        if proximity_supporting_satisfied is not UNSET:
            field_dict["Proximity_supporting_satisfied"] = (
                proximity_supporting_satisfied
            )
        if proximity_supporting_neutral is not UNSET:
            field_dict["Proximity_supporting_Neutral"] = proximity_supporting_neutral
        if proximity_supporting_dissatisfied is not UNSET:
            field_dict["Proximity_supporting_dissatisfied"] = (
                proximity_supporting_dissatisfied
            )
        if proximity_supporting_no_comment is not UNSET:
            field_dict["Proximity_supporting_No_comment"] = (
                proximity_supporting_no_comment
            )
        if choices_retail_eating_satisfied is not UNSET:
            field_dict["Choices_retail_eating_satisfied"] = (
                choices_retail_eating_satisfied
            )
        if choices_retail_eating_neutral is not UNSET:
            field_dict["Choices_retail_eating_Neutral"] = choices_retail_eating_neutral
        if choices_retail_eating_dissatisfied is not UNSET:
            field_dict["Choices_retail_eating_dissatisfied"] = (
                choices_retail_eating_dissatisfied
            )
        if choices_retail_eating_no_comment is not UNSET:
            field_dict["Choices_retail_eating_No_comment"] = (
                choices_retail_eating_no_comment
            )
        if environmental_satisfied is not UNSET:
            field_dict["Environmental_satisfied"] = environmental_satisfied
        if environmental_neutral is not UNSET:
            field_dict["Environmental_Neutral"] = environmental_neutral
        if environmental_dissatisfied is not UNSET:
            field_dict["Environmental_dissatisfied"] = environmental_dissatisfied
        if vibrant_satisfied is not UNSET:
            field_dict["Vibrant_satisfied"] = vibrant_satisfied
        if vibrant_neutral is not UNSET:
            field_dict["Vibrant_Neutral"] = vibrant_neutral
        if vibrant_dissatisfied is not UNSET:
            field_dict["Vibrant_dissatisfied"] = vibrant_dissatisfied
        if prestigious_location_satisfied is not UNSET:
            field_dict["Prestigious_location_satisfied"] = (
                prestigious_location_satisfied
            )
        if prestigious_location_neutral is not UNSET:
            field_dict["Prestigious_location_Neutral"] = prestigious_location_neutral
        if prestigious_location_dissatisfied is not UNSET:
            field_dict["Prestigious_location_dissatisfied"] = (
                prestigious_location_dissatisfied
            )
        if prestigious_location_no_comment is not UNSET:
            field_dict["Prestigious_location_No_comment"] = (
                prestigious_location_no_comment
            )

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

        def _parse_occupancy_cost_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        occupancy_cost_satisfied = _parse_occupancy_cost_satisfied(
            d.pop("Occupancy_cost_satisfied", UNSET)
        )

        def _parse_occupancy_cost_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        occupancy_cost_neutral = _parse_occupancy_cost_neutral(
            d.pop("Occupancy_cost_Neutral", UNSET)
        )

        def _parse_occupancy_cost_dissatisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        occupancy_cost_dissatisfied = _parse_occupancy_cost_dissatisfied(
            d.pop("Occupancy_cost_dissatisfied", UNSET)
        )

        def _parse_occupancy_cost_no_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        occupancy_cost_no_comment = _parse_occupancy_cost_no_comment(
            d.pop("Occupancy_cost_No_comment", UNSET)
        )

        def _parse_operational_cost_general_satisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        operational_cost_general_satisfied = _parse_operational_cost_general_satisfied(
            d.pop("Operational_cost_general_satisfied", UNSET)
        )

        def _parse_operational_cost_general_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        operational_cost_general_neutral = _parse_operational_cost_general_neutral(
            d.pop("Operational_cost_general_Neutral", UNSET)
        )

        def _parse_operational_cost_general_dissatisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        operational_cost_general_dissatisfied = (
            _parse_operational_cost_general_dissatisfied(
                d.pop("Operational_cost_general_dissatisfied", UNSET)
            )
        )

        def _parse_operational_cost_general_no_comment(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operational_cost_general_no_comment = (
            _parse_operational_cost_general_no_comment(
                d.pop("Operational_cost_general_No_comment", UNSET)
            )
        )

        def _parse_choices_suitable_premises_satisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        choices_suitable_premises_satisfied = (
            _parse_choices_suitable_premises_satisfied(
                d.pop("Choices_suitable_premises_satisfied", UNSET)
            )
        )

        def _parse_choices_suitable_premises_neutral(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        choices_suitable_premises_neutral = _parse_choices_suitable_premises_neutral(
            d.pop("Choices_suitable_premises_Neutral", UNSET)
        )

        def _parse_choices_suitable_premises_dissatisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        choices_suitable_premises_dissatisfied = (
            _parse_choices_suitable_premises_dissatisfied(
                d.pop("Choices_suitable_premises_dissatisfied", UNSET)
            )
        )

        def _parse_choices_suitable_premises_no_comment(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        choices_suitable_premises_no_comment = (
            _parse_choices_suitable_premises_no_comment(
                d.pop("Choices_suitable_premises_No_comment", UNSET)
            )
        )

        def _parse_accessibility_cross_boundary_satisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_cross_boundary_satisfied = (
            _parse_accessibility_cross_boundary_satisfied(
                d.pop("Accessibility_cross_boundary_satisfied", UNSET)
            )
        )

        def _parse_accessibility_cross_boundary_neutral(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_cross_boundary_neutral = (
            _parse_accessibility_cross_boundary_neutral(
                d.pop("Accessibility_cross_boundary_Neutral", UNSET)
            )
        )

        def _parse_accessibility_cross_boundary_dissatisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_cross_boundary_dissatisfied = (
            _parse_accessibility_cross_boundary_dissatisfied(
                d.pop("Accessibility_cross_boundary_dissatisfied", UNSET)
            )
        )

        def _parse_accessibility_cross_boundary_no_comment(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_cross_boundary_no_comment = (
            _parse_accessibility_cross_boundary_no_comment(
                d.pop("Accessibility_cross_boundary_No_comment", UNSET)
            )
        )

        def _parse_accessibility_local_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_local_satisfied = _parse_accessibility_local_satisfied(
            d.pop("Accessibility_local_satisfied", UNSET)
        )

        def _parse_accessibility_local_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_local_neutral = _parse_accessibility_local_neutral(
            d.pop("Accessibility_local_Neutral", UNSET)
        )

        def _parse_accessibility_local_dissatisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_local_dissatisfied = _parse_accessibility_local_dissatisfied(
            d.pop("Accessibility_local_dissatisfied", UNSET)
        )

        def _parse_accessibility_local_no_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        accessibility_local_no_comment = _parse_accessibility_local_no_comment(
            d.pop("Accessibility_local_No_comment", UNSET)
        )

        def _parse_accessibility_ke_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_ke_satisfied = _parse_accessibility_ke_satisfied(
            d.pop("Accessibility_KE_satisfied", UNSET)
        )

        def _parse_accessibility_ke_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_ke_neutral = _parse_accessibility_ke_neutral(
            d.pop("Accessibility_KE_Neutral", UNSET)
        )

        def _parse_accessibility_ke_dissatisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_ke_dissatisfied = _parse_accessibility_ke_dissatisfied(
            d.pop("Accessibility_KE_dissatisfied", UNSET)
        )

        def _parse_accessibility_ke_no_comment(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        accessibility_ke_no_comment = _parse_accessibility_ke_no_comment(
            d.pop("Accessibility_KENo_comment", UNSET)
        )

        def _parse_proximity_clients_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proximity_clients_satisfied = _parse_proximity_clients_satisfied(
            d.pop("Proximity_clients_satisfied", UNSET)
        )

        def _parse_proximity_clients_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proximity_clients_neutral = _parse_proximity_clients_neutral(
            d.pop("Proximity_clients_Neutral", UNSET)
        )

        def _parse_proximity_clients_dissatisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proximity_clients_dissatisfied = _parse_proximity_clients_dissatisfied(
            d.pop("Proximity_clients_dissatisfied", UNSET)
        )

        def _parse_proximity_clients_no_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proximity_clients_no_comment = _parse_proximity_clients_no_comment(
            d.pop("Proximity_clients_No_comment", UNSET)
        )

        def _parse_proximity_government_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proximity_government_satisfied = _parse_proximity_government_satisfied(
            d.pop("Proximity_government_satisfied", UNSET)
        )

        def _parse_proximity_government_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proximity_government_neutral = _parse_proximity_government_neutral(
            d.pop("Proximity_government_Neutral", UNSET)
        )

        def _parse_proximity_government_dissatisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proximity_government_dissatisfied = _parse_proximity_government_dissatisfied(
            d.pop("Proximity_government_dissatisfied", UNSET)
        )

        def _parse_proximity_government_no_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proximity_government_no_comment = _parse_proximity_government_no_comment(
            d.pop("Proximity_government_No_comment", UNSET)
        )

        def _parse_presence_like_businesses_satisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        presence_like_businesses_satisfied = _parse_presence_like_businesses_satisfied(
            d.pop("Presence_like_businesses_satisfied", UNSET)
        )

        def _parse_presence_like_businesses_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        presence_like_businesses_neutral = _parse_presence_like_businesses_neutral(
            d.pop("Presence_like_businesses_Neutral", UNSET)
        )

        def _parse_presence_like_businesses_dissatisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        presence_like_businesses_dissatisfied = (
            _parse_presence_like_businesses_dissatisfied(
                d.pop("Presence_like_businesses_dissatisfied", UNSET)
            )
        )

        def _parse_presence_like_businesses_no_comment(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        presence_like_businesses_no_comment = (
            _parse_presence_like_businesses_no_comment(
                d.pop("Presence_like_businesses_No_comment", UNSET)
            )
        )

        def _parse_proximity_supporting_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proximity_supporting_satisfied = _parse_proximity_supporting_satisfied(
            d.pop("Proximity_supporting_satisfied", UNSET)
        )

        def _parse_proximity_supporting_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proximity_supporting_neutral = _parse_proximity_supporting_neutral(
            d.pop("Proximity_supporting_Neutral", UNSET)
        )

        def _parse_proximity_supporting_dissatisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        proximity_supporting_dissatisfied = _parse_proximity_supporting_dissatisfied(
            d.pop("Proximity_supporting_dissatisfied", UNSET)
        )

        def _parse_proximity_supporting_no_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proximity_supporting_no_comment = _parse_proximity_supporting_no_comment(
            d.pop("Proximity_supporting_No_comment", UNSET)
        )

        def _parse_choices_retail_eating_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        choices_retail_eating_satisfied = _parse_choices_retail_eating_satisfied(
            d.pop("Choices_retail_eating_satisfied", UNSET)
        )

        def _parse_choices_retail_eating_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        choices_retail_eating_neutral = _parse_choices_retail_eating_neutral(
            d.pop("Choices_retail_eating_Neutral", UNSET)
        )

        def _parse_choices_retail_eating_dissatisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        choices_retail_eating_dissatisfied = _parse_choices_retail_eating_dissatisfied(
            d.pop("Choices_retail_eating_dissatisfied", UNSET)
        )

        def _parse_choices_retail_eating_no_comment(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        choices_retail_eating_no_comment = _parse_choices_retail_eating_no_comment(
            d.pop("Choices_retail_eating_No_comment", UNSET)
        )

        def _parse_environmental_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        environmental_satisfied = _parse_environmental_satisfied(
            d.pop("Environmental_satisfied", UNSET)
        )

        def _parse_environmental_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        environmental_neutral = _parse_environmental_neutral(
            d.pop("Environmental_Neutral", UNSET)
        )

        def _parse_environmental_dissatisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        environmental_dissatisfied = _parse_environmental_dissatisfied(
            d.pop("Environmental_dissatisfied", UNSET)
        )

        def _parse_vibrant_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vibrant_satisfied = _parse_vibrant_satisfied(d.pop("Vibrant_satisfied", UNSET))

        def _parse_vibrant_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vibrant_neutral = _parse_vibrant_neutral(d.pop("Vibrant_Neutral", UNSET))

        def _parse_vibrant_dissatisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vibrant_dissatisfied = _parse_vibrant_dissatisfied(
            d.pop("Vibrant_dissatisfied", UNSET)
        )

        def _parse_prestigious_location_satisfied(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prestigious_location_satisfied = _parse_prestigious_location_satisfied(
            d.pop("Prestigious_location_satisfied", UNSET)
        )

        def _parse_prestigious_location_neutral(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prestigious_location_neutral = _parse_prestigious_location_neutral(
            d.pop("Prestigious_location_Neutral", UNSET)
        )

        def _parse_prestigious_location_dissatisfied(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        prestigious_location_dissatisfied = _parse_prestigious_location_dissatisfied(
            d.pop("Prestigious_location_dissatisfied", UNSET)
        )

        def _parse_prestigious_location_no_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        prestigious_location_no_comment = _parse_prestigious_location_no_comment(
            d.pop("Prestigious_location_No_comment", UNSET)
        )

        wfs_map_server_wfs_table_268_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            occupancy_cost_satisfied=occupancy_cost_satisfied,
            occupancy_cost_neutral=occupancy_cost_neutral,
            occupancy_cost_dissatisfied=occupancy_cost_dissatisfied,
            occupancy_cost_no_comment=occupancy_cost_no_comment,
            operational_cost_general_satisfied=operational_cost_general_satisfied,
            operational_cost_general_neutral=operational_cost_general_neutral,
            operational_cost_general_dissatisfied=operational_cost_general_dissatisfied,
            operational_cost_general_no_comment=operational_cost_general_no_comment,
            choices_suitable_premises_satisfied=choices_suitable_premises_satisfied,
            choices_suitable_premises_neutral=choices_suitable_premises_neutral,
            choices_suitable_premises_dissatisfied=choices_suitable_premises_dissatisfied,
            choices_suitable_premises_no_comment=choices_suitable_premises_no_comment,
            accessibility_cross_boundary_satisfied=accessibility_cross_boundary_satisfied,
            accessibility_cross_boundary_neutral=accessibility_cross_boundary_neutral,
            accessibility_cross_boundary_dissatisfied=accessibility_cross_boundary_dissatisfied,
            accessibility_cross_boundary_no_comment=accessibility_cross_boundary_no_comment,
            accessibility_local_satisfied=accessibility_local_satisfied,
            accessibility_local_neutral=accessibility_local_neutral,
            accessibility_local_dissatisfied=accessibility_local_dissatisfied,
            accessibility_local_no_comment=accessibility_local_no_comment,
            accessibility_ke_satisfied=accessibility_ke_satisfied,
            accessibility_ke_neutral=accessibility_ke_neutral,
            accessibility_ke_dissatisfied=accessibility_ke_dissatisfied,
            accessibility_ke_no_comment=accessibility_ke_no_comment,
            proximity_clients_satisfied=proximity_clients_satisfied,
            proximity_clients_neutral=proximity_clients_neutral,
            proximity_clients_dissatisfied=proximity_clients_dissatisfied,
            proximity_clients_no_comment=proximity_clients_no_comment,
            proximity_government_satisfied=proximity_government_satisfied,
            proximity_government_neutral=proximity_government_neutral,
            proximity_government_dissatisfied=proximity_government_dissatisfied,
            proximity_government_no_comment=proximity_government_no_comment,
            presence_like_businesses_satisfied=presence_like_businesses_satisfied,
            presence_like_businesses_neutral=presence_like_businesses_neutral,
            presence_like_businesses_dissatisfied=presence_like_businesses_dissatisfied,
            presence_like_businesses_no_comment=presence_like_businesses_no_comment,
            proximity_supporting_satisfied=proximity_supporting_satisfied,
            proximity_supporting_neutral=proximity_supporting_neutral,
            proximity_supporting_dissatisfied=proximity_supporting_dissatisfied,
            proximity_supporting_no_comment=proximity_supporting_no_comment,
            choices_retail_eating_satisfied=choices_retail_eating_satisfied,
            choices_retail_eating_neutral=choices_retail_eating_neutral,
            choices_retail_eating_dissatisfied=choices_retail_eating_dissatisfied,
            choices_retail_eating_no_comment=choices_retail_eating_no_comment,
            environmental_satisfied=environmental_satisfied,
            environmental_neutral=environmental_neutral,
            environmental_dissatisfied=environmental_dissatisfied,
            vibrant_satisfied=vibrant_satisfied,
            vibrant_neutral=vibrant_neutral,
            vibrant_dissatisfied=vibrant_dissatisfied,
            prestigious_location_satisfied=prestigious_location_satisfied,
            prestigious_location_neutral=prestigious_location_neutral,
            prestigious_location_dissatisfied=prestigious_location_dissatisfied,
            prestigious_location_no_comment=prestigious_location_no_comment,
        )

        wfs_map_server_wfs_table_268_attributes.additional_properties = d
        return wfs_map_server_wfs_table_268_attributes

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
