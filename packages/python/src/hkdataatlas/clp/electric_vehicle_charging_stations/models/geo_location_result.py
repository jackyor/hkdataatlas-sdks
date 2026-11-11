from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.charger import Charger


T = TypeVar("T", bound="GeoLocationResult")


@_attrs_define
class GeoLocationResult:
    """
    Attributes:
        charger_list (list[Charger] | Unset): List of charger objects.
        detailed_address (str | Unset): Full address of the location.
        distance (str | Unset): Distance from the location of access versus the charging station. The dictionary says
            this is currently a placeholder and that actual distance logic may be added later; the sample shows "0".
        district_item_id (str | Unset): Identifier for the district.
        item_id (str | Unset): Unique identifier.
        last_update (str | Unset): Last update timestamp for the location. Dictionary labels this as date; its sample is
            a date-time string (2025-12-08 15:36:04), so no specific format is asserted.
        latitude (float | Unset): Latitude in decimal degrees (for example, 22.3193).
        longitude (float | Unset): Longitude in decimal degrees (for example, 114.1694).
        provider (str | Unset): Documented value: CLP.
        status (str | Unset): Location status. Documented values: Status_Not_Available, Charging_Not_Available,
            Charging_Available.
        title (str | Unset): Item title.
        total_number_of_available_charger (int | Unset): Number of available chargers.
        total_number_of_available_quick_charger (int | Unset): Number of available quick chargers.
        total_number_of_available_semi_quick_charger (int | Unset): Number of available semi-quick chargers.
        total_number_of_charger (int | Unset): Total number of chargers at the location.
        total_number_of_not_available_charger (int | Unset): Dictionary description: number of not-available semi-quick
            chargers. The field name suggests a total across charger types; the documented wording is retained as written.
        total_number_of_not_available_quick_charger (int | Unset): Number of not-available quick chargers.
        total_number_of_not_available_semi_quick_charger (int | Unset): Number of not-available semi-quick chargers.
        total_number_of_out_of_service_charger (int | Unset): Number of out-of-service chargers.
        total_number_of_out_of_service_quick_charger (int | Unset): Number of out-of-service quick chargers.
        total_number_of_out_of_service_semi_quick_charger (int | Unset): Number of out-of-service semi-quick chargers.
        total_number_of_quick_charger (int | Unset): Total number of quick chargers.
        total_number_of_semi_quick_charger (int | Unset): Total number of semi-quick chargers.
        total_number_of_status_not_available_charger (int | Unset): Number of chargers with status not available.
    """

    charger_list: list[Charger] | Unset = UNSET
    detailed_address: str | Unset = UNSET
    distance: str | Unset = UNSET
    district_item_id: str | Unset = UNSET
    item_id: str | Unset = UNSET
    last_update: str | Unset = UNSET
    latitude: float | Unset = UNSET
    longitude: float | Unset = UNSET
    provider: str | Unset = UNSET
    status: str | Unset = UNSET
    title: str | Unset = UNSET
    total_number_of_available_charger: int | Unset = UNSET
    total_number_of_available_quick_charger: int | Unset = UNSET
    total_number_of_available_semi_quick_charger: int | Unset = UNSET
    total_number_of_charger: int | Unset = UNSET
    total_number_of_not_available_charger: int | Unset = UNSET
    total_number_of_not_available_quick_charger: int | Unset = UNSET
    total_number_of_not_available_semi_quick_charger: int | Unset = UNSET
    total_number_of_out_of_service_charger: int | Unset = UNSET
    total_number_of_out_of_service_quick_charger: int | Unset = UNSET
    total_number_of_out_of_service_semi_quick_charger: int | Unset = UNSET
    total_number_of_quick_charger: int | Unset = UNSET
    total_number_of_semi_quick_charger: int | Unset = UNSET
    total_number_of_status_not_available_charger: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charger_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.charger_list, Unset):
            charger_list = []
            for charger_list_item_data in self.charger_list:
                charger_list_item = charger_list_item_data.to_dict()
                charger_list.append(charger_list_item)

        detailed_address = self.detailed_address

        distance = self.distance

        district_item_id = self.district_item_id

        item_id = self.item_id

        last_update = self.last_update

        latitude = self.latitude

        longitude = self.longitude

        provider = self.provider

        status = self.status

        title = self.title

        total_number_of_available_charger = self.total_number_of_available_charger

        total_number_of_available_quick_charger = (
            self.total_number_of_available_quick_charger
        )

        total_number_of_available_semi_quick_charger = (
            self.total_number_of_available_semi_quick_charger
        )

        total_number_of_charger = self.total_number_of_charger

        total_number_of_not_available_charger = (
            self.total_number_of_not_available_charger
        )

        total_number_of_not_available_quick_charger = (
            self.total_number_of_not_available_quick_charger
        )

        total_number_of_not_available_semi_quick_charger = (
            self.total_number_of_not_available_semi_quick_charger
        )

        total_number_of_out_of_service_charger = (
            self.total_number_of_out_of_service_charger
        )

        total_number_of_out_of_service_quick_charger = (
            self.total_number_of_out_of_service_quick_charger
        )

        total_number_of_out_of_service_semi_quick_charger = (
            self.total_number_of_out_of_service_semi_quick_charger
        )

        total_number_of_quick_charger = self.total_number_of_quick_charger

        total_number_of_semi_quick_charger = self.total_number_of_semi_quick_charger

        total_number_of_status_not_available_charger = (
            self.total_number_of_status_not_available_charger
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if charger_list is not UNSET:
            field_dict["chargerList"] = charger_list
        if detailed_address is not UNSET:
            field_dict["detailedAddress"] = detailed_address
        if distance is not UNSET:
            field_dict["distance"] = distance
        if district_item_id is not UNSET:
            field_dict["districtItemId"] = district_item_id
        if item_id is not UNSET:
            field_dict["itemId"] = item_id
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if provider is not UNSET:
            field_dict["provider"] = provider
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if total_number_of_available_charger is not UNSET:
            field_dict["totalNumberOfAvailableCharger"] = (
                total_number_of_available_charger
            )
        if total_number_of_available_quick_charger is not UNSET:
            field_dict["totalNumberOfAvailableQuickCharger"] = (
                total_number_of_available_quick_charger
            )
        if total_number_of_available_semi_quick_charger is not UNSET:
            field_dict["totalNumberOfAvailableSemiQuickCharger"] = (
                total_number_of_available_semi_quick_charger
            )
        if total_number_of_charger is not UNSET:
            field_dict["totalNumberOfCharger"] = total_number_of_charger
        if total_number_of_not_available_charger is not UNSET:
            field_dict["totalNumberOfNotAvailableCharger"] = (
                total_number_of_not_available_charger
            )
        if total_number_of_not_available_quick_charger is not UNSET:
            field_dict["totalNumberOfNotAvailableQuickCharger"] = (
                total_number_of_not_available_quick_charger
            )
        if total_number_of_not_available_semi_quick_charger is not UNSET:
            field_dict["totalNumberOfNotAvailableSemiQuickCharger"] = (
                total_number_of_not_available_semi_quick_charger
            )
        if total_number_of_out_of_service_charger is not UNSET:
            field_dict["totalNumberOfOutOfServiceCharger"] = (
                total_number_of_out_of_service_charger
            )
        if total_number_of_out_of_service_quick_charger is not UNSET:
            field_dict["totalNumberOfOutOfServiceQuickCharger"] = (
                total_number_of_out_of_service_quick_charger
            )
        if total_number_of_out_of_service_semi_quick_charger is not UNSET:
            field_dict["totalNumberOfOutOfServiceSemiQuickCharger"] = (
                total_number_of_out_of_service_semi_quick_charger
            )
        if total_number_of_quick_charger is not UNSET:
            field_dict["totalNumberOfQuickCharger"] = total_number_of_quick_charger
        if total_number_of_semi_quick_charger is not UNSET:
            field_dict["totalNumberOfSemiQuickCharger"] = (
                total_number_of_semi_quick_charger
            )
        if total_number_of_status_not_available_charger is not UNSET:
            field_dict["totalNumberOfStatusNotAvailableCharger"] = (
                total_number_of_status_not_available_charger
            )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.charger import Charger

        d = dict(src_dict)
        _charger_list = d.pop("chargerList", UNSET)
        charger_list: list[Charger] | Unset = UNSET
        if _charger_list is not UNSET:
            charger_list = []
            for charger_list_item_data in _charger_list:
                charger_list_item = Charger.from_dict(charger_list_item_data)

                charger_list.append(charger_list_item)

        detailed_address = d.pop("detailedAddress", UNSET)

        distance = d.pop("distance", UNSET)

        district_item_id = d.pop("districtItemId", UNSET)

        item_id = d.pop("itemId", UNSET)

        last_update = d.pop("lastUpdate", UNSET)

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        provider = d.pop("provider", UNSET)

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        total_number_of_available_charger = d.pop(
            "totalNumberOfAvailableCharger", UNSET
        )

        total_number_of_available_quick_charger = d.pop(
            "totalNumberOfAvailableQuickCharger", UNSET
        )

        total_number_of_available_semi_quick_charger = d.pop(
            "totalNumberOfAvailableSemiQuickCharger", UNSET
        )

        total_number_of_charger = d.pop("totalNumberOfCharger", UNSET)

        total_number_of_not_available_charger = d.pop(
            "totalNumberOfNotAvailableCharger", UNSET
        )

        total_number_of_not_available_quick_charger = d.pop(
            "totalNumberOfNotAvailableQuickCharger", UNSET
        )

        total_number_of_not_available_semi_quick_charger = d.pop(
            "totalNumberOfNotAvailableSemiQuickCharger", UNSET
        )

        total_number_of_out_of_service_charger = d.pop(
            "totalNumberOfOutOfServiceCharger", UNSET
        )

        total_number_of_out_of_service_quick_charger = d.pop(
            "totalNumberOfOutOfServiceQuickCharger", UNSET
        )

        total_number_of_out_of_service_semi_quick_charger = d.pop(
            "totalNumberOfOutOfServiceSemiQuickCharger", UNSET
        )

        total_number_of_quick_charger = d.pop("totalNumberOfQuickCharger", UNSET)

        total_number_of_semi_quick_charger = d.pop(
            "totalNumberOfSemiQuickCharger", UNSET
        )

        total_number_of_status_not_available_charger = d.pop(
            "totalNumberOfStatusNotAvailableCharger", UNSET
        )

        geo_location_result = cls(
            charger_list=charger_list,
            detailed_address=detailed_address,
            distance=distance,
            district_item_id=district_item_id,
            item_id=item_id,
            last_update=last_update,
            latitude=latitude,
            longitude=longitude,
            provider=provider,
            status=status,
            title=title,
            total_number_of_available_charger=total_number_of_available_charger,
            total_number_of_available_quick_charger=total_number_of_available_quick_charger,
            total_number_of_available_semi_quick_charger=total_number_of_available_semi_quick_charger,
            total_number_of_charger=total_number_of_charger,
            total_number_of_not_available_charger=total_number_of_not_available_charger,
            total_number_of_not_available_quick_charger=total_number_of_not_available_quick_charger,
            total_number_of_not_available_semi_quick_charger=total_number_of_not_available_semi_quick_charger,
            total_number_of_out_of_service_charger=total_number_of_out_of_service_charger,
            total_number_of_out_of_service_quick_charger=total_number_of_out_of_service_quick_charger,
            total_number_of_out_of_service_semi_quick_charger=total_number_of_out_of_service_semi_quick_charger,
            total_number_of_quick_charger=total_number_of_quick_charger,
            total_number_of_semi_quick_charger=total_number_of_semi_quick_charger,
            total_number_of_status_not_available_charger=total_number_of_status_not_available_charger,
        )

        geo_location_result.additional_properties = d
        return geo_location_result

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
