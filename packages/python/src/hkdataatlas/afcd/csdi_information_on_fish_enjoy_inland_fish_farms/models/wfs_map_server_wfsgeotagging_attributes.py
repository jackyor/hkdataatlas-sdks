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
        farm_name_ch (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        farm_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid_1 (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    farm_name_ch: None | str | Unset = UNSET
    farm_name_en: None | str | Unset = UNSET
    objectid: float | None | Unset = UNSET
    objectid_1: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        farm_name_ch: None | str | Unset
        if isinstance(self.farm_name_ch, Unset):
            farm_name_ch = UNSET
        else:
            farm_name_ch = self.farm_name_ch

        farm_name_en: None | str | Unset
        if isinstance(self.farm_name_en, Unset):
            farm_name_en = UNSET
        else:
            farm_name_en = self.farm_name_en

        objectid: float | None | Unset
        if isinstance(self.objectid, Unset):
            objectid = UNSET
        else:
            objectid = self.objectid

        objectid_1 = self.objectid_1

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if farm_name_ch is not UNSET:
            field_dict["FarmNameCH"] = farm_name_ch
        if farm_name_en is not UNSET:
            field_dict["FarmNameEN"] = farm_name_en
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if objectid_1 is not UNSET:
            field_dict["OBJECTID_1"] = objectid_1
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_farm_name_ch(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        farm_name_ch = _parse_farm_name_ch(d.pop("FarmNameCH", UNSET))

        def _parse_farm_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        farm_name_en = _parse_farm_name_en(d.pop("FarmNameEN", UNSET))

        def _parse_objectid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        objectid = _parse_objectid(d.pop("OBJECTID", UNSET))

        objectid_1 = d.pop("OBJECTID_1", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            farm_name_ch=farm_name_ch,
            farm_name_en=farm_name_en,
            objectid=objectid,
            objectid_1=objectid_1,
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
