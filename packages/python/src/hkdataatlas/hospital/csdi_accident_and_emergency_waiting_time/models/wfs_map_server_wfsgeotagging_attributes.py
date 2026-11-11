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
        json_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        json_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        json_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        hosp_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        hosp_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        hosp_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    json_en: None | str | Unset = UNSET
    json_sc: None | str | Unset = UNSET
    json_tc: None | str | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    hosp_name_en: None | str | Unset = UNSET
    hosp_name_sc: None | str | Unset = UNSET
    hosp_name_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        json_en: None | str | Unset
        if isinstance(self.json_en, Unset):
            json_en = UNSET
        else:
            json_en = self.json_en

        json_sc: None | str | Unset
        if isinstance(self.json_sc, Unset):
            json_sc = UNSET
        else:
            json_sc = self.json_sc

        json_tc: None | str | Unset
        if isinstance(self.json_tc, Unset):
            json_tc = UNSET
        else:
            json_tc = self.json_tc

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

        hosp_name_en: None | str | Unset
        if isinstance(self.hosp_name_en, Unset):
            hosp_name_en = UNSET
        else:
            hosp_name_en = self.hosp_name_en

        hosp_name_sc: None | str | Unset
        if isinstance(self.hosp_name_sc, Unset):
            hosp_name_sc = UNSET
        else:
            hosp_name_sc = self.hosp_name_sc

        hosp_name_tc: None | str | Unset
        if isinstance(self.hosp_name_tc, Unset):
            hosp_name_tc = UNSET
        else:
            hosp_name_tc = self.hosp_name_tc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if json_en is not UNSET:
            field_dict["JSON_EN"] = json_en
        if json_sc is not UNSET:
            field_dict["JSON_SC"] = json_sc
        if json_tc is not UNSET:
            field_dict["JSON_TC"] = json_tc
        if latitude is not UNSET:
            field_dict["LATITUDE"] = latitude
        if longitude is not UNSET:
            field_dict["LONGITUDE"] = longitude
        if hosp_name_en is not UNSET:
            field_dict["hospName_EN"] = hosp_name_en
        if hosp_name_sc is not UNSET:
            field_dict["hospName_SC"] = hosp_name_sc
        if hosp_name_tc is not UNSET:
            field_dict["hospName_TC"] = hosp_name_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_json_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        json_en = _parse_json_en(d.pop("JSON_EN", UNSET))

        def _parse_json_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        json_sc = _parse_json_sc(d.pop("JSON_SC", UNSET))

        def _parse_json_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        json_tc = _parse_json_tc(d.pop("JSON_TC", UNSET))

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

        def _parse_hosp_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hosp_name_en = _parse_hosp_name_en(d.pop("hospName_EN", UNSET))

        def _parse_hosp_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hosp_name_sc = _parse_hosp_name_sc(d.pop("hospName_SC", UNSET))

        def _parse_hosp_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hosp_name_tc = _parse_hosp_name_tc(d.pop("hospName_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            json_en=json_en,
            json_sc=json_sc,
            json_tc=json_tc,
            latitude=latitude,
            longitude=longitude,
            hosp_name_en=hosp_name_en,
            hosp_name_sc=hosp_name_sc,
            hosp_name_tc=hosp_name_tc,
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
