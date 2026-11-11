from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aed_csv_fields_ground_level_category import (
    AedCsvFieldsGroundLevelCategory,
    check_aed_csv_fields_ground_level_category,
)
from ..models.aed_csv_fields_person_allowed_to_operate import (
    AedCsvFieldsPersonAllowedToOperate,
    check_aed_csv_fields_person_allowed_to_operate,
)
from ..models.aed_csv_fields_person_with_access import (
    AedCsvFieldsPersonWithAccess,
    check_aed_csv_fields_person_with_access,
)
from ..models.aed_csv_fields_usable_by_anyone import (
    AedCsvFieldsUsableByAnyone,
    check_aed_csv_fields_usable_by_anyone,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AedCsvFields")


@_attrs_define
class AedCsvFields:
    """Field dictionary for the CSV structure, represented as conceptual fields because the source does not establish exact
    CSV header names or quoting conventions. The data dictionary identifies an item containing the following
    information. These are documented field descriptions, not a guarantee that every field is populated in every record.

        Attributes:
            aed_address (str | Unset): Detailed address of the AED.
            aed_brand (str | Unset): Brand name of the AED.
            aed_model (str | Unset): Model of the AED.
            aed_name (str | Unset): Name of the location where the AED is installed.
            aed_remark (str | Unset): Other remark.
            detailed_location (str | Unset): Exact location of the AED installed.
            ground_level_category (AedCsvFieldsGroundLevelCategory | Unset): Whether the AED is installed at ground level.
                Documented values: Street Level or Non-Street Level.
            latitude (float | Unset): Latitude of the WGS84 coordinate system. The source declares Decimal.
            longitude (float | Unset): Longitude of the WGS84 coordinate system. The source declares Decimal.
            person_allowed_to_operate (AedCsvFieldsPersonAllowedToOperate | Unset): Type of people allowed to operate the
                AED. Documented values: Anyone, Staff Only, Trained Personnel Only, or Trained Staff Only.
            person_with_access (AedCsvFieldsPersonWithAccess | Unset): Person who has access to the AED. Documented values:
                Anyone, Staff Only, Accompanied By Staff Only, Teaching And Non-Teaching Staff, or Trained Staff Only.
            service_hour_remark (str | Unset): The service hour that the AED is accessible.
            usable_by_anyone (AedCsvFieldsUsableByAnyone | Unset): Indicates whether the AED can be used by anybody.
                Documented values: Yes or No.
    """

    aed_address: str | Unset = UNSET
    aed_brand: str | Unset = UNSET
    aed_model: str | Unset = UNSET
    aed_name: str | Unset = UNSET
    aed_remark: str | Unset = UNSET
    detailed_location: str | Unset = UNSET
    ground_level_category: AedCsvFieldsGroundLevelCategory | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    person_allowed_to_operate: AedCsvFieldsPersonAllowedToOperate | Unset = UNSET
    person_with_access: AedCsvFieldsPersonWithAccess | Unset = UNSET
    service_hour_remark: str | Unset = UNSET
    usable_by_anyone: AedCsvFieldsUsableByAnyone | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aed_address = self.aed_address

        aed_brand = self.aed_brand

        aed_model = self.aed_model

        aed_name = self.aed_name

        aed_remark = self.aed_remark

        detailed_location = self.detailed_location

        ground_level_category: str | Unset = UNSET
        if not isinstance(self.ground_level_category, Unset):
            ground_level_category = self.ground_level_category

        latitude = self.latitude

        longitude = self.longitude

        person_allowed_to_operate: str | Unset = UNSET
        if not isinstance(self.person_allowed_to_operate, Unset):
            person_allowed_to_operate = self.person_allowed_to_operate

        person_with_access: str | Unset = UNSET
        if not isinstance(self.person_with_access, Unset):
            person_with_access = self.person_with_access

        service_hour_remark = self.service_hour_remark

        usable_by_anyone: str | Unset = UNSET
        if not isinstance(self.usable_by_anyone, Unset):
            usable_by_anyone = self.usable_by_anyone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aed_address is not UNSET:
            field_dict["aedAddress"] = aed_address
        if aed_brand is not UNSET:
            field_dict["aedBrand"] = aed_brand
        if aed_model is not UNSET:
            field_dict["aedModel"] = aed_model
        if aed_name is not UNSET:
            field_dict["aedName"] = aed_name
        if aed_remark is not UNSET:
            field_dict["aedRemark"] = aed_remark
        if detailed_location is not UNSET:
            field_dict["detailedLocation"] = detailed_location
        if ground_level_category is not UNSET:
            field_dict["groundLevelCategory"] = ground_level_category
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if person_allowed_to_operate is not UNSET:
            field_dict["personAllowedToOperate"] = person_allowed_to_operate
        if person_with_access is not UNSET:
            field_dict["personWithAccess"] = person_with_access
        if service_hour_remark is not UNSET:
            field_dict["serviceHourRemark"] = service_hour_remark
        if usable_by_anyone is not UNSET:
            field_dict["usableByAnyone"] = usable_by_anyone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        aed_address = d.pop("aedAddress", UNSET)

        aed_brand = d.pop("aedBrand", UNSET)

        aed_model = d.pop("aedModel", UNSET)

        aed_name = d.pop("aedName", UNSET)

        aed_remark = d.pop("aedRemark", UNSET)

        detailed_location = d.pop("detailedLocation", UNSET)

        _ground_level_category = d.pop("groundLevelCategory", UNSET)
        ground_level_category: AedCsvFieldsGroundLevelCategory | Unset
        if isinstance(_ground_level_category, Unset):
            ground_level_category = UNSET
        else:
            ground_level_category = check_aed_csv_fields_ground_level_category(
                _ground_level_category
            )

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        _person_allowed_to_operate = d.pop("personAllowedToOperate", UNSET)
        person_allowed_to_operate: AedCsvFieldsPersonAllowedToOperate | Unset
        if isinstance(_person_allowed_to_operate, Unset):
            person_allowed_to_operate = UNSET
        else:
            person_allowed_to_operate = check_aed_csv_fields_person_allowed_to_operate(
                _person_allowed_to_operate
            )

        _person_with_access = d.pop("personWithAccess", UNSET)
        person_with_access: AedCsvFieldsPersonWithAccess | Unset
        if isinstance(_person_with_access, Unset):
            person_with_access = UNSET
        else:
            person_with_access = check_aed_csv_fields_person_with_access(
                _person_with_access
            )

        service_hour_remark = d.pop("serviceHourRemark", UNSET)

        _usable_by_anyone = d.pop("usableByAnyone", UNSET)
        usable_by_anyone: AedCsvFieldsUsableByAnyone | Unset
        if isinstance(_usable_by_anyone, Unset):
            usable_by_anyone = UNSET
        else:
            usable_by_anyone = check_aed_csv_fields_usable_by_anyone(_usable_by_anyone)

        aed_csv_fields = cls(
            aed_address=aed_address,
            aed_brand=aed_brand,
            aed_model=aed_model,
            aed_name=aed_name,
            aed_remark=aed_remark,
            detailed_location=detailed_location,
            ground_level_category=ground_level_category,
            latitude=latitude,
            longitude=longitude,
            person_allowed_to_operate=person_allowed_to_operate,
            person_with_access=person_with_access,
            service_hour_remark=service_hour_remark,
            usable_by_anyone=usable_by_anyone,
        )

        aed_csv_fields.additional_properties = d
        return aed_csv_fields

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
