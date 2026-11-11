from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meeting_info import MeetingInfo


T = TypeVar("T", bound="GetMeetingAgendaItemsResponse200")


@_attrs_define
class GetMeetingAgendaItemsResponse200:
    """Retained OData JSON uses an object envelope with value-array records and optional metadata/nextLink strings. The
    dictionary describes records; it does not establish universal envelope-field requiredness.

        Attributes:
            odata_metadata (str | Unset):
            value (list[MeetingInfo] | Unset):
            odata_next_link (str | Unset):
    """

    odata_metadata: str | Unset = UNSET
    value: list[MeetingInfo] | Unset = UNSET
    odata_next_link: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        odata_metadata = self.odata_metadata

        value: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item = value_item_data.to_dict()
                value.append(value_item)

        odata_next_link = self.odata_next_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if odata_metadata is not UNSET:
            field_dict["odata.metadata"] = odata_metadata
        if value is not UNSET:
            field_dict["value"] = value
        if odata_next_link is not UNSET:
            field_dict["odata.nextLink"] = odata_next_link

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.meeting_info import MeetingInfo

        d = dict(src_dict)
        odata_metadata = d.pop("odata.metadata", UNSET)

        _value = d.pop("value", UNSET)
        value: list[MeetingInfo] | Unset = UNSET
        if _value is not UNSET:
            value = []
            for value_item_data in _value:
                value_item = MeetingInfo.from_dict(value_item_data)

                value.append(value_item)

        odata_next_link = d.pop("odata.nextLink", UNSET)

        get_meeting_agenda_items_response_200 = cls(
            odata_metadata=odata_metadata,
            value=value,
            odata_next_link=odata_next_link,
        )

        get_meeting_agenda_items_response_200.additional_properties = d
        return get_meeting_agenda_items_response_200

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
