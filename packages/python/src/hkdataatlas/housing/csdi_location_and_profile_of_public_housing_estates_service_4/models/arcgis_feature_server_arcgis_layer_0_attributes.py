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
        type_of_estate_en (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_estate_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_estate_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        year_of_intake_en (None | str | Unset): Publisher field type: esriFieldTypeString
        year_of_intake_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        year_of_intake_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_blocks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_blocks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_blocks_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_blocks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_blocks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_blocks_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_units_en (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_units_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        no_of_units_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        storey_en (None | str | Unset): Publisher field type: esriFieldTypeString
        storey_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        storey_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        factory_estate_office_en (None | str | Unset): Publisher field type: esriFieldTypeString
        factory_estate_office_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        factory_estate_office_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        property_management_en (None | str | Unset): Publisher field type: esriFieldTypeString
        property_management_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        property_management_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        carpark_management_en (None | str | Unset): Publisher field type: esriFieldTypeString
        carpark_management_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        carpark_management_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        flatted_factories_website (None | str | Unset): Publisher field type: esriFieldTypeString
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
    type_of_estate_en: None | str | Unset = UNSET
    type_of_estate_tc: None | str | Unset = UNSET
    type_of_estate_sc: None | str | Unset = UNSET
    year_of_intake_en: None | str | Unset = UNSET
    year_of_intake_tc: None | str | Unset = UNSET
    year_of_intake_sc: None | str | Unset = UNSET
    no_of_blocks_en: None | str | Unset = UNSET
    no_of_blocks_tc: None | str | Unset = UNSET
    no_of_blocks_sc: None | str | Unset = UNSET
    name_of_blocks_en: None | str | Unset = UNSET
    name_of_blocks_tc: None | str | Unset = UNSET
    name_of_blocks_sc: None | str | Unset = UNSET
    no_of_units_en: None | str | Unset = UNSET
    no_of_units_tc: None | str | Unset = UNSET
    no_of_units_sc: None | str | Unset = UNSET
    storey_en: None | str | Unset = UNSET
    storey_tc: None | str | Unset = UNSET
    storey_sc: None | str | Unset = UNSET
    factory_estate_office_en: None | str | Unset = UNSET
    factory_estate_office_tc: None | str | Unset = UNSET
    factory_estate_office_sc: None | str | Unset = UNSET
    property_management_en: None | str | Unset = UNSET
    property_management_tc: None | str | Unset = UNSET
    property_management_sc: None | str | Unset = UNSET
    carpark_management_en: None | str | Unset = UNSET
    carpark_management_tc: None | str | Unset = UNSET
    carpark_management_sc: None | str | Unset = UNSET
    flatted_factories_website: None | str | Unset = UNSET
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

        type_of_estate_en: None | str | Unset
        if isinstance(self.type_of_estate_en, Unset):
            type_of_estate_en = UNSET
        else:
            type_of_estate_en = self.type_of_estate_en

        type_of_estate_tc: None | str | Unset
        if isinstance(self.type_of_estate_tc, Unset):
            type_of_estate_tc = UNSET
        else:
            type_of_estate_tc = self.type_of_estate_tc

        type_of_estate_sc: None | str | Unset
        if isinstance(self.type_of_estate_sc, Unset):
            type_of_estate_sc = UNSET
        else:
            type_of_estate_sc = self.type_of_estate_sc

        year_of_intake_en: None | str | Unset
        if isinstance(self.year_of_intake_en, Unset):
            year_of_intake_en = UNSET
        else:
            year_of_intake_en = self.year_of_intake_en

        year_of_intake_tc: None | str | Unset
        if isinstance(self.year_of_intake_tc, Unset):
            year_of_intake_tc = UNSET
        else:
            year_of_intake_tc = self.year_of_intake_tc

        year_of_intake_sc: None | str | Unset
        if isinstance(self.year_of_intake_sc, Unset):
            year_of_intake_sc = UNSET
        else:
            year_of_intake_sc = self.year_of_intake_sc

        no_of_blocks_en: None | str | Unset
        if isinstance(self.no_of_blocks_en, Unset):
            no_of_blocks_en = UNSET
        else:
            no_of_blocks_en = self.no_of_blocks_en

        no_of_blocks_tc: None | str | Unset
        if isinstance(self.no_of_blocks_tc, Unset):
            no_of_blocks_tc = UNSET
        else:
            no_of_blocks_tc = self.no_of_blocks_tc

        no_of_blocks_sc: None | str | Unset
        if isinstance(self.no_of_blocks_sc, Unset):
            no_of_blocks_sc = UNSET
        else:
            no_of_blocks_sc = self.no_of_blocks_sc

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

        no_of_units_en: None | str | Unset
        if isinstance(self.no_of_units_en, Unset):
            no_of_units_en = UNSET
        else:
            no_of_units_en = self.no_of_units_en

        no_of_units_tc: None | str | Unset
        if isinstance(self.no_of_units_tc, Unset):
            no_of_units_tc = UNSET
        else:
            no_of_units_tc = self.no_of_units_tc

        no_of_units_sc: None | str | Unset
        if isinstance(self.no_of_units_sc, Unset):
            no_of_units_sc = UNSET
        else:
            no_of_units_sc = self.no_of_units_sc

        storey_en: None | str | Unset
        if isinstance(self.storey_en, Unset):
            storey_en = UNSET
        else:
            storey_en = self.storey_en

        storey_tc: None | str | Unset
        if isinstance(self.storey_tc, Unset):
            storey_tc = UNSET
        else:
            storey_tc = self.storey_tc

        storey_sc: None | str | Unset
        if isinstance(self.storey_sc, Unset):
            storey_sc = UNSET
        else:
            storey_sc = self.storey_sc

        factory_estate_office_en: None | str | Unset
        if isinstance(self.factory_estate_office_en, Unset):
            factory_estate_office_en = UNSET
        else:
            factory_estate_office_en = self.factory_estate_office_en

        factory_estate_office_tc: None | str | Unset
        if isinstance(self.factory_estate_office_tc, Unset):
            factory_estate_office_tc = UNSET
        else:
            factory_estate_office_tc = self.factory_estate_office_tc

        factory_estate_office_sc: None | str | Unset
        if isinstance(self.factory_estate_office_sc, Unset):
            factory_estate_office_sc = UNSET
        else:
            factory_estate_office_sc = self.factory_estate_office_sc

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

        flatted_factories_website: None | str | Unset
        if isinstance(self.flatted_factories_website, Unset):
            flatted_factories_website = UNSET
        else:
            flatted_factories_website = self.flatted_factories_website

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
        if type_of_estate_en is not UNSET:
            field_dict["type_of_estate_en"] = type_of_estate_en
        if type_of_estate_tc is not UNSET:
            field_dict["type_of_estate_tc"] = type_of_estate_tc
        if type_of_estate_sc is not UNSET:
            field_dict["type_of_estate_sc"] = type_of_estate_sc
        if year_of_intake_en is not UNSET:
            field_dict["year_of_intake_en"] = year_of_intake_en
        if year_of_intake_tc is not UNSET:
            field_dict["year_of_intake_tc"] = year_of_intake_tc
        if year_of_intake_sc is not UNSET:
            field_dict["year_of_intake_sc"] = year_of_intake_sc
        if no_of_blocks_en is not UNSET:
            field_dict["no_of_blocks_en"] = no_of_blocks_en
        if no_of_blocks_tc is not UNSET:
            field_dict["no_of_blocks_tc"] = no_of_blocks_tc
        if no_of_blocks_sc is not UNSET:
            field_dict["no_of_blocks_sc"] = no_of_blocks_sc
        if name_of_blocks_en is not UNSET:
            field_dict["name_of_blocks_en"] = name_of_blocks_en
        if name_of_blocks_tc is not UNSET:
            field_dict["name_of_blocks_tc"] = name_of_blocks_tc
        if name_of_blocks_sc is not UNSET:
            field_dict["name_of_blocks_sc"] = name_of_blocks_sc
        if no_of_units_en is not UNSET:
            field_dict["no_of_units_en"] = no_of_units_en
        if no_of_units_tc is not UNSET:
            field_dict["no_of_units_tc"] = no_of_units_tc
        if no_of_units_sc is not UNSET:
            field_dict["no_of_units_sc"] = no_of_units_sc
        if storey_en is not UNSET:
            field_dict["storey_en"] = storey_en
        if storey_tc is not UNSET:
            field_dict["storey_tc"] = storey_tc
        if storey_sc is not UNSET:
            field_dict["storey_sc"] = storey_sc
        if factory_estate_office_en is not UNSET:
            field_dict["factory_estate_office_en"] = factory_estate_office_en
        if factory_estate_office_tc is not UNSET:
            field_dict["factory_estate_office_tc"] = factory_estate_office_tc
        if factory_estate_office_sc is not UNSET:
            field_dict["factory_estate_office_sc"] = factory_estate_office_sc
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
        if flatted_factories_website is not UNSET:
            field_dict["flatted_factories_website"] = flatted_factories_website
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

        def _parse_type_of_estate_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_estate_en = _parse_type_of_estate_en(d.pop("type_of_estate_en", UNSET))

        def _parse_type_of_estate_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_estate_tc = _parse_type_of_estate_tc(d.pop("type_of_estate_tc", UNSET))

        def _parse_type_of_estate_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_estate_sc = _parse_type_of_estate_sc(d.pop("type_of_estate_sc", UNSET))

        def _parse_year_of_intake_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_of_intake_en = _parse_year_of_intake_en(d.pop("year_of_intake_en", UNSET))

        def _parse_year_of_intake_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_of_intake_tc = _parse_year_of_intake_tc(d.pop("year_of_intake_tc", UNSET))

        def _parse_year_of_intake_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_of_intake_sc = _parse_year_of_intake_sc(d.pop("year_of_intake_sc", UNSET))

        def _parse_no_of_blocks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_blocks_en = _parse_no_of_blocks_en(d.pop("no_of_blocks_en", UNSET))

        def _parse_no_of_blocks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_blocks_tc = _parse_no_of_blocks_tc(d.pop("no_of_blocks_tc", UNSET))

        def _parse_no_of_blocks_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_blocks_sc = _parse_no_of_blocks_sc(d.pop("no_of_blocks_sc", UNSET))

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

        def _parse_no_of_units_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_units_en = _parse_no_of_units_en(d.pop("no_of_units_en", UNSET))

        def _parse_no_of_units_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_units_tc = _parse_no_of_units_tc(d.pop("no_of_units_tc", UNSET))

        def _parse_no_of_units_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        no_of_units_sc = _parse_no_of_units_sc(d.pop("no_of_units_sc", UNSET))

        def _parse_storey_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storey_en = _parse_storey_en(d.pop("storey_en", UNSET))

        def _parse_storey_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storey_tc = _parse_storey_tc(d.pop("storey_tc", UNSET))

        def _parse_storey_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storey_sc = _parse_storey_sc(d.pop("storey_sc", UNSET))

        def _parse_factory_estate_office_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        factory_estate_office_en = _parse_factory_estate_office_en(
            d.pop("factory_estate_office_en", UNSET)
        )

        def _parse_factory_estate_office_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        factory_estate_office_tc = _parse_factory_estate_office_tc(
            d.pop("factory_estate_office_tc", UNSET)
        )

        def _parse_factory_estate_office_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        factory_estate_office_sc = _parse_factory_estate_office_sc(
            d.pop("factory_estate_office_sc", UNSET)
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

        def _parse_flatted_factories_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        flatted_factories_website = _parse_flatted_factories_website(
            d.pop("flatted_factories_website", UNSET)
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
            type_of_estate_en=type_of_estate_en,
            type_of_estate_tc=type_of_estate_tc,
            type_of_estate_sc=type_of_estate_sc,
            year_of_intake_en=year_of_intake_en,
            year_of_intake_tc=year_of_intake_tc,
            year_of_intake_sc=year_of_intake_sc,
            no_of_blocks_en=no_of_blocks_en,
            no_of_blocks_tc=no_of_blocks_tc,
            no_of_blocks_sc=no_of_blocks_sc,
            name_of_blocks_en=name_of_blocks_en,
            name_of_blocks_tc=name_of_blocks_tc,
            name_of_blocks_sc=name_of_blocks_sc,
            no_of_units_en=no_of_units_en,
            no_of_units_tc=no_of_units_tc,
            no_of_units_sc=no_of_units_sc,
            storey_en=storey_en,
            storey_tc=storey_tc,
            storey_sc=storey_sc,
            factory_estate_office_en=factory_estate_office_en,
            factory_estate_office_tc=factory_estate_office_tc,
            factory_estate_office_sc=factory_estate_office_sc,
            property_management_en=property_management_en,
            property_management_tc=property_management_tc,
            property_management_sc=property_management_sc,
            carpark_management_en=carpark_management_en,
            carpark_management_tc=carpark_management_tc,
            carpark_management_sc=carpark_management_sc,
            flatted_factories_website=flatted_factories_website,
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
