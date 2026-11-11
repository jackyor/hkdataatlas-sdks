from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArcgisFeatureServerArcgisLayer0Attributes")


@_attrs_define
class ArcgisFeatureServerArcgisLayer0Attributes:
    """
    Attributes:
        district_en (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        bank_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        bank_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        bank_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        branch_name_en (None | str | Unset): Publisher field type: esriFieldTypeString
        branch_name_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        branch_name_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_en (None | str | Unset): Publisher field type: esriFieldTypeString
        address_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        address_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hours_en (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hours_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        service_hours_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        barrier_free_access_en (None | str | Unset): Publisher field type: esriFieldTypeString
        barrier_free_access_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        barrier_free_access_sc (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    district_en: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sc: None | str | Unset = UNSET
    bank_name_en: None | str | Unset = UNSET
    bank_name_tc: None | str | Unset = UNSET
    bank_name_sc: None | str | Unset = UNSET
    branch_name_en: None | str | Unset = UNSET
    branch_name_tc: None | str | Unset = UNSET
    branch_name_sc: None | str | Unset = UNSET
    address_en: None | str | Unset = UNSET
    address_tc: None | str | Unset = UNSET
    address_sc: None | str | Unset = UNSET
    service_hours_en: None | str | Unset = UNSET
    service_hours_tc: None | str | Unset = UNSET
    service_hours_sc: None | str | Unset = UNSET
    barrier_free_access_en: None | str | Unset = UNSET
    barrier_free_access_tc: None | str | Unset = UNSET
    barrier_free_access_sc: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
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

        branch_name_en: None | str | Unset
        if isinstance(self.branch_name_en, Unset):
            branch_name_en = UNSET
        else:
            branch_name_en = self.branch_name_en

        branch_name_tc: None | str | Unset
        if isinstance(self.branch_name_tc, Unset):
            branch_name_tc = UNSET
        else:
            branch_name_tc = self.branch_name_tc

        branch_name_sc: None | str | Unset
        if isinstance(self.branch_name_sc, Unset):
            branch_name_sc = UNSET
        else:
            branch_name_sc = self.branch_name_sc

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

        objectid = self.objectid

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
        if branch_name_en is not UNSET:
            field_dict["BranchName_EN"] = branch_name_en
        if branch_name_tc is not UNSET:
            field_dict["BranchName_TC"] = branch_name_tc
        if branch_name_sc is not UNSET:
            field_dict["BranchName_SC"] = branch_name_sc
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
        if barrier_free_access_en is not UNSET:
            field_dict["barrier_free_access_EN"] = barrier_free_access_en
        if barrier_free_access_tc is not UNSET:
            field_dict["barrier_free_access_TC"] = barrier_free_access_tc
        if barrier_free_access_sc is not UNSET:
            field_dict["barrier_free_access_SC"] = barrier_free_access_sc
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

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

        def _parse_branch_name_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name_en = _parse_branch_name_en(d.pop("BranchName_EN", UNSET))

        def _parse_branch_name_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name_tc = _parse_branch_name_tc(d.pop("BranchName_TC", UNSET))

        def _parse_branch_name_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        branch_name_sc = _parse_branch_name_sc(d.pop("BranchName_SC", UNSET))

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

        def _parse_barrier_free_access_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barrier_free_access_en = _parse_barrier_free_access_en(
            d.pop("barrier_free_access_EN", UNSET)
        )

        def _parse_barrier_free_access_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barrier_free_access_tc = _parse_barrier_free_access_tc(
            d.pop("barrier_free_access_TC", UNSET)
        )

        def _parse_barrier_free_access_sc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        barrier_free_access_sc = _parse_barrier_free_access_sc(
            d.pop("barrier_free_access_SC", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            district_en=district_en,
            district_tc=district_tc,
            district_sc=district_sc,
            bank_name_en=bank_name_en,
            bank_name_tc=bank_name_tc,
            bank_name_sc=bank_name_sc,
            branch_name_en=branch_name_en,
            branch_name_tc=branch_name_tc,
            branch_name_sc=branch_name_sc,
            address_en=address_en,
            address_tc=address_tc,
            address_sc=address_sc,
            service_hours_en=service_hours_en,
            service_hours_tc=service_hours_tc,
            service_hours_sc=service_hours_sc,
            barrier_free_access_en=barrier_free_access_en,
            barrier_free_access_tc=barrier_free_access_tc,
            barrier_free_access_sc=barrier_free_access_sc,
            objectid=objectid,
        )

        arcgis_feature_server_arcgis_layer_0_attributes.additional_properties = d
        return arcgis_feature_server_arcgis_layer_0_attributes

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
