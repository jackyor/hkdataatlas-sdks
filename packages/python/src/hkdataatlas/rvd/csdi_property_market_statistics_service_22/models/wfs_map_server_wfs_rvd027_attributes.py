from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsRVD027Attributes")


@_attrs_define
class WfsMapServerWfsRVD027Attributes:
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
        year_end (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all JSON
            queries.
        year_end_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence into all
            JSON queries.
        yr_of_comp_pre_1960_overall_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_pre_1960_overall_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_196069_overall_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_196069_overall_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_197079_overall_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_197079_overall_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_198089_overall_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_198089_overall_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_199099_overall_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_199099_overall_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_200009_overall_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_200009_overall_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_post_2009_overall_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_post_2009_overall_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        stock_no_of_unit_overall (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        stock_no_of_unit_overall_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        yr_of_comp_pre_1960_small_medium_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_pre_1960_small_medium_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        yr_of_comp_196069_small_medium_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_196069_small_medium_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        yr_of_comp_197079_small_medium_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_197079_small_medium_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        yr_of_comp_198089_small_medium_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_198089_small_medium_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        yr_of_comp_199099_small_medium_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_199099_small_medium_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        yr_of_comp_200009_small_medium_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_200009_small_medium_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        yr_of_comp_post_2009_small_medium_stock_pct (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        yr_of_comp_post_2009_small_medium_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not
            projected from XML occurrence into all JSON queries.
        stock_no_of_unit_small_medium (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        stock_no_of_unit_small_medium_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        yr_of_comp_pre_1960_large_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_pre_1960_large_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        yr_of_comp_196069_large_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        yr_of_comp_196069_large_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_197079_large_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        yr_of_comp_197079_large_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_198089_large_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        yr_of_comp_198089_large_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_199099_large_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        yr_of_comp_199099_large_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_200009_large_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        yr_of_comp_200009_large_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_post_2009_large_stock_pct (None | str | Unset): Native XSD type . Requiredness is not projected from
            XML occurrence into all JSON queries.
        yr_of_comp_post_2009_large_stock_pct_tc (None | str | Unset): Native XSD type . Requiredness is not projected
            from XML occurrence into all JSON queries.
        stock_no_of_unit_large (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        stock_no_of_unit_large_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
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
    year_end: None | str | Unset = UNSET
    year_end_tc: None | str | Unset = UNSET
    yr_of_comp_pre_1960_overall_stock_pct: None | str | Unset = UNSET
    yr_of_comp_pre_1960_overall_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_196069_overall_stock_pct: None | str | Unset = UNSET
    yr_of_comp_196069_overall_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_197079_overall_stock_pct: None | str | Unset = UNSET
    yr_of_comp_197079_overall_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_198089_overall_stock_pct: None | str | Unset = UNSET
    yr_of_comp_198089_overall_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_199099_overall_stock_pct: None | str | Unset = UNSET
    yr_of_comp_199099_overall_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_200009_overall_stock_pct: None | str | Unset = UNSET
    yr_of_comp_200009_overall_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_post_2009_overall_stock_pct: None | str | Unset = UNSET
    yr_of_comp_post_2009_overall_stock_pct_tc: None | str | Unset = UNSET
    stock_no_of_unit_overall: None | str | Unset = UNSET
    stock_no_of_unit_overall_tc: None | str | Unset = UNSET
    yr_of_comp_pre_1960_small_medium_stock_pct: None | str | Unset = UNSET
    yr_of_comp_pre_1960_small_medium_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_196069_small_medium_stock_pct: None | str | Unset = UNSET
    yr_of_comp_196069_small_medium_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_197079_small_medium_stock_pct: None | str | Unset = UNSET
    yr_of_comp_197079_small_medium_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_198089_small_medium_stock_pct: None | str | Unset = UNSET
    yr_of_comp_198089_small_medium_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_199099_small_medium_stock_pct: None | str | Unset = UNSET
    yr_of_comp_199099_small_medium_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_200009_small_medium_stock_pct: None | str | Unset = UNSET
    yr_of_comp_200009_small_medium_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_post_2009_small_medium_stock_pct: None | str | Unset = UNSET
    yr_of_comp_post_2009_small_medium_stock_pct_tc: None | str | Unset = UNSET
    stock_no_of_unit_small_medium: None | str | Unset = UNSET
    stock_no_of_unit_small_medium_tc: None | str | Unset = UNSET
    yr_of_comp_pre_1960_large_stock_pct: None | str | Unset = UNSET
    yr_of_comp_pre_1960_large_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_196069_large_stock_pct: None | str | Unset = UNSET
    yr_of_comp_196069_large_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_197079_large_stock_pct: None | str | Unset = UNSET
    yr_of_comp_197079_large_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_198089_large_stock_pct: None | str | Unset = UNSET
    yr_of_comp_198089_large_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_199099_large_stock_pct: None | str | Unset = UNSET
    yr_of_comp_199099_large_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_200009_large_stock_pct: None | str | Unset = UNSET
    yr_of_comp_200009_large_stock_pct_tc: None | str | Unset = UNSET
    yr_of_comp_post_2009_large_stock_pct: None | str | Unset = UNSET
    yr_of_comp_post_2009_large_stock_pct_tc: None | str | Unset = UNSET
    stock_no_of_unit_large: None | str | Unset = UNSET
    stock_no_of_unit_large_tc: None | str | Unset = UNSET
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

        year_end: None | str | Unset
        if isinstance(self.year_end, Unset):
            year_end = UNSET
        else:
            year_end = self.year_end

        year_end_tc: None | str | Unset
        if isinstance(self.year_end_tc, Unset):
            year_end_tc = UNSET
        else:
            year_end_tc = self.year_end_tc

        yr_of_comp_pre_1960_overall_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_pre_1960_overall_stock_pct, Unset):
            yr_of_comp_pre_1960_overall_stock_pct = UNSET
        else:
            yr_of_comp_pre_1960_overall_stock_pct = (
                self.yr_of_comp_pre_1960_overall_stock_pct
            )

        yr_of_comp_pre_1960_overall_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_pre_1960_overall_stock_pct_tc, Unset):
            yr_of_comp_pre_1960_overall_stock_pct_tc = UNSET
        else:
            yr_of_comp_pre_1960_overall_stock_pct_tc = (
                self.yr_of_comp_pre_1960_overall_stock_pct_tc
            )

        yr_of_comp_196069_overall_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_196069_overall_stock_pct, Unset):
            yr_of_comp_196069_overall_stock_pct = UNSET
        else:
            yr_of_comp_196069_overall_stock_pct = (
                self.yr_of_comp_196069_overall_stock_pct
            )

        yr_of_comp_196069_overall_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_196069_overall_stock_pct_tc, Unset):
            yr_of_comp_196069_overall_stock_pct_tc = UNSET
        else:
            yr_of_comp_196069_overall_stock_pct_tc = (
                self.yr_of_comp_196069_overall_stock_pct_tc
            )

        yr_of_comp_197079_overall_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_197079_overall_stock_pct, Unset):
            yr_of_comp_197079_overall_stock_pct = UNSET
        else:
            yr_of_comp_197079_overall_stock_pct = (
                self.yr_of_comp_197079_overall_stock_pct
            )

        yr_of_comp_197079_overall_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_197079_overall_stock_pct_tc, Unset):
            yr_of_comp_197079_overall_stock_pct_tc = UNSET
        else:
            yr_of_comp_197079_overall_stock_pct_tc = (
                self.yr_of_comp_197079_overall_stock_pct_tc
            )

        yr_of_comp_198089_overall_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_198089_overall_stock_pct, Unset):
            yr_of_comp_198089_overall_stock_pct = UNSET
        else:
            yr_of_comp_198089_overall_stock_pct = (
                self.yr_of_comp_198089_overall_stock_pct
            )

        yr_of_comp_198089_overall_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_198089_overall_stock_pct_tc, Unset):
            yr_of_comp_198089_overall_stock_pct_tc = UNSET
        else:
            yr_of_comp_198089_overall_stock_pct_tc = (
                self.yr_of_comp_198089_overall_stock_pct_tc
            )

        yr_of_comp_199099_overall_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_199099_overall_stock_pct, Unset):
            yr_of_comp_199099_overall_stock_pct = UNSET
        else:
            yr_of_comp_199099_overall_stock_pct = (
                self.yr_of_comp_199099_overall_stock_pct
            )

        yr_of_comp_199099_overall_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_199099_overall_stock_pct_tc, Unset):
            yr_of_comp_199099_overall_stock_pct_tc = UNSET
        else:
            yr_of_comp_199099_overall_stock_pct_tc = (
                self.yr_of_comp_199099_overall_stock_pct_tc
            )

        yr_of_comp_200009_overall_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_200009_overall_stock_pct, Unset):
            yr_of_comp_200009_overall_stock_pct = UNSET
        else:
            yr_of_comp_200009_overall_stock_pct = (
                self.yr_of_comp_200009_overall_stock_pct
            )

        yr_of_comp_200009_overall_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_200009_overall_stock_pct_tc, Unset):
            yr_of_comp_200009_overall_stock_pct_tc = UNSET
        else:
            yr_of_comp_200009_overall_stock_pct_tc = (
                self.yr_of_comp_200009_overall_stock_pct_tc
            )

        yr_of_comp_post_2009_overall_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_post_2009_overall_stock_pct, Unset):
            yr_of_comp_post_2009_overall_stock_pct = UNSET
        else:
            yr_of_comp_post_2009_overall_stock_pct = (
                self.yr_of_comp_post_2009_overall_stock_pct
            )

        yr_of_comp_post_2009_overall_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_post_2009_overall_stock_pct_tc, Unset):
            yr_of_comp_post_2009_overall_stock_pct_tc = UNSET
        else:
            yr_of_comp_post_2009_overall_stock_pct_tc = (
                self.yr_of_comp_post_2009_overall_stock_pct_tc
            )

        stock_no_of_unit_overall: None | str | Unset
        if isinstance(self.stock_no_of_unit_overall, Unset):
            stock_no_of_unit_overall = UNSET
        else:
            stock_no_of_unit_overall = self.stock_no_of_unit_overall

        stock_no_of_unit_overall_tc: None | str | Unset
        if isinstance(self.stock_no_of_unit_overall_tc, Unset):
            stock_no_of_unit_overall_tc = UNSET
        else:
            stock_no_of_unit_overall_tc = self.stock_no_of_unit_overall_tc

        yr_of_comp_pre_1960_small_medium_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_pre_1960_small_medium_stock_pct, Unset):
            yr_of_comp_pre_1960_small_medium_stock_pct = UNSET
        else:
            yr_of_comp_pre_1960_small_medium_stock_pct = (
                self.yr_of_comp_pre_1960_small_medium_stock_pct
            )

        yr_of_comp_pre_1960_small_medium_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_pre_1960_small_medium_stock_pct_tc, Unset):
            yr_of_comp_pre_1960_small_medium_stock_pct_tc = UNSET
        else:
            yr_of_comp_pre_1960_small_medium_stock_pct_tc = (
                self.yr_of_comp_pre_1960_small_medium_stock_pct_tc
            )

        yr_of_comp_196069_small_medium_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_196069_small_medium_stock_pct, Unset):
            yr_of_comp_196069_small_medium_stock_pct = UNSET
        else:
            yr_of_comp_196069_small_medium_stock_pct = (
                self.yr_of_comp_196069_small_medium_stock_pct
            )

        yr_of_comp_196069_small_medium_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_196069_small_medium_stock_pct_tc, Unset):
            yr_of_comp_196069_small_medium_stock_pct_tc = UNSET
        else:
            yr_of_comp_196069_small_medium_stock_pct_tc = (
                self.yr_of_comp_196069_small_medium_stock_pct_tc
            )

        yr_of_comp_197079_small_medium_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_197079_small_medium_stock_pct, Unset):
            yr_of_comp_197079_small_medium_stock_pct = UNSET
        else:
            yr_of_comp_197079_small_medium_stock_pct = (
                self.yr_of_comp_197079_small_medium_stock_pct
            )

        yr_of_comp_197079_small_medium_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_197079_small_medium_stock_pct_tc, Unset):
            yr_of_comp_197079_small_medium_stock_pct_tc = UNSET
        else:
            yr_of_comp_197079_small_medium_stock_pct_tc = (
                self.yr_of_comp_197079_small_medium_stock_pct_tc
            )

        yr_of_comp_198089_small_medium_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_198089_small_medium_stock_pct, Unset):
            yr_of_comp_198089_small_medium_stock_pct = UNSET
        else:
            yr_of_comp_198089_small_medium_stock_pct = (
                self.yr_of_comp_198089_small_medium_stock_pct
            )

        yr_of_comp_198089_small_medium_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_198089_small_medium_stock_pct_tc, Unset):
            yr_of_comp_198089_small_medium_stock_pct_tc = UNSET
        else:
            yr_of_comp_198089_small_medium_stock_pct_tc = (
                self.yr_of_comp_198089_small_medium_stock_pct_tc
            )

        yr_of_comp_199099_small_medium_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_199099_small_medium_stock_pct, Unset):
            yr_of_comp_199099_small_medium_stock_pct = UNSET
        else:
            yr_of_comp_199099_small_medium_stock_pct = (
                self.yr_of_comp_199099_small_medium_stock_pct
            )

        yr_of_comp_199099_small_medium_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_199099_small_medium_stock_pct_tc, Unset):
            yr_of_comp_199099_small_medium_stock_pct_tc = UNSET
        else:
            yr_of_comp_199099_small_medium_stock_pct_tc = (
                self.yr_of_comp_199099_small_medium_stock_pct_tc
            )

        yr_of_comp_200009_small_medium_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_200009_small_medium_stock_pct, Unset):
            yr_of_comp_200009_small_medium_stock_pct = UNSET
        else:
            yr_of_comp_200009_small_medium_stock_pct = (
                self.yr_of_comp_200009_small_medium_stock_pct
            )

        yr_of_comp_200009_small_medium_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_200009_small_medium_stock_pct_tc, Unset):
            yr_of_comp_200009_small_medium_stock_pct_tc = UNSET
        else:
            yr_of_comp_200009_small_medium_stock_pct_tc = (
                self.yr_of_comp_200009_small_medium_stock_pct_tc
            )

        yr_of_comp_post_2009_small_medium_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_post_2009_small_medium_stock_pct, Unset):
            yr_of_comp_post_2009_small_medium_stock_pct = UNSET
        else:
            yr_of_comp_post_2009_small_medium_stock_pct = (
                self.yr_of_comp_post_2009_small_medium_stock_pct
            )

        yr_of_comp_post_2009_small_medium_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_post_2009_small_medium_stock_pct_tc, Unset):
            yr_of_comp_post_2009_small_medium_stock_pct_tc = UNSET
        else:
            yr_of_comp_post_2009_small_medium_stock_pct_tc = (
                self.yr_of_comp_post_2009_small_medium_stock_pct_tc
            )

        stock_no_of_unit_small_medium: None | str | Unset
        if isinstance(self.stock_no_of_unit_small_medium, Unset):
            stock_no_of_unit_small_medium = UNSET
        else:
            stock_no_of_unit_small_medium = self.stock_no_of_unit_small_medium

        stock_no_of_unit_small_medium_tc: None | str | Unset
        if isinstance(self.stock_no_of_unit_small_medium_tc, Unset):
            stock_no_of_unit_small_medium_tc = UNSET
        else:
            stock_no_of_unit_small_medium_tc = self.stock_no_of_unit_small_medium_tc

        yr_of_comp_pre_1960_large_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_pre_1960_large_stock_pct, Unset):
            yr_of_comp_pre_1960_large_stock_pct = UNSET
        else:
            yr_of_comp_pre_1960_large_stock_pct = (
                self.yr_of_comp_pre_1960_large_stock_pct
            )

        yr_of_comp_pre_1960_large_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_pre_1960_large_stock_pct_tc, Unset):
            yr_of_comp_pre_1960_large_stock_pct_tc = UNSET
        else:
            yr_of_comp_pre_1960_large_stock_pct_tc = (
                self.yr_of_comp_pre_1960_large_stock_pct_tc
            )

        yr_of_comp_196069_large_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_196069_large_stock_pct, Unset):
            yr_of_comp_196069_large_stock_pct = UNSET
        else:
            yr_of_comp_196069_large_stock_pct = self.yr_of_comp_196069_large_stock_pct

        yr_of_comp_196069_large_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_196069_large_stock_pct_tc, Unset):
            yr_of_comp_196069_large_stock_pct_tc = UNSET
        else:
            yr_of_comp_196069_large_stock_pct_tc = (
                self.yr_of_comp_196069_large_stock_pct_tc
            )

        yr_of_comp_197079_large_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_197079_large_stock_pct, Unset):
            yr_of_comp_197079_large_stock_pct = UNSET
        else:
            yr_of_comp_197079_large_stock_pct = self.yr_of_comp_197079_large_stock_pct

        yr_of_comp_197079_large_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_197079_large_stock_pct_tc, Unset):
            yr_of_comp_197079_large_stock_pct_tc = UNSET
        else:
            yr_of_comp_197079_large_stock_pct_tc = (
                self.yr_of_comp_197079_large_stock_pct_tc
            )

        yr_of_comp_198089_large_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_198089_large_stock_pct, Unset):
            yr_of_comp_198089_large_stock_pct = UNSET
        else:
            yr_of_comp_198089_large_stock_pct = self.yr_of_comp_198089_large_stock_pct

        yr_of_comp_198089_large_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_198089_large_stock_pct_tc, Unset):
            yr_of_comp_198089_large_stock_pct_tc = UNSET
        else:
            yr_of_comp_198089_large_stock_pct_tc = (
                self.yr_of_comp_198089_large_stock_pct_tc
            )

        yr_of_comp_199099_large_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_199099_large_stock_pct, Unset):
            yr_of_comp_199099_large_stock_pct = UNSET
        else:
            yr_of_comp_199099_large_stock_pct = self.yr_of_comp_199099_large_stock_pct

        yr_of_comp_199099_large_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_199099_large_stock_pct_tc, Unset):
            yr_of_comp_199099_large_stock_pct_tc = UNSET
        else:
            yr_of_comp_199099_large_stock_pct_tc = (
                self.yr_of_comp_199099_large_stock_pct_tc
            )

        yr_of_comp_200009_large_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_200009_large_stock_pct, Unset):
            yr_of_comp_200009_large_stock_pct = UNSET
        else:
            yr_of_comp_200009_large_stock_pct = self.yr_of_comp_200009_large_stock_pct

        yr_of_comp_200009_large_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_200009_large_stock_pct_tc, Unset):
            yr_of_comp_200009_large_stock_pct_tc = UNSET
        else:
            yr_of_comp_200009_large_stock_pct_tc = (
                self.yr_of_comp_200009_large_stock_pct_tc
            )

        yr_of_comp_post_2009_large_stock_pct: None | str | Unset
        if isinstance(self.yr_of_comp_post_2009_large_stock_pct, Unset):
            yr_of_comp_post_2009_large_stock_pct = UNSET
        else:
            yr_of_comp_post_2009_large_stock_pct = (
                self.yr_of_comp_post_2009_large_stock_pct
            )

        yr_of_comp_post_2009_large_stock_pct_tc: None | str | Unset
        if isinstance(self.yr_of_comp_post_2009_large_stock_pct_tc, Unset):
            yr_of_comp_post_2009_large_stock_pct_tc = UNSET
        else:
            yr_of_comp_post_2009_large_stock_pct_tc = (
                self.yr_of_comp_post_2009_large_stock_pct_tc
            )

        stock_no_of_unit_large: None | str | Unset
        if isinstance(self.stock_no_of_unit_large, Unset):
            stock_no_of_unit_large = UNSET
        else:
            stock_no_of_unit_large = self.stock_no_of_unit_large

        stock_no_of_unit_large_tc: None | str | Unset
        if isinstance(self.stock_no_of_unit_large_tc, Unset):
            stock_no_of_unit_large_tc = UNSET
        else:
            stock_no_of_unit_large_tc = self.stock_no_of_unit_large_tc

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
        if year_end is not UNSET:
            field_dict["Year_End"] = year_end
        if year_end_tc is not UNSET:
            field_dict["Year_End_TC"] = year_end_tc
        if yr_of_comp_pre_1960_overall_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_Pre1960_Overall_Stock_Pct"] = (
                yr_of_comp_pre_1960_overall_stock_pct
            )
        if yr_of_comp_pre_1960_overall_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_Pre1960_Overall_Stock_Pct_TC"] = (
                yr_of_comp_pre_1960_overall_stock_pct_tc
            )
        if yr_of_comp_196069_overall_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_196069_Overall_Stock_Pct"] = (
                yr_of_comp_196069_overall_stock_pct
            )
        if yr_of_comp_196069_overall_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_196069_Overall_Stock_Pct_TC"] = (
                yr_of_comp_196069_overall_stock_pct_tc
            )
        if yr_of_comp_197079_overall_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_197079_Overall_Stock_Pct"] = (
                yr_of_comp_197079_overall_stock_pct
            )
        if yr_of_comp_197079_overall_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_197079_Overall_Stock_Pct_TC"] = (
                yr_of_comp_197079_overall_stock_pct_tc
            )
        if yr_of_comp_198089_overall_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_198089_Overall_Stock_Pct"] = (
                yr_of_comp_198089_overall_stock_pct
            )
        if yr_of_comp_198089_overall_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_198089_Overall_Stock_Pct_TC"] = (
                yr_of_comp_198089_overall_stock_pct_tc
            )
        if yr_of_comp_199099_overall_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_199099_Overall_Stock_Pct"] = (
                yr_of_comp_199099_overall_stock_pct
            )
        if yr_of_comp_199099_overall_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_199099_Overall_Stock_Pct_TC"] = (
                yr_of_comp_199099_overall_stock_pct_tc
            )
        if yr_of_comp_200009_overall_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_200009_Overall_Stock_Pct"] = (
                yr_of_comp_200009_overall_stock_pct
            )
        if yr_of_comp_200009_overall_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_200009_Overall_Stock_Pct_TC"] = (
                yr_of_comp_200009_overall_stock_pct_tc
            )
        if yr_of_comp_post_2009_overall_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_Post2009_Overall_Stock_Pct"] = (
                yr_of_comp_post_2009_overall_stock_pct
            )
        if yr_of_comp_post_2009_overall_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_Post2009_Overall_Stock_Pct_TC"] = (
                yr_of_comp_post_2009_overall_stock_pct_tc
            )
        if stock_no_of_unit_overall is not UNSET:
            field_dict["Stock_No_of_Unit_Overall"] = stock_no_of_unit_overall
        if stock_no_of_unit_overall_tc is not UNSET:
            field_dict["Stock_No_of_Unit_Overall_TC"] = stock_no_of_unit_overall_tc
        if yr_of_comp_pre_1960_small_medium_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_Pre1960_Small_Medium_Stock_Pct"] = (
                yr_of_comp_pre_1960_small_medium_stock_pct
            )
        if yr_of_comp_pre_1960_small_medium_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_Pre1960_Small_Medium_Stock_Pct_TC"] = (
                yr_of_comp_pre_1960_small_medium_stock_pct_tc
            )
        if yr_of_comp_196069_small_medium_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_196069_Small_Medium_Stock_Pct"] = (
                yr_of_comp_196069_small_medium_stock_pct
            )
        if yr_of_comp_196069_small_medium_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_196069_Small_Medium_Stock_Pct_TC"] = (
                yr_of_comp_196069_small_medium_stock_pct_tc
            )
        if yr_of_comp_197079_small_medium_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_197079_Small_Medium_Stock_Pct"] = (
                yr_of_comp_197079_small_medium_stock_pct
            )
        if yr_of_comp_197079_small_medium_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_197079_Small_Medium_Stock_Pct_TC"] = (
                yr_of_comp_197079_small_medium_stock_pct_tc
            )
        if yr_of_comp_198089_small_medium_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_198089_Small_Medium_Stock_Pct"] = (
                yr_of_comp_198089_small_medium_stock_pct
            )
        if yr_of_comp_198089_small_medium_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_198089_Small_Medium_Stock_Pct_TC"] = (
                yr_of_comp_198089_small_medium_stock_pct_tc
            )
        if yr_of_comp_199099_small_medium_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_199099_Small_Medium_Stock_Pct"] = (
                yr_of_comp_199099_small_medium_stock_pct
            )
        if yr_of_comp_199099_small_medium_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_199099_Small_Medium_Stock_Pct_TC"] = (
                yr_of_comp_199099_small_medium_stock_pct_tc
            )
        if yr_of_comp_200009_small_medium_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_200009_Small_Medium_Stock_Pct"] = (
                yr_of_comp_200009_small_medium_stock_pct
            )
        if yr_of_comp_200009_small_medium_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_200009_Small_Medium_Stock_Pct_TC"] = (
                yr_of_comp_200009_small_medium_stock_pct_tc
            )
        if yr_of_comp_post_2009_small_medium_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_Post2009_Small_Medium_Stock_Pct"] = (
                yr_of_comp_post_2009_small_medium_stock_pct
            )
        if yr_of_comp_post_2009_small_medium_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_Post2009_Small_Medium_Stock_Pct_TC"] = (
                yr_of_comp_post_2009_small_medium_stock_pct_tc
            )
        if stock_no_of_unit_small_medium is not UNSET:
            field_dict["Stock_No_of_Unit_Small_Medium"] = stock_no_of_unit_small_medium
        if stock_no_of_unit_small_medium_tc is not UNSET:
            field_dict["Stock_No_of_Unit_Small_Medium_TC"] = (
                stock_no_of_unit_small_medium_tc
            )
        if yr_of_comp_pre_1960_large_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_Pre1960_Large_Stock_Pct"] = (
                yr_of_comp_pre_1960_large_stock_pct
            )
        if yr_of_comp_pre_1960_large_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_Pre1960_Large_Stock_Pct_TC"] = (
                yr_of_comp_pre_1960_large_stock_pct_tc
            )
        if yr_of_comp_196069_large_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_196069_Large_Stock_Pct"] = (
                yr_of_comp_196069_large_stock_pct
            )
        if yr_of_comp_196069_large_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_196069_Large_Stock_Pct_TC"] = (
                yr_of_comp_196069_large_stock_pct_tc
            )
        if yr_of_comp_197079_large_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_197079_Large_Stock_Pct"] = (
                yr_of_comp_197079_large_stock_pct
            )
        if yr_of_comp_197079_large_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_197079_Large_Stock_Pct_TC"] = (
                yr_of_comp_197079_large_stock_pct_tc
            )
        if yr_of_comp_198089_large_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_198089_Large_Stock_Pct"] = (
                yr_of_comp_198089_large_stock_pct
            )
        if yr_of_comp_198089_large_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_198089_Large_Stock_Pct_TC"] = (
                yr_of_comp_198089_large_stock_pct_tc
            )
        if yr_of_comp_199099_large_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_199099_Large_Stock_Pct"] = (
                yr_of_comp_199099_large_stock_pct
            )
        if yr_of_comp_199099_large_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_199099_Large_Stock_Pct_TC"] = (
                yr_of_comp_199099_large_stock_pct_tc
            )
        if yr_of_comp_200009_large_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_200009_Large_Stock_Pct"] = (
                yr_of_comp_200009_large_stock_pct
            )
        if yr_of_comp_200009_large_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_200009_Large_Stock_Pct_TC"] = (
                yr_of_comp_200009_large_stock_pct_tc
            )
        if yr_of_comp_post_2009_large_stock_pct is not UNSET:
            field_dict["Yr_of_Comp_Post2009_Large_Stock_Pct"] = (
                yr_of_comp_post_2009_large_stock_pct
            )
        if yr_of_comp_post_2009_large_stock_pct_tc is not UNSET:
            field_dict["Yr_of_Comp_Post2009_Large_Stock_Pct_TC"] = (
                yr_of_comp_post_2009_large_stock_pct_tc
            )
        if stock_no_of_unit_large is not UNSET:
            field_dict["Stock_No_of_Unit_Large"] = stock_no_of_unit_large
        if stock_no_of_unit_large_tc is not UNSET:
            field_dict["Stock_No_of_Unit_Large_TC"] = stock_no_of_unit_large_tc
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

        def _parse_year_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_end = _parse_year_end(d.pop("Year_End", UNSET))

        def _parse_year_end_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        year_end_tc = _parse_year_end_tc(d.pop("Year_End_TC", UNSET))

        def _parse_yr_of_comp_pre_1960_overall_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_pre_1960_overall_stock_pct = (
            _parse_yr_of_comp_pre_1960_overall_stock_pct(
                d.pop("Yr_of_Comp_Pre1960_Overall_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_pre_1960_overall_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_pre_1960_overall_stock_pct_tc = (
            _parse_yr_of_comp_pre_1960_overall_stock_pct_tc(
                d.pop("Yr_of_Comp_Pre1960_Overall_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_196069_overall_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_196069_overall_stock_pct = (
            _parse_yr_of_comp_196069_overall_stock_pct(
                d.pop("Yr_of_Comp_196069_Overall_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_196069_overall_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_196069_overall_stock_pct_tc = (
            _parse_yr_of_comp_196069_overall_stock_pct_tc(
                d.pop("Yr_of_Comp_196069_Overall_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_197079_overall_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_197079_overall_stock_pct = (
            _parse_yr_of_comp_197079_overall_stock_pct(
                d.pop("Yr_of_Comp_197079_Overall_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_197079_overall_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_197079_overall_stock_pct_tc = (
            _parse_yr_of_comp_197079_overall_stock_pct_tc(
                d.pop("Yr_of_Comp_197079_Overall_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_198089_overall_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_198089_overall_stock_pct = (
            _parse_yr_of_comp_198089_overall_stock_pct(
                d.pop("Yr_of_Comp_198089_Overall_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_198089_overall_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_198089_overall_stock_pct_tc = (
            _parse_yr_of_comp_198089_overall_stock_pct_tc(
                d.pop("Yr_of_Comp_198089_Overall_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_199099_overall_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_199099_overall_stock_pct = (
            _parse_yr_of_comp_199099_overall_stock_pct(
                d.pop("Yr_of_Comp_199099_Overall_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_199099_overall_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_199099_overall_stock_pct_tc = (
            _parse_yr_of_comp_199099_overall_stock_pct_tc(
                d.pop("Yr_of_Comp_199099_Overall_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_200009_overall_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_200009_overall_stock_pct = (
            _parse_yr_of_comp_200009_overall_stock_pct(
                d.pop("Yr_of_Comp_200009_Overall_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_200009_overall_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_200009_overall_stock_pct_tc = (
            _parse_yr_of_comp_200009_overall_stock_pct_tc(
                d.pop("Yr_of_Comp_200009_Overall_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_post_2009_overall_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_post_2009_overall_stock_pct = (
            _parse_yr_of_comp_post_2009_overall_stock_pct(
                d.pop("Yr_of_Comp_Post2009_Overall_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_post_2009_overall_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_post_2009_overall_stock_pct_tc = (
            _parse_yr_of_comp_post_2009_overall_stock_pct_tc(
                d.pop("Yr_of_Comp_Post2009_Overall_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_stock_no_of_unit_overall(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_no_of_unit_overall = _parse_stock_no_of_unit_overall(
            d.pop("Stock_No_of_Unit_Overall", UNSET)
        )

        def _parse_stock_no_of_unit_overall_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_no_of_unit_overall_tc = _parse_stock_no_of_unit_overall_tc(
            d.pop("Stock_No_of_Unit_Overall_TC", UNSET)
        )

        def _parse_yr_of_comp_pre_1960_small_medium_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_pre_1960_small_medium_stock_pct = (
            _parse_yr_of_comp_pre_1960_small_medium_stock_pct(
                d.pop("Yr_of_Comp_Pre1960_Small_Medium_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_pre_1960_small_medium_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_pre_1960_small_medium_stock_pct_tc = (
            _parse_yr_of_comp_pre_1960_small_medium_stock_pct_tc(
                d.pop("Yr_of_Comp_Pre1960_Small_Medium_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_196069_small_medium_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_196069_small_medium_stock_pct = (
            _parse_yr_of_comp_196069_small_medium_stock_pct(
                d.pop("Yr_of_Comp_196069_Small_Medium_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_196069_small_medium_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_196069_small_medium_stock_pct_tc = (
            _parse_yr_of_comp_196069_small_medium_stock_pct_tc(
                d.pop("Yr_of_Comp_196069_Small_Medium_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_197079_small_medium_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_197079_small_medium_stock_pct = (
            _parse_yr_of_comp_197079_small_medium_stock_pct(
                d.pop("Yr_of_Comp_197079_Small_Medium_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_197079_small_medium_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_197079_small_medium_stock_pct_tc = (
            _parse_yr_of_comp_197079_small_medium_stock_pct_tc(
                d.pop("Yr_of_Comp_197079_Small_Medium_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_198089_small_medium_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_198089_small_medium_stock_pct = (
            _parse_yr_of_comp_198089_small_medium_stock_pct(
                d.pop("Yr_of_Comp_198089_Small_Medium_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_198089_small_medium_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_198089_small_medium_stock_pct_tc = (
            _parse_yr_of_comp_198089_small_medium_stock_pct_tc(
                d.pop("Yr_of_Comp_198089_Small_Medium_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_199099_small_medium_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_199099_small_medium_stock_pct = (
            _parse_yr_of_comp_199099_small_medium_stock_pct(
                d.pop("Yr_of_Comp_199099_Small_Medium_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_199099_small_medium_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_199099_small_medium_stock_pct_tc = (
            _parse_yr_of_comp_199099_small_medium_stock_pct_tc(
                d.pop("Yr_of_Comp_199099_Small_Medium_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_200009_small_medium_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_200009_small_medium_stock_pct = (
            _parse_yr_of_comp_200009_small_medium_stock_pct(
                d.pop("Yr_of_Comp_200009_Small_Medium_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_200009_small_medium_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_200009_small_medium_stock_pct_tc = (
            _parse_yr_of_comp_200009_small_medium_stock_pct_tc(
                d.pop("Yr_of_Comp_200009_Small_Medium_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_post_2009_small_medium_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_post_2009_small_medium_stock_pct = (
            _parse_yr_of_comp_post_2009_small_medium_stock_pct(
                d.pop("Yr_of_Comp_Post2009_Small_Medium_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_post_2009_small_medium_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_post_2009_small_medium_stock_pct_tc = (
            _parse_yr_of_comp_post_2009_small_medium_stock_pct_tc(
                d.pop("Yr_of_Comp_Post2009_Small_Medium_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_stock_no_of_unit_small_medium(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_no_of_unit_small_medium = _parse_stock_no_of_unit_small_medium(
            d.pop("Stock_No_of_Unit_Small_Medium", UNSET)
        )

        def _parse_stock_no_of_unit_small_medium_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_no_of_unit_small_medium_tc = _parse_stock_no_of_unit_small_medium_tc(
            d.pop("Stock_No_of_Unit_Small_Medium_TC", UNSET)
        )

        def _parse_yr_of_comp_pre_1960_large_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_pre_1960_large_stock_pct = (
            _parse_yr_of_comp_pre_1960_large_stock_pct(
                d.pop("Yr_of_Comp_Pre1960_Large_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_pre_1960_large_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_pre_1960_large_stock_pct_tc = (
            _parse_yr_of_comp_pre_1960_large_stock_pct_tc(
                d.pop("Yr_of_Comp_Pre1960_Large_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_196069_large_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_196069_large_stock_pct = _parse_yr_of_comp_196069_large_stock_pct(
            d.pop("Yr_of_Comp_196069_Large_Stock_Pct", UNSET)
        )

        def _parse_yr_of_comp_196069_large_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_196069_large_stock_pct_tc = (
            _parse_yr_of_comp_196069_large_stock_pct_tc(
                d.pop("Yr_of_Comp_196069_Large_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_197079_large_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_197079_large_stock_pct = _parse_yr_of_comp_197079_large_stock_pct(
            d.pop("Yr_of_Comp_197079_Large_Stock_Pct", UNSET)
        )

        def _parse_yr_of_comp_197079_large_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_197079_large_stock_pct_tc = (
            _parse_yr_of_comp_197079_large_stock_pct_tc(
                d.pop("Yr_of_Comp_197079_Large_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_198089_large_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_198089_large_stock_pct = _parse_yr_of_comp_198089_large_stock_pct(
            d.pop("Yr_of_Comp_198089_Large_Stock_Pct", UNSET)
        )

        def _parse_yr_of_comp_198089_large_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_198089_large_stock_pct_tc = (
            _parse_yr_of_comp_198089_large_stock_pct_tc(
                d.pop("Yr_of_Comp_198089_Large_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_199099_large_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_199099_large_stock_pct = _parse_yr_of_comp_199099_large_stock_pct(
            d.pop("Yr_of_Comp_199099_Large_Stock_Pct", UNSET)
        )

        def _parse_yr_of_comp_199099_large_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_199099_large_stock_pct_tc = (
            _parse_yr_of_comp_199099_large_stock_pct_tc(
                d.pop("Yr_of_Comp_199099_Large_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_200009_large_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_200009_large_stock_pct = _parse_yr_of_comp_200009_large_stock_pct(
            d.pop("Yr_of_Comp_200009_Large_Stock_Pct", UNSET)
        )

        def _parse_yr_of_comp_200009_large_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_200009_large_stock_pct_tc = (
            _parse_yr_of_comp_200009_large_stock_pct_tc(
                d.pop("Yr_of_Comp_200009_Large_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_yr_of_comp_post_2009_large_stock_pct(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_post_2009_large_stock_pct = (
            _parse_yr_of_comp_post_2009_large_stock_pct(
                d.pop("Yr_of_Comp_Post2009_Large_Stock_Pct", UNSET)
            )
        )

        def _parse_yr_of_comp_post_2009_large_stock_pct_tc(
            data: object,
        ) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        yr_of_comp_post_2009_large_stock_pct_tc = (
            _parse_yr_of_comp_post_2009_large_stock_pct_tc(
                d.pop("Yr_of_Comp_Post2009_Large_Stock_Pct_TC", UNSET)
            )
        )

        def _parse_stock_no_of_unit_large(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_no_of_unit_large = _parse_stock_no_of_unit_large(
            d.pop("Stock_No_of_Unit_Large", UNSET)
        )

        def _parse_stock_no_of_unit_large_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stock_no_of_unit_large_tc = _parse_stock_no_of_unit_large_tc(
            d.pop("Stock_No_of_Unit_Large_TC", UNSET)
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

        shape_length = _parse_shape_length(d.pop("SHAPE_Length", UNSET))

        def _parse_shape_area(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shape_area = _parse_shape_area(d.pop("SHAPE_Area", UNSET))

        wfs_map_server_wfs_rvd027_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset=dataset,
            dataset_tc=dataset_tc,
            region=region,
            region_tc=region_tc,
            year_end=year_end,
            year_end_tc=year_end_tc,
            yr_of_comp_pre_1960_overall_stock_pct=yr_of_comp_pre_1960_overall_stock_pct,
            yr_of_comp_pre_1960_overall_stock_pct_tc=yr_of_comp_pre_1960_overall_stock_pct_tc,
            yr_of_comp_196069_overall_stock_pct=yr_of_comp_196069_overall_stock_pct,
            yr_of_comp_196069_overall_stock_pct_tc=yr_of_comp_196069_overall_stock_pct_tc,
            yr_of_comp_197079_overall_stock_pct=yr_of_comp_197079_overall_stock_pct,
            yr_of_comp_197079_overall_stock_pct_tc=yr_of_comp_197079_overall_stock_pct_tc,
            yr_of_comp_198089_overall_stock_pct=yr_of_comp_198089_overall_stock_pct,
            yr_of_comp_198089_overall_stock_pct_tc=yr_of_comp_198089_overall_stock_pct_tc,
            yr_of_comp_199099_overall_stock_pct=yr_of_comp_199099_overall_stock_pct,
            yr_of_comp_199099_overall_stock_pct_tc=yr_of_comp_199099_overall_stock_pct_tc,
            yr_of_comp_200009_overall_stock_pct=yr_of_comp_200009_overall_stock_pct,
            yr_of_comp_200009_overall_stock_pct_tc=yr_of_comp_200009_overall_stock_pct_tc,
            yr_of_comp_post_2009_overall_stock_pct=yr_of_comp_post_2009_overall_stock_pct,
            yr_of_comp_post_2009_overall_stock_pct_tc=yr_of_comp_post_2009_overall_stock_pct_tc,
            stock_no_of_unit_overall=stock_no_of_unit_overall,
            stock_no_of_unit_overall_tc=stock_no_of_unit_overall_tc,
            yr_of_comp_pre_1960_small_medium_stock_pct=yr_of_comp_pre_1960_small_medium_stock_pct,
            yr_of_comp_pre_1960_small_medium_stock_pct_tc=yr_of_comp_pre_1960_small_medium_stock_pct_tc,
            yr_of_comp_196069_small_medium_stock_pct=yr_of_comp_196069_small_medium_stock_pct,
            yr_of_comp_196069_small_medium_stock_pct_tc=yr_of_comp_196069_small_medium_stock_pct_tc,
            yr_of_comp_197079_small_medium_stock_pct=yr_of_comp_197079_small_medium_stock_pct,
            yr_of_comp_197079_small_medium_stock_pct_tc=yr_of_comp_197079_small_medium_stock_pct_tc,
            yr_of_comp_198089_small_medium_stock_pct=yr_of_comp_198089_small_medium_stock_pct,
            yr_of_comp_198089_small_medium_stock_pct_tc=yr_of_comp_198089_small_medium_stock_pct_tc,
            yr_of_comp_199099_small_medium_stock_pct=yr_of_comp_199099_small_medium_stock_pct,
            yr_of_comp_199099_small_medium_stock_pct_tc=yr_of_comp_199099_small_medium_stock_pct_tc,
            yr_of_comp_200009_small_medium_stock_pct=yr_of_comp_200009_small_medium_stock_pct,
            yr_of_comp_200009_small_medium_stock_pct_tc=yr_of_comp_200009_small_medium_stock_pct_tc,
            yr_of_comp_post_2009_small_medium_stock_pct=yr_of_comp_post_2009_small_medium_stock_pct,
            yr_of_comp_post_2009_small_medium_stock_pct_tc=yr_of_comp_post_2009_small_medium_stock_pct_tc,
            stock_no_of_unit_small_medium=stock_no_of_unit_small_medium,
            stock_no_of_unit_small_medium_tc=stock_no_of_unit_small_medium_tc,
            yr_of_comp_pre_1960_large_stock_pct=yr_of_comp_pre_1960_large_stock_pct,
            yr_of_comp_pre_1960_large_stock_pct_tc=yr_of_comp_pre_1960_large_stock_pct_tc,
            yr_of_comp_196069_large_stock_pct=yr_of_comp_196069_large_stock_pct,
            yr_of_comp_196069_large_stock_pct_tc=yr_of_comp_196069_large_stock_pct_tc,
            yr_of_comp_197079_large_stock_pct=yr_of_comp_197079_large_stock_pct,
            yr_of_comp_197079_large_stock_pct_tc=yr_of_comp_197079_large_stock_pct_tc,
            yr_of_comp_198089_large_stock_pct=yr_of_comp_198089_large_stock_pct,
            yr_of_comp_198089_large_stock_pct_tc=yr_of_comp_198089_large_stock_pct_tc,
            yr_of_comp_199099_large_stock_pct=yr_of_comp_199099_large_stock_pct,
            yr_of_comp_199099_large_stock_pct_tc=yr_of_comp_199099_large_stock_pct_tc,
            yr_of_comp_200009_large_stock_pct=yr_of_comp_200009_large_stock_pct,
            yr_of_comp_200009_large_stock_pct_tc=yr_of_comp_200009_large_stock_pct_tc,
            yr_of_comp_post_2009_large_stock_pct=yr_of_comp_post_2009_large_stock_pct,
            yr_of_comp_post_2009_large_stock_pct_tc=yr_of_comp_post_2009_large_stock_pct_tc,
            stock_no_of_unit_large=stock_no_of_unit_large,
            stock_no_of_unit_large_tc=stock_no_of_unit_large_tc,
            last_update=last_update,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_rvd027_attributes.additional_properties = d
        return wfs_map_server_wfs_rvd027_attributes

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
