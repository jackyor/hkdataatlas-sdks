from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfshpinternetAttributes")


@_attrs_define
class WfsMapServerWfshpinternetAttributes:
    """
    Attributes:
        fid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        hp_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        plan_area (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        max_ed (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        new_no (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        orig_fid (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
    """

    fid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    hp_no: None | str | Unset = UNSET
    plan_area: int | None | Unset = UNSET
    max_ed: int | None | Unset = UNSET
    new_no: None | str | Unset = UNSET
    orig_fid: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fid = self.fid

        shape = self.shape

        hp_no: None | str | Unset
        if isinstance(self.hp_no, Unset):
            hp_no = UNSET
        else:
            hp_no = self.hp_no

        plan_area: int | None | Unset
        if isinstance(self.plan_area, Unset):
            plan_area = UNSET
        else:
            plan_area = self.plan_area

        max_ed: int | None | Unset
        if isinstance(self.max_ed, Unset):
            max_ed = UNSET
        else:
            max_ed = self.max_ed

        new_no: None | str | Unset
        if isinstance(self.new_no, Unset):
            new_no = UNSET
        else:
            new_no = self.new_no

        orig_fid: int | None | Unset
        if isinstance(self.orig_fid, Unset):
            orig_fid = UNSET
        else:
            orig_fid = self.orig_fid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fid is not UNSET:
            field_dict["FID"] = fid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if hp_no is not UNSET:
            field_dict["HP_NO"] = hp_no
        if plan_area is not UNSET:
            field_dict["Plan_Area"] = plan_area
        if max_ed is not UNSET:
            field_dict["Max_ED"] = max_ed
        if new_no is not UNSET:
            field_dict["New_No"] = new_no
        if orig_fid is not UNSET:
            field_dict["ORIG_FID"] = orig_fid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fid = d.pop("FID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_hp_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hp_no = _parse_hp_no(d.pop("HP_NO", UNSET))

        def _parse_plan_area(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        plan_area = _parse_plan_area(d.pop("Plan_Area", UNSET))

        def _parse_max_ed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ed = _parse_max_ed(d.pop("Max_ED", UNSET))

        def _parse_new_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_no = _parse_new_no(d.pop("New_No", UNSET))

        def _parse_orig_fid(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        orig_fid = _parse_orig_fid(d.pop("ORIG_FID", UNSET))

        wfs_map_server_wfshpinternet_attributes = cls(
            fid=fid,
            shape=shape,
            hp_no=hp_no,
            plan_area=plan_area,
            max_ed=max_ed,
            new_no=new_no,
            orig_fid=orig_fid,
        )

        wfs_map_server_wfshpinternet_attributes.additional_properties = d
        return wfs_map_server_wfshpinternet_attributes

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
