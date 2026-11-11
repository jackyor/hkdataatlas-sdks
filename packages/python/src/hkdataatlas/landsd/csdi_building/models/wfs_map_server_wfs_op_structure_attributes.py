from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsOPStructureAttributes")


@_attrs_define
class WfsMapServerWfsOPStructureAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        building_structure_id (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        op_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        storeys (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into
            all JSON queries.
        storeys_in_basement (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML
            occurrence into all JSON queries.
        top_height (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        storey_remarks (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        op_block_type (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        op_building_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    objectid: int | Unset = UNSET
    building_structure_id: int | Unset = UNSET
    op_no: None | str | Unset = UNSET
    storeys: int | None | Unset = UNSET
    storeys_in_basement: int | None | Unset = UNSET
    top_height: float | None | Unset = UNSET
    storey_remarks: None | str | Unset = UNSET
    op_block_type: str | Unset = UNSET
    op_building_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        building_structure_id = self.building_structure_id

        op_no: None | str | Unset
        if isinstance(self.op_no, Unset):
            op_no = UNSET
        else:
            op_no = self.op_no

        storeys: int | None | Unset
        if isinstance(self.storeys, Unset):
            storeys = UNSET
        else:
            storeys = self.storeys

        storeys_in_basement: int | None | Unset
        if isinstance(self.storeys_in_basement, Unset):
            storeys_in_basement = UNSET
        else:
            storeys_in_basement = self.storeys_in_basement

        top_height: float | None | Unset
        if isinstance(self.top_height, Unset):
            top_height = UNSET
        else:
            top_height = self.top_height

        storey_remarks: None | str | Unset
        if isinstance(self.storey_remarks, Unset):
            storey_remarks = UNSET
        else:
            storey_remarks = self.storey_remarks

        op_block_type = self.op_block_type

        op_building_type: None | str | Unset
        if isinstance(self.op_building_type, Unset):
            op_building_type = UNSET
        else:
            op_building_type = self.op_building_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if building_structure_id is not UNSET:
            field_dict["BuildingStructureID"] = building_structure_id
        if op_no is not UNSET:
            field_dict["OPNo"] = op_no
        if storeys is not UNSET:
            field_dict["Storeys"] = storeys
        if storeys_in_basement is not UNSET:
            field_dict["StoreysInBasement"] = storeys_in_basement
        if top_height is not UNSET:
            field_dict["TopHeight"] = top_height
        if storey_remarks is not UNSET:
            field_dict["StoreyRemarks"] = storey_remarks
        if op_block_type is not UNSET:
            field_dict["OPBlockType"] = op_block_type
        if op_building_type is not UNSET:
            field_dict["OPBuildingType"] = op_building_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        building_structure_id = d.pop("BuildingStructureID", UNSET)

        def _parse_op_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        op_no = _parse_op_no(d.pop("OPNo", UNSET))

        def _parse_storeys(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storeys = _parse_storeys(d.pop("Storeys", UNSET))

        def _parse_storeys_in_basement(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storeys_in_basement = _parse_storeys_in_basement(
            d.pop("StoreysInBasement", UNSET)
        )

        def _parse_top_height(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        top_height = _parse_top_height(d.pop("TopHeight", UNSET))

        def _parse_storey_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storey_remarks = _parse_storey_remarks(d.pop("StoreyRemarks", UNSET))

        op_block_type = d.pop("OPBlockType", UNSET)

        def _parse_op_building_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        op_building_type = _parse_op_building_type(d.pop("OPBuildingType", UNSET))

        wfs_map_server_wfs_op_structure_attributes = cls(
            objectid=objectid,
            building_structure_id=building_structure_id,
            op_no=op_no,
            storeys=storeys,
            storeys_in_basement=storeys_in_basement,
            top_height=top_height,
            storey_remarks=storey_remarks,
            op_block_type=op_block_type,
            op_building_type=op_building_type,
        )

        wfs_map_server_wfs_op_structure_attributes.additional_properties = d
        return wfs_map_server_wfs_op_structure_attributes

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
