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
        name_of_building_or_facility_en (None | str | Unset): Publisher field type: esriFieldTypeString
        street_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        region_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_en (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_water_dispenser_en (None | str | Unset): Publisher field type: esriFieldTypeString
        number_of_water_dispenser (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hours_from (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hours_to (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hours_exception_en (None | str | Unset): Publisher field type: esriFieldTypeString
        water_temperature_en (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_outdoor_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_building_or_facility_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        street_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        region_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_water_dispenser_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hours_exception_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        water_temperature_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_outdoor_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_of_building_or_facility_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        street_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        region_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        type_of_water_dispenser_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hours_exception_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        water_temperature_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        indoor_outdoor_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    name_of_building_or_facility_en: None | str | Unset = UNSET
    street_en: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    region_en: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    type_of_water_dispenser_en: None | str | Unset = UNSET
    number_of_water_dispenser: None | str | Unset = UNSET
    service_hours_from: None | str | Unset = UNSET
    service_hours_to: None | str | Unset = UNSET
    service_hours_exception_en: None | str | Unset = UNSET
    water_temperature_en: None | str | Unset = UNSET
    indoor_outdoor_en: None | str | Unset = UNSET
    remarks_en: None | str | Unset = UNSET
    name_of_building_or_facility_tc: None | str | Unset = UNSET
    street_tc: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    region_tc: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    type_of_water_dispenser_tc: None | str | Unset = UNSET
    service_hours_exception_tc: None | str | Unset = UNSET
    water_temperature_tc: None | str | Unset = UNSET
    indoor_outdoor_tc: None | str | Unset = UNSET
    remarks_tc: None | str | Unset = UNSET
    name_of_building_or_facility_sc: None | str | Unset = UNSET
    street_sc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    region_sc: None | str | Unset = UNSET
    location_sc: None | str | Unset = UNSET
    type_of_water_dispenser_sc: None | str | Unset = UNSET
    service_hours_exception_sc: None | str | Unset = UNSET
    water_temperature_sc: None | str | Unset = UNSET
    indoor_outdoor_sc: None | str | Unset = UNSET
    remarks_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_of_building_or_facility_en: None | str | Unset
        if isinstance(self.name_of_building_or_facility_en, Unset):
            name_of_building_or_facility_en = UNSET
        else:
            name_of_building_or_facility_en = self.name_of_building_or_facility_en

        street_en: None | str | Unset
        if isinstance(self.street_en, Unset):
            street_en = UNSET
        else:
            street_en = self.street_en

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        region_en: None | str | Unset
        if isinstance(self.region_en, Unset):
            region_en = UNSET
        else:
            region_en = self.region_en

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        latitude: None | str | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: None | str | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        type_of_water_dispenser_en: None | str | Unset
        if isinstance(self.type_of_water_dispenser_en, Unset):
            type_of_water_dispenser_en = UNSET
        else:
            type_of_water_dispenser_en = self.type_of_water_dispenser_en

        number_of_water_dispenser: None | str | Unset
        if isinstance(self.number_of_water_dispenser, Unset):
            number_of_water_dispenser = UNSET
        else:
            number_of_water_dispenser = self.number_of_water_dispenser

        service_hours_from: None | str | Unset
        if isinstance(self.service_hours_from, Unset):
            service_hours_from = UNSET
        else:
            service_hours_from = self.service_hours_from

        service_hours_to: None | str | Unset
        if isinstance(self.service_hours_to, Unset):
            service_hours_to = UNSET
        else:
            service_hours_to = self.service_hours_to

        service_hours_exception_en: None | str | Unset
        if isinstance(self.service_hours_exception_en, Unset):
            service_hours_exception_en = UNSET
        else:
            service_hours_exception_en = self.service_hours_exception_en

        water_temperature_en: None | str | Unset
        if isinstance(self.water_temperature_en, Unset):
            water_temperature_en = UNSET
        else:
            water_temperature_en = self.water_temperature_en

        indoor_outdoor_en: None | str | Unset
        if isinstance(self.indoor_outdoor_en, Unset):
            indoor_outdoor_en = UNSET
        else:
            indoor_outdoor_en = self.indoor_outdoor_en

        remarks_en: None | str | Unset
        if isinstance(self.remarks_en, Unset):
            remarks_en = UNSET
        else:
            remarks_en = self.remarks_en

        name_of_building_or_facility_tc: None | str | Unset
        if isinstance(self.name_of_building_or_facility_tc, Unset):
            name_of_building_or_facility_tc = UNSET
        else:
            name_of_building_or_facility_tc = self.name_of_building_or_facility_tc

        street_tc: None | str | Unset
        if isinstance(self.street_tc, Unset):
            street_tc = UNSET
        else:
            street_tc = self.street_tc

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        region_tc: None | str | Unset
        if isinstance(self.region_tc, Unset):
            region_tc = UNSET
        else:
            region_tc = self.region_tc

        location_tc: None | str | Unset
        if isinstance(self.location_tc, Unset):
            location_tc = UNSET
        else:
            location_tc = self.location_tc

        type_of_water_dispenser_tc: None | str | Unset
        if isinstance(self.type_of_water_dispenser_tc, Unset):
            type_of_water_dispenser_tc = UNSET
        else:
            type_of_water_dispenser_tc = self.type_of_water_dispenser_tc

        service_hours_exception_tc: None | str | Unset
        if isinstance(self.service_hours_exception_tc, Unset):
            service_hours_exception_tc = UNSET
        else:
            service_hours_exception_tc = self.service_hours_exception_tc

        water_temperature_tc: None | str | Unset
        if isinstance(self.water_temperature_tc, Unset):
            water_temperature_tc = UNSET
        else:
            water_temperature_tc = self.water_temperature_tc

        indoor_outdoor_tc: None | str | Unset
        if isinstance(self.indoor_outdoor_tc, Unset):
            indoor_outdoor_tc = UNSET
        else:
            indoor_outdoor_tc = self.indoor_outdoor_tc

        remarks_tc: None | str | Unset
        if isinstance(self.remarks_tc, Unset):
            remarks_tc = UNSET
        else:
            remarks_tc = self.remarks_tc

        name_of_building_or_facility_sc: None | str | Unset
        if isinstance(self.name_of_building_or_facility_sc, Unset):
            name_of_building_or_facility_sc = UNSET
        else:
            name_of_building_or_facility_sc = self.name_of_building_or_facility_sc

        street_sc: None | str | Unset
        if isinstance(self.street_sc, Unset):
            street_sc = UNSET
        else:
            street_sc = self.street_sc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        region_sc: None | str | Unset
        if isinstance(self.region_sc, Unset):
            region_sc = UNSET
        else:
            region_sc = self.region_sc

        location_sc: None | str | Unset
        if isinstance(self.location_sc, Unset):
            location_sc = UNSET
        else:
            location_sc = self.location_sc

        type_of_water_dispenser_sc: None | str | Unset
        if isinstance(self.type_of_water_dispenser_sc, Unset):
            type_of_water_dispenser_sc = UNSET
        else:
            type_of_water_dispenser_sc = self.type_of_water_dispenser_sc

        service_hours_exception_sc: None | str | Unset
        if isinstance(self.service_hours_exception_sc, Unset):
            service_hours_exception_sc = UNSET
        else:
            service_hours_exception_sc = self.service_hours_exception_sc

        water_temperature_sc: None | str | Unset
        if isinstance(self.water_temperature_sc, Unset):
            water_temperature_sc = UNSET
        else:
            water_temperature_sc = self.water_temperature_sc

        indoor_outdoor_sc: None | str | Unset
        if isinstance(self.indoor_outdoor_sc, Unset):
            indoor_outdoor_sc = UNSET
        else:
            indoor_outdoor_sc = self.indoor_outdoor_sc

        remarks_sc: None | str | Unset
        if isinstance(self.remarks_sc, Unset):
            remarks_sc = UNSET
        else:
            remarks_sc = self.remarks_sc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_of_building_or_facility_en is not UNSET:
            field_dict["Name_of_Building_or_Facility_EN"] = (
                name_of_building_or_facility_en
            )
        if street_en is not UNSET:
            field_dict["Street_EN"] = street_en
        if district_en is not UNSET:
            field_dict["District_EN"] = district_en
        if region_en is not UNSET:
            field_dict["Region_EN"] = region_en
        if location_en is not UNSET:
            field_dict["Location_EN"] = location_en
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if type_of_water_dispenser_en is not UNSET:
            field_dict["Type_of_Water_Dispenser_EN"] = type_of_water_dispenser_en
        if number_of_water_dispenser is not UNSET:
            field_dict["Number_of_Water_Dispenser"] = number_of_water_dispenser
        if service_hours_from is not UNSET:
            field_dict["Service_Hours_From"] = service_hours_from
        if service_hours_to is not UNSET:
            field_dict["Service_Hours_To"] = service_hours_to
        if service_hours_exception_en is not UNSET:
            field_dict["Service_Hours_Exception_EN"] = service_hours_exception_en
        if water_temperature_en is not UNSET:
            field_dict["Water_Temperature_EN"] = water_temperature_en
        if indoor_outdoor_en is not UNSET:
            field_dict["Indoor_Outdoor_EN"] = indoor_outdoor_en
        if remarks_en is not UNSET:
            field_dict["Remarks_EN"] = remarks_en
        if name_of_building_or_facility_tc is not UNSET:
            field_dict["Name_of_Building_or_Facility_TC"] = (
                name_of_building_or_facility_tc
            )
        if street_tc is not UNSET:
            field_dict["Street_TC"] = street_tc
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if region_tc is not UNSET:
            field_dict["Region_TC"] = region_tc
        if location_tc is not UNSET:
            field_dict["Location_TC"] = location_tc
        if type_of_water_dispenser_tc is not UNSET:
            field_dict["Type_of_Water_Dispenser_TC"] = type_of_water_dispenser_tc
        if service_hours_exception_tc is not UNSET:
            field_dict["Service_Hours_Exception_TC"] = service_hours_exception_tc
        if water_temperature_tc is not UNSET:
            field_dict["Water_Temperature_TC"] = water_temperature_tc
        if indoor_outdoor_tc is not UNSET:
            field_dict["Indoor_Outdoor_TC"] = indoor_outdoor_tc
        if remarks_tc is not UNSET:
            field_dict["Remarks_TC"] = remarks_tc
        if name_of_building_or_facility_sc is not UNSET:
            field_dict["Name_of_Building_or_Facility_SC"] = (
                name_of_building_or_facility_sc
            )
        if street_sc is not UNSET:
            field_dict["Street_SC"] = street_sc
        if district_sc is not UNSET:
            field_dict["District_SC"] = district_sc
        if region_sc is not UNSET:
            field_dict["Region_SC"] = region_sc
        if location_sc is not UNSET:
            field_dict["Location_SC"] = location_sc
        if type_of_water_dispenser_sc is not UNSET:
            field_dict["Type_of_Water_Dispenser_SC"] = type_of_water_dispenser_sc
        if service_hours_exception_sc is not UNSET:
            field_dict["Service_Hours_Exception_SC"] = service_hours_exception_sc
        if water_temperature_sc is not UNSET:
            field_dict["Water_Temperature_SC"] = water_temperature_sc
        if indoor_outdoor_sc is not UNSET:
            field_dict["Indoor_Outdoor_SC"] = indoor_outdoor_sc
        if remarks_sc is not UNSET:
            field_dict["Remarks_SC"] = remarks_sc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_name_of_building_or_facility_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_building_or_facility_en = _parse_name_of_building_or_facility_en(
            d.pop("Name_of_Building_or_Facility_EN", UNSET)
        )

        def _parse_street_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_en = _parse_street_en(d.pop("Street_EN", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_EN", UNSET))

        def _parse_region_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_en = _parse_region_en(d.pop("Region_EN", UNSET))

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("Location_EN", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_type_of_water_dispenser_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_water_dispenser_en = _parse_type_of_water_dispenser_en(
            d.pop("Type_of_Water_Dispenser_EN", UNSET)
        )

        def _parse_number_of_water_dispenser(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        number_of_water_dispenser = _parse_number_of_water_dispenser(
            d.pop("Number_of_Water_Dispenser", UNSET)
        )

        def _parse_service_hours_from(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours_from = _parse_service_hours_from(
            d.pop("Service_Hours_From", UNSET)
        )

        def _parse_service_hours_to(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours_to = _parse_service_hours_to(d.pop("Service_Hours_To", UNSET))

        def _parse_service_hours_exception_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours_exception_en = _parse_service_hours_exception_en(
            d.pop("Service_Hours_Exception_EN", UNSET)
        )

        def _parse_water_temperature_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        water_temperature_en = _parse_water_temperature_en(
            d.pop("Water_Temperature_EN", UNSET)
        )

        def _parse_indoor_outdoor_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        indoor_outdoor_en = _parse_indoor_outdoor_en(d.pop("Indoor_Outdoor_EN", UNSET))

        def _parse_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_en = _parse_remarks_en(d.pop("Remarks_EN", UNSET))

        def _parse_name_of_building_or_facility_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_building_or_facility_tc = _parse_name_of_building_or_facility_tc(
            d.pop("Name_of_Building_or_Facility_TC", UNSET)
        )

        def _parse_street_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_tc = _parse_street_tc(d.pop("Street_TC", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_region_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_tc = _parse_region_tc(d.pop("Region_TC", UNSET))

        def _parse_location_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_tc = _parse_location_tc(d.pop("Location_TC", UNSET))

        def _parse_type_of_water_dispenser_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_water_dispenser_tc = _parse_type_of_water_dispenser_tc(
            d.pop("Type_of_Water_Dispenser_TC", UNSET)
        )

        def _parse_service_hours_exception_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours_exception_tc = _parse_service_hours_exception_tc(
            d.pop("Service_Hours_Exception_TC", UNSET)
        )

        def _parse_water_temperature_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        water_temperature_tc = _parse_water_temperature_tc(
            d.pop("Water_Temperature_TC", UNSET)
        )

        def _parse_indoor_outdoor_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        indoor_outdoor_tc = _parse_indoor_outdoor_tc(d.pop("Indoor_Outdoor_TC", UNSET))

        def _parse_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_tc = _parse_remarks_tc(d.pop("Remarks_TC", UNSET))

        def _parse_name_of_building_or_facility_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_building_or_facility_sc = _parse_name_of_building_or_facility_sc(
            d.pop("Name_of_Building_or_Facility_SC", UNSET)
        )

        def _parse_street_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_sc = _parse_street_sc(d.pop("Street_SC", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("District_SC", UNSET))

        def _parse_region_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_sc = _parse_region_sc(d.pop("Region_SC", UNSET))

        def _parse_location_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_sc = _parse_location_sc(d.pop("Location_SC", UNSET))

        def _parse_type_of_water_dispenser_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_water_dispenser_sc = _parse_type_of_water_dispenser_sc(
            d.pop("Type_of_Water_Dispenser_SC", UNSET)
        )

        def _parse_service_hours_exception_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours_exception_sc = _parse_service_hours_exception_sc(
            d.pop("Service_Hours_Exception_SC", UNSET)
        )

        def _parse_water_temperature_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        water_temperature_sc = _parse_water_temperature_sc(
            d.pop("Water_Temperature_SC", UNSET)
        )

        def _parse_indoor_outdoor_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        indoor_outdoor_sc = _parse_indoor_outdoor_sc(d.pop("Indoor_Outdoor_SC", UNSET))

        def _parse_remarks_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_sc = _parse_remarks_sc(d.pop("Remarks_SC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            name_of_building_or_facility_en=name_of_building_or_facility_en,
            street_en=street_en,
            district_en=district_en,
            region_en=region_en,
            location_en=location_en,
            latitude=latitude,
            longitude=longitude,
            type_of_water_dispenser_en=type_of_water_dispenser_en,
            number_of_water_dispenser=number_of_water_dispenser,
            service_hours_from=service_hours_from,
            service_hours_to=service_hours_to,
            service_hours_exception_en=service_hours_exception_en,
            water_temperature_en=water_temperature_en,
            indoor_outdoor_en=indoor_outdoor_en,
            remarks_en=remarks_en,
            name_of_building_or_facility_tc=name_of_building_or_facility_tc,
            street_tc=street_tc,
            district_tc=district_tc,
            region_tc=region_tc,
            location_tc=location_tc,
            type_of_water_dispenser_tc=type_of_water_dispenser_tc,
            service_hours_exception_tc=service_hours_exception_tc,
            water_temperature_tc=water_temperature_tc,
            indoor_outdoor_tc=indoor_outdoor_tc,
            remarks_tc=remarks_tc,
            name_of_building_or_facility_sc=name_of_building_or_facility_sc,
            street_sc=street_sc,
            district_sc=district_sc,
            region_sc=region_sc,
            location_sc=location_sc,
            type_of_water_dispenser_sc=type_of_water_dispenser_sc,
            service_hours_exception_sc=service_hours_exception_sc,
            water_temperature_sc=water_temperature_sc,
            indoor_outdoor_sc=indoor_outdoor_sc,
            remarks_sc=remarks_sc,
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
