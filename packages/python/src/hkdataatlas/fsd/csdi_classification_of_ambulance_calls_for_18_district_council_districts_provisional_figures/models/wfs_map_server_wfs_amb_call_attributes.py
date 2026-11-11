from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsAmbCallAttributes")


@_attrs_define
class WfsMapServerWfsAmbCallAttributes:
    """
    Attributes:
        object_identifier (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        geometry (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred
            from its XML type.
        sname (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        year_month (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        fire (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        special_services (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        ambulance (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        total (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    object_identifier: int | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    geometry: Any | Unset = UNSET
    sname: None | str | Unset = UNSET
    year_month: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    fire: float | None | Unset = UNSET
    special_services: float | None | Unset = UNSET
    ambulance: float | None | Unset = UNSET
    total: float | None | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_identifier = self.object_identifier

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        geometry = self.geometry

        sname: None | str | Unset
        if isinstance(self.sname, Unset):
            sname = UNSET
        else:
            sname = self.sname

        year_month: None | str | Unset
        if isinstance(self.year_month, Unset):
            year_month = UNSET
        else:
            year_month = self.year_month

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        fire: float | None | Unset
        if isinstance(self.fire, Unset):
            fire = UNSET
        else:
            fire = self.fire

        special_services: float | None | Unset
        if isinstance(self.special_services, Unset):
            special_services = UNSET
        else:
            special_services = self.special_services

        ambulance: float | None | Unset
        if isinstance(self.ambulance, Unset):
            ambulance = UNSET
        else:
            ambulance = self.ambulance

        total: float | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if object_identifier is not UNSET:
            field_dict["object_identifier"] = object_identifier
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if geometry is not UNSET:
            field_dict["geometry"] = geometry
        if sname is not UNSET:
            field_dict["SNAME"] = sname
        if year_month is not UNSET:
            field_dict["Year_Month"] = year_month
        if district is not UNSET:
            field_dict["District"] = district
        if fire is not UNSET:
            field_dict["Fire"] = fire
        if special_services is not UNSET:
            field_dict["Special_Services"] = special_services
        if ambulance is not UNSET:
            field_dict["Ambulance"] = ambulance
        if total is not UNSET:
            field_dict["Total"] = total
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        object_identifier = d.pop("object_identifier", UNSET)

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        geometry = d.pop("geometry", UNSET)

        def _parse_sname(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sname = _parse_sname(d.pop("SNAME", UNSET))

        def _parse_year_month(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_month = _parse_year_month(d.pop("Year_Month", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("District", UNSET))

        def _parse_fire(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fire = _parse_fire(d.pop("Fire", UNSET))

        def _parse_special_services(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        special_services = _parse_special_services(d.pop("Special_Services", UNSET))

        def _parse_ambulance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        ambulance = _parse_ambulance(d.pop("Ambulance", UNSET))

        def _parse_total(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total = _parse_total(d.pop("Total", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("SHAPE_Area", UNSET))

        wfs_map_server_wfs_amb_call_attributes = cls(
            object_identifier=object_identifier,
            district_tc=district_tc,
            geometry=geometry,
            sname=sname,
            year_month=year_month,
            district=district,
            fire=fire,
            special_services=special_services,
            ambulance=ambulance,
            total=total,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_amb_call_attributes.additional_properties = d
        return wfs_map_server_wfs_amb_call_attributes

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
