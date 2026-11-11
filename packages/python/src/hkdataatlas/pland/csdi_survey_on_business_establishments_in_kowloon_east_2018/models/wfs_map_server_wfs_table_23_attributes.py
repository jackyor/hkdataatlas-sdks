from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsTable23Attributes")


@_attrs_define
class WfsMapServerWfsTable23Attributes:
    """
    Attributes:
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        area_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        manufacturing (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        construction (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        import_export_trades (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        restaurants_hotels (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        transportation_storage (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        telecommunications_services (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from
            XML occurrence into all JSON queries.
        banking (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        banking_set_up_insurance_agents (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        banking_excluding_insurance_agents (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected
            from XML occurrence into all JSON queries.
        real_estate (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence
            into all JSON queries.
        publishing (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into
            all JSON queries.
        healthcare_services (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        social_personal_services (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
        waste_management (int | None | Unset): Native XSD type xsd:int. Requiredness is not projected from XML
            occurrence into all JSON queries.
    """

    objectid: int | Unset = UNSET
    area_en: None | str | Unset = UNSET
    manufacturing: int | None | Unset = UNSET
    construction: int | None | Unset = UNSET
    import_export_trades: int | None | Unset = UNSET
    restaurants_hotels: int | None | Unset = UNSET
    transportation_storage: int | None | Unset = UNSET
    telecommunications_services: int | None | Unset = UNSET
    banking: int | None | Unset = UNSET
    banking_set_up_insurance_agents: int | None | Unset = UNSET
    banking_excluding_insurance_agents: int | None | Unset = UNSET
    real_estate: int | None | Unset = UNSET
    publishing: int | None | Unset = UNSET
    healthcare_services: int | None | Unset = UNSET
    social_personal_services: int | None | Unset = UNSET
    waste_management: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        area_en: None | str | Unset
        if isinstance(self.area_en, Unset):
            area_en = UNSET
        else:
            area_en = self.area_en

        manufacturing: int | None | Unset
        if isinstance(self.manufacturing, Unset):
            manufacturing = UNSET
        else:
            manufacturing = self.manufacturing

        construction: int | None | Unset
        if isinstance(self.construction, Unset):
            construction = UNSET
        else:
            construction = self.construction

        import_export_trades: int | None | Unset
        if isinstance(self.import_export_trades, Unset):
            import_export_trades = UNSET
        else:
            import_export_trades = self.import_export_trades

        restaurants_hotels: int | None | Unset
        if isinstance(self.restaurants_hotels, Unset):
            restaurants_hotels = UNSET
        else:
            restaurants_hotels = self.restaurants_hotels

        transportation_storage: int | None | Unset
        if isinstance(self.transportation_storage, Unset):
            transportation_storage = UNSET
        else:
            transportation_storage = self.transportation_storage

        telecommunications_services: int | None | Unset
        if isinstance(self.telecommunications_services, Unset):
            telecommunications_services = UNSET
        else:
            telecommunications_services = self.telecommunications_services

        banking: int | None | Unset
        if isinstance(self.banking, Unset):
            banking = UNSET
        else:
            banking = self.banking

        banking_set_up_insurance_agents: int | None | Unset
        if isinstance(self.banking_set_up_insurance_agents, Unset):
            banking_set_up_insurance_agents = UNSET
        else:
            banking_set_up_insurance_agents = self.banking_set_up_insurance_agents

        banking_excluding_insurance_agents: int | None | Unset
        if isinstance(self.banking_excluding_insurance_agents, Unset):
            banking_excluding_insurance_agents = UNSET
        else:
            banking_excluding_insurance_agents = self.banking_excluding_insurance_agents

        real_estate: int | None | Unset
        if isinstance(self.real_estate, Unset):
            real_estate = UNSET
        else:
            real_estate = self.real_estate

        publishing: int | None | Unset
        if isinstance(self.publishing, Unset):
            publishing = UNSET
        else:
            publishing = self.publishing

        healthcare_services: int | None | Unset
        if isinstance(self.healthcare_services, Unset):
            healthcare_services = UNSET
        else:
            healthcare_services = self.healthcare_services

        social_personal_services: int | None | Unset
        if isinstance(self.social_personal_services, Unset):
            social_personal_services = UNSET
        else:
            social_personal_services = self.social_personal_services

        waste_management: int | None | Unset
        if isinstance(self.waste_management, Unset):
            waste_management = UNSET
        else:
            waste_management = self.waste_management

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if area_en is not UNSET:
            field_dict["Area_En"] = area_en
        if manufacturing is not UNSET:
            field_dict["Manufacturing"] = manufacturing
        if construction is not UNSET:
            field_dict["Construction"] = construction
        if import_export_trades is not UNSET:
            field_dict["Import_export_trades"] = import_export_trades
        if restaurants_hotels is not UNSET:
            field_dict["Restaurants_hotels"] = restaurants_hotels
        if transportation_storage is not UNSET:
            field_dict["Transportation_storage"] = transportation_storage
        if telecommunications_services is not UNSET:
            field_dict["Telecommunications_services"] = telecommunications_services
        if banking is not UNSET:
            field_dict["Banking"] = banking
        if banking_set_up_insurance_agents is not UNSET:
            field_dict["Banking_set_up_insurance_agents"] = (
                banking_set_up_insurance_agents
            )
        if banking_excluding_insurance_agents is not UNSET:
            field_dict["Banking_excluding_insurance_agents"] = (
                banking_excluding_insurance_agents
            )
        if real_estate is not UNSET:
            field_dict["Real_estate"] = real_estate
        if publishing is not UNSET:
            field_dict["Publishing"] = publishing
        if healthcare_services is not UNSET:
            field_dict["Healthcare_services"] = healthcare_services
        if social_personal_services is not UNSET:
            field_dict["Social_personal_services"] = social_personal_services
        if waste_management is not UNSET:
            field_dict["Waste_management"] = waste_management

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_area_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        area_en = _parse_area_en(d.pop("Area_En", UNSET))

        def _parse_manufacturing(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        manufacturing = _parse_manufacturing(d.pop("Manufacturing", UNSET))

        def _parse_construction(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        construction = _parse_construction(d.pop("Construction", UNSET))

        def _parse_import_export_trades(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        import_export_trades = _parse_import_export_trades(
            d.pop("Import_export_trades", UNSET)
        )

        def _parse_restaurants_hotels(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        restaurants_hotels = _parse_restaurants_hotels(
            d.pop("Restaurants_hotels", UNSET)
        )

        def _parse_transportation_storage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        transportation_storage = _parse_transportation_storage(
            d.pop("Transportation_storage", UNSET)
        )

        def _parse_telecommunications_services(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        telecommunications_services = _parse_telecommunications_services(
            d.pop("Telecommunications_services", UNSET)
        )

        def _parse_banking(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        banking = _parse_banking(d.pop("Banking", UNSET))

        def _parse_banking_set_up_insurance_agents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        banking_set_up_insurance_agents = _parse_banking_set_up_insurance_agents(
            d.pop("Banking_set_up_insurance_agents", UNSET)
        )

        def _parse_banking_excluding_insurance_agents(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        banking_excluding_insurance_agents = _parse_banking_excluding_insurance_agents(
            d.pop("Banking_excluding_insurance_agents", UNSET)
        )

        def _parse_real_estate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        real_estate = _parse_real_estate(d.pop("Real_estate", UNSET))

        def _parse_publishing(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        publishing = _parse_publishing(d.pop("Publishing", UNSET))

        def _parse_healthcare_services(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        healthcare_services = _parse_healthcare_services(
            d.pop("Healthcare_services", UNSET)
        )

        def _parse_social_personal_services(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        social_personal_services = _parse_social_personal_services(
            d.pop("Social_personal_services", UNSET)
        )

        def _parse_waste_management(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        waste_management = _parse_waste_management(d.pop("Waste_management", UNSET))

        wfs_map_server_wfs_table_23_attributes = cls(
            objectid=objectid,
            area_en=area_en,
            manufacturing=manufacturing,
            construction=construction,
            import_export_trades=import_export_trades,
            restaurants_hotels=restaurants_hotels,
            transportation_storage=transportation_storage,
            telecommunications_services=telecommunications_services,
            banking=banking,
            banking_set_up_insurance_agents=banking_set_up_insurance_agents,
            banking_excluding_insurance_agents=banking_excluding_insurance_agents,
            real_estate=real_estate,
            publishing=publishing,
            healthcare_services=healthcare_services,
            social_personal_services=social_personal_services,
            waste_management=waste_management,
        )

        wfs_map_server_wfs_table_23_attributes.additional_properties = d
        return wfs_map_server_wfs_table_23_attributes

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
