from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeetingInfo")


@_attrs_define
class MeetingInfo:
    """Field specification for agenda items and time markers (VMeetingInfo). The data dictionary does not declare which
    fields are always present.

        Attributes:
            agenda_name (None | str | Unset): English agenda / subject name.
            agenda_running_time (str | Unset): Time stamp (based on running time).
            agenda_time (str | Unset): Time stamp (based on meeting time).
            chi_agenda_name (None | str | Unset): Chinese agenda / subject name.
            meeting_id (str | Unset): Meeting identifier.
            nrow (int | str | Unset): Dictionary integer item number is encoded as a decimal-digit string in every item of
                the retained response; both representations remain supported.
    """

    agenda_name: None | str | Unset = UNSET
    agenda_running_time: str | Unset = UNSET
    agenda_time: str | Unset = UNSET
    chi_agenda_name: None | str | Unset = UNSET
    meeting_id: str | Unset = UNSET
    nrow: int | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agenda_name: None | str | Unset
        if isinstance(self.agenda_name, Unset):
            agenda_name = UNSET
        else:
            agenda_name = self.agenda_name

        agenda_running_time = self.agenda_running_time

        agenda_time = self.agenda_time

        chi_agenda_name: None | str | Unset
        if isinstance(self.chi_agenda_name, Unset):
            chi_agenda_name = UNSET
        else:
            chi_agenda_name = self.chi_agenda_name

        meeting_id = self.meeting_id

        nrow: int | str | Unset
        if isinstance(self.nrow, Unset):
            nrow = UNSET
        else:
            nrow = self.nrow

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agenda_name is not UNSET:
            field_dict["AgendaName"] = agenda_name
        if agenda_running_time is not UNSET:
            field_dict["AgendaRunningTime"] = agenda_running_time
        if agenda_time is not UNSET:
            field_dict["AgendaTime"] = agenda_time
        if chi_agenda_name is not UNSET:
            field_dict["ChiAgendaName"] = chi_agenda_name
        if meeting_id is not UNSET:
            field_dict["MeetingID"] = meeting_id
        if nrow is not UNSET:
            field_dict["nrow"] = nrow

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_agenda_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agenda_name = _parse_agenda_name(d.pop("AgendaName", UNSET))

        agenda_running_time = d.pop("AgendaRunningTime", UNSET)

        agenda_time = d.pop("AgendaTime", UNSET)

        def _parse_chi_agenda_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chi_agenda_name = _parse_chi_agenda_name(d.pop("ChiAgendaName", UNSET))

        meeting_id = d.pop("MeetingID", UNSET)

        def _parse_nrow(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        nrow = _parse_nrow(d.pop("nrow", UNSET))

        meeting_info = cls(
            agenda_name=agenda_name,
            agenda_running_time=agenda_running_time,
            agenda_time=agenda_time,
            chi_agenda_name=chi_agenda_name,
            meeting_id=meeting_id,
            nrow=nrow,
        )

        meeting_info.additional_properties = d
        return meeting_info

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
