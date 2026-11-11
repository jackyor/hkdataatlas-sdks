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
        lpmworks_slope_num (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_location (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_c_location (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_d_board2 (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_d_cboard (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_contract (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_new (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_c_new (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_date_start_e (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_date_start_c (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_date_comp_e (None | str | Unset): Publisher field type: esriFieldTypeString
        lpmworks_date_comp_c (None | str | Unset): Publisher field type: esriFieldTypeString
        shape_length (float | None | Unset): Publisher field type: esriFieldTypeDouble
        shape_area (float | None | Unset): Publisher field type: esriFieldTypeDouble
    """

    objectid: int | Unset = UNSET
    lpmworks_slope_num: None | str | Unset = UNSET
    lpmworks_location: None | str | Unset = UNSET
    lpmworks_c_location: None | str | Unset = UNSET
    lpmworks_d_board2: None | str | Unset = UNSET
    lpmworks_d_cboard: None | str | Unset = UNSET
    lpmworks_contract: None | str | Unset = UNSET
    lpmworks_new: None | str | Unset = UNSET
    lpmworks_c_new: None | str | Unset = UNSET
    lpmworks_date_start_e: None | str | Unset = UNSET
    lpmworks_date_start_c: None | str | Unset = UNSET
    lpmworks_date_comp_e: None | str | Unset = UNSET
    lpmworks_date_comp_c: None | str | Unset = UNSET
    shape_length: float | None | Unset = UNSET
    shape_area: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        objectid = self.objectid

        lpmworks_slope_num: None | str | Unset
        if isinstance(self.lpmworks_slope_num, Unset):
            lpmworks_slope_num = UNSET
        else:
            lpmworks_slope_num = self.lpmworks_slope_num

        lpmworks_location: None | str | Unset
        if isinstance(self.lpmworks_location, Unset):
            lpmworks_location = UNSET
        else:
            lpmworks_location = self.lpmworks_location

        lpmworks_c_location: None | str | Unset
        if isinstance(self.lpmworks_c_location, Unset):
            lpmworks_c_location = UNSET
        else:
            lpmworks_c_location = self.lpmworks_c_location

        lpmworks_d_board2: None | str | Unset
        if isinstance(self.lpmworks_d_board2, Unset):
            lpmworks_d_board2 = UNSET
        else:
            lpmworks_d_board2 = self.lpmworks_d_board2

        lpmworks_d_cboard: None | str | Unset
        if isinstance(self.lpmworks_d_cboard, Unset):
            lpmworks_d_cboard = UNSET
        else:
            lpmworks_d_cboard = self.lpmworks_d_cboard

        lpmworks_contract: None | str | Unset
        if isinstance(self.lpmworks_contract, Unset):
            lpmworks_contract = UNSET
        else:
            lpmworks_contract = self.lpmworks_contract

        lpmworks_new: None | str | Unset
        if isinstance(self.lpmworks_new, Unset):
            lpmworks_new = UNSET
        else:
            lpmworks_new = self.lpmworks_new

        lpmworks_c_new: None | str | Unset
        if isinstance(self.lpmworks_c_new, Unset):
            lpmworks_c_new = UNSET
        else:
            lpmworks_c_new = self.lpmworks_c_new

        lpmworks_date_start_e: None | str | Unset
        if isinstance(self.lpmworks_date_start_e, Unset):
            lpmworks_date_start_e = UNSET
        else:
            lpmworks_date_start_e = self.lpmworks_date_start_e

        lpmworks_date_start_c: None | str | Unset
        if isinstance(self.lpmworks_date_start_c, Unset):
            lpmworks_date_start_c = UNSET
        else:
            lpmworks_date_start_c = self.lpmworks_date_start_c

        lpmworks_date_comp_e: None | str | Unset
        if isinstance(self.lpmworks_date_comp_e, Unset):
            lpmworks_date_comp_e = UNSET
        else:
            lpmworks_date_comp_e = self.lpmworks_date_comp_e

        lpmworks_date_comp_c: None | str | Unset
        if isinstance(self.lpmworks_date_comp_c, Unset):
            lpmworks_date_comp_c = UNSET
        else:
            lpmworks_date_comp_c = self.lpmworks_date_comp_c

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
        if lpmworks_slope_num is not UNSET:
            field_dict["LPMWORKS_SLOPE_NUM"] = lpmworks_slope_num
        if lpmworks_location is not UNSET:
            field_dict["LPMWORKS_LOCATION"] = lpmworks_location
        if lpmworks_c_location is not UNSET:
            field_dict["LPMWORKS_C_LOCATION"] = lpmworks_c_location
        if lpmworks_d_board2 is not UNSET:
            field_dict["LPMWORKS_D_BOARD2"] = lpmworks_d_board2
        if lpmworks_d_cboard is not UNSET:
            field_dict["LPMWORKS_D_CBOARD"] = lpmworks_d_cboard
        if lpmworks_contract is not UNSET:
            field_dict["LPMWORKS_CONTRACT"] = lpmworks_contract
        if lpmworks_new is not UNSET:
            field_dict["LPMWORKS_NEW"] = lpmworks_new
        if lpmworks_c_new is not UNSET:
            field_dict["LPMWORKS_C_NEW"] = lpmworks_c_new
        if lpmworks_date_start_e is not UNSET:
            field_dict["LPMWORKS_DATE_START_E"] = lpmworks_date_start_e
        if lpmworks_date_start_c is not UNSET:
            field_dict["LPMWORKS_DATE_START_C"] = lpmworks_date_start_c
        if lpmworks_date_comp_e is not UNSET:
            field_dict["LPMWORKS_DATE_COMP_E"] = lpmworks_date_comp_e
        if lpmworks_date_comp_c is not UNSET:
            field_dict["LPMWORKS_DATE_COMP_C"] = lpmworks_date_comp_c
        if shape_length is not UNSET:
            field_dict["Shape__Length"] = shape_length
        if shape_area is not UNSET:
            field_dict["Shape__Area"] = shape_area

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        objectid = d.pop("OBJECTID", UNSET)

        def _parse_lpmworks_slope_num(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_slope_num = _parse_lpmworks_slope_num(
            d.pop("LPMWORKS_SLOPE_NUM", UNSET)
        )

        def _parse_lpmworks_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_location = _parse_lpmworks_location(d.pop("LPMWORKS_LOCATION", UNSET))

        def _parse_lpmworks_c_location(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_c_location = _parse_lpmworks_c_location(
            d.pop("LPMWORKS_C_LOCATION", UNSET)
        )

        def _parse_lpmworks_d_board2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_d_board2 = _parse_lpmworks_d_board2(d.pop("LPMWORKS_D_BOARD2", UNSET))

        def _parse_lpmworks_d_cboard(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_d_cboard = _parse_lpmworks_d_cboard(d.pop("LPMWORKS_D_CBOARD", UNSET))

        def _parse_lpmworks_contract(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_contract = _parse_lpmworks_contract(d.pop("LPMWORKS_CONTRACT", UNSET))

        def _parse_lpmworks_new(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_new = _parse_lpmworks_new(d.pop("LPMWORKS_NEW", UNSET))

        def _parse_lpmworks_c_new(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_c_new = _parse_lpmworks_c_new(d.pop("LPMWORKS_C_NEW", UNSET))

        def _parse_lpmworks_date_start_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_date_start_e = _parse_lpmworks_date_start_e(
            d.pop("LPMWORKS_DATE_START_E", UNSET)
        )

        def _parse_lpmworks_date_start_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_date_start_c = _parse_lpmworks_date_start_c(
            d.pop("LPMWORKS_DATE_START_C", UNSET)
        )

        def _parse_lpmworks_date_comp_e(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_date_comp_e = _parse_lpmworks_date_comp_e(
            d.pop("LPMWORKS_DATE_COMP_E", UNSET)
        )

        def _parse_lpmworks_date_comp_c(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        lpmworks_date_comp_c = _parse_lpmworks_date_comp_c(
            d.pop("LPMWORKS_DATE_COMP_C", UNSET)
        )

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
            lpmworks_slope_num=lpmworks_slope_num,
            lpmworks_location=lpmworks_location,
            lpmworks_c_location=lpmworks_c_location,
            lpmworks_d_board2=lpmworks_d_board2,
            lpmworks_d_cboard=lpmworks_d_cboard,
            lpmworks_contract=lpmworks_contract,
            lpmworks_new=lpmworks_new,
            lpmworks_c_new=lpmworks_c_new,
            lpmworks_date_start_e=lpmworks_date_start_e,
            lpmworks_date_start_c=lpmworks_date_start_c,
            lpmworks_date_comp_e=lpmworks_date_comp_e,
            lpmworks_date_comp_c=lpmworks_date_comp_c,
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
