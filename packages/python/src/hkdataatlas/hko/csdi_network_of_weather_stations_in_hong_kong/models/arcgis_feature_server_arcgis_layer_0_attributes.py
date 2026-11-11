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
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        data_gov_hk_en (None | str | Unset): Publisher field type: esriFieldTypeString
        data_gov_hk_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        data_gov_hk_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        elevationofgroundabovemeansea_level_metres_en (float | None | Unset): Publisher field type: esriFieldTypeDouble
        elevationofgroundabovemeansea_level_metres_sc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        elevationofgroundabovemeansea_level_metres_tc (float | None | Unset): Publisher field type: esriFieldTypeDouble
        email_address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        email_address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        email_address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number_en (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude_n_en (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude_n_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude_n_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude_e_en (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude_e_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude_e_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        opening_hours_en (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        opening_hours_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_en (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        typesof_weather_station_en (None | str | Unset): Publisher field type: esriFieldTypeString
        typesof_weather_station_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        typesof_weather_station_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        website_en (None | str | Unset): Publisher field type: esriFieldTypeString
        website_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        website_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    address_en: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    data_gov_hk_en: None | str | Unset = UNSET
    data_gov_hk_sc: None | str | Unset = UNSET
    data_gov_hk_tc: None | str | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_sc: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    elevationofgroundabovemeansea_level_metres_en: float | None | Unset = UNSET
    elevationofgroundabovemeansea_level_metres_sc: float | None | Unset = UNSET
    elevationofgroundabovemeansea_level_metres_tc: float | None | Unset = UNSET
    email_address_en: None | str | Unset = UNSET
    email_address_sc: None | str | Unset = UNSET
    email_address_tc: None | str | Unset = UNSET
    fax_number_en: None | str | Unset = UNSET
    fax_number_sc: None | str | Unset = UNSET
    fax_number_tc: None | str | Unset = UNSET
    last_update: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    latitude_n_en: None | str | Unset = UNSET
    latitude_n_sc: None | str | Unset = UNSET
    latitude_n_tc: None | str | Unset = UNSET
    longitude: float | None | Unset = UNSET
    longitude_e_en: None | str | Unset = UNSET
    longitude_e_sc: None | str | Unset = UNSET
    longitude_e_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_sc: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    opening_hours_en: None | str | Unset = UNSET
    opening_hours_sc: None | str | Unset = UNSET
    opening_hours_tc: None | str | Unset = UNSET
    telephone_en: None | str | Unset = UNSET
    telephone_sc: None | str | Unset = UNSET
    telephone_tc: None | str | Unset = UNSET
    typesof_weather_station_en: None | str | Unset = UNSET
    typesof_weather_station_sc: None | str | Unset = UNSET
    typesof_weather_station_tc: None | str | Unset = UNSET
    website_en: None | str | Unset = UNSET
    website_sc: None | str | Unset = UNSET
    website_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        data_gov_hk_en: None | str | Unset
        if isinstance(self.data_gov_hk_en, Unset):
            data_gov_hk_en = UNSET
        else:
            data_gov_hk_en = self.data_gov_hk_en

        data_gov_hk_sc: None | str | Unset
        if isinstance(self.data_gov_hk_sc, Unset):
            data_gov_hk_sc = UNSET
        else:
            data_gov_hk_sc = self.data_gov_hk_sc

        data_gov_hk_tc: None | str | Unset
        if isinstance(self.data_gov_hk_tc, Unset):
            data_gov_hk_tc = UNSET
        else:
            data_gov_hk_tc = self.data_gov_hk_tc

        dataset_en: None | str | Unset
        if isinstance(self.dataset_en, Unset):
            dataset_en = UNSET
        else:
            dataset_en = self.dataset_en

        dataset_sc: None | str | Unset
        if isinstance(self.dataset_sc, Unset):
            dataset_sc = UNSET
        else:
            dataset_sc = self.dataset_sc

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        elevationofgroundabovemeansea_level_metres_en: float | None | Unset
        if isinstance(self.elevationofgroundabovemeansea_level_metres_en, Unset):
            elevationofgroundabovemeansea_level_metres_en = UNSET
        else:
            elevationofgroundabovemeansea_level_metres_en = (
                self.elevationofgroundabovemeansea_level_metres_en
            )

        elevationofgroundabovemeansea_level_metres_sc: float | None | Unset
        if isinstance(self.elevationofgroundabovemeansea_level_metres_sc, Unset):
            elevationofgroundabovemeansea_level_metres_sc = UNSET
        else:
            elevationofgroundabovemeansea_level_metres_sc = (
                self.elevationofgroundabovemeansea_level_metres_sc
            )

        elevationofgroundabovemeansea_level_metres_tc: float | None | Unset
        if isinstance(self.elevationofgroundabovemeansea_level_metres_tc, Unset):
            elevationofgroundabovemeansea_level_metres_tc = UNSET
        else:
            elevationofgroundabovemeansea_level_metres_tc = (
                self.elevationofgroundabovemeansea_level_metres_tc
            )

        email_address_en: None | str | Unset
        if isinstance(self.email_address_en, Unset):
            email_address_en = UNSET
        else:
            email_address_en = self.email_address_en

        email_address_sc: None | str | Unset
        if isinstance(self.email_address_sc, Unset):
            email_address_sc = UNSET
        else:
            email_address_sc = self.email_address_sc

        email_address_tc: None | str | Unset
        if isinstance(self.email_address_tc, Unset):
            email_address_tc = UNSET
        else:
            email_address_tc = self.email_address_tc

        fax_number_en: None | str | Unset
        if isinstance(self.fax_number_en, Unset):
            fax_number_en = UNSET
        else:
            fax_number_en = self.fax_number_en

        fax_number_sc: None | str | Unset
        if isinstance(self.fax_number_sc, Unset):
            fax_number_sc = UNSET
        else:
            fax_number_sc = self.fax_number_sc

        fax_number_tc: None | str | Unset
        if isinstance(self.fax_number_tc, Unset):
            fax_number_tc = UNSET
        else:
            fax_number_tc = self.fax_number_tc

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        latitude_n_en: None | str | Unset
        if isinstance(self.latitude_n_en, Unset):
            latitude_n_en = UNSET
        else:
            latitude_n_en = self.latitude_n_en

        latitude_n_sc: None | str | Unset
        if isinstance(self.latitude_n_sc, Unset):
            latitude_n_sc = UNSET
        else:
            latitude_n_sc = self.latitude_n_sc

        latitude_n_tc: None | str | Unset
        if isinstance(self.latitude_n_tc, Unset):
            latitude_n_tc = UNSET
        else:
            latitude_n_tc = self.latitude_n_tc

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        longitude_e_en: None | str | Unset
        if isinstance(self.longitude_e_en, Unset):
            longitude_e_en = UNSET
        else:
            longitude_e_en = self.longitude_e_en

        longitude_e_sc: None | str | Unset
        if isinstance(self.longitude_e_sc, Unset):
            longitude_e_sc = UNSET
        else:
            longitude_e_sc = self.longitude_e_sc

        longitude_e_tc: None | str | Unset
        if isinstance(self.longitude_e_tc, Unset):
            longitude_e_tc = UNSET
        else:
            longitude_e_tc = self.longitude_e_tc

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

        name_sc: None | str | Unset
        if isinstance(self.name_sc, Unset):
            name_sc = UNSET
        else:
            name_sc = self.name_sc

        name_tc: None | str | Unset
        if isinstance(self.name_tc, Unset):
            name_tc = UNSET
        else:
            name_tc = self.name_tc

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        opening_hours_en: None | str | Unset
        if isinstance(self.opening_hours_en, Unset):
            opening_hours_en = UNSET
        else:
            opening_hours_en = self.opening_hours_en

        opening_hours_sc: None | str | Unset
        if isinstance(self.opening_hours_sc, Unset):
            opening_hours_sc = UNSET
        else:
            opening_hours_sc = self.opening_hours_sc

        opening_hours_tc: None | str | Unset
        if isinstance(self.opening_hours_tc, Unset):
            opening_hours_tc = UNSET
        else:
            opening_hours_tc = self.opening_hours_tc

        telephone_en: None | str | Unset
        if isinstance(self.telephone_en, Unset):
            telephone_en = UNSET
        else:
            telephone_en = self.telephone_en

        telephone_sc: None | str | Unset
        if isinstance(self.telephone_sc, Unset):
            telephone_sc = UNSET
        else:
            telephone_sc = self.telephone_sc

        telephone_tc: None | str | Unset
        if isinstance(self.telephone_tc, Unset):
            telephone_tc = UNSET
        else:
            telephone_tc = self.telephone_tc

        typesof_weather_station_en: None | str | Unset
        if isinstance(self.typesof_weather_station_en, Unset):
            typesof_weather_station_en = UNSET
        else:
            typesof_weather_station_en = self.typesof_weather_station_en

        typesof_weather_station_sc: None | str | Unset
        if isinstance(self.typesof_weather_station_sc, Unset):
            typesof_weather_station_sc = UNSET
        else:
            typesof_weather_station_sc = self.typesof_weather_station_sc

        typesof_weather_station_tc: None | str | Unset
        if isinstance(self.typesof_weather_station_tc, Unset):
            typesof_weather_station_tc = UNSET
        else:
            typesof_weather_station_tc = self.typesof_weather_station_tc

        website_en: None | str | Unset
        if isinstance(self.website_en, Unset):
            website_en = UNSET
        else:
            website_en = self.website_en

        website_sc: None | str | Unset
        if isinstance(self.website_sc, Unset):
            website_sc = UNSET
        else:
            website_sc = self.website_sc

        website_tc: None | str | Unset
        if isinstance(self.website_tc, Unset):
            website_tc = UNSET
        else:
            website_tc = self.website_tc

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["Address_en"] = address_en
        if address_sc is not UNSET:
            field_dict["Address_sc"] = address_sc
        if address_tc is not UNSET:
            field_dict["Address_tc"] = address_tc
        if data_gov_hk_en is not UNSET:
            field_dict["DataGovHK_en"] = data_gov_hk_en
        if data_gov_hk_sc is not UNSET:
            field_dict["DataGovHK_sc"] = data_gov_hk_sc
        if data_gov_hk_tc is not UNSET:
            field_dict["DataGovHK_tc"] = data_gov_hk_tc
        if dataset_en is not UNSET:
            field_dict["Dataset_en"] = dataset_en
        if dataset_sc is not UNSET:
            field_dict["Dataset_sc"] = dataset_sc
        if dataset_tc is not UNSET:
            field_dict["Dataset_tc"] = dataset_tc
        if easting is not UNSET:
            field_dict["Easting"] = easting
        if elevationofgroundabovemeansea_level_metres_en is not UNSET:
            field_dict["Elevationofgroundabovemeansea_level_metres_en"] = (
                elevationofgroundabovemeansea_level_metres_en
            )
        if elevationofgroundabovemeansea_level_metres_sc is not UNSET:
            field_dict["Elevationofgroundabovemeansea_level_metres_sc"] = (
                elevationofgroundabovemeansea_level_metres_sc
            )
        if elevationofgroundabovemeansea_level_metres_tc is not UNSET:
            field_dict["Elevationofgroundabovemeansea_level_metres_tc"] = (
                elevationofgroundabovemeansea_level_metres_tc
            )
        if email_address_en is not UNSET:
            field_dict["EmailAddress_en"] = email_address_en
        if email_address_sc is not UNSET:
            field_dict["EmailAddress_sc"] = email_address_sc
        if email_address_tc is not UNSET:
            field_dict["EmailAddress_tc"] = email_address_tc
        if fax_number_en is not UNSET:
            field_dict["FaxNumber_en"] = fax_number_en
        if fax_number_sc is not UNSET:
            field_dict["FaxNumber_sc"] = fax_number_sc
        if fax_number_tc is not UNSET:
            field_dict["FaxNumber_tc"] = fax_number_tc
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if latitude_n_en is not UNSET:
            field_dict["Latitude_N_en"] = latitude_n_en
        if latitude_n_sc is not UNSET:
            field_dict["Latitude_N_sc"] = latitude_n_sc
        if latitude_n_tc is not UNSET:
            field_dict["Latitude_N_tc"] = latitude_n_tc
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if longitude_e_en is not UNSET:
            field_dict["Longitude_E_en"] = longitude_e_en
        if longitude_e_sc is not UNSET:
            field_dict["Longitude_E_sc"] = longitude_e_sc
        if longitude_e_tc is not UNSET:
            field_dict["Longitude_E_tc"] = longitude_e_tc
        if name_en is not UNSET:
            field_dict["Name_en"] = name_en
        if name_sc is not UNSET:
            field_dict["Name_sc"] = name_sc
        if name_tc is not UNSET:
            field_dict["Name_tc"] = name_tc
        if northing is not UNSET:
            field_dict["Northing"] = northing
        if opening_hours_en is not UNSET:
            field_dict["OpeningHours_en"] = opening_hours_en
        if opening_hours_sc is not UNSET:
            field_dict["OpeningHours_sc"] = opening_hours_sc
        if opening_hours_tc is not UNSET:
            field_dict["OpeningHours_tc"] = opening_hours_tc
        if telephone_en is not UNSET:
            field_dict["Telephone_en"] = telephone_en
        if telephone_sc is not UNSET:
            field_dict["Telephone_sc"] = telephone_sc
        if telephone_tc is not UNSET:
            field_dict["Telephone_tc"] = telephone_tc
        if typesof_weather_station_en is not UNSET:
            field_dict["TypesofWeatherStation_en"] = typesof_weather_station_en
        if typesof_weather_station_sc is not UNSET:
            field_dict["TypesofWeatherStation_sc"] = typesof_weather_station_sc
        if typesof_weather_station_tc is not UNSET:
            field_dict["TypesofWeatherStation_tc"] = typesof_weather_station_tc
        if website_en is not UNSET:
            field_dict["Website_en"] = website_en
        if website_sc is not UNSET:
            field_dict["Website_sc"] = website_sc
        if website_tc is not UNSET:
            field_dict["Website_tc"] = website_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_en", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_sc", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_tc", UNSET))

        def _parse_data_gov_hk_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_gov_hk_en = _parse_data_gov_hk_en(d.pop("DataGovHK_en", UNSET))

        def _parse_data_gov_hk_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_gov_hk_sc = _parse_data_gov_hk_sc(d.pop("DataGovHK_sc", UNSET))

        def _parse_data_gov_hk_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_gov_hk_tc = _parse_data_gov_hk_tc(d.pop("DataGovHK_tc", UNSET))

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("Dataset_en", UNSET))

        def _parse_dataset_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_sc = _parse_dataset_sc(d.pop("Dataset_sc", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("Dataset_tc", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("Easting", UNSET))

        def _parse_elevationofgroundabovemeansea_level_metres_en(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        elevationofgroundabovemeansea_level_metres_en = (
            _parse_elevationofgroundabovemeansea_level_metres_en(
                d.pop("Elevationofgroundabovemeansea_level_metres_en", UNSET)
            )
        )

        def _parse_elevationofgroundabovemeansea_level_metres_sc(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        elevationofgroundabovemeansea_level_metres_sc = (
            _parse_elevationofgroundabovemeansea_level_metres_sc(
                d.pop("Elevationofgroundabovemeansea_level_metres_sc", UNSET)
            )
        )

        def _parse_elevationofgroundabovemeansea_level_metres_tc(
            data: object,
        ) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        elevationofgroundabovemeansea_level_metres_tc = (
            _parse_elevationofgroundabovemeansea_level_metres_tc(
                d.pop("Elevationofgroundabovemeansea_level_metres_tc", UNSET)
            )
        )

        def _parse_email_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address_en = _parse_email_address_en(d.pop("EmailAddress_en", UNSET))

        def _parse_email_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address_sc = _parse_email_address_sc(d.pop("EmailAddress_sc", UNSET))

        def _parse_email_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email_address_tc = _parse_email_address_tc(d.pop("EmailAddress_tc", UNSET))

        def _parse_fax_number_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_en = _parse_fax_number_en(d.pop("FaxNumber_en", UNSET))

        def _parse_fax_number_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_sc = _parse_fax_number_sc(d.pop("FaxNumber_sc", UNSET))

        def _parse_fax_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_tc = _parse_fax_number_tc(d.pop("FaxNumber_tc", UNSET))

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("LastUpdate", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_latitude_n_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude_n_en = _parse_latitude_n_en(d.pop("Latitude_N_en", UNSET))

        def _parse_latitude_n_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude_n_sc = _parse_latitude_n_sc(d.pop("Latitude_N_sc", UNSET))

        def _parse_latitude_n_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude_n_tc = _parse_latitude_n_tc(d.pop("Latitude_N_tc", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        def _parse_longitude_e_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude_e_en = _parse_longitude_e_en(d.pop("Longitude_E_en", UNSET))

        def _parse_longitude_e_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude_e_sc = _parse_longitude_e_sc(d.pop("Longitude_E_sc", UNSET))

        def _parse_longitude_e_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude_e_tc = _parse_longitude_e_tc(d.pop("Longitude_E_tc", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("Name_en", UNSET))

        def _parse_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_sc = _parse_name_sc(d.pop("Name_sc", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("Name_tc", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("Northing", UNSET))

        def _parse_opening_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_en = _parse_opening_hours_en(d.pop("OpeningHours_en", UNSET))

        def _parse_opening_hours_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_sc = _parse_opening_hours_sc(d.pop("OpeningHours_sc", UNSET))

        def _parse_opening_hours_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_hours_tc = _parse_opening_hours_tc(d.pop("OpeningHours_tc", UNSET))

        def _parse_telephone_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_en = _parse_telephone_en(d.pop("Telephone_en", UNSET))

        def _parse_telephone_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_sc = _parse_telephone_sc(d.pop("Telephone_sc", UNSET))

        def _parse_telephone_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_tc = _parse_telephone_tc(d.pop("Telephone_tc", UNSET))

        def _parse_typesof_weather_station_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        typesof_weather_station_en = _parse_typesof_weather_station_en(
            d.pop("TypesofWeatherStation_en", UNSET)
        )

        def _parse_typesof_weather_station_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        typesof_weather_station_sc = _parse_typesof_weather_station_sc(
            d.pop("TypesofWeatherStation_sc", UNSET)
        )

        def _parse_typesof_weather_station_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        typesof_weather_station_tc = _parse_typesof_weather_station_tc(
            d.pop("TypesofWeatherStation_tc", UNSET)
        )

        def _parse_website_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_en = _parse_website_en(d.pop("Website_en", UNSET))

        def _parse_website_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_sc = _parse_website_sc(d.pop("Website_sc", UNSET))

        def _parse_website_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_tc = _parse_website_tc(d.pop("Website_tc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            address_en=address_en,
            address_sc=address_sc,
            address_tc=address_tc,
            data_gov_hk_en=data_gov_hk_en,
            data_gov_hk_sc=data_gov_hk_sc,
            data_gov_hk_tc=data_gov_hk_tc,
            dataset_en=dataset_en,
            dataset_sc=dataset_sc,
            dataset_tc=dataset_tc,
            easting=easting,
            elevationofgroundabovemeansea_level_metres_en=elevationofgroundabovemeansea_level_metres_en,
            elevationofgroundabovemeansea_level_metres_sc=elevationofgroundabovemeansea_level_metres_sc,
            elevationofgroundabovemeansea_level_metres_tc=elevationofgroundabovemeansea_level_metres_tc,
            email_address_en=email_address_en,
            email_address_sc=email_address_sc,
            email_address_tc=email_address_tc,
            fax_number_en=fax_number_en,
            fax_number_sc=fax_number_sc,
            fax_number_tc=fax_number_tc,
            last_update=last_update,
            latitude=latitude,
            latitude_n_en=latitude_n_en,
            latitude_n_sc=latitude_n_sc,
            latitude_n_tc=latitude_n_tc,
            longitude=longitude,
            longitude_e_en=longitude_e_en,
            longitude_e_sc=longitude_e_sc,
            longitude_e_tc=longitude_e_tc,
            name_en=name_en,
            name_sc=name_sc,
            name_tc=name_tc,
            northing=northing,
            opening_hours_en=opening_hours_en,
            opening_hours_sc=opening_hours_sc,
            opening_hours_tc=opening_hours_tc,
            telephone_en=telephone_en,
            telephone_sc=telephone_sc,
            telephone_tc=telephone_tc,
            typesof_weather_station_en=typesof_weather_station_en,
            typesof_weather_station_sc=typesof_weather_station_sc,
            typesof_weather_station_tc=typesof_weather_station_tc,
            website_en=website_en,
            website_sc=website_sc,
            website_tc=website_tc,
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
