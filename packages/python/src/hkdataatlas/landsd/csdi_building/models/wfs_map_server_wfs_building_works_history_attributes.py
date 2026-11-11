from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsBuildingWorksHistoryAttributes")


@_attrs_define
class WfsMapServerWfsBuildingWorksHistoryAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        building_csuid (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        data_provider_id (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        works_type (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        works_date (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
    """

    objectid: int | Unset = UNSET
    building_csuid: str | Unset = UNSET
    data_provider_id: str | Unset = UNSET
    works_type: str | Unset = UNSET
    works_date: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        building_csuid = self.building_csuid

        data_provider_id = self.data_provider_id

        works_type = self.works_type

        works_date = self.works_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if building_csuid is not UNSET:
            field_dict["BuildingCSUID"] = building_csuid
        if data_provider_id is not UNSET:
            field_dict["DataProviderID"] = data_provider_id
        if works_type is not UNSET:
            field_dict["WorksType"] = works_type
        if works_date is not UNSET:
            field_dict["WorksDate"] = works_date

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        building_csuid = d.pop("BuildingCSUID", UNSET)

        data_provider_id = d.pop("DataProviderID", UNSET)

        works_type = d.pop("WorksType", UNSET)

        works_date = d.pop("WorksDate", UNSET)

        wfs_map_server_wfs_building_works_history_attributes = cls(
            objectid=objectid,
            building_csuid=building_csuid,
            data_provider_id=data_provider_id,
            works_type=works_type,
            works_date=works_date,
        )

        wfs_map_server_wfs_building_works_history_attributes.additional_properties = d
        return wfs_map_server_wfs_building_works_history_attributes

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
