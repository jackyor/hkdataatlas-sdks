from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wfs_map_server_wfs_customer_enquiry_centre_attributes import (
        WfsMapServerWfsCustomerEnquiryCentreAttributes,
    )
    from ..models.wfs_map_server_wfs_depot_workshop_attributes import (
        WfsMapServerWfsDepotWorkshopAttributes,
    )
    from ..models.wfs_map_server_wfs_office_headquarters_attributes import (
        WfsMapServerWfsOfficeHeadquartersAttributes,
    )
    from ..models.wfs_map_server_wfs_pump_house_attributes import (
        WfsMapServerWfsPumpHouseAttributes,
    )
    from ..models.wfs_map_server_wfs_pumping_station_attributes import (
        WfsMapServerWfsPumpingStationAttributes,
    )
    from ..models.wfs_map_server_wfs_reservoir_attributes import (
        WfsMapServerWfsReservoirAttributes,
    )
    from ..models.wfs_map_server_wfs_service_reservoir_attributes import (
        WfsMapServerWfsServiceReservoirAttributes,
    )
    from ..models.wfs_map_server_wfs_water_selling_kiosk_attributes import (
        WfsMapServerWfsWaterSellingKioskAttributes,
    )
    from ..models.wfs_map_server_wfs_water_tank_attributes import (
        WfsMapServerWfsWaterTankAttributes,
    )
    from ..models.wfs_map_server_wfs_water_treatment_works_attributes import (
        WfsMapServerWfsWaterTreatmentWorksAttributes,
    )


T = TypeVar("T", bound="WfsMapServerWfsFeatureCollectionFeaturesItem")


