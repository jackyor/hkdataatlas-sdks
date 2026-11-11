from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.carpark_info_lang import CarparkInfoLang, check_carpark_info_lang
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grace_period import GracePeriod
    from ..models.height_limit import HeightLimit
    from ..models.opening_hour import OpeningHour
    from ..models.rendition_urls import RenditionUrls
    from ..models.vehicle_information import VehicleInformation


T = TypeVar("T", bound="CarparkInfo")


@_attrs_define
class CarparkInfo:
    """Basic car park information. Properties marked required in the publisher dictionary are required for this object;
    other dictionary fields are optional.

        Attributes:
            display_address (str): Display address of the car park.
            lang (CarparkInfoLang): Display language of the car park information.
            latitude (float): Latitude of the car park.
            longitude (float): Longitude of the car park.
            name (str): The name of the car park.
            park_id (str): The system ID of the car park.
            cv (VehicleInformation | Unset): Vehicle-space and rating information. The property may be omitted if the car
                park has no information for that vehicle type.
            hgv (VehicleInformation | Unset): Vehicle-space and rating information. The property may be omitted if the car
                park has no information for that vehicle type.
            lgv (VehicleInformation | Unset): Vehicle-space and rating information. The property may be omitted if the car
                park has no information for that vehicle type.
            address (Any | Unset): Address of the car park. Locale-specific address fields are documented as optional except
                where marked required. The publisher declares the district field required with spelling dcDestrict; one bounded
                three-item response uses dcDistrict instead. At least one of these source/observed spellings is required, while
                both are permitted. Other declared required address fields remain required.
            carpark_type (str | Unset): Type of car park; documented possible values are multi-storey, off-street, and
                metered.
            coach (VehicleInformation | Unset): Vehicle-space and rating information. The property may be omitted if the car
                park has no information for that vehicle type.
            contact_no (str | Unset): Telephone number of the car park.
            creation_date (str | Unset): Creation time (YYYY-MM-DD HH:MM:SS).
            district (str | Unset): District name.
            facilities (list[str] | Unset):
            grace_periods (list[GracePeriod] | Unset): Array of grace-period rules.
            height_limits (list[HeightLimit] | Unset): Array of height limits.
            modified_date (str | Unset): Last modified time (YYYY-MM-DD HH:MM:SS).
            motor_cycle (VehicleInformation | Unset): Vehicle-space and rating information. The property may be omitted if
                the car park has no information for that vehicle type.
            nature (str | Unset): Nature of the car park; documented possible values are government or commercial.
            opening_hours (list[OpeningHour] | Unset): Array of opening-hour rules.
            opening_status (str | Unset): Current opening status: OPEN or CLOSED.
            payment_methods (list[str] | Unset):
            private_car (VehicleInformation | Unset): Vehicle-space and rating information. The property may be omitted if
                the car park has no information for that vehicle type.
            published_date (str | Unset): Publication time (YYYY-MM-DD HH:MM:SS).
            rendition_urls (RenditionUrls | Unset): Image renditions generated from a photo uploaded by the car park owner.
                Empty if the car park has no photo.
            website (str | Unset): URL of the car park website. The publisher declares an optional String and does not
                impose a URI format constraint. One retained bounded response contains an empty string.
    """

    display_address: str
    lang: CarparkInfoLang
    latitude: float
    longitude: float
    name: str
    park_id: str
    cv: VehicleInformation | Unset = UNSET
    hgv: VehicleInformation | Unset = UNSET
    lgv: VehicleInformation | Unset = UNSET
    address: Any | Unset = UNSET
    carpark_type: str | Unset = UNSET
    coach: VehicleInformation | Unset = UNSET
    contact_no: str | Unset = UNSET
    creation_date: str | Unset = UNSET
    district: str | Unset = UNSET
    facilities: list[str] | Unset = UNSET
    grace_periods: list[GracePeriod] | Unset = UNSET
    height_limits: list[HeightLimit] | Unset = UNSET
    modified_date: str | Unset = UNSET
    motor_cycle: VehicleInformation | Unset = UNSET
    nature: str | Unset = UNSET
    opening_hours: list[OpeningHour] | Unset = UNSET
    opening_status: str | Unset = UNSET
    payment_methods: list[str] | Unset = UNSET
    private_car: VehicleInformation | Unset = UNSET
    published_date: str | Unset = UNSET
    rendition_urls: RenditionUrls | Unset = UNSET
    website: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_address = self.display_address

        lang: str = self.lang

        latitude = self.latitude

        longitude = self.longitude

        name = self.name

        park_id = self.park_id

        cv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cv, Unset):
            cv = self.cv.to_dict()

        hgv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hgv, Unset):
            hgv = self.hgv.to_dict()

        lgv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lgv, Unset):
            lgv = self.lgv.to_dict()

        address: Any | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        carpark_type = self.carpark_type

        coach: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coach, Unset):
            coach = self.coach.to_dict()

        contact_no = self.contact_no

        creation_date = self.creation_date

        district = self.district

        facilities: list[str] | Unset = UNSET
        if not isinstance(self.facilities, Unset):
            facilities = self.facilities

        grace_periods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grace_periods, Unset):
            grace_periods = []
            for grace_periods_item_data in self.grace_periods:
                grace_periods_item = grace_periods_item_data.to_dict()
                grace_periods.append(grace_periods_item)

        height_limits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.height_limits, Unset):
            height_limits = []
            for height_limits_item_data in self.height_limits:
                height_limits_item = height_limits_item_data.to_dict()
                height_limits.append(height_limits_item)

        modified_date = self.modified_date

        motor_cycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.motor_cycle, Unset):
            motor_cycle = self.motor_cycle.to_dict()

        nature = self.nature

        opening_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.opening_hours, Unset):
            opening_hours = []
            for opening_hours_item_data in self.opening_hours:
                opening_hours_item = opening_hours_item_data.to_dict()
                opening_hours.append(opening_hours_item)

        opening_status = self.opening_status

        payment_methods: list[str] | Unset = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods

        private_car: dict[str, Any] | Unset = UNSET
        if not isinstance(self.private_car, Unset):
            private_car = self.private_car.to_dict()

        published_date = self.published_date

        rendition_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rendition_urls, Unset):
            rendition_urls = self.rendition_urls.to_dict()

        website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayAddress": display_address,
                "lang": lang,
                "latitude": latitude,
                "longitude": longitude,
                "name": name,
                "park_Id": park_id,
            }
        )
        if cv is not UNSET:
            field_dict["CV"] = cv
        if hgv is not UNSET:
            field_dict["HGV"] = hgv
        if lgv is not UNSET:
            field_dict["LGV"] = lgv
        if address is not UNSET:
            field_dict["address"] = address
        if carpark_type is not UNSET:
            field_dict["carpark_Type"] = carpark_type
        if coach is not UNSET:
            field_dict["coach"] = coach
        if contact_no is not UNSET:
            field_dict["contactNo"] = contact_no
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if district is not UNSET:
            field_dict["district"] = district
        if facilities is not UNSET:
            field_dict["facilities"] = facilities
        if grace_periods is not UNSET:
            field_dict["gracePeriods"] = grace_periods
        if height_limits is not UNSET:
            field_dict["heightLimits"] = height_limits
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if motor_cycle is not UNSET:
            field_dict["motorCycle"] = motor_cycle
        if nature is not UNSET:
            field_dict["nature"] = nature
        if opening_hours is not UNSET:
            field_dict["openingHours"] = opening_hours
        if opening_status is not UNSET:
            field_dict["opening_status"] = opening_status
        if payment_methods is not UNSET:
            field_dict["paymentMethods"] = payment_methods
        if private_car is not UNSET:
            field_dict["privateCar"] = private_car
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if rendition_urls is not UNSET:
            field_dict["renditionUrls"] = rendition_urls
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grace_period import GracePeriod
        from ..models.height_limit import HeightLimit
        from ..models.opening_hour import OpeningHour
        from ..models.rendition_urls import RenditionUrls
        from ..models.vehicle_information import VehicleInformation

        d = dict(src_dict)
        display_address = d.pop("displayAddress")

        lang = check_carpark_info_lang(d.pop("lang"))

        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        name = d.pop("name")

        park_id = d.pop("park_Id")

        _cv = d.pop("CV", UNSET)
        cv: VehicleInformation | Unset
        if isinstance(_cv, Unset):
            cv = UNSET
        else:
            cv = VehicleInformation.from_dict(_cv)

        _hgv = d.pop("HGV", UNSET)
        hgv: VehicleInformation | Unset
        if isinstance(_hgv, Unset):
            hgv = UNSET
        else:
            hgv = VehicleInformation.from_dict(_hgv)

        _lgv = d.pop("LGV", UNSET)
        lgv: VehicleInformation | Unset
        if isinstance(_lgv, Unset):
            lgv = UNSET
        else:
            lgv = VehicleInformation.from_dict(_lgv)

        def _parse_address(data: object) -> Any | Unset:
            if isinstance(data, Unset):
                return data
            return cast(Any | Unset, data)

        address = _parse_address(d.pop("address", UNSET))

        carpark_type = d.pop("carpark_Type", UNSET)

        _coach = d.pop("coach", UNSET)
        coach: VehicleInformation | Unset
        if isinstance(_coach, Unset):
            coach = UNSET
        else:
            coach = VehicleInformation.from_dict(_coach)

        contact_no = d.pop("contactNo", UNSET)

        creation_date = d.pop("creationDate", UNSET)

        district = d.pop("district", UNSET)

        facilities = cast(list[str], d.pop("facilities", UNSET))

        _grace_periods = d.pop("gracePeriods", UNSET)
        grace_periods: list[GracePeriod] | Unset = UNSET
        if _grace_periods is not UNSET:
            grace_periods = []
            for grace_periods_item_data in _grace_periods:
                grace_periods_item = GracePeriod.from_dict(grace_periods_item_data)

                grace_periods.append(grace_periods_item)

        _height_limits = d.pop("heightLimits", UNSET)
        height_limits: list[HeightLimit] | Unset = UNSET
        if _height_limits is not UNSET:
            height_limits = []
            for height_limits_item_data in _height_limits:
                height_limits_item = HeightLimit.from_dict(height_limits_item_data)

                height_limits.append(height_limits_item)

        modified_date = d.pop("modifiedDate", UNSET)

        _motor_cycle = d.pop("motorCycle", UNSET)
        motor_cycle: VehicleInformation | Unset
        if isinstance(_motor_cycle, Unset):
            motor_cycle = UNSET
        else:
            motor_cycle = VehicleInformation.from_dict(_motor_cycle)

        nature = d.pop("nature", UNSET)

        _opening_hours = d.pop("openingHours", UNSET)
        opening_hours: list[OpeningHour] | Unset = UNSET
        if _opening_hours is not UNSET:
            opening_hours = []
            for opening_hours_item_data in _opening_hours:
                opening_hours_item = OpeningHour.from_dict(opening_hours_item_data)

                opening_hours.append(opening_hours_item)

        opening_status = d.pop("opening_status", UNSET)

        payment_methods = cast(list[str], d.pop("paymentMethods", UNSET))

        _private_car = d.pop("privateCar", UNSET)
        private_car: VehicleInformation | Unset
        if isinstance(_private_car, Unset):
            private_car = UNSET
        else:
            private_car = VehicleInformation.from_dict(_private_car)

        published_date = d.pop("publishedDate", UNSET)

        _rendition_urls = d.pop("renditionUrls", UNSET)
        rendition_urls: RenditionUrls | Unset
        if isinstance(_rendition_urls, Unset):
            rendition_urls = UNSET
        else:
            rendition_urls = RenditionUrls.from_dict(_rendition_urls)

        website = d.pop("website", UNSET)

        carpark_info = cls(
            display_address=display_address,
            lang=lang,
            latitude=latitude,
            longitude=longitude,
            name=name,
            park_id=park_id,
            cv=cv,
            hgv=hgv,
            lgv=lgv,
            address=address,
            carpark_type=carpark_type,
            coach=coach,
            contact_no=contact_no,
            creation_date=creation_date,
            district=district,
            facilities=facilities,
            grace_periods=grace_periods,
            height_limits=height_limits,
            modified_date=modified_date,
            motor_cycle=motor_cycle,
            nature=nature,
            opening_hours=opening_hours,
            opening_status=opening_status,
            payment_methods=payment_methods,
            private_car=private_car,
            published_date=published_date,
            rendition_urls=rendition_urls,
            website=website,
        )

        carpark_info.additional_properties = d
        return carpark_info

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
