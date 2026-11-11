from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsSiteWindAvailabilityDataAttributes")


@_attrs_define
class WfsMapServerWfsSiteWindAvailabilityDataAttributes:
    """
    Attributes:
        annual_500 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        annual_300 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        annual_200 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        winter_500 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        winter_300 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        winter_200 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        summer_500 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        summer_300 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        summer_200 (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    annual_500: None | str | Unset = UNSET
    annual_300: None | str | Unset = UNSET
    annual_200: None | str | Unset = UNSET
    winter_500: None | str | Unset = UNSET
    winter_300: None | str | Unset = UNSET
    winter_200: None | str | Unset = UNSET
    summer_500: None | str | Unset = UNSET
    summer_300: None | str | Unset = UNSET
    summer_200: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        annual_500: None | str | Unset
        if isinstance(self.annual_500, Unset):
            annual_500 = UNSET
        else:
            annual_500 = self.annual_500

        annual_300: None | str | Unset
        if isinstance(self.annual_300, Unset):
            annual_300 = UNSET
        else:
            annual_300 = self.annual_300

        annual_200: None | str | Unset
        if isinstance(self.annual_200, Unset):
            annual_200 = UNSET
        else:
            annual_200 = self.annual_200

        winter_500: None | str | Unset
        if isinstance(self.winter_500, Unset):
            winter_500 = UNSET
        else:
            winter_500 = self.winter_500

        winter_300: None | str | Unset
        if isinstance(self.winter_300, Unset):
            winter_300 = UNSET
        else:
            winter_300 = self.winter_300

        winter_200: None | str | Unset
        if isinstance(self.winter_200, Unset):
            winter_200 = UNSET
        else:
            winter_200 = self.winter_200

        summer_500: None | str | Unset
        if isinstance(self.summer_500, Unset):
            summer_500 = UNSET
        else:
            summer_500 = self.summer_500

        summer_300: None | str | Unset
        if isinstance(self.summer_300, Unset):
            summer_300 = UNSET
        else:
            summer_300 = self.summer_300

        summer_200: None | str | Unset
        if isinstance(self.summer_200, Unset):
            summer_200 = UNSET
        else:
            summer_200 = self.summer_200

        objectid = self.objectid

        shape = self.shape

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
        if annual_500 is not UNSET:
            field_dict["annual_500"] = annual_500
        if annual_300 is not UNSET:
            field_dict["annual_300"] = annual_300
        if annual_200 is not UNSET:
            field_dict["annual_200"] = annual_200
        if winter_500 is not UNSET:
            field_dict["winter_500"] = winter_500
        if winter_300 is not UNSET:
            field_dict["winter_300"] = winter_300
        if winter_200 is not UNSET:
            field_dict["winter_200"] = winter_200
        if summer_500 is not UNSET:
            field_dict["summer_500"] = summer_500
        if summer_300 is not UNSET:
            field_dict["summer_300"] = summer_300
        if summer_200 is not UNSET:
            field_dict["summer_200"] = summer_200
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_annual_500(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annual_500 = _parse_annual_500(d.pop("annual_500", UNSET))

        def _parse_annual_300(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annual_300 = _parse_annual_300(d.pop("annual_300", UNSET))

        def _parse_annual_200(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        annual_200 = _parse_annual_200(d.pop("annual_200", UNSET))

        def _parse_winter_500(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        winter_500 = _parse_winter_500(d.pop("winter_500", UNSET))

        def _parse_winter_300(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        winter_300 = _parse_winter_300(d.pop("winter_300", UNSET))

        def _parse_winter_200(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        winter_200 = _parse_winter_200(d.pop("winter_200", UNSET))

        def _parse_summer_500(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summer_500 = _parse_summer_500(d.pop("summer_500", UNSET))

        def _parse_summer_300(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summer_300 = _parse_summer_300(d.pop("summer_300", UNSET))

        def _parse_summer_200(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summer_200 = _parse_summer_200(d.pop("summer_200", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

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

        wfs_map_server_wfs_site_wind_availability_data_attributes = cls(
            annual_500=annual_500,
            annual_300=annual_300,
            annual_200=annual_200,
            winter_500=winter_500,
            winter_300=winter_300,
            winter_200=winter_200,
            summer_500=summer_500,
            summer_300=summer_300,
            summer_200=summer_200,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_site_wind_availability_data_attributes.additional_properties = d
        return wfs_map_server_wfs_site_wind_availability_data_attributes

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
