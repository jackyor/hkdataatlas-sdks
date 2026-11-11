from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeodatastoreAttributes")


@_attrs_define
class WfsMapServerWfsgeodatastoreAttributes:
    """
    Attributes:
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dataset_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        lastupdate (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        nsearch01_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch01_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch02_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch02_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch03_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch03_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch04_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch04_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch05_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch05_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch06_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        nsearch06_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        no_of_squash_courts_en (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        no_of_squash_courts_tc (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from
            XML occurrence into all JSON queries.
        search01_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        search01_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        search02_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        search02_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        easting_lands (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        latitude_lands (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        longitude_lands (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        northing_lands (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    lastupdate: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    northing: float | None | Unset = UNSET
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
    no_of_squash_courts_en: float | None | Unset = UNSET
    no_of_squash_courts_tc: float | None | Unset = UNSET
    search01_en: None | str | Unset = UNSET
    search01_tc: None | str | Unset = UNSET
    search02_en: None | str | Unset = UNSET
    search02_tc: None | str | Unset = UNSET
    easting_lands: float | None | Unset = UNSET
    latitude_lands: float | None | Unset = UNSET
    longitude_lands: float | None | Unset = UNSET
    northing_lands: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

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

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        lastupdate: None | str | Unset
        if isinstance(self.lastupdate, Unset):
            lastupdate = UNSET
        else:
            lastupdate = self.lastupdate

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

        name_en: None | str | Unset
        if isinstance(self.name_en, Unset):
            name_en = UNSET
        else:
            name_en = self.name_en

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

        no_of_squash_courts_en: float | None | Unset
        if isinstance(self.no_of_squash_courts_en, Unset):
            no_of_squash_courts_en = UNSET
        else:
            no_of_squash_courts_en = self.no_of_squash_courts_en

        no_of_squash_courts_tc: float | None | Unset
        if isinstance(self.no_of_squash_courts_tc, Unset):
            no_of_squash_courts_tc = UNSET
        else:
            no_of_squash_courts_tc = self.no_of_squash_courts_tc

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

        search02_en: None | str | Unset
        if isinstance(self.search02_en, Unset):
            search02_en = UNSET
        else:
            search02_en = self.search02_en

        search02_tc: None | str | Unset
        if isinstance(self.search02_tc, Unset):
            search02_tc = UNSET
        else:
            search02_tc = self.search02_tc

        easting_lands: float | None | Unset
        if isinstance(self.easting_lands, Unset):
            easting_lands = UNSET
        else:
            easting_lands = self.easting_lands

        latitude_lands: float | None | Unset
        if isinstance(self.latitude_lands, Unset):
            latitude_lands = UNSET
        else:
            latitude_lands = self.latitude_lands

        longitude_lands: float | None | Unset
        if isinstance(self.longitude_lands, Unset):
            longitude_lands = UNSET
        else:
            longitude_lands = self.longitude_lands

        northing_lands: float | None | Unset
        if isinstance(self.northing_lands, Unset):
            northing_lands = UNSET
        else:
            northing_lands = self.northing_lands

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_en is not UNSET:
            field_dict["ADDRESS_EN"] = address_en
        if address_tc is not UNSET:
            field_dict["ADDRESS_TC"] = address_tc
        if dataset_en is not UNSET:
            field_dict["DATASET_EN"] = dataset_en
        if dataset_tc is not UNSET:
            field_dict["DATASET_TC"] = dataset_tc
        if easting is not UNSET:
            field_dict["EASTING"] = easting
        if lastupdate is not UNSET:
            field_dict["LASTUPDATE"] = lastupdate
        if latitude is not UNSET:
            field_dict["LATITUDE"] = latitude
        if longitude is not UNSET:
            field_dict["LONGITUDE"] = longitude
        if name_en is not UNSET:
            field_dict["NAME_EN"] = name_en
        if name_tc is not UNSET:
            field_dict["NAME_TC"] = name_tc
        if northing is not UNSET:
            field_dict["NORTHING"] = northing
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
        if no_of_squash_courts_en is not UNSET:
            field_dict["No__of_Squash_Courts_EN"] = no_of_squash_courts_en
        if no_of_squash_courts_tc is not UNSET:
            field_dict["No__of_Squash_Courts_TC"] = no_of_squash_courts_tc
        if search01_en is not UNSET:
            field_dict["SEARCH01_EN"] = search01_en
        if search01_tc is not UNSET:
            field_dict["SEARCH01_TC"] = search01_tc
        if search02_en is not UNSET:
            field_dict["SEARCH02_EN"] = search02_en
        if search02_tc is not UNSET:
            field_dict["SEARCH02_TC"] = search02_tc
        if easting_lands is not UNSET:
            field_dict["easting_lands"] = easting_lands
        if latitude_lands is not UNSET:
            field_dict["latitude_lands"] = latitude_lands
        if longitude_lands is not UNSET:
            field_dict["longitude_lands"] = longitude_lands
        if northing_lands is not UNSET:
            field_dict["northing_lands"] = northing_lands
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

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

        address_en = _parse_address_en(d.pop("ADDRESS_EN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("ADDRESS_TC", UNSET))

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

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("EASTING", UNSET))

        def _parse_lastupdate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lastupdate = _parse_lastupdate(d.pop("LASTUPDATE", UNSET))

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

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("NAME_EN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("NAME_TC", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("NORTHING", UNSET))

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

        def _parse_no_of_squash_courts_en(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_of_squash_courts_en = _parse_no_of_squash_courts_en(
            d.pop("No__of_Squash_Courts_EN", UNSET)
        )

        def _parse_no_of_squash_courts_tc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_of_squash_courts_tc = _parse_no_of_squash_courts_tc(
            d.pop("No__of_Squash_Courts_TC", UNSET)
        )

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

        def _parse_search02_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search02_en = _parse_search02_en(d.pop("SEARCH02_EN", UNSET))

        def _parse_search02_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        search02_tc = _parse_search02_tc(d.pop("SEARCH02_TC", UNSET))

        def _parse_easting_lands(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting_lands = _parse_easting_lands(d.pop("easting_lands", UNSET))

        def _parse_latitude_lands(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude_lands = _parse_latitude_lands(d.pop("latitude_lands", UNSET))

        def _parse_longitude_lands(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude_lands = _parse_longitude_lands(d.pop("longitude_lands", UNSET))

        def _parse_northing_lands(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing_lands = _parse_northing_lands(d.pop("northing_lands", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeodatastore_attributes = cls(
            address_en=address_en,
            address_tc=address_tc,
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            easting=easting,
            lastupdate=lastupdate,
            latitude=latitude,
            longitude=longitude,
            name_en=name_en,
            name_tc=name_tc,
            northing=northing,
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
            no_of_squash_courts_en=no_of_squash_courts_en,
            no_of_squash_courts_tc=no_of_squash_courts_tc,
            search01_en=search01_en,
            search01_tc=search01_tc,
            search02_en=search02_en,
            search02_tc=search02_tc,
            easting_lands=easting_lands,
            latitude_lands=latitude_lands,
            longitude_lands=longitude_lands,
            northing_lands=northing_lands,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeodatastore_attributes.additional_properties = d
        return wfs_map_server_wfsgeodatastore_attributes

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
