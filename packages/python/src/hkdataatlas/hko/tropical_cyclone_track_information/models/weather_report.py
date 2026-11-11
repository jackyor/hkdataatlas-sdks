from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.track_position_collection import TrackPositionCollection


T = TypeVar("T", bound="WeatherReport")


@_attrs_define
class WeatherReport:
    """
    Attributes:
        analysis_information (TrackPositionCollection | Unset): A grouping of track-position fields. The dictionary
            describes these tags but does not fully specify XML cardinality or exact nesting for repeated positions; the
            schema therefore leaves the object permissive.
        forecast_information (TrackPositionCollection | Unset): A grouping of track-position fields. The dictionary
            describes these tags but does not fully specify XML cardinality or exact nesting for repeated positions; the
            schema therefore leaves the object permissive.
        past_information (TrackPositionCollection | Unset): A grouping of track-position fields. The dictionary
            describes these tags but does not fully specify XML cardinality or exact nesting for repeated positions; the
            schema therefore leaves the object permissive.
        tropical_cyclone_name (str | Unset): Name of the tropical cyclone. If not yet named, the latest intensity
            category is given; see the Intensity values. Example: YUTU.
    """

    analysis_information: TrackPositionCollection | Unset = UNSET
    forecast_information: TrackPositionCollection | Unset = UNSET
    past_information: TrackPositionCollection | Unset = UNSET
    tropical_cyclone_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        analysis_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.analysis_information, Unset):
            analysis_information = self.analysis_information.to_dict()

        forecast_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.forecast_information, Unset):
            forecast_information = self.forecast_information.to_dict()

        past_information: dict[str, Any] | Unset = UNSET
        if not isinstance(self.past_information, Unset):
            past_information = self.past_information.to_dict()

        tropical_cyclone_name = self.tropical_cyclone_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if analysis_information is not UNSET:
            field_dict["AnalysisInformation"] = analysis_information
        if forecast_information is not UNSET:
            field_dict["ForecastInformation"] = forecast_information
        if past_information is not UNSET:
            field_dict["PastInformation"] = past_information
        if tropical_cyclone_name is not UNSET:
            field_dict["TropicalCycloneName"] = tropical_cyclone_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.track_position_collection import TrackPositionCollection

        d = dict(src_dict)
        _analysis_information = d.pop("AnalysisInformation", UNSET)
        analysis_information: TrackPositionCollection | Unset
        if isinstance(_analysis_information, Unset):
            analysis_information = UNSET
        else:
            analysis_information = TrackPositionCollection.from_dict(
                _analysis_information
            )

        _forecast_information = d.pop("ForecastInformation", UNSET)
        forecast_information: TrackPositionCollection | Unset
        if isinstance(_forecast_information, Unset):
            forecast_information = UNSET
        else:
            forecast_information = TrackPositionCollection.from_dict(
                _forecast_information
            )

        _past_information = d.pop("PastInformation", UNSET)
        past_information: TrackPositionCollection | Unset
        if isinstance(_past_information, Unset):
            past_information = UNSET
        else:
            past_information = TrackPositionCollection.from_dict(_past_information)

        tropical_cyclone_name = d.pop("TropicalCycloneName", UNSET)

        weather_report = cls(
            analysis_information=analysis_information,
            forecast_information=forecast_information,
            past_information=past_information,
            tropical_cyclone_name=tropical_cyclone_name,
        )

        weather_report.additional_properties = d
        return weather_report

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
