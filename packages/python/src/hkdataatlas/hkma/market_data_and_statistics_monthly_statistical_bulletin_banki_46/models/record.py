from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Record")


@_attrs_define
class Record:
    """
    Attributes:
        end_of_month (datetime.date | Unset):
        ndi_obs_exposures (float | Unset):
        obs_exposures (float | Unset):
        lending_total (float | Unset):
    """

    end_of_month: datetime.date | Unset = UNSET
    ndi_obs_exposures: float | Unset = UNSET
    obs_exposures: float | Unset = UNSET
    lending_total: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_of_month: str | Unset = UNSET
        if not isinstance(self.end_of_month, Unset):
            end_of_month = self.end_of_month.isoformat()

        ndi_obs_exposures = self.ndi_obs_exposures

        obs_exposures = self.obs_exposures

        lending_total = self.lending_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_of_month is not UNSET:
            field_dict["end_of_month"] = end_of_month
        if ndi_obs_exposures is not UNSET:
            field_dict["ndi_obs_exposures"] = ndi_obs_exposures
        if obs_exposures is not UNSET:
            field_dict["obs_exposures"] = obs_exposures
        if lending_total is not UNSET:
            field_dict["lending_total"] = lending_total

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _end_of_month = d.pop("end_of_month", UNSET)
        end_of_month: datetime.date | Unset
        if isinstance(_end_of_month, Unset):
            end_of_month = UNSET
        else:
            end_of_month = datetime.date.fromisoformat(_end_of_month)

        ndi_obs_exposures = d.pop("ndi_obs_exposures", UNSET)

        obs_exposures = d.pop("obs_exposures", UNSET)

        lending_total = d.pop("lending_total", UNSET)

        record = cls(
            end_of_month=end_of_month,
            ndi_obs_exposures=ndi_obs_exposures,
            obs_exposures=obs_exposures,
            lending_total=lending_total,
        )

        record.additional_properties = d
        return record

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
