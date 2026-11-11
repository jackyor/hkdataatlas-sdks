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
        dataset_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        region_en (None | str | Unset): Publisher field type: esriFieldTypeString
        region_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nearby_post_office_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nearby_post_office_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        i_postal_kiosk_code_en (None | str | Unset): Publisher field type: esriFieldTypeString
        i_postal_kiosk_code_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        max_size_en (None | str | Unset): Publisher field type: esriFieldTypeString
        max_size_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        scopeof_services_en (None | str | Unset): Publisher field type: esriFieldTypeString
        scopeof_services_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        open_hours_weekday_en (None | str | Unset): Publisher field type: esriFieldTypeString
        open_hours_weekday_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        open_hours_sat_en (None | str | Unset): Publisher field type: esriFieldTypeString
        open_hours_sat_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        open_hours_sun_en (None | str | Unset): Publisher field type: esriFieldTypeString
        open_hours_sun_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        open_hours_holiday_en (None | str | Unset): Publisher field type: esriFieldTypeString
        open_hours_holiday_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_en (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_en (None | str | Unset): Publisher field type: esriFieldTypeString
        remarks_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        last_update (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
    """

    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    region_en: None | str | Unset = UNSET
    region_tc: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    nearby_post_office_en: None | str | Unset = UNSET
    nearby_post_office_tc: None | str | Unset = UNSET
    i_postal_kiosk_code_en: None | str | Unset = UNSET
    i_postal_kiosk_code_tc: None | str | Unset = UNSET
    max_size_en: None | str | Unset = UNSET
    max_size_tc: None | str | Unset = UNSET
    scopeof_services_en: None | str | Unset = UNSET
    scopeof_services_tc: None | str | Unset = UNSET
    open_hours_weekday_en: None | str | Unset = UNSET
    open_hours_weekday_tc: None | str | Unset = UNSET
    open_hours_sat_en: None | str | Unset = UNSET
    open_hours_sat_tc: None | str | Unset = UNSET
    open_hours_sun_en: None | str | Unset = UNSET
    open_hours_sun_tc: None | str | Unset = UNSET
    open_hours_holiday_en: None | str | Unset = UNSET
    open_hours_holiday_tc: None | str | Unset = UNSET
    telephone_en: None | str | Unset = UNSET
    telephone_tc: None | str | Unset = UNSET
    remarks_en: None | str | Unset = UNSET
    remarks_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    last_update: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        dataset_en: None | str | Unset
        if isinstance(self.dataset_en, Unset):
            dataset_en = UNSET
        else:
            dataset_en = self.dataset_en

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        region_en: None | str | Unset
        if isinstance(self.region_en, Unset):
            region_en = UNSET
        else:
            region_en = self.region_en

        region_tc: None | str | Unset
        if isinstance(self.region_tc, Unset):
            region_tc = UNSET
        else:
            region_tc = self.region_tc

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        nearby_post_office_en: None | str | Unset
        if isinstance(self.nearby_post_office_en, Unset):
            nearby_post_office_en = UNSET
        else:
            nearby_post_office_en = self.nearby_post_office_en

        nearby_post_office_tc: None | str | Unset
        if isinstance(self.nearby_post_office_tc, Unset):
            nearby_post_office_tc = UNSET
        else:
            nearby_post_office_tc = self.nearby_post_office_tc

        i_postal_kiosk_code_en: None | str | Unset
        if isinstance(self.i_postal_kiosk_code_en, Unset):
            i_postal_kiosk_code_en = UNSET
        else:
            i_postal_kiosk_code_en = self.i_postal_kiosk_code_en

        i_postal_kiosk_code_tc: None | str | Unset
        if isinstance(self.i_postal_kiosk_code_tc, Unset):
            i_postal_kiosk_code_tc = UNSET
        else:
            i_postal_kiosk_code_tc = self.i_postal_kiosk_code_tc

        max_size_en: None | str | Unset
        if isinstance(self.max_size_en, Unset):
            max_size_en = UNSET
        else:
            max_size_en = self.max_size_en

        max_size_tc: None | str | Unset
        if isinstance(self.max_size_tc, Unset):
            max_size_tc = UNSET
        else:
            max_size_tc = self.max_size_tc

        scopeof_services_en: None | str | Unset
        if isinstance(self.scopeof_services_en, Unset):
            scopeof_services_en = UNSET
        else:
            scopeof_services_en = self.scopeof_services_en

        scopeof_services_tc: None | str | Unset
        if isinstance(self.scopeof_services_tc, Unset):
            scopeof_services_tc = UNSET
        else:
            scopeof_services_tc = self.scopeof_services_tc

        open_hours_weekday_en: None | str | Unset
        if isinstance(self.open_hours_weekday_en, Unset):
            open_hours_weekday_en = UNSET
        else:
            open_hours_weekday_en = self.open_hours_weekday_en

        open_hours_weekday_tc: None | str | Unset
        if isinstance(self.open_hours_weekday_tc, Unset):
            open_hours_weekday_tc = UNSET
        else:
            open_hours_weekday_tc = self.open_hours_weekday_tc

        open_hours_sat_en: None | str | Unset
        if isinstance(self.open_hours_sat_en, Unset):
            open_hours_sat_en = UNSET
        else:
            open_hours_sat_en = self.open_hours_sat_en

        open_hours_sat_tc: None | str | Unset
        if isinstance(self.open_hours_sat_tc, Unset):
            open_hours_sat_tc = UNSET
        else:
            open_hours_sat_tc = self.open_hours_sat_tc

        open_hours_sun_en: None | str | Unset
        if isinstance(self.open_hours_sun_en, Unset):
            open_hours_sun_en = UNSET
        else:
            open_hours_sun_en = self.open_hours_sun_en

        open_hours_sun_tc: None | str | Unset
        if isinstance(self.open_hours_sun_tc, Unset):
            open_hours_sun_tc = UNSET
        else:
            open_hours_sun_tc = self.open_hours_sun_tc

        open_hours_holiday_en: None | str | Unset
        if isinstance(self.open_hours_holiday_en, Unset):
            open_hours_holiday_en = UNSET
        else:
            open_hours_holiday_en = self.open_hours_holiday_en

        open_hours_holiday_tc: None | str | Unset
        if isinstance(self.open_hours_holiday_tc, Unset):
            open_hours_holiday_tc = UNSET
        else:
            open_hours_holiday_tc = self.open_hours_holiday_tc

        telephone_en: None | str | Unset
        if isinstance(self.telephone_en, Unset):
            telephone_en = UNSET
        else:
            telephone_en = self.telephone_en

        telephone_tc: None | str | Unset
        if isinstance(self.telephone_tc, Unset):
            telephone_tc = UNSET
        else:
            telephone_tc = self.telephone_tc

        remarks_en: None | str | Unset
        if isinstance(self.remarks_en, Unset):
            remarks_en = UNSET
        else:
            remarks_en = self.remarks_en

        remarks_tc: None | str | Unset
        if isinstance(self.remarks_tc, Unset):
            remarks_tc = UNSET
        else:
            remarks_tc = self.remarks_tc

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

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

        last_update = self.last_update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if dataset_en is not UNSET:
            field_dict["DatasetEN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["DatasetTC"] = dataset_tc
        if name_en is not UNSET:
            field_dict["NameEN"] = name_en
        if address_en is not UNSET:
            field_dict["AddressEN"] = address_en
        if name_tc is not UNSET:
            field_dict["NameTC"] = name_tc
        if address_tc is not UNSET:
            field_dict["AddressTC"] = address_tc
        if region_en is not UNSET:
            field_dict["RegionEN"] = region_en
        if region_tc is not UNSET:
            field_dict["RegionTC"] = region_tc
        if district_en is not UNSET:
            field_dict["DistrictEN"] = district_en
        if district_tc is not UNSET:
            field_dict["DistrictTC"] = district_tc
        if nearby_post_office_en is not UNSET:
            field_dict["NearbyPostOfficeEN"] = nearby_post_office_en
        if nearby_post_office_tc is not UNSET:
            field_dict["NearbyPostOfficeTC"] = nearby_post_office_tc
        if i_postal_kiosk_code_en is not UNSET:
            field_dict["iPostalKioskCodeEN"] = i_postal_kiosk_code_en
        if i_postal_kiosk_code_tc is not UNSET:
            field_dict["iPostalKioskCodeTC"] = i_postal_kiosk_code_tc
        if max_size_en is not UNSET:
            field_dict["MaxSizeEN"] = max_size_en
        if max_size_tc is not UNSET:
            field_dict["MaxSizeTC"] = max_size_tc
        if scopeof_services_en is not UNSET:
            field_dict["ScopeofServicesEN"] = scopeof_services_en
        if scopeof_services_tc is not UNSET:
            field_dict["ScopeofServicesTC"] = scopeof_services_tc
        if open_hours_weekday_en is not UNSET:
            field_dict["OpenHoursWeekdayEN"] = open_hours_weekday_en
        if open_hours_weekday_tc is not UNSET:
            field_dict["OpenHoursWeekdayTC"] = open_hours_weekday_tc
        if open_hours_sat_en is not UNSET:
            field_dict["OpenHoursSatEN"] = open_hours_sat_en
        if open_hours_sat_tc is not UNSET:
            field_dict["OpenHoursSatTC"] = open_hours_sat_tc
        if open_hours_sun_en is not UNSET:
            field_dict["OpenHoursSunEN"] = open_hours_sun_en
        if open_hours_sun_tc is not UNSET:
            field_dict["OpenHoursSunTC"] = open_hours_sun_tc
        if open_hours_holiday_en is not UNSET:
            field_dict["OpenHoursHolidayEN"] = open_hours_holiday_en
        if open_hours_holiday_tc is not UNSET:
            field_dict["OpenHoursHolidayTC"] = open_hours_holiday_tc
        if telephone_en is not UNSET:
            field_dict["TelephoneEN"] = telephone_en
        if telephone_tc is not UNSET:
            field_dict["TelephoneTC"] = telephone_tc
        if remarks_en is not UNSET:
            field_dict["RemarksEN"] = remarks_en
        if remarks_tc is not UNSET:
            field_dict["RemarksTC"] = remarks_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("DatasetEN", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DatasetTC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NameEN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("AddressEN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NameTC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("AddressTC", UNSET))

        def _parse_region_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_en = _parse_region_en(d.pop("RegionEN", UNSET))

        def _parse_region_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_tc = _parse_region_tc(d.pop("RegionTC", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("DistrictEN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("DistrictTC", UNSET))

        def _parse_nearby_post_office_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nearby_post_office_en = _parse_nearby_post_office_en(
            d.pop("NearbyPostOfficeEN", UNSET)
        )

        def _parse_nearby_post_office_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nearby_post_office_tc = _parse_nearby_post_office_tc(
            d.pop("NearbyPostOfficeTC", UNSET)
        )

        def _parse_i_postal_kiosk_code_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        i_postal_kiosk_code_en = _parse_i_postal_kiosk_code_en(
            d.pop("iPostalKioskCodeEN", UNSET)
        )

        def _parse_i_postal_kiosk_code_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        i_postal_kiosk_code_tc = _parse_i_postal_kiosk_code_tc(
            d.pop("iPostalKioskCodeTC", UNSET)
        )

        def _parse_max_size_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_size_en = _parse_max_size_en(d.pop("MaxSizeEN", UNSET))

        def _parse_max_size_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        max_size_tc = _parse_max_size_tc(d.pop("MaxSizeTC", UNSET))

        def _parse_scopeof_services_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scopeof_services_en = _parse_scopeof_services_en(
            d.pop("ScopeofServicesEN", UNSET)
        )

        def _parse_scopeof_services_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scopeof_services_tc = _parse_scopeof_services_tc(
            d.pop("ScopeofServicesTC", UNSET)
        )

        def _parse_open_hours_weekday_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_hours_weekday_en = _parse_open_hours_weekday_en(
            d.pop("OpenHoursWeekdayEN", UNSET)
        )

        def _parse_open_hours_weekday_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_hours_weekday_tc = _parse_open_hours_weekday_tc(
            d.pop("OpenHoursWeekdayTC", UNSET)
        )

        def _parse_open_hours_sat_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_hours_sat_en = _parse_open_hours_sat_en(d.pop("OpenHoursSatEN", UNSET))

        def _parse_open_hours_sat_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_hours_sat_tc = _parse_open_hours_sat_tc(d.pop("OpenHoursSatTC", UNSET))

        def _parse_open_hours_sun_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_hours_sun_en = _parse_open_hours_sun_en(d.pop("OpenHoursSunEN", UNSET))

        def _parse_open_hours_sun_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_hours_sun_tc = _parse_open_hours_sun_tc(d.pop("OpenHoursSunTC", UNSET))

        def _parse_open_hours_holiday_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_hours_holiday_en = _parse_open_hours_holiday_en(
            d.pop("OpenHoursHolidayEN", UNSET)
        )

        def _parse_open_hours_holiday_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        open_hours_holiday_tc = _parse_open_hours_holiday_tc(
            d.pop("OpenHoursHolidayTC", UNSET)
        )

        def _parse_telephone_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_en = _parse_telephone_en(d.pop("TelephoneEN", UNSET))

        def _parse_telephone_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_tc = _parse_telephone_tc(d.pop("TelephoneTC", UNSET))

        def _parse_remarks_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_en = _parse_remarks_en(d.pop("RemarksEN", UNSET))

        def _parse_remarks_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        remarks_tc = _parse_remarks_tc(d.pop("RemarksTC", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        last_update = d.pop("LastUpdate", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            region_en=region_en,
            region_tc=region_tc,
            district_en=district_en,
            district_tc=district_tc,
            nearby_post_office_en=nearby_post_office_en,
            nearby_post_office_tc=nearby_post_office_tc,
            i_postal_kiosk_code_en=i_postal_kiosk_code_en,
            i_postal_kiosk_code_tc=i_postal_kiosk_code_tc,
            max_size_en=max_size_en,
            max_size_tc=max_size_tc,
            scopeof_services_en=scopeof_services_en,
            scopeof_services_tc=scopeof_services_tc,
            open_hours_weekday_en=open_hours_weekday_en,
            open_hours_weekday_tc=open_hours_weekday_tc,
            open_hours_sat_en=open_hours_sat_en,
            open_hours_sat_tc=open_hours_sat_tc,
            open_hours_sun_en=open_hours_sun_en,
            open_hours_sun_tc=open_hours_sun_tc,
            open_hours_holiday_en=open_hours_holiday_en,
            open_hours_holiday_tc=open_hours_holiday_tc,
            telephone_en=telephone_en,
            telephone_tc=telephone_tc,
            remarks_en=remarks_en,
            remarks_tc=remarks_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            last_update=last_update,
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