@_attrs_define
class WfsMapServerWfsFeatureCollectionFeaturesItem:
    """
    Attributes:
        type_ (str | Unset):
        properties (Unset | WfsMapServerWfsCustomerEnquiryCentreAttributes | WfsMapServerWfsDepotWorkshopAttributes |
            WfsMapServerWfsOfficeHeadquartersAttributes | WfsMapServerWfsPumpHouseAttributes |
            WfsMapServerWfsPumpingStationAttributes | WfsMapServerWfsReservoirAttributes |
            WfsMapServerWfsServiceReservoirAttributes | WfsMapServerWfsWaterSellingKioskAttributes |
            WfsMapServerWfsWaterTankAttributes | WfsMapServerWfsWaterTreatmentWorksAttributes):
        geometry (Any | Unset): Geometry representation is not constrained by the retained attribute metadata.
    """

    type_: str | Unset = UNSET
    properties: (
        Unset
        | WfsMapServerWfsCustomerEnquiryCentreAttributes
        | WfsMapServerWfsDepotWorkshopAttributes
        | WfsMapServerWfsOfficeHeadquartersAttributes
        | WfsMapServerWfsPumpHouseAttributes
        | WfsMapServerWfsPumpingStationAttributes
        | WfsMapServerWfsReservoirAttributes
        | WfsMapServerWfsServiceReservoirAttributes
        | WfsMapServerWfsWaterSellingKioskAttributes
        | WfsMapServerWfsWaterTankAttributes
        | WfsMapServerWfsWaterTreatmentWorksAttributes
    ) = UNSET
    geometry: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wfs_map_server_wfs_customer_enquiry_centre_attributes import (
            WfsMapServerWfsCustomerEnquiryCentreAttributes,
        )
        from ..models.wfs_map_server_wfs_office_headquarters_attributes import (
            WfsMapServerWfsOfficeHeadquartersAttributes,
        )
        from ..models.wfs_map_server_wfs_pump_house_attributes import (
            WfsMapServerWfsPumpHouseAttributes,
        )
        from ..models.wfs_map_server_wfs_pumping_station_attributes import (
            WfsMapServerWfsPumpingStationAttributes,
        )
        from ..models.wfs_map_server_wfs_reservoir_attributes import (
            WfsMapServerWfsReservoirAttributes,
        )
        from ..models.wfs_map_server_wfs_service_reservoir_attributes import (
            WfsMapServerWfsServiceReservoirAttributes,
        )
        from ..models.wfs_map_server_wfs_water_selling_kiosk_attributes import (
            WfsMapServerWfsWaterSellingKioskAttributes,
        )
        from ..models.wfs_map_server_wfs_water_tank_attributes import (
            WfsMapServerWfsWaterTankAttributes,
        )
        from ..models.wfs_map_server_wfs_water_treatment_works_attributes import (
            WfsMapServerWfsWaterTreatmentWorksAttributes,
        )

        type_ = self.type_

        properties: dict[str, Any] | Unset
        if isinstance(self.properties, Unset):
            properties = UNSET
        elif (
            isinstance(self.properties, WfsMapServerWfsWaterTankAttributes)
            or isinstance(self.properties, WfsMapServerWfsWaterSellingKioskAttributes)
            or isinstance(self.properties, WfsMapServerWfsWaterTreatmentWorksAttributes)
            or isinstance(self.properties, WfsMapServerWfsServiceReservoirAttributes)
            or isinstance(self.properties, WfsMapServerWfsReservoirAttributes)
            or isinstance(self.properties, WfsMapServerWfsPumpingStationAttributes)
            or isinstance(self.properties, WfsMapServerWfsPumpHouseAttributes)
            or isinstance(self.properties, WfsMapServerWfsOfficeHeadquartersAttributes)
            or isinstance(
                self.properties, WfsMapServerWfsCustomerEnquiryCentreAttributes
            )
        ):
            properties = self.properties.to_dict()
        else:
            properties = self.properties.to_dict()

        geometry = self.geometry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if properties is not UNSET:
            field_dict["properties"] = properties
        if geometry is not UNSET:
            field_dict["geometry"] = geometry

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wfs_map_server_wfs_customer_enquiry_centre_attributes import (
            WfsMapServerWfsCustomerEnquiryCentreAttributes,
        )
        from ..models.wfs_map_server_wfs_depot_workshop_attributes import (
            WfsMapServerWfsDepotWorkshopAttributes,
        )
        from ..models.wfs_map_server_wfs_office_headquarters_attributes import (
            WfsMapServerWfsOfficeHeadquartersAttributes,
        )
        from ..models.wfs_map_server_wfs_pump_house_attributes import (
            WfsMapServerWfsPumpHouseAttributes,
        )
        from ..models.wfs_map_server_wfs_pumping_station_attributes import (
            WfsMapServerWfsPumpingStationAttributes,
        )
        from ..models.wfs_map_server_wfs_reservoir_attributes import (
            WfsMapServerWfsReservoirAttributes,
        )
        from ..models.wfs_map_server_wfs_service_reservoir_attributes import (
            WfsMapServerWfsServiceReservoirAttributes,
        )
        from ..models.wfs_map_server_wfs_water_selling_kiosk_attributes import (
            WfsMapServerWfsWaterSellingKioskAttributes,
        )
        from ..models.wfs_map_server_wfs_water_tank_attributes import (
            WfsMapServerWfsWaterTankAttributes,
        )
        from ..models.wfs_map_server_wfs_water_treatment_works_attributes import (
            WfsMapServerWfsWaterTreatmentWorksAttributes,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        def _parse_properties(
            data: object,
        ) -> (
            Unset
            | WfsMapServerWfsCustomerEnquiryCentreAttributes
            | WfsMapServerWfsDepotWorkshopAttributes
            | WfsMapServerWfsOfficeHeadquartersAttributes
            | WfsMapServerWfsPumpHouseAttributes
            | WfsMapServerWfsPumpingStationAttributes
            | WfsMapServerWfsReservoirAttributes
            | WfsMapServerWfsServiceReservoirAttributes
            | WfsMapServerWfsWaterSellingKioskAttributes
            | WfsMapServerWfsWaterTankAttributes
            | WfsMapServerWfsWaterTreatmentWorksAttributes
        ):
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_0 = WfsMapServerWfsWaterTankAttributes.from_dict(data)

                return properties_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_1 = (
                    WfsMapServerWfsWaterSellingKioskAttributes.from_dict(data)
                )

                return properties_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_2 = (
                    WfsMapServerWfsWaterTreatmentWorksAttributes.from_dict(data)
                )

                return properties_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_3 = WfsMapServerWfsServiceReservoirAttributes.from_dict(
                    data
                )

                return properties_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_4 = WfsMapServerWfsReservoirAttributes.from_dict(data)

                return properties_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_5 = WfsMapServerWfsPumpingStationAttributes.from_dict(
                    data
                )

                return properties_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_6 = WfsMapServerWfsPumpHouseAttributes.from_dict(data)

                return properties_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_7 = (
                    WfsMapServerWfsOfficeHeadquartersAttributes.from_dict(data)
                )

                return properties_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                properties_type_8 = (
                    WfsMapServerWfsCustomerEnquiryCentreAttributes.from_dict(data)
                )

                return properties_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            properties_type_9 = WfsMapServerWfsDepotWorkshopAttributes.from_dict(data)

            return properties_type_9

        properties = _parse_properties(d.pop("properties", UNSET))

        geometry = d.pop("geometry", UNSET)

        wfs_map_server_wfs_feature_collection_features_item = cls(
            type_=type_,
            properties=properties,
            geometry=geometry,
        )

        wfs_map_server_wfs_feature_collection_features_item.additional_properties = d
        return wfs_map_server_wfs_feature_collection_features_item

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
