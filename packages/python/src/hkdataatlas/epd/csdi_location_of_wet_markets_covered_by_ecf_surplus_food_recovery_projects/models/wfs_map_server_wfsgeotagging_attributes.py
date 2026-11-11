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
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        market_address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        market_address_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        market_address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        market_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        market_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        market_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    market_address_en: None | str | Unset = UNSET
    market_address_sc: None | str | Unset = UNSET
    market_address_tc: None | str | Unset = UNSET
    market_name_en: None | str | Unset = UNSET
    market_name_sc: None | str | Unset = UNSET
    market_name_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        market_address_en: None | str | Unset
        if isinstance(self.market_address_en, Unset):
            market_address_en = UNSET
        else:
            market_address_en = self.market_address_en

        market_address_sc: None | str | Unset
        if isinstance(self.market_address_sc, Unset):
            market_address_sc = UNSET
        else:
            market_address_sc = self.market_address_sc

        market_address_tc: None | str | Unset
        if isinstance(self.market_address_tc, Unset):
            market_address_tc = UNSET
        else:
            market_address_tc = self.market_address_tc

        market_name_en: None | str | Unset
        if isinstance(self.market_name_en, Unset):
            market_name_en = UNSET
        else:
            market_name_en = self.market_name_en

        market_name_sc: None | str | Unset
        if isinstance(self.market_name_sc, Unset):
            market_name_sc = UNSET
        else:
            market_name_sc = self.market_name_sc

        market_name_tc: None | str | Unset
        if isinstance(self.market_name_tc, Unset):
            market_name_tc = UNSET
        else:
            market_name_tc = self.market_name_tc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["Latitude"] = latitude
        if longitude is not UNSET:
            field_dict["Longitude"] = longitude
        if market_address_en is not UNSET:
            field_dict["Market_Address_EN"] = market_address_en
        if market_address_sc is not UNSET:
            field_dict["Market_Address_SC"] = market_address_sc
        if market_address_tc is not UNSET:
            field_dict["Market_Address_TC"] = market_address_tc
        if market_name_en is not UNSET:
            field_dict["Market_Name_EN"] = market_name_en
        if market_name_sc is not UNSET:
            field_dict["Market_Name_SC"] = market_name_sc
        if market_name_tc is not UNSET:
            field_dict["Market_Name_TC"] = market_name_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

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

        def _parse_market_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        market_address_en = _parse_market_address_en(d.pop("Market_Address_EN", UNSET))

        def _parse_market_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        market_address_sc = _parse_market_address_sc(d.pop("Market_Address_SC", UNSET))

        def _parse_market_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        market_address_tc = _parse_market_address_tc(d.pop("Market_Address_TC", UNSET))

        def _parse_market_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        market_name_en = _parse_market_name_en(d.pop("Market_Name_EN", UNSET))

        def _parse_market_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        market_name_sc = _parse_market_name_sc(d.pop("Market_Name_SC", UNSET))

        def _parse_market_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        market_name_tc = _parse_market_name_tc(d.pop("Market_Name_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            latitude=latitude,
            longitude=longitude,
            market_address_en=market_address_en,
            market_address_sc=market_address_sc,
            market_address_tc=market_address_tc,
            market_name_en=market_name_en,
            market_name_sc=market_name_sc,
            market_name_tc=market_name_tc,
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
