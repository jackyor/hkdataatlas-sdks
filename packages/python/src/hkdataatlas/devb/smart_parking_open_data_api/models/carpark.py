from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.carpark_facilities_item import (
    CarparkFacilitiesItem,
    check_carpark_facilities_item,
)
from ..models.carpark_nature import CarparkNature, check_carpark_nature
from ..models.carpark_type import CarparkType, check_carpark_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.grace_period import GracePeriod
    from ..models.height_limit import HeightLimit
    from ..models.opening_hours import OpeningHours
    from ..models.rendition_urls import RenditionUrls
    from ..models.vehicle_information import VehicleInformation


T = TypeVar("T", bound="Carpark")


@_attrs_define
class Carpark:
    """Carpark structure from the field definitions. In general, a property containing an empty array or value is omitted
    from responses. Requiredness in the field dictionary describes its structure; samples are not a guarantee that every
    field appears in every response.

        Attributes:
            hgv (VehicleInformation | Unset): Fields vary by vehicle type and availability. Vacancy-only responses primarily
                provide vacancy fields; detailed information may include spaces and charges.
            lgv (VehicleInformation | Unset): Fields vary by vehicle type and availability. Vacancy-only responses primarily
                provide vacancy fields; detailed information may include spaces and charges.
            field_id (int | Unset): Mandatory system ID of carpark.
            address (Address | Unset): Address fields in the requested locale. The dictionary uses the spelling dcDestrict;
                the detailed response sample uses dcDistrict.
            closed (bool | Unset): Mandatory indication whether carpark is closed.
            coach (VehicleInformation | Unset): Fields vary by vehicle type and availability. Vacancy-only responses
                primarily provide vacancy fields; detailed information may include spaces and charges.
            contact_no (str | Unset):
            coordinates (list[float] | Unset): Mandatory longitude and latitude, in that order.
            creation_date (datetime.datetime | Unset): Creation time in UTC format; sample uses an ISO date-time.
            facilities (list[CarparkFacilitiesItem] | Unset):
            grace_periods (list[GracePeriod] | Unset):
            height_limits (list[HeightLimit] | Unset):
            input_masked (bool | Unset): Granularity of input data; field is used only by terminal.
            last_upload_date (datetime.datetime | Unset): Last data upload time from carpark owner in UTC format.
            modified_date (datetime.datetime | Unset): Last modified time in UTC format.
            motor_cycle (VehicleInformation | Unset): Fields vary by vehicle type and availability. Vacancy-only responses
                primarily provide vacancy fields; detailed information may include spaces and charges.
            name (str | Unset): Mandatory carpark name, localized when requested.
            nature (CarparkNature | Unset): Mandatory nature of carpark.
            opening_hours (list[OpeningHours] | Unset):
            output_masked (bool | Unset): Whether vacancy is quantized for display.
            payment_methods (list[str] | Unset):
            private_car (VehicleInformation | Unset): Fields vary by vehicle type and availability. Vacancy-only responses
                primarily provide vacancy fields; detailed information may include spaces and charges.
            published (bool | Unset):
            published_date (datetime.datetime | Unset): Publication time in UTC format.
            rendition_urls (RenditionUrls | Unset): Image renditions; the property is empty/omitted when the carpark has no
                photo.
            type_ (CarparkType | Unset): Mandatory carpark type.
            website (str | Unset):
    """

    hgv: VehicleInformation | Unset = UNSET
    lgv: VehicleInformation | Unset = UNSET
    field_id: int | Unset = UNSET
    address: Address | Unset = UNSET
    closed: bool | Unset = UNSET
    coach: VehicleInformation | Unset = UNSET
    contact_no: str | Unset = UNSET
    coordinates: list[float] | Unset = UNSET
    creation_date: datetime.datetime | Unset = UNSET
    facilities: list[CarparkFacilitiesItem] | Unset = UNSET
    grace_periods: list[GracePeriod] | Unset = UNSET
    height_limits: list[HeightLimit] | Unset = UNSET
    input_masked: bool | Unset = UNSET
    last_upload_date: datetime.datetime | Unset = UNSET
    modified_date: datetime.datetime | Unset = UNSET
    motor_cycle: VehicleInformation | Unset = UNSET
    name: str | Unset = UNSET
    nature: CarparkNature | Unset = UNSET
    opening_hours: list[OpeningHours] | Unset = UNSET
    output_masked: bool | Unset = UNSET
    payment_methods: list[str] | Unset = UNSET
    private_car: VehicleInformation | Unset = UNSET
    published: bool | Unset = UNSET
    published_date: datetime.datetime | Unset = UNSET
    rendition_urls: RenditionUrls | Unset = UNSET
    type_: CarparkType | Unset = UNSET
    website: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hgv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.hgv, Unset):
            hgv = self.hgv.to_dict()

        lgv: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lgv, Unset):
            lgv = self.lgv.to_dict()

        field_id = self.field_id

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        closed = self.closed

        coach: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coach, Unset):
            coach = self.coach.to_dict()

        contact_no = self.contact_no

        coordinates: list[float] | Unset = UNSET
        if not isinstance(self.coordinates, Unset):
            coordinates = []
            for coordinates_item_data in self.coordinates:
                coordinates_item: float
                coordinates_item = coordinates_item_data
                coordinates.append(coordinates_item)

        creation_date: str | Unset = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        facilities: list[str] | Unset = UNSET
        if not isinstance(self.facilities, Unset):
            facilities = []
            for facilities_item_data in self.facilities:
                facilities_item: str = facilities_item_data
                facilities.append(facilities_item)

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

        input_masked = self.input_masked

        last_upload_date: str | Unset = UNSET
        if not isinstance(self.last_upload_date, Unset):
            last_upload_date = self.last_upload_date.isoformat()

        modified_date: str | Unset = UNSET
        if not isinstance(self.modified_date, Unset):
            modified_date = self.modified_date.isoformat()

        motor_cycle: dict[str, Any] | Unset = UNSET
        if not isinstance(self.motor_cycle, Unset):
            motor_cycle = self.motor_cycle.to_dict()

        name = self.name

        nature: str | Unset = UNSET
        if not isinstance(self.nature, Unset):
            nature = self.nature

        opening_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.opening_hours, Unset):
            opening_hours = []
            for opening_hours_item_data in self.opening_hours:
                opening_hours_item = opening_hours_item_data.to_dict()
                opening_hours.append(opening_hours_item)

        output_masked = self.output_masked

        payment_methods: list[str] | Unset = UNSET
        if not isinstance(self.payment_methods, Unset):
            payment_methods = self.payment_methods

        private_car: dict[str, Any] | Unset = UNSET
        if not isinstance(self.private_car, Unset):
            private_car = self.private_car.to_dict()

        published = self.published

        published_date: str | Unset = UNSET
        if not isinstance(self.published_date, Unset):
            published_date = self.published_date.isoformat()

        rendition_urls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rendition_urls, Unset):
            rendition_urls = self.rendition_urls.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        website = self.website

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hgv is not UNSET:
            field_dict["HGV"] = hgv
        if lgv is not UNSET:
            field_dict["LGV"] = lgv
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if address is not UNSET:
            field_dict["address"] = address
        if closed is not UNSET:
            field_dict["closed"] = closed
        if coach is not UNSET:
            field_dict["coach"] = coach
        if contact_no is not UNSET:
            field_dict["contactNo"] = contact_no
        if coordinates is not UNSET:
            field_dict["coordinates"] = coordinates
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if facilities is not UNSET:
            field_dict["facilities"] = facilities
        if grace_periods is not UNSET:
            field_dict["gracePeriods"] = grace_periods
        if height_limits is not UNSET:
            field_dict["heightLimits"] = height_limits
        if input_masked is not UNSET:
            field_dict["inputMasked"] = input_masked
        if last_upload_date is not UNSET:
            field_dict["lastUploadDate"] = last_upload_date
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if motor_cycle is not UNSET:
            field_dict["motorCycle"] = motor_cycle
        if name is not UNSET:
            field_dict["name"] = name
        if nature is not UNSET:
            field_dict["nature"] = nature
        if opening_hours is not UNSET:
            field_dict["openingHours"] = opening_hours
        if output_masked is not UNSET:
            field_dict["outputMasked"] = output_masked
        if payment_methods is not UNSET:
            field_dict["paymentMethods"] = payment_methods
        if private_car is not UNSET:
            field_dict["privateCar"] = private_car
        if published is not UNSET:
            field_dict["published"] = published
        if published_date is not UNSET:
            field_dict["publishedDate"] = published_date
        if rendition_urls is not UNSET:
            field_dict["renditionUrls"] = rendition_urls
        if type_ is not UNSET:
            field_dict["type"] = type_
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.address import Address
        from ..models.grace_period import GracePeriod
        from ..models.height_limit import HeightLimit
        from ..models.opening_hours import OpeningHours
        from ..models.rendition_urls import RenditionUrls
        from ..models.vehicle_information import VehicleInformation

        d = dict(src_dict)
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

        field_id = d.pop("_id", UNSET)

        _address = d.pop("address", UNSET)
        address: Address | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        closed = d.pop("closed", UNSET)

        _coach = d.pop("coach", UNSET)
        coach: VehicleInformation | Unset
        if isinstance(_coach, Unset):
            coach = UNSET
        else:
            coach = VehicleInformation.from_dict(_coach)

        contact_no = d.pop("contactNo", UNSET)

        _coordinates = d.pop("coordinates", UNSET)
        coordinates: list[float] | Unset = UNSET
        if _coordinates is not UNSET:
            coordinates = []
            for coordinates_item_data in _coordinates:

                def _parse_coordinates_item(data: object) -> float:
                    return cast(float, data)

                coordinates_item = _parse_coordinates_item(coordinates_item_data)

                coordinates.append(coordinates_item)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: datetime.datetime | Unset
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = datetime.datetime.fromisoformat(_creation_date)

        _facilities = d.pop("facilities", UNSET)
        facilities: list[CarparkFacilitiesItem] | Unset = UNSET
        if _facilities is not UNSET:
            facilities = []
            for facilities_item_data in _facilities:
                facilities_item = check_carpark_facilities_item(facilities_item_data)

                facilities.append(facilities_item)

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

        input_masked = d.pop("inputMasked", UNSET)

        _last_upload_date = d.pop("lastUploadDate", UNSET)
        last_upload_date: datetime.datetime | Unset
        if isinstance(_last_upload_date, Unset):
            last_upload_date = UNSET
        else:
            last_upload_date = datetime.datetime.fromisoformat(_last_upload_date)

        _modified_date = d.pop("modifiedDate", UNSET)
        modified_date: datetime.datetime | Unset
        if isinstance(_modified_date, Unset):
            modified_date = UNSET
        else:
            modified_date = datetime.datetime.fromisoformat(_modified_date)

        _motor_cycle = d.pop("motorCycle", UNSET)
        motor_cycle: VehicleInformation | Unset
        if isinstance(_motor_cycle, Unset):
            motor_cycle = UNSET
        else:
            motor_cycle = VehicleInformation.from_dict(_motor_cycle)

        name = d.pop("name", UNSET)

        _nature = d.pop("nature", UNSET)
        nature: CarparkNature | Unset
        if isinstance(_nature, Unset):
            nature = UNSET
        else:
            nature = check_carpark_nature(_nature)

        _opening_hours = d.pop("openingHours", UNSET)
        opening_hours: list[OpeningHours] | Unset = UNSET
        if _opening_hours is not UNSET:
            opening_hours = []
            for opening_hours_item_data in _opening_hours:
                opening_hours_item = OpeningHours.from_dict(opening_hours_item_data)

                opening_hours.append(opening_hours_item)

        output_masked = d.pop("outputMasked", UNSET)

        payment_methods = cast(list[str], d.pop("paymentMethods", UNSET))

        _private_car = d.pop("privateCar", UNSET)
        private_car: VehicleInformation | Unset
        if isinstance(_private_car, Unset):
            private_car = UNSET
        else:
            private_car = VehicleInformation.from_dict(_private_car)

        published = d.pop("published", UNSET)

        _published_date = d.pop("publishedDate", UNSET)
        published_date: datetime.datetime | Unset
        if isinstance(_published_date, Unset):
            published_date = UNSET
        else:
            published_date = datetime.datetime.fromisoformat(_published_date)

        _rendition_urls = d.pop("renditionUrls", UNSET)
        rendition_urls: RenditionUrls | Unset
        if isinstance(_rendition_urls, Unset):
            rendition_urls = UNSET
        else:
            rendition_urls = RenditionUrls.from_dict(_rendition_urls)

        _type_ = d.pop("type", UNSET)
        type_: CarparkType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_carpark_type(_type_)

        website = d.pop("website", UNSET)

        carpark = cls(
            hgv=hgv,
            lgv=lgv,
            field_id=field_id,
            address=address,
            closed=closed,
            coach=coach,
            contact_no=contact_no,
            coordinates=coordinates,
            creation_date=creation_date,
            facilities=facilities,
            grace_periods=grace_periods,
            height_limits=height_limits,
            input_masked=input_masked,
            last_upload_date=last_upload_date,
            modified_date=modified_date,
            motor_cycle=motor_cycle,
            name=name,
            nature=nature,
            opening_hours=opening_hours,
            output_masked=output_masked,
            payment_methods=payment_methods,
            private_car=private_car,
            published=published,
            published_date=published_date,
            rendition_urls=rendition_urls,
            type_=type_,
            website=website,
        )

        carpark.additional_properties = d
        return carpark

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
