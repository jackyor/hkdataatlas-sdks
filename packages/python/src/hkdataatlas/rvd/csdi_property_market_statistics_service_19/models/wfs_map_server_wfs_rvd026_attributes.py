from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsRVD026Attributes")


@_attrs_define
class WfsMapServerWfsRVD026Attributes:
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
        region (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        region_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        quarter (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        quarter_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        a_b_c (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        a_b_c_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        a_b_c_rmk (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        a_b_c_rmk_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        d_e (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        d_e_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        d_e_rmk (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        d_e_rmk_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        overall (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        overall_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        overall_rmk (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        overall_rmk_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into
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
    region: None | str | Unset = UNSET
    region_tc: None | str | Unset = UNSET
    quarter: None | str | Unset = UNSET
    quarter_tc: None | str | Unset = UNSET
    a_b_c: None | str | Unset = UNSET
    a_b_c_tc: None | str | Unset = UNSET
    a_b_c_rmk: None | str | Unset = UNSET
    a_b_c_rmk_tc: None | str | Unset = UNSET
    d_e: None | str | Unset = UNSET
    d_e_tc: None | str | Unset = UNSET
    d_e_rmk: None | str | Unset = UNSET
    d_e_rmk_tc: None | str | Unset = UNSET
    overall: None | str | Unset = UNSET
    overall_tc: None | str | Unset = UNSET
    overall_rmk: None | str | Unset = UNSET
    overall_rmk_tc: None | str | Unset = UNSET
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

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        region_tc: None | str | Unset
        if isinstance(self.region_tc, Unset):
            region_tc = UNSET
        else:
            region_tc = self.region_tc

        quarter: None | str | Unset
        if isinstance(self.quarter, Unset):
            quarter = UNSET
        else:
            quarter = self.quarter

        quarter_tc: None | str | Unset
        if isinstance(self.quarter_tc, Unset):
            quarter_tc = UNSET
        else:
            quarter_tc = self.quarter_tc

        a_b_c: None | str | Unset
        if isinstance(self.a_b_c, Unset):
            a_b_c = UNSET
        else:
            a_b_c = self.a_b_c

        a_b_c_tc: None | str | Unset
        if isinstance(self.a_b_c_tc, Unset):
            a_b_c_tc = UNSET
        else:
            a_b_c_tc = self.a_b_c_tc

        a_b_c_rmk: None | str | Unset
        if isinstance(self.a_b_c_rmk, Unset):
            a_b_c_rmk = UNSET
        else:
            a_b_c_rmk = self.a_b_c_rmk

        a_b_c_rmk_tc: None | str | Unset
        if isinstance(self.a_b_c_rmk_tc, Unset):
            a_b_c_rmk_tc = UNSET
        else:
            a_b_c_rmk_tc = self.a_b_c_rmk_tc

        d_e: None | str | Unset
        if isinstance(self.d_e, Unset):
            d_e = UNSET
        else:
            d_e = self.d_e

        d_e_tc: None | str | Unset
        if isinstance(self.d_e_tc, Unset):
            d_e_tc = UNSET
        else:
            d_e_tc = self.d_e_tc

        d_e_rmk: None | str | Unset
        if isinstance(self.d_e_rmk, Unset):
            d_e_rmk = UNSET
        else:
            d_e_rmk = self.d_e_rmk

        d_e_rmk_tc: None | str | Unset
        if isinstance(self.d_e_rmk_tc, Unset):
            d_e_rmk_tc = UNSET
        else:
            d_e_rmk_tc = self.d_e_rmk_tc

        overall: None | str | Unset
        if isinstance(self.overall, Unset):
            overall = UNSET
        else:
            overall = self.overall

        overall_tc: None | str | Unset
        if isinstance(self.overall_tc, Unset):
            overall_tc = UNSET
        else:
            overall_tc = self.overall_tc

        overall_rmk: None | str | Unset
        if isinstance(self.overall_rmk, Unset):
            overall_rmk = UNSET
        else:
            overall_rmk = self.overall_rmk

        overall_rmk_tc: None | str | Unset
        if isinstance(self.overall_rmk_tc, Unset):
            overall_rmk_tc = UNSET
        else:
            overall_rmk_tc = self.overall_rmk_tc

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
        if region is not UNSET:
            field_dict["Region"] = region
        if region_tc is not UNSET:
            field_dict["Region_TC"] = region_tc
        if quarter is not UNSET:
            field_dict["Quarter"] = quarter
        if quarter_tc is not UNSET:
            field_dict["Quarter_TC"] = quarter_tc
        if a_b_c is not UNSET:
            field_dict["A_B_C"] = a_b_c
        if a_b_c_tc is not UNSET:
            field_dict["A_B_C_TC"] = a_b_c_tc
        if a_b_c_rmk is not UNSET:
            field_dict["A_B_C_Rmk"] = a_b_c_rmk
        if a_b_c_rmk_tc is not UNSET:
            field_dict["A_B_C_Rmk_TC"] = a_b_c_rmk_tc
        if d_e is not UNSET:
            field_dict["D_E"] = d_e
        if d_e_tc is not UNSET:
            field_dict["D_E_TC"] = d_e_tc
        if d_e_rmk is not UNSET:
            field_dict["D_E_Rmk"] = d_e_rmk
        if d_e_rmk_tc is not UNSET:
            field_dict["D_E_Rmk_TC"] = d_e_rmk_tc
        if overall is not UNSET:
            field_dict["Overall"] = overall
        if overall_tc is not UNSET:
            field_dict["Overall_TC"] = overall_tc
        if overall_rmk is not UNSET:
            field_dict["Overall_Rmk"] = overall_rmk
        if overall_rmk_tc is not UNSET:
            field_dict["Overall_Rmk_TC"] = overall_rmk_tc
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

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("Region", UNSET))

        def _parse_region_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region_tc = _parse_region_tc(d.pop("Region_TC", UNSET))

        def _parse_quarter(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quarter = _parse_quarter(d.pop("Quarter", UNSET))

        def _parse_quarter_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quarter_tc = _parse_quarter_tc(d.pop("Quarter_TC", UNSET))

        def _parse_a_b_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        a_b_c = _parse_a_b_c(d.pop("A_B_C", UNSET))

        def _parse_a_b_c_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        a_b_c_tc = _parse_a_b_c_tc(d.pop("A_B_C_TC", UNSET))

        def _parse_a_b_c_rmk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        a_b_c_rmk = _parse_a_b_c_rmk(d.pop("A_B_C_Rmk", UNSET))

        def _parse_a_b_c_rmk_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        a_b_c_rmk_tc = _parse_a_b_c_rmk_tc(d.pop("A_B_C_Rmk_TC", UNSET))

        def _parse_d_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_e = _parse_d_e(d.pop("D_E", UNSET))

        def _parse_d_e_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_e_tc = _parse_d_e_tc(d.pop("D_E_TC", UNSET))

        def _parse_d_e_rmk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_e_rmk = _parse_d_e_rmk(d.pop("D_E_Rmk", UNSET))

        def _parse_d_e_rmk_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        d_e_rmk_tc = _parse_d_e_rmk_tc(d.pop("D_E_Rmk_TC", UNSET))

        def _parse_overall(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overall = _parse_overall(d.pop("Overall", UNSET))

        def _parse_overall_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overall_tc = _parse_overall_tc(d.pop("Overall_TC", UNSET))

        def _parse_overall_rmk(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overall_rmk = _parse_overall_rmk(d.pop("Overall_Rmk", UNSET))

        def _parse_overall_rmk_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overall_rmk_tc = _parse_overall_rmk_tc(d.pop("Overall_Rmk_TC", UNSET))

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

        wfs_map_server_wfs_rvd026_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset=dataset,
            dataset_tc=dataset_tc,
            region=region,
            region_tc=region_tc,
            quarter=quarter,
            quarter_tc=quarter_tc,
            a_b_c=a_b_c,
            a_b_c_tc=a_b_c_tc,
            a_b_c_rmk=a_b_c_rmk,
            a_b_c_rmk_tc=a_b_c_rmk_tc,
            d_e=d_e,
            d_e_tc=d_e_tc,
            d_e_rmk=d_e_rmk,
            d_e_rmk_tc=d_e_rmk_tc,
            overall=overall,
            overall_tc=overall_tc,
            overall_rmk=overall_rmk,
            overall_rmk_tc=overall_rmk_tc,
            last_update=last_update,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_rvd026_attributes.additional_properties = d
        return wfs_map_server_wfs_rvd026_attributes

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
