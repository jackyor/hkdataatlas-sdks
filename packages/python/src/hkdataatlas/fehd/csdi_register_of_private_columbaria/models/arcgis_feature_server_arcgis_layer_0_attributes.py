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
        search01_en (None | str | Unset): Publisher field type: esriFieldTypeString
        search01_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch01_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch01_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch02_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch02_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (None | str | Unset): Publisher field type: esriFieldTypeString
        easting (None | str | Unset): Publisher field type: esriFieldTypeString
        latitude (None | str | Unset): Publisher field type: esriFieldTypeString
        longitude (None | str | Unset): Publisher field type: esriFieldTypeString
        lastupdate (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    search01_en: None | str | Unset = UNSET
    search01_tc: None | str | Unset = UNSET
    nsearch01_en: None | str | Unset = UNSET
    nsearch01_tc: None | str | Unset = UNSET
    nsearch02_en: None | str | Unset = UNSET
    nsearch02_tc: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    lastupdate: None | str | Unset = UNSET
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

        nsearch01_en: None | str | Unset
        if isinstance(self.nsearch01_en, Unset):
            nsearch01_en = UNSET
        else:
            nsearch01_en = self.nsearch01_en

        nsearch01_tc: None | str | Unset
        if isinstance(self.nsearch01_tc, Unset):
            nsearch01_tc = UNSET
        else:
            nsearch01_tc = self.nsearch01_tc

        nsearch02_en: None | str | Unset
        if isinstance(self.nsearch02_en, Unset):
            nsearch02_en = UNSET
        else:
            nsearch02_en = self.nsearch02_en

        nsearch02_tc: None | str | Unset
        if isinstance(self.nsearch02_tc, Unset):
            nsearch02_tc = UNSET
        else:
            nsearch02_tc = self.nsearch02_tc

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
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
        if nsearch01_en is not UNSET:
            field_dict["NSEARCH01_EN"] = nsearch01_en
        if nsearch01_tc is not UNSET:
            field_dict["NSEARCH01_TC"] = nsearch01_tc
        if nsearch02_en is not UNSET:
            field_dict["NSEARCH02_EN"] = nsearch02_en
        if nsearch02_tc is not UNSET:
            field_dict["NSEARCH02_TC"] = nsearch02_tc
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

        def _parse_nsearch01_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch01_en = _parse_nsearch01_en(d.pop("NSEARCH01_EN", UNSET))

        def _parse_nsearch01_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch01_tc = _parse_nsearch01_tc(d.pop("NSEARCH01_TC", UNSET))

        def _parse_nsearch02_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch02_en = _parse_nsearch02_en(d.pop("NSEARCH02_EN", UNSET))

        def _parse_nsearch02_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch02_tc = _parse_nsearch02_tc(d.pop("NSEARCH02_TC", UNSET))

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

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            search01_en=search01_en,
            search01_tc=search01_tc,
            nsearch01_en=nsearch01_en,
            nsearch01_tc=nsearch01_tc,
            nsearch02_en=nsearch02_en,
            nsearch02_tc=nsearch02_tc,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            lastupdate=lastupdate,
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
