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
        fac_id (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_type_en (None | str | Unset): Publisher field type: esriFieldTypeString
        facility_type_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        location_en (None | str | Unset): Publisher field type: esriFieldTypeString
        location_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        status_en (None | str | Unset): Publisher field type: esriFieldTypeString
        status_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        effective_date (Any | Unset): Publisher field type: esriFieldTypeDate; JSON wire representation remains unknown.
        csdi_dataset (None | str | Unset): Publisher field type: esriFieldTypeString
        expected_expiry_date (None | str | Unset): Publisher field type: esriFieldTypeString
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
    """

    fac_id: None | str | Unset = UNSET
    facility_type_en: None | str | Unset = UNSET
    facility_type_tc: None | str | Unset = UNSET
    location_en: None | str | Unset = UNSET
    location_tc: None | str | Unset = UNSET
    status_en: None | str | Unset = UNSET
    status_tc: None | str | Unset = UNSET
    effective_date: Any | Unset = UNSET
    csdi_dataset: None | str | Unset = UNSET
    expected_expiry_date: None | str | Unset = UNSET
    objectid: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fac_id: None | str | Unset
        if isinstance(self.fac_id, Unset):
            fac_id = UNSET
        else:
            fac_id = self.fac_id

        facility_type_en: None | str | Unset
        if isinstance(self.facility_type_en, Unset):
            facility_type_en = UNSET
        else:
            facility_type_en = self.facility_type_en

        facility_type_tc: None | str | Unset
        if isinstance(self.facility_type_tc, Unset):
            facility_type_tc = UNSET
        else:
            facility_type_tc = self.facility_type_tc

        location_en: None | str | Unset
        if isinstance(self.location_en, Unset):
            location_en = UNSET
        else:
            location_en = self.location_en

        location_tc: None | str | Unset
        if isinstance(self.location_tc, Unset):
            location_tc = UNSET
        else:
            location_tc = self.location_tc

        status_en: None | str | Unset
        if isinstance(self.status_en, Unset):
            status_en = UNSET
        else:
            status_en = self.status_en

        status_tc: None | str | Unset
        if isinstance(self.status_tc, Unset):
            status_tc = UNSET
        else:
            status_tc = self.status_tc

        effective_date = self.effective_date

        csdi_dataset: None | str | Unset
        if isinstance(self.csdi_dataset, Unset):
            csdi_dataset = UNSET
        else:
            csdi_dataset = self.csdi_dataset

        expected_expiry_date: None | str | Unset
        if isinstance(self.expected_expiry_date, Unset):
            expected_expiry_date = UNSET
        else:
            expected_expiry_date = self.expected_expiry_date

        objectid = self.objectid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fac_id is not UNSET:
            field_dict["FAC_ID"] = fac_id
        if facility_type_en is not UNSET:
            field_dict["FACILITY_TYPE_EN"] = facility_type_en
        if facility_type_tc is not UNSET:
            field_dict["FACILITY_TYPE_TC"] = facility_type_tc
        if location_en is not UNSET:
            field_dict["LOCATION_EN"] = location_en
        if location_tc is not UNSET:
            field_dict["LOCATION_TC"] = location_tc
        if status_en is not UNSET:
            field_dict["STATUS_EN"] = status_en
        if status_tc is not UNSET:
            field_dict["STATUS_TC"] = status_tc
        if effective_date is not UNSET:
            field_dict["EFFECTIVE_DATE"] = effective_date
        if csdi_dataset is not UNSET:
            field_dict["CSDI_DATASET"] = csdi_dataset
        if expected_expiry_date is not UNSET:
            field_dict["EXPECTED_EXPIRY_DATE"] = expected_expiry_date
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_fac_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fac_id = _parse_fac_id(d.pop("FAC_ID", UNSET))

        def _parse_facility_type_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_type_en = _parse_facility_type_en(d.pop("FACILITY_TYPE_EN", UNSET))

        def _parse_facility_type_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        facility_type_tc = _parse_facility_type_tc(d.pop("FACILITY_TYPE_TC", UNSET))

        def _parse_location_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_en = _parse_location_en(d.pop("LOCATION_EN", UNSET))

        def _parse_location_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        location_tc = _parse_location_tc(d.pop("LOCATION_TC", UNSET))

        def _parse_status_en(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_en = _parse_status_en(d.pop("STATUS_EN", UNSET))

        def _parse_status_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_tc = _parse_status_tc(d.pop("STATUS_TC", UNSET))

        effective_date = d.pop("EFFECTIVE_DATE", UNSET)

        def _parse_csdi_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        csdi_dataset = _parse_csdi_dataset(d.pop("CSDI_DATASET", UNSET))

        def _parse_expected_expiry_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_expiry_date = _parse_expected_expiry_date(
            d.pop("EXPECTED_EXPIRY_DATE", UNSET)
        )

        objectid = d.pop("OBJECTID", UNSET)

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            fac_id=fac_id,
            facility_type_en=facility_type_en,
            facility_type_tc=facility_type_tc,
            location_en=location_en,
            location_tc=location_tc,
            status_en=status_en,
            status_tc=status_tc,
            effective_date=effective_date,
            csdi_dataset=csdi_dataset,
            expected_expiry_date=expected_expiry_date,
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
