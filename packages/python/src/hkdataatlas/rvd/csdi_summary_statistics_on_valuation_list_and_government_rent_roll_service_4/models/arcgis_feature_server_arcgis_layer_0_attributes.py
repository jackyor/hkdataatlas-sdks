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
        office_number (None | str | Unset): Publisher field type: esriFieldTypeString
        office_number_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        office_rv_hkd_in_thousand (None | str | Unset): Publisher field type: esriFieldTypeString
        office_rv_hkd_in_thousand_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        io_number (None | str | Unset): Publisher field type: esriFieldTypeString
        io_number_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        io_rv_hkd_in_thousand (None | str | Unset): Publisher field type: esriFieldTypeString
        io_rv_hkd_in_thousand_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    dataset: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    office_number: None | str | Unset = UNSET
    office_number_tc: None | str | Unset = UNSET
    office_rv_hkd_in_thousand: None | str | Unset = UNSET
    office_rv_hkd_in_thousand_tc: None | str | Unset = UNSET
    io_number: None | str | Unset = UNSET
    io_number_tc: None | str | Unset = UNSET
    io_rv_hkd_in_thousand: None | str | Unset = UNSET
    io_rv_hkd_in_thousand_tc: None | str | Unset = UNSET
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

        office_number: None | str | Unset
        if isinstance(self.office_number, Unset):
            office_number = UNSET
        else:
            office_number = self.office_number

        office_number_tc: None | str | Unset
        if isinstance(self.office_number_tc, Unset):
            office_number_tc = UNSET
        else:
            office_number_tc = self.office_number_tc

        office_rv_hkd_in_thousand: None | str | Unset
        if isinstance(self.office_rv_hkd_in_thousand, Unset):
            office_rv_hkd_in_thousand = UNSET
        else:
            office_rv_hkd_in_thousand = self.office_rv_hkd_in_thousand

        office_rv_hkd_in_thousand_tc: None | str | Unset
        if isinstance(self.office_rv_hkd_in_thousand_tc, Unset):
            office_rv_hkd_in_thousand_tc = UNSET
        else:
            office_rv_hkd_in_thousand_tc = self.office_rv_hkd_in_thousand_tc

        io_number: None | str | Unset
        if isinstance(self.io_number, Unset):
            io_number = UNSET
        else:
            io_number = self.io_number

        io_number_tc: None | str | Unset
        if isinstance(self.io_number_tc, Unset):
            io_number_tc = UNSET
        else:
            io_number_tc = self.io_number_tc

        io_rv_hkd_in_thousand: None | str | Unset
        if isinstance(self.io_rv_hkd_in_thousand, Unset):
            io_rv_hkd_in_thousand = UNSET
        else:
            io_rv_hkd_in_thousand = self.io_rv_hkd_in_thousand

        io_rv_hkd_in_thousand_tc: None | str | Unset
        if isinstance(self.io_rv_hkd_in_thousand_tc, Unset):
            io_rv_hkd_in_thousand_tc = UNSET
        else:
            io_rv_hkd_in_thousand_tc = self.io_rv_hkd_in_thousand_tc

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
        if office_number is not UNSET:
            field_dict["Office_Number"] = office_number
        if office_number_tc is not UNSET:
            field_dict["Office_Number_TC"] = office_number_tc
        if office_rv_hkd_in_thousand is not UNSET:
            field_dict["Office_RV_HKD_In_Thousand"] = office_rv_hkd_in_thousand
        if office_rv_hkd_in_thousand_tc is not UNSET:
            field_dict["Office_RV_HKD_In_Thousand_TC"] = office_rv_hkd_in_thousand_tc
        if io_number is not UNSET:
            field_dict["IO_Number"] = io_number
        if io_number_tc is not UNSET:
            field_dict["IO_Number_TC"] = io_number_tc
        if io_rv_hkd_in_thousand is not UNSET:
            field_dict["IO_RV_HKD_In_Thousand"] = io_rv_hkd_in_thousand
        if io_rv_hkd_in_thousand_tc is not UNSET:
            field_dict["IO_RV_HKD_In_Thousand_TC"] = io_rv_hkd_in_thousand_tc
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

        def _parse_office_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_number = _parse_office_number(d.pop("Office_Number", UNSET))

        def _parse_office_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_number_tc = _parse_office_number_tc(d.pop("Office_Number_TC", UNSET))

        def _parse_office_rv_hkd_in_thousand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_rv_hkd_in_thousand = _parse_office_rv_hkd_in_thousand(
            d.pop("Office_RV_HKD_In_Thousand", UNSET)
        )

        def _parse_office_rv_hkd_in_thousand_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_rv_hkd_in_thousand_tc = _parse_office_rv_hkd_in_thousand_tc(
            d.pop("Office_RV_HKD_In_Thousand_TC", UNSET)
        )

        def _parse_io_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        io_number = _parse_io_number(d.pop("IO_Number", UNSET))

        def _parse_io_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        io_number_tc = _parse_io_number_tc(d.pop("IO_Number_TC", UNSET))

        def _parse_io_rv_hkd_in_thousand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        io_rv_hkd_in_thousand = _parse_io_rv_hkd_in_thousand(
            d.pop("IO_RV_HKD_In_Thousand", UNSET)
        )

        def _parse_io_rv_hkd_in_thousand_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        io_rv_hkd_in_thousand_tc = _parse_io_rv_hkd_in_thousand_tc(
            d.pop("IO_RV_HKD_In_Thousand_TC", UNSET)
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
            office_number=office_number,
            office_number_tc=office_number_tc,
            office_rv_hkd_in_thousand=office_rv_hkd_in_thousand,
            office_rv_hkd_in_thousand_tc=office_rv_hkd_in_thousand_tc,
            io_number=io_number,
            io_number_tc=io_number_tc,
            io_rv_hkd_in_thousand=io_rv_hkd_in_thousand,
            io_rv_hkd_in_thousand_tc=io_rv_hkd_in_thousand_tc,
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
