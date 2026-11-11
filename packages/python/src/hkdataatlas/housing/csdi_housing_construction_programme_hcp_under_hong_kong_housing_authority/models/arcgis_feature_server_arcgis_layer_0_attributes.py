from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        district_council_districts_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_council_districts_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_council_districts_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        project_title_en (None | str | Unset): Publisher field type: esriFieldTypeString
        project_title_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        project_title_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        housing_type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        housing_type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        housing_type_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        estimated_flat_number (int | None | Unset): Publisher field type: esriFieldTypeSmallInteger
        completion_year (None | str | Unset): Publisher field type: esriFieldTypeString
    """

    objectid: int | Unset = UNSET
    district_council_districts_en: None | str | Unset = UNSET
    district_council_districts_tc: None | str | Unset = UNSET
    district_council_districts_sc: None | str | Unset = UNSET
    project_title_en: None | str | Unset = UNSET
    project_title_tc: None | str | Unset = UNSET
    project_title_sc: None | str | Unset = UNSET
    housing_type_en: None | str | Unset = UNSET
    housing_type_tc: None | str | Unset = UNSET
    housing_type_sc: None | str | Unset = UNSET
    estimated_flat_number: int | None | Unset = UNSET
    completion_year: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        district_council_districts_en: None | str | Unset
        if isinstance(self.district_council_districts_en, Unset):
            district_council_districts_en = UNSET
        else:
            district_council_districts_en = self.district_council_districts_en

        district_council_districts_tc: None | str | Unset
        if isinstance(self.district_council_districts_tc, Unset):
            district_council_districts_tc = UNSET
        else:
            district_council_districts_tc = self.district_council_districts_tc

        district_council_districts_sc: None | str | Unset
        if isinstance(self.district_council_districts_sc, Unset):
            district_council_districts_sc = UNSET
        else:
            district_council_districts_sc = self.district_council_districts_sc

        project_title_en: None | str | Unset
        if isinstance(self.project_title_en, Unset):
            project_title_en = UNSET
        else:
            project_title_en = self.project_title_en

        project_title_tc: None | str | Unset
        if isinstance(self.project_title_tc, Unset):
            project_title_tc = UNSET
        else:
            project_title_tc = self.project_title_tc

        project_title_sc: None | str | Unset
        if isinstance(self.project_title_sc, Unset):
            project_title_sc = UNSET
        else:
            project_title_sc = self.project_title_sc

        housing_type_en: None | str | Unset
        if isinstance(self.housing_type_en, Unset):
            housing_type_en = UNSET
        else:
            housing_type_en = self.housing_type_en

        housing_type_tc: None | str | Unset
        if isinstance(self.housing_type_tc, Unset):
            housing_type_tc = UNSET
        else:
            housing_type_tc = self.housing_type_tc

        housing_type_sc: None | str | Unset
        if isinstance(self.housing_type_sc, Unset):
            housing_type_sc = UNSET
        else:
            housing_type_sc = self.housing_type_sc

        estimated_flat_number: int | None | Unset
        if isinstance(self.estimated_flat_number, Unset):
            estimated_flat_number = UNSET
        else:
            estimated_flat_number = self.estimated_flat_number

        completion_year: None | str | Unset
        if isinstance(self.completion_year, Unset):
            completion_year = UNSET
        else:
            completion_year = self.completion_year

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if district_council_districts_en is not UNSET:
            field_dict["DISTRICT_COUNCIL_DISTRICTS_EN"] = district_council_districts_en
        if district_council_districts_tc is not UNSET:
            field_dict["DISTRICT_COUNCIL_DISTRICTS_TC"] = district_council_districts_tc
        if district_council_districts_sc is not UNSET:
            field_dict["DISTRICT_COUNCIL_DISTRICTS_SC"] = district_council_districts_sc
        if project_title_en is not UNSET:
            field_dict["PROJECT_TITLE_EN"] = project_title_en
        if project_title_tc is not UNSET:
            field_dict["PROJECT_TITLE_TC"] = project_title_tc
        if project_title_sc is not UNSET:
            field_dict["PROJECT_TITLE_SC"] = project_title_sc
        if housing_type_en is not UNSET:
            field_dict["HOUSING_TYPE_EN"] = housing_type_en
        if housing_type_tc is not UNSET:
            field_dict["HOUSING_TYPE_TC"] = housing_type_tc
        if housing_type_sc is not UNSET:
            field_dict["HOUSING_TYPE_SC"] = housing_type_sc
        if estimated_flat_number is not UNSET:
            field_dict["ESTIMATED_FLAT_NUMBER"] = estimated_flat_number
        if completion_year is not UNSET:
            field_dict["COMPLETION_YEAR"] = completion_year

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_district_council_districts_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_council_districts_en = _parse_district_council_districts_en(
            d.pop("DISTRICT_COUNCIL_DISTRICTS_EN", UNSET)
        )

        def _parse_district_council_districts_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_council_districts_tc = _parse_district_council_districts_tc(
            d.pop("DISTRICT_COUNCIL_DISTRICTS_TC", UNSET)
        )

        def _parse_district_council_districts_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_council_districts_sc = _parse_district_council_districts_sc(
            d.pop("DISTRICT_COUNCIL_DISTRICTS_SC", UNSET)
        )

        def _parse_project_title_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title_en = _parse_project_title_en(d.pop("PROJECT_TITLE_EN", UNSET))

        def _parse_project_title_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title_tc = _parse_project_title_tc(d.pop("PROJECT_TITLE_TC", UNSET))

        def _parse_project_title_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        project_title_sc = _parse_project_title_sc(d.pop("PROJECT_TITLE_SC", UNSET))

        def _parse_housing_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        housing_type_en = _parse_housing_type_en(d.pop("HOUSING_TYPE_EN", UNSET))

        def _parse_housing_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        housing_type_tc = _parse_housing_type_tc(d.pop("HOUSING_TYPE_TC", UNSET))

        def _parse_housing_type_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        housing_type_sc = _parse_housing_type_sc(d.pop("HOUSING_TYPE_SC", UNSET))

        def _parse_estimated_flat_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        estimated_flat_number = _parse_estimated_flat_number(
            d.pop("ESTIMATED_FLAT_NUMBER", UNSET)
        )

        def _parse_completion_year(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        completion_year = _parse_completion_year(d.pop("COMPLETION_YEAR", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            district_council_districts_en=district_council_districts_en,
            district_council_districts_tc=district_council_districts_tc,
            district_council_districts_sc=district_council_districts_sc,
            project_title_en=project_title_en,
            project_title_tc=project_title_tc,
            project_title_sc=project_title_sc,
            housing_type_en=housing_type_en,
            housing_type_tc=housing_type_tc,
            housing_type_sc=housing_type_sc,
            estimated_flat_number=estimated_flat_number,
            completion_year=completion_year,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
