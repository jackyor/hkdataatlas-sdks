from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WfsMapServerWfsRVD006Attributes")


@_attrs_define
class WfsMapServerWfsRVD006Attributes:
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
        not_exceeding_min_rv_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        not_exceeding_min_rv_number_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        above_min_rv_number (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        above_min_rv_number_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML occurrence
            into all JSON queries.
        above_min_rv_hkd_in_thousand (None | str | Unset): Native XSD type . Requiredness is not projected from XML
            occurrence into all JSON queries.
        above_min_rv_hkd_in_thousand_tc (None | str | Unset): Native XSD type . Requiredness is not projected from XML
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
    district: None | str | Unset = UNSET
    district_tc: None | str | Unset = UNSET
    not_exceeding_min_rv_number: None | str | Unset = UNSET
    not_exceeding_min_rv_number_tc: None | str | Unset = UNSET
    above_min_rv_number: None | str | Unset = UNSET
    above_min_rv_number_tc: None | str | Unset = UNSET
    above_min_rv_hkd_in_thousand: None | str | Unset = UNSET
    above_min_rv_hkd_in_thousand_tc: None | str | Unset = UNSET
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

        not_exceeding_min_rv_number: None | str | Unset
        if isinstance(self.not_exceeding_min_rv_number, Unset):
            not_exceeding_min_rv_number = UNSET
        else:
            not_exceeding_min_rv_number = self.not_exceeding_min_rv_number

        not_exceeding_min_rv_number_tc: None | str | Unset
        if isinstance(self.not_exceeding_min_rv_number_tc, Unset):
            not_exceeding_min_rv_number_tc = UNSET
        else:
            not_exceeding_min_rv_number_tc = self.not_exceeding_min_rv_number_tc

        above_min_rv_number: None | str | Unset
        if isinstance(self.above_min_rv_number, Unset):
            above_min_rv_number = UNSET
        else:
            above_min_rv_number = self.above_min_rv_number

        above_min_rv_number_tc: None | str | Unset
        if isinstance(self.above_min_rv_number_tc, Unset):
            above_min_rv_number_tc = UNSET
        else:
            above_min_rv_number_tc = self.above_min_rv_number_tc

        above_min_rv_hkd_in_thousand: None | str | Unset
        if isinstance(self.above_min_rv_hkd_in_thousand, Unset):
            above_min_rv_hkd_in_thousand = UNSET
        else:
            above_min_rv_hkd_in_thousand = self.above_min_rv_hkd_in_thousand

        above_min_rv_hkd_in_thousand_tc: None | str | Unset
        if isinstance(self.above_min_rv_hkd_in_thousand_tc, Unset):
            above_min_rv_hkd_in_thousand_tc = UNSET
        else:
            above_min_rv_hkd_in_thousand_tc = self.above_min_rv_hkd_in_thousand_tc

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
        if not_exceeding_min_rv_number is not UNSET:
            field_dict["Not_Exceeding_Min_RV_Number"] = not_exceeding_min_rv_number
        if not_exceeding_min_rv_number_tc is not UNSET:
            field_dict["Not_Exceeding_Min_RV_Number_TC"] = (
                not_exceeding_min_rv_number_tc
            )
        if above_min_rv_number is not UNSET:
            field_dict["Above_Min_RV_Number"] = above_min_rv_number
        if above_min_rv_number_tc is not UNSET:
            field_dict["Above_Min_RV_Number_TC"] = above_min_rv_number_tc
        if above_min_rv_hkd_in_thousand is not UNSET:
            field_dict["Above_Min_RV_HKD_In_Thousand"] = above_min_rv_hkd_in_thousand
        if above_min_rv_hkd_in_thousand_tc is not UNSET:
            field_dict["Above_Min_RV_HKD_In_Thousand_TC"] = (
                above_min_rv_hkd_in_thousand_tc
            )
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

        def _parse_not_exceeding_min_rv_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        not_exceeding_min_rv_number = _parse_not_exceeding_min_rv_number(
            d.pop("Not_Exceeding_Min_RV_Number", UNSET)
        )

        def _parse_not_exceeding_min_rv_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        not_exceeding_min_rv_number_tc = _parse_not_exceeding_min_rv_number_tc(
            d.pop("Not_Exceeding_Min_RV_Number_TC", UNSET)
        )

        def _parse_above_min_rv_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        above_min_rv_number = _parse_above_min_rv_number(
            d.pop("Above_Min_RV_Number", UNSET)
        )

        def _parse_above_min_rv_number_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        above_min_rv_number_tc = _parse_above_min_rv_number_tc(
            d.pop("Above_Min_RV_Number_TC", UNSET)
        )

        def _parse_above_min_rv_hkd_in_thousand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        above_min_rv_hkd_in_thousand = _parse_above_min_rv_hkd_in_thousand(
            d.pop("Above_Min_RV_HKD_In_Thousand", UNSET)
        )

        def _parse_above_min_rv_hkd_in_thousand_tc(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        above_min_rv_hkd_in_thousand_tc = _parse_above_min_rv_hkd_in_thousand_tc(
            d.pop("Above_Min_RV_HKD_In_Thousand_TC", UNSET)
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

        wfs_map_server_wfs_rvd006_attributes = cls(
            shape=shape,
            objectid=objectid,
            dataset=dataset,
            dataset_tc=dataset_tc,
            district=district,
            district_tc=district_tc,
            not_exceeding_min_rv_number=not_exceeding_min_rv_number,
            not_exceeding_min_rv_number_tc=not_exceeding_min_rv_number_tc,
            above_min_rv_number=above_min_rv_number,
            above_min_rv_number_tc=above_min_rv_number_tc,
            above_min_rv_hkd_in_thousand=above_min_rv_hkd_in_thousand,
            above_min_rv_hkd_in_thousand_tc=above_min_rv_hkd_in_thousand_tc,
            last_update=last_update,
            shape_length=shape_length,
            shape_area=shape_area,
        )

        wfs_map_server_wfs_rvd006_attributes.additional_properties = d
        return wfs_map_server_wfs_rvd006_attributes

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
