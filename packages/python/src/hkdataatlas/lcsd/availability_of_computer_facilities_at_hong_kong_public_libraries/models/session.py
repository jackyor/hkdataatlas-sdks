from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workstation_group import WorkstationGroup


T = TypeVar("T", bound="Session")


@_attrs_define
class Session:
    """A session object containing the documented session fields.

    Attributes:
        session_end (str | Unset): The session end date and time, in "YYYY-MM-DD hh24:mm:ss" format.
        session_start (str | Unset): The session start date and time, in "YYYY-MM-DD hh24:mm:ss" format.
        workstation_group (list[WorkstationGroup] | Unset): An array of workstation group objects.
    """

    session_end: str | Unset = UNSET
    session_start: str | Unset = UNSET
    workstation_group: list[WorkstationGroup] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        session_end = self.session_end

        session_start = self.session_start

        workstation_group: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.workstation_group, Unset):
            workstation_group = []
            for workstation_group_item_data in self.workstation_group:
                workstation_group_item = workstation_group_item_data.to_dict()
                workstation_group.append(workstation_group_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if session_end is not UNSET:
            field_dict["sessionEnd"] = session_end
        if session_start is not UNSET:
            field_dict["sessionStart"] = session_start
        if workstation_group is not UNSET:
            field_dict["workstationGroup"] = workstation_group

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.workstation_group import WorkstationGroup

        d = dict(src_dict)
        session_end = d.pop("sessionEnd", UNSET)

        session_start = d.pop("sessionStart", UNSET)

        _workstation_group = d.pop("workstationGroup", UNSET)
        workstation_group: list[WorkstationGroup] | Unset = UNSET
        if _workstation_group is not UNSET:
            workstation_group = []
            for workstation_group_item_data in _workstation_group:
                workstation_group_item = WorkstationGroup.from_dict(
                    workstation_group_item_data
                )

                workstation_group.append(workstation_group_item)

        session = cls(
            session_end=session_end,
            session_start=session_start,
            workstation_group=workstation_group,
        )

        session.additional_properties = d
        return session

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
