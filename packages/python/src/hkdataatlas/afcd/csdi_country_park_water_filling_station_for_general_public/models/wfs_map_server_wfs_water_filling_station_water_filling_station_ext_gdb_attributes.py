from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="WfsMapServerWfsWaterFillingStationWaterFillingStationExtGDBAttributes"
)


@_attrs_define
class WfsMapServerWfsWaterFillingStationWaterFillingStationExtGDBAttributes:
    """
    Attributes:
        fac_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        country_park_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        country_park_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        facility_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        facility_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        location_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        type_of_water_dispenser_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        type_of_water_dispenser_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        service_hour (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        type_of_venue_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        type_of_venue_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        water_temperature_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        water_temperature_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    fac_id: None | str | Unset = UNSET
    country_park_en: None | str | Unset = UNSET
    country_park_tc: None | str | Unset = UNSET
    facility_name_en: None | str | Unset = UNSET
    facility_name_tc: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    type_of_water_dispenser_en: None | str | Unset = UNSET
    type_of_water_dispenser_tc: None | str | Unset = UNSET
    service_hour: None | str | Unset = UNSET
    type_of_venue_en: None | str | Unset = UNSET
    type_of_venue_tc: None | str | Unset = UNSET
    water_temperature_en: None | str | Unset = UNSET
    water_temperature_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fac_id: None | str | Unset
        if isinstance(self.fac_id, Unset):
            fac_id = UNSET
        else:
            fac_id = self.fac_id

        country_park_en: None | str | Unset
        if isinstance(self.country_park_en, Unset):
            country_park_en = UNSET
        else:
            country_park_en = self.country_park_en

        country_park_tc: None | str | Unset
        if isinstance(self.country_park_tc, Unset):
            country_park_tc = UNSET
        else:
            country_park_tc = self.country_park_tc

        facility_name_en: None | str | Unset
        if isinstance(self.facility_name_en, Unset):
            facility_name_en = UNSET
        else:
            facility_name_en = self.facility_name_en

        facility_name_tc: None | str | Unset
        if isinstance(self.facility_name_tc, Unset):
            facility_name_tc = UNSET
        else:
            facility_name_tc = self.facility_name_tc

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        location_tc: None | str | Unset
        if isinstance(self.location_tc, Unset):
            location_tc = UNSET
        else:
            location_tc = self.location_tc

        type_of_water_dispenser_en: None | str | Unset
        if isinstance(self.type_of_water_dispenser_en, Unset):
            type_of_water_dispenser_en = UNSET
        else:
            type_of_water_dispenser_en = self.type_of_water_dispenser_en

        type_of_water_dispenser_tc: None | str | Unset
        if isinstance(self.type_of_water_dispenser_tc, Unset):
            type_of_water_dispenser_tc = UNSET
        else:
            type_of_water_dispenser_tc = self.type_of_water_dispenser_tc

        service_hour: None | str | Unset
        if isinstance(self.service_hour, Unset):
            service_hour = UNSET
        else:
            service_hour = self.service_hour

        type_of_venue_en: None | str | Unset
        if isinstance(self.type_of_venue_en, Unset):
            type_of_venue_en = UNSET
        else:
            type_of_venue_en = self.type_of_venue_en

        type_of_venue_tc: None | str | Unset
        if isinstance(self.type_of_venue_tc, Unset):
            type_of_venue_tc = UNSET
        else:
            type_of_venue_tc = self.type_of_venue_tc

        water_temperature_en: None | str | Unset
        if isinstance(self.water_temperature_en, Unset):
            water_temperature_en = UNSET
        else:
            water_temperature_en = self.water_temperature_en

        water_temperature_tc: None | str | Unset
        if isinstance(self.water_temperature_tc, Unset):
            water_temperature_tc = UNSET
        else:
            water_temperature_tc = self.water_temperature_tc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fac_id is not UNSET:
            field_dict["FAC_ID"] = fac_id
        if country_park_en is not UNSET:
            field_dict["COUNTRY_PARK_EN"] = country_park_en
        if country_park_tc is not UNSET:
            field_dict["COUNTRY_PARK_TC"] = country_park_tc
        if facility_name_en is not UNSET:
            field_dict["FACILITY_NAME_EN"] = facility_name_en
        if facility_name_tc is not UNSET:
            field_dict["FACILITY_NAME_TC"] = facility_name_tc
        if location_en is not UNSET:
            field_dict["LOCATION_EN"] = location_en
        if location_tc is not UNSET:
            field_dict["LOCATION_TC"] = location_tc
        if type_of_water_dispenser_en is not UNSET:
            field_dict["TYPE_OF_WATER_DISPENSER_EN"] = type_of_water_dispenser_en
        if type_of_water_dispenser_tc is not UNSET:
            field_dict["TYPE_OF_WATER_DISPENSER_TC"] = type_of_water_dispenser_tc
        if service_hour is not UNSET:
            field_dict["SERVICE_HOUR"] = service_hour
        if type_of_venue_en is not UNSET:
            field_dict["TYPE_OF_VENUE_EN"] = type_of_venue_en
        if type_of_venue_tc is not UNSET:
            field_dict["TYPE_OF_VENUE_TC"] = type_of_venue_tc
        if water_temperature_en is not UNSET:
            field_dict["WATER_TEMPERATURE_EN"] = water_temperature_en
        if water_temperature_tc is not UNSET:
            field_dict["WATER_TEMPERATURE_TC"] = water_temperature_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_fac_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_id = _parse_fac_id(d.pop("FAC_ID", UNSET))

        def _parse_country_park_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_park_en = _parse_country_park_en(d.pop("COUNTRY_PARK_EN", UNSET))

        def _parse_country_park_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_park_tc = _parse_country_park_tc(d.pop("COUNTRY_PARK_TC", UNSET))

        def _parse_facility_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_en = _parse_facility_name_en(d.pop("FACILITY_NAME_EN", UNSET))

        def _parse_facility_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_name_tc = _parse_facility_name_tc(d.pop("FACILITY_NAME_TC", UNSET))

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("LOCATION_EN", UNSET))

        def _parse_location_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_tc = _parse_location_tc(d.pop("LOCATION_TC", UNSET))

        def _parse_type_of_water_dispenser_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_water_dispenser_en = _parse_type_of_water_dispenser_en(
            d.pop("TYPE_OF_WATER_DISPENSER_EN", UNSET)
        )

        def _parse_type_of_water_dispenser_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_water_dispenser_tc = _parse_type_of_water_dispenser_tc(
            d.pop("TYPE_OF_WATER_DISPENSER_TC", UNSET)
        )

        def _parse_service_hour(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hour = _parse_service_hour(d.pop("SERVICE_HOUR", UNSET))

        def _parse_type_of_venue_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_venue_en = _parse_type_of_venue_en(d.pop("TYPE_OF_VENUE_EN", UNSET))

        def _parse_type_of_venue_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_venue_tc = _parse_type_of_venue_tc(d.pop("TYPE_OF_VENUE_TC", UNSET))

        def _parse_water_temperature_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        water_temperature_en = _parse_water_temperature_en(
            d.pop("WATER_TEMPERATURE_EN", UNSET)
        )

        def _parse_water_temperature_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        water_temperature_tc = _parse_water_temperature_tc(
            d.pop("WATER_TEMPERATURE_TC", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        wfs_map_server_wfs_water_filling_station_water_filling_station_ext_gdb_attributes = cls(
            fac_id=fac_id,
            country_park_en=country_park_en,
            country_park_tc=country_park_tc,
            facility_name_en=facility_name_en,
            facility_name_tc=facility_name_tc,
            location_en=location_en,
            location_tc=location_tc,
            type_of_water_dispenser_en=type_of_water_dispenser_en,
            type_of_water_dispenser_tc=type_of_water_dispenser_tc,
            service_hour=service_hour,
            type_of_venue_en=type_of_venue_en,
            type_of_venue_tc=type_of_venue_tc,
            water_temperature_en=water_temperature_en,
            water_temperature_tc=water_temperature_tc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_water_filling_station_water_filling_station_ext_gdb_attributes.additional_properties = d
        return wfs_map_server_wfs_water_filling_station_water_filling_station_ext_gdb_attributes

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
