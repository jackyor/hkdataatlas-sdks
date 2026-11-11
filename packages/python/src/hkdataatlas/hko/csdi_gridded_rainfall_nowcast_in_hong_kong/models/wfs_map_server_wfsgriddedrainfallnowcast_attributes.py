from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgriddedrainfallnowcastAttributes")


@_attrs_define
class WfsMapServerWfsgriddedrainfallnowcastAttributes:
    """
    Attributes:
        data_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        latitude_degree (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        longitude_degree (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    data_url: None | str | Unset = UNSET
    latitude_degree: float | None | Unset = UNSET
    longitude_degree: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data_url: None | str | Unset
        if isinstance(self.data_url, Unset):
            data_url = UNSET
        else:
            data_url = self.data_url

        latitude_degree: float | None | Unset
        if isinstance(self.latitude_degree, Unset):
            latitude_degree = UNSET
        else:
            latitude_degree = self.latitude_degree

        longitude_degree: float | None | Unset
        if isinstance(self.longitude_degree, Unset):
            longitude_degree = UNSET
        else:
            longitude_degree = self.longitude_degree

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_url is not UNSET:
            field_dict["Data_url"] = data_url
        if latitude_degree is not UNSET:
            field_dict["Latitude_degree_"] = latitude_degree
        if longitude_degree is not UNSET:
            field_dict["Longitude_degree_"] = longitude_degree
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_data_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        data_url = _parse_data_url(d.pop("Data_url", UNSET))

        def _parse_latitude_degree(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude_degree = _parse_latitude_degree(d.pop("Latitude_degree_", UNSET))

        def _parse_longitude_degree(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude_degree = _parse_longitude_degree(d.pop("Longitude_degree_", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgriddedrainfallnowcast_attributes = cls(
            data_url=data_url,
            latitude_degree=latitude_degree,
            longitude_degree=longitude_degree,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgriddedrainfallnowcast_attributes.additional_properties = d
        return wfs_map_server_wfsgriddedrainfallnowcast_attributes

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
