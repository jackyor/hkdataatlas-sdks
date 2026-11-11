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
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        walking_track_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        walking_track_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        walking_track_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        total_length_m (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        latitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        longitude (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    district_en: None | str | Unset = UNSET
    walking_track_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    walking_track_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    walking_track_sc: None | str | Unset = UNSET
    total_length_m: None | str | Unset = UNSET
    latitude: None | str | Unset = UNSET
    longitude: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        walking_track_en: None | str | Unset
        if isinstance(self.walking_track_en, Unset):
            walking_track_en = UNSET
        else:
            walking_track_en = self.walking_track_en

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        walking_track_tc: None | str | Unset
        if isinstance(self.walking_track_tc, Unset):
            walking_track_tc = UNSET
        else:
            walking_track_tc = self.walking_track_tc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        walking_track_sc: None | str | Unset
        if isinstance(self.walking_track_sc, Unset):
            walking_track_sc = UNSET
        else:
            walking_track_sc = self.walking_track_sc

        total_length_m: None | str | Unset
        if isinstance(self.total_length_m, Unset):
            total_length_m = UNSET
        else:
            total_length_m = self.total_length_m

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

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if district_en is not UNSET:
            field_dict["District_EN"] = district_en
        if walking_track_en is not UNSET:
            field_dict["Walking_Track_EN"] = walking_track_en
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if walking_track_tc is not UNSET:
            field_dict["Walking_Track_TC"] = walking_track_tc
        if district_sc is not UNSET:
            field_dict["District_SC"] = district_sc
        if walking_track_sc is not UNSET:
            field_dict["Walking_Track_SC"] = walking_track_sc
        if total_length_m is not UNSET:
            field_dict["Total_Length_M"] = total_length_m
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_EN", UNSET))

        def _parse_walking_track_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        walking_track_en = _parse_walking_track_en(d.pop("Walking_Track_EN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_walking_track_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        walking_track_tc = _parse_walking_track_tc(d.pop("Walking_Track_TC", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("District_SC", UNSET))

        def _parse_walking_track_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        walking_track_sc = _parse_walking_track_sc(d.pop("Walking_Track_SC", UNSET))

        def _parse_total_length_m(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        total_length_m = _parse_total_length_m(d.pop("Total_Length_M", UNSET))

        def _parse_latitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        latitude = _parse_latitude(d.pop("Latitude", UNSET))

        def _parse_longitude(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        longitude = _parse_longitude(d.pop("Longitude", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            district_en=district_en,
            walking_track_en=walking_track_en,
            district_tc=district_tc,
            walking_track_tc=walking_track_tc,
            district_sc=district_sc,
            walking_track_sc=walking_track_sc,
            total_length_m=total_length_m,
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
