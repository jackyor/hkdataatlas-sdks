from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsgeotaggingAttributes")


@_attrs_define
class WfsMapServerWfsgeotaggingAttributes:
    """
    Attributes:
        district_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        bank_name_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        bank_name_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        bank_name_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        type_of_machine_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        type_of_machine_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        type_of_machine_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        function_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        function_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        function_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        currencies_supported_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        currencies_supported_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        currencies_supported_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        barrier_free_access_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        barrier_free_access_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        barrier_free_access_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        network_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        network_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        network_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        address_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        service_hours_en (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        service_hours_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        service_hours_sc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        shape (Any | Unset): Native geometry property gml:PointPropertyType; JSON geometry is not inferred from its XML
            type.
    """

    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    bank_name_en: None | str | Unset = UNSET
    bank_name_tc: None | str | Unset = UNSET
    bank_name_sc: None | str | Unset = UNSET
    type_of_machine_en: None | str | Unset = UNSET
    type_of_machine_tc: None | str | Unset = UNSET
    type_of_machine_sc: None | str | Unset = UNSET
    function_en: None | str | Unset = UNSET
    function_tc: None | str | Unset = UNSET
    function_sc: None | str | Unset = UNSET
    currencies_supported_en: None | str | Unset = UNSET
    currencies_supported_tc: None | str | Unset = UNSET
    currencies_supported_sc: None | str | Unset = UNSET
    barrier_free_access_en: None | str | Unset = UNSET
    barrier_free_access_tc: None | str | Unset = UNSET
    barrier_free_access_sc: None | str | Unset = UNSET
    network_en: None | str | Unset = UNSET
    network_tc: None | str | Unset = UNSET
    network_sc: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    service_hours_en: None | str | Unset = UNSET
    service_hours_tc: None | str | Unset = UNSET
    service_hours_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    shape: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        district_en: None | str | Unset
        if isinstance(self.district_en, Unset):
            district_en = UNSET
        else:
            district_en = self.district_en

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

        bank_name_en: None | str | Unset
        if isinstance(self.bank_name_en, Unset):
            bank_name_en = UNSET
        else:
            bank_name_en = self.bank_name_en

        bank_name_tc: None | str | Unset
        if isinstance(self.bank_name_tc, Unset):
            bank_name_tc = UNSET
        else:
            bank_name_tc = self.bank_name_tc

        bank_name_sc: None | str | Unset
        if isinstance(self.bank_name_sc, Unset):
            bank_name_sc = UNSET
        else:
            bank_name_sc = self.bank_name_sc

        type_of_machine_en: None | str | Unset
        if isinstance(self.type_of_machine_en, Unset):
            type_of_machine_en = UNSET
        else:
            type_of_machine_en = self.type_of_machine_en

        type_of_machine_tc: None | str | Unset
        if isinstance(self.type_of_machine_tc, Unset):
            type_of_machine_tc = UNSET
        else:
            type_of_machine_tc = self.type_of_machine_tc

        type_of_machine_sc: None | str | Unset
        if isinstance(self.type_of_machine_sc, Unset):
            type_of_machine_sc = UNSET
        else:
            type_of_machine_sc = self.type_of_machine_sc

        function_en: None | str | Unset
        if isinstance(self.function_en, Unset):
            function_en = UNSET
        else:
            function_en = self.function_en

        function_tc: None | str | Unset
        if isinstance(self.function_tc, Unset):
            function_tc = UNSET
        else:
            function_tc = self.function_tc

        function_sc: None | str | Unset
        if isinstance(self.function_sc, Unset):
            function_sc = UNSET
        else:
            function_sc = self.function_sc

        currencies_supported_en: None | str | Unset
        if isinstance(self.currencies_supported_en, Unset):
            currencies_supported_en = UNSET
        else:
            currencies_supported_en = self.currencies_supported_en

        currencies_supported_tc: None | str | Unset
        if isinstance(self.currencies_supported_tc, Unset):
            currencies_supported_tc = UNSET
        else:
            currencies_supported_tc = self.currencies_supported_tc

        currencies_supported_sc: None | str | Unset
        if isinstance(self.currencies_supported_sc, Unset):
            currencies_supported_sc = UNSET
        else:
            currencies_supported_sc = self.currencies_supported_sc

        barrier_free_access_en: None | str | Unset
        if isinstance(self.barrier_free_access_en, Unset):
            barrier_free_access_en = UNSET
        else:
            barrier_free_access_en = self.barrier_free_access_en

        barrier_free_access_tc: None | str | Unset
        if isinstance(self.barrier_free_access_tc, Unset):
            barrier_free_access_tc = UNSET
        else:
            barrier_free_access_tc = self.barrier_free_access_tc

        barrier_free_access_sc: None | str | Unset
        if isinstance(self.barrier_free_access_sc, Unset):
            barrier_free_access_sc = UNSET
        else:
            barrier_free_access_sc = self.barrier_free_access_sc

        network_en: None | str | Unset
        if isinstance(self.network_en, Unset):
            network_en = UNSET
        else:
            network_en = self.network_en

        network_tc: None | str | Unset
        if isinstance(self.network_tc, Unset):
            network_tc = UNSET
        else:
            network_tc = self.network_tc

        network_sc: None | str | Unset
        if isinstance(self.network_sc, Unset):
            network_sc = UNSET
        else:
            network_sc = self.network_sc

        address_en: None | str | Unset
        if isinstance(self.address_en, Unset):
            address_en = UNSET
        else:
            address_en = self.address_en

        address_tc: None | str | Unset
        if isinstance(self.address_tc, Unset):
            address_tc = UNSET
        else:
            address_tc = self.address_tc

        address_sc: None | str | Unset
        if isinstance(self.address_sc, Unset):
            address_sc = UNSET
        else:
            address_sc = self.address_sc

        service_hours_en: None | str | Unset
        if isinstance(self.service_hours_en, Unset):
            service_hours_en = UNSET
        else:
            service_hours_en = self.service_hours_en

        service_hours_tc: None | str | Unset
        if isinstance(self.service_hours_tc, Unset):
            service_hours_tc = UNSET
        else:
            service_hours_tc = self.service_hours_tc

        service_hours_sc: None | str | Unset
        if isinstance(self.service_hours_sc, Unset):
            service_hours_sc = UNSET
        else:
            service_hours_sc = self.service_hours_sc

        objectid = self.objectid

        shape = self.shape

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if district_en is not UNSET:
            field_dict["District_EN"] = district_en
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if district_sc is not UNSET:
            field_dict["District_SC"] = district_sc
        if bank_name_en is not UNSET:
            field_dict["BankName_EN"] = bank_name_en
        if bank_name_tc is not UNSET:
            field_dict["BankName_TC"] = bank_name_tc
        if bank_name_sc is not UNSET:
            field_dict["BankName_SC"] = bank_name_sc
        if type_of_machine_en is not UNSET:
            field_dict["TypeOfMachine_EN"] = type_of_machine_en
        if type_of_machine_tc is not UNSET:
            field_dict["TypeOfMachine_TC"] = type_of_machine_tc
        if type_of_machine_sc is not UNSET:
            field_dict["TypeOfMachine_SC"] = type_of_machine_sc
        if function_en is not UNSET:
            field_dict["Function_EN"] = function_en
        if function_tc is not UNSET:
            field_dict["Function_TC"] = function_tc
        if function_sc is not UNSET:
            field_dict["Function_SC"] = function_sc
        if currencies_supported_en is not UNSET:
            field_dict["CurrenciesSupported_EN"] = currencies_supported_en
        if currencies_supported_tc is not UNSET:
            field_dict["CurrenciesSupported_TC"] = currencies_supported_tc
        if currencies_supported_sc is not UNSET:
            field_dict["CurrenciesSupported_SC"] = currencies_supported_sc
        if barrier_free_access_en is not UNSET:
            field_dict["BarrierFreeAccess_EN"] = barrier_free_access_en
        if barrier_free_access_tc is not UNSET:
            field_dict["BarrierFreeAccess_TC"] = barrier_free_access_tc
        if barrier_free_access_sc is not UNSET:
            field_dict["BarrierFreeAccess_SC"] = barrier_free_access_sc
        if network_en is not UNSET:
            field_dict["Network_EN"] = network_en
        if network_tc is not UNSET:
            field_dict["Network_TC"] = network_tc
        if network_sc is not UNSET:
            field_dict["Network_SC"] = network_sc
        if address_en is not UNSET:
            field_dict["Address_EN"] = address_en
        if address_tc is not UNSET:
            field_dict["Address_TC"] = address_tc
        if address_sc is not UNSET:
            field_dict["Address_SC"] = address_sc
        if service_hours_en is not UNSET:
            field_dict["ServiceHours_EN"] = service_hours_en
        if service_hours_tc is not UNSET:
            field_dict["ServiceHours_TC"] = service_hours_tc
        if service_hours_sc is not UNSET:
            field_dict["ServiceHours_SC"] = service_hours_sc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if shape is not UNSET:
            field_dict["SHAPE"] = shape

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_district_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_en = _parse_district_en(d.pop("District_EN", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_district_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sc = _parse_district_sc(d.pop("District_SC", UNSET))

        def _parse_bank_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_name_en = _parse_bank_name_en(d.pop("BankName_EN", UNSET))

        def _parse_bank_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_name_tc = _parse_bank_name_tc(d.pop("BankName_TC", UNSET))

        def _parse_bank_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_name_sc = _parse_bank_name_sc(d.pop("BankName_SC", UNSET))

        def _parse_type_of_machine_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_machine_en = _parse_type_of_machine_en(d.pop("TypeOfMachine_EN", UNSET))

        def _parse_type_of_machine_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_machine_tc = _parse_type_of_machine_tc(d.pop("TypeOfMachine_TC", UNSET))

        def _parse_type_of_machine_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_of_machine_sc = _parse_type_of_machine_sc(d.pop("TypeOfMachine_SC", UNSET))

        def _parse_function_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        function_en = _parse_function_en(d.pop("Function_EN", UNSET))

        def _parse_function_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        function_tc = _parse_function_tc(d.pop("Function_TC", UNSET))

        def _parse_function_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        function_sc = _parse_function_sc(d.pop("Function_SC", UNSET))

        def _parse_currencies_supported_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currencies_supported_en = _parse_currencies_supported_en(
            d.pop("CurrenciesSupported_EN", UNSET)
        )

        def _parse_currencies_supported_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currencies_supported_tc = _parse_currencies_supported_tc(
            d.pop("CurrenciesSupported_TC", UNSET)
        )

        def _parse_currencies_supported_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currencies_supported_sc = _parse_currencies_supported_sc(
            d.pop("CurrenciesSupported_SC", UNSET)
        )

        def _parse_barrier_free_access_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barrier_free_access_en = _parse_barrier_free_access_en(
            d.pop("BarrierFreeAccess_EN", UNSET)
        )

        def _parse_barrier_free_access_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barrier_free_access_tc = _parse_barrier_free_access_tc(
            d.pop("BarrierFreeAccess_TC", UNSET)
        )

        def _parse_barrier_free_access_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barrier_free_access_sc = _parse_barrier_free_access_sc(
            d.pop("BarrierFreeAccess_SC", UNSET)
        )

        def _parse_network_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_en = _parse_network_en(d.pop("Network_EN", UNSET))

        def _parse_network_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_tc = _parse_network_tc(d.pop("Network_TC", UNSET))

        def _parse_network_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        network_sc = _parse_network_sc(d.pop("Network_SC", UNSET))

        def _parse_address_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_en = _parse_address_en(d.pop("Address_EN", UNSET))

        def _parse_address_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_tc = _parse_address_tc(d.pop("Address_TC", UNSET))

        def _parse_address_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_sc = _parse_address_sc(d.pop("Address_SC", UNSET))

        def _parse_service_hours_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours_en = _parse_service_hours_en(d.pop("ServiceHours_EN", UNSET))

        def _parse_service_hours_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours_tc = _parse_service_hours_tc(d.pop("ServiceHours_TC", UNSET))

        def _parse_service_hours_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service_hours_sc = _parse_service_hours_sc(d.pop("ServiceHours_SC", UNSET))

        objectid = d.pop("OBJECTID", UNSET)

        shape = d.pop("SHAPE", UNSET)

        wfs_map_server_wfsgeotagging_attributes = cls(
            district_en=district_en,
            district_tc=district_tc,
            district_sc=district_sc,
            bank_name_en=bank_name_en,
            bank_name_tc=bank_name_tc,
            bank_name_sc=bank_name_sc,
            type_of_machine_en=type_of_machine_en,
            type_of_machine_tc=type_of_machine_tc,
            type_of_machine_sc=type_of_machine_sc,
            function_en=function_en,
            function_tc=function_tc,
            function_sc=function_sc,
            currencies_supported_en=currencies_supported_en,
            currencies_supported_tc=currencies_supported_tc,
            currencies_supported_sc=currencies_supported_sc,
            barrier_free_access_en=barrier_free_access_en,
            barrier_free_access_tc=barrier_free_access_tc,
            barrier_free_access_sc=barrier_free_access_sc,
            network_en=network_en,
            network_tc=network_tc,
            network_sc=network_sc,
            address_en=address_en,
            address_tc=address_tc,
            address_sc=address_sc,
            service_hours_en=service_hours_en,
            service_hours_tc=service_hours_tc,
            service_hours_sc=service_hours_sc,
            objectid=objectid,
            shape=shape,
        )

        wfs_map_server_wfsgeotagging_attributes.additional_properties = d
        return wfs_map_server_wfsgeotagging_attributes

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
