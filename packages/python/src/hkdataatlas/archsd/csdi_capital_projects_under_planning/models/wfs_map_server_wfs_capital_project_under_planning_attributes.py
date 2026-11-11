from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsCapitalProjectUnderPlanningAttributes")


@_attrs_define
class WfsMapServerWfsCapitalProjectUnderPlanningAttributes:
    """
    Attributes:
        project_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        project_title (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        project_title_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        project_title_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        location (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        location_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        contact_person (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        contact_person_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        contact_person_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        project_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        project_type_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        project_type_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        building_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        building_type_cht (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        building_type_chs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        estimated_project_cost (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        scheduled_project_start (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        scheduled_project_completion (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        northing (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        easting (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        fid (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    project_code: None | str | Unset = UNSET
    project_title: None | str | Unset = UNSET
    project_title_cht: None | str | Unset = UNSET
    project_title_chs: None | str | Unset = UNSET
    location: None | str | Unset = UNSET
    location_cht: None | str | Unset = UNSET
    location_chs: None | str | Unset = UNSET
    contact_person: None | str | Unset = UNSET
    contact_person_cht: None | str | Unset = UNSET
    contact_person_chs: None | str | Unset = UNSET
    project_type: None | str | Unset = UNSET
    project_type_cht: None | str | Unset = UNSET
    project_type_chs: None | str | Unset = UNSET
    building_type: None | str | Unset = UNSET
    building_type_cht: None | str | Unset = UNSET
    building_type_chs: None | str | Unset = UNSET
    estimated_project_cost: None | str | Unset = UNSET
    scheduled_project_start: None | str | Unset = UNSET
    scheduled_project_completion: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        project_code: None | str | Unset
        if isinstance(self.project_code, Unset):
            project_code = UNSET
        else:
            project_code = self.project_code

        project_title: None | str | Unset
        if isinstance(self.project_title, Unset):
            project_title = UNSET
        else:
            project_title = self.project_title

        project_title_cht: None | str | Unset
        if isinstance(self.project_title_cht, Unset):
            project_title_cht = UNSET
        else:
            project_title_cht = self.project_title_cht

        project_title_chs: None | str | Unset
        if isinstance(self.project_title_chs, Unset):
            project_title_chs = UNSET
        else:
            project_title_chs = self.project_title_chs

        location: None | str | Unset
        if isinstance(self.location, Unset):
            location = UNSET
        else:
            location = self.location

        location_cht: None | str | Unset
        if isinstance(self.location_cht, Unset):
            location_cht = UNSET
        else:
            location_cht = self.location_cht

        location_chs: None | str | Unset
        if isinstance(self.location_chs, Unset):
            location_chs = UNSET
        else:
            location_chs = self.location_chs

        contact_person: None | str | Unset
        if isinstance(self.contact_person, Unset):
            contact_person = UNSET
        else:
            contact_person = self.contact_person

        contact_person_cht: None | str | Unset
        if isinstance(self.contact_person_cht, Unset):
            contact_person_cht = UNSET
        else:
            contact_person_cht = self.contact_person_cht

        contact_person_chs: None | str | Unset
        if isinstance(self.contact_person_chs, Unset):
            contact_person_chs = UNSET
        else:
            contact_person_chs = self.contact_person_chs

        project_type: None | str | Unset
        if isinstance(self.project_type, Unset):
            project_type = UNSET
        else:
            project_type = self.project_type

        project_type_cht: None | str | Unset
        if isinstance(self.project_type_cht, Unset):
            project_type_cht = UNSET
        else:
            project_type_cht = self.project_type_cht

        project_type_chs: None | str | Unset
        if isinstance(self.project_type_chs, Unset):
            project_type_chs = UNSET
        else:
            project_type_chs = self.project_type_chs

        building_type: None | str | Unset
        if isinstance(self.building_type, Unset):
            building_type = UNSET
        else:
            building_type = self.building_type

        building_type_cht: None | str | Unset
        if isinstance(self.building_type_cht, Unset):
            building_type_cht = UNSET
        else:
            building_type_cht = self.building_type_cht

        building_type_chs: None | str | Unset
        if isinstance(self.building_type_chs, Unset):
            building_type_chs = UNSET
        else:
            building_type_chs = self.building_type_chs

        estimated_project_cost: None | str | Unset
        if isinstance(self.estimated_project_cost, Unset):
            estimated_project_cost = UNSET
        else:
            estimated_project_cost = self.estimated_project_cost

        scheduled_project_start: None | str | Unset
        if isinstance(self.scheduled_project_start, Unset):
            scheduled_project_start = UNSET
        else:
            scheduled_project_start = self.scheduled_project_start

        scheduled_project_completion: None | str | Unset
        if isinstance(self.scheduled_project_completion, Unset):
            scheduled_project_completion = UNSET
        else:
            scheduled_project_completion = self.scheduled_project_completion

        northing: None | str | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: None | str | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project_code is not UNSET:
            field_dict["projectCode"] = project_code
        if project_title is not UNSET:
            field_dict["projectTitle"] = project_title
        if project_title_cht is not UNSET:
            field_dict["projectTitleCht"] = project_title_cht
        if project_title_chs is not UNSET:
            field_dict["projectTitleChs"] = project_title_chs
        if location is not UNSET:
            field_dict["location"] = location
        if location_cht is not UNSET:
            field_dict["locationCht"] = location_cht
        if location_chs is not UNSET:
            field_dict["locationChs"] = location_chs
        if contact_person is not UNSET:
            field_dict["contactPerson"] = contact_person
        if contact_person_cht is not UNSET:
            field_dict["contactPersonCht"] = contact_person_cht
        if contact_person_chs is not UNSET:
            field_dict["contactPersonChs"] = contact_person_chs
        if project_type is not UNSET:
            field_dict["projectType"] = project_type
        if project_type_cht is not UNSET:
            field_dict["projectTypeCht"] = project_type_cht
        if project_type_chs is not UNSET:
            field_dict["projectTypeChs"] = project_type_chs
        if building_type is not UNSET:
            field_dict["buildingType"] = building_type
        if building_type_cht is not UNSET:
            field_dict["buildingTypeCht"] = building_type_cht
        if building_type_chs is not UNSET:
            field_dict["buildingTypeChs"] = building_type_chs
        if estimated_project_cost is not UNSET:
            field_dict["estimatedProjectCost"] = estimated_project_cost
        if scheduled_project_start is not UNSET:
            field_dict["scheduledProjectStart"] = scheduled_project_start
        if scheduled_project_completion is not UNSET:
            field_dict["scheduledProjectCompletion"] = scheduled_project_completion
        if northing is not UNSET:
            field_dict["northing"] = northing
        if easting is not UNSET:
            field_dict["easting"] = easting
        if fid is not UNSET:
            field_dict["fid"] = fid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_project_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_code = _parse_project_code(d.pop("projectCode", UNSET))

        def _parse_project_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title = _parse_project_title(d.pop("projectTitle", UNSET))

        def _parse_project_title_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title_cht = _parse_project_title_cht(d.pop("projectTitleCht", UNSET))

        def _parse_project_title_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title_chs = _parse_project_title_chs(d.pop("projectTitleChs", UNSET))

        def _parse_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location = _parse_location(d.pop("location", UNSET))

        def _parse_location_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_cht = _parse_location_cht(d.pop("locationCht", UNSET))

        def _parse_location_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_chs = _parse_location_chs(d.pop("locationChs", UNSET))

        def _parse_contact_person(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_person = _parse_contact_person(d.pop("contactPerson", UNSET))

        def _parse_contact_person_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_person_cht = _parse_contact_person_cht(d.pop("contactPersonCht", UNSET))

        def _parse_contact_person_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        contact_person_chs = _parse_contact_person_chs(d.pop("contactPersonChs", UNSET))

        def _parse_project_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_type = _parse_project_type(d.pop("projectType", UNSET))

        def _parse_project_type_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_type_cht = _parse_project_type_cht(d.pop("projectTypeCht", UNSET))

        def _parse_project_type_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_type_chs = _parse_project_type_chs(d.pop("projectTypeChs", UNSET))

        def _parse_building_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_type = _parse_building_type(d.pop("buildingType", UNSET))

        def _parse_building_type_cht(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_type_cht = _parse_building_type_cht(d.pop("buildingTypeCht", UNSET))

        def _parse_building_type_chs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_type_chs = _parse_building_type_chs(d.pop("buildingTypeChs", UNSET))

        def _parse_estimated_project_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estimated_project_cost = _parse_estimated_project_cost(
            d.pop("estimatedProjectCost", UNSET)
        )

        def _parse_scheduled_project_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheduled_project_start = _parse_scheduled_project_start(
            d.pop("scheduledProjectStart", UNSET)
        )

        def _parse_scheduled_project_completion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scheduled_project_completion = _parse_scheduled_project_completion(
            d.pop("scheduledProjectCompletion", UNSET)
        )

        def _parse_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        northing = _parse_northing(d.pop("northing", UNSET))

        def _parse_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        easting = _parse_easting(d.pop("easting", UNSET))

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_capital_project_under_planning_attributes = cls(
            project_code=project_code,
            project_title=project_title,
            project_title_cht=project_title_cht,
            project_title_chs=project_title_chs,
            location=location,
            location_cht=location_cht,
            location_chs=location_chs,
            contact_person=contact_person,
            contact_person_cht=contact_person_cht,
            contact_person_chs=contact_person_chs,
            project_type=project_type,
            project_type_cht=project_type_cht,
            project_type_chs=project_type_chs,
            building_type=building_type,
            building_type_cht=building_type_cht,
            building_type_chs=building_type_chs,
            estimated_project_cost=estimated_project_cost,
            scheduled_project_start=scheduled_project_start,
            scheduled_project_completion=scheduled_project_completion,
            northing=northing,
            easting=easting,
            fid=fid,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_capital_project_under_planning_attributes.additional_properties = d
        return wfs_map_server_wfs_capital_project_under_planning_attributes

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
