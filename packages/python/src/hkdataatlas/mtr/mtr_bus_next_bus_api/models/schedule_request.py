from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.schedule_request_language import (
    ScheduleRequestLanguage,
    check_schedule_request_language,
)
from ..models.schedule_request_route_name import (
    ScheduleRequestRouteName,
    check_schedule_request_route_name,
)

T = TypeVar("T", bound="ScheduleRequest")


@_attrs_define
class ScheduleRequest:
    """The publisher says a valid result is returned only when both language and routeName are correct.

    Attributes:
        language (ScheduleRequestLanguage): Language selection.
        route_name (ScheduleRequestRouteName): Selected route name. The listed routes can have multiple directions or
            variants under the same routeName. The list is not a statement of current availability.
    """

    language: ScheduleRequestLanguage
    route_name: ScheduleRequestRouteName
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language: str = self.language

        route_name: str = self.route_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "language": language,
                "routeName": route_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        language = check_schedule_request_language(d.pop("language"))

        route_name = check_schedule_request_route_name(d.pop("routeName"))

        schedule_request = cls(
            language=language,
            route_name=route_name,
        )

        schedule_request.additional_properties = d
        return schedule_request

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
