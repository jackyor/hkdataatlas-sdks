from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsfaeaec20260902Attributes")


@_attrs_define
class WfsMapServerWfsfaeaec20260902Attributes:
    """
    Attributes:
        dataset_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        course_provider_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        course_provider_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        telephone_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        northing (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        easting (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        latitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        longitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        lastupdate (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML occurrence
            into all JSON queries.
        fid (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    dataset_en: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    course_provider_en: None | str | Unset = UNSET
    course_provider_tc: None | str | Unset = UNSET
    telephone_number: None | str | Unset = UNSET
    northing: None | str | Unset = UNSET
    easting: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    lastupdate: None | str | Unset = UNSET
    fid: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
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

        course_provider_en: None | str | Unset
        if isinstance(self.course_provider_en, Unset):
            course_provider_en = UNSET
        else:
            course_provider_en = self.course_provider_en

        course_provider_tc: None | str | Unset
        if isinstance(self.course_provider_tc, Unset):
            course_provider_tc = UNSET
        else:
            course_provider_tc = self.course_provider_tc

        telephone_number: None | str | Unset
        if isinstance(self.telephone_number, Unset):
            telephone_number = UNSET
        else:
            telephone_number = self.telephone_number

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

        fid: None | str | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        objectid = self.objectid

        shape = self.shape

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
        if course_provider_en is not UNSET:
            field_dict["COURSE_PROVIDER_EN"] = course_provider_en
        if course_provider_tc is not UNSET:
            field_dict["COURSE_PROVIDER_TC"] = course_provider_tc
        if telephone_number is not UNSET:
            field_dict["TELEPHONE_NUMBER"] = telephone_number
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
        if fid is not UNSET:
            field_dict["fid"] = fid
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

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

        def _parse_course_provider_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        course_provider_en = _parse_course_provider_en(
            d.pop("COURSE_PROVIDER_EN", UNSET)
        )

        def _parse_course_provider_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        course_provider_tc = _parse_course_provider_tc(
            d.pop("COURSE_PROVIDER_TC", UNSET)
        )

        def _parse_telephone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        telephone_number = _parse_telephone_number(d.pop("TELEPHONE_NUMBER", UNSET))

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

        def _parse_fid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsfaeaec_20260902_attributes = cls(
            dataset_en=dataset_en,
            dataset_tc=dataset_tc,
            name_en=name_en,
            address_en=address_en,
            name_tc=name_tc,
            address_tc=address_tc,
            course_provider_en=course_provider_en,
            course_provider_tc=course_provider_tc,
            telephone_number=telephone_number,
            northing=northing,
            easting=easting,
            latitude=latitude,
            longitude=longitude,
            lastupdate=lastupdate,
            fid=fid,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsfaeaec_20260902_attributes.additional_properties = d
        return wfs_map_server_wfsfaeaec_20260902_attributes

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
