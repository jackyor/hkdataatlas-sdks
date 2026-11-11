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
        carpark_no (None | str | Unset): Publisher field type: esriFieldTypeString
        en_address (None | str | Unset): Publisher field type: esriFieldTypeString
        en_district (None | str | Unset): Publisher field type: esriFieldTypeString
        en_landlords_break_clause (None | str | Unset): Publisher field type: esriFieldTypeString
        en_monthly_rent (None | str | Unset): Publisher field type: esriFieldTypeString
        en_name (None | str | Unset): Publisher field type: esriFieldTypeString
        en_photos_description (None | str | Unset): Publisher field type: esriFieldTypeString
        en_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        en_rent_free_period (None | str | Unset): Publisher field type: esriFieldTypeString
        en_tenants_break_clause (None | str | Unset): Publisher field type: esriFieldTypeString
        en_term (None | str | Unset): Publisher field type: esriFieldTypeString
        en_website (None | str | Unset): Publisher field type: esriFieldTypeString
        number_of_bedrooms (float | None | Unset): Publisher field type: esriFieldTypeDouble
        photos (None | str | Unset): Publisher field type: esriFieldTypeString
        saleable_area_in_square_feet (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_landlords_break_clause (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_monthly_rent (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_name (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_photos_description (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_rent_free_period (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_tenants_break_clause (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_term (None | str | Unset): Publisher field type: esriFieldTypeString
        sc_website (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_address (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_district (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_landlords_break_clause (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_monthly_rent (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_name (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_photos_description (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_remarks (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_rent_free_period (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_tenants_break_clause (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_term (None | str | Unset): Publisher field type: esriFieldTypeString
        tc_website (None | str | Unset): Publisher field type: esriFieldTypeString
        year_built (float | None | Unset): Publisher field type: esriFieldTypeDouble
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    carpark_no: None | str | Unset = UNSET
    en_address: None | str | Unset = UNSET
    en_district: None | str | Unset = UNSET
    en_landlords_break_clause: None | str | Unset = UNSET
    en_monthly_rent: None | str | Unset = UNSET
    en_name: None | str | Unset = UNSET
    en_photos_description: None | str | Unset = UNSET
    en_remarks: None | str | Unset = UNSET
    en_rent_free_period: None | str | Unset = UNSET
    en_tenants_break_clause: None | str | Unset = UNSET
    en_term: None | str | Unset = UNSET
    en_website: None | str | Unset = UNSET
    number_of_bedrooms: float | None | Unset = UNSET
    photos: None | str | Unset = UNSET
    saleable_area_in_square_feet: float | None | Unset = UNSET
    sc_address: None | str | Unset = UNSET
    sc_district: None | str | Unset = UNSET
    sc_landlords_break_clause: None | str | Unset = UNSET
    sc_monthly_rent: None | str | Unset = UNSET
    sc_name: None | str | Unset = UNSET
    sc_photos_description: None | str | Unset = UNSET
    sc_remarks: None | str | Unset = UNSET
    sc_rent_free_period: None | str | Unset = UNSET
    sc_tenants_break_clause: None | str | Unset = UNSET
    sc_term: None | str | Unset = UNSET
    sc_website: None | str | Unset = UNSET
    tc_address: None | str | Unset = UNSET
    tc_district: None | str | Unset = UNSET
    tc_landlords_break_clause: None | str | Unset = UNSET
    tc_monthly_rent: None | str | Unset = UNSET
    tc_name: None | str | Unset = UNSET
    tc_photos_description: None | str | Unset = UNSET
    tc_remarks: None | str | Unset = UNSET
    tc_rent_free_period: None | str | Unset = UNSET
    tc_tenants_break_clause: None | str | Unset = UNSET
    tc_term: None | str | Unset = UNSET
    tc_website: None | str | Unset = UNSET
    year_built: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carpark_no: None | str | Unset
        if isinstance(self.carpark_no, Unset):
            carpark_no = UNSET
        else:
            carpark_no = self.carpark_no

        en_address: None | str | Unset
        if isinstance(self.en_address, Unset):
            en_address = UNSET
        else:
            en_address = self.en_address

        en_district: None | str | Unset
        if isinstance(self.en_district, Unset):
            en_district = UNSET
        else:
            en_district = self.en_district

        en_landlords_break_clause: None | str | Unset
        if isinstance(self.en_landlords_break_clause, Unset):
            en_landlords_break_clause = UNSET
        else:
            en_landlords_break_clause = self.en_landlords_break_clause

        en_monthly_rent: None | str | Unset
        if isinstance(self.en_monthly_rent, Unset):
            en_monthly_rent = UNSET
        else:
            en_monthly_rent = self.en_monthly_rent

        en_name: None | str | Unset
        if isinstance(self.en_name, Unset):
            en_name = UNSET
        else:
            en_name = self.en_name

        en_photos_description: None | str | Unset
        if isinstance(self.en_photos_description, Unset):
            en_photos_description = UNSET
        else:
            en_photos_description = self.en_photos_description

        en_remarks: None | str | Unset
        if isinstance(self.en_remarks, Unset):
            en_remarks = UNSET
        else:
            en_remarks = self.en_remarks

        en_rent_free_period: None | str | Unset
        if isinstance(self.en_rent_free_period, Unset):
            en_rent_free_period = UNSET
        else:
            en_rent_free_period = self.en_rent_free_period

        en_tenants_break_clause: None | str | Unset
        if isinstance(self.en_tenants_break_clause, Unset):
            en_tenants_break_clause = UNSET
        else:
            en_tenants_break_clause = self.en_tenants_break_clause

        en_term: None | str | Unset
        if isinstance(self.en_term, Unset):
            en_term = UNSET
        else:
            en_term = self.en_term

        en_website: None | str | Unset
        if isinstance(self.en_website, Unset):
            en_website = UNSET
        else:
            en_website = self.en_website

        number_of_bedrooms: float | None | Unset
        if isinstance(self.number_of_bedrooms, Unset):
            number_of_bedrooms = UNSET
        else:
            number_of_bedrooms = self.number_of_bedrooms

        photos: None | str | Unset
        if isinstance(self.photos, Unset):
            photos = UNSET
        else:
            photos = self.photos

        saleable_area_in_square_feet: float | None | Unset
        if isinstance(self.saleable_area_in_square_feet, Unset):
            saleable_area_in_square_feet = UNSET
        else:
            saleable_area_in_square_feet = self.saleable_area_in_square_feet

        sc_address: None | str | Unset
        if isinstance(self.sc_address, Unset):
            sc_address = UNSET
        else:
            sc_address = self.sc_address

        sc_district: None | str | Unset
        if isinstance(self.sc_district, Unset):
            sc_district = UNSET
        else:
            sc_district = self.sc_district

        sc_landlords_break_clause: None | str | Unset
        if isinstance(self.sc_landlords_break_clause, Unset):
            sc_landlords_break_clause = UNSET
        else:
            sc_landlords_break_clause = self.sc_landlords_break_clause

        sc_monthly_rent: None | str | Unset
        if isinstance(self.sc_monthly_rent, Unset):
            sc_monthly_rent = UNSET
        else:
            sc_monthly_rent = self.sc_monthly_rent

        sc_name: None | str | Unset
        if isinstance(self.sc_name, Unset):
            sc_name = UNSET
        else:
            sc_name = self.sc_name

        sc_photos_description: None | str | Unset
        if isinstance(self.sc_photos_description, Unset):
            sc_photos_description = UNSET
        else:
            sc_photos_description = self.sc_photos_description

        sc_remarks: None | str | Unset
        if isinstance(self.sc_remarks, Unset):
            sc_remarks = UNSET
        else:
            sc_remarks = self.sc_remarks

        sc_rent_free_period: None | str | Unset
        if isinstance(self.sc_rent_free_period, Unset):
            sc_rent_free_period = UNSET
        else:
            sc_rent_free_period = self.sc_rent_free_period

        sc_tenants_break_clause: None | str | Unset
        if isinstance(self.sc_tenants_break_clause, Unset):
            sc_tenants_break_clause = UNSET
        else:
            sc_tenants_break_clause = self.sc_tenants_break_clause

        sc_term: None | str | Unset
        if isinstance(self.sc_term, Unset):
            sc_term = UNSET
        else:
            sc_term = self.sc_term

        sc_website: None | str | Unset
        if isinstance(self.sc_website, Unset):
            sc_website = UNSET
        else:
            sc_website = self.sc_website

        tc_address: None | str | Unset
        if isinstance(self.tc_address, Unset):
            tc_address = UNSET
        else:
            tc_address = self.tc_address

        tc_district: None | str | Unset
        if isinstance(self.tc_district, Unset):
            tc_district = UNSET
        else:
            tc_district = self.tc_district

        tc_landlords_break_clause: None | str | Unset
        if isinstance(self.tc_landlords_break_clause, Unset):
            tc_landlords_break_clause = UNSET
        else:
            tc_landlords_break_clause = self.tc_landlords_break_clause

        tc_monthly_rent: None | str | Unset
        if isinstance(self.tc_monthly_rent, Unset):
            tc_monthly_rent = UNSET
        else:
            tc_monthly_rent = self.tc_monthly_rent

        tc_name: None | str | Unset
        if isinstance(self.tc_name, Unset):
            tc_name = UNSET
        else:
            tc_name = self.tc_name

        tc_photos_description: None | str | Unset
        if isinstance(self.tc_photos_description, Unset):
            tc_photos_description = UNSET
        else:
            tc_photos_description = self.tc_photos_description

        tc_remarks: None | str | Unset
        if isinstance(self.tc_remarks, Unset):
            tc_remarks = UNSET
        else:
            tc_remarks = self.tc_remarks

        tc_rent_free_period: None | str | Unset
        if isinstance(self.tc_rent_free_period, Unset):
            tc_rent_free_period = UNSET
        else:
            tc_rent_free_period = self.tc_rent_free_period

        tc_tenants_break_clause: None | str | Unset
        if isinstance(self.tc_tenants_break_clause, Unset):
            tc_tenants_break_clause = UNSET
        else:
            tc_tenants_break_clause = self.tc_tenants_break_clause

        tc_term: None | str | Unset
        if isinstance(self.tc_term, Unset):
            tc_term = UNSET
        else:
            tc_term = self.tc_term

        tc_website: None | str | Unset
        if isinstance(self.tc_website, Unset):
            tc_website = UNSET
        else:
            tc_website = self.tc_website

        year_built: float | None | Unset
        if isinstance(self.year_built, Unset):
            year_built = UNSET
        else:
            year_built = self.year_built

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carpark_no is not UNSET:
            field_dict["carpark_no"] = carpark_no
        if en_address is not UNSET:
            field_dict["en_address"] = en_address
        if en_district is not UNSET:
            field_dict["en_district"] = en_district
        if en_landlords_break_clause is not UNSET:
            field_dict["en_landlords_break_clause"] = en_landlords_break_clause
        if en_monthly_rent is not UNSET:
            field_dict["en_monthly_rent"] = en_monthly_rent
        if en_name is not UNSET:
            field_dict["en_name"] = en_name
        if en_photos_description is not UNSET:
            field_dict["en_photos_description"] = en_photos_description
        if en_remarks is not UNSET:
            field_dict["en_remarks"] = en_remarks
        if en_rent_free_period is not UNSET:
            field_dict["en_rent_free_period"] = en_rent_free_period
        if en_tenants_break_clause is not UNSET:
            field_dict["en_tenants_break_clause"] = en_tenants_break_clause
        if en_term is not UNSET:
            field_dict["en_term"] = en_term
        if en_website is not UNSET:
            field_dict["en_website"] = en_website
        if number_of_bedrooms is not UNSET:
            field_dict["number_of_bedrooms"] = number_of_bedrooms
        if photos is not UNSET:
            field_dict["photos"] = photos
        if saleable_area_in_square_feet is not UNSET:
            field_dict["saleable_area_in_square_feet"] = saleable_area_in_square_feet
        if sc_address is not UNSET:
            field_dict["sc_address"] = sc_address
        if sc_district is not UNSET:
            field_dict["sc_district"] = sc_district
        if sc_landlords_break_clause is not UNSET:
            field_dict["sc_landlords_break_clause"] = sc_landlords_break_clause
        if sc_monthly_rent is not UNSET:
            field_dict["sc_monthly_rent"] = sc_monthly_rent
        if sc_name is not UNSET:
            field_dict["sc_name"] = sc_name
        if sc_photos_description is not UNSET:
            field_dict["sc_photos_description"] = sc_photos_description
        if sc_remarks is not UNSET:
            field_dict["sc_remarks"] = sc_remarks
        if sc_rent_free_period is not UNSET:
            field_dict["sc_rent_free_period"] = sc_rent_free_period
        if sc_tenants_break_clause is not UNSET:
            field_dict["sc_tenants_break_clause"] = sc_tenants_break_clause
        if sc_term is not UNSET:
            field_dict["sc_term"] = sc_term
        if sc_website is not UNSET:
            field_dict["sc_website"] = sc_website
        if tc_address is not UNSET:
            field_dict["tc_address"] = tc_address
        if tc_district is not UNSET:
            field_dict["tc_district"] = tc_district
        if tc_landlords_break_clause is not UNSET:
            field_dict["tc_landlords_break_clause"] = tc_landlords_break_clause
        if tc_monthly_rent is not UNSET:
            field_dict["tc_monthly_rent"] = tc_monthly_rent
        if tc_name is not UNSET:
            field_dict["tc_name"] = tc_name
        if tc_photos_description is not UNSET:
            field_dict["tc_photos_description"] = tc_photos_description
        if tc_remarks is not UNSET:
            field_dict["tc_remarks"] = tc_remarks
        if tc_rent_free_period is not UNSET:
            field_dict["tc_rent_free_period"] = tc_rent_free_period
        if tc_tenants_break_clause is not UNSET:
            field_dict["tc_tenants_break_clause"] = tc_tenants_break_clause
        if tc_term is not UNSET:
            field_dict["tc_term"] = tc_term
        if tc_website is not UNSET:
            field_dict["tc_website"] = tc_website
        if year_built is not UNSET:
            field_dict["year_built"] = year_built
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_carpark_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carpark_no = _parse_carpark_no(d.pop("carpark_no", UNSET))

        def _parse_en_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_address = _parse_en_address(d.pop("en_address", UNSET))

        def _parse_en_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_district = _parse_en_district(d.pop("en_district", UNSET))

        def _parse_en_landlords_break_clause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_landlords_break_clause = _parse_en_landlords_break_clause(
            d.pop("en_landlords_break_clause", UNSET)
        )

        def _parse_en_monthly_rent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_monthly_rent = _parse_en_monthly_rent(d.pop("en_monthly_rent", UNSET))

        def _parse_en_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_name = _parse_en_name(d.pop("en_name", UNSET))

        def _parse_en_photos_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_photos_description = _parse_en_photos_description(
            d.pop("en_photos_description", UNSET)
        )

        def _parse_en_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_remarks = _parse_en_remarks(d.pop("en_remarks", UNSET))

        def _parse_en_rent_free_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_rent_free_period = _parse_en_rent_free_period(
            d.pop("en_rent_free_period", UNSET)
        )

        def _parse_en_tenants_break_clause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_tenants_break_clause = _parse_en_tenants_break_clause(
            d.pop("en_tenants_break_clause", UNSET)
        )

        def _parse_en_term(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_term = _parse_en_term(d.pop("en_term", UNSET))

        def _parse_en_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_website = _parse_en_website(d.pop("en_website", UNSET))

        def _parse_number_of_bedrooms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        number_of_bedrooms = _parse_number_of_bedrooms(
            d.pop("number_of_bedrooms", UNSET)
        )

        def _parse_photos(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photos = _parse_photos(d.pop("photos", UNSET))

        def _parse_saleable_area_in_square_feet(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        saleable_area_in_square_feet = _parse_saleable_area_in_square_feet(
            d.pop("saleable_area_in_square_feet", UNSET)
        )

        def _parse_sc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_address = _parse_sc_address(d.pop("sc_address", UNSET))

        def _parse_sc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_district = _parse_sc_district(d.pop("sc_district", UNSET))

        def _parse_sc_landlords_break_clause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_landlords_break_clause = _parse_sc_landlords_break_clause(
            d.pop("sc_landlords_break_clause", UNSET)
        )

        def _parse_sc_monthly_rent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_monthly_rent = _parse_sc_monthly_rent(d.pop("sc_monthly_rent", UNSET))

        def _parse_sc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_name = _parse_sc_name(d.pop("sc_name", UNSET))

        def _parse_sc_photos_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_photos_description = _parse_sc_photos_description(
            d.pop("sc_photos_description", UNSET)
        )

        def _parse_sc_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_remarks = _parse_sc_remarks(d.pop("sc_remarks", UNSET))

        def _parse_sc_rent_free_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_rent_free_period = _parse_sc_rent_free_period(
            d.pop("sc_rent_free_period", UNSET)
        )

        def _parse_sc_tenants_break_clause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_tenants_break_clause = _parse_sc_tenants_break_clause(
            d.pop("sc_tenants_break_clause", UNSET)
        )

        def _parse_sc_term(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_term = _parse_sc_term(d.pop("sc_term", UNSET))

        def _parse_sc_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_website = _parse_sc_website(d.pop("sc_website", UNSET))

        def _parse_tc_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_address = _parse_tc_address(d.pop("tc_address", UNSET))

        def _parse_tc_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_district = _parse_tc_district(d.pop("tc_district", UNSET))

        def _parse_tc_landlords_break_clause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_landlords_break_clause = _parse_tc_landlords_break_clause(
            d.pop("tc_landlords_break_clause", UNSET)
        )

        def _parse_tc_monthly_rent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_monthly_rent = _parse_tc_monthly_rent(d.pop("tc_monthly_rent", UNSET))

        def _parse_tc_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_name = _parse_tc_name(d.pop("tc_name", UNSET))

        def _parse_tc_photos_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_photos_description = _parse_tc_photos_description(
            d.pop("tc_photos_description", UNSET)
        )

        def _parse_tc_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_remarks = _parse_tc_remarks(d.pop("tc_remarks", UNSET))

        def _parse_tc_rent_free_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_rent_free_period = _parse_tc_rent_free_period(
            d.pop("tc_rent_free_period", UNSET)
        )

        def _parse_tc_tenants_break_clause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_tenants_break_clause = _parse_tc_tenants_break_clause(
            d.pop("tc_tenants_break_clause", UNSET)
        )

        def _parse_tc_term(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_term = _parse_tc_term(d.pop("tc_term", UNSET))

        def _parse_tc_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_website = _parse_tc_website(d.pop("tc_website", UNSET))

        def _parse_year_built(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year_built = _parse_year_built(d.pop("year_built", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            carpark_no=carpark_no,
            en_address=en_address,
            en_district=en_district,
            en_landlords_break_clause=en_landlords_break_clause,
            en_monthly_rent=en_monthly_rent,
            en_name=en_name,
            en_photos_description=en_photos_description,
            en_remarks=en_remarks,
            en_rent_free_period=en_rent_free_period,
            en_tenants_break_clause=en_tenants_break_clause,
            en_term=en_term,
            en_website=en_website,
            number_of_bedrooms=number_of_bedrooms,
            photos=photos,
            saleable_area_in_square_feet=saleable_area_in_square_feet,
            sc_address=sc_address,
            sc_district=sc_district,
            sc_landlords_break_clause=sc_landlords_break_clause,
            sc_monthly_rent=sc_monthly_rent,
            sc_name=sc_name,
            sc_photos_description=sc_photos_description,
            sc_remarks=sc_remarks,
            sc_rent_free_period=sc_rent_free_period,
            sc_tenants_break_clause=sc_tenants_break_clause,
            sc_term=sc_term,
            sc_website=sc_website,
            tc_address=tc_address,
            tc_district=tc_district,
            tc_landlords_break_clause=tc_landlords_break_clause,
            tc_monthly_rent=tc_monthly_rent,
            tc_name=tc_name,
            tc_photos_description=tc_photos_description,
            tc_remarks=tc_remarks,
            tc_rent_free_period=tc_rent_free_period,
            tc_tenants_break_clause=tc_tenants_break_clause,
            tc_term=tc_term,
            tc_website=tc_website,
            year_built=year_built,
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
