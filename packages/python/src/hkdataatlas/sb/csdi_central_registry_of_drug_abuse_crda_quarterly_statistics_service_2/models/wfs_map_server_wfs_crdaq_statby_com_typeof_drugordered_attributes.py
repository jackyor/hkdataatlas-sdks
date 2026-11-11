from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsCRDAQStatbyComTypeofDrugorderedAttributes")


@_attrs_define
class WfsMapServerWfsCRDAQStatbyComTypeofDrugorderedAttributes:
    """
    Attributes:
        year (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        drugs (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        fid (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence into
            all JSON queries.
        quarter (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        res_district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        value (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        variable (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    year: float | None | Unset = UNSET
    district: None | str | Unset = UNSET
    drugs: None | str | Unset = UNSET
    fid: float | None | Unset = UNSET
    quarter: None | str | Unset = UNSET
    res_district: None | str | Unset = UNSET
    value: None | str | Unset = UNSET
    variable: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        year: float | None | Unset
        if isinstance(self.year, Unset):
            year = UNSET
        else:
            year = self.year

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        drugs: None | str | Unset
        if isinstance(self.drugs, Unset):
            drugs = UNSET
        else:
            drugs = self.drugs

        fid: float | None | Unset
        if isinstance(self.fid, Unset):
            fid = UNSET
        else:
            fid = self.fid

        quarter: None | str | Unset
        if isinstance(self.quarter, Unset):
            quarter = UNSET
        else:
            quarter = self.quarter

        res_district: None | str | Unset
        if isinstance(self.res_district, Unset):
            res_district = UNSET
        else:
            res_district = self.res_district

        value: None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        variable: None | str | Unset
        if isinstance(self.variable, Unset):
            variable = UNSET
        else:
            variable = self.variable

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
        if year is not UNSET:
            field_dict["Year"] = year
        if district is not UNSET:
            field_dict["district"] = district
        if drugs is not UNSET:
            field_dict["drugs"] = drugs
        if fid is not UNSET:
            field_dict["fid"] = fid
        if quarter is not UNSET:
            field_dict["quarter"] = quarter
        if res_district is not UNSET:
            field_dict["resDistrict"] = res_district
        if value is not UNSET:
            field_dict["value"] = value
        if variable is not UNSET:
            field_dict["variable"] = variable
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

        def _parse_year(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        year = _parse_year(d.pop("Year", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("district", UNSET))

        def _parse_drugs(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        drugs = _parse_drugs(d.pop("drugs", UNSET))

        def _parse_fid(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        fid = _parse_fid(d.pop("fid", UNSET))

        def _parse_quarter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quarter = _parse_quarter(d.pop("quarter", UNSET))

        def _parse_res_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        res_district = _parse_res_district(d.pop("resDistrict", UNSET))

        def _parse_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_variable(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        variable = _parse_variable(d.pop("variable", UNSET))

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

        wfs_map_server_wfs_crdaq_statby_com_typeof_drugordered_attributes = cls(
            year=year,
            district=district,
            drugs=drugs,
            fid=fid,
            quarter=quarter,
            res_district=res_district,
            value=value,
            variable=variable,
            objectid=objectid,
            shape=shape,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_crdaq_statby_com_typeof_drugordered_attributes.additional_properties = d
        return wfs_map_server_wfs_crdaq_statby_com_typeof_drugordered_attributes

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
