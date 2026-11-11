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
        stock_2023_year_end (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2023_year_end_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        comp_2024 (None | str | Unset): Publisher field type: esriFieldTypeString
        comp_2024_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        comp_pct_2023_stock (None | str | Unset): Publisher field type: esriFieldTypeString
        comp_pct_2023_stock_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end (None | str | Unset): Publisher field type: esriFieldTypeString
        stock_2024_year_end_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        vac_2024_year_end (None | str | Unset): Publisher field type: esriFieldTypeString
        vac_2024_year_end_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        pct_vac (None | str | Unset): Publisher field type: esriFieldTypeString
        pct_vac_tc (None | str | Unset): Publisher field type: esriFieldTypeString
        last_update (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    dataset: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    stock_2023_year_end: None | str | Unset = UNSET
    stock_2023_year_end_tc: None | str | Unset = UNSET
    comp_2024: None | str | Unset = UNSET
    comp_2024_tc: None | str | Unset = UNSET
    comp_pct_2023_stock: None | str | Unset = UNSET
    comp_pct_2023_stock_tc: None | str | Unset = UNSET
    stock_2024_year_end: None | str | Unset = UNSET
    stock_2024_year_end_tc: None | str | Unset = UNSET
    vac_2024_year_end: None | str | Unset = UNSET
    vac_2024_year_end_tc: None | str | Unset = UNSET
    pct_vac: None | str | Unset = UNSET
    pct_vac_tc: None | str | Unset = UNSET
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

        stock_2023_year_end: None | str | Unset
        if isinstance(self.stock_2023_year_end, Unset):
            stock_2023_year_end = UNSET
        else:
            stock_2023_year_end = self.stock_2023_year_end

        stock_2023_year_end_tc: None | str | Unset
        if isinstance(self.stock_2023_year_end_tc, Unset):
            stock_2023_year_end_tc = UNSET
        else:
            stock_2023_year_end_tc = self.stock_2023_year_end_tc

        comp_2024: None | str | Unset
        if isinstance(self.comp_2024, Unset):
            comp_2024 = UNSET
        else:
            comp_2024 = self.comp_2024

        comp_2024_tc: None | str | Unset
        if isinstance(self.comp_2024_tc, Unset):
            comp_2024_tc = UNSET
        else:
            comp_2024_tc = self.comp_2024_tc

        comp_pct_2023_stock: None | str | Unset
        if isinstance(self.comp_pct_2023_stock, Unset):
            comp_pct_2023_stock = UNSET
        else:
            comp_pct_2023_stock = self.comp_pct_2023_stock

        comp_pct_2023_stock_tc: None | str | Unset
        if isinstance(self.comp_pct_2023_stock_tc, Unset):
            comp_pct_2023_stock_tc = UNSET
        else:
            comp_pct_2023_stock_tc = self.comp_pct_2023_stock_tc

        stock_2024_year_end: None | str | Unset
        if isinstance(self.stock_2024_year_end, Unset):
            stock_2024_year_end = UNSET
        else:
            stock_2024_year_end = self.stock_2024_year_end

        stock_2024_year_end_tc: None | str | Unset
        if isinstance(self.stock_2024_year_end_tc, Unset):
            stock_2024_year_end_tc = UNSET
        else:
            stock_2024_year_end_tc = self.stock_2024_year_end_tc

        vac_2024_year_end: None | str | Unset
        if isinstance(self.vac_2024_year_end, Unset):
            vac_2024_year_end = UNSET
        else:
            vac_2024_year_end = self.vac_2024_year_end

        vac_2024_year_end_tc: None | str | Unset
        if isinstance(self.vac_2024_year_end_tc, Unset):
            vac_2024_year_end_tc = UNSET
        else:
            vac_2024_year_end_tc = self.vac_2024_year_end_tc

        pct_vac: None | str | Unset
        if isinstance(self.pct_vac, Unset):
            pct_vac = UNSET
        else:
            pct_vac = self.pct_vac

        pct_vac_tc: None | str | Unset
        if isinstance(self.pct_vac_tc, Unset):
            pct_vac_tc = UNSET
        else:
            pct_vac_tc = self.pct_vac_tc

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
        if stock_2023_year_end is not UNSET:
            field_dict["Stock_2023_Year_End"] = stock_2023_year_end
        if stock_2023_year_end_tc is not UNSET:
            field_dict["Stock_2023_Year_End_TC"] = stock_2023_year_end_tc
        if comp_2024 is not UNSET:
            field_dict["Comp_2024"] = comp_2024
        if comp_2024_tc is not UNSET:
            field_dict["Comp_2024_TC"] = comp_2024_tc
        if comp_pct_2023_stock is not UNSET:
            field_dict["Comp_Pct_2023_Stock"] = comp_pct_2023_stock
        if comp_pct_2023_stock_tc is not UNSET:
            field_dict["Comp_Pct_2023_Stock_TC"] = comp_pct_2023_stock_tc
        if stock_2024_year_end is not UNSET:
            field_dict["Stock_2024_Year_End"] = stock_2024_year_end
        if stock_2024_year_end_tc is not UNSET:
            field_dict["Stock_2024_Year_End_TC"] = stock_2024_year_end_tc
        if vac_2024_year_end is not UNSET:
            field_dict["Vac_2024_Year_End"] = vac_2024_year_end
        if vac_2024_year_end_tc is not UNSET:
            field_dict["Vac_2024_Year_End_TC"] = vac_2024_year_end_tc
        if pct_vac is not UNSET:
            field_dict["Pct_Vac"] = pct_vac
        if pct_vac_tc is not UNSET:
            field_dict["Pct_Vac_TC"] = pct_vac_tc
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

        def _parse_stock_2023_year_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2023_year_end = _parse_stock_2023_year_end(
            d.pop("Stock_2023_Year_End", UNSET)
        )

        def _parse_stock_2023_year_end_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2023_year_end_tc = _parse_stock_2023_year_end_tc(
            d.pop("Stock_2023_Year_End_TC", UNSET)
        )

        def _parse_comp_2024(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp_2024 = _parse_comp_2024(d.pop("Comp_2024", UNSET))

        def _parse_comp_2024_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp_2024_tc = _parse_comp_2024_tc(d.pop("Comp_2024_TC", UNSET))

        def _parse_comp_pct_2023_stock(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp_pct_2023_stock = _parse_comp_pct_2023_stock(
            d.pop("Comp_Pct_2023_Stock", UNSET)
        )

        def _parse_comp_pct_2023_stock_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comp_pct_2023_stock_tc = _parse_comp_pct_2023_stock_tc(
            d.pop("Comp_Pct_2023_Stock_TC", UNSET)
        )

        def _parse_stock_2024_year_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end = _parse_stock_2024_year_end(
            d.pop("Stock_2024_Year_End", UNSET)
        )

        def _parse_stock_2024_year_end_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_2024_year_end_tc = _parse_stock_2024_year_end_tc(
            d.pop("Stock_2024_Year_End_TC", UNSET)
        )

        def _parse_vac_2024_year_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vac_2024_year_end = _parse_vac_2024_year_end(d.pop("Vac_2024_Year_End", UNSET))

        def _parse_vac_2024_year_end_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vac_2024_year_end_tc = _parse_vac_2024_year_end_tc(
            d.pop("Vac_2024_Year_End_TC", UNSET)
        )

        def _parse_pct_vac(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pct_vac = _parse_pct_vac(d.pop("Pct_Vac", UNSET))

        def _parse_pct_vac_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pct_vac_tc = _parse_pct_vac_tc(d.pop("Pct_Vac_TC", UNSET))

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
            stock_2023_year_end=stock_2023_year_end,
            stock_2023_year_end_tc=stock_2023_year_end_tc,
            comp_2024=comp_2024,
            comp_2024_tc=comp_2024_tc,
            comp_pct_2023_stock=comp_pct_2023_stock,
            comp_pct_2023_stock_tc=comp_pct_2023_stock_tc,
            stock_2024_year_end=stock_2024_year_end,
            stock_2024_year_end_tc=stock_2024_year_end_tc,
            vac_2024_year_end=vac_2024_year_end,
            vac_2024_year_end_tc=vac_2024_year_end_tc,
            pct_vac=pct_vac,
            pct_vac_tc=pct_vac_tc,
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
