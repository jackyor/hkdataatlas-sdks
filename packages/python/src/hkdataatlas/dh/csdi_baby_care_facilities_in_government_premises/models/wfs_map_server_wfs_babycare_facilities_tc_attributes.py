from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsBabycareFacilitiesTCAttributes")


@_attrs_define
class WfsMapServerWfsBabycareFacilitiesTCAttributes:
    """
    Attributes:
        amount (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        department_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        easting_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        name_babycare_facilities_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        northing_m (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
        region_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        website_facilities (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    amount: float | None | Unset = UNSET
    department_tc: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    easting_m: float | None | Unset = UNSET
    name_babycare_facilities_tc: None | str | Unset = UNSET
    northing_m: float | None | Unset = UNSET
    region_tc: None | str | Unset = UNSET
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

        department_tc: None | str | Unset
        if isinstance(self.department_tc, Unset):
            department_tc = UNSET
        else:
            department_tc = self.department_tc

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        easting_m: float | None | Unset
        if isinstance(self.easting_m, Unset):
            easting_m = UNSET
        else:
            easting_m = self.easting_m

        name_babycare_facilities_tc: None | str | Unset
        if isinstance(self.name_babycare_facilities_tc, Unset):
            name_babycare_facilities_tc = UNSET
        else:
            name_babycare_facilities_tc = self.name_babycare_facilities_tc

        northing_m: float | None | Unset
        if isinstance(self.northing_m, Unset):
            northing_m = UNSET
        else:
            northing_m = self.northing_m

        region_tc: None | str | Unset
        if isinstance(self.region_tc, Unset):
            region_tc = UNSET
        else:
            region_tc = self.region_tc

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
        if department_tc is not UNSET:
            field_dict["Department_TC"] = department_tc
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if easting_m is not UNSET:
            field_dict["Easting_m"] = easting_m
        if name_babycare_facilities_tc is not UNSET:
            field_dict["Name_Babycare_Facilities_TC"] = name_babycare_facilities_tc
        if northing_m is not UNSET:
            field_dict["Northing_m"] = northing_m
        if region_tc is not UNSET:
            field_dict["Region_TC"] = region_tc
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

        def _parse_department_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        department_tc = _parse_department_tc(d.pop("Department_TC", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_easting_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        easting_m = _parse_easting_m(d.pop("Easting_m", UNSET))

        def _parse_name_babycare_facilities_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name_babycare_facilities_tc = _parse_name_babycare_facilities_tc(
            d.pop("Name_Babycare_Facilities_TC", UNSET)
        )

        def _parse_northing_m(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        northing_m = _parse_northing_m(d.pop("Northing_m", UNSET))

        def _parse_region_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_tc = _parse_region_tc(d.pop("Region_TC", UNSET))

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

        wfs_map_server_wfs_babycare_facilities_tc_attributes = cls(
            amount=amount,
            department_tc=department_tc,
            district_tc=district_tc,
            easting_m=easting_m,
            name_babycare_facilities_tc=name_babycare_facilities_tc,
            northing_m=northing_m,
            region_tc=region_tc,
            website_facilities=website_facilities,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfs_babycare_facilities_tc_attributes.additional_properties = d
        return wfs_map_server_wfs_babycare_facilities_tc_attributes

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
