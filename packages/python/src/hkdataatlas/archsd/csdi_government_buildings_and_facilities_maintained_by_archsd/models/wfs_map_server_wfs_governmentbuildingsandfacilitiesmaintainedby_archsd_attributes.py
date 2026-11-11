from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="WfsMapServerWfsGovernmentbuildingsandfacilitiesmaintainedbyARCHSDAttributes",
)


@_attrs_define
class WfsMapServerWfsGovernmentbuildingsandfacilitiesmaintainedbyARCHSDAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        loc_name_eng (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        loc_name_chi (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        bldg_type (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        user_dept (str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        year_of_completion (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    loc_name_eng: str | Unset = UNSET
    loc_name_chi: str | Unset = UNSET
    bldg_type: str | Unset = UNSET
    user_dept: str | Unset = UNSET
    year_of_completion: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        loc_name_eng = self.loc_name_eng

        loc_name_chi = self.loc_name_chi

        bldg_type = self.bldg_type

        user_dept = self.user_dept

        year_of_completion: None | str | Unset
        if isinstance(self.year_of_completion, Unset):
            year_of_completion = UNSET
        else:
            year_of_completion = self.year_of_completion

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if loc_name_eng is not UNSET:
            field_dict["LOC_NAME_ENG"] = loc_name_eng
        if loc_name_chi is not UNSET:
            field_dict["LOC_NAME_CHI"] = loc_name_chi
        if bldg_type is not UNSET:
            field_dict["BLDG_TYPE"] = bldg_type
        if user_dept is not UNSET:
            field_dict["USER_DEPT"] = user_dept
        if year_of_completion is not UNSET:
            field_dict["YEAR_OF_COMPLETION"] = year_of_completion

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        loc_name_eng = d.pop("LOC_NAME_ENG", UNSET)

        loc_name_chi = d.pop("LOC_NAME_CHI", UNSET)

        bldg_type = d.pop("BLDG_TYPE", UNSET)

        user_dept = d.pop("USER_DEPT", UNSET)

        def _parse_year_of_completion(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_of_completion = _parse_year_of_completion(
            d.pop("YEAR_OF_COMPLETION", UNSET)
        )

        wfs_map_server_wfs_governmentbuildingsandfacilitiesmaintainedby_archsd_attributes = cls(
            objectid=objectid,
            shape=shape,
            loc_name_eng=loc_name_eng,
            loc_name_chi=loc_name_chi,
            bldg_type=bldg_type,
            user_dept=user_dept,
            year_of_completion=year_of_completion,
        )

        wfs_map_server_wfs_governmentbuildingsandfacilitiesmaintainedby_archsd_attributes.additional_properties = d
        return wfs_map_server_wfs_governmentbuildingsandfacilitiesmaintainedby_archsd_attributes

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
