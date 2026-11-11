from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        en_land_boundary_control_points (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        en_quarter (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        en_vehicle (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        en_vehicular_throughput_000 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        en_year (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        latitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        longitude (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        sc_land_boundary_control_points (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        sc_quarter (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        sc_vehicle (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        sc_vehicular_throughput_000 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        sc_year (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        tc_land_boundary_control_points (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        tc_quarter (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        tc_vehicle (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        tc_vehicular_throughput_000 (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        tc_year (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    en_land_boundary_control_points: None | str | Unset = UNSET
    en_quarter: None | str | Unset = UNSET
    en_vehicle: None | str | Unset = UNSET
    en_vehicular_throughput_000: None | str | Unset = UNSET
    en_year: float | None | Unset = UNSET
    latitude: float | None | Unset = UNSET
    longitude: float | None | Unset = UNSET
    sc_land_boundary_control_points: None | str | Unset = UNSET
    sc_quarter: None | str | Unset = UNSET
    sc_vehicle: None | str | Unset = UNSET
    sc_vehicular_throughput_000: None | str | Unset = UNSET
    sc_year: float | None | Unset = UNSET
    tc_land_boundary_control_points: None | str | Unset = UNSET
    tc_quarter: None | str | Unset = UNSET
    tc_vehicle: None | str | Unset = UNSET
    tc_vehicular_throughput_000: None | str | Unset = UNSET
    tc_year: float | None | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        en_land_boundary_control_points: None | str | Unset
        if isinstance(self.en_land_boundary_control_points, Unset):
            en_land_boundary_control_points = UNSET
        else:
            en_land_boundary_control_points = self.en_land_boundary_control_points

        en_quarter: None | str | Unset
        if isinstance(self.en_quarter, Unset):
            en_quarter = UNSET
        else:
            en_quarter = self.en_quarter

        en_vehicle: None | str | Unset
        if isinstance(self.en_vehicle, Unset):
            en_vehicle = UNSET
        else:
            en_vehicle = self.en_vehicle

        en_vehicular_throughput_000: None | str | Unset
        if isinstance(self.en_vehicular_throughput_000, Unset):
            en_vehicular_throughput_000 = UNSET
        else:
            en_vehicular_throughput_000 = self.en_vehicular_throughput_000

        en_year: float | None | Unset
        if isinstance(self.en_year, Unset):
            en_year = UNSET
        else:
            en_year = self.en_year

        latitude: float | None | Unset
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: float | None | Unset
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        sc_land_boundary_control_points: None | str | Unset
        if isinstance(self.sc_land_boundary_control_points, Unset):
            sc_land_boundary_control_points = UNSET
        else:
            sc_land_boundary_control_points = self.sc_land_boundary_control_points

        sc_quarter: None | str | Unset
        if isinstance(self.sc_quarter, Unset):
            sc_quarter = UNSET
        else:
            sc_quarter = self.sc_quarter

        sc_vehicle: None | str | Unset
        if isinstance(self.sc_vehicle, Unset):
            sc_vehicle = UNSET
        else:
            sc_vehicle = self.sc_vehicle

        sc_vehicular_throughput_000: None | str | Unset
        if isinstance(self.sc_vehicular_throughput_000, Unset):
            sc_vehicular_throughput_000 = UNSET
        else:
            sc_vehicular_throughput_000 = self.sc_vehicular_throughput_000

        sc_year: float | None | Unset
        if isinstance(self.sc_year, Unset):
            sc_year = UNSET
        else:
            sc_year = self.sc_year

        tc_land_boundary_control_points: None | str | Unset
        if isinstance(self.tc_land_boundary_control_points, Unset):
            tc_land_boundary_control_points = UNSET
        else:
            tc_land_boundary_control_points = self.tc_land_boundary_control_points

        tc_quarter: None | str | Unset
        if isinstance(self.tc_quarter, Unset):
            tc_quarter = UNSET
        else:
            tc_quarter = self.tc_quarter

        tc_vehicle: None | str | Unset
        if isinstance(self.tc_vehicle, Unset):
            tc_vehicle = UNSET
        else:
            tc_vehicle = self.tc_vehicle

        tc_vehicular_throughput_000: None | str | Unset
        if isinstance(self.tc_vehicular_throughput_000, Unset):
            tc_vehicular_throughput_000 = UNSET
        else:
            tc_vehicular_throughput_000 = self.tc_vehicular_throughput_000

        tc_year: float | None | Unset
        if isinstance(self.tc_year, Unset):
            tc_year = UNSET
        else:
            tc_year = self.tc_year

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if en_land_boundary_control_points is not UNSET:
            field_dict["en_land_boundary_control_points"] = (
                en_land_boundary_control_points
            )
        if en_quarter is not UNSET:
            field_dict["en_quarter"] = en_quarter
        if en_vehicle is not UNSET:
            field_dict["en_vehicle"] = en_vehicle
        if en_vehicular_throughput_000 is not UNSET:
            field_dict["en_vehicular_throughput__000"] = en_vehicular_throughput_000
        if en_year is not UNSET:
            field_dict["en_year"] = en_year
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if sc_land_boundary_control_points is not UNSET:
            field_dict["sc_land_boundary_control_points"] = (
                sc_land_boundary_control_points
            )
        if sc_quarter is not UNSET:
            field_dict["sc_quarter"] = sc_quarter
        if sc_vehicle is not UNSET:
            field_dict["sc_vehicle"] = sc_vehicle
        if sc_vehicular_throughput_000 is not UNSET:
            field_dict["sc_vehicular_throughput__000"] = sc_vehicular_throughput_000
        if sc_year is not UNSET:
            field_dict["sc_year"] = sc_year
        if tc_land_boundary_control_points is not UNSET:
            field_dict["tc_land_boundary_control_points"] = (
                tc_land_boundary_control_points
            )
        if tc_quarter is not UNSET:
            field_dict["tc_quarter"] = tc_quarter
        if tc_vehicle is not UNSET:
            field_dict["tc_vehicle"] = tc_vehicle
        if tc_vehicular_throughput_000 is not UNSET:
            field_dict["tc_vehicular_throughput__000"] = tc_vehicular_throughput_000
        if tc_year is not UNSET:
            field_dict["tc_year"] = tc_year
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_en_land_boundary_control_points(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_land_boundary_control_points = _parse_en_land_boundary_control_points(
            d.pop("en_land_boundary_control_points", UNSET)
        )

        def _parse_en_quarter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_quarter = _parse_en_quarter(d.pop("en_quarter", UNSET))

        def _parse_en_vehicle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_vehicle = _parse_en_vehicle(d.pop("en_vehicle", UNSET))

        def _parse_en_vehicular_throughput_000(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        en_vehicular_throughput_000 = _parse_en_vehicular_throughput_000(
            d.pop("en_vehicular_throughput__000", UNSET)
        )

        def _parse_en_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        en_year = _parse_en_year(d.pop("en_year", UNSET))

        def _parse_latitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_sc_land_boundary_control_points(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_land_boundary_control_points = _parse_sc_land_boundary_control_points(
            d.pop("sc_land_boundary_control_points", UNSET)
        )

        def _parse_sc_quarter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_quarter = _parse_sc_quarter(d.pop("sc_quarter", UNSET))

        def _parse_sc_vehicle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_vehicle = _parse_sc_vehicle(d.pop("sc_vehicle", UNSET))

        def _parse_sc_vehicular_throughput_000(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sc_vehicular_throughput_000 = _parse_sc_vehicular_throughput_000(
            d.pop("sc_vehicular_throughput__000", UNSET)
        )

        def _parse_sc_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sc_year = _parse_sc_year(d.pop("sc_year", UNSET))

        def _parse_tc_land_boundary_control_points(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_land_boundary_control_points = _parse_tc_land_boundary_control_points(
            d.pop("tc_land_boundary_control_points", UNSET)
        )

        def _parse_tc_quarter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_quarter = _parse_tc_quarter(d.pop("tc_quarter", UNSET))

        def _parse_tc_vehicle(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_vehicle = _parse_tc_vehicle(d.pop("tc_vehicle", UNSET))

        def _parse_tc_vehicular_throughput_000(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tc_vehicular_throughput_000 = _parse_tc_vehicular_throughput_000(
            d.pop("tc_vehicular_throughput__000", UNSET)
        )

        def _parse_tc_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        tc_year = _parse_tc_year(d.pop("tc_year", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            en_land_boundary_control_points=en_land_boundary_control_points,
            en_quarter=en_quarter,
            en_vehicle=en_vehicle,
            en_vehicular_throughput_000=en_vehicular_throughput_000,
            en_year=en_year,
            latitude=latitude,
            longitude=longitude,
            sc_land_boundary_control_points=sc_land_boundary_control_points,
            sc_quarter=sc_quarter,
            sc_vehicle=sc_vehicle,
            sc_vehicular_throughput_000=sc_vehicular_throughput_000,
            sc_year=sc_year,
            tc_land_boundary_control_points=tc_land_boundary_control_points,
            tc_quarter=tc_quarter,
            tc_vehicle=tc_vehicle,
            tc_vehicular_throughput_000=tc_vehicular_throughput_000,
            tc_year=tc_year,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
