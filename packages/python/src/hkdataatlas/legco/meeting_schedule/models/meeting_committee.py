from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.committee import Committee


T = TypeVar("T", bound="MeetingCommittee")


@_attrs_define
class MeetingCommittee:
    """Fields documented for Tmeeting_committee. The dictionary gives examples for identifiers but does not specify
    universal requiredness.

        Attributes:
            tcommittee (Committee | Unset): Fields documented for Tcommittee. No universal requiredness is specified.
            committee_id (int | Unset): Committee identifier. Dictionary example: 2608.
            meet_committee_id (int | Unset): Record identifier. Dictionary example: 10936.
            slot_id (int | Unset): Meeting slot identifier. Dictionary example: 162955.
    """

    tcommittee: Committee | Unset = UNSET
    committee_id: int | Unset = UNSET
    meet_committee_id: int | Unset = UNSET
    slot_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tcommittee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tcommittee, Unset):
            tcommittee = self.tcommittee.to_dict()

        committee_id = self.committee_id

        meet_committee_id = self.meet_committee_id

        slot_id = self.slot_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tcommittee is not UNSET:
            field_dict["Tcommittee"] = tcommittee
        if committee_id is not UNSET:
            field_dict["committee_id"] = committee_id
        if meet_committee_id is not UNSET:
            field_dict["meet_committee_id"] = meet_committee_id
        if slot_id is not UNSET:
            field_dict["slot_id"] = slot_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.committee import Committee

        d = dict(src_dict)
        _tcommittee = d.pop("Tcommittee", UNSET)
        tcommittee: Committee | Unset
        if isinstance(_tcommittee, Unset):
            tcommittee = UNSET
        else:
            tcommittee = Committee.from_dict(_tcommittee)

        committee_id = d.pop("committee_id", UNSET)

        meet_committee_id = d.pop("meet_committee_id", UNSET)

        slot_id = d.pop("slot_id", UNSET)

        meeting_committee = cls(
            tcommittee=tcommittee,
            committee_id=committee_id,
            meet_committee_id=meet_committee_id,
            slot_id=slot_id,
        )

        meeting_committee.additional_properties = d
        return meeting_committee

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
