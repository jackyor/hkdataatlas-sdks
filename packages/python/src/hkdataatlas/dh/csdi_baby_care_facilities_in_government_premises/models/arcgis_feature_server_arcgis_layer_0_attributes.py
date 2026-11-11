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
        amount (float | None | Unset): Publisher field type: esriFieldTypeDouble
        department_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        easting_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        name_babycare_facilities_en (None | str | Unset): Publisher field type: esriFieldTypeString
        northing_m (float | None | Unset): Publisher field type: esriFieldTypeDouble
        region_en (None | str | Unset): Publisher field type: esriFieldTypeString
        website_facilities (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    amount: float | None | Unset = UNSET
    department_en: None | str | Unset = UNSET
    district_en: None | str | Unset = UNSET
    easting_m: float | None | Unset = UNSET
    name_babycare_facilities_en: None | str | Unset = UNSET
    northing_m: float | None | Unset = UNSET
    region_en: None | str | Unset = UNSET
    website_facilities: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        department_en: None | str | Unset
        if isinstance(self.department_en, Unset):
            department_en = UNSET
        else:
            department_en = self.department_en

        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

        easting_m: float | None | Unset
        if isinstance(self.easting_m, Unset):
            easting_m = UNSET
        else:
            easting_m = self.easting_m

        name_babycare_facilities_en: None | str | Unset
        if isinstance(self.name_babycare_facilities_en, Unset):
            name_babycare_facilities_en = UNSET
        else:
            name_babycare_facilities_en = self.name_babycare_facilities_en

        northing_m: float | None | Unset
        if isinstance(self.northing_m, Unset):
            northing_m = UNSET
        else:
            northing_m = self.northing_m

        region_en: None | str | Unset
        if isinstance(self.region_en, Unset):
            region_en = UNSET
        else:
            region_en = self.region_en

        website_facilities: None | str | Unset
        if isinstance(self.website_facilities, Unset):
            website_facilities = UNSET
        else:
            website_facilities = self.website_facilities

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["Amount"] = amount
        if department_en is not UNSET:
            field_dict["Department_EN"] = department_en
        if district_en is not UNSET:
            field_dict["District_EN"] = district_en
        if easting_m is not UNSET:
            field_dict["Easting_m"] = easting_m
        if name_babycare_facilities_en is not UNSET:
            field_dict["Name_Babycare_Facilities_EN"] = name_babycare_facilities_en
        if northing_m is not UNSET:
            field_dict["Northing_m"] = northing_m
        if region_en is not UNSET:
            field_dict["Region_EN"] = region_en
        if website_facilities is not UNSET:
            field_dict["Website_Facilities"] = website_facilities
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("Amount", UNSET))

        def _parse_department_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department_en = _parse_department_en(d.pop("Department_EN", UNSET))

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_EN", UNSET))

        def _parse_easting_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting_m = _parse_easting_m(d.pop("Easting_m", UNSET))

        def _parse_name_babycare_facilities_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_babycare_facilities_en = _parse_name_babycare_facilities_en(
            d.pop("Name_Babycare_Facilities_EN", UNSET)
        )

        def _parse_northing_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing_m = _parse_northing_m(d.pop("Northing_m", UNSET))

        def _parse_region_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_en = _parse_region_en(d.pop("Region_EN", UNSET))

        def _parse_website_facilities(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_facilities = _parse_website_facilities(
            d.pop("Website_Facilities", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            amount=amount,
            department_en=department_en,
            district_en=district_en,
            easting_m=easting_m,
            name_babycare_facilities_en=name_babycare_facilities_en,
            northing_m=northing_m,
            region_en=region_en,
            website_facilities=website_facilities,
            objectid=objectid,
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
