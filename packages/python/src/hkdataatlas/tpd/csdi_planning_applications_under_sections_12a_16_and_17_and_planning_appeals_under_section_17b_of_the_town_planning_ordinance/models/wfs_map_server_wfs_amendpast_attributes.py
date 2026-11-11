from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsAMENDPASTAttributes")


@_attrs_define
class WfsMapServerWfsAMENDPASTAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        application_case_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        further_information_number (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from
            XML occurrence into all JSON queries.
        district_planning_office (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        ozp_scheme_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        ozp_plan_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        case_status_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        proposed_amendment (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        location_address_of_application (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        latest_s_12a_decision_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        date_of_latest_s_12a_latest_decision (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        last_upload_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        feature_geometry_type (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not
            inferred from its XML type.
        perimeter_in_meters (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        area_in_sq_meters (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    application_case_number: None | str | Unset = UNSET
    further_information_number: int | None | Unset = UNSET
    district_planning_office: None | str | Unset = UNSET
    ozp_scheme_code: None | str | Unset = UNSET
    ozp_plan_number: None | str | Unset = UNSET
    case_status_code: None | str | Unset = UNSET
    proposed_amendment: None | str | Unset = UNSET
    location_address_of_application: None | str | Unset = UNSET
    latest_s_12a_decision_code: None | str | Unset = UNSET
    date_of_latest_s_12a_latest_decision: None | str | Unset = UNSET
    last_upload_date: None | str | Unset = UNSET
    feature_geometry_type: Any | Unset = UNSET
    perimeter_in_meters: float | None | Unset = UNSET
    area_in_sq_meters: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        application_case_number: None | str | Unset
        if isinstance(self.application_case_number, Unset):
            application_case_number = UNSET
        else:
            application_case_number = self.application_case_number

        further_information_number: int | None | Unset
        if isinstance(self.further_information_number, Unset):
            further_information_number = UNSET
        else:
            further_information_number = self.further_information_number

        district_planning_office: None | str | Unset
        if isinstance(self.district_planning_office, Unset):
            district_planning_office = UNSET
        else:
            district_planning_office = self.district_planning_office

        ozp_scheme_code: None | str | Unset
        if isinstance(self.ozp_scheme_code, Unset):
            ozp_scheme_code = UNSET
        else:
            ozp_scheme_code = self.ozp_scheme_code

        ozp_plan_number: None | str | Unset
        if isinstance(self.ozp_plan_number, Unset):
            ozp_plan_number = UNSET
        else:
            ozp_plan_number = self.ozp_plan_number

        case_status_code: None | str | Unset
        if isinstance(self.case_status_code, Unset):
            case_status_code = UNSET
        else:
            case_status_code = self.case_status_code

        proposed_amendment: None | str | Unset
        if isinstance(self.proposed_amendment, Unset):
            proposed_amendment = UNSET
        else:
            proposed_amendment = self.proposed_amendment

        location_address_of_application: None | str | Unset
        if isinstance(self.location_address_of_application, Unset):
            location_address_of_application = UNSET
        else:
            location_address_of_application = self.location_address_of_application

        latest_s_12a_decision_code: None | str | Unset
        if isinstance(self.latest_s_12a_decision_code, Unset):
            latest_s_12a_decision_code = UNSET
        else:
            latest_s_12a_decision_code = self.latest_s_12a_decision_code

        date_of_latest_s_12a_latest_decision: None | str | Unset
        if isinstance(self.date_of_latest_s_12a_latest_decision, Unset):
            date_of_latest_s_12a_latest_decision = UNSET
        else:
            date_of_latest_s_12a_latest_decision = (
                self.date_of_latest_s_12a_latest_decision
            )

        last_upload_date: None | str | Unset
        if isinstance(self.last_upload_date, Unset):
            last_upload_date = UNSET
        else:
            last_upload_date = self.last_upload_date

        feature_geometry_type = self.feature_geometry_type

        perimeter_in_meters: float | None | Unset
        if isinstance(self.perimeter_in_meters, Unset):
            perimeter_in_meters = UNSET
        else:
            perimeter_in_meters = self.perimeter_in_meters

        area_in_sq_meters: float | None | Unset
        if isinstance(self.area_in_sq_meters, Unset):
            area_in_sq_meters = UNSET
        else:
            area_in_sq_meters = self.area_in_sq_meters

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if application_case_number is not UNSET:
            field_dict["Application_case_number"] = application_case_number
        if further_information_number is not UNSET:
            field_dict["Further_information_number"] = further_information_number
        if district_planning_office is not UNSET:
            field_dict["District_planning_office"] = district_planning_office
        if ozp_scheme_code is not UNSET:
            field_dict["OZP_scheme_code"] = ozp_scheme_code
        if ozp_plan_number is not UNSET:
            field_dict["OZP_plan_number"] = ozp_plan_number
        if case_status_code is not UNSET:
            field_dict["Case_status_code"] = case_status_code
        if proposed_amendment is not UNSET:
            field_dict["Proposed_Amendment"] = proposed_amendment
        if location_address_of_application is not UNSET:
            field_dict["Location_address_of_application"] = (
                location_address_of_application
            )
        if latest_s_12a_decision_code is not UNSET:
            field_dict["Latest_s.12A_decision_code"] = latest_s_12a_decision_code
        if date_of_latest_s_12a_latest_decision is not UNSET:
            field_dict["Date_of_latest_s.12A_latest_decision"] = (
                date_of_latest_s_12a_latest_decision
            )
        if last_upload_date is not UNSET:
            field_dict["Last_upload_date"] = last_upload_date
        if feature_geometry_type is not UNSET:
            field_dict["Feature_geometry_type"] = feature_geometry_type
        if perimeter_in_meters is not UNSET:
            field_dict["Perimeter_in_meters"] = perimeter_in_meters
        if area_in_sq_meters is not UNSET:
            field_dict["Area_in_sq._meters"] = area_in_sq_meters

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_application_case_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_case_number = _parse_application_case_number(
            d.pop("Application_case_number", UNSET)
        )

        def _parse_further_information_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        further_information_number = _parse_further_information_number(
            d.pop("Further_information_number", UNSET)
        )

        def _parse_district_planning_office(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_planning_office = _parse_district_planning_office(
            d.pop("District_planning_office", UNSET)
        )

        def _parse_ozp_scheme_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ozp_scheme_code = _parse_ozp_scheme_code(d.pop("OZP_scheme_code", UNSET))

        def _parse_ozp_plan_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ozp_plan_number = _parse_ozp_plan_number(d.pop("OZP_plan_number", UNSET))

        def _parse_case_status_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        case_status_code = _parse_case_status_code(d.pop("Case_status_code", UNSET))

        def _parse_proposed_amendment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proposed_amendment = _parse_proposed_amendment(
            d.pop("Proposed_Amendment", UNSET)
        )

        def _parse_location_address_of_application(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_address_of_application = _parse_location_address_of_application(
            d.pop("Location_address_of_application", UNSET)
        )

        def _parse_latest_s_12a_decision_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_s_12a_decision_code = _parse_latest_s_12a_decision_code(
            d.pop("Latest_s.12A_decision_code", UNSET)
        )

        def _parse_date_of_latest_s_12a_latest_decision(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_latest_s_12a_latest_decision = (
            _parse_date_of_latest_s_12a_latest_decision(
                d.pop("Date_of_latest_s.12A_latest_decision", UNSET)
            )
        )

        def _parse_last_upload_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_upload_date = _parse_last_upload_date(d.pop("Last_upload_date", UNSET))

        feature_geometry_type = d.pop("Feature_geometry_type", UNSET)

        def _parse_perimeter_in_meters(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        perimeter_in_meters = _parse_perimeter_in_meters(
            d.pop("Perimeter_in_meters", UNSET)
        )

        def _parse_area_in_sq_meters(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        area_in_sq_meters = _parse_area_in_sq_meters(d.pop("Area_in_sq._meters", UNSET))

        wfs_map_server_wfs_amendpast_attributes = cls(
            objectid=objectid,
            application_case_number=application_case_number,
            further_information_number=further_information_number,
            district_planning_office=district_planning_office,
            ozp_scheme_code=ozp_scheme_code,
            ozp_plan_number=ozp_plan_number,
            case_status_code=case_status_code,
            proposed_amendment=proposed_amendment,
            location_address_of_application=location_address_of_application,
            latest_s_12a_decision_code=latest_s_12a_decision_code,
            date_of_latest_s_12a_latest_decision=date_of_latest_s_12a_latest_decision,
            last_upload_date=last_upload_date,
            feature_geometry_type=feature_geometry_type,
            perimeter_in_meters=perimeter_in_meters,
            area_in_sq_meters=area_in_sq_meters,
        )

        wfs_map_server_wfs_amendpast_attributes.additional_properties = d
        return wfs_map_server_wfs_amendpast_attributes

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
