from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsSTOPTRAMAttributes")


@_attrs_define
class WfsMapServerWfsSTOPTRAMAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        stop_id (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        last_update_date (None | str | Unset): Native XSD type xsd:dateTime. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    stop_id: int | None | Unset = UNSET
    last_update_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        stop_id: int | None | Unset
        if isinstance(self.stop_id, Unset):
            stop_id = UNSET
        else:
            stop_id = self.stop_id

        last_update_date: None | str | Unset
        if isinstance(self.last_update_date, Unset):
            last_update_date = UNSET
        else:
            last_update_date = self.last_update_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if stop_id is not UNSET:
            field_dict["STOP_ID"] = stop_id
        if last_update_date is not UNSET:
            field_dict["LAST_UPDATE_DATE"] = last_update_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("SHAPE", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_stop_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        stop_id = _parse_stop_id(d.pop("STOP_ID", UNSET))

        def _parse_last_update_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update_date = _parse_last_update_date(d.pop("LAST_UPDATE_DATE", UNSET))

        wfs_map_server_wfs_stoptram_attributes = cls(
            shape=shape,
            objectid=objectid,
            stop_id=stop_id,
            last_update_date=last_update_date,
        )

        wfs_map_server_wfs_stoptram_attributes.additional_properties = d
        return wfs_map_server_wfs_stoptram_attributes

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
