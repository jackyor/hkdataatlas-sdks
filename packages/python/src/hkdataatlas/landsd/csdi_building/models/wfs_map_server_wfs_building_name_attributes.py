from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsBuildingNameAttributes")


@_attrs_define
class WfsMapServerWfsBuildingNameAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        building_csuid (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        building_name_id (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        building_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        building_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        name_status (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        data_provider_id (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
    """

    objectid: int | Unset = UNSET
    building_csuid: str | Unset = UNSET
    building_name_id: int | Unset = UNSET
    building_name_en: None | str | Unset = UNSET
    building_name_tc: None | str | Unset = UNSET
    name_status: str | Unset = UNSET
    data_provider_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        building_csuid = self.building_csuid

        building_name_id = self.building_name_id

        building_name_en: None | str | Unset
        if isinstance(self.building_name_en, Unset):
            building_name_en = UNSET
        else:
            building_name_en = self.building_name_en

        building_name_tc: None | str | Unset
        if isinstance(self.building_name_tc, Unset):
            building_name_tc = UNSET
        else:
            building_name_tc = self.building_name_tc

        name_status = self.name_status

        data_provider_id = self.data_provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if building_csuid is not UNSET:
            field_dict["BuildingCSUID"] = building_csuid
        if building_name_id is not UNSET:
            field_dict["BuildingNameID"] = building_name_id
        if building_name_en is not UNSET:
            field_dict["BuildingNameEN"] = building_name_en
        if building_name_tc is not UNSET:
            field_dict["BuildingNameTC"] = building_name_tc
        if name_status is not UNSET:
            field_dict["NameStatus"] = name_status
        if data_provider_id is not UNSET:
            field_dict["DataProviderID"] = data_provider_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        building_csuid = d.pop("BuildingCSUID", UNSET)

        building_name_id = d.pop("BuildingNameID", UNSET)

        def _parse_building_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_name_en = _parse_building_name_en(d.pop("BuildingNameEN", UNSET))

        def _parse_building_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        building_name_tc = _parse_building_name_tc(d.pop("BuildingNameTC", UNSET))

        name_status = d.pop("NameStatus", UNSET)

        data_provider_id = d.pop("DataProviderID", UNSET)

        wfs_map_server_wfs_building_name_attributes = cls(
            objectid=objectid,
            building_csuid=building_csuid,
            building_name_id=building_name_id,
            building_name_en=building_name_en,
            building_name_tc=building_name_tc,
            name_status=name_status,
            data_provider_id=data_provider_id,
        )

        wfs_map_server_wfs_building_name_attributes.additional_properties = d
        return wfs_map_server_wfs_building_name_attributes

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
