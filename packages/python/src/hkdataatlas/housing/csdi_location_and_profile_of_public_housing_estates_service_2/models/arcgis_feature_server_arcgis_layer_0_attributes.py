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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        estate_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        estate_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        estate_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        region_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        region_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        region_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        sold_under_en (None | str | Unset): Publisher field type: esriFieldTypeString
        sold_under_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        sold_under_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        year_of_completion_en (None | str | Unset): Publisher field type: esriFieldTypeString
        year_of_completion_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        year_of_completion_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        types_of_blocks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        types_of_blocks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        types_of_blocks_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_blocks (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_blocks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_blocks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_blocks_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_flats_en (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_flats_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_flats_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        gross_floor_area_m2 (None | str | Unset): Publisher field type: esriFieldTypeString
        saleable_area_m2 (None | str | Unset): Publisher field type: esriFieldTypeString
        initial_sale_price (None | str | Unset): Publisher field type: esriFieldTypeString
        owners_corporation_en (None | str | Unset): Publisher field type: esriFieldTypeString
        owners_corporation_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        owners_corporation_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        management_office_en (None | str | Unset): Publisher field type: esriFieldTypeString
        management_office_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        management_office_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        property_management_en (None | str | Unset): Publisher field type: esriFieldTypeString
        property_management_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        property_management_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        carpark_management_en (None | str | Unset): Publisher field type: esriFieldTypeString
        carpark_management_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        carpark_management_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        court_website (None | str | Unset): Publisher field type: esriFieldTypeString
        further_information_en (None | str | Unset): Publisher field type: esriFieldTypeString
        further_information_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        further_information_sc (None | str | Unset): Publisher field type: esriFieldTypeString
    """

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
    sold_under_en: None | str | Unset = UNSET
    sold_under_tc: None | str | Unset = UNSET
    sold_under_sc: None | str | Unset = UNSET
    year_of_completion_en: None | str | Unset = UNSET
    year_of_completion_tc: None | str | Unset = UNSET
    year_of_completion_sc: None | str | Unset = UNSET
    types_of_blocks_en: None | str | Unset = UNSET
    types_of_blocks_tc: None | str | Unset = UNSET
    types_of_blocks_sc: None | str | Unset = UNSET
    no_of_blocks: None | str | Unset = UNSET
    name_of_blocks_en: None | str | Unset = UNSET
    name_of_blocks_tc: None | str | Unset = UNSET
    name_of_blocks_sc: None | str | Unset = UNSET
    no_of_flats_en: None | str | Unset = UNSET
    no_of_flats_tc: None | str | Unset = UNSET
    no_of_flats_sc: None | str | Unset = UNSET
    gross_floor_area_m2: None | str | Unset = UNSET
    saleable_area_m2: None | str | Unset = UNSET
    initial_sale_price: None | str | Unset = UNSET
    owners_corporation_en: None | str | Unset = UNSET
    owners_corporation_tc: None | str | Unset = UNSET
    owners_corporation_sc: None | str | Unset = UNSET
    management_office_en: None | str | Unset = UNSET
    management_office_tc: None | str | Unset = UNSET
    management_office_sc: None | str | Unset = UNSET
    property_management_en: None | str | Unset = UNSET
    property_management_tc: None | str | Unset = UNSET
    property_management_sc: None | str | Unset = UNSET
    carpark_management_en: None | str | Unset = UNSET
    carpark_management_tc: None | str | Unset = UNSET
    carpark_management_sc: None | str | Unset = UNSET
    court_website: None | str | Unset = UNSET
    further_information_en: None | str | Unset = UNSET
    further_information_tc: None | str | Unset = UNSET
    further_information_sc: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        sold_under_en: None | str | Unset
        if isinstance(self.sold_under_en, Unset):
            sold_under_en = UNSET
        else:
            sold_under_en = self.sold_under_en

        sold_under_tc: None | str | Unset
        if isinstance(self.sold_under_tc, Unset):
            sold_under_tc = UNSET
        else:
            sold_under_tc = self.sold_under_tc

        sold_under_sc: None | str | Unset
        if isinstance(self.sold_under_sc, Unset):
            sold_under_sc = UNSET
        else:
            sold_under_sc = self.sold_under_sc

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

        types_of_blocks_en: None | str | Unset
        if isinstance(self.types_of_blocks_en, Unset):
            types_of_blocks_en = UNSET
        else:
            types_of_blocks_en = self.types_of_blocks_en

        types_of_blocks_tc: None | str | Unset
        if isinstance(self.types_of_blocks_tc, Unset):
            types_of_blocks_tc = UNSET
        else:
            types_of_blocks_tc = self.types_of_blocks_tc

        types_of_blocks_sc: None | str | Unset
        if isinstance(self.types_of_blocks_sc, Unset):
            types_of_blocks_sc = UNSET
        else:
            types_of_blocks_sc = self.types_of_blocks_sc

        no_of_blocks: None | str | Unset
        if isinstance(self.no_of_blocks, Unset):
            no_of_blocks = UNSET
        else:
            no_of_blocks = self.no_of_blocks

        name_of_blocks_en: None | str | Unset
        if isinstance(self.name_of_blocks_en, Unset):
            name_of_blocks_en = UNSET
        else:
            name_of_blocks_en = self.name_of_blocks_en

        name_of_blocks_tc: None | str | Unset
        if isinstance(self.name_of_blocks_tc, Unset):
            name_of_blocks_tc = UNSET
        else:
            name_of_blocks_tc = self.name_of_blocks_tc

        name_of_blocks_sc: None | str | Unset
        if isinstance(self.name_of_blocks_sc, Unset):
            name_of_blocks_sc = UNSET
        else:
            name_of_blocks_sc = self.name_of_blocks_sc

        no_of_flats_en: None | str | Unset
        if isinstance(self.no_of_flats_en, Unset):
            no_of_flats_en = UNSET
        else:
            no_of_flats_en = self.no_of_flats_en

        no_of_flats_tc: None | str | Unset
        if isinstance(self.no_of_flats_tc, Unset):
            no_of_flats_tc = UNSET
        else:
            no_of_flats_tc = self.no_of_flats_tc

        no_of_flats_sc: None | str | Unset
        if isinstance(self.no_of_flats_sc, Unset):
            no_of_flats_sc = UNSET
        else:
            no_of_flats_sc = self.no_of_flats_sc

        gross_floor_area_m2: None | str | Unset
        if isinstance(self.gross_floor_area_m2, Unset):
            gross_floor_area_m2 = UNSET
        else:
            gross_floor_area_m2 = self.gross_floor_area_m2

        saleable_area_m2: None | str | Unset
        if isinstance(self.saleable_area_m2, Unset):
            saleable_area_m2 = UNSET
        else:
            saleable_area_m2 = self.saleable_area_m2

        initial_sale_price: None | str | Unset
        if isinstance(self.initial_sale_price, Unset):
            initial_sale_price = UNSET
        else:
            initial_sale_price = self.initial_sale_price

        owners_corporation_en: None | str | Unset
        if isinstance(self.owners_corporation_en, Unset):
            owners_corporation_en = UNSET
        else:
            owners_corporation_en = self.owners_corporation_en

        owners_corporation_tc: None | str | Unset
        if isinstance(self.owners_corporation_tc, Unset):
            owners_corporation_tc = UNSET
        else:
            owners_corporation_tc = self.owners_corporation_tc

        owners_corporation_sc: None | str | Unset
        if isinstance(self.owners_corporation_sc, Unset):
            owners_corporation_sc = UNSET
        else:
            owners_corporation_sc = self.owners_corporation_sc

        management_office_en: None | str | Unset
        if isinstance(self.management_office_en, Unset):
            management_office_en = UNSET
        else:
            management_office_en = self.management_office_en

        management_office_tc: None | str | Unset
        if isinstance(self.management_office_tc, Unset):
            management_office_tc = UNSET
        else:
            management_office_tc = self.management_office_tc

        management_office_sc: None | str | Unset
        if isinstance(self.management_office_sc, Unset):
            management_office_sc = UNSET
        else:
            management_office_sc = self.management_office_sc

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

        court_website: None | str | Unset
        if isinstance(self.court_website, Unset):
            court_website = UNSET
        else:
            court_website = self.court_website

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
        if sold_under_en is not UNSET:
            field_dict["sold_under_en"] = sold_under_en
        if sold_under_tc is not UNSET:
            field_dict["sold_under_tc"] = sold_under_tc
        if sold_under_sc is not UNSET:
            field_dict["sold_under_sc"] = sold_under_sc
        if year_of_completion_en is not UNSET:
            field_dict["year_of_completion_en"] = year_of_completion_en
        if year_of_completion_tc is not UNSET:
            field_dict["year_of_completion_tc"] = year_of_completion_tc
        if year_of_completion_sc is not UNSET:
            field_dict["year_of_completion_sc"] = year_of_completion_sc
        if types_of_blocks_en is not UNSET:
            field_dict["types_of_blocks_en"] = types_of_blocks_en
        if types_of_blocks_tc is not UNSET:
            field_dict["types_of_blocks_tc"] = types_of_blocks_tc
        if types_of_blocks_sc is not UNSET:
            field_dict["types_of_blocks_sc"] = types_of_blocks_sc
        if no_of_blocks is not UNSET:
            field_dict["no_of_blocks"] = no_of_blocks
        if name_of_blocks_en is not UNSET:
            field_dict["name_of_blocks_en"] = name_of_blocks_en
        if name_of_blocks_tc is not UNSET:
            field_dict["name_of_blocks_tc"] = name_of_blocks_tc
        if name_of_blocks_sc is not UNSET:
            field_dict["name_of_blocks_sc"] = name_of_blocks_sc
        if no_of_flats_en is not UNSET:
            field_dict["no_of_flats_en"] = no_of_flats_en
        if no_of_flats_tc is not UNSET:
            field_dict["no_of_flats_tc"] = no_of_flats_tc
        if no_of_flats_sc is not UNSET:
            field_dict["no_of_flats_sc"] = no_of_flats_sc
        if gross_floor_area_m2 is not UNSET:
            field_dict["gross_floor_area_m2"] = gross_floor_area_m2
        if saleable_area_m2 is not UNSET:
            field_dict["saleable_area_m2"] = saleable_area_m2
        if initial_sale_price is not UNSET:
            field_dict["initial_sale_price"] = initial_sale_price
        if owners_corporation_en is not UNSET:
            field_dict["owners_corporation_en"] = owners_corporation_en
        if owners_corporation_tc is not UNSET:
            field_dict["owners_corporation_tc"] = owners_corporation_tc
        if owners_corporation_sc is not UNSET:
            field_dict["owners_corporation_sc"] = owners_corporation_sc
        if management_office_en is not UNSET:
            field_dict["management_office_en"] = management_office_en
        if management_office_tc is not UNSET:
            field_dict["management_office_tc"] = management_office_tc
        if management_office_sc is not UNSET:
            field_dict["management_office_sc"] = management_office_sc
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
        if court_website is not UNSET:
            field_dict["court_website"] = court_website
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

        def _parse_sold_under_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sold_under_en = _parse_sold_under_en(d.pop("sold_under_en", UNSET))

        def _parse_sold_under_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sold_under_tc = _parse_sold_under_tc(d.pop("sold_under_tc", UNSET))

        def _parse_sold_under_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sold_under_sc = _parse_sold_under_sc(d.pop("sold_under_sc", UNSET))

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

        def _parse_types_of_blocks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_blocks_en = _parse_types_of_blocks_en(
            d.pop("types_of_blocks_en", UNSET)
        )

        def _parse_types_of_blocks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_blocks_tc = _parse_types_of_blocks_tc(
            d.pop("types_of_blocks_tc", UNSET)
        )

        def _parse_types_of_blocks_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        types_of_blocks_sc = _parse_types_of_blocks_sc(
            d.pop("types_of_blocks_sc", UNSET)
        )

        def _parse_no_of_blocks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_blocks = _parse_no_of_blocks(d.pop("no_of_blocks", UNSET))

        def _parse_name_of_blocks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_blocks_en = _parse_name_of_blocks_en(d.pop("name_of_blocks_en", UNSET))

        def _parse_name_of_blocks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_blocks_tc = _parse_name_of_blocks_tc(d.pop("name_of_blocks_tc", UNSET))

        def _parse_name_of_blocks_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_blocks_sc = _parse_name_of_blocks_sc(d.pop("name_of_blocks_sc", UNSET))

        def _parse_no_of_flats_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_flats_en = _parse_no_of_flats_en(d.pop("no_of_flats_en", UNSET))

        def _parse_no_of_flats_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_flats_tc = _parse_no_of_flats_tc(d.pop("no_of_flats_tc", UNSET))

        def _parse_no_of_flats_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_flats_sc = _parse_no_of_flats_sc(d.pop("no_of_flats_sc", UNSET))

        def _parse_gross_floor_area_m2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gross_floor_area_m2 = _parse_gross_floor_area_m2(
            d.pop("gross_floor_area_m2", UNSET)
        )

        def _parse_saleable_area_m2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saleable_area_m2 = _parse_saleable_area_m2(d.pop("saleable_area_m2", UNSET))

        def _parse_initial_sale_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initial_sale_price = _parse_initial_sale_price(
            d.pop("initial_sale_price", UNSET)
        )

        def _parse_owners_corporation_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owners_corporation_en = _parse_owners_corporation_en(
            d.pop("owners_corporation_en", UNSET)
        )

        def _parse_owners_corporation_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owners_corporation_tc = _parse_owners_corporation_tc(
            d.pop("owners_corporation_tc", UNSET)
        )

        def _parse_owners_corporation_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        owners_corporation_sc = _parse_owners_corporation_sc(
            d.pop("owners_corporation_sc", UNSET)
        )

        def _parse_management_office_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        management_office_en = _parse_management_office_en(
            d.pop("management_office_en", UNSET)
        )

        def _parse_management_office_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        management_office_tc = _parse_management_office_tc(
            d.pop("management_office_tc", UNSET)
        )

        def _parse_management_office_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        management_office_sc = _parse_management_office_sc(
            d.pop("management_office_sc", UNSET)
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

        def _parse_court_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        court_website = _parse_court_website(d.pop("court_website", UNSET))

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

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
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
            sold_under_en=sold_under_en,
            sold_under_tc=sold_under_tc,
            sold_under_sc=sold_under_sc,
            year_of_completion_en=year_of_completion_en,
            year_of_completion_tc=year_of_completion_tc,
            year_of_completion_sc=year_of_completion_sc,
            types_of_blocks_en=types_of_blocks_en,
            types_of_blocks_tc=types_of_blocks_tc,
            types_of_blocks_sc=types_of_blocks_sc,
            no_of_blocks=no_of_blocks,
            name_of_blocks_en=name_of_blocks_en,
            name_of_blocks_tc=name_of_blocks_tc,
            name_of_blocks_sc=name_of_blocks_sc,
            no_of_flats_en=no_of_flats_en,
            no_of_flats_tc=no_of_flats_tc,
            no_of_flats_sc=no_of_flats_sc,
            gross_floor_area_m2=gross_floor_area_m2,
            saleable_area_m2=saleable_area_m2,
            initial_sale_price=initial_sale_price,
            owners_corporation_en=owners_corporation_en,
            owners_corporation_tc=owners_corporation_tc,
            owners_corporation_sc=owners_corporation_sc,
            management_office_en=management_office_en,
            management_office_tc=management_office_tc,
            management_office_sc=management_office_sc,
            property_management_en=property_management_en,
            property_management_tc=property_management_tc,
            property_management_sc=property_management_sc,
            carpark_management_en=carpark_management_en,
            carpark_management_tc=carpark_management_tc,
            carpark_management_sc=carpark_management_sc,
            court_website=court_website,
            further_information_en=further_information_en,
            further_information_tc=further_information_tc,
            further_information_sc=further_information_sc,
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
