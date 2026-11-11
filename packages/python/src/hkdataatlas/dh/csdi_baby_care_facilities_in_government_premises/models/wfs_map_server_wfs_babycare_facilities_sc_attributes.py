from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsBabycareFacilitiesSCAttributes")


@_attrs_define
class WfsMapServerWfsBabycareFacilitiesSCAttributes:
    """
    Attributes:
        amount (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        department_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        easting_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        name_babycare_facilities_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        northing_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        region_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        website_facilities (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    amount: float | None | Unset = UNSET
    department_sc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    easting_m: float | None | Unset = UNSET
    name_babycare_facilities_sc: None | str | Unset = UNSET
    northing_m: float | None | Unset = UNSET
    region_sc: None | str | Unset = UNSET
    website_facilities: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        department_sc: None | str | Unset
        if isinstance(self.department_sc, Unset):
            department_sc = UNSET
        else:
            department_sc = self.department_sc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        easting_m: float | None | Unset
        if isinstance(self.easting_m, Unset):
            easting_m = UNSET
        else:
            easting_m = self.easting_m

        name_babycare_facilities_sc: None | str | Unset
        if isinstance(self.name_babycare_facilities_sc, Unset):
            name_babycare_facilities_sc = UNSET
        else:
            name_babycare_facilities_sc = self.name_babycare_facilities_sc

        northing_m: float | None | Unset
        if isinstance(self.northing_m, Unset):
            northing_m = UNSET
        else:
            northing_m = self.northing_m

        region_sc: None | str | Unset
        if isinstance(self.region_sc, Unset):
            region_sc = UNSET
        else:
            region_sc = self.region_sc

        website_facilities: None | str | Unset
        if isinstance(self.website_facilities, Unset):
            website_facilities = UNSET
        else:
            website_facilities = self.website_facilities

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["Amount"] = amount
        if department_sc is not UNSET:
            field_dict["Department_SC"] = department_sc
        if district_sc is not UNSET:
            field_dict["District_SC"] = district_sc
        if easting_m is not UNSET:
            field_dict["Easting_m"] = easting_m
        if name_babycare_facilities_sc is not UNSET:
            field_dict["Name_Babycare_Facilities_SC"] = name_babycare_facilities_sc
        if northing_m is not UNSET:
            field_dict["Northing_m"] = northing_m
        if region_sc is not UNSET:
            field_dict["Region_SC"] = region_sc
        if website_facilities is not UNSET:
            field_dict["Website_Facilities"] = website_facilities
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

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

        def _parse_department_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department_sc = _parse_department_sc(d.pop("Department_SC", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("District_SC", UNSET))

        def _parse_easting_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting_m = _parse_easting_m(d.pop("Easting_m", UNSET))

        def _parse_name_babycare_facilities_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_babycare_facilities_sc = _parse_name_babycare_facilities_sc(
            d.pop("Name_Babycare_Facilities_SC", UNSET)
        )

        def _parse_northing_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing_m = _parse_northing_m(d.pop("Northing_m", UNSET))

        def _parse_region_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_sc = _parse_region_sc(d.pop("Region_SC", UNSET))

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

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfs_babycare_facilities_sc_attributes = cls(
            amount=amount,
            department_sc=department_sc,
            district_sc=district_sc,
            easting_m=easting_m,
            name_babycare_facilities_sc=name_babycare_facilities_sc,
            northing_m=northing_m,
            region_sc=region_sc,
            website_facilities=website_facilities,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_babycare_facilities_sc_attributes.additional_properties = d
        return wfs_map_server_wfs_babycare_facilities_sc_attributes

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
