from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        fmsc (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        gop (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        primary_care (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        facility_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        facility_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        facility_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        fin_yr (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    fmsc: float | None | Unset = UNSET
    gop: float | None | Unset = UNSET
    primary_care: float | None | Unset = UNSET
    facility_en: None | str | Unset = UNSET
    facility_sc: None | str | Unset = UNSET
    facility_tc: None | str | Unset = UNSET
    fin_yr: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fmsc: float | None | Unset
        if isinstance(self.fmsc, Unset):
            fmsc = UNSET
        else:
            fmsc = self.fmsc

        gop: float | None | Unset
        if isinstance(self.gop, Unset):
            gop = UNSET
        else:
            gop = self.gop

        primary_care: float | None | Unset
        if isinstance(self.primary_care, Unset):
            primary_care = UNSET
        else:
            primary_care = self.primary_care

        facility_en: None | str | Unset
        if isinstance(self.facility_en, Unset):
            facility_en = UNSET
        else:
            facility_en = self.facility_en

        facility_sc: None | str | Unset
        if isinstance(self.facility_sc, Unset):
            facility_sc = UNSET
        else:
            facility_sc = self.facility_sc

        facility_tc: None | str | Unset
        if isinstance(self.facility_tc, Unset):
            facility_tc = UNSET
        else:
            facility_tc = self.facility_tc

        fin_yr: None | str | Unset
        if isinstance(self.fin_yr, Unset):
            fin_yr = UNSET
        else:
            fin_yr = self.fin_yr

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

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fmsc is not UNSET:
            field_dict["FMSC"] = fmsc
        if gop is not UNSET:
            field_dict["GOP"] = gop
        if primary_care is not UNSET:
            field_dict["PrimaryCare"] = primary_care
        if facility_en is not UNSET:
            field_dict["facility_en"] = facility_en
        if facility_sc is not UNSET:
            field_dict["facility_sc"] = facility_sc
        if facility_tc is not UNSET:
            field_dict["facility_tc"] = facility_tc
        if fin_yr is not UNSET:
            field_dict["fin_yr"] = fin_yr
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_fmsc(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fmsc = _parse_fmsc(d.pop("FMSC", UNSET))

        def _parse_gop(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        gop = _parse_gop(d.pop("GOP", UNSET))

        def _parse_primary_care(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        primary_care = _parse_primary_care(d.pop("PrimaryCare", UNSET))

        def _parse_facility_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_en = _parse_facility_en(d.pop("facility_en", UNSET))

        def _parse_facility_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_sc = _parse_facility_sc(d.pop("facility_sc", UNSET))

        def _parse_facility_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_tc = _parse_facility_tc(d.pop("facility_tc", UNSET))

        def _parse_fin_yr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fin_yr = _parse_fin_yr(d.pop("fin_yr", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            fmsc=fmsc,
            gop=gop,
            primary_care=primary_care,
            facility_en=facility_en,
            facility_sc=facility_sc,
            facility_tc=facility_tc,
            fin_yr=fin_yr,
            latitude=latitude,
            longitude=longitude,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
