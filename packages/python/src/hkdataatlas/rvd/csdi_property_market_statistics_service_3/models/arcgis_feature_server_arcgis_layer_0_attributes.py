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
        forecast_comp_2025_a (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_a_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_b (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_b_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_c (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_c_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_d (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_d_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_e (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_e_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_total (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2025_total_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_a (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_a_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_b (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_b_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_c (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_c_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_d (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_d_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_e (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_e_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_total (None | str | Unset): Publisher field type: esriFieldTypeString
        forecast_comp_2026_total_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    dataset: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    forecast_comp_2025_a: None | str | Unset = UNSET
    forecast_comp_2025_a_tc: None | str | Unset = UNSET
    forecast_comp_2025_b: None | str | Unset = UNSET
    forecast_comp_2025_b_tc: None | str | Unset = UNSET
    forecast_comp_2025_c: None | str | Unset = UNSET
    forecast_comp_2025_c_tc: None | str | Unset = UNSET
    forecast_comp_2025_d: None | str | Unset = UNSET
    forecast_comp_2025_d_tc: None | str | Unset = UNSET
    forecast_comp_2025_e: None | str | Unset = UNSET
    forecast_comp_2025_e_tc: None | str | Unset = UNSET
    forecast_comp_2025_total: None | str | Unset = UNSET
    forecast_comp_2025_total_tc: None | str | Unset = UNSET
    forecast_comp_2026_a: None | str | Unset = UNSET
    forecast_comp_2026_a_tc: None | str | Unset = UNSET
    forecast_comp_2026_b: None | str | Unset = UNSET
    forecast_comp_2026_b_tc: None | str | Unset = UNSET
    forecast_comp_2026_c: None | str | Unset = UNSET
    forecast_comp_2026_c_tc: None | str | Unset = UNSET
    forecast_comp_2026_d: None | str | Unset = UNSET
    forecast_comp_2026_d_tc: None | str | Unset = UNSET
    forecast_comp_2026_e: None | str | Unset = UNSET
    forecast_comp_2026_e_tc: None | str | Unset = UNSET
    forecast_comp_2026_total: None | str | Unset = UNSET
    forecast_comp_2026_total_tc: None | str | Unset = UNSET
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

        forecast_comp_2025_a: None | str | Unset
        if isinstance(self.forecast_comp_2025_a, Unset):
            forecast_comp_2025_a = UNSET
        else:
            forecast_comp_2025_a = self.forecast_comp_2025_a

        forecast_comp_2025_a_tc: None | str | Unset
        if isinstance(self.forecast_comp_2025_a_tc, Unset):
            forecast_comp_2025_a_tc = UNSET
        else:
            forecast_comp_2025_a_tc = self.forecast_comp_2025_a_tc

        forecast_comp_2025_b: None | str | Unset
        if isinstance(self.forecast_comp_2025_b, Unset):
            forecast_comp_2025_b = UNSET
        else:
            forecast_comp_2025_b = self.forecast_comp_2025_b

        forecast_comp_2025_b_tc: None | str | Unset
        if isinstance(self.forecast_comp_2025_b_tc, Unset):
            forecast_comp_2025_b_tc = UNSET
        else:
            forecast_comp_2025_b_tc = self.forecast_comp_2025_b_tc

        forecast_comp_2025_c: None | str | Unset
        if isinstance(self.forecast_comp_2025_c, Unset):
            forecast_comp_2025_c = UNSET
        else:
            forecast_comp_2025_c = self.forecast_comp_2025_c

        forecast_comp_2025_c_tc: None | str | Unset
        if isinstance(self.forecast_comp_2025_c_tc, Unset):
            forecast_comp_2025_c_tc = UNSET
        else:
            forecast_comp_2025_c_tc = self.forecast_comp_2025_c_tc

        forecast_comp_2025_d: None | str | Unset
        if isinstance(self.forecast_comp_2025_d, Unset):
            forecast_comp_2025_d = UNSET
        else:
            forecast_comp_2025_d = self.forecast_comp_2025_d

        forecast_comp_2025_d_tc: None | str | Unset
        if isinstance(self.forecast_comp_2025_d_tc, Unset):
            forecast_comp_2025_d_tc = UNSET
        else:
            forecast_comp_2025_d_tc = self.forecast_comp_2025_d_tc

        forecast_comp_2025_e: None | str | Unset
        if isinstance(self.forecast_comp_2025_e, Unset):
            forecast_comp_2025_e = UNSET
        else:
            forecast_comp_2025_e = self.forecast_comp_2025_e

        forecast_comp_2025_e_tc: None | str | Unset
        if isinstance(self.forecast_comp_2025_e_tc, Unset):
            forecast_comp_2025_e_tc = UNSET
        else:
            forecast_comp_2025_e_tc = self.forecast_comp_2025_e_tc

        forecast_comp_2025_total: None | str | Unset
        if isinstance(self.forecast_comp_2025_total, Unset):
            forecast_comp_2025_total = UNSET
        else:
            forecast_comp_2025_total = self.forecast_comp_2025_total

        forecast_comp_2025_total_tc: None | str | Unset
        if isinstance(self.forecast_comp_2025_total_tc, Unset):
            forecast_comp_2025_total_tc = UNSET
        else:
            forecast_comp_2025_total_tc = self.forecast_comp_2025_total_tc

        forecast_comp_2026_a: None | str | Unset
        if isinstance(self.forecast_comp_2026_a, Unset):
            forecast_comp_2026_a = UNSET
        else:
            forecast_comp_2026_a = self.forecast_comp_2026_a

        forecast_comp_2026_a_tc: None | str | Unset
        if isinstance(self.forecast_comp_2026_a_tc, Unset):
            forecast_comp_2026_a_tc = UNSET
        else:
            forecast_comp_2026_a_tc = self.forecast_comp_2026_a_tc

        forecast_comp_2026_b: None | str | Unset
        if isinstance(self.forecast_comp_2026_b, Unset):
            forecast_comp_2026_b = UNSET
        else:
            forecast_comp_2026_b = self.forecast_comp_2026_b

        forecast_comp_2026_b_tc: None | str | Unset
        if isinstance(self.forecast_comp_2026_b_tc, Unset):
            forecast_comp_2026_b_tc = UNSET
        else:
            forecast_comp_2026_b_tc = self.forecast_comp_2026_b_tc

        forecast_comp_2026_c: None | str | Unset
        if isinstance(self.forecast_comp_2026_c, Unset):
            forecast_comp_2026_c = UNSET
        else:
            forecast_comp_2026_c = self.forecast_comp_2026_c

        forecast_comp_2026_c_tc: None | str | Unset
        if isinstance(self.forecast_comp_2026_c_tc, Unset):
            forecast_comp_2026_c_tc = UNSET
        else:
            forecast_comp_2026_c_tc = self.forecast_comp_2026_c_tc

        forecast_comp_2026_d: None | str | Unset
        if isinstance(self.forecast_comp_2026_d, Unset):
            forecast_comp_2026_d = UNSET
        else:
            forecast_comp_2026_d = self.forecast_comp_2026_d

        forecast_comp_2026_d_tc: None | str | Unset
        if isinstance(self.forecast_comp_2026_d_tc, Unset):
            forecast_comp_2026_d_tc = UNSET
        else:
            forecast_comp_2026_d_tc = self.forecast_comp_2026_d_tc

        forecast_comp_2026_e: None | str | Unset
        if isinstance(self.forecast_comp_2026_e, Unset):
            forecast_comp_2026_e = UNSET
        else:
            forecast_comp_2026_e = self.forecast_comp_2026_e

        forecast_comp_2026_e_tc: None | str | Unset
        if isinstance(self.forecast_comp_2026_e_tc, Unset):
            forecast_comp_2026_e_tc = UNSET
        else:
            forecast_comp_2026_e_tc = self.forecast_comp_2026_e_tc

        forecast_comp_2026_total: None | str | Unset
        if isinstance(self.forecast_comp_2026_total, Unset):
            forecast_comp_2026_total = UNSET
        else:
            forecast_comp_2026_total = self.forecast_comp_2026_total

        forecast_comp_2026_total_tc: None | str | Unset
        if isinstance(self.forecast_comp_2026_total_tc, Unset):
            forecast_comp_2026_total_tc = UNSET
        else:
            forecast_comp_2026_total_tc = self.forecast_comp_2026_total_tc

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
        if forecast_comp_2025_a is not UNSET:
            field_dict["Forecast_Comp_2025_A"] = forecast_comp_2025_a
        if forecast_comp_2025_a_tc is not UNSET:
            field_dict["Forecast_Comp_2025_A_TC"] = forecast_comp_2025_a_tc
        if forecast_comp_2025_b is not UNSET:
            field_dict["Forecast_Comp_2025_B"] = forecast_comp_2025_b
        if forecast_comp_2025_b_tc is not UNSET:
            field_dict["Forecast_Comp_2025_B_TC"] = forecast_comp_2025_b_tc
        if forecast_comp_2025_c is not UNSET:
            field_dict["Forecast_Comp_2025_C"] = forecast_comp_2025_c
        if forecast_comp_2025_c_tc is not UNSET:
            field_dict["Forecast_Comp_2025_C_TC"] = forecast_comp_2025_c_tc
        if forecast_comp_2025_d is not UNSET:
            field_dict["Forecast_Comp_2025_D"] = forecast_comp_2025_d
        if forecast_comp_2025_d_tc is not UNSET:
            field_dict["Forecast_Comp_2025_D_TC"] = forecast_comp_2025_d_tc
        if forecast_comp_2025_e is not UNSET:
            field_dict["Forecast_Comp_2025_E"] = forecast_comp_2025_e
        if forecast_comp_2025_e_tc is not UNSET:
            field_dict["Forecast_Comp_2025_E_TC"] = forecast_comp_2025_e_tc
        if forecast_comp_2025_total is not UNSET:
            field_dict["Forecast_Comp_2025_Total"] = forecast_comp_2025_total
        if forecast_comp_2025_total_tc is not UNSET:
            field_dict["Forecast_Comp_2025_Total_TC"] = forecast_comp_2025_total_tc
        if forecast_comp_2026_a is not UNSET:
            field_dict["Forecast_Comp_2026_A"] = forecast_comp_2026_a
        if forecast_comp_2026_a_tc is not UNSET:
            field_dict["Forecast_Comp_2026_A_TC"] = forecast_comp_2026_a_tc
        if forecast_comp_2026_b is not UNSET:
            field_dict["Forecast_Comp_2026_B"] = forecast_comp_2026_b
        if forecast_comp_2026_b_tc is not UNSET:
            field_dict["Forecast_Comp_2026_B_TC"] = forecast_comp_2026_b_tc
        if forecast_comp_2026_c is not UNSET:
            field_dict["Forecast_Comp_2026_C"] = forecast_comp_2026_c
        if forecast_comp_2026_c_tc is not UNSET:
            field_dict["Forecast_Comp_2026_C_TC"] = forecast_comp_2026_c_tc
        if forecast_comp_2026_d is not UNSET:
            field_dict["Forecast_Comp_2026_D"] = forecast_comp_2026_d
        if forecast_comp_2026_d_tc is not UNSET:
            field_dict["Forecast_Comp_2026_D_TC"] = forecast_comp_2026_d_tc
        if forecast_comp_2026_e is not UNSET:
            field_dict["Forecast_Comp_2026_E"] = forecast_comp_2026_e
        if forecast_comp_2026_e_tc is not UNSET:
            field_dict["Forecast_Comp_2026_E_TC"] = forecast_comp_2026_e_tc
        if forecast_comp_2026_total is not UNSET:
            field_dict["Forecast_Comp_2026_Total"] = forecast_comp_2026_total
        if forecast_comp_2026_total_tc is not UNSET:
            field_dict["Forecast_Comp_2026_Total_TC"] = forecast_comp_2026_total_tc
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

        def _parse_forecast_comp_2025_a(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_a = _parse_forecast_comp_2025_a(
            d.pop("Forecast_Comp_2025_A", UNSET)
        )

        def _parse_forecast_comp_2025_a_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_a_tc = _parse_forecast_comp_2025_a_tc(
            d.pop("Forecast_Comp_2025_A_TC", UNSET)
        )

        def _parse_forecast_comp_2025_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_b = _parse_forecast_comp_2025_b(
            d.pop("Forecast_Comp_2025_B", UNSET)
        )

        def _parse_forecast_comp_2025_b_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_b_tc = _parse_forecast_comp_2025_b_tc(
            d.pop("Forecast_Comp_2025_B_TC", UNSET)
        )

        def _parse_forecast_comp_2025_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_c = _parse_forecast_comp_2025_c(
            d.pop("Forecast_Comp_2025_C", UNSET)
        )

        def _parse_forecast_comp_2025_c_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_c_tc = _parse_forecast_comp_2025_c_tc(
            d.pop("Forecast_Comp_2025_C_TC", UNSET)
        )

        def _parse_forecast_comp_2025_d(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_d = _parse_forecast_comp_2025_d(
            d.pop("Forecast_Comp_2025_D", UNSET)
        )

        def _parse_forecast_comp_2025_d_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_d_tc = _parse_forecast_comp_2025_d_tc(
            d.pop("Forecast_Comp_2025_D_TC", UNSET)
        )

        def _parse_forecast_comp_2025_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_e = _parse_forecast_comp_2025_e(
            d.pop("Forecast_Comp_2025_E", UNSET)
        )

        def _parse_forecast_comp_2025_e_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_e_tc = _parse_forecast_comp_2025_e_tc(
            d.pop("Forecast_Comp_2025_E_TC", UNSET)
        )

        def _parse_forecast_comp_2025_total(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_total = _parse_forecast_comp_2025_total(
            d.pop("Forecast_Comp_2025_Total", UNSET)
        )

        def _parse_forecast_comp_2025_total_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2025_total_tc = _parse_forecast_comp_2025_total_tc(
            d.pop("Forecast_Comp_2025_Total_TC", UNSET)
        )

        def _parse_forecast_comp_2026_a(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_a = _parse_forecast_comp_2026_a(
            d.pop("Forecast_Comp_2026_A", UNSET)
        )

        def _parse_forecast_comp_2026_a_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_a_tc = _parse_forecast_comp_2026_a_tc(
            d.pop("Forecast_Comp_2026_A_TC", UNSET)
        )

        def _parse_forecast_comp_2026_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_b = _parse_forecast_comp_2026_b(
            d.pop("Forecast_Comp_2026_B", UNSET)
        )

        def _parse_forecast_comp_2026_b_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_b_tc = _parse_forecast_comp_2026_b_tc(
            d.pop("Forecast_Comp_2026_B_TC", UNSET)
        )

        def _parse_forecast_comp_2026_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_c = _parse_forecast_comp_2026_c(
            d.pop("Forecast_Comp_2026_C", UNSET)
        )

        def _parse_forecast_comp_2026_c_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_c_tc = _parse_forecast_comp_2026_c_tc(
            d.pop("Forecast_Comp_2026_C_TC", UNSET)
        )

        def _parse_forecast_comp_2026_d(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_d = _parse_forecast_comp_2026_d(
            d.pop("Forecast_Comp_2026_D", UNSET)
        )

        def _parse_forecast_comp_2026_d_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_d_tc = _parse_forecast_comp_2026_d_tc(
            d.pop("Forecast_Comp_2026_D_TC", UNSET)
        )

        def _parse_forecast_comp_2026_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_e = _parse_forecast_comp_2026_e(
            d.pop("Forecast_Comp_2026_E", UNSET)
        )

        def _parse_forecast_comp_2026_e_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_e_tc = _parse_forecast_comp_2026_e_tc(
            d.pop("Forecast_Comp_2026_E_TC", UNSET)
        )

        def _parse_forecast_comp_2026_total(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_total = _parse_forecast_comp_2026_total(
            d.pop("Forecast_Comp_2026_Total", UNSET)
        )

        def _parse_forecast_comp_2026_total_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        forecast_comp_2026_total_tc = _parse_forecast_comp_2026_total_tc(
            d.pop("Forecast_Comp_2026_Total_TC", UNSET)
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
            forecast_comp_2025_a=forecast_comp_2025_a,
            forecast_comp_2025_a_tc=forecast_comp_2025_a_tc,
            forecast_comp_2025_b=forecast_comp_2025_b,
            forecast_comp_2025_b_tc=forecast_comp_2025_b_tc,
            forecast_comp_2025_c=forecast_comp_2025_c,
            forecast_comp_2025_c_tc=forecast_comp_2025_c_tc,
            forecast_comp_2025_d=forecast_comp_2025_d,
            forecast_comp_2025_d_tc=forecast_comp_2025_d_tc,
            forecast_comp_2025_e=forecast_comp_2025_e,
            forecast_comp_2025_e_tc=forecast_comp_2025_e_tc,
            forecast_comp_2025_total=forecast_comp_2025_total,
            forecast_comp_2025_total_tc=forecast_comp_2025_total_tc,
            forecast_comp_2026_a=forecast_comp_2026_a,
            forecast_comp_2026_a_tc=forecast_comp_2026_a_tc,
            forecast_comp_2026_b=forecast_comp_2026_b,
            forecast_comp_2026_b_tc=forecast_comp_2026_b_tc,
            forecast_comp_2026_c=forecast_comp_2026_c,
            forecast_comp_2026_c_tc=forecast_comp_2026_c_tc,
            forecast_comp_2026_d=forecast_comp_2026_d,
            forecast_comp_2026_d_tc=forecast_comp_2026_d_tc,
            forecast_comp_2026_e=forecast_comp_2026_e,
            forecast_comp_2026_e_tc=forecast_comp_2026_e_tc,
            forecast_comp_2026_total=forecast_comp_2026_total,
            forecast_comp_2026_total_tc=forecast_comp_2026_total_tc,
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
