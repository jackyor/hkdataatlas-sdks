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
        objectid (int | Unset): Publisher field type: esriFieldTypeOID
        dataset (None | str | Unset): Publisher field type: esriFieldTypeString
        dataset_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        district (None | str | Unset): Publisher field type: esriFieldTypeString
        district_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        factory_number (None | str | Unset): Publisher field type: esriFieldTypeString
        factory_number_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        factory_rv_hkd_in_thousand (None | str | Unset): Publisher field type: esriFieldTypeString
        factory_rv_hkd_in_thousand_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        storage_number (None | str | Unset): Publisher field type: esriFieldTypeString
        storage_number_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        storage_rv_hkd_in_thousand (None | str | Unset): Publisher field type: esriFieldTypeString
        storage_rv_hkd_in_thousand_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    dataset: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    factory_number: None | str | Unset = UNSET
    factory_number_tc: None | str | Unset = UNSET
    factory_rv_hkd_in_thousand: None | str | Unset = UNSET
    factory_rv_hkd_in_thousand_tc: None | str | Unset = UNSET
    storage_number: None | str | Unset = UNSET
    storage_number_tc: None | str | Unset = UNSET
    storage_rv_hkd_in_thousand: None | str | Unset = UNSET
    storage_rv_hkd_in_thousand_tc: None | str | Unset = UNSET
    last_update: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        else:
            dataset = self.dataset

        dataset_tc: None | str | Unset
        if isinstance(self.dataset_tc, Unset):
            dataset_tc = UNSET
        else:
            dataset_tc = self.dataset_tc

        district: None | str | Unset
        if isinstance(self.district, Unset):
            district = UNSET
        else:
            district = self.district

        district_tc: None | str | Unset
        if isinstance(self.district_tc, Unset):
            district_tc = UNSET
        else:
            district_tc = self.district_tc

        factory_number: None | str | Unset
        if isinstance(self.factory_number, Unset):
            factory_number = UNSET
        else:
            factory_number = self.factory_number

        factory_number_tc: None | str | Unset
        if isinstance(self.factory_number_tc, Unset):
            factory_number_tc = UNSET
        else:
            factory_number_tc = self.factory_number_tc

        factory_rv_hkd_in_thousand: None | str | Unset
        if isinstance(self.factory_rv_hkd_in_thousand, Unset):
            factory_rv_hkd_in_thousand = UNSET
        else:
            factory_rv_hkd_in_thousand = self.factory_rv_hkd_in_thousand

        factory_rv_hkd_in_thousand_tc: None | str | Unset
        if isinstance(self.factory_rv_hkd_in_thousand_tc, Unset):
            factory_rv_hkd_in_thousand_tc = UNSET
        else:
            factory_rv_hkd_in_thousand_tc = self.factory_rv_hkd_in_thousand_tc

        storage_number: None | str | Unset
        if isinstance(self.storage_number, Unset):
            storage_number = UNSET
        else:
            storage_number = self.storage_number

        storage_number_tc: None | str | Unset
        if isinstance(self.storage_number_tc, Unset):
            storage_number_tc = UNSET
        else:
            storage_number_tc = self.storage_number_tc

        storage_rv_hkd_in_thousand: None | str | Unset
        if isinstance(self.storage_rv_hkd_in_thousand, Unset):
            storage_rv_hkd_in_thousand = UNSET
        else:
            storage_rv_hkd_in_thousand = self.storage_rv_hkd_in_thousand

        storage_rv_hkd_in_thousand_tc: None | str | Unset
        if isinstance(self.storage_rv_hkd_in_thousand_tc, Unset):
            storage_rv_hkd_in_thousand_tc = UNSET
        else:
            storage_rv_hkd_in_thousand_tc = self.storage_rv_hkd_in_thousand_tc

        last_update: None | str | Unset
        if isinstance(self.last_update, Unset):
            last_update = UNSET
        else:
            last_update = self.last_update

        shape_length: float | None | Unset
        if isinstance(self.shape_length, Unset):
            shape_length = UNSET
        else:
            shape_length = self.shape_length

        shape_area: float | None | Unset
        if isinstance(self.shape_area, Unset):
            shape_area = UNSET
        else:
            shape_area = self.shape_area

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objectid is not UNSET:
            field_dict["OBJECTID"] = objectid
        if dataset is not UNSET:
            field_dict["Dataset"] = dataset
        if dataset_tc is not UNSET:
            field_dict["Dataset_TC"] = dataset_tc
        if district is not UNSET:
            field_dict["District"] = district
        if district_tc is not UNSET:
            field_dict["District_TC"] = district_tc
        if factory_number is not UNSET:
            field_dict["Factory_Number"] = factory_number
        if factory_number_tc is not UNSET:
            field_dict["Factory_Number_TC"] = factory_number_tc
        if factory_rv_hkd_in_thousand is not UNSET:
            field_dict["Factory_RV_HKD_In_Thousand"] = factory_rv_hkd_in_thousand
        if factory_rv_hkd_in_thousand_tc is not UNSET:
            field_dict["Factory_RV_HKD_In_Thousand_TC"] = factory_rv_hkd_in_thousand_tc
        if storage_number is not UNSET:
            field_dict["Storage_Number"] = storage_number
        if storage_number_tc is not UNSET:
            field_dict["Storage_Number_TC"] = storage_number_tc
        if storage_rv_hkd_in_thousand is not UNSET:
            field_dict["Storage_RV_HKD_In_Thousand"] = storage_rv_hkd_in_thousand
        if storage_rv_hkd_in_thousand_tc is not UNSET:
            field_dict["Storage_RV_HKD_In_Thousand_TC"] = storage_rv_hkd_in_thousand_tc
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_dataset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset = _parse_dataset(d.pop("Dataset", UNSET))

        def _parse_dataset_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dataset_tc = _parse_dataset_tc(d.pop("Dataset_TC", UNSET))

        def _parse_district(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district = _parse_district(d.pop("District", UNSET))

        def _parse_district_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_tc = _parse_district_tc(d.pop("District_TC", UNSET))

        def _parse_factory_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        factory_number = _parse_factory_number(d.pop("Factory_Number", UNSET))

        def _parse_factory_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        factory_number_tc = _parse_factory_number_tc(d.pop("Factory_Number_TC", UNSET))

        def _parse_factory_rv_hkd_in_thousand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        factory_rv_hkd_in_thousand = _parse_factory_rv_hkd_in_thousand(
            d.pop("Factory_RV_HKD_In_Thousand", UNSET)
        )

        def _parse_factory_rv_hkd_in_thousand_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        factory_rv_hkd_in_thousand_tc = _parse_factory_rv_hkd_in_thousand_tc(
            d.pop("Factory_RV_HKD_In_Thousand_TC", UNSET)
        )

        def _parse_storage_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_number = _parse_storage_number(d.pop("Storage_Number", UNSET))

        def _parse_storage_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_number_tc = _parse_storage_number_tc(d.pop("Storage_Number_TC", UNSET))

        def _parse_storage_rv_hkd_in_thousand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_rv_hkd_in_thousand = _parse_storage_rv_hkd_in_thousand(
            d.pop("Storage_RV_HKD_In_Thousand", UNSET)
        )

        def _parse_storage_rv_hkd_in_thousand_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_rv_hkd_in_thousand_tc = _parse_storage_rv_hkd_in_thousand_tc(
            d.pop("Storage_RV_HKD_In_Thousand_TC", UNSET)
        )

        def _parse_last_update(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_update = _parse_last_update(d.pop("LastUpdate", UNSET))

        def _parse_shape_length(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_length = _parse_shape_length(d.pop("Shape__Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("Shape__Area", UNSET))

        arcgis_feature_server_arcgis_layer_0_attributes = cls(
            objectid=objectid,
            dataset=dataset,
            dataset_tc=dataset_tc,
            district=district,
            district_tc=district_tc,
            factory_number=factory_number,
            factory_number_tc=factory_number_tc,
            factory_rv_hkd_in_thousand=factory_rv_hkd_in_thousand,
            factory_rv_hkd_in_thousand_tc=factory_rv_hkd_in_thousand_tc,
            storage_number=storage_number,
            storage_number_tc=storage_number_tc,
            storage_rv_hkd_in_thousand=storage_rv_hkd_in_thousand,
            storage_rv_hkd_in_thousand_tc=storage_rv_hkd_in_thousand_tc,
            last_update=last_update,
            shape_length=shape_length,
            shape_area=shape_area,
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
