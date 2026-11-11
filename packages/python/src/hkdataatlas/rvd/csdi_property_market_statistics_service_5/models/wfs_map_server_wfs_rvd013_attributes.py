from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsRVD013Attributes")


@_attrs_define
class WfsMapServerWfsRVD013Attributes:
    """
    Attributes:
        shape (Any | Unset): Native geometry property gml:MultiSurfacePropertyType; JSON geometry is not inferred from
            its XML type.
        objectid (int | Unset): Native XSD type xsd:int. Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        dataset_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        district_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        district_sub_districts_rmk (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        district_sub_districts_rmk_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        stock_2024_year_end_a (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        stock_2024_year_end_a_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        stock_2024_year_end_b (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        stock_2024_year_end_b_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        stock_2024_year_end_c (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        stock_2024_year_end_c_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        stock_2024_year_end_total (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        stock_2024_year_end_total_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        vac_2024_year_end_a (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        vac_2024_year_end_a_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        vac_2024_year_end_b (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        vac_2024_year_end_b_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        vac_2024_year_end_c (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        vac_2024_year_end_c_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        vac_2024_year_end_total (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        vac_2024_year_end_total_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        pct_vac_a (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        pct_vac_a_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        pct_vac_b (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        pct_vac_b_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        pct_vac_c (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        pct_vac_c_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        pct_vac_total (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        pct_vac_total_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
            all JSON queries.
        last_update (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        shape_length (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML
            occurrence into all JSON queries.
        shape_area (float | None | Unset): Native XSD type xsd:double. Requiredness is not projected from XML occurrence
            into all JSON queries.
    """

    shape: Any | Unset = UNSET
    objectid: int | Unset = UNSET
    dataset: None | str | Unset = UNSET
    dataset_tc: None | str | Unset = UNSET
    district: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    district_sub_districts_rmk: None | str | Unset = UNSET
    district_sub_districts_rmk_tc: None | str | Unset = UNSET
    stock_2024_year_end_a: None | str | Unset = UNSET
    stock_2024_year_end_a_tc: None | str | Unset = UNSET
    stock_2024_year_end_b: None | str | Unset = UNSET
    stock_2024_year_end_b_tc: None | str | Unset = UNSET
    stock_2024_year_end_c: None | str | Unset = UNSET
    stock_2024_year_end_c_tc: None | str | Unset = UNSET
    stock_2024_year_end_total: None | str | Unset = UNSET
    stock_2024_year_end_total_tc: None | str | Unset = UNSET
    vac_2024_year_end_a: None | str | Unset = UNSET
    vac_2024_year_end_a_tc: None | str | Unset = UNSET
    vac_2024_year_end_b: None | str | Unset = UNSET
    vac_2024_year_end_b_tc: None | str | Unset = UNSET
    vac_2024_year_end_c: None | str | Unset = UNSET
    vac_2024_year_end_c_tc: None | str | Unset = UNSET
    vac_2024_year_end_total: None | str | Unset = UNSET
    vac_2024_year_end_total_tc: None | str | Unset = UNSET
    pct_vac_a: None | str | Unset = UNSET
    pct_vac_a_tc: None | str | Unset = UNSET
    pct_vac_b: None | str | Unset = UNSET
    pct_vac_b_tc: None | str | Unset = UNSET
    pct_vac_c: None | str | Unset = UNSET
    pct_vac_c_tc: None | str | Unset = UNSET
    pct_vac_total: None | str | Unset = UNSET
    pct_vac_total_tc: None | str | Unset = UNSET
    last_update: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shape = self.shape

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

        district_sub_districts_rmk: None | str | Unset
        if isinstance(self.district_sub_districts_rmk, Unset):
            district_sub_districts_rmk = UNSET
        else:
            district_sub_districts_rmk = self.district_sub_districts_rmk

        district_sub_districts_rmk_tc: None | str | Unset
        if isinstance(self.district_sub_districts_rmk_tc, Unset):
            district_sub_districts_rmk_tc = UNSET
        else:
            district_sub_districts_rmk_tc = self.district_sub_districts_rmk_tc

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

        vac_2024_year_end_a: None | str | Unset
        if isinstance(self.vac_2024_year_end_a, Unset):
            vac_2024_year_end_a = UNSET
        else:
            vac_2024_year_end_a = self.vac_2024_year_end_a

        vac_2024_year_end_a_tc: None | str | Unset
        if isinstance(self.vac_2024_year_end_a_tc, Unset):
            vac_2024_year_end_a_tc = UNSET
        else:
            vac_2024_year_end_a_tc = self.vac_2024_year_end_a_tc

        vac_2024_year_end_b: None | str | Unset
        if isinstance(self.vac_2024_year_end_b, Unset):
            vac_2024_year_end_b = UNSET
        else:
            vac_2024_year_end_b = self.vac_2024_year_end_b

        vac_2024_year_end_b_tc: None | str | Unset
        if isinstance(self.vac_2024_year_end_b_tc, Unset):
            vac_2024_year_end_b_tc = UNSET
        else:
            vac_2024_year_end_b_tc = self.vac_2024_year_end_b_tc

        vac_2024_year_end_c: None | str | Unset
        if isinstance(self.vac_2024_year_end_c, Unset):
            vac_2024_year_end_c = UNSET
        else:
            vac_2024_year_end_c = self.vac_2024_year_end_c

        vac_2024_year_end_c_tc: None | str | Unset
        if isinstance(self.vac_2024_year_end_c_tc, Unset):
            vac_2024_year_end_c_tc = UNSET
        else:
            vac_2024_year_end_c_tc = self.vac_2024_year_end_c_tc

        vac_2024_year_end_total: None | str | Unset
        if isinstance(self.vac_2024_year_end_total, Unset):
            vac_2024_year_end_total = UNSET
        else:
            vac_2024_year_end_total = self.vac_2024_year_end_total

        vac_2024_year_end_total_tc: None | str | Unset
        if isinstance(self.vac_2024_year_end_total_tc, Unset):
            vac_2024_year_end_total_tc = UNSET
        else:
            vac_2024_year_end_total_tc = self.vac_2024_year_end_total_tc

        pct_vac_a: None | str | Unset
        if isinstance(self.pct_vac_a, Unset):
            pct_vac_a = UNSET
        else:
            pct_vac_a = self.pct_vac_a

        pct_vac_a_tc: None | str | Unset
        if isinstance(self.pct_vac_a_tc, Unset):
            pct_vac_a_tc = UNSET
        else:
            pct_vac_a_tc = self.pct_vac_a_tc

        pct_vac_b: None | str | Unset
        if isinstance(self.pct_vac_b, Unset):
            pct_vac_b = UNSET
        else:
            pct_vac_b = self.pct_vac_b

        pct_vac_b_tc: None | str | Unset
        if isinstance(self.pct_vac_b_tc, Unset):
            pct_vac_b_tc = UNSET
        else:
            pct_vac_b_tc = self.pct_vac_b_tc

        pct_vac_c: None | str | Unset
        if isinstance(self.pct_vac_c, Unset):
            pct_vac_c = UNSET
        else:
            pct_vac_c = self.pct_vac_c

        pct_vac_c_tc: None | str | Unset
        if isinstance(self.pct_vac_c_tc, Unset):
            pct_vac_c_tc = UNSET
        else:
            pct_vac_c_tc = self.pct_vac_c_tc

        pct_vac_total: None | str | Unset
        if isinstance(self.pct_vac_total, Unset):
            pct_vac_total = UNSET
        else:
            pct_vac_total = self.pct_vac_total

        pct_vac_total_tc: None | str | Unset
        if isinstance(self.pct_vac_total_tc, Unset):
            pct_vac_total_tc = UNSET
        else:
            pct_vac_total_tc = self.pct_vac_total_tc

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
        if shape is not UNSET:
            field_dict["SHAPE"] = shape
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
        if district_sub_districts_rmk is not UNSET:
            field_dict["District_Sub_Districts_Rmk"] = district_sub_districts_rmk
        if district_sub_districts_rmk_tc is not UNSET:
            field_dict["District_Sub_Districts_Rmk_TC"] = district_sub_districts_rmk_tc
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
        if stock_2024_year_end_total is not UNSET:
            field_dict["Stock_2024_Year_End_Total"] = stock_2024_year_end_total
        if stock_2024_year_end_total_tc is not UNSET:
            field_dict["Stock_2024_Year_End_Total_TC"] = stock_2024_year_end_total_tc
        if vac_2024_year_end_a is not UNSET:
            field_dict["Vac_2024_Year_End_A"] = vac_2024_year_end_a
        if vac_2024_year_end_a_tc is not UNSET:
            field_dict["Vac_2024_Year_End_A_TC"] = vac_2024_year_end_a_tc
        if vac_2024_year_end_b is not UNSET:
            field_dict["Vac_2024_Year_End_B"] = vac_2024_year_end_b
        if vac_2024_year_end_b_tc is not UNSET:
            field_dict["Vac_2024_Year_End_B_TC"] = vac_2024_year_end_b_tc
        if vac_2024_year_end_c is not UNSET:
            field_dict["Vac_2024_Year_End_C"] = vac_2024_year_end_c
        if vac_2024_year_end_c_tc is not UNSET:
            field_dict["Vac_2024_Year_End_C_TC"] = vac_2024_year_end_c_tc
        if vac_2024_year_end_total is not UNSET:
            field_dict["Vac_2024_Year_End_Total"] = vac_2024_year_end_total
        if vac_2024_year_end_total_tc is not UNSET:
            field_dict["Vac_2024_Year_End_Total_TC"] = vac_2024_year_end_total_tc
        if pct_vac_a is not UNSET:
            field_dict["Pct_Vac_A"] = pct_vac_a
        if pct_vac_a_tc is not UNSET:
            field_dict["Pct_Vac_A_TC"] = pct_vac_a_tc
        if pct_vac_b is not UNSET:
            field_dict["Pct_Vac_B"] = pct_vac_b
        if pct_vac_b_tc is not UNSET:
            field_dict["Pct_Vac_B_TC"] = pct_vac_b_tc
        if pct_vac_c is not UNSET:
            field_dict["Pct_Vac_C"] = pct_vac_c
        if pct_vac_c_tc is not UNSET:
            field_dict["Pct_Vac_C_TC"] = pct_vac_c_tc
        if pct_vac_total is not UNSET:
            field_dict["Pct_Vac_Total"] = pct_vac_total
        if pct_vac_total_tc is not UNSET:
            field_dict["Pct_Vac_Total_TC"] = pct_vac_total_tc
        if last_update is not UNSET:
            field_dict["LastUpdate"] = last_update
        if shape_length is not UNSET:
            field_dict["SHAPE_Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["SHAPE_Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        shape = d.pop("SHAPE", UNSET)

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

        def _parse_district_sub_districts_rmk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sub_districts_rmk = _parse_district_sub_districts_rmk(
            d.pop("District_Sub_Districts_Rmk", UNSET)
        )

        def _parse_district_sub_districts_rmk_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        district_sub_districts_rmk_tc = _parse_district_sub_districts_rmk_tc(
            d.pop("District_Sub_Districts_Rmk_TC", UNSET)
        )

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

        def _parse_vac_2024_year_end_a(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vac_2024_year_end_a = _parse_vac_2024_year_end_a(
            d.pop("Vac_2024_Year_End_A", UNSET)
        )

        def _parse_vac_2024_year_end_a_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vac_2024_year_end_a_tc = _parse_vac_2024_year_end_a_tc(
            d.pop("Vac_2024_Year_End_A_TC", UNSET)
        )

        def _parse_vac_2024_year_end_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vac_2024_year_end_b = _parse_vac_2024_year_end_b(
            d.pop("Vac_2024_Year_End_B", UNSET)
        )

        def _parse_vac_2024_year_end_b_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vac_2024_year_end_b_tc = _parse_vac_2024_year_end_b_tc(
            d.pop("Vac_2024_Year_End_B_TC", UNSET)
        )

        def _parse_vac_2024_year_end_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vac_2024_year_end_c = _parse_vac_2024_year_end_c(
            d.pop("Vac_2024_Year_End_C", UNSET)
        )

        def _parse_vac_2024_year_end_c_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vac_2024_year_end_c_tc = _parse_vac_2024_year_end_c_tc(
            d.pop("Vac_2024_Year_End_C_TC", UNSET)
        )

        def _parse_vac_2024_year_end_total(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vac_2024_year_end_total = _parse_vac_2024_year_end_total(
            d.pop("Vac_2024_Year_End_Total", UNSET)
        )

        def _parse_vac_2024_year_end_total_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vac_2024_year_end_total_tc = _parse_vac_2024_year_end_total_tc(
            d.pop("Vac_2024_Year_End_Total_TC", UNSET)
        )

        def _parse_pct_vac_a(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pct_vac_a = _parse_pct_vac_a(d.pop("Pct_Vac_A", UNSET))

        def _parse_pct_vac_a_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pct_vac_a_tc = _parse_pct_vac_a_tc(d.pop("Pct_Vac_A_TC", UNSET))

        def _parse_pct_vac_b(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pct_vac_b = _parse_pct_vac_b(d.pop("Pct_Vac_B", UNSET))

        def _parse_pct_vac_b_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pct_vac_b_tc = _parse_pct_vac_b_tc(d.pop("Pct_Vac_B_TC", UNSET))

        def _parse_pct_vac_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pct_vac_c = _parse_pct_vac_c(d.pop("Pct_Vac_C", UNSET))

        def _parse_pct_vac_c_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pct_vac_c_tc = _parse_pct_vac_c_tc(d.pop("Pct_Vac_C_TC", UNSET))

        def _parse_pct_vac_total(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pct_vac_total = _parse_pct_vac_total(d.pop("Pct_Vac_Total", UNSET))

        def _parse_pct_vac_total_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pct_vac_total_tc = _parse_pct_vac_total_tc(d.pop("Pct_Vac_Total_TC", UNSET))

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

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("SHAPE_Area", UNSET))

        wfs_map_server_wfs_rvd013_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset=dataset,
            dataset_tc=dataset_tc,
            district=district,
            district_tc=district_tc,
            district_sub_districts_rmk=district_sub_districts_rmk,
            district_sub_districts_rmk_tc=district_sub_districts_rmk_tc,
            stock_2024_year_end_a=stock_2024_year_end_a,
            stock_2024_year_end_a_tc=stock_2024_year_end_a_tc,
            stock_2024_year_end_b=stock_2024_year_end_b,
            stock_2024_year_end_b_tc=stock_2024_year_end_b_tc,
            stock_2024_year_end_c=stock_2024_year_end_c,
            stock_2024_year_end_c_tc=stock_2024_year_end_c_tc,
            stock_2024_year_end_total=stock_2024_year_end_total,
            stock_2024_year_end_total_tc=stock_2024_year_end_total_tc,
            vac_2024_year_end_a=vac_2024_year_end_a,
            vac_2024_year_end_a_tc=vac_2024_year_end_a_tc,
            vac_2024_year_end_b=vac_2024_year_end_b,
            vac_2024_year_end_b_tc=vac_2024_year_end_b_tc,
            vac_2024_year_end_c=vac_2024_year_end_c,
            vac_2024_year_end_c_tc=vac_2024_year_end_c_tc,
            vac_2024_year_end_total=vac_2024_year_end_total,
            vac_2024_year_end_total_tc=vac_2024_year_end_total_tc,
            pct_vac_a=pct_vac_a,
            pct_vac_a_tc=pct_vac_a_tc,
            pct_vac_b=pct_vac_b,
            pct_vac_b_tc=pct_vac_b_tc,
            pct_vac_c=pct_vac_c,
            pct_vac_c_tc=pct_vac_c_tc,
            pct_vac_total=pct_vac_total,
            pct_vac_total_tc=pct_vac_total_tc,
            last_update=last_update,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_rvd013_attributes.additional_properties = d
        return wfs_map_server_wfs_rvd013_attributes

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
