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
        area_en (None | str | Unset): Publisher field type: esriFieldTypeString
        area_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        office_hours_en (None | str | Unset): Publisher field type: esriFieldTypeString
        office_hours_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_en (None | str | Unset): Publisher field type: esriFieldTypeString
        telephone_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_en (None | str | Unset): Publisher field type: esriFieldTypeString
        fax_tc (None | str | Unset): Publisher field type: esriFieldTypeString
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
        objectid (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid_1 (int | Unset): Publisher field type: esriFieldTypeOID
    """

    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    area_en: None | str | Unset = UNSET
    area_tc: None | str | Unset = UNSET
    office_hours_en: None | str | Unset = UNSET
    office_hours_tc: None | str | Unset = UNSET
    telephone_en: None | str | Unset = UNSET
    telephone_tc: None | str | Unset = UNSET
    fax_en: None | str | Unset = UNSET
    fax_tc: None | str | Unset = UNSET
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
    objectid: None | str | Unset = UNSET
    objectid_1: int | Unset = UNSET
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

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        area_tc: None | str | Unset
        if isinstance(self.area_tc, Unset):
            area_tc = UNSET
        else:
            area_tc = self.area_tc

        office_hours_en: None | str | Unset
        if isinstance(self.office_hours_en, Unset):
            office_hours_en = UNSET
        else:
            office_hours_en = self.office_hours_en

        office_hours_tc: None | str | Unset
        if isinstance(self.office_hours_tc, Unset):
            office_hours_tc = UNSET
        else:
            office_hours_tc = self.office_hours_tc

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

        fax_en: None | str | Unset
        if isinstance(self.fax_en, Unset):
            fax_en = UNSET
        else:
            fax_en = self.fax_en

        fax_tc: None | str | Unset
        if isinstance(self.fax_tc, Unset):
            fax_tc = UNSET
        else:
            fax_tc = self.fax_tc

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

        objectid: None | str | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        objectid_1 = self.objectid_1

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
        if area_en is not UNSET:
            field_dict["Area_EN"] = area_en
        if area_tc is not UNSET:
            field_dict["Area_TC"] = area_tc
        if office_hours_en is not UNSET:
            field_dict["Office_hours_EN"] = office_hours_en
        if office_hours_tc is not UNSET:
            field_dict["Office_hours_TC"] = office_hours_tc
        if telephone_en is not UNSET:
            field_dict["Telephone_EN"] = telephone_en
        if telephone_tc is not UNSET:
            field_dict["Telephone_TC"] = telephone_tc
        if fax_en is not UNSET:
            field_dict["Fax_EN"] = fax_en
        if fax_tc is not UNSET:
            field_dict["Fax_TC"] = fax_tc
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
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1

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

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("Area_EN", UNSET))

        def _parse_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_tc = _parse_area_tc(d.pop("Area_TC", UNSET))

        def _parse_office_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_hours_en = _parse_office_hours_en(d.pop("Office_hours_EN", UNSET))

        def _parse_office_hours_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_hours_tc = _parse_office_hours_tc(d.pop("Office_hours_TC", UNSET))

        def _parse_telephone_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_en = _parse_telephone_en(d.pop("Telephone_EN", UNSET))

        def _parse_telephone_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_tc = _parse_telephone_tc(d.pop("Telephone_TC", UNSET))

        def _parse_fax_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_en = _parse_fax_en(d.pop("Fax_EN", UNSET))

        def _parse_fax_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fax_tc = _parse_fax_tc(d.pop("Fax_TC", UNSET))

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

        def _parse_objectid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        objectid_1 = d.pop("OBJECTID_1", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            area_en=area_en,
            area_tc=area_tc,
            office_hours_en=office_hours_en,
            office_hours_tc=office_hours_tc,
            telephone_en=telephone_en,
            telephone_tc=telephone_tc,
            fax_en=fax_en,
            fax_tc=fax_tc,
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
            objectid=objectid,
            objectid_1=objectid_1,
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
