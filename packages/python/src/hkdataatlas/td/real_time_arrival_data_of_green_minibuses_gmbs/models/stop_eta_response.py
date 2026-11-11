from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stop_eta_response_type import (
    StopEtaResponseType,
    check_stop_eta_response_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stop_eta_disabled import StopEtaDisabled
    from ..models.stop_eta_enabled import StopEtaEnabled


T = TypeVar("T", bound="StopEtaResponse")


@_attrs_define
class StopEtaResponse:
    """
    Attributes:
        data (list[StopEtaDisabled | StopEtaEnabled] | Unset): Route variations serving the stop.
        generated_timestamp (datetime.datetime | Unset): Time when the response is generated, in Hong Kong Time (HKT).
        type_ (StopEtaResponseType | Unset): Entity name specified for the payload.
        version (str | Unset): API version of the response.
    """

    data: list[StopEtaDisabled | StopEtaEnabled] | Unset = UNSET
    generated_timestamp: datetime.datetime | Unset = UNSET
    type_: StopEtaResponseType | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.stop_eta_enabled import StopEtaEnabled

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item: dict[str, Any]
                if isinstance(data_item_data, StopEtaEnabled):
                    data_item = data_item_data.to_dict()
                else:
                    data_item = data_item_data.to_dict()

                data.append(data_item)

        generated_timestamp: str | Unset = UNSET
        if not isinstance(self.generated_timestamp, Unset):
            generated_timestamp = self.generated_timestamp.isoformat()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if generated_timestamp is not UNSET:
            field_dict["generated_timestamp"] = generated_timestamp
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.stop_eta_disabled import StopEtaDisabled
        from ..models.stop_eta_enabled import StopEtaEnabled

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[StopEtaDisabled | StopEtaEnabled] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:

                def _parse_data_item(data: object) -> StopEtaDisabled | StopEtaEnabled:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        data_item_type_0 = StopEtaEnabled.from_dict(data)

                        return data_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = StopEtaDisabled.from_dict(data)

                    return data_item_type_1

                data_item = _parse_data_item(data_item_data)

                data.append(data_item)

        _generated_timestamp = d.pop("generated_timestamp", UNSET)
        generated_timestamp: datetime.datetime | Unset
        if isinstance(_generated_timestamp, Unset):
            generated_timestamp = UNSET
        else:
            generated_timestamp = datetime.datetime.fromisoformat(_generated_timestamp)

        _type_ = d.pop("type", UNSET)
        type_: StopEtaResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_stop_eta_response_type(_type_)

        version = d.pop("version", UNSET)

        stop_eta_response = cls(
            data=data,
            generated_timestamp=generated_timestamp,
            type_=type_,
            version=version,
        )

        stop_eta_response.additional_properties = d
        return stop_eta_response

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
