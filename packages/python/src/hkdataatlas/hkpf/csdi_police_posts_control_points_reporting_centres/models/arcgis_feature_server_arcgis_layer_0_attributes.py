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
        dataset_en (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        search01_en (None | str | Unset): Publisher field type: esriFieldTypeString
        search01_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hours_en (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hours_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_number_en (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_number_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number_en (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_number_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch04_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch04_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch05_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch05_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        lastupdate (None | str | Unset): Publisher field type: esriFieldTypeString
        geometry_easting (None | str | Unset): Publisher field type: esriFieldTypeString
        geometry_northing (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid_1 (None | str | Unset): Publisher field type: esriFieldTypeString
        geometry_longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        geometry_latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    search01_en: None | str | Unset = UNSET
    search01_tc: None | str | Unset = UNSET
    service_hours_en: None | str | Unset = UNSET
    service_hours_tc: None | str | Unset = UNSET
    telephone_number_en: None | str | Unset = UNSET
    telephone_number_tc: None | str | Unset = UNSET
    fax_number_en: None | str | Unset = UNSET
    fax_number_tc: None | str | Unset = UNSET
    nsearch04_en: None | str | Unset = UNSET
    nsearch04_tc: None | str | Unset = UNSET
    nsearch05_en: None | str | Unset = UNSET
    nsearch05_tc: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    lastupdate: None | str | Unset = UNSET
    geometry_easting: None | str | Unset = UNSET
    geometry_northing: None | str | Unset = UNSET
    objectid_1: None | str | Unset = UNSET
    geometry_longitude: None | str | Unset = UNSET
    geometry_latitude: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        search01_en: None | str | Unset
        if isinstance(self.search01_en, Unset):
            search01_en = UNSET
        else:
            search01_en = self.search01_en

        search01_tc: None | str | Unset
        if isinstance(self.search01_tc, Unset):
            search01_tc = UNSET
        else:
            search01_tc = self.search01_tc

        service_hours_en: None | str | Unset
        if isinstance(self.service_hours_en, Unset):
            service_hours_en = UNSET
        else:
            service_hours_en = self.service_hours_en

        service_hours_tc: None | str | Unset
        if isinstance(self.service_hours_tc, Unset):
            service_hours_tc = UNSET
        else:
            service_hours_tc = self.service_hours_tc

        telephone_number_en: None | str | Unset
        if isinstance(self.telephone_number_en, Unset):
            telephone_number_en = UNSET
        else:
            telephone_number_en = self.telephone_number_en

        telephone_number_tc: None | str | Unset
        if isinstance(self.telephone_number_tc, Unset):
            telephone_number_tc = UNSET
        else:
            telephone_number_tc = self.telephone_number_tc

        fax_number_en: None | str | Unset
        if isinstance(self.fax_number_en, Unset):
            fax_number_en = UNSET
        else:
            fax_number_en = self.fax_number_en

        fax_number_tc: None | str | Unset
        if isinstance(self.fax_number_tc, Unset):
            fax_number_tc = UNSET
        else:
            fax_number_tc = self.fax_number_tc

        nsearch04_en: None | str | Unset
        if isinstance(self.nsearch04_en, Unset):
            nsearch04_en = UNSET
        else:
            nsearch04_en = self.nsearch04_en

        nsearch04_tc: None | str | Unset
        if isinstance(self.nsearch04_tc, Unset):
            nsearch04_tc = UNSET
        else:
            nsearch04_tc = self.nsearch04_tc

        nsearch05_en: None | str | Unset
        if isinstance(self.nsearch05_en, Unset):
            nsearch05_en = UNSET
        else:
            nsearch05_en = self.nsearch05_en

        nsearch05_tc: None | str | Unset
        if isinstance(self.nsearch05_tc, Unset):
            nsearch05_tc = UNSET
        else:
            nsearch05_tc = self.nsearch05_tc

        northing: None | str | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        easting: None | str | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

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

        lastupdate: None | str | Unset
        if isinstance(self.lastupdate, Unset):
            lastupdate = UNSET
        else:
            lastupdate = self.lastupdate

        geometry_easting: None | str | Unset
        if isinstance(self.geometry_easting, Unset):
            geometry_easting = UNSET
        else:
            geometry_easting = self.geometry_easting

        geometry_northing: None | str | Unset
        if isinstance(self.geometry_northing, Unset):
            geometry_northing = UNSET
        else:
            geometry_northing = self.geometry_northing

        objectid_1: None | str | Unset
        if isinstance(self.objectid_1, Unset):
            objectid_1 = UNSET
        else:
            objectid_1 = self.objectid_1

        geometry_longitude: None | str | Unset
        if isinstance(self.geometry_longitude, Unset):
            geometry_longitude = UNSET
        else:
            geometry_longitude = self.geometry_longitude

        geometry_latitude: None | str | Unset
        if isinstance(self.geometry_latitude, Unset):
            geometry_latitude = UNSET
        else:
            geometry_latitude = self.geometry_latitude

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dataset_en is not UNSET:
            field_dict["DATASET_EN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["DATASET_TC"] = dataset_tc
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if address_en is not UNSET:
            field_dict["ADDRESS_EN"] = address_en
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if search01_en is not UNSET:
            field_dict["SEARCH01_EN"] = search01_en
        if search01_tc is not UNSET:
            field_dict["SEARCH01_TC"] = search01_tc
        if service_hours_en is not UNSET:
            field_dict["Service_Hours_EN"] = service_hours_en
        if service_hours_tc is not UNSET:
            field_dict["Service_Hours_TC"] = service_hours_tc
        if telephone_number_en is not UNSET:
            field_dict["Telephone_Number_EN"] = telephone_number_en
        if telephone_number_tc is not UNSET:
            field_dict["Telephone_Number_TC"] = telephone_number_tc
        if fax_number_en is not UNSET:
            field_dict["Fax_Number_EN"] = fax_number_en
        if fax_number_tc is not UNSET:
            field_dict["Fax_Number_TC"] = fax_number_tc
        if nsearch04_en is not UNSET:
            field_dict["NSEARCH04_EN"] = nsearch04_en
        if nsearch04_tc is not UNSET:
            field_dict["NSEARCH04_TC"] = nsearch04_tc
        if nsearch05_en is not UNSET:
            field_dict["NSEARCH05_EN"] = nsearch05_en
        if nsearch05_tc is not UNSET:
            field_dict["NSEARCH05_TC"] = nsearch05_tc
        if northing is not UNSET:
            field_dict["NORTHING"] = northing
        if easting is not UNSET:
            field_dict["EASTING"] = easting
        if latitude is not UNSET:
            field_dict["LATITUDE"] = latitude
        if longitude is not UNSET:
            field_dict["LONGITUDE"] = longitude
        if lastupdate is not UNSET:
            field_dict["LASTUPDATE"] = lastupdate
        if geometry_easting is not UNSET:
            field_dict["GeometryEasting"] = geometry_easting
        if geometry_northing is not UNSET:
            field_dict["GeometryNorthing"] = geometry_northing
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
        if geometry_longitude is not UNSET:
            field_dict["GeometryLongitude"] = geometry_longitude
        if geometry_latitude is not UNSET:
            field_dict["GeometryLatitude"] = geometry_latitude
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_dataset_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_en = _parse_dataset_en(d.pop("DATASET_EN", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("DATASET_TC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NAME_EN", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("ADDRESS_EN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

        def _parse_search01_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search01_en = _parse_search01_en(d.pop("SEARCH01_EN", UNSET))

        def _parse_search01_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search01_tc = _parse_search01_tc(d.pop("SEARCH01_TC", UNSET))

        def _parse_service_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours_en = _parse_service_hours_en(d.pop("Service_Hours_EN", UNSET))

        def _parse_service_hours_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours_tc = _parse_service_hours_tc(d.pop("Service_Hours_TC", UNSET))

        def _parse_telephone_number_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_number_en = _parse_telephone_number_en(
            d.pop("Telephone_Number_EN", UNSET)
        )

        def _parse_telephone_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_number_tc = _parse_telephone_number_tc(
            d.pop("Telephone_Number_TC", UNSET)
        )

        def _parse_fax_number_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_en = _parse_fax_number_en(d.pop("Fax_Number_EN", UNSET))

        def _parse_fax_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_number_tc = _parse_fax_number_tc(d.pop("Fax_Number_TC", UNSET))

        def _parse_nsearch04_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch04_en = _parse_nsearch04_en(d.pop("NSEARCH04_EN", UNSET))

        def _parse_nsearch04_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch04_tc = _parse_nsearch04_tc(d.pop("NSEARCH04_TC", UNSET))

        def _parse_nsearch05_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch05_en = _parse_nsearch05_en(d.pop("NSEARCH05_EN", UNSET))

        def _parse_nsearch05_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch05_tc = _parse_nsearch05_tc(d.pop("NSEARCH05_TC", UNSET))

        def _parse_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

        def _parse_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("LATITUDE", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("LONGITUDE", UNSET))

        def _parse_lastupdate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lastupdate = _parse_lastupdate(d.pop("LASTUPDATE", UNSET))

        def _parse_geometry_easting(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geometry_easting = _parse_geometry_easting(d.pop("GeometryEasting", UNSET))

        def _parse_geometry_northing(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geometry_northing = _parse_geometry_northing(d.pop("GeometryNorthing", UNSET))

        def _parse_objectid_1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        objectid_1 = _parse_objectid_1(d.pop("OBJECTID_1", UNSET))

        def _parse_geometry_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geometry_longitude = _parse_geometry_longitude(
            d.pop("GeometryLongitude", UNSET)
        )

        def _parse_geometry_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        geometry_latitude = _parse_geometry_latitude(d.pop("GeometryLatitude", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            search01_en=search01_en,
            search01_tc=search01_tc,
            service_hours_en=service_hours_en,
            service_hours_tc=service_hours_tc,
            telephone_number_en=telephone_number_en,
            telephone_number_tc=telephone_number_tc,
            fax_number_en=fax_number_en,
            fax_number_tc=fax_number_tc,
            nsearch04_en=nsearch04_en,
            nsearch04_tc=nsearch04_tc,
            nsearch05_en=nsearch05_en,
            nsearch05_tc=nsearch05_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            lastupdate=lastupdate,
            geometry_easting=geometry_easting,
            geometry_northing=geometry_northing,
            objectid_1=objectid_1,
            geometry_longitude=geometry_longitude,
            geometry_latitude=geometry_latitude,
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
