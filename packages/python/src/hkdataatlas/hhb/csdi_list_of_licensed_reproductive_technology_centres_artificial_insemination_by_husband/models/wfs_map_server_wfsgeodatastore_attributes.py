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
        address_of_premises (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        name_of_centre_in_alphabetical_order (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        easting (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        northing (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    address_of_premises: None | str | Unset = UNSET
    name_of_centre_in_alphabetical_order: None | str | Unset = UNSET
    easting: float | None | Unset = UNSET
    northing: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address_of_premises: None | str | Unset
        if isinstance(self.address_of_premises, Unset):
            address_of_premises = UNSET
        else:
            address_of_premises = self.address_of_premises

        name_of_centre_in_alphabetical_order: None | str | Unset
        if isinstance(self.name_of_centre_in_alphabetical_order, Unset):
            name_of_centre_in_alphabetical_order = UNSET
        else:
            name_of_centre_in_alphabetical_order = (
                self.name_of_centre_in_alphabetical_order
            )

        easting: float | None | Unset
        if isinstance(self.easting, Unset):
            easting = UNSET
        else:
            easting = self.easting

        northing: float | None | Unset
        if isinstance(self.northing, Unset):
            northing = UNSET
        else:
            northing = self.northing

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_of_premises is not UNSET:
            field_dict["Address_of_premises"] = address_of_premises
        if name_of_centre_in_alphabetical_order is not UNSET:
            field_dict["Name_of_centre__in_alphabetical_order_"] = (
                name_of_centre_in_alphabetical_order
            )
        if easting is not UNSET:
            field_dict["easting"] = easting
        if northing is not UNSET:
            field_dict["northing"] = northing
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_address_of_premises(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_of_premises = _parse_address_of_premises(
            d.pop("Address_of_premises", UNSET)
        )

        def _parse_name_of_centre_in_alphabetical_order(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_of_centre_in_alphabetical_order = (
            _parse_name_of_centre_in_alphabetical_order(
                d.pop("Name_of_centre__in_alphabetical_order_", UNSET)
            )
        )

        def _parse_easting(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting = _parse_easting(d.pop("easting", UNSET))

        def _parse_northing(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing = _parse_northing(d.pop("northing", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeodatastore_attributes = cls(
            address_of_premises=address_of_premises,
            name_of_centre_in_alphabetical_order=name_of_centre_in_alphabetical_order,
            easting=easting,
            northing=northing,
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
