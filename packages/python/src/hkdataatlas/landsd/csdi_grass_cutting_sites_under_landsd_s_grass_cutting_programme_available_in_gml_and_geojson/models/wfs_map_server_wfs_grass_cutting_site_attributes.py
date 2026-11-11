from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsGrassCuttingSiteAttributes")


@_attrs_define
class WfsMapServerWfsGrassCuttingSiteAttributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        site_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        english_location (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        chinese_location (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        dlo (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        site_ref_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        estimated_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        year (int | None | Unset): Native XSD type xsd:short. Requiredness is not projected from XML occurrence into all
            JSON queries.
        quarter (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        english_remarks (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        chinese_remarks (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    site_number: None | str | Unset = UNSET
    english_location: None | str | Unset = UNSET
    chinese_location: None | str | Unset = UNSET
    dlo: None | str | Unset = UNSET
    site_ref_number: None | str | Unset = UNSET
    estimated_area: float | None | Unset = UNSET
    year: int | None | Unset = UNSET
    quarter: None | str | Unset = UNSET
    english_remarks: None | str | Unset = UNSET
    chinese_remarks: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        shape = self.shape

        site_number: None | str | Unset
        if isinstance(self.site_number, Unset):
            site_number = UNSET
        else:
            site_number = self.site_number

        english_location: None | str | Unset
        if isinstance(self.english_location, Unset):
            english_location = UNSET
        else:
            english_location = self.english_location

        chinese_location: None | str | Unset
        if isinstance(self.chinese_location, Unset):
            chinese_location = UNSET
        else:
            chinese_location = self.chinese_location

        dlo: None | str | Unset
        if isinstance(self.dlo, Unset):
            dlo = UNSET
        else:
            dlo = self.dlo

        site_ref_number: None | str | Unset
        if isinstance(self.site_ref_number, Unset):
            site_ref_number = UNSET
        else:
            site_ref_number = self.site_ref_number

        estimated_area: float | None | Unset
        if isinstance(self.estimated_area, Unset):
            estimated_area = UNSET
        else:
            estimated_area = self.estimated_area

        year: int | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        quarter: None | str | Unset
        if isinstance(self.quarter, Unset):
            quarter = UNSET
        else:
            quarter = self.quarter

        english_remarks: None | str | Unset
        if isinstance(self.english_remarks, Unset):
            english_remarks = UNSET
        else:
            english_remarks = self.english_remarks

        chinese_remarks: None | str | Unset
        if isinstance(self.chinese_remarks, Unset):
            chinese_remarks = UNSET
        else:
            chinese_remarks = self.chinese_remarks

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
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["Shape"] = shape
        if site_number is not UNSET:
            field_dict["SiteNumber"] = site_number
        if english_location is not UNSET:
            field_dict["EnglishLocation"] = english_location
        if chinese_location is not UNSET:
            field_dict["ChineseLocation"] = chinese_location
        if dlo is not UNSET:
            field_dict["DLO"] = dlo
        if site_ref_number is not UNSET:
            field_dict["SiteRefNumber"] = site_ref_number
        if estimated_area is not UNSET:
            field_dict["EstimatedArea"] = estimated_area
        if year is not UNSET:
            field_dict["Year"] = year
        if quarter is not UNSET:
            field_dict["Quarter"] = quarter
        if english_remarks is not UNSET:
            field_dict["EnglishRemarks"] = english_remarks
        if chinese_remarks is not UNSET:
            field_dict["ChineseRemarks"] = chinese_remarks
        if shape_length is not UNSET:
            field_dict["Shape_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("Shape", UNSET)

        def _parse_site_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_number = _parse_site_number(d.pop("SiteNumber", UNSET))

        def _parse_english_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_location = _parse_english_location(d.pop("EnglishLocation", UNSET))

        def _parse_chinese_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_location = _parse_chinese_location(d.pop("ChineseLocation", UNSET))

        def _parse_dlo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dlo = _parse_dlo(d.pop("DLO", UNSET))

        def _parse_site_ref_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_ref_number = _parse_site_ref_number(d.pop("SiteRefNumber", UNSET))

        def _parse_estimated_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        estimated_area = _parse_estimated_area(d.pop("EstimatedArea", UNSET))

        def _parse_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        year = _parse_year(d.pop("Year", UNSET))

        def _parse_quarter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quarter = _parse_quarter(d.pop("Quarter", UNSET))

        def _parse_english_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        english_remarks = _parse_english_remarks(d.pop("EnglishRemarks", UNSET))

        def _parse_chinese_remarks(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chinese_remarks = _parse_chinese_remarks(d.pop("ChineseRemarks", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape_Area", UNSET))

        wfs_map_server_wfs_grass_cutting_site_attributes = cls(
            objectid=objectid,
            shape=shape,
            site_number=site_number,
            english_location=english_location,
            chinese_location=chinese_location,
            dlo=dlo,
            site_ref_number=site_ref_number,
            estimated_area=estimated_area,
            year=year,
            quarter=quarter,
            english_remarks=english_remarks,
            chinese_remarks=chinese_remarks,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_grass_cutting_site_attributes.additional_properties = d
        return wfs_map_server_wfs_grass_cutting_site_attributes

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
