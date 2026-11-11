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
        stock_2024_year_end_a (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_a_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_b (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_b_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_c (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_c_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_d (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_d_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_e (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_e_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_total (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_total_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    dataset: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    stock_2024_year_end_a: None | str | Unset = UNSET
    stock_2024_year_end_a_tc: None | str | Unset = UNSET
    stock_2024_year_end_b: None | str | Unset = UNSET
    stock_2024_year_end_b_tc: None | str | Unset = UNSET
    stock_2024_year_end_c: None | str | Unset = UNSET
    stock_2024_year_end_c_tc: None | str | Unset = UNSET
    stock_2024_year_end_d: None | str | Unset = UNSET
    stock_2024_year_end_d_tc: None | str | Unset = UNSET
    stock_2024_year_end_e: None | str | Unset = UNSET
    stock_2024_year_end_e_tc: None | str | Unset = UNSET
    stock_2024_year_end_total: None | str | Unset = UNSET
    stock_2024_year_end_total_tc: None | str | Unset = UNSET
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

        stock_2024_year_end_a: None | str | Unset
        if isinstance(self.stock_2024_year_end_a, Unset):
            stock_2024_year_end_a = UNSET
        else:
            stock_2024_year_end_a = self.stock_2024_year_end_a

        stock_2024_year_end_a_tc: None | str | Unset
        if isinstance(self.stock_2024_year_end_a_tc, Unset):
            stock_2024_year_end_a_tc = UNSET
        else:
            stock_2024_year_end_a_tc = self.stock_2024_year_end_a_tc

        stock_2024_year_end_b: None | str | Unset
        if isinstance(self.stock_2024_year_end_b, Unset):
            stock_2024_year_end_b = UNSET
        else:
            stock_2024_year_end_b = self.stock_2024_year_end_b

        stock_2024_year_end_b_tc: None | str | Unset
        if isinstance(self.stock_2024_year_end_b_tc, Unset):
            stock_2024_year_end_b_tc = UNSET
        else:
            stock_2024_year_end_b_tc = self.stock_2024_year_end_b_tc

        stock_2024_year_end_c: None | str | Unset
        if isinstance(self.stock_2024_year_end_c, Unset):
            stock_2024_year_end_c = UNSET
        else:
            stock_2024_year_end_c = self.stock_2024_year_end_c

        stock_2024_year_end_c_tc: None | str | Unset
        if isinstance(self.stock_2024_year_end_c_tc, Unset):
            stock_2024_year_end_c_tc = UNSET
        else:
            stock_2024_year_end_c_tc = self.stock_2024_year_end_c_tc

        stock_2024_year_end_d: None | str | Unset
        if isinstance(self.stock_2024_year_end_d, Unset):
            stock_2024_year_end_d = UNSET
        else:
            stock_2024_year_end_d = self.stock_2024_year_end_d

        stock_2024_year_end_d_tc: None | str | Unset
        if isinstance(self.stock_2024_year_end_d_tc, Unset):
            stock_2024_year_end_d_tc = UNSET
        else:
            stock_2024_year_end_d_tc = self.stock_2024_year_end_d_tc

        stock_2024_year_end_e: None | str | Unset
        if isinstance(self.stock_2024_year_end_e, Unset):
            stock_2024_year_end_e = UNSET
        else:
            stock_2024_year_end_e = self.stock_2024_year_end_e

        stock_2024_year_end_e_tc: None | str | Unset
        if isinstance(self.stock_2024_year_end_e_tc, Unset):
            stock_2024_year_end_e_tc = UNSET
        else:
            stock_2024_year_end_e_tc = self.stock_2024_year_end_e_tc

        stock_2024_year_end_total: None | str | Unset
        if isinstance(self.stock_2024_year_end_total, Unset):
            stock_2024_year_end_total = UNSET
        else:
            stock_2024_year_end_total = self.stock_2024_year_end_total

        stock_2024_year_end_total_tc: None | str | Unset
        if isinstance(self.stock_2024_year_end_total_tc, Unset):
            stock_2024_year_end_total_tc = UNSET
        else:
            stock_2024_year_end_total_tc = self.stock_2024_year_end_total_tc

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
        if stock_2024_year_end_a is not UNSET:
            field_dict["Stock_2024_Year_End_A"] = stock_2024_year_end_a
        if stock_2024_year_end_a_tc is not UNSET:
            field_dict["Stock_2024_Year_End_A_TC"] = stock_2024_year_end_a_tc
        if stock_2024_year_end_b is not UNSET:
            field_dict["Stock_2024_Year_End_B"] = stock_2024_year_end_b
        if stock_2024_year_end_b_tc is not UNSET:
            field_dict["Stock_2024_Year_End_B_TC"] = stock_2024_year_end_b_tc
        if stock_2024_year_end_c is not UNSET:
            field_dict["Stock_2024_Year_End_C"] = stock_2024_year_end_c
        if stock_2024_year_end_c_tc is not UNSET:
            field_dict["Stock_2024_Year_End_C_TC"] = stock_2024_year_end_c_tc
        if stock_2024_year_end_d is not UNSET:
            field_dict["Stock_2024_Year_End_D"] = stock_2024_year_end_d
        if stock_2024_year_end_d_tc is not UNSET:
            field_dict["Stock_2024_Year_End_D_TC"] = stock_2024_year_end_d_tc
        if stock_2024_year_end_e is not UNSET:
            field_dict["Stock_2024_Year_End_E"] = stock_2024_year_end_e
        if stock_2024_year_end_e_tc is not UNSET:
            field_dict["Stock_2024_Year_End_E_TC"] = stock_2024_year_end_e_tc
        if stock_2024_year_end_total is not UNSET:
            field_dict["Stock_2024_Year_End_Total"] = stock_2024_year_end_total
        if stock_2024_year_end_total_tc is not UNSET:
            field_dict["Stock_2024_Year_End_Total_TC"] = stock_2024_year_end_total_tc
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

        def _parse_stock_2024_year_end_a(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_a = _parse_stock_2024_year_end_a(
            d.pop("Stock_2024_Year_End_A", UNSET)
        )

        def _parse_stock_2024_year_end_a_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_a_tc = _parse_stock_2024_year_end_a_tc(
            d.pop("Stock_2024_Year_End_A_TC", UNSET)
        )

        def _parse_stock_2024_year_end_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_b = _parse_stock_2024_year_end_b(
            d.pop("Stock_2024_Year_End_B", UNSET)
        )

        def _parse_stock_2024_year_end_b_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_b_tc = _parse_stock_2024_year_end_b_tc(
            d.pop("Stock_2024_Year_End_B_TC", UNSET)
        )

        def _parse_stock_2024_year_end_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_c = _parse_stock_2024_year_end_c(
            d.pop("Stock_2024_Year_End_C", UNSET)
        )

        def _parse_stock_2024_year_end_c_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_c_tc = _parse_stock_2024_year_end_c_tc(
            d.pop("Stock_2024_Year_End_C_TC", UNSET)
        )

        def _parse_stock_2024_year_end_d(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_d = _parse_stock_2024_year_end_d(
            d.pop("Stock_2024_Year_End_D", UNSET)
        )

        def _parse_stock_2024_year_end_d_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_d_tc = _parse_stock_2024_year_end_d_tc(
            d.pop("Stock_2024_Year_End_D_TC", UNSET)
        )

        def _parse_stock_2024_year_end_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_e = _parse_stock_2024_year_end_e(
            d.pop("Stock_2024_Year_End_E", UNSET)
        )

        def _parse_stock_2024_year_end_e_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_e_tc = _parse_stock_2024_year_end_e_tc(
            d.pop("Stock_2024_Year_End_E_TC", UNSET)
        )

        def _parse_stock_2024_year_end_total(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_total = _parse_stock_2024_year_end_total(
            d.pop("Stock_2024_Year_End_Total", UNSET)
        )

        def _parse_stock_2024_year_end_total_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_total_tc = _parse_stock_2024_year_end_total_tc(
            d.pop("Stock_2024_Year_End_Total_TC", UNSET)
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
            stock_2024_year_end_a=stock_2024_year_end_a,
            stock_2024_year_end_a_tc=stock_2024_year_end_a_tc,
            stock_2024_year_end_b=stock_2024_year_end_b,
            stock_2024_year_end_b_tc=stock_2024_year_end_b_tc,
            stock_2024_year_end_c=stock_2024_year_end_c,
            stock_2024_year_end_c_tc=stock_2024_year_end_c_tc,
            stock_2024_year_end_d=stock_2024_year_end_d,
            stock_2024_year_end_d_tc=stock_2024_year_end_d_tc,
            stock_2024_year_end_e=stock_2024_year_end_e,
            stock_2024_year_end_e_tc=stock_2024_year_end_e_tc,
            stock_2024_year_end_total=stock_2024_year_end_total,
            stock_2024_year_end_total_tc=stock_2024_year_end_total_tc,
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
