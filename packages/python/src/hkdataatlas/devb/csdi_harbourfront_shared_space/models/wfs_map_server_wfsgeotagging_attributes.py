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
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        length_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        length_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        opening_details_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        opening_details_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        transport_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        transport_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    area_en: None | str | Unset = UNSET
    area_tc: None | str | Unset = UNSET
    length_en: None | str | Unset = UNSET
    length_tc: None | str | Unset = UNSET
    name_en: None | str | Unset = UNSET
    name_tc: None | str | Unset = UNSET
    opening_details_en: None | str | Unset = UNSET
    opening_details_tc: None | str | Unset = UNSET
    transport_en: None | str | Unset = UNSET
    transport_tc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        area_tc: None | str | Unset
        if isinstance(self.area_tc, Unset):
            area_tc = UNSET
        else:
            area_tc = self.area_tc

        length_en: None | str | Unset
        if isinstance(self.length_en, Unset):
            length_en = UNSET
        else:
            length_en = self.length_en

        length_tc: None | str | Unset
        if isinstance(self.length_tc, Unset):
            length_tc = UNSET
        else:
            length_tc = self.length_tc

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

        opening_details_en: None | str | Unset
        if isinstance(self.opening_details_en, Unset):
            opening_details_en = UNSET
        else:
            opening_details_en = self.opening_details_en

        opening_details_tc: None | str | Unset
        if isinstance(self.opening_details_tc, Unset):
            opening_details_tc = UNSET
        else:
            opening_details_tc = self.opening_details_tc

        transport_en: None | str | Unset
        if isinstance(self.transport_en, Unset):
            transport_en = UNSET
        else:
            transport_en = self.transport_en

        transport_tc: None | str | Unset
        if isinstance(self.transport_tc, Unset):
            transport_tc = UNSET
        else:
            transport_tc = self.transport_tc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area_en is not UNSET:
            field_dict["Area_EN"] = area_en
        if area_tc is not UNSET:
            field_dict["Area_TC"] = area_tc
        if length_en is not UNSET:
            field_dict["Length_EN"] = length_en
        if length_tc is not UNSET:
            field_dict["Length_TC"] = length_tc
        if name_en is not UNSET:
            field_dict["Name_EN"] = name_en
        if name_tc is not UNSET:
            field_dict["Name_TC"] = name_tc
        if opening_details_en is not UNSET:
            field_dict["Opening_Details_EN"] = opening_details_en
        if opening_details_tc is not UNSET:
            field_dict["Opening_Details_TC"] = opening_details_tc
        if transport_en is not UNSET:
            field_dict["Transport_EN"] = transport_en
        if transport_tc is not UNSET:
            field_dict["Transport_TC"] = transport_tc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("Area_EN", UNSET))

        def _parse_area_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_tc = _parse_area_tc(d.pop("Area_TC", UNSET))

        def _parse_length_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        length_en = _parse_length_en(d.pop("Length_EN", UNSET))

        def _parse_length_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        length_tc = _parse_length_tc(d.pop("Length_TC", UNSET))

        def _parse_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_en = _parse_name_en(d.pop("Name_EN", UNSET))

        def _parse_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_tc = _parse_name_tc(d.pop("Name_TC", UNSET))

        def _parse_opening_details_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_details_en = _parse_opening_details_en(
            d.pop("Opening_Details_EN", UNSET)
        )

        def _parse_opening_details_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        opening_details_tc = _parse_opening_details_tc(
            d.pop("Opening_Details_TC", UNSET)
        )

        def _parse_transport_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transport_en = _parse_transport_en(d.pop("Transport_EN", UNSET))

        def _parse_transport_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transport_tc = _parse_transport_tc(d.pop("Transport_TC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            area_en=area_en,
            area_tc=area_tc,
            length_en=length_en,
            length_tc=length_tc,
            name_en=name_en,
            name_tc=name_tc,
            opening_details_en=opening_details_en,
            opening_details_tc=opening_details_tc,
            transport_en=transport_en,
            transport_tc=transport_tc,
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
