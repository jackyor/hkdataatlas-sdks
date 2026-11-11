from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsAPPPASTAttributes")


@_attrs_define
class WfsMapServerWfsAPPPASTAttributes:
    """
    Attributes:
        feature_id (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        application_case_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        application_type_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
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
        applied_use (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_address_of_application (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        appeal_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        latest_s_16_decision_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        date_of_latest_s_16_decision (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        latest_s_17_decision_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        date_of_latest_s_17_decision (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        latest_s_17b_decision_code (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        date_of_latest_s_17b_decision (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        last_upload_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
        feature_geometry_type (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not
            inferred from its XML type.
        perimeter_in_meters (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        area_in_sq_meters (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    feature_id: int | Unset = UNSET
    application_case_number: None | str | Unset = UNSET
    application_type_code: None | str | Unset = UNSET
    further_information_number: int | None | Unset = UNSET
    district_planning_office: None | str | Unset = UNSET
    ozp_scheme_code: None | str | Unset = UNSET
    ozp_plan_number: None | str | Unset = UNSET
    case_status_code: None | str | Unset = UNSET
    applied_use: None | str | Unset = UNSET
    location_address_of_application: None | str | Unset = UNSET
    appeal_number: None | str | Unset = UNSET
    latest_s_16_decision_code: None | str | Unset = UNSET
    date_of_latest_s_16_decision: None | str | Unset = UNSET
    latest_s_17_decision_code: None | str | Unset = UNSET
    date_of_latest_s_17_decision: None | str | Unset = UNSET
    latest_s_17b_decision_code: None | str | Unset = UNSET
    date_of_latest_s_17b_decision: None | str | Unset = UNSET
    last_upload_date: None | str | Unset = UNSET
    feature_geometry_type: Any | Unset = UNSET
    perimeter_in_meters: float | None | Unset = UNSET
    area_in_sq_meters: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature_id = self.feature_id

        application_case_number: None | str | Unset
        if isinstance(self.application_case_number, Unset):
            application_case_number = UNSET
        else:
            application_case_number = self.application_case_number

        application_type_code: None | str | Unset
        if isinstance(self.application_type_code, Unset):
            application_type_code = UNSET
        else:
            application_type_code = self.application_type_code

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

        applied_use: None | str | Unset
        if isinstance(self.applied_use, Unset):
            applied_use = UNSET
        else:
            applied_use = self.applied_use

        location_address_of_application: None | str | Unset
        if isinstance(self.location_address_of_application, Unset):
            location_address_of_application = UNSET
        else:
            location_address_of_application = self.location_address_of_application

        appeal_number: None | str | Unset
        if isinstance(self.appeal_number, Unset):
            appeal_number = UNSET
        else:
            appeal_number = self.appeal_number

        latest_s_16_decision_code: None | str | Unset
        if isinstance(self.latest_s_16_decision_code, Unset):
            latest_s_16_decision_code = UNSET
        else:
            latest_s_16_decision_code = self.latest_s_16_decision_code

        date_of_latest_s_16_decision: None | str | Unset
        if isinstance(self.date_of_latest_s_16_decision, Unset):
            date_of_latest_s_16_decision = UNSET
        else:
            date_of_latest_s_16_decision = self.date_of_latest_s_16_decision

        latest_s_17_decision_code: None | str | Unset
        if isinstance(self.latest_s_17_decision_code, Unset):
            latest_s_17_decision_code = UNSET
        else:
            latest_s_17_decision_code = self.latest_s_17_decision_code

        date_of_latest_s_17_decision: None | str | Unset
        if isinstance(self.date_of_latest_s_17_decision, Unset):
            date_of_latest_s_17_decision = UNSET
        else:
            date_of_latest_s_17_decision = self.date_of_latest_s_17_decision

        latest_s_17b_decision_code: None | str | Unset
        if isinstance(self.latest_s_17b_decision_code, Unset):
            latest_s_17b_decision_code = UNSET
        else:
            latest_s_17b_decision_code = self.latest_s_17b_decision_code

        date_of_latest_s_17b_decision: None | str | Unset
        if isinstance(self.date_of_latest_s_17b_decision, Unset):
            date_of_latest_s_17b_decision = UNSET
        else:
            date_of_latest_s_17b_decision = self.date_of_latest_s_17b_decision

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
        if feature_id is not UNSET:
            field_dict["Feature_ID"] = feature_id
        if application_case_number is not UNSET:
            field_dict["Application_case_number"] = application_case_number
        if application_type_code is not UNSET:
            field_dict["Application_type_code"] = application_type_code
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
        if applied_use is not UNSET:
            field_dict["Applied_use"] = applied_use
        if location_address_of_application is not UNSET:
            field_dict["Location_address_of_application"] = (
                location_address_of_application
            )
        if appeal_number is not UNSET:
            field_dict["Appeal_number"] = appeal_number
        if latest_s_16_decision_code is not UNSET:
            field_dict["Latest_s.16_decision_code"] = latest_s_16_decision_code
        if date_of_latest_s_16_decision is not UNSET:
            field_dict["Date_of_latest_s.16_decision"] = date_of_latest_s_16_decision
        if latest_s_17_decision_code is not UNSET:
            field_dict["Latest_s.17_decision_code"] = latest_s_17_decision_code
        if date_of_latest_s_17_decision is not UNSET:
            field_dict["Date_of_latest_s.17_decision"] = date_of_latest_s_17_decision
        if latest_s_17b_decision_code is not UNSET:
            field_dict["Latest_s.17B_decision_code"] = latest_s_17b_decision_code
        if date_of_latest_s_17b_decision is not UNSET:
            field_dict["Date_of_latest_s.17B_decision"] = date_of_latest_s_17b_decision
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
        feature_id = d.pop("Feature_ID", UNSET)

        def _parse_application_case_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_case_number = _parse_application_case_number(
            d.pop("Application_case_number", UNSET)
        )

        def _parse_application_type_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_type_code = _parse_application_type_code(
            d.pop("Application_type_code", UNSET)
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

        def _parse_applied_use(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        applied_use = _parse_applied_use(d.pop("Applied_use", UNSET))

        def _parse_location_address_of_application(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_address_of_application = _parse_location_address_of_application(
            d.pop("Location_address_of_application", UNSET)
        )

        def _parse_appeal_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        appeal_number = _parse_appeal_number(d.pop("Appeal_number", UNSET))

        def _parse_latest_s_16_decision_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_s_16_decision_code = _parse_latest_s_16_decision_code(
            d.pop("Latest_s.16_decision_code", UNSET)
        )

        def _parse_date_of_latest_s_16_decision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_latest_s_16_decision = _parse_date_of_latest_s_16_decision(
            d.pop("Date_of_latest_s.16_decision", UNSET)
        )

        def _parse_latest_s_17_decision_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_s_17_decision_code = _parse_latest_s_17_decision_code(
            d.pop("Latest_s.17_decision_code", UNSET)
        )

        def _parse_date_of_latest_s_17_decision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_latest_s_17_decision = _parse_date_of_latest_s_17_decision(
            d.pop("Date_of_latest_s.17_decision", UNSET)
        )

        def _parse_latest_s_17b_decision_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latest_s_17b_decision_code = _parse_latest_s_17b_decision_code(
            d.pop("Latest_s.17B_decision_code", UNSET)
        )

        def _parse_date_of_latest_s_17b_decision(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_of_latest_s_17b_decision = _parse_date_of_latest_s_17b_decision(
            d.pop("Date_of_latest_s.17B_decision", UNSET)
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

        wfs_map_server_wfs_apppast_attributes = cls(
            feature_id=feature_id,
            application_case_number=application_case_number,
            application_type_code=application_type_code,
            further_information_number=further_information_number,
            district_planning_office=district_planning_office,
            ozp_scheme_code=ozp_scheme_code,
            ozp_plan_number=ozp_plan_number,
            case_status_code=case_status_code,
            applied_use=applied_use,
            location_address_of_application=location_address_of_application,
            appeal_number=appeal_number,
            latest_s_16_decision_code=latest_s_16_decision_code,
            date_of_latest_s_16_decision=date_of_latest_s_16_decision,
            latest_s_17_decision_code=latest_s_17_decision_code,
            date_of_latest_s_17_decision=date_of_latest_s_17_decision,
            latest_s_17b_decision_code=latest_s_17b_decision_code,
            date_of_latest_s_17b_decision=date_of_latest_s_17b_decision,
            last_upload_date=last_upload_date,
            feature_geometry_type=feature_geometry_type,
            perimeter_in_meters=perimeter_in_meters,
            area_in_sq_meters=area_in_sq_meters,
        )

        wfs_map_server_wfs_apppast_attributes.additional_properties = d
        return wfs_map_server_wfs_apppast_attributes

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
