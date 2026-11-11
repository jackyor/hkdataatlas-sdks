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
        center_address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        center_address_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        center_address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        center_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        center_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        center_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    center_address_en: None | str | Unset = UNSET
    center_address_sc: None | str | Unset = UNSET
    center_address_tc: None | str | Unset = UNSET
    center_name_en: None | str | Unset = UNSET
    center_name_sc: None | str | Unset = UNSET
    center_name_tc: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        center_address_en: None | str | Unset
        if isinstance(self.center_address_en, Unset):
            center_address_en = UNSET
        else:
            center_address_en = self.center_address_en

        center_address_sc: None | str | Unset
        if isinstance(self.center_address_sc, Unset):
            center_address_sc = UNSET
        else:
            center_address_sc = self.center_address_sc

        center_address_tc: None | str | Unset
        if isinstance(self.center_address_tc, Unset):
            center_address_tc = UNSET
        else:
            center_address_tc = self.center_address_tc

        center_name_en: None | str | Unset
        if isinstance(self.center_name_en, Unset):
            center_name_en = UNSET
        else:
            center_name_en = self.center_name_en

        center_name_sc: None | str | Unset
        if isinstance(self.center_name_sc, Unset):
            center_name_sc = UNSET
        else:
            center_name_sc = self.center_name_sc

        center_name_tc: None | str | Unset
        if isinstance(self.center_name_tc, Unset):
            center_name_tc = UNSET
        else:
            center_name_tc = self.center_name_tc

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
        if center_address_en is not UNSET:
            field_dict["Center_Address_EN"] = center_address_en
        if center_address_sc is not UNSET:
            field_dict["Center_Address_SC"] = center_address_sc
        if center_address_tc is not UNSET:
            field_dict["Center_Address_TC"] = center_address_tc
        if center_name_en is not UNSET:
            field_dict["Center_Name_EN"] = center_name_en
        if center_name_sc is not UNSET:
            field_dict["Center_Name_SC"] = center_name_sc
        if center_name_tc is not UNSET:
            field_dict["Center_Name_TC"] = center_name_tc
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

        def _parse_center_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        center_address_en = _parse_center_address_en(d.pop("Center_Address_EN", UNSET))

        def _parse_center_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        center_address_sc = _parse_center_address_sc(d.pop("Center_Address_SC", UNSET))

        def _parse_center_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        center_address_tc = _parse_center_address_tc(d.pop("Center_Address_TC", UNSET))

        def _parse_center_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        center_name_en = _parse_center_name_en(d.pop("Center_Name_EN", UNSET))

        def _parse_center_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        center_name_sc = _parse_center_name_sc(d.pop("Center_Name_SC", UNSET))

        def _parse_center_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        center_name_tc = _parse_center_name_tc(d.pop("Center_Name_TC", UNSET))

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

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            center_address_en=center_address_en,
            center_address_sc=center_address_sc,
            center_address_tc=center_address_tc,
            center_name_en=center_name_en,
            center_name_sc=center_name_sc,
            center_name_tc=center_name_tc,
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
