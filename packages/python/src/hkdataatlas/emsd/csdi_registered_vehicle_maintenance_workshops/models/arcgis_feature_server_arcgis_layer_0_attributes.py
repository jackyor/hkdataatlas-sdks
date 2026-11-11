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
        area_english (None | str | Unset): Publisher field type: esriFieldTypeString
        area_traditional_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        business_address_english (None | str | Unset): Publisher field type: esriFieldTypeString
        business_address_traditional_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        district_english (None | str | Unset): Publisher field type: esriFieldTypeString
        district_traditional_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        expiry_date (None | str | Unset): Publisher field type: esriFieldTypeString
        fridays_closed (None | str | Unset): Publisher field type: esriFieldTypeString
        fridays_open (None | str | Unset): Publisher field type: esriFieldTypeString
        mondays_closed (None | str | Unset): Publisher field type: esriFieldTypeString
        mondays_open (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_company_english (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_company_traditional_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours (None | str | Unset): Publisher field type: esriFieldTypeString
        public_holidays_closed (None | str | Unset): Publisher field type: esriFieldTypeString
        public_holidays_open (None | str | Unset): Publisher field type: esriFieldTypeString
        registration_number (None | str | Unset): Publisher field type: esriFieldTypeString
        review_status (None | str | Unset): Publisher field type: esriFieldTypeString
        saturdays_closed (None | str | Unset): Publisher field type: esriFieldTypeString
        saturdays_open (None | str | Unset): Publisher field type: esriFieldTypeString
        service_scope (None | str | Unset): Publisher field type: esriFieldTypeString
        statutory_holidays_closed (None | str | Unset): Publisher field type: esriFieldTypeString
        statutory_holidays_open (None | str | Unset): Publisher field type: esriFieldTypeString
        sundays_closed (None | str | Unset): Publisher field type: esriFieldTypeString
        sundays_open (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_number (None | str | Unset): Publisher field type: esriFieldTypeString
        thursdays_closed (None | str | Unset): Publisher field type: esriFieldTypeString
        thursdays_open (None | str | Unset): Publisher field type: esriFieldTypeString
        tuesdays_closed (None | str | Unset): Publisher field type: esriFieldTypeString
        tuesdays_open (None | str | Unset): Publisher field type: esriFieldTypeString
        types_of_services_provided_by_the_workshop_english (None | str | Unset): Publisher field type:
            esriFieldTypeString
        types_of_services_provided_by_the_workshop_traditional_chinese (None | str | Unset): Publisher field type:
            esriFieldTypeString
        types_of_vehicles_serviced_english (None | str | Unset): Publisher field type: esriFieldTypeString
        types_of_vehicles_serviced_traditional_chinese (None | str | Unset): Publisher field type: esriFieldTypeString
        wednesdays_closed (None | str | Unset): Publisher field type: esriFieldTypeString
        wednesdays_open (None | str | Unset): Publisher field type: esriFieldTypeString
        workshop_type (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    area_english: None | str | Unset = UNSET
    area_traditional_chinese: None | str | Unset = UNSET
    business_address_english: None | str | Unset = UNSET
    business_address_traditional_chinese: None | str | Unset = UNSET
    district_english: None | str | Unset = UNSET
    district_traditional_chinese: None | str | Unset = UNSET
    expiry_date: None | str | Unset = UNSET
    fridays_closed: None | str | Unset = UNSET
    fridays_open: None | str | Unset = UNSET
    mondays_closed: None | str | Unset = UNSET
    mondays_open: None | str | Unset = UNSET
    name_of_company_english: None | str | Unset = UNSET
    name_of_company_traditional_chinese: None | str | Unset = UNSET
    opening_hours: None | str | Unset = UNSET
    public_holidays_closed: None | str | Unset = UNSET
    public_holidays_open: None | str | Unset = UNSET
    registration_number: None | str | Unset = UNSET
    review_status: None | str | Unset = UNSET
    saturdays_closed: None | str | Unset = UNSET
    saturdays_open: None | str | Unset = UNSET
    service_scope: None | str | Unset = UNSET
    statutory_holidays_closed: None | str | Unset = UNSET
    statutory_holidays_open: None | str | Unset = UNSET
    sundays_closed: None | str | Unset = UNSET
    sundays_open: None | str | Unset = UNSET
    telephone_number: None | str | Unset = UNSET
    thursdays_closed: None | str | Unset = UNSET
    thursdays_open: None | str | Unset = UNSET
    tuesdays_closed: None | str | Unset = UNSET
    tuesdays_open: None | str | Unset = UNSET
    types_of_services_provided_by_the_workshop_english: None | str | Unset = UNSET
    types_of_services_provided_by_the_workshop_traditional_chinese: (
        None | str | Unset
    ) = UNSET
    types_of_vehicles_serviced_english: None | str | Unset = UNSET
    types_of_vehicles_serviced_traditional_chinese: None | str | Unset = UNSET
    wednesdays_closed: None | str | Unset = UNSET
    wednesdays_open: None | str | Unset = UNSET
    workshop_type: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area_english: None | str | Unset
        if isinstance(self.area_english, Unset):
            area_english = UNSET
        else:
            area_english = self.area_english

        area_traditional_chinese: None | str | Unset
        if isinstance(self.area_traditional_chinese, Unset):
            area_traditional_chinese = UNSET
        else:
            area_traditional_chinese = self.area_traditional_chinese

        business_address_english: None | str | Unset
        if isinstance(self.business_address_english, Unset):
            business_address_english = UNSET
        else:
            business_address_english = self.business_address_english

        business_address_traditional_chinese: None | str | Unset
        if isinstance(self.business_address_traditional_chinese, Unset):
            business_address_traditional_chinese = UNSET
        else:
            business_address_traditional_chinese = (
                self.business_address_traditional_chinese
            )

        district_english: None | str | Unset
        if isinstance(self.district_english, Unset):
            district_english = UNSET
        else:
            district_english = self.district_english

        district_traditional_chinese: None | str | Unset
        if isinstance(self.district_traditional_chinese, Unset):
            district_traditional_chinese = UNSET
        else:
            district_traditional_chinese = self.district_traditional_chinese

        expiry_date: None | str | Unset
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        else:
            expiry_date = self.expiry_date

        fridays_closed: None | str | Unset
        if isinstance(self.fridays_closed, Unset):
            fridays_closed = UNSET
        else:
            fridays_closed = self.fridays_closed

        fridays_open: None | str | Unset
        if isinstance(self.fridays_open, Unset):
            fridays_open = UNSET
        else:
            fridays_open = self.fridays_open

        mondays_closed: None | str | Unset
        if isinstance(self.mondays_closed, Unset):
            mondays_closed = UNSET
        else:
            mondays_closed = self.mondays_closed

        mondays_open: None | str | Unset
        if isinstance(self.mondays_open, Unset):
            mondays_open = UNSET
        else:
            mondays_open = self.mondays_open

        name_of_company_english: None | str | Unset
        if isinstance(self.name_of_company_english, Unset):
            name_of_company_english = UNSET
        else:
            name_of_company_english = self.name_of_company_english

        name_of_company_traditional_chinese: None | str | Unset
        if isinstance(self.name_of_company_traditional_chinese, Unset):
            name_of_company_traditional_chinese = UNSET
        else:
            name_of_company_traditional_chinese = (
                self.name_of_company_traditional_chinese
            )

        opening_hours: None | str | Unset
        if isinstance(self.opening_hours, Unset):
            opening_hours = UNSET
        else:
            opening_hours = self.opening_hours

        public_holidays_closed: None | str | Unset
        if isinstance(self.public_holidays_closed, Unset):
            public_holidays_closed = UNSET
        else:
            public_holidays_closed = self.public_holidays_closed

        public_holidays_open: None | str | Unset
        if isinstance(self.public_holidays_open, Unset):
            public_holidays_open = UNSET
        else:
            public_holidays_open = self.public_holidays_open

        registration_number: None | str | Unset
        if isinstance(self.registration_number, Unset):
            registration_number = UNSET
        else:
            registration_number = self.registration_number

        review_status: None | str | Unset
        if isinstance(self.review_status, Unset):
            review_status = UNSET
        else:
            review_status = self.review_status

        saturdays_closed: None | str | Unset
        if isinstance(self.saturdays_closed, Unset):
            saturdays_closed = UNSET
        else:
            saturdays_closed = self.saturdays_closed

        saturdays_open: None | str | Unset
        if isinstance(self.saturdays_open, Unset):
            saturdays_open = UNSET
        else:
            saturdays_open = self.saturdays_open

        service_scope: None | str | Unset
        if isinstance(self.service_scope, Unset):
            service_scope = UNSET
        else:
            service_scope = self.service_scope

        statutory_holidays_closed: None | str | Unset
        if isinstance(self.statutory_holidays_closed, Unset):
            statutory_holidays_closed = UNSET
        else:
            statutory_holidays_closed = self.statutory_holidays_closed

        statutory_holidays_open: None | str | Unset
        if isinstance(self.statutory_holidays_open, Unset):
            statutory_holidays_open = UNSET
        else:
            statutory_holidays_open = self.statutory_holidays_open

        sundays_closed: None | str | Unset
        if isinstance(self.sundays_closed, Unset):
            sundays_closed = UNSET
        else:
            sundays_closed = self.sundays_closed

        sundays_open: None | str | Unset
        if isinstance(self.sundays_open, Unset):
            sundays_open = UNSET
        else:
            sundays_open = self.sundays_open

        telephone_number: None | str | Unset
        if isinstance(self.telephone_number, Unset):
            telephone_number = UNSET
        else:
            telephone_number = self.telephone_number

        thursdays_closed: None | str | Unset
        if isinstance(self.thursdays_closed, Unset):
            thursdays_closed = UNSET
        else:
            thursdays_closed = self.thursdays_closed

        thursdays_open: None | str | Unset
        if isinstance(self.thursdays_open, Unset):
            thursdays_open = UNSET
        else:
            thursdays_open = self.thursdays_open

        tuesdays_closed: None | str | Unset
        if isinstance(self.tuesdays_closed, Unset):
            tuesdays_closed = UNSET
        else:
            tuesdays_closed = self.tuesdays_closed

        tuesdays_open: None | str | Unset
        if isinstance(self.tuesdays_open, Unset):
            tuesdays_open = UNSET
        else:
            tuesdays_open = self.tuesdays_open

        types_of_services_provided_by_the_workshop_english: None | str | Unset
        if isinstance(self.types_of_services_provided_by_the_workshop_english, Unset):
            types_of_services_provided_by_the_workshop_english = UNSET
        else:
            types_of_services_provided_by_the_workshop_english = (
                self.types_of_services_provided_by_the_workshop_english
            )

        types_of_services_provided_by_the_workshop_traditional_chinese: (
            None | str | Unset
        )
        if isinstance(
            self.types_of_services_provided_by_the_workshop_traditional_chinese, Unset
        ):
            types_of_services_provided_by_the_workshop_traditional_chinese = UNSET
        else:
            types_of_services_provided_by_the_workshop_traditional_chinese = (
                self.types_of_services_provided_by_the_workshop_traditional_chinese
            )

        types_of_vehicles_serviced_english: None | str | Unset
        if isinstance(self.types_of_vehicles_serviced_english, Unset):
            types_of_vehicles_serviced_english = UNSET
        else:
            types_of_vehicles_serviced_english = self.types_of_vehicles_serviced_english

        types_of_vehicles_serviced_traditional_chinese: None | str | Unset
        if isinstance(self.types_of_vehicles_serviced_traditional_chinese, Unset):
            types_of_vehicles_serviced_traditional_chinese = UNSET
        else:
            types_of_vehicles_serviced_traditional_chinese = (
                self.types_of_vehicles_serviced_traditional_chinese
            )

        wednesdays_closed: None | str | Unset
        if isinstance(self.wednesdays_closed, Unset):
            wednesdays_closed = UNSET
        else:
            wednesdays_closed = self.wednesdays_closed

        wednesdays_open: None | str | Unset
        if isinstance(self.wednesdays_open, Unset):
            wednesdays_open = UNSET
        else:
            wednesdays_open = self.wednesdays_open

        workshop_type: float | None | Unset
        if isinstance(self.workshop_type, Unset):
            workshop_type = UNSET
        else:
            workshop_type = self.workshop_type

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area_english is not UNSET:
            field_dict["Area_English"] = area_english
        if area_traditional_chinese is not UNSET:
            field_dict["Area_Traditional_Chinese"] = area_traditional_chinese
        if business_address_english is not UNSET:
            field_dict["Business_Address_English"] = business_address_english
        if business_address_traditional_chinese is not UNSET:
            field_dict["Business_Address_Traditional_Chinese"] = (
                business_address_traditional_chinese
            )
        if district_english is not UNSET:
            field_dict["District_English"] = district_english
        if district_traditional_chinese is not UNSET:
            field_dict["District_Traditional_Chinese"] = district_traditional_chinese
        if expiry_date is not UNSET:
            field_dict["Expiry_Date"] = expiry_date
        if fridays_closed is not UNSET:
            field_dict["Fridays_Closed"] = fridays_closed
        if fridays_open is not UNSET:
            field_dict["Fridays_Open"] = fridays_open
        if mondays_closed is not UNSET:
            field_dict["Mondays_Closed"] = mondays_closed
        if mondays_open is not UNSET:
            field_dict["Mondays_Open"] = mondays_open
        if name_of_company_english is not UNSET:
            field_dict["Name_of_Company_English"] = name_of_company_english
        if name_of_company_traditional_chinese is not UNSET:
            field_dict["Name_of_Company_Traditional_Chinese"] = (
                name_of_company_traditional_chinese
            )
        if opening_hours is not UNSET:
            field_dict["Opening_Hours"] = opening_hours
        if public_holidays_closed is not UNSET:
            field_dict["Public_Holidays_Closed"] = public_holidays_closed
        if public_holidays_open is not UNSET:
            field_dict["Public_Holidays_Open"] = public_holidays_open
        if registration_number is not UNSET:
            field_dict["Registration_Number"] = registration_number
        if review_status is not UNSET:
            field_dict["Review_Status"] = review_status
        if saturdays_closed is not UNSET:
            field_dict["Saturdays_Closed"] = saturdays_closed
        if saturdays_open is not UNSET:
            field_dict["Saturdays_Open"] = saturdays_open
        if service_scope is not UNSET:
            field_dict["Service_Scope"] = service_scope
        if statutory_holidays_closed is not UNSET:
            field_dict["Statutory_Holidays_Closed"] = statutory_holidays_closed
        if statutory_holidays_open is not UNSET:
            field_dict["Statutory_Holidays_Open"] = statutory_holidays_open
        if sundays_closed is not UNSET:
            field_dict["Sundays_Closed"] = sundays_closed
        if sundays_open is not UNSET:
            field_dict["Sundays_Open"] = sundays_open
        if telephone_number is not UNSET:
            field_dict["Telephone_Number"] = telephone_number
        if thursdays_closed is not UNSET:
            field_dict["Thursdays_Closed"] = thursdays_closed
        if thursdays_open is not UNSET:
            field_dict["Thursdays_Open"] = thursdays_open
        if tuesdays_closed is not UNSET:
            field_dict["Tuesdays_Closed"] = tuesdays_closed
        if tuesdays_open is not UNSET:
            field_dict["Tuesdays_Open"] = tuesdays_open
        if types_of_services_provided_by_the_workshop_english is not UNSET:
            field_dict["Types_of_Services_Provided_by_the_Workshop_English"] = (
                types_of_services_provided_by_the_workshop_english
            )
        if types_of_services_provided_by_the_workshop_traditional_chinese is not UNSET:
            field_dict[
                "Types_of_Services_Provided_by_the_Workshop_Traditional_Chinese"
            ] = types_of_services_provided_by_the_workshop_traditional_chinese
        if types_of_vehicles_serviced_english is not UNSET:
            field_dict["Types_of_Vehicles_Serviced_English"] = (
                types_of_vehicles_serviced_english
            )
        if types_of_vehicles_serviced_traditional_chinese is not UNSET:
            field_dict["Types_of_Vehicles_Serviced_Traditional_Chinese"] = (
                types_of_vehicles_serviced_traditional_chinese
            )
        if wednesdays_closed is not UNSET:
            field_dict["Wednesdays_Closed"] = wednesdays_closed
        if wednesdays_open is not UNSET:
            field_dict["Wednesdays_Open"] = wednesdays_open
        if workshop_type is not UNSET:
            field_dict["Workshop_Type"] = workshop_type
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_area_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_english = _parse_area_english(d.pop("Area_English", UNSET))

        def _parse_area_traditional_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_traditional_chinese = _parse_area_traditional_chinese(
            d.pop("Area_Traditional_Chinese", UNSET)
        )

        def _parse_business_address_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        business_address_english = _parse_business_address_english(
            d.pop("Business_Address_English", UNSET)
        )

        def _parse_business_address_traditional_chinese(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        business_address_traditional_chinese = (
            _parse_business_address_traditional_chinese(
                d.pop("Business_Address_Traditional_Chinese", UNSET)
            )
        )

        def _parse_district_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_english = _parse_district_english(d.pop("District_English", UNSET))

        def _parse_district_traditional_chinese(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_traditional_chinese = _parse_district_traditional_chinese(
            d.pop("District_Traditional_Chinese", UNSET)
        )

        def _parse_expiry_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expiry_date = _parse_expiry_date(d.pop("Expiry_Date", UNSET))

        def _parse_fridays_closed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fridays_closed = _parse_fridays_closed(d.pop("Fridays_Closed", UNSET))

        def _parse_fridays_open(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fridays_open = _parse_fridays_open(d.pop("Fridays_Open", UNSET))

        def _parse_mondays_closed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mondays_closed = _parse_mondays_closed(d.pop("Mondays_Closed", UNSET))

        def _parse_mondays_open(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mondays_open = _parse_mondays_open(d.pop("Mondays_Open", UNSET))

        def _parse_name_of_company_english(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_company_english = _parse_name_of_company_english(
            d.pop("Name_of_Company_English", UNSET)
        )

        def _parse_name_of_company_traditional_chinese(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_company_traditional_chinese = (
            _parse_name_of_company_traditional_chinese(
                d.pop("Name_of_Company_Traditional_Chinese", UNSET)
            )
        )

        def _parse_opening_hours(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours = _parse_opening_hours(d.pop("Opening_Hours", UNSET))

        def _parse_public_holidays_closed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_holidays_closed = _parse_public_holidays_closed(
            d.pop("Public_Holidays_Closed", UNSET)
        )

        def _parse_public_holidays_open(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_holidays_open = _parse_public_holidays_open(
            d.pop("Public_Holidays_Open", UNSET)
        )

        def _parse_registration_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        registration_number = _parse_registration_number(
            d.pop("Registration_Number", UNSET)
        )

        def _parse_review_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        review_status = _parse_review_status(d.pop("Review_Status", UNSET))

        def _parse_saturdays_closed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saturdays_closed = _parse_saturdays_closed(d.pop("Saturdays_Closed", UNSET))

        def _parse_saturdays_open(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saturdays_open = _parse_saturdays_open(d.pop("Saturdays_Open", UNSET))

        def _parse_service_scope(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_scope = _parse_service_scope(d.pop("Service_Scope", UNSET))

        def _parse_statutory_holidays_closed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        statutory_holidays_closed = _parse_statutory_holidays_closed(
            d.pop("Statutory_Holidays_Closed", UNSET)
        )

        def _parse_statutory_holidays_open(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        statutory_holidays_open = _parse_statutory_holidays_open(
            d.pop("Statutory_Holidays_Open", UNSET)
        )

        def _parse_sundays_closed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sundays_closed = _parse_sundays_closed(d.pop("Sundays_Closed", UNSET))

        def _parse_sundays_open(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sundays_open = _parse_sundays_open(d.pop("Sundays_Open", UNSET))

        def _parse_telephone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_number = _parse_telephone_number(d.pop("Telephone_Number", UNSET))

        def _parse_thursdays_closed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thursdays_closed = _parse_thursdays_closed(d.pop("Thursdays_Closed", UNSET))

        def _parse_thursdays_open(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thursdays_open = _parse_thursdays_open(d.pop("Thursdays_Open", UNSET))

        def _parse_tuesdays_closed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tuesdays_closed = _parse_tuesdays_closed(d.pop("Tuesdays_Closed", UNSET))

        def _parse_tuesdays_open(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tuesdays_open = _parse_tuesdays_open(d.pop("Tuesdays_Open", UNSET))

        def _parse_types_of_services_provided_by_the_workshop_english(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_services_provided_by_the_workshop_english = (
            _parse_types_of_services_provided_by_the_workshop_english(
                d.pop("Types_of_Services_Provided_by_the_Workshop_English", UNSET)
            )
        )

        def _parse_types_of_services_provided_by_the_workshop_traditional_chinese(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_services_provided_by_the_workshop_traditional_chinese = (
            _parse_types_of_services_provided_by_the_workshop_traditional_chinese(
                d.pop(
                    "Types_of_Services_Provided_by_the_Workshop_Traditional_Chinese",
                    UNSET,
                )
            )
        )

        def _parse_types_of_vehicles_serviced_english(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_vehicles_serviced_english = _parse_types_of_vehicles_serviced_english(
            d.pop("Types_of_Vehicles_Serviced_English", UNSET)
        )

        def _parse_types_of_vehicles_serviced_traditional_chinese(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_vehicles_serviced_traditional_chinese = (
            _parse_types_of_vehicles_serviced_traditional_chinese(
                d.pop("Types_of_Vehicles_Serviced_Traditional_Chinese", UNSET)
            )
        )

        def _parse_wednesdays_closed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wednesdays_closed = _parse_wednesdays_closed(d.pop("Wednesdays_Closed", UNSET))

        def _parse_wednesdays_open(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wednesdays_open = _parse_wednesdays_open(d.pop("Wednesdays_Open", UNSET))

        def _parse_workshop_type(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        workshop_type = _parse_workshop_type(d.pop("Workshop_Type", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            area_english=area_english,
            area_traditional_chinese=area_traditional_chinese,
            business_address_english=business_address_english,
            business_address_traditional_chinese=business_address_traditional_chinese,
            district_english=district_english,
            district_traditional_chinese=district_traditional_chinese,
            expiry_date=expiry_date,
            fridays_closed=fridays_closed,
            fridays_open=fridays_open,
            mondays_closed=mondays_closed,
            mondays_open=mondays_open,
            name_of_company_english=name_of_company_english,
            name_of_company_traditional_chinese=name_of_company_traditional_chinese,
            opening_hours=opening_hours,
            public_holidays_closed=public_holidays_closed,
            public_holidays_open=public_holidays_open,
            registration_number=registration_number,
            review_status=review_status,
            saturdays_closed=saturdays_closed,
            saturdays_open=saturdays_open,
            service_scope=service_scope,
            statutory_holidays_closed=statutory_holidays_closed,
            statutory_holidays_open=statutory_holidays_open,
            sundays_closed=sundays_closed,
            sundays_open=sundays_open,
            telephone_number=telephone_number,
            thursdays_closed=thursdays_closed,
            thursdays_open=thursdays_open,
            tuesdays_closed=tuesdays_closed,
            tuesdays_open=tuesdays_open,
            types_of_services_provided_by_the_workshop_english=types_of_services_provided_by_the_workshop_english,
            types_of_services_provided_by_the_workshop_traditional_chinese=types_of_services_provided_by_the_workshop_traditional_chinese,
            types_of_vehicles_serviced_english=types_of_vehicles_serviced_english,
            types_of_vehicles_serviced_traditional_chinese=types_of_vehicles_serviced_traditional_chinese,
            wednesdays_closed=wednesdays_closed,
            wednesdays_open=wednesdays_open,
            workshop_type=workshop_type,
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
