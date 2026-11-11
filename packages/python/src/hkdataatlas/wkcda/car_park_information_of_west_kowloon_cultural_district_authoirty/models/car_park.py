from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.localized_text import LocalizedText
    from ..models.vacancy import Vacancy


T = TypeVar("T", bound="CarPark")


@_attrs_define
class CarPark:
    """
    Attributes:
        address (LocalizedText | Unset):
        contact_no (str | Unset):
        day_park (str | Unset):
        day_park_800am_600pm (str | Unset):
        district (LocalizedText | Unset):
        height_limit (float | Unset):
        hourly_park_sat_sun_and_public_holidays (str | Unset): Hourly parking rate on Saturdays, Sundays and public
            holidays.
        hourly_park_weekdays_except_public_holidays (str | Unset): Hourly parking rate on weekdays except public
            holidays.
        id (str | Unset): Car park identifier.
        latitude (str | Unset):
        longitude (str | Unset):
        name (LocalizedText | Unset):
        opening_status (str | Unset):
        opening_hours (str | Unset):
        remark (LocalizedText | Unset):
        td_e_parking_id (str | Unset): Identifier used for TD eParking.
        timestamp (str | Unset): Timestamp for the car park record. The example is a string with a +800 suffix; no
            standardized date-time format is asserted.
        vacancies (list[Vacancy] | Unset):
        website (LocalizedText | Unset):
    """

    address: LocalizedText | Unset = UNSET
    contact_no: str | Unset = UNSET
    day_park: str | Unset = UNSET
    day_park_800am_600pm: str | Unset = UNSET
    district: LocalizedText | Unset = UNSET
    height_limit: float | Unset = UNSET
    hourly_park_sat_sun_and_public_holidays: str | Unset = UNSET
    hourly_park_weekdays_except_public_holidays: str | Unset = UNSET
    id: str | Unset = UNSET
    latitude: str | Unset = UNSET
    longitude: str | Unset = UNSET
    name: LocalizedText | Unset = UNSET
    opening_status: str | Unset = UNSET
    opening_hours: str | Unset = UNSET
    remark: LocalizedText | Unset = UNSET
    td_e_parking_id: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    vacancies: list[Vacancy] | Unset = UNSET
    website: LocalizedText | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        contact_no = self.contact_no

        day_park = self.day_park

        day_park_800am_600pm = self.day_park_800am_600pm

        district: dict[str, Any] | Unset = UNSET
        if not isinstance(self.district, Unset):
            district = self.district.to_dict()

        height_limit = self.height_limit

        hourly_park_sat_sun_and_public_holidays = (
            self.hourly_park_sat_sun_and_public_holidays
        )

        hourly_park_weekdays_except_public_holidays = (
            self.hourly_park_weekdays_except_public_holidays
        )

        id = self.id

        latitude = self.latitude

        longitude = self.longitude

        name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.to_dict()

        opening_status = self.opening_status

        opening_hours = self.opening_hours

        remark: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remark, Unset):
            remark = self.remark.to_dict()

        td_e_parking_id = self.td_e_parking_id

        timestamp = self.timestamp

        vacancies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vacancies, Unset):
            vacancies = []
            for vacancies_item_data in self.vacancies:
                vacancies_item = vacancies_item_data.to_dict()
                vacancies.append(vacancies_item)

        website: dict[str, Any] | Unset = UNSET
        if not isinstance(self.website, Unset):
            website = self.website.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if contact_no is not UNSET:
            field_dict["contactNo"] = contact_no
        if day_park is not UNSET:
            field_dict["day_park"] = day_park
        if day_park_800am_600pm is not UNSET:
            field_dict["day_park_8:00am_6:00pm"] = day_park_800am_600pm
        if district is not UNSET:
            field_dict["district"] = district
        if height_limit is not UNSET:
            field_dict["heightLimit"] = height_limit
        if hourly_park_sat_sun_and_public_holidays is not UNSET:
            field_dict["hourly_park_Sat_Sun_and_public_holidays"] = (
                hourly_park_sat_sun_and_public_holidays
            )
        if hourly_park_weekdays_except_public_holidays is not UNSET:
            field_dict["hourly_park_weekdays_except_public_holidays"] = (
                hourly_park_weekdays_except_public_holidays
            )
        if id is not UNSET:
            field_dict["id"] = id
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if name is not UNSET:
            field_dict["name"] = name
        if opening_status is not UNSET:
            field_dict["openingStatus"] = opening_status
        if opening_hours is not UNSET:
            field_dict["opening_hours"] = opening_hours
        if remark is not UNSET:
            field_dict["remark"] = remark
        if td_e_parking_id is not UNSET:
            field_dict["td_eParking_id"] = td_e_parking_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if vacancies is not UNSET:
            field_dict["vacancies"] = vacancies
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.localized_text import LocalizedText
        from ..models.vacancy import Vacancy

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: LocalizedText | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = LocalizedText.from_dict(_address)

        contact_no = d.pop("contactNo", UNSET)

        day_park = d.pop("day_park", UNSET)

        day_park_800am_600pm = d.pop("day_park_8:00am_6:00pm", UNSET)

        _district = d.pop("district", UNSET)
        district: LocalizedText | Unset
        if isinstance(_district, Unset):
            district = UNSET
        else:
            district = LocalizedText.from_dict(_district)

        height_limit = d.pop("heightLimit", UNSET)

        hourly_park_sat_sun_and_public_holidays = d.pop(
            "hourly_park_Sat_Sun_and_public_holidays", UNSET
        )

        hourly_park_weekdays_except_public_holidays = d.pop(
            "hourly_park_weekdays_except_public_holidays", UNSET
        )

        id = d.pop("id", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        _name = d.pop("name", UNSET)
        name: LocalizedText | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = LocalizedText.from_dict(_name)

        opening_status = d.pop("openingStatus", UNSET)

        opening_hours = d.pop("opening_hours", UNSET)

        _remark = d.pop("remark", UNSET)
        remark: LocalizedText | Unset
        if isinstance(_remark, Unset):
            remark = UNSET
        else:
            remark = LocalizedText.from_dict(_remark)

        td_e_parking_id = d.pop("td_eParking_id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        _vacancies = d.pop("vacancies", UNSET)
        vacancies: list[Vacancy] | Unset = UNSET
        if _vacancies is not UNSET:
            vacancies = []
            for vacancies_item_data in _vacancies:
                vacancies_item = Vacancy.from_dict(vacancies_item_data)

                vacancies.append(vacancies_item)

        _website = d.pop("website", UNSET)
        website: LocalizedText | Unset
        if isinstance(_website, Unset):
            website = UNSET
        else:
            website = LocalizedText.from_dict(_website)

        car_park = cls(
            address=address,
            contact_no=contact_no,
            day_park=day_park,
            day_park_800am_600pm=day_park_800am_600pm,
            district=district,
            height_limit=height_limit,
            hourly_park_sat_sun_and_public_holidays=hourly_park_sat_sun_and_public_holidays,
            hourly_park_weekdays_except_public_holidays=hourly_park_weekdays_except_public_holidays,
            id=id,
            latitude=latitude,
            longitude=longitude,
            name=name,
            opening_status=opening_status,
            opening_hours=opening_hours,
            remark=remark,
            td_e_parking_id=td_e_parking_id,
            timestamp=timestamp,
            vacancies=vacancies,
            website=website,
        )

        car_park.additional_properties = d
        return car_park

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
