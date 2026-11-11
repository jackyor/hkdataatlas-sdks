from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsLocationsofJourneyTimeIndicatorsAttributes")


@_attrs_define
class WfsMapServerWfsLocationsofJourneyTimeIndicatorsAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        location_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        location_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        location_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        location_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        destination_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        destination_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        destination_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        destination_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    location_id: None | str | Unset = UNSET
    location_name_en: None | str | Unset = UNSET
    location_name_tc: None | str | Unset = UNSET
    location_name_sc: None | str | Unset = UNSET
    destination_id: None | str | Unset = UNSET
    destination_name_en: None | str | Unset = UNSET
    destination_name_tc: None | str | Unset = UNSET
    destination_name_sc: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        location_id: None | str | Unset
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        location_name_en: None | str | Unset
        if isinstance(self.location_name_en, Unset):
            location_name_en = UNSET
        else:
            location_name_en = self.location_name_en

        location_name_tc: None | str | Unset
        if isinstance(self.location_name_tc, Unset):
            location_name_tc = UNSET
        else:
            location_name_tc = self.location_name_tc

        location_name_sc: None | str | Unset
        if isinstance(self.location_name_sc, Unset):
            location_name_sc = UNSET
        else:
            location_name_sc = self.location_name_sc

        destination_id: None | str | Unset
        if isinstance(self.destination_id, Unset):
            destination_id = UNSET
        else:
            destination_id = self.destination_id

        destination_name_en: None | str | Unset
        if isinstance(self.destination_name_en, Unset):
            destination_name_en = UNSET
        else:
            destination_name_en = self.destination_name_en

        destination_name_tc: None | str | Unset
        if isinstance(self.destination_name_tc, Unset):
            destination_name_tc = UNSET
        else:
            destination_name_tc = self.destination_name_tc

        destination_name_sc: None | str | Unset
        if isinstance(self.destination_name_sc, Unset):
            destination_name_sc = UNSET
        else:
            destination_name_sc = self.destination_name_sc

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if location_id is not UNSET:
            field_dict["location_id"] = location_id
        if location_name_en is not UNSET:
            field_dict["location_name_en"] = location_name_en
        if location_name_tc is not UNSET:
            field_dict["location_name_tc"] = location_name_tc
        if location_name_sc is not UNSET:
            field_dict["location_name_sc"] = location_name_sc
        if destination_id is not UNSET:
            field_dict["destination_id"] = destination_id
        if destination_name_en is not UNSET:
            field_dict["destination_name_en"] = destination_name_en
        if destination_name_tc is not UNSET:
            field_dict["destination_name_tc"] = destination_name_tc
        if destination_name_sc is not UNSET:
            field_dict["destination_name_sc"] = destination_name_sc
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("SHAPE", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_location_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_id = _parse_location_id(d.pop("location_id", UNSET))

        def _parse_location_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_name_en = _parse_location_name_en(d.pop("location_name_en", UNSET))

        def _parse_location_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_name_tc = _parse_location_name_tc(d.pop("location_name_tc", UNSET))

        def _parse_location_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_name_sc = _parse_location_name_sc(d.pop("location_name_sc", UNSET))

        def _parse_destination_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_id = _parse_destination_id(d.pop("destination_id", UNSET))

        def _parse_destination_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_name_en = _parse_destination_name_en(
            d.pop("destination_name_en", UNSET)
        )

        def _parse_destination_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_name_tc = _parse_destination_name_tc(
            d.pop("destination_name_tc", UNSET)
        )

        def _parse_destination_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_name_sc = _parse_destination_name_sc(
            d.pop("destination_name_sc", UNSET)
        )

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        wfs_map_server_wfs_locationsof_journey_time_indicators_attributes = cls(
            shape=shape,
            objectid=objectid,
            location_id=location_id,
            location_name_en=location_name_en,
            location_name_tc=location_name_tc,
            location_name_sc=location_name_sc,
            destination_id=destination_id,
            destination_name_en=destination_name_en,
            destination_name_tc=destination_name_tc,
            destination_name_sc=destination_name_sc,
            url=url,
        )

        wfs_map_server_wfs_locationsof_journey_time_indicators_attributes.additional_properties = d
        return wfs_map_server_wfs_locationsof_journey_time_indicators_attributes

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
