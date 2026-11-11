from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsCommercialPropertiesAttributes")


@_attrs_define
class WfsMapServerWfsCommercialPropertiesAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        estate_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        estate_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        estate_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        region_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        region_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        region_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        year_of_completion_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        year_of_completion_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        year_of_completion_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        no_of_floors_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        no_of_floors_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        no_of_floors_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        total_lettable_area_m2_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        total_lettable_area_m2_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        total_lettable_area_m2_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        property_management_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        property_management_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        property_management_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        carpark_management_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        carpark_management_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        carpark_management_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        shopping_centre_website (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        further_information_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        further_information_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        further_information_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    estate_name_en: None | str | Unset = UNSET
    estate_name_tc: None | str | Unset = UNSET
    estate_name_sc: None | str | Unset = UNSET
    district_name_en: None | str | Unset = UNSET
    district_name_tc: None | str | Unset = UNSET
    district_name_sc: None | str | Unset = UNSET
    region_name_en: None | str | Unset = UNSET
    region_name_tc: None | str | Unset = UNSET
    region_name_sc: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    year_of_completion_en: None | str | Unset = UNSET
    year_of_completion_tc: None | str | Unset = UNSET
    year_of_completion_sc: None | str | Unset = UNSET
    no_of_floors_en: None | str | Unset = UNSET
    no_of_floors_tc: None | str | Unset = UNSET
    no_of_floors_sc: None | str | Unset = UNSET
    total_lettable_area_m2_en: None | str | Unset = UNSET
    total_lettable_area_m2_tc: None | str | Unset = UNSET
    total_lettable_area_m2_sc: None | str | Unset = UNSET
    property_management_en: None | str | Unset = UNSET
    property_management_tc: None | str | Unset = UNSET
    property_management_sc: None | str | Unset = UNSET
    carpark_management_en: None | str | Unset = UNSET
    carpark_management_tc: None | str | Unset = UNSET
    carpark_management_sc: None | str | Unset = UNSET
    shopping_centre_website: None | str | Unset = UNSET
    further_information_en: None | str | Unset = UNSET
    further_information_tc: None | str | Unset = UNSET
    further_information_sc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        estate_name_en: None | str | Unset
        if isinstance(self.estate_name_en, Unset):
            estate_name_en = UNSET
        else:
            estate_name_en = self.estate_name_en

        estate_name_tc: None | str | Unset
        if isinstance(self.estate_name_tc, Unset):
            estate_name_tc = UNSET
        else:
            estate_name_tc = self.estate_name_tc

        estate_name_sc: None | str | Unset
        if isinstance(self.estate_name_sc, Unset):
            estate_name_sc = UNSET
        else:
            estate_name_sc = self.estate_name_sc

        district_name_en: None | str | Unset
        if isinstance(self.district_name_en, Unset):
            district_name_en = UNSET
        else:
            district_name_en = self.district_name_en

        district_name_tc: None | str | Unset
        if isinstance(self.district_name_tc, Unset):
            district_name_tc = UNSET
        else:
            district_name_tc = self.district_name_tc

        district_name_sc: None | str | Unset
        if isinstance(self.district_name_sc, Unset):
            district_name_sc = UNSET
        else:
            district_name_sc = self.district_name_sc

        region_name_en: None | str | Unset
        if isinstance(self.region_name_en, Unset):
            region_name_en = UNSET
        else:
            region_name_en = self.region_name_en

        region_name_tc: None | str | Unset
        if isinstance(self.region_name_tc, Unset):
            region_name_tc = UNSET
        else:
            region_name_tc = self.region_name_tc

        region_name_sc: None | str | Unset
        if isinstance(self.region_name_sc, Unset):
            region_name_sc = UNSET
        else:
            region_name_sc = self.region_name_sc

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

        year_of_completion_en: None | str | Unset
        if isinstance(self.year_of_completion_en, Unset):
            year_of_completion_en = UNSET
        else:
            year_of_completion_en = self.year_of_completion_en

        year_of_completion_tc: None | str | Unset
        if isinstance(self.year_of_completion_tc, Unset):
            year_of_completion_tc = UNSET
        else:
            year_of_completion_tc = self.year_of_completion_tc

        year_of_completion_sc: None | str | Unset
        if isinstance(self.year_of_completion_sc, Unset):
            year_of_completion_sc = UNSET
        else:
            year_of_completion_sc = self.year_of_completion_sc

        no_of_floors_en: None | str | Unset
        if isinstance(self.no_of_floors_en, Unset):
            no_of_floors_en = UNSET
        else:
            no_of_floors_en = self.no_of_floors_en

        no_of_floors_tc: None | str | Unset
        if isinstance(self.no_of_floors_tc, Unset):
            no_of_floors_tc = UNSET
        else:
            no_of_floors_tc = self.no_of_floors_tc

        no_of_floors_sc: None | str | Unset
        if isinstance(self.no_of_floors_sc, Unset):
            no_of_floors_sc = UNSET
        else:
            no_of_floors_sc = self.no_of_floors_sc

        total_lettable_area_m2_en: None | str | Unset
        if isinstance(self.total_lettable_area_m2_en, Unset):
            total_lettable_area_m2_en = UNSET
        else:
            total_lettable_area_m2_en = self.total_lettable_area_m2_en

        total_lettable_area_m2_tc: None | str | Unset
        if isinstance(self.total_lettable_area_m2_tc, Unset):
            total_lettable_area_m2_tc = UNSET
        else:
            total_lettable_area_m2_tc = self.total_lettable_area_m2_tc

        total_lettable_area_m2_sc: None | str | Unset
        if isinstance(self.total_lettable_area_m2_sc, Unset):
            total_lettable_area_m2_sc = UNSET
        else:
            total_lettable_area_m2_sc = self.total_lettable_area_m2_sc

        property_management_en: None | str | Unset
        if isinstance(self.property_management_en, Unset):
            property_management_en = UNSET
        else:
            property_management_en = self.property_management_en

        property_management_tc: None | str | Unset
        if isinstance(self.property_management_tc, Unset):
            property_management_tc = UNSET
        else:
            property_management_tc = self.property_management_tc

        property_management_sc: None | str | Unset
        if isinstance(self.property_management_sc, Unset):
            property_management_sc = UNSET
        else:
            property_management_sc = self.property_management_sc

        carpark_management_en: None | str | Unset
        if isinstance(self.carpark_management_en, Unset):
            carpark_management_en = UNSET
        else:
            carpark_management_en = self.carpark_management_en

        carpark_management_tc: None | str | Unset
        if isinstance(self.carpark_management_tc, Unset):
            carpark_management_tc = UNSET
        else:
            carpark_management_tc = self.carpark_management_tc

        carpark_management_sc: None | str | Unset
        if isinstance(self.carpark_management_sc, Unset):
            carpark_management_sc = UNSET
        else:
            carpark_management_sc = self.carpark_management_sc

        shopping_centre_website: None | str | Unset
        if isinstance(self.shopping_centre_website, Unset):
            shopping_centre_website = UNSET
        else:
            shopping_centre_website = self.shopping_centre_website

        further_information_en: None | str | Unset
        if isinstance(self.further_information_en, Unset):
            further_information_en = UNSET
        else:
            further_information_en = self.further_information_en

        further_information_tc: None | str | Unset
        if isinstance(self.further_information_tc, Unset):
            further_information_tc = UNSET
        else:
            further_information_tc = self.further_information_tc

        further_information_sc: None | str | Unset
        if isinstance(self.further_information_sc, Unset):
            further_information_sc = UNSET
        else:
            further_information_sc = self.further_information_sc

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if estate_name_en is not UNSET:
            field_dict["estate_name_en"] = estate_name_en
        if estate_name_tc is not UNSET:
            field_dict["estate_name_tc"] = estate_name_tc
        if estate_name_sc is not UNSET:
            field_dict["estate_name_sc"] = estate_name_sc
        if district_name_en is not UNSET:
            field_dict["district_name_en"] = district_name_en
        if district_name_tc is not UNSET:
            field_dict["district_name_tc"] = district_name_tc
        if district_name_sc is not UNSET:
            field_dict["district_name_sc"] = district_name_sc
        if region_name_en is not UNSET:
            field_dict["region_name_en"] = region_name_en
        if region_name_tc is not UNSET:
            field_dict["region_name_tc"] = region_name_tc
        if region_name_sc is not UNSET:
            field_dict["region_name_sc"] = region_name_sc
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if year_of_completion_en is not UNSET:
            field_dict["year_of_completion_en"] = year_of_completion_en
        if year_of_completion_tc is not UNSET:
            field_dict["year_of_completion_tc"] = year_of_completion_tc
        if year_of_completion_sc is not UNSET:
            field_dict["year_of_completion_sc"] = year_of_completion_sc
        if no_of_floors_en is not UNSET:
            field_dict["no_of_floors_en"] = no_of_floors_en
        if no_of_floors_tc is not UNSET:
            field_dict["no_of_floors_tc"] = no_of_floors_tc
        if no_of_floors_sc is not UNSET:
            field_dict["no_of_floors_sc"] = no_of_floors_sc
        if total_lettable_area_m2_en is not UNSET:
            field_dict["total_lettable_area_m2_en"] = total_lettable_area_m2_en
        if total_lettable_area_m2_tc is not UNSET:
            field_dict["total_lettable_area_m2_tc"] = total_lettable_area_m2_tc
        if total_lettable_area_m2_sc is not UNSET:
            field_dict["total_lettable_area_m2_sc"] = total_lettable_area_m2_sc
        if property_management_en is not UNSET:
            field_dict["property_management_en"] = property_management_en
        if property_management_tc is not UNSET:
            field_dict["property_management_tc"] = property_management_tc
        if property_management_sc is not UNSET:
            field_dict["property_management_sc"] = property_management_sc
        if carpark_management_en is not UNSET:
            field_dict["carpark_management_en"] = carpark_management_en
        if carpark_management_tc is not UNSET:
            field_dict["carpark_management_tc"] = carpark_management_tc
        if carpark_management_sc is not UNSET:
            field_dict["carpark_management_sc"] = carpark_management_sc
        if shopping_centre_website is not UNSET:
            field_dict["shopping_centre_website"] = shopping_centre_website
        if further_information_en is not UNSET:
            field_dict["further_information_en"] = further_information_en
        if further_information_tc is not UNSET:
            field_dict["further_information_tc"] = further_information_tc
        if further_information_sc is not UNSET:
            field_dict["further_information_sc"] = further_information_sc

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("SHAPE", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_estate_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estate_name_en = _parse_estate_name_en(d.pop("estate_name_en", UNSET))

        def _parse_estate_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estate_name_tc = _parse_estate_name_tc(d.pop("estate_name_tc", UNSET))

        def _parse_estate_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        estate_name_sc = _parse_estate_name_sc(d.pop("estate_name_sc", UNSET))

        def _parse_district_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_name_en = _parse_district_name_en(d.pop("district_name_en", UNSET))

        def _parse_district_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_name_tc = _parse_district_name_tc(d.pop("district_name_tc", UNSET))

        def _parse_district_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_name_sc = _parse_district_name_sc(d.pop("district_name_sc", UNSET))

        def _parse_region_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name_en = _parse_region_name_en(d.pop("region_name_en", UNSET))

        def _parse_region_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name_tc = _parse_region_name_tc(d.pop("region_name_tc", UNSET))

        def _parse_region_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_name_sc = _parse_region_name_sc(d.pop("region_name_sc", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_year_of_completion_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_of_completion_en = _parse_year_of_completion_en(
            d.pop("year_of_completion_en", UNSET)
        )

        def _parse_year_of_completion_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_of_completion_tc = _parse_year_of_completion_tc(
            d.pop("year_of_completion_tc", UNSET)
        )

        def _parse_year_of_completion_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_of_completion_sc = _parse_year_of_completion_sc(
            d.pop("year_of_completion_sc", UNSET)
        )

        def _parse_no_of_floors_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_floors_en = _parse_no_of_floors_en(d.pop("no_of_floors_en", UNSET))

        def _parse_no_of_floors_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_floors_tc = _parse_no_of_floors_tc(d.pop("no_of_floors_tc", UNSET))

        def _parse_no_of_floors_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_floors_sc = _parse_no_of_floors_sc(d.pop("no_of_floors_sc", UNSET))

        def _parse_total_lettable_area_m2_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_lettable_area_m2_en = _parse_total_lettable_area_m2_en(
            d.pop("total_lettable_area_m2_en", UNSET)
        )

        def _parse_total_lettable_area_m2_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_lettable_area_m2_tc = _parse_total_lettable_area_m2_tc(
            d.pop("total_lettable_area_m2_tc", UNSET)
        )

        def _parse_total_lettable_area_m2_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_lettable_area_m2_sc = _parse_total_lettable_area_m2_sc(
            d.pop("total_lettable_area_m2_sc", UNSET)
        )

        def _parse_property_management_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_management_en = _parse_property_management_en(
            d.pop("property_management_en", UNSET)
        )

        def _parse_property_management_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_management_tc = _parse_property_management_tc(
            d.pop("property_management_tc", UNSET)
        )

        def _parse_property_management_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_management_sc = _parse_property_management_sc(
            d.pop("property_management_sc", UNSET)
        )

        def _parse_carpark_management_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carpark_management_en = _parse_carpark_management_en(
            d.pop("carpark_management_en", UNSET)
        )

        def _parse_carpark_management_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carpark_management_tc = _parse_carpark_management_tc(
            d.pop("carpark_management_tc", UNSET)
        )

        def _parse_carpark_management_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        carpark_management_sc = _parse_carpark_management_sc(
            d.pop("carpark_management_sc", UNSET)
        )

        def _parse_shopping_centre_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        shopping_centre_website = _parse_shopping_centre_website(
            d.pop("shopping_centre_website", UNSET)
        )

        def _parse_further_information_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        further_information_en = _parse_further_information_en(
            d.pop("further_information_en", UNSET)
        )

        def _parse_further_information_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        further_information_tc = _parse_further_information_tc(
            d.pop("further_information_tc", UNSET)
        )

        def _parse_further_information_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        further_information_sc = _parse_further_information_sc(
            d.pop("further_information_sc", UNSET)
        )

        wfs_map_server_wfs_commercial_properties_attributes = cls(
            shape=shape,
            objectid=objectid,
            estate_name_en=estate_name_en,
            estate_name_tc=estate_name_tc,
            estate_name_sc=estate_name_sc,
            district_name_en=district_name_en,
            district_name_tc=district_name_tc,
            district_name_sc=district_name_sc,
            region_name_en=region_name_en,
            region_name_tc=region_name_tc,
            region_name_sc=region_name_sc,
            latitude=latitude,
            longitude=longitude,
            year_of_completion_en=year_of_completion_en,
            year_of_completion_tc=year_of_completion_tc,
            year_of_completion_sc=year_of_completion_sc,
            no_of_floors_en=no_of_floors_en,
            no_of_floors_tc=no_of_floors_tc,
            no_of_floors_sc=no_of_floors_sc,
            total_lettable_area_m2_en=total_lettable_area_m2_en,
            total_lettable_area_m2_tc=total_lettable_area_m2_tc,
            total_lettable_area_m2_sc=total_lettable_area_m2_sc,
            property_management_en=property_management_en,
            property_management_tc=property_management_tc,
            property_management_sc=property_management_sc,
            carpark_management_en=carpark_management_en,
            carpark_management_tc=carpark_management_tc,
            carpark_management_sc=carpark_management_sc,
            shopping_centre_website=shopping_centre_website,
            further_information_en=further_information_en,
            further_information_tc=further_information_tc,
            further_information_sc=further_information_sc,
        )

        wfs_map_server_wfs_commercial_properties_attributes.additional_properties = d
        return wfs_map_server_wfs_commercial_properties_attributes

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
