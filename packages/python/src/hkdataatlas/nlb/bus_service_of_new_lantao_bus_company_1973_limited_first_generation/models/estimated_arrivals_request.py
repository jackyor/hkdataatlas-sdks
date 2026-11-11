from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.estimated_arrivals_request_language import (
    EstimatedArrivalsRequestLanguage,
    check_estimated_arrivals_request_language,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EstimatedArrivalsRequest")


@_attrs_define
class EstimatedArrivalsRequest:
    """
    Attributes:
        language (EstimatedArrivalsRequestLanguage | Unset): Language of response content: `en` English, `zh`
            Traditional Chinese, `cn` Simplified Chinese.
        route_id (int | str | Unset): Documented as Integer; the sample request represents this identifier as a string.
        stop_id (int | str | Unset): Documented as Integer; the sample request represents this identifier as a string.
    """

    language: EstimatedArrivalsRequestLanguage | Unset = UNSET
    route_id: int | str | Unset = UNSET
    stop_id: int | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        language: str | Unset = UNSET
        if not isinstance(self.language, Unset):
            language = self.language

        route_id: int | str | Unset
        if isinstance(self.route_id, Unset):
            route_id = UNSET
        else:
            route_id = self.route_id

        stop_id: int | str | Unset
        if isinstance(self.stop_id, Unset):
            stop_id = UNSET
        else:
            stop_id = self.stop_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language is not UNSET:
            field_dict["language"] = language
        if route_id is not UNSET:
            field_dict["routeId"] = route_id
        if stop_id is not UNSET:
            field_dict["stopId"] = stop_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _language = d.pop("language", UNSET)
        language: EstimatedArrivalsRequestLanguage | Unset
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = check_estimated_arrivals_request_language(_language)

        def _parse_route_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        route_id = _parse_route_id(d.pop("routeId", UNSET))

        def _parse_stop_id(data: object) -> int | str | Unset:
            if isinstance(data, Unset):
                return data
            return cast(int | str | Unset, data)

        stop_id = _parse_stop_id(d.pop("stopId", UNSET))

        estimated_arrivals_request = cls(
            language=language,
            route_id=route_id,
            stop_id=stop_id,
        )

        estimated_arrivals_request.additional_properties = d
        return estimated_arrivals_request

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
