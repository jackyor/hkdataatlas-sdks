from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.eta_response_type import EtaResponseType, check_eta_response_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.eta import Eta
    from ..models.eta_response_data_type_1 import EtaResponseDataType1


T = TypeVar("T", bound="EtaResponse")


@_attrs_define
class EtaResponse:
    """
    Attributes:
        generated_timestamp (datetime.datetime | Unset): Date-time timestamp with time zone in ISO 8601 format.
        type_ (EtaResponseType | Unset): Identifier of the API response.
        version (str | Unset): Version number of the returned JSON, in major.minor format. Example: 1.0.
        data (EtaResponseDataType1 | list[Eta] | Unset): The API examples show an array of records. The companion
            dictionary sections2.3/2.4 also explicitly say an empty data object denotes unavailable data; both documented
            representations are permitted.
    """

    generated_timestamp: datetime.datetime | Unset = UNSET
    type_: EtaResponseType | Unset = UNSET
    version: str | Unset = UNSET
    data: EtaResponseDataType1 | list[Eta] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        generated_timestamp: str | Unset = UNSET
        if not isinstance(self.generated_timestamp, Unset):
            generated_timestamp = self.generated_timestamp.isoformat()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        version = self.version

        data: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if generated_timestamp is not UNSET:
            field_dict["generated_timestamp"] = generated_timestamp
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version is not UNSET:
            field_dict["version"] = version
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.eta import Eta
        from ..models.eta_response_data_type_1 import EtaResponseDataType1

        d = dict(src_dict)
        _generated_timestamp = d.pop("generated_timestamp", UNSET)
        generated_timestamp: datetime.datetime | Unset
        if isinstance(_generated_timestamp, Unset):
            generated_timestamp = UNSET
        else:
            generated_timestamp = datetime.datetime.fromisoformat(_generated_timestamp)

        _type_ = d.pop("type", UNSET)
        type_: EtaResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_eta_response_type(_type_)

        version = d.pop("version", UNSET)

        def _parse_data(data: object) -> EtaResponseDataType1 | list[Eta] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = Eta.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = EtaResponseDataType1.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data", UNSET))

        eta_response = cls(
            generated_timestamp=generated_timestamp,
            type_=type_,
            version=version,
            data=data,
        )

        eta_response.additional_properties = d
        return eta_response

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
