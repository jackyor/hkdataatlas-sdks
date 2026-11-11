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
        nsearch01_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch01_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch02_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch02_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch03_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch03_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch04_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch04_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch05_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch05_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch06_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch06_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch07_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch07_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch08_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch08_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch09_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch09_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch10_en (None | str | Unset): Publisher field type: esriFieldTypeString
        nsearch10_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        northing (float | None | Unset): Publisher field type: esriFieldTypeDouble
        easting (float | None | Unset): Publisher field type: esriFieldTypeDouble
        latitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        longitude (float | None | Unset): Publisher field type: esriFieldTypeDouble
        lastupdate (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
    """

    objectid: int | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    nsearch01_en: None | str | Unset = UNSET
    nsearch01_tc: None | str | Unset = UNSET
    nsearch02_en: None | str | Unset = UNSET
    nsearch02_tc: None | str | Unset = UNSET
    nsearch03_en: None | str | Unset = UNSET
    nsearch03_tc: None | str | Unset = UNSET
    nsearch04_en: None | str | Unset = UNSET
    nsearch04_tc: None | str | Unset = UNSET
    nsearch05_en: None | str | Unset = UNSET
    nsearch05_tc: None | str | Unset = UNSET
    nsearch06_en: None | str | Unset = UNSET
    nsearch06_tc: None | str | Unset = UNSET
    nsearch07_en: None | str | Unset = UNSET
    nsearch07_tc: None | str | Unset = UNSET
    nsearch08_en: None | str | Unset = UNSET
    nsearch08_tc: None | str | Unset = UNSET
    nsearch09_en: None | str | Unset = UNSET
    nsearch09_tc: None | str | Unset = UNSET
    nsearch10_en: None | str | Unset = UNSET
    nsearch10_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
    easting: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    lastupdate: Any | Unset = UNSET
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

        nsearch03_en: None | str | Unset
        if isinstance(self.nsearch03_en, Unset):
            nsearch03_en = UNSET
        else:
            nsearch03_en = self.nsearch03_en

        nsearch03_tc: None | str | Unset
        if isinstance(self.nsearch03_tc, Unset):
            nsearch03_tc = UNSET
        else:
            nsearch03_tc = self.nsearch03_tc

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

        nsearch06_en: None | str | Unset
        if isinstance(self.nsearch06_en, Unset):
            nsearch06_en = UNSET
        else:
            nsearch06_en = self.nsearch06_en

        nsearch06_tc: None | str | Unset
        if isinstance(self.nsearch06_tc, Unset):
            nsearch06_tc = UNSET
        else:
            nsearch06_tc = self.nsearch06_tc

        nsearch07_en: None | str | Unset
        if isinstance(self.nsearch07_en, Unset):
            nsearch07_en = UNSET
        else:
            nsearch07_en = self.nsearch07_en

        nsearch07_tc: None | str | Unset
        if isinstance(self.nsearch07_tc, Unset):
            nsearch07_tc = UNSET
        else:
            nsearch07_tc = self.nsearch07_tc

        nsearch08_en: None | str | Unset
        if isinstance(self.nsearch08_en, Unset):
            nsearch08_en = UNSET
        else:
            nsearch08_en = self.nsearch08_en

        nsearch08_tc: None | str | Unset
        if isinstance(self.nsearch08_tc, Unset):
            nsearch08_tc = UNSET
        else:
            nsearch08_tc = self.nsearch08_tc

        nsearch09_en: None | str | Unset
        if isinstance(self.nsearch09_en, Unset):
            nsearch09_en = UNSET
        else:
            nsearch09_en = self.nsearch09_en

        nsearch09_tc: None | str | Unset
        if isinstance(self.nsearch09_tc, Unset):
            nsearch09_tc = UNSET
        else:
            nsearch09_tc = self.nsearch09_tc

        nsearch10_en: None | str | Unset
        if isinstance(self.nsearch10_en, Unset):
            nsearch10_en = UNSET
        else:
            nsearch10_en = self.nsearch10_en

        nsearch10_tc: None | str | Unset
        if isinstance(self.nsearch10_tc, Unset):
            nsearch10_tc = UNSET
        else:
            nsearch10_tc = self.nsearch10_tc

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
        if nsearch01_en is not UNSET:
            field_dict["NSEARCH01_EN"] = nsearch01_en
        if nsearch01_tc is not UNSET:
            field_dict["NSEARCH01_TC"] = nsearch01_tc
        if nsearch02_en is not UNSET:
            field_dict["NSEARCH02_EN"] = nsearch02_en
        if nsearch02_tc is not UNSET:
            field_dict["NSEARCH02_TC"] = nsearch02_tc
        if nsearch03_en is not UNSET:
            field_dict["NSEARCH03_EN"] = nsearch03_en
        if nsearch03_tc is not UNSET:
            field_dict["NSEARCH03_TC"] = nsearch03_tc
        if nsearch04_en is not UNSET:
            field_dict["NSEARCH04_EN"] = nsearch04_en
        if nsearch04_tc is not UNSET:
            field_dict["NSEARCH04_TC"] = nsearch04_tc
        if nsearch05_en is not UNSET:
            field_dict["NSEARCH05_EN"] = nsearch05_en
        if nsearch05_tc is not UNSET:
            field_dict["NSEARCH05_TC"] = nsearch05_tc
        if nsearch06_en is not UNSET:
            field_dict["NSEARCH06_EN"] = nsearch06_en
        if nsearch06_tc is not UNSET:
            field_dict["NSEARCH06_TC"] = nsearch06_tc
        if nsearch07_en is not UNSET:
            field_dict["NSEARCH07_EN"] = nsearch07_en
        if nsearch07_tc is not UNSET:
            field_dict["NSEARCH07_TC"] = nsearch07_tc
        if nsearch08_en is not UNSET:
            field_dict["NSEARCH08_EN"] = nsearch08_en
        if nsearch08_tc is not UNSET:
            field_dict["NSEARCH08_TC"] = nsearch08_tc
        if nsearch09_en is not UNSET:
            field_dict["NSEARCH09_EN"] = nsearch09_en
        if nsearch09_tc is not UNSET:
            field_dict["NSEARCH09_TC"] = nsearch09_tc
        if nsearch10_en is not UNSET:
            field_dict["NSEARCH10_EN"] = nsearch10_en
        if nsearch10_tc is not UNSET:
            field_dict["NSEARCH10_TC"] = nsearch10_tc
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

        def _parse_nsearch03_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch03_en = _parse_nsearch03_en(d.pop("NSEARCH03_EN", UNSET))

        def _parse_nsearch03_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch03_tc = _parse_nsearch03_tc(d.pop("NSEARCH03_TC", UNSET))

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

        def _parse_nsearch06_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch06_en = _parse_nsearch06_en(d.pop("NSEARCH06_EN", UNSET))

        def _parse_nsearch06_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch06_tc = _parse_nsearch06_tc(d.pop("NSEARCH06_TC", UNSET))

        def _parse_nsearch07_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch07_en = _parse_nsearch07_en(d.pop("NSEARCH07_EN", UNSET))

        def _parse_nsearch07_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch07_tc = _parse_nsearch07_tc(d.pop("NSEARCH07_TC", UNSET))

        def _parse_nsearch08_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch08_en = _parse_nsearch08_en(d.pop("NSEARCH08_EN", UNSET))

        def _parse_nsearch08_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch08_tc = _parse_nsearch08_tc(d.pop("NSEARCH08_TC", UNSET))

        def _parse_nsearch09_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch09_en = _parse_nsearch09_en(d.pop("NSEARCH09_EN", UNSET))

        def _parse_nsearch09_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch09_tc = _parse_nsearch09_tc(d.pop("NSEARCH09_TC", UNSET))

        def _parse_nsearch10_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch10_en = _parse_nsearch10_en(d.pop("NSEARCH10_EN", UNSET))

        def _parse_nsearch10_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nsearch10_tc = _parse_nsearch10_tc(d.pop("NSEARCH10_TC", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("LATITUDE", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("LONGITUDE", UNSET))

        lastupdate = d.pop("LASTUPDATE", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            nsearch01_en=nsearch01_en,
            nsearch01_tc=nsearch01_tc,
            nsearch02_en=nsearch02_en,
            nsearch02_tc=nsearch02_tc,
            nsearch03_en=nsearch03_en,
            nsearch03_tc=nsearch03_tc,
            nsearch04_en=nsearch04_en,
            nsearch04_tc=nsearch04_tc,
            nsearch05_en=nsearch05_en,
            nsearch05_tc=nsearch05_tc,
            nsearch06_en=nsearch06_en,
            nsearch06_tc=nsearch06_tc,
            nsearch07_en=nsearch07_en,
            nsearch07_tc=nsearch07_tc,
            nsearch08_en=nsearch08_en,
            nsearch08_tc=nsearch08_tc,
            nsearch09_en=nsearch09_en,
            nsearch09_tc=nsearch09_tc,
            nsearch10_en=nsearch10_en,
            nsearch10_tc=nsearch10_tc,
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
