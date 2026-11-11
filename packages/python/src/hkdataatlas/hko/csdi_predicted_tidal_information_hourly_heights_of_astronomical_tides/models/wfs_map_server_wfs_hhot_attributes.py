from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsHHOTAttributes")


@_attrs_define
class WfsMapServerWfsHHOTAttributes:
    """
    Attributes:
        predicted_hourly_heights_url_2026 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        predicted_hourly_heights_url_2027 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        predicted_hourly_heights_url_2028 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        tide_station_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        tide_station_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        tide_station_uc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    predicted_hourly_heights_url_2026: None | str | Unset = UNSET
    predicted_hourly_heights_url_2027: None | str | Unset = UNSET
    predicted_hourly_heights_url_2028: None | str | Unset = UNSET
    tide_station_en: None | str | Unset = UNSET
    tide_station_sc: None | str | Unset = UNSET
    tide_station_uc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        predicted_hourly_heights_url_2026: None | str | Unset
        if isinstance(self.predicted_hourly_heights_url_2026, Unset):
            predicted_hourly_heights_url_2026 = UNSET
        else:
            predicted_hourly_heights_url_2026 = self.predicted_hourly_heights_url_2026

        predicted_hourly_heights_url_2027: None | str | Unset
        if isinstance(self.predicted_hourly_heights_url_2027, Unset):
            predicted_hourly_heights_url_2027 = UNSET
        else:
            predicted_hourly_heights_url_2027 = self.predicted_hourly_heights_url_2027

        predicted_hourly_heights_url_2028: None | str | Unset
        if isinstance(self.predicted_hourly_heights_url_2028, Unset):
            predicted_hourly_heights_url_2028 = UNSET
        else:
            predicted_hourly_heights_url_2028 = self.predicted_hourly_heights_url_2028

        tide_station_en: None | str | Unset
        if isinstance(self.tide_station_en, Unset):
            tide_station_en = UNSET
        else:
            tide_station_en = self.tide_station_en

        tide_station_sc: None | str | Unset
        if isinstance(self.tide_station_sc, Unset):
            tide_station_sc = UNSET
        else:
            tide_station_sc = self.tide_station_sc

        tide_station_uc: None | str | Unset
        if isinstance(self.tide_station_uc, Unset):
            tide_station_uc = UNSET
        else:
            tide_station_uc = self.tide_station_uc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if predicted_hourly_heights_url_2026 is not UNSET:
            field_dict["PredictedHourlyHeights_url_2026"] = (
                predicted_hourly_heights_url_2026
            )
        if predicted_hourly_heights_url_2027 is not UNSET:
            field_dict["PredictedHourlyHeights_url_2027"] = (
                predicted_hourly_heights_url_2027
            )
        if predicted_hourly_heights_url_2028 is not UNSET:
            field_dict["PredictedHourlyHeights_url_2028"] = (
                predicted_hourly_heights_url_2028
            )
        if tide_station_en is not UNSET:
            field_dict["TideStation_en"] = tide_station_en
        if tide_station_sc is not UNSET:
            field_dict["TideStation_sc"] = tide_station_sc
        if tide_station_uc is not UNSET:
            field_dict["TideStation_uc"] = tide_station_uc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_predicted_hourly_heights_url_2026(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        predicted_hourly_heights_url_2026 = _parse_predicted_hourly_heights_url_2026(
            d.pop("PredictedHourlyHeights_url_2026", UNSET)
        )

        def _parse_predicted_hourly_heights_url_2027(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        predicted_hourly_heights_url_2027 = _parse_predicted_hourly_heights_url_2027(
            d.pop("PredictedHourlyHeights_url_2027", UNSET)
        )

        def _parse_predicted_hourly_heights_url_2028(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        predicted_hourly_heights_url_2028 = _parse_predicted_hourly_heights_url_2028(
            d.pop("PredictedHourlyHeights_url_2028", UNSET)
        )

        def _parse_tide_station_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tide_station_en = _parse_tide_station_en(d.pop("TideStation_en", UNSET))

        def _parse_tide_station_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tide_station_sc = _parse_tide_station_sc(d.pop("TideStation_sc", UNSET))

        def _parse_tide_station_uc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tide_station_uc = _parse_tide_station_uc(d.pop("TideStation_uc", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_hhot_attributes = cls(
            predicted_hourly_heights_url_2026=predicted_hourly_heights_url_2026,
            predicted_hourly_heights_url_2027=predicted_hourly_heights_url_2027,
            predicted_hourly_heights_url_2028=predicted_hourly_heights_url_2028,
            tide_station_en=tide_station_en,
            tide_station_sc=tide_station_sc,
            tide_station_uc=tide_station_uc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_hhot_attributes.additional_properties = d
        return wfs_map_server_wfs_hhot_attributes

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
