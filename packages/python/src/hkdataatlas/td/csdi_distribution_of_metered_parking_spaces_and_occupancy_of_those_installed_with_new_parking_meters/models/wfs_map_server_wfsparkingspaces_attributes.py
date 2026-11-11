from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsparkingspacesAttributes")


@_attrs_define
class WfsMapServerWfsparkingspacesAttributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        pole_id (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        parking_space_id (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        region (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        region_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        region_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        sub_district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        sub_district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        sub_district_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        street (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        street_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        street_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        section_of_street (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        section_of_street_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        section_of_street_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        vehicle_type (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        lpp (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all
            JSON queries.
        operating_period (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        time_unit (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        payment_unit (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        vacancy_url (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    pole_id: int | None | Unset = UNSET
    parking_space_id: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    region_tc: None | str | Unset = UNSET
    region_sc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    sub_district: None | str | Unset = UNSET
    sub_district_tc: None | str | Unset = UNSET
    sub_district_sc: None | str | Unset = UNSET
    street: None | str | Unset = UNSET
    street_tc: None | str | Unset = UNSET
    street_sc: None | str | Unset = UNSET
    section_of_street: None | str | Unset = UNSET
    section_of_street_tc: None | str | Unset = UNSET
    section_of_street_sc: None | str | Unset = UNSET
    vehicle_type: None | str | Unset = UNSET
    lpp: int | None | Unset = UNSET
    operating_period: None | str | Unset = UNSET
    time_unit: int | None | Unset = UNSET
    payment_unit: float | None | Unset = UNSET
    vacancy_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

        objectid = self.objectid

        pole_id: int | None | Unset
        if isinstance(self.pole_id, Unset):
            pole_id = UNSET
        else:
            pole_id = self.pole_id

        parking_space_id: None | str | Unset
        if isinstance(self.parking_space_id, Unset):
            parking_space_id = UNSET
        else:
            parking_space_id = self.parking_space_id

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        region_tc: None | str | Unset
        if isinstance(self.region_tc, Unset):
            region_tc = UNSET
        else:
            region_tc = self.region_tc

        region_sc: None | str | Unset
        if isinstance(self.region_sc, Unset):
            region_sc = UNSET
        else:
            region_sc = self.region_sc

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        district_sc: None | str | Unset
        if isinstance(self.district_sc, Unset):
            district_sc = UNSET
        else:
            district_sc = self.district_sc

        sub_district: None | str | Unset
        if isinstance(self.sub_district, Unset):
            sub_district = UNSET
        else:
            sub_district = self.sub_district

        sub_district_tc: None | str | Unset
        if isinstance(self.sub_district_tc, Unset):
            sub_district_tc = UNSET
        else:
            sub_district_tc = self.sub_district_tc

        sub_district_sc: None | str | Unset
        if isinstance(self.sub_district_sc, Unset):
            sub_district_sc = UNSET
        else:
            sub_district_sc = self.sub_district_sc

        street: None | str | Unset
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        street_tc: None | str | Unset
        if isinstance(self.street_tc, Unset):
            street_tc = UNSET
        else:
            street_tc = self.street_tc

        street_sc: None | str | Unset
        if isinstance(self.street_sc, Unset):
            street_sc = UNSET
        else:
            street_sc = self.street_sc

        section_of_street: None | str | Unset
        if isinstance(self.section_of_street, Unset):
            section_of_street = UNSET
        else:
            section_of_street = self.section_of_street

        section_of_street_tc: None | str | Unset
        if isinstance(self.section_of_street_tc, Unset):
            section_of_street_tc = UNSET
        else:
            section_of_street_tc = self.section_of_street_tc

        section_of_street_sc: None | str | Unset
        if isinstance(self.section_of_street_sc, Unset):
            section_of_street_sc = UNSET
        else:
            section_of_street_sc = self.section_of_street_sc

        vehicle_type: None | str | Unset
        if isinstance(self.vehicle_type, Unset):
            vehicle_type = UNSET
        else:
            vehicle_type = self.vehicle_type

        lpp: int | None | Unset
        if isinstance(self.lpp, Unset):
            lpp = UNSET
        else:
            lpp = self.lpp

        operating_period: None | str | Unset
        if isinstance(self.operating_period, Unset):
            operating_period = UNSET
        else:
            operating_period = self.operating_period

        time_unit: int | None | Unset
        if isinstance(self.time_unit, Unset):
            time_unit = UNSET
        else:
            time_unit = self.time_unit

        payment_unit: float | None | Unset
        if isinstance(self.payment_unit, Unset):
            payment_unit = UNSET
        else:
            payment_unit = self.payment_unit

        vacancy_url: None | str | Unset
        if isinstance(self.vacancy_url, Unset):
            vacancy_url = UNSET
        else:
            vacancy_url = self.vacancy_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if pole_id is not UNSET:
            field_dict["PoleId"] = pole_id
        if parking_space_id is not UNSET:
            field_dict["ParkingSpaceId"] = parking_space_id
        if region is not UNSET:
            field_dict["Region"] = region
        if region_tc is not UNSET:
            field_dict["Region_tc"] = region_tc
        if region_sc is not UNSET:
            field_dict["Region_sc"] = region_sc
        if district is not UNSET:
            field_dict["District"] = district
        if district_tc is not UNSET:
            field_dict["District_tc"] = district_tc
        if district_sc is not UNSET:
            field_dict["District_sc"] = district_sc
        if sub_district is not UNSET:
            field_dict["SubDistrict"] = sub_district
        if sub_district_tc is not UNSET:
            field_dict["SubDistrict_tc"] = sub_district_tc
        if sub_district_sc is not UNSET:
            field_dict["SubDistrict_sc"] = sub_district_sc
        if street is not UNSET:
            field_dict["Street"] = street
        if street_tc is not UNSET:
            field_dict["Street_tc"] = street_tc
        if street_sc is not UNSET:
            field_dict["Street_sc"] = street_sc
        if section_of_street is not UNSET:
            field_dict["SectionOfStreet"] = section_of_street
        if section_of_street_tc is not UNSET:
            field_dict["SectionOfStreet_tc"] = section_of_street_tc
        if section_of_street_sc is not UNSET:
            field_dict["SectionOfStreet_sc"] = section_of_street_sc
        if vehicle_type is not UNSET:
            field_dict["VehicleType"] = vehicle_type
        if lpp is not UNSET:
            field_dict["LPP"] = lpp
        if operating_period is not UNSET:
            field_dict["OperatingPeriod"] = operating_period
        if time_unit is not UNSET:
            field_dict["TimeUnit"] = time_unit
        if payment_unit is not UNSET:
            field_dict["PaymentUnit"] = payment_unit
        if vacancy_url is not UNSET:
            field_dict["VacancyUrl"] = vacancy_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("SHAPE", UNSET)

        objectid = d.pop("OBJECTID", UNSET)

        def _parse_pole_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pole_id = _parse_pole_id(d.pop("PoleId", UNSET))

        def _parse_parking_space_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parking_space_id = _parse_parking_space_id(d.pop("ParkingSpaceId", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("Region", UNSET))

        def _parse_region_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_tc = _parse_region_tc(d.pop("Region_tc", UNSET))

        def _parse_region_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_sc = _parse_region_sc(d.pop("Region_sc", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("District", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_tc", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("District_sc", UNSET))

        def _parse_sub_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_district = _parse_sub_district(d.pop("SubDistrict", UNSET))

        def _parse_sub_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_district_tc = _parse_sub_district_tc(d.pop("SubDistrict_tc", UNSET))

        def _parse_sub_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_district_sc = _parse_sub_district_sc(d.pop("SubDistrict_sc", UNSET))

        def _parse_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street = _parse_street(d.pop("Street", UNSET))

        def _parse_street_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_tc = _parse_street_tc(d.pop("Street_tc", UNSET))

        def _parse_street_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        street_sc = _parse_street_sc(d.pop("Street_sc", UNSET))

        def _parse_section_of_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_of_street = _parse_section_of_street(d.pop("SectionOfStreet", UNSET))

        def _parse_section_of_street_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_of_street_tc = _parse_section_of_street_tc(
            d.pop("SectionOfStreet_tc", UNSET)
        )

        def _parse_section_of_street_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section_of_street_sc = _parse_section_of_street_sc(
            d.pop("SectionOfStreet_sc", UNSET)
        )

        def _parse_vehicle_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vehicle_type = _parse_vehicle_type(d.pop("VehicleType", UNSET))

        def _parse_lpp(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        lpp = _parse_lpp(d.pop("LPP", UNSET))

        def _parse_operating_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operating_period = _parse_operating_period(d.pop("OperatingPeriod", UNSET))

        def _parse_time_unit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        time_unit = _parse_time_unit(d.pop("TimeUnit", UNSET))

        def _parse_payment_unit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        payment_unit = _parse_payment_unit(d.pop("PaymentUnit", UNSET))

        def _parse_vacancy_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vacancy_url = _parse_vacancy_url(d.pop("VacancyUrl", UNSET))

        wfs_map_server_wfsparkingspaces_attributes = cls(
            shape=shape,
            objectid=objectid,
            pole_id=pole_id,
            parking_space_id=parking_space_id,
            region=region,
            region_tc=region_tc,
            region_sc=region_sc,
            district=district,
            district_tc=district_tc,
            district_sc=district_sc,
            sub_district=sub_district,
            sub_district_tc=sub_district_tc,
            sub_district_sc=sub_district_sc,
            street=street,
            street_tc=street_tc,
            street_sc=street_sc,
            section_of_street=section_of_street,
            section_of_street_tc=section_of_street_tc,
            section_of_street_sc=section_of_street_sc,
            vehicle_type=vehicle_type,
            lpp=lpp,
            operating_period=operating_period,
            time_unit=time_unit,
            payment_unit=payment_unit,
            vacancy_url=vacancy_url,
        )

        wfs_map_server_wfsparkingspaces_attributes.additional_properties = d
        return wfs_map_server_wfsparkingspaces_attributes

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
