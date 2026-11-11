from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer1007Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer1007Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        aa_code (None | str | Unset): Publisher field type: esriFieldTypeString
        aa_title (None | str | Unset): Publisher field type: esriFieldTypeString
        manufacturing_workshop (float | None | Unset): Publisher field type: esriFieldTypeDouble
        warehouse_storage (float | None | Unset): Publisher field type: esriFieldTypeDouble
        office (float | None | Unset): Publisher field type: esriFieldTypeDouble
        others (float | None | Unset): Publisher field type: esriFieldTypeDouble
        vacant_under_renovation (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    aa_code: None | str | Unset = UNSET
    aa_title: None | str | Unset = UNSET
    manufacturing_workshop: float | None | Unset = UNSET
    warehouse_storage: float | None | Unset = UNSET
    office: float | None | Unset = UNSET
    others: float | None | Unset = UNSET
    vacant_under_renovation: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        aa_code: None | str | Unset
        if isinstance(self.aa_code, Unset):
            aa_code = UNSET
        else:
            aa_code = self.aa_code

        aa_title: None | str | Unset
        if isinstance(self.aa_title, Unset):
            aa_title = UNSET
        else:
            aa_title = self.aa_title

        manufacturing_workshop: float | None | Unset
        if isinstance(self.manufacturing_workshop, Unset):
            manufacturing_workshop = UNSET
        else:
            manufacturing_workshop = self.manufacturing_workshop

        warehouse_storage: float | None | Unset
        if isinstance(self.warehouse_storage, Unset):
            warehouse_storage = UNSET
        else:
            warehouse_storage = self.warehouse_storage

        office: float | None | Unset
        if isinstance(self.office, Unset):
            office = UNSET
        else:
            office = self.office

        others: float | None | Unset
        if isinstance(self.others, Unset):
            others = UNSET
        else:
            others = self.others

        vacant_under_renovation: float | None | Unset
        if isinstance(self.vacant_under_renovation, Unset):
            vacant_under_renovation = UNSET
        else:
            vacant_under_renovation = self.vacant_under_renovation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if aa_code is not UNSET:
            field_dict["AA_Code"] = aa_code
        if aa_title is not UNSET:
            field_dict["AA_Title"] = aa_title
        if manufacturing_workshop is not UNSET:
            field_dict["Manufacturing_Workshop"] = manufacturing_workshop
        if warehouse_storage is not UNSET:
            field_dict["Warehouse_Storage"] = warehouse_storage
        if office is not UNSET:
            field_dict["Office"] = office
        if others is not UNSET:
            field_dict["Others_"] = others
        if vacant_under_renovation is not UNSET:
            field_dict["Vacant_Under_renovation"] = vacant_under_renovation

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_aa_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_code = _parse_aa_code(d.pop("AA_Code", UNSET))

        def _parse_aa_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aa_title = _parse_aa_title(d.pop("AA_Title", UNSET))

        def _parse_manufacturing_workshop(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        manufacturing_workshop = _parse_manufacturing_workshop(
            d.pop("Manufacturing_Workshop", UNSET)
        )

        def _parse_warehouse_storage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        warehouse_storage = _parse_warehouse_storage(d.pop("Warehouse_Storage", UNSET))

        def _parse_office(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        office = _parse_office(d.pop("Office", UNSET))

        def _parse_others(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        others = _parse_others(d.pop("Others_", UNSET))

        def _parse_vacant_under_renovation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        vacant_under_renovation = _parse_vacant_under_renovation(
            d.pop("Vacant_Under_renovation", UNSET)
        )

        arcgis_feature_server_arcgis_layer_1007_attributes = cls(
            objectid=objectid,
            aa_code=aa_code,
            aa_title=aa_title,
            manufacturing_workshop=manufacturing_workshop,
            warehouse_storage=warehouse_storage,
            office=office,
            others=others,
            vacant_under_renovation=vacant_under_renovation,
        )

        arcgis_feature_server_arcgis_layer_1007_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_1007_attributes

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
